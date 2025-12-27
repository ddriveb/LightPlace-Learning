cmake_minimum_required(VERSION 3.5)
project(NCTUgr.ICCAD2012)

# Add source files
file(GLOB_RECURSE NCTUgr.ICCAD2012_SOURCES 
    "*.c" "*.cpp" "*.h" "*.hpp"
)

# Create static library for NCTUgr.ICCAD2012
if(NCTUgr.ICCAD2012_SOURCES)
    add_library(NCTUgr.ICCAD2012 STATIC ${NCTUgr.ICCAD2012_SOURCES})
    
    # Include directories
    target_include_directories(NCTUgr.ICCAD2012 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()