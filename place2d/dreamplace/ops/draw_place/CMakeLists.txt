cmake_minimum_required(VERSION 3.5)
project(draw_place)

# Find required packages
find_package(Cairo REQUIRED)

# Add subdirectory if src exists
if(EXISTS ${CMAKE_CURRENT_LIST_DIR}/src)
    add_subdirectory(src)
endif()

# Include directories
include_directories(${CAIRO_INCLUDE_DIRS})

# Link libraries
link_libraries(${CAIRO_LIBRARIES})

# Python bindings will be handled by the parent CMakeLists.txt