cmake_minimum_required(VERSION 3.5)
project(flute-3.1)

# Add source files for FLUTE-3.1
file(GLOB_RECURSE FLUTE3_1_SOURCES 
    "*.c" "*.cpp" "*.h" "*.hpp"
)

# Create static library for FLUTE-3.1
if(FLUTE3_1_SOURCES)
    add_library(flute-3.1 STATIC ${FLUTE3_1_SOURCES})
    
    # Include directories
    target_include_directories(flute-3.1 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()