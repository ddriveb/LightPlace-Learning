cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE INDEPENDENT_SET_MATCHING_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc" "*.cuh"
)

# Collect CUDA files if CUDA is enabled
if(USE_CUDA)
    file(GLOB INDEPENDENT_SET_MATCHING_CUDA_SOURCES "*.cu")
    list(APPEND INDEPENDENT_SET_MATCHING_SOURCES ${INDEPENDENT_SET_MATCHING_CUDA_SOURCES})
endif()

# Create static library for independent_set_matching
if(INDEPENDENT_SET_MATCHING_SOURCES)
    if(USE_CUDA AND INDEPENDENT_SET_MATCHING_CUDA_SOURCES)
        cuda_add_library(independent_set_matching STATIC ${INDEPENDENT_SET_MATCHING_SOURCES})
    else()
        add_library(independent_set_matching STATIC ${INDEPENDENT_SET_MATCHING_SOURCES})
    endif()
    
    # Include directories
    target_include_directories(independent_set_matching PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
    
    # Link with required libraries
    if(USE_CUDA)
        target_link_libraries(independent_set_matching ${CUDA_LIBRARIES})
    endif()
endif()