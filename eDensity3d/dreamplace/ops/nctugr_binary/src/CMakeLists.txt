cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE NCTUGR_BINARY_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc" "*.cuh"
)

# Create static library for nctugr_binary
if(NCTUGR_BINARY_SOURCES)
    add_library(nctugr_binary STATIC ${NCTUGR_BINARY_SOURCES})
    
    # Include directories
    target_include_directories(nctugr_binary PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()