cmake_minimum_required(VERSION 3.12)

# 收集rmst_wl操作源文件
set(RMST_WL_SOURCES
    src\rmst_wl.cpp
)

# 创建Python绑定
pybind11_add_module(rmst_wl_cpp SHARED ${RMST_WL_SOURCES})

# 链接库
target_link_libraries(rmst_wl_cpp PRIVATE 
    torch
    ${Boost_LIBRARIES}
)

# 设置编译属性
set_target_properties(rmst_wl_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(rmst_wl_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(rmst_wl_cpp PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(rmst_wl_cpp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 安装模块
install(TARGETS rmst_wl_cpp DESTINATION dreamplace/ops/rmst_wl)
if(CUDA_FOUND)
    install(TARGETS rmst_wl_cuda DESTINATION dreamplace/ops/rmst_wl)
endif()
