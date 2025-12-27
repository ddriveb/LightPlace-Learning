cmake_minimum_required(VERSION 3.12)

# 收集pin_weight_sum操作源文件
set(PIN_WEIGHT_SUM_SOURCES
    src\pws.cpp
    src\pws_cuda.cpp
)

if(CUDA_FOUND)
    list(APPEND PIN_WEIGHT_SUM_SOURCES
        src\pws_cuda_kernel.cu
    )
endif()

# 创建Python绑定
pybind11_add_module(pin_weight_sum_cpp SHARED ${PIN_WEIGHT_SUM_SOURCES})

# 链接库
target_link_libraries(pin_weight_sum_cpp PRIVATE 
    torch
    ${Boost_LIBRARIES}
)

# 设置编译属性
set_target_properties(pin_weight_sum_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(pin_weight_sum_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(pin_weight_sum_cpp PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(pin_weight_sum_cpp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 如果有CUDA，创建CUDA版本
if(CUDA_FOUND)
    pybind11_add_module(pin_weight_sum_cuda SHARED
    )
    target_link_libraries(pin_weight_sum_cuda PRIVATE torch ${Boost_LIBRARIES})
    set_target_properties(pin_weight_sum_cuda PROPERTIES CXX_STANDARD 14 CUDA_SEPARABLE_COMPILATION ON)
    target_include_directories(pin_weight_sum_cuda PRIVATE ${CUDA_INCLUDE_DIRS} ${TORCH_INCLUDE_DIRS})
endif()

# 安装模块
install(TARGETS pin_weight_sum_cpp DESTINATION dreamplace/ops/pin_weight_sum)
if(CUDA_FOUND)
    install(TARGETS pin_weight_sum_cuda DESTINATION dreamplace/ops/pin_weight_sum)
endif()
