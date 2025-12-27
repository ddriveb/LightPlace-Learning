cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE FENCE_REGION_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc" "*.cuh"
)

# Create static library for fence_region
if(FENCE_REGION_SOURCES)
    add_library(fence_region STATIC ${FENCE_REGION_SOURCES})
    
    # Include directories
    target_include_directories(fence_region PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()