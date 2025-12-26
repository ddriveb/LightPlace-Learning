cmake_minimum_required(VERSION 3.12)

# 收集rudy操作源文件
set(RUDY_SOURCES
    src/rudy.cpp
)

if(CUDA_FOUND)
    list(APPEND RUDY_SOURCES
        src/rudy_cuda.cpp
    )
endif()

# 创建Python绑定
pybind11_add_module(rudy_cpp SHARED ${RUDY_SOURCES})

# 链接库
target_link_libraries(rudy_cpp PRIVATE 
    torch
    ${Boost_LIBRARIES}
)

# 设置编译属性
set_target_properties(rudy_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(rudy_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(rudy_cpp PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(rudy_cpp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 如果有CUDA，创建CUDA版本
if(CUDA_FOUND)
    pybind11_add_module(rudy_cuda SHARED src/rudy_cuda.cpp)
    target_link_libraries(rudy_cuda PRIVATE torch ${Boost_LIBRARIES})
    set_target_properties(rudy_cuda PROPERTIES CXX_STANDARD 14 CUDA_SEPARABLE_COMPILATION ON)
    target_include_directories(rudy_cuda PRIVATE ${CUDA_INCLUDE_DIRS} ${TORCH_INCLUDE_DIRS})
endif()

# 安装模块
install(TARGETS rudy_cpp DESTINATION dreamplace/ops/rudy)
if(CUDA_FOUND)
    install(TARGETS rudy_cuda DESTINATION dreamplace/ops/rudy)
endif()