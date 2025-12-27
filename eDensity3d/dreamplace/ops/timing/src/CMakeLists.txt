cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE TIMING_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc" "*.cuh"
)

# Create static library for timing
if(TIMING_SOURCES)
    add_library(timing STATIC ${TIMING_SOURCES})
    
    # Include directories
    target_include_directories(timing PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()