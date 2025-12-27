cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE MOVE_BOUNDARY_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc" "*.cuh"
)

# Create static library for move_boundary
if(MOVE_BOUNDARY_SOURCES)
    add_library(move_boundary STATIC ${MOVE_BOUNDARY_SOURCES})
    
    # Include directories
    target_include_directories(move_boundary PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()