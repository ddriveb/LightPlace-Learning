cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE DCT_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc" "*.cuh"
)

# Collect CUDA files if CUDA is enabled
if(USE_CUDA)
    file(GLOB DCT_CUDA_SOURCES "*.cu")
    list(APPEND DCT_SOURCES ${DCT_CUDA_SOURCES})
endif()

# Create static library for dct
if(DCT_SOURCES)
    if(USE_CUDA AND DCT_CUDA_SOURCES)
        cuda_add_library(dct STATIC ${DCT_SOURCES})
    else()
        add_library(dct STATIC ${DCT_SOURCES})
    endif()
    
    # Include directories
    target_include_directories(dct PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
    
    # Link with required libraries
    if(USE_CUDA)
        target_link_libraries(dct ${CUDA_LIBRARIES})
    endif()
endif()