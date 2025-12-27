cmake_minimum_required(VERSION 3.5)
project(munkres-cpp)

# Add source files
file(GLOB_RECURSE munkres-cpp_SOURCES 
    "*.c" "*.cpp" "*.h" "*.hpp"
)

# Create static library for munkres-cpp
if(munkres-cpp_SOURCES)
    add_library(munkres-cpp STATIC ${munkres-cpp_SOURCES})
    
    # Include directories
    target_include_directories(munkres-cpp PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()