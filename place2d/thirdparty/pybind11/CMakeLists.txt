cmake_minimum_required(VERSION 3.5)
project(pybind11)

# Add pybind11 source files
file(GLOB_RECURSE PYBIND11_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc"
)

# Create interface library for pybind11
if(PYBIND11_SOURCES)
    add_library(pybind11 INTERFACE)
    
    # Include directories
    target_include_directories(pybind11 INTERFACE 
        ${CMAKE_CURRENT_SOURCE_DIR}/include
        ${CMAKE_CURRENT_SOURCE_DIR}
    )
endif()