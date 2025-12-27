cmake_minimum_required(VERSION 3.12)

# 收集place_io操作源文件
set(PLACE_IO_SOURCES
    src\BenchMetrics.cpp
    src\BinMap.cpp
    src\BookshelfWriter.cpp
    src\DefWriter.cpp
    src\Enums.cpp
    src\Group.cpp
    src\Net.cpp
    src\Node.cpp
    src\Params.cpp
    src\PlaceDB.cpp
    src\place_io.cpp
    src\PybindPlaceDB.cpp
    src\PybindPyPlaceDB.cpp
    src\PyPlaceDB.cpp
    src\Region.cpp
    src\RowMap.cpp
    src\SubRowNodeMap.cpp
)

# 创建Python绑定
pybind11_add_module(place_io_cpp SHARED ${PLACE_IO_SOURCES})

# 链接库
target_link_libraries(place_io_cpp PRIVATE 
    torch
    ${Boost_LIBRARIES}
)

# 设置编译属性
set_target_properties(place_io_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(place_io_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(place_io_cpp PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(place_io_cpp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 安装模块
install(TARGETS place_io_cpp DESTINATION dreamplace/ops/place_io)
if(CUDA_FOUND)
    install(TARGETS place_io_cuda DESTINATION dreamplace/ops/place_io)
endif()
