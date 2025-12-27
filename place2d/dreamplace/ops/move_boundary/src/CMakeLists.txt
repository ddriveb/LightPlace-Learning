cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE SRC_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc" "*.cuh"
)

# Collect CUDA files if CUDA is enabled
if(USE_CUDA)
    file(GLOB SRC_CUDA_SOURCES "*.cu")
    list(APPEND SRC_SOURCES ${SRC_CUDA_SOURCES})
endif()

# Create static library for src
if(SRC_SOURCES)
    if(USE_CUDA AND SRC_CUDA_SOURCES)
        cuda_add_library(src STATIC ${SRC_SOURCES})
    else()
        add_library(src STATIC ${SRC_SOURCES})
    endif()
    
    # Include directories
    target_include_directories(src PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
    
    # Link with required libraries
    if(USE_CUDA)
        target_link_libraries(src ${CUDA_LIBRARIES})
    endif()
endif()