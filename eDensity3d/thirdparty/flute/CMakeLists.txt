cmake_minimum_required(VERSION 3.5)
project(flute)

# Add source files for FLUTE
file(GLOB_RECURSE FLUTE_SOURCES 
    "*.c" "*.cpp" "*.h" "*.hpp"
)

# Create static library for FLUTE
if(FLUTE_SOURCES)
    add_library(flute STATIC ${FLUTE_SOURCES})
    
    # Include directories
    target_include_directories(flute PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()