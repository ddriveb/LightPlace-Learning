cmake_minimum_required(VERSION 3.12)

# 构建第三方库
message(STATUS "Building third-party libraries...")

# 构建CUB (CUDA库)
if(CUDA_FOUND AND EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/cub)
    message(STATUS "Including CUB library")
    include_directories(${CMAKE_CURRENT_SOURCE_DIR}/cub)
endif()

# 构建Flute (线长估计)
if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/flute)
    message(STATUS "Including Flute library")
    add_subdirectory(flute)
endif()

# 构建Limbo (布局算法库)
if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/Limbo)
    message(STATUS "Including Limbo library")
    add_subdirectory(Limbo)
endif()

# 构建munkres-cpp (匈牙利算法)
if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/munkres-cpp)
    message(STATUS "Including munkres-cpp library")
    add_subdirectory(munkres-cpp)
endif()

# 处理压缩的第三方库
if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/flute-3.1.zip)
    message(STATUS "Extracting flute-3.1.zip")
    execute_process(
        COMMAND ${CMAKE_COMMAND} -E tar xf flute-3.1.zip
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    )
    add_subdirectory(flute-3.1)
endif()

if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/Limbo-ff81012852bf948ec7346a96a0abc088b943c5e4.zip)
    message(STATUS "Extracting Limbo archive")
    execute_process(
        COMMAND ${CMAKE_COMMAND} -E tar xf Limbo-ff81012852bf948ec7346a96a0abc088b943c5e4.zip
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    )
    if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/Limbo)
        add_subdirectory(Limbo)
    endif()
endif()

if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/munkres-cpp-61086fcf5b3a8ad4bda578cdc2d1dca57b548786.zip)
    message(STATUS "Extracting munkres-cpp archive")
    execute_process(
        COMMAND ${CMAKE_COMMAND} -E tar xf munkres-cpp-61086fcf5b3a8ad4bda578cdc2d1dca57b548786.zip
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    )
    if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/munkres-cpp)
        add_subdirectory(munkres-cpp)
    endif()
endif()

if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/cub-c3cceac115c072fb63df1836ff46d8c60d9eb304.zip)
    message(STATUS "Extracting CUB archive")
    execute_process(
        COMMAND ${CMAKE_COMMAND} -E tar xf cub-c3cceac115c072fb63df1836ff46d8c60d9eb304.zip
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    )
    if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/cub)
        include_directories(${CMAKE_CURRENT_SOURCE_DIR}/cub)
    endif()
endif()

message(STATUS "Third-party libraries configured")