cmake_minimum_required(VERSION 3.12)

# 收集density_map操作源文件
set(DENSITY_MAP_SOURCES
    src\density_map.cpp
    src\density_map_cuda.cpp
)

if(CUDA_FOUND)
    list(APPEND DENSITY_MAP_SOURCES
        src\density_map_cuda_kernel.cu
    )
endif()

# 创建Python绑定
pybind11_add_module(density_map_cpp SHARED ${DENSITY_MAP_SOURCES})

# 链接库
target_link_libraries(density_map_cpp PRIVATE 
    torch
    ${Boost_LIBRARIES}
)

# 设置编译属性
set_target_properties(density_map_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(density_map_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(density_map_cpp PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(density_map_cpp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 如果有CUDA，创建CUDA版本
if(CUDA_FOUND)
    pybind11_add_module(density_map_cuda SHARED
    )
    target_link_libraries(density_map_cuda PRIVATE torch ${Boost_LIBRARIES})
    set_target_properties(density_map_cuda PROPERTIES CXX_STANDARD 14 CUDA_SEPARABLE_COMPILATION ON)
    target_include_directories(density_map_cuda PRIVATE ${CUDA_INCLUDE_DIRS} ${TORCH_INCLUDE_DIRS})
endif()

# 安装模块
install(TARGETS density_map_cpp DESTINATION dreamplace/ops/density_map)
if(CUDA_FOUND)
    install(TARGETS density_map_cuda DESTINATION dreamplace/ops/density_map)
endif()
