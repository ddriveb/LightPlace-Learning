cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE DENSITY_OVERFLOW_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc" "*.cuh"
)

# Create static library for density_overflow
if(DENSITY_OVERFLOW_SOURCES)
    add_library(density_overflow STATIC ${DENSITY_OVERFLOW_SOURCES})
    
    # Include directories
    target_include_directories(density_overflow PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()