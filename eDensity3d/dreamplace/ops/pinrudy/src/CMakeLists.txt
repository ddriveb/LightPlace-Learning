cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE PINRUDY_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc" "*.cuh"
)

# Create static library for pinrudy
if(PINRUDY_SOURCES)
    add_library(pinrudy STATIC ${PINRUDY_SOURCES})
    
    # Include directories
    target_include_directories(pinrudy PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()