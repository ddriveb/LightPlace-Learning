cmake_minimum_required(VERSION 3.5)
project(logsumexp_wirelength)

# Check for CUDA support
if(USE_CUDA)
    enable_language(CUDA)
    set(CUDA_SEPARABLE_COMPILATION ON)
endif()

# Add subdirectory if src exists
if(EXISTS ${CMAKE_CURRENT_LIST_DIR}/src)
    add_subdirectory(src)
endif()

# Python bindings will be handled by the parent CMakeLists.txt