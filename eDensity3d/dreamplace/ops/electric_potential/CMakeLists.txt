cmake_minimum_required(VERSION 3.12)

# 收集electric_potential操作源文件
set(ELECTRIC_POTENTIAL_SOURCES
    src/electric_density_map.cpp
    src/electric_force.cpp
)

if(CUDA_FOUND)
    list(APPEND ELECTRIC_POTENTIAL_SOURCES
        src/electric_density_map_cuda.cpp
        src/electric_force_cuda.cpp
    )
endif()

# 创建Python绑定
pybind11_add_module(electric_potential_cpp SHARED ${ELECTRIC_POTENTIAL_SOURCES})

# 链接库
target_link_libraries(electric_potential_cpp PRIVATE 
    torch
    ${Boost_LIBRARIES}
)

# 设置编译属性
set_target_properties(electric_potential_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(electric_potential_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(electric_potential_cpp PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(electric_potential_cpp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 如果有CUDA，创建CUDA版本
if(CUDA_FOUND)
    pybind11_add_module(electric_potential_cuda SHARED 
        src/electric_density_map_cuda.cpp
        src/electric_force_cuda.cpp
    )
    target_link_libraries(electric_potential_cuda PRIVATE torch ${Boost_LIBRARIES})
    set_target_properties(electric_potential_cuda PROPERTIES CXX_STANDARD 14 CUDA_SEPARABLE_COMPILATION ON)
    target_include_directories(electric_potential_cuda PRIVATE ${CUDA_INCLUDE_DIRS} ${TORCH_INCLUDE_DIRS})
endif()

# 安装模块
install(TARGETS electric_potential_cpp DESTINATION dreamplace/ops/electric_potential)
if(CUDA_FOUND)
    install(TARGETS electric_potential_cuda DESTINATION dreamplace/ops/electric_potential)
endif()