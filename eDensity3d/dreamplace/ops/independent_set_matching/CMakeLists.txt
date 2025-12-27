cmake_minimum_required(VERSION 3.12)

# 收集independent_set_matching操作源文件
set(INDEPENDENT_SET_MATCHING_SOURCES
    src\independent_set_matching.cpp
    src\independent_set_matching_cuda.cpp
    src\independent_set_matching_sequential.cpp
)

if(CUDA_FOUND)
    list(APPEND INDEPENDENT_SET_MATCHING_SOURCES
        src\hungarian_cuda_kernel.cu
        src\independent_set_matching_cuda_kernel.cu
    )
endif()

# 创建Python绑定
pybind11_add_module(independent_set_matching_cpp SHARED ${INDEPENDENT_SET_MATCHING_SOURCES})

# 链接库
target_link_libraries(independent_set_matching_cpp PRIVATE 
    torch
    ${Boost_LIBRARIES}
)

# 设置编译属性
set_target_properties(independent_set_matching_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(independent_set_matching_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(independent_set_matching_cpp PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(independent_set_matching_cpp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 如果有CUDA，创建CUDA版本
if(CUDA_FOUND)
    pybind11_add_module(independent_set_matching_cuda SHARED
    )
    target_link_libraries(independent_set_matching_cuda PRIVATE torch ${Boost_LIBRARIES})
    set_target_properties(independent_set_matching_cuda PROPERTIES CXX_STANDARD 14 CUDA_SEPARABLE_COMPILATION ON)
    target_include_directories(independent_set_matching_cuda PRIVATE ${CUDA_INCLUDE_DIRS} ${TORCH_INCLUDE_DIRS})
endif()

# 安装模块
install(TARGETS independent_set_matching_cpp DESTINATION dreamplace/ops/independent_set_matching)
if(CUDA_FOUND)
    install(TARGETS independent_set_matching_cuda DESTINATION dreamplace/ops/independent_set_matching)
endif()
