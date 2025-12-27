cmake_minimum_required(VERSION 3.12)

# 收集pinrudy操作源文件
set(PINRUDY_SOURCES
    src\pinrudy.cpp
    src\pinrudy_cuda.cpp
)

if(CUDA_FOUND)
    list(APPEND PINRUDY_SOURCES
        src\pinrudy_cuda_kernel.cu
    )
endif()

# 创建Python绑定
pybind11_add_module(pinrudy_cpp SHARED ${PINRUDY_SOURCES})

# 链接库
target_link_libraries(pinrudy_cpp PRIVATE 
    torch
    ${Boost_LIBRARIES}
)

# 设置编译属性
set_target_properties(pinrudy_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(pinrudy_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(pinrudy_cpp PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(pinrudy_cpp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 如果有CUDA，创建CUDA版本
if(CUDA_FOUND)
    pybind11_add_module(pinrudy_cuda SHARED
    )
    target_link_libraries(pinrudy_cuda PRIVATE torch ${Boost_LIBRARIES})
    set_target_properties(pinrudy_cuda PROPERTIES CXX_STANDARD 14 CUDA_SEPARABLE_COMPILATION ON)
    target_include_directories(pinrudy_cuda PRIVATE ${CUDA_INCLUDE_DIRS} ${TORCH_INCLUDE_DIRS})
endif()

# 安装模块
install(TARGETS pinrudy_cpp DESTINATION dreamplace/ops/pinrudy)
if(CUDA_FOUND)
    install(TARGETS pinrudy_cuda DESTINATION dreamplace/ops/pinrudy)
endif()
