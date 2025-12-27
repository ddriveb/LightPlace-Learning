cmake_minimum_required(VERSION 3.5)
project(Limbo)

# Add source files
file(GLOB_RECURSE Limbo_SOURCES 
    "*.c" "*.cpp" "*.h" "*.hpp"
)

# Create static library for Limbo
if(Limbo_SOURCES)
    add_library(Limbo STATIC ${Limbo_SOURCES})
    
    # Include directories
    target_include_directories(Limbo PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()