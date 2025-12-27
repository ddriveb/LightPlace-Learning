cmake_minimum_required(VERSION 3.5)
project(flute-3.1)

# Add source files
file(GLOB_RECURSE flute-3.1_SOURCES 
    "*.c" "*.cpp" "*.h" "*.hpp"
)

# Create static library for flute-3.1
if(flute-3.1_SOURCES)
    add_library(flute-3.1 STATIC ${flute-3.1_SOURCES})
    
    # Include directories
    target_include_directories(flute-3.1 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()