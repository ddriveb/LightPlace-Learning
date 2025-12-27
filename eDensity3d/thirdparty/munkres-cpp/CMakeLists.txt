cmake_minimum_required(VERSION 3.5)
project(munkres-cpp)

# Add source files for munkres-cpp
file(GLOB_RECURSE MUNKRES_SOURCES 
    "*.c" "*.cpp" "*.h" "*.hpp"
)

# Create static library for munkres-cpp
if(MUNKRES_SOURCES)
    add_library(munkres-cpp STATIC ${MUNKRES_SOURCES})
    
    # Include directories
    target_include_directories(munkres-cpp PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()