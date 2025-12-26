cmake_minimum_required(VERSION 3.12)

# 收集dct操作源文件
set(DCT_SOURCES
    src\dct.cpp
    src\dct2_fft2.cpp
    src\dct2_fft2_cuda.cpp
    src\dct_2N.cpp
    src\dct_2N_cuda.cpp
    src\dct_cuda.cpp
    src\dct_lee.cpp
    src\dct_lee_cuda.cpp
    src\dst.cpp
    src\dst_cuda.cpp
    src\dxt.cpp
    src\dxt_cuda.cpp
)

if(CUDA_FOUND)
    list(APPEND DCT_SOURCES
        src\dct2_fft2_cuda_kernel.cu
        src\dct_cuda_kernel.cu
        src\dct_lee_cuda_kernel.cu
        src\dst_cuda_kernel.cu
    )
endif()

# 创建Python绑定
pybind11_add_module(dct_cpp SHARED ${DCT_SOURCES})

# 链接库
target_link_libraries(dct_cpp PRIVATE 
    torch
    ${Boost_LIBRARIES}
)

# 设置编译属性
set_target_properties(dct_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(dct_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(dct_cpp PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(dct_cpp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 如果有CUDA，创建CUDA版本
if(CUDA_FOUND)
    pybind11_add_module(dct_cuda SHARED
    )
    target_link_libraries(dct_cuda PRIVATE torch ${Boost_LIBRARIES})
    set_target_properties(dct_cuda PROPERTIES CXX_STANDARD 14 CUDA_SEPARABLE_COMPILATION ON)
    target_include_directories(dct_cuda PRIVATE ${CUDA_INCLUDE_DIRS} ${TORCH_INCLUDE_DIRS})
endif()

# 安装模块
install(TARGETS dct_cpp DESTINATION dreamplace/ops/dct)
if(CUDA_FOUND)
    install(TARGETS dct_cuda DESTINATION dreamplace/ops/dct)
endif()
