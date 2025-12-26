cmake_minimum_required(VERSION 3.12)

# 收集pin_pos操作源文件
set(PIN_POS_SOURCES
    src/pin_pos.cpp
)

if(CUDA_FOUND)
    list(APPEND PIN_POS_SOURCES
        src/pin_pos_cuda.cpp
        src/pin_pos_cuda_segment.cpp
    )
endif()

# 创建Python绑定
pybind11_add_module(pin_pos_cpp SHARED ${PIN_POS_SOURCES})

# 链接库
target_link_libraries(pin_pos_cpp PRIVATE 
    torch
    ${Boost_LIBRARIES}
)

# 设置编译属性
set_target_properties(pin_pos_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(pin_pos_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(pin_pos_cpp PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(pin_pos_cpp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 如果有CUDA，创建CUDA版本
if(CUDA_FOUND)
    pybind11_add_module(pin_pos_cuda SHARED 
        src/pin_pos_cuda.cpp
        src/pin_pos_cuda_segment.cpp
    )
    target_link_libraries(pin_pos_cuda PRIVATE torch ${Boost_LIBRARIES})
    set_target_properties(pin_pos_cuda PROPERTIES CXX_STANDARD 14 CUDA_SEPARABLE_COMPILATION ON)
    target_include_directories(pin_pos_cuda PRIVATE ${CUDA_INCLUDE_DIRS} ${TORCH_INCLUDE_DIRS})
    
    pybind11_add_module(pin_pos_cuda_segment SHARED src/pin_pos_cuda_segment.cpp)
    target_link_libraries(pin_pos_cuda_segment PRIVATE torch ${Boost_LIBRARIES})
    set_target_properties(pin_pos_cuda_segment PROPERTIES CXX_STANDARD 14 CUDA_SEPARABLE_COMPILATION ON)
    target_include_directories(pin_pos_cuda_segment PRIVATE ${CUDA_INCLUDE_DIRS} ${TORCH_INCLUDE_DIRS})
endif()

# 安装模块
install(TARGETS pin_pos_cpp DESTINATION dreamplace/ops/pin_pos)
if(CUDA_FOUND)
    install(TARGETS pin_pos_cuda pin_pos_cuda_segment DESTINATION dreamplace/ops/pin_pos)
endif()