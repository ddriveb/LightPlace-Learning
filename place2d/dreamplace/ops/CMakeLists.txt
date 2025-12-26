cmake_minimum_required(VERSION 3.12)

# 查找pybind11
if(DEFINED pybind11_DIR)
    find_package(pybind11 REQUIRED)
else()
    find_package(pybind11 CONFIG REQUIRED)
endif()

# 设置源文件目录
set(OPS_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR})

# 收集所有操作算子 (place2d版本的子目录)
set(OPS_SUBDIRS
    hpwl
    density_map
    density_potential
    density_overflow
    electric_potential
    pin_pos
    pin_weight_sum
    rudy
    utility
    legality_check
    greedy_legalize
    global_swap
    weighted_average_wirelength
    logsumexp_wirelength
    move_boundary
    abacus_legalize
    macro_legalize
    independent_set_matching
    k_reorder
    dct
    place_io
    timing
    fence_region
    nctugr_binary
    pinrudy
    rmst_wl
    draw_place
    pin_utilization
    adjust_node_area
)

# 构建每个操作算子
foreach(OP_SUBDIR ${OPS_SUBDIRS})
    if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/${OP_SUBDIR})
        add_subdirectory(${OP_SUBDIR})
    endif()
endforeach()

# 创建主Python模块
pybind11_add_module(place2d_ops SHARED)

# 收集所有源文件
file(GLOB_RECURSE OPS_SOURCES 
    "${CMAKE_CURRENT_SOURCE_DIR}/*/src/*.cpp"
    "${CMAKE_CURRENT_SOURCE_DIR}/*/src/*.cu"
)

# 添加源文件到模块
target_sources(place2d_ops PRIVATE ${OPS_SOURCES})

# 链接库
target_link_libraries(place2d_ops PRIVATE 
    torch
    ${Boost_LIBRARIES}
    ${ZLIB_LIBRARIES}
)

# 设置编译属性
set_target_properties(place2d_ops PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(place2d_ops PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(place2d_ops PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(place2d_ops PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 生成Python __init__.py文件
set(OPS_INIT_FILE "${CMAKE_CURRENT_BINARY_DIR}/__init__.py")
file(WRITE ${OPS_INIT_FILE}
"# Auto-generated place2d operations module
")

foreach(OP_SUBDIR ${OPS_SUBDIRS})
    if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/${OP_SUBDIR})
        file(APPEND ${OPS_INIT_FILE}
"from . import ${OP_SUBDIR}\n")
    endif()
endforeach()

# 安装操作算子模块
install(TARGETS place2d_ops DESTINATION dreamplace/ops)
install(FILES ${OPS_INIT_FILE} DESTINATION dreamplace/ops)