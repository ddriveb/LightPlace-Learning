cmake_minimum_required(VERSION 3.12)

# 收集utility操作源文件
set(UTILITY_SOURCES
    src\msg.cpp
)

# 创建Python绑定
pybind11_add_module(utility_cpp SHARED ${UTILITY_SOURCES})

# 链接库
target_link_libraries(utility_cpp PRIVATE 
    torch
    ${Boost_LIBRARIES}
)

# 设置编译属性
set_target_properties(utility_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(utility_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(utility_cpp PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(utility_cpp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 安装模块
install(TARGETS utility_cpp DESTINATION dreamplace/ops/utility)
if(CUDA_FOUND)
    install(TARGETS utility_cuda DESTINATION dreamplace/ops/utility)
endif()
