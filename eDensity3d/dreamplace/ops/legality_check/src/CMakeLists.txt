cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE LEGALITY_CHECK_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc"
)

# Create static library for legality_check
if(LEGALITY_CHECK_SOURCES)
    add_library(legality_check STATIC ${LEGALITY_CHECK_SOURCES})
    
    # Include directories
    target_include_directories(legality_check PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()