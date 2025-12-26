cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE GLOBAL_SWAP_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc"
)

# Collect CUDA files if CUDA is enabled
if(USE_CUDA)
    file(GLOB GLOBAL_SWAP_CUDA_SOURCES "*.cu")
    list(APPEND GLOBAL_SWAP_SOURCES ${GLOBAL_SWAP_CUDA_SOURCES})
endif()

# Create static library for global_swap
if(GLOBAL_SWAP_SOURCES)
    if(USE_CUDA AND GLOBAL_SWAP_CUDA_SOURCES)
        cuda_add_library(global_swap STATIC ${GLOBAL_SWAP_SOURCES})
    else()
        add_library(global_swap STATIC ${GLOBAL_SWAP_SOURCES})
    endif()
    
    # Include directories
    target_include_directories(global_swap PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
    
    # Link with required libraries
    if(USE_CUDA)
        target_link_libraries(global_swap ${CUDA_LIBRARIES})
    endif()
endif()