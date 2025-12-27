cmake_minimum_required(VERSION 3.12)

# 收集draw_place操作源文件
set(DRAW_PLACE_SOURCES
    src\draw_place.cpp
)

# 创建Python绑定
pybind11_add_module(draw_place_cpp SHARED ${DRAW_PLACE_SOURCES})

# 链接库
target_link_libraries(draw_place_cpp PRIVATE 
    torch
    ${Boost_LIBRARIES}
)

# 设置编译属性
set_target_properties(draw_place_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(draw_place_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(draw_place_cpp PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(draw_place_cpp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 安装模块
install(TARGETS draw_place_cpp DESTINATION dreamplace/ops/draw_place)
if(CUDA_FOUND)
    install(TARGETS draw_place_cuda DESTINATION dreamplace/ops/draw_place)
endif()
