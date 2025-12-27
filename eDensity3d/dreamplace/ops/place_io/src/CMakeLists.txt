cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE PLACE_IO_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc" "*.cuh"
)

# Create static library for place_io
if(PLACE_IO_SOURCES)
    add_library(place_io STATIC ${PLACE_IO_SOURCES})
    
    # Include directories
    target_include_directories(place_io PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()