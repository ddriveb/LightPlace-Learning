cmake_minimum_required(VERSION 3.12)

# 收集adjust_node_area操作源文件
set(ADJUST_NODE_AREA_SOURCES
    src\adjust_node_area.cpp
    src\adjust_node_area_cuda.cpp
    src\update_pin_offset.cpp
    src\update_pin_offset_cuda.cpp
)

if(CUDA_FOUND)
    list(APPEND ADJUST_NODE_AREA_SOURCES
        src\adjust_node_area_cuda_kernel.cu
        src\update_pin_offset_cuda_kernel.cu
    )
endif()

# 创建Python绑定
pybind11_add_module(adjust_node_area_cpp SHARED ${ADJUST_NODE_AREA_SOURCES})

# 链接库
target_link_libraries(adjust_node_area_cpp PRIVATE 
    torch
    ${Boost_LIBRARIES}
)

# 设置编译属性
set_target_properties(adjust_node_area_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(adjust_node_area_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(adjust_node_area_cpp PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(adjust_node_area_cpp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 如果有CUDA，创建CUDA版本
if(CUDA_FOUND)
    pybind11_add_module(adjust_node_area_cuda SHARED
    )
    target_link_libraries(adjust_node_area_cuda PRIVATE torch ${Boost_LIBRARIES})
    set_target_properties(adjust_node_area_cuda PROPERTIES CXX_STANDARD 14 CUDA_SEPARABLE_COMPILATION ON)
    target_include_directories(adjust_node_area_cuda PRIVATE ${CUDA_INCLUDE_DIRS} ${TORCH_INCLUDE_DIRS})
endif()

# 安装模块
install(TARGETS adjust_node_area_cpp DESTINATION dreamplace/ops/adjust_node_area)
if(CUDA_FOUND)
    install(TARGETS adjust_node_area_cuda DESTINATION dreamplace/ops/adjust_node_area)
endif()
