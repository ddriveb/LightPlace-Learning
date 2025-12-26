cmake_minimum_required(VERSION 3.12)

# 收集weighted_average_wirelength操作源文件
set(WEIGHTED_AVERAGE_WIRELENGTH_SOURCES
    src/weighted_average_wirelength_atomic.cpp
)

if(CUDA_FOUND)
    list(APPEND WEIGHTED_AVERAGE_WIRELENGTH_SOURCES
        src/weighted_average_wirelength_cuda_atomic.cpp
        src/weighted_average_wirelength_cuda_merged.cpp
    )
endif()

# 创建Python绑定
pybind11_add_module(weighted_average_wirelength_cpp SHARED ${WEIGHTED_AVERAGE_WIRELENGTH_SOURCES})

# 链接库
target_link_libraries(weighted_average_wirelength_cpp PRIVATE 
    torch
    ${Boost_LIBRARIES}
)

# 设置编译属性
set_target_properties(weighted_average_wirelength_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(weighted_average_wirelength_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(weighted_average_wirelength_cpp PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(weighted_average_wirelength_cpp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 如果有CUDA，创建CUDA版本
if(CUDA_FOUND)
    pybind11_add_module(weighted_average_wirelength_cuda_atomic SHARED src/weighted_average_wirelength_cuda_atomic.cpp)
    target_link_libraries(weighted_average_wirelength_cuda_atomic PRIVATE torch ${Boost_LIBRARIES})
    set_target_properties(weighted_average_wirelength_cuda_atomic PROPERTIES CXX_STANDARD 14 CUDA_SEPARABLE_COMPILATION ON)
    target_include_directories(weighted_average_wirelength_cuda_atomic PRIVATE ${CUDA_INCLUDE_DIRS} ${TORCH_INCLUDE_DIRS})
    
    pybind11_add_module(weighted_average_wirelength_cuda_merged SHARED src/weighted_average_wirelength_cuda_merged.cpp)
    target_link_libraries(weighted_average_wirelength_cuda_merged PRIVATE torch ${Boost_LIBRARIES})
    set_target_properties(weighted_average_wirelength_cuda_merged PROPERTIES CXX_STANDARD 14 CUDA_SEPARABLE_COMPILATION ON)
    target_include_directories(weighted_average_wirelength_cuda_merged PRIVATE ${CUDA_INCLUDE_DIRS} ${TORCH_INCLUDE_DIRS})
endif()

# 安装模块
install(TARGETS weighted_average_wirelength_cpp DESTINATION dreamplace/ops/weighted_average_wirelength)
if(CUDA_FOUND)
    install(TARGETS weighted_average_wirelength_cuda_atomic weighted_average_wirelength_cuda_merged DESTINATION dreamplace/ops/weighted_average_wirelength)
endif()