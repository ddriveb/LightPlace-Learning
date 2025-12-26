cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE GREEDY_LEGALIZE_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc"
)

# Create static library for greedy_legalize
if(GREEDY_LEGALIZE_SOURCES)
    add_library(greedy_legalize STATIC ${GREEDY_LEGALIZE_SOURCES})
    
    # Include directories
    target_include_directories(greedy_legalize PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()