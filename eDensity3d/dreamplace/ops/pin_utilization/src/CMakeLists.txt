cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE PIN_UTILIZATION_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc" "*.cuh"
)

# Create static library for pin_utilization
if(PIN_UTILIZATION_SOURCES)
    add_library(pin_utilization STATIC ${PIN_UTILIZATION_SOURCES})
    
    # Include directories
    target_include_directories(pin_utilization PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()