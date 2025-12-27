cmake_minimum_required(VERSION 3.12)

# 收集greedy_legalize操作源文件
set(GREEDY_LEGALIZE_SOURCES
    src\greedy_legalize.cpp
    src\greedy_legalize_cpu.cpp
    src\legalize_bin_cpu.cpp
    src\merge_bin_cpu.cpp
)

# 创建Python绑定
pybind11_add_module(greedy_legalize_cpp SHARED ${GREEDY_LEGALIZE_SOURCES})

# 链接库
target_link_libraries(greedy_legalize_cpp PRIVATE 
    torch
    ${Boost_LIBRARIES}
)

# 设置编译属性
set_target_properties(greedy_legalize_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(greedy_legalize_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(greedy_legalize_cpp PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(greedy_legalize_cpp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 安装模块
install(TARGETS greedy_legalize_cpp DESTINATION dreamplace/ops/greedy_legalize)
if(CUDA_FOUND)
    install(TARGETS greedy_legalize_cuda DESTINATION dreamplace/ops/greedy_legalize)
endif()
