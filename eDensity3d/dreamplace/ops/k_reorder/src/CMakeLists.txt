cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE K_REORDER_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc" "*.cuh"
)

# Create static library for k_reorder
if(K_REORDER_SOURCES)
    add_library(k_reorder STATIC ${K_REORDER_SOURCES})
    
    # Include directories
    target_include_directories(k_reorder PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()