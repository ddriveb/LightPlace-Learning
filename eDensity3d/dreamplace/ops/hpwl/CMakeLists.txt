cmake_minimum_required(VERSION 3.12)

# 收集HPWL操作源文件
set(HPWL_SOURCES
    src/hpwl.cpp
    src/hpwl_atomic.cpp
)

if(CUDA_FOUND)
    list(APPEND HPWL_SOURCES
        src/hpwl_cuda.cpp
        src/hpwl_cuda_atomic.cpp
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

# 设置CUDA编译属性
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
    set(HPWL_CUDA_SOURCES
        src/hpwl_cuda.cpp
        src/hpwl_cuda_atomic.cpp
    )
    
    pybind11_add_module(hpwl_cuda SHARED ${HPWL_CUDA_SOURCES})
    target_link_libraries(hpwl_cuda PRIVATE torch ${Boost_LIBRARIES})
    set_target_properties(hpwl_cuda PROPERTIES CXX_STANDARD 14 CUDA_SEPARABLE_COMPILATION ON)
    target_include_directories(hpwl_cuda PRIVATE ${CUDA_INCLUDE_DIRS} ${TORCH_INCLUDE_DIRS})
    
    pybind11_add_module(hpwl_cuda_atomic SHARED ${HPWL_CUDA_SOURCES})
    target_link_libraries(hpwl_cuda_atomic PRIVATE torch ${Boost_LIBRARIES})
    set_target_properties(hpwl_cuda_atomic PROPERTIES CXX_STANDARD 14 CUDA_SEPARABLE_COMPILATION ON)
    target_include_directories(hpwl_cuda_atomic PRIVATE ${CUDA_INCLUDE_DIRS} ${TORCH_INCLUDE_DIRS})
endif()

# 创建atomic版本
pybind11_add_module(hpwl_cpp_atomic SHARED src/hpwl_atomic.cpp)
target_link_libraries(hpwl_cpp_atomic PRIVATE torch ${Boost_LIBRARIES})
set_target_properties(hpwl_cpp_atomic PROPERTIES CXX_STANDARD 14)
target_include_directories(hpwl_cpp_atomic PRIVATE ${TORCH_INCLUDE_DIRS})

# 安装模块
install(TARGETS hpwl_cpp hpwl_cpp_atomic DESTINATION dreamplace/ops/hpwl)
if(CUDA_FOUND)
    install(TARGETS hpwl_cuda hpwl_cuda_atomic DESTINATION dreamplace/ops/hpwl)
endif()