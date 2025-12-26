cmake_minimum_required(VERSION 3.5)
project(pin_weight_sum)

# Add subdirectory if src exists
if(EXISTS ${CMAKE_CURRENT_LIST_DIR}/src)
    add_subdirectory(src)
endif()

# Python bindings will be handled by the parent CMakeLists.txt