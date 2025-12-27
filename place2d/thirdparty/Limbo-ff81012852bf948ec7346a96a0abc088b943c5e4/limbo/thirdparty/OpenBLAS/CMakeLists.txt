cmake_minimum_required(VERSION 3.5)
project(OpenBLAS)

# Add source files
file(GLOB_RECURSE OpenBLAS_SOURCES 
    "*.c" "*.cpp" "*.h" "*.hpp"
)

# Create static library for OpenBLAS
if(OpenBLAS_SOURCES)
    add_library(OpenBLAS STATIC ${OpenBLAS_SOURCES})
    
    # Include directories
    target_include_directories(OpenBLAS PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()