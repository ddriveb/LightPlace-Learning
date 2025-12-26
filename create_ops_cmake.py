#!/usr/bin/env python3
"""
为所有ops模块创建CMakeLists.txt文件
"""

import os
import glob

def get_src_files(op_dir):
    """获取操作模块的源文件"""
    src_dir = os.path.join(op_dir, "src")
    if not os.path.exists(src_dir):
        return []
    
    cpp_files = glob.glob(os.path.join(src_dir, "*.cpp"))
    cu_files = glob.glob(os.path.join(src_dir, "*.cu"))
    
    return cpp_files, cu_files

def create_cmake_for_op(op_name, op_dir):
    """为单个操作模块创建CMakeLists.txt"""
    cpp_files, cu_files = get_src_files(op_dir)
    
    if not cpp_files and not cu_files:
        return False  # 没有源文件，不需要CMakeLists.txt
    
    op_name_upper = op_name.upper()
    
    cmake_content = f"""cmake_minimum_required(VERSION 3.12)

# 收集{op_name}操作源文件
set({op_name_upper}_SOURCES
"""

    # 添加CPU源文件
    for cpp_file in cpp_files:
        rel_path = os.path.relpath(cpp_file, op_dir)
        cmake_content += f"    {rel_path}\n"
    
    cmake_content += ")\n\n"
    
    # 添加CUDA条件
    if cu_files:
        cmake_content += "if(CUDA_FOUND)\n    list(APPEND " + f"{op_name_upper}_SOURCES\n"
        for cu_file in cu_files:
            rel_path = os.path.relpath(cu_file, op_dir)
            cmake_content += f"        {rel_path}\n"
        cmake_content += "    )\nendif()\n\n"
    
    # 添加Python绑定
    cmake_content += f"""# 创建Python绑定
pybind11_add_module({op_name}_cpp SHARED ${{{op_name_upper}_SOURCES}})

# 链接库
target_link_libraries({op_name}_cpp PRIVATE 
    torch
    ${{Boost_LIBRARIES}}
)

# 设置编译属性
set_target_properties({op_name}_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties({op_name}_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories({op_name}_cpp PRIVATE ${{CUDA_INCLUDE_DIRS}})
endif()

# 包含目录
target_include_directories({op_name}_cpp PRIVATE
    ${{CMAKE_CURRENT_SOURCE_DIR}}
    ${{CMAKE_CURRENT_SOURCE_DIR}}/utility/src
    ${{TORCH_INCLUDE_DIRS}}
)
"""
    
    # 添加CUDA版本（如果有CUDA文件）
    if cu_files:
        cmake_content += f"""
# 如果有CUDA，创建CUDA版本
if(CUDA_FOUND)
    pybind11_add_module({op_name}_cuda SHARED
"""
        for cu_file in cu_files:
            if not cu_file.endswith('_kernel.cu'):  # 跳过kernel文件，通常包含在其他cpp中
                rel_path = os.path.relpath(cu_file, op_dir)
                cmake_content += f"        {rel_path}\n"
        
        cmake_content += f"""    )
    target_link_libraries({op_name}_cuda PRIVATE torch ${{Boost_LIBRARIES}})
    set_target_properties({op_name}_cuda PROPERTIES CXX_STANDARD 14 CUDA_SEPARABLE_COMPILATION ON)
    target_include_directories({op_name}_cuda PRIVATE ${{CUDA_INCLUDE_DIRS}} ${{TORCH_INCLUDE_DIRS}})
endif()
"""
    
    # 添加安装指令
    cmake_content += f"""
# 安装模块
install(TARGETS {op_name}_cpp DESTINATION dreamplace/ops/{op_name})
if(CUDA_FOUND)
    install(TARGETS {op_name}_cuda DESTINATION dreamplace/ops/{op_name})
endif()
"""
    
    # 写入文件
    cmake_file = os.path.join(op_dir, "CMakeLists.txt")
    with open(cmake_file, 'w') as f:
        f.write(cmake_content)
    
    print(f"Created: {cmake_file}")
    return True

def main():
    """主函数"""
    ops_dir = "eDensity3d/dreamplace/ops"
    
    # 获取所有子目录
    for item in os.listdir(ops_dir):
        op_dir = os.path.join(ops_dir, item)
        if os.path.isdir(op_dir) and item not in ['.', '..', '__pycache__', '.git']:
            create_cmake_for_op(item, op_dir)

if __name__ == "__main__":
    main()