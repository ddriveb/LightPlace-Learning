cmake_minimum_required(VERSION 3.12)

# 收集hpwl操作源文件
set(HPWL_SOURCES
    src\hpwl.cpp
    src\hpwl_atomic.cpp
    src\hpwl_cuda.cpp
    src\hpwl_cuda_atomic.cpp
)

if(CUDA_FOUND)
    list(APPEND HPWL_SOURCES
        src\hpwl_cuda_atomic_kernel.cu
        src\hpwl_cuda_kernel.cu
    )
endif()

# 创建Python绑定
pybind11_add_module(hpwl_cpp SHARED ${HPWL_SOURCES})

# 链接库
target_link_libraries(hpwl_cpp PRIVATE 
    torch
    ${Boost_LIBRARIES}
)

# 设置编译属性
set_target_properties(hpwl_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(hpwl_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(hpwl_cpp PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(hpwl_cpp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 如果有CUDA，创建CUDA版本
if(CUDA_FOUND)
    pybind11_add_module(hpwl_cuda SHARED
    )
    target_link_libraries(hpwl_cuda PRIVATE torch ${Boost_LIBRARIES})
    set_target_properties(hpwl_cuda PROPERTIES CXX_STANDARD 14 CUDA_SEPARABLE_COMPILATION ON)
    target_include_directories(hpwl_cuda PRIVATE ${CUDA_INCLUDE_DIRS} ${TORCH_INCLUDE_DIRS})
endif()

# 安装模块
install(TARGETS hpwl_cpp DESTINATION dreamplace/ops/hpwl)
if(CUDA_FOUND)
    install(TARGETS hpwl_cuda DESTINATION dreamplace/ops/hpwl)
endif()
