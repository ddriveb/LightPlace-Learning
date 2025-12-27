cmake_minimum_required(VERSION 3.12)

# 收集legality_check操作源文件
set(LEGALITY_CHECK_SOURCES
    src\legality_check.cpp
)

# 创建Python绑定
pybind11_add_module(legality_check_cpp SHARED ${LEGALITY_CHECK_SOURCES})

# 链接库
target_link_libraries(legality_check_cpp PRIVATE 
    torch
    ${Boost_LIBRARIES}
)

# 设置编译属性
set_target_properties(legality_check_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(legality_check_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(legality_check_cpp PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(legality_check_cpp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 安装模块
install(TARGETS legality_check_cpp DESTINATION dreamplace/ops/legality_check)
if(CUDA_FOUND)
    install(TARGETS legality_check_cuda DESTINATION dreamplace/ops/legality_check)
endif()
