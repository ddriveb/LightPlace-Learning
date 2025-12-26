cmake_minimum_required(VERSION 3.12)
project(eDensity3d)

# 设置C++标准
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 构建类型
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# 安装前缀设置
if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
    set(CMAKE_INSTALL_PREFIX ${CMAKE_CURRENT_BINARY_DIR}/install CACHE PATH "Install path" FORCE)
endif()

# 查找Python
find_package(Python COMPONENTS Interpreter Development REQUIRED)
message(STATUS "Python executable: ${Python_EXECUTABLE}")

# 查找PyTorch
execute_process(
    COMMAND ${Python_EXECUTABLE} -c "import torch; print(torch.utils.cmake_prefix_path)"
    OUTPUT_VARIABLE TORCH_CMAKE_PREFIX_PATH
    OUTPUT_STRIP_TRAILING_WHITESPACE
    RESULT_VARIABLE TORCH_FOUND
)
if(TORCH_FOUND EQUAL 0)
    list(APPEND CMAKE_PREFIX_PATH ${TORCH_CMAKE_PREFIX_PATH})
    find_package(Torch REQUIRED)
    message(STATUS "Found PyTorch: ${TORCH_VERSION}")
else()
    message(FATAL_ERROR "PyTorch not found!")
endif()

# 查找其他依赖
find_package(Boost REQUIRED COMPONENTS system filesystem thread)
find_package(ZLIB REQUIRED)

# 查找CUDA (可选)
find_package(CUDA QUIET)
if(CUDA_FOUND)
    message(STATUS "Found CUDA: ${CUDA_VERSION}")
    enable_language(CUDA)
    set(CMAKE_CUDA_FLAGS "${CMAKE_CUDA_FLAGS} -gencode=arch=compute_60,code=sm_60")
    set(CUDA_FOUND_STRING "TRUE")
else()
    message(STATUS "CUDA not found, building CPU only")
    set(CUDA_FOUND_STRING "FALSE")
endif()

# 查找Bison
find_program(BISON_EXECUTABLE bison)
if(NOT BISON_EXECUTABLE)
    message(FATAL_ERROR "Bison not found! Please install bison.")
endif()

# 查找Flex
find_program(FLEX_EXECUTABLE flex)
if(NOT FLEX_EXECUTABLE)
    message(FATAL_ERROR "Flex not found! Please install flex.")
endif()

# 查找Cairo (可选)
find_package(Cairo QUIET)
if(CAIRO_FOUND)
    message(STATUS "Found Cairo: enabling fast plotting")
    set(CAIRO_FOUND_STRING "TRUE")
else()
    message(STATUS "Cairo not found: using Python plotting")
    set(CAIRO_FOUND_STRING "FALSE")
endif()

# 包含自定义cmake模块
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

# 设置编译选项
if(CMAKE_BUILD_TYPE STREQUAL "Release")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -DNDEBUG")
    set(CMAKE_CUDA_FLAGS "${CMAKE_CUDA_FLAGS} -O3 -DNDEBUG")
else()
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -O0")
    set(CMAKE_CUDA_FLAGS "${CMAKE_CUDA_FLAGS} -g -O0")
endif()

# 设置C++ ABI兼容性
if(NOT DEFINED CMAKE_CXX_ABI)
    set(CMAKE_CXX_ABI 0 CACHE STRING "C++11 ABI compatibility")
endif()

# 配置Python文件
configure_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/dreamplace/configure.py.in
    ${CMAKE_CURRENT_BINARY_DIR}/dreamplace/configure.py
    @ONLY
)

# 添加第三方库
add_subdirectory(thirdparty)

# 包含目录
include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_BINARY_DIR}
    ${TORCH_INCLUDE_DIRS}
    ${Boost_INCLUDE_DIRS}
)

# 构建操作算子
add_subdirectory(dreamplace/ops)

# 创建Python扩展
pybind11_add_module(dreamplace_ops
    dreamplace/ops/utility/src/utils.cpp
    dreamplace/ops/utility/src/torch.h
)

# 链接库
target_link_libraries(dreamplace_ops 
    ${TORCH_LIBRARIES}
    ${Boost_LIBRARIES}
    ${ZLIB_LIBRARIES}
)

# 设置属性
set_target_properties(dreamplace_ops PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 安装目标
install(TARGETS dreamplace_ops DESTINATION lib)

# 安装Python文件
install(DIRECTORY dreamplace/ DESTINATION dreamplace
    FILES_MATCHING PATTERN "*.py"
)

# 安装配置文件
install(FILES 
    ${CMAKE_CURRENT_BINARY_DIR}/dreamplace/configure.py
    DESTINATION dreamplace
)

# 安装参数文件
install(FILES
    dreamplace/params.json
    DESTINATION dreamplace
)

# 打印配置信息
message(STATUS "")
message(STATUS "Configuration Summary:")
message(STATUS "  PyTorch: ${TORCH_VERSION}")
message(STATUS "  CUDA: ${CUDA_FOUND_STRING}")
message(STATUS "  Cairo: ${CAIRO_FOUND_STRING}")
message(STATUS "  C++ ABI: ${CMAKE_CXX_ABI}")
message(STATUS "  Build Type: ${CMAKE_BUILD_TYPE}")
message(STATUS "  Install Prefix: ${CMAKE_INSTALL_PREFIX}")
message(STATUS "")