cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE RMST_WL_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc" "*.cuh"
)

# Create static library for rmst_wl
if(RMST_WL_SOURCES)
    add_library(rmst_wl STATIC ${RMST_WL_SOURCES})
    
    # Include directories
    target_include_directories(rmst_wl PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()