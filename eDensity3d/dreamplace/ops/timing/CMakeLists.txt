cmake_minimum_required(VERSION 3.12)

# 收集timing操作源文件
set(TIMING_SOURCES
    src\timing_cpp.cpp
    src\timing_io_cpp.cpp
    src\timing_pybind.cpp
)

# 创建Python绑定
pybind11_add_module(timing_cpp SHARED ${TIMING_SOURCES})

# 链接库
target_link_libraries(timing_cpp PRIVATE 
    torch
    ${Boost_LIBRARIES}
)

# 设置编译属性
set_target_properties(timing_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(timing_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(timing_cpp PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(timing_cpp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 安装模块
install(TARGETS timing_cpp DESTINATION dreamplace/ops/timing)
if(CUDA_FOUND)
    install(TARGETS timing_cuda DESTINATION dreamplace/ops/timing)
endif()
