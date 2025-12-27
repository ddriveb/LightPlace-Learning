cmake_minimum_required(VERSION 3.12)

# 收集move_boundary操作源文件
set(MOVE_BOUNDARY_SOURCES
    src\move_boundary.cpp
    src\move_boundary_cuda.cpp
)

if(CUDA_FOUND)
    list(APPEND MOVE_BOUNDARY_SOURCES
        src\move_boundary_cuda_kernel.cu
    )
endif()

# 创建Python绑定
pybind11_add_module(move_boundary_cpp SHARED ${MOVE_BOUNDARY_SOURCES})

# 链接库
target_link_libraries(move_boundary_cpp PRIVATE 
    torch
    ${Boost_LIBRARIES}
)

# 设置编译属性
set_target_properties(move_boundary_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(move_boundary_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(move_boundary_cpp PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(move_boundary_cpp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 如果有CUDA，创建CUDA版本
if(CUDA_FOUND)
    pybind11_add_module(move_boundary_cuda SHARED
    )
    target_link_libraries(move_boundary_cuda PRIVATE torch ${Boost_LIBRARIES})
    set_target_properties(move_boundary_cuda PROPERTIES CXX_STANDARD 14 CUDA_SEPARABLE_COMPILATION ON)
    target_include_directories(move_boundary_cuda PRIVATE ${CUDA_INCLUDE_DIRS} ${TORCH_INCLUDE_DIRS})
endif()

# 安装模块
install(TARGETS move_boundary_cpp DESTINATION dreamplace/ops/move_boundary)
if(CUDA_FOUND)
    install(TARGETS move_boundary_cuda DESTINATION dreamplace/ops/move_boundary)
endif()
