cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE MACRO_LEGALIZE_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc" "*.cuh"
)

# Create static library for macro_legalize
if(MACRO_LEGALIZE_SOURCES)
    add_library(macro_legalize STATIC ${MACRO_LEGALIZE_SOURCES})
    
    # Include directories
    target_include_directories(macro_legalize PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()