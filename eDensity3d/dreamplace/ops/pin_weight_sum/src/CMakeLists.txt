cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE PIN_WEIGHT_SUM_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc" "*.cuh"
)

# Create static library for pin_weight_sum
if(PIN_WEIGHT_SUM_SOURCES)
    add_library(pin_weight_sum STATIC ${PIN_WEIGHT_SUM_SOURCES})
    
    # Include directories
    target_include_directories(pin_weight_sum PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
endif()