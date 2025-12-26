cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE ABACUS_LEGALIZE_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc"
)

# Create static library for abacus_legalize
if(ABACUS_LEGALIZE_SOURCES)
    add_library(abacus_legalize STATIC ${ABACUS_LEGALIZE_SOURCES})
    
    # Include directories
    target_include_directories(abacus_legalize PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()