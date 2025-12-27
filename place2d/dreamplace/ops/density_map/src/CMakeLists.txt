cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE DENSITY_MAP_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc" "*.cuh"
)

# Collect CUDA files if CUDA is enabled
if(USE_CUDA)
    file(GLOB DENSITY_MAP_CUDA_SOURCES "*.cu")
    list(APPEND DENSITY_MAP_SOURCES ${DENSITY_MAP_CUDA_SOURCES})
endif()

# Create static library for density_map
if(DENSITY_MAP_SOURCES)
    if(USE_CUDA AND DENSITY_MAP_CUDA_SOURCES)
        cuda_add_library(density_map STATIC ${DENSITY_MAP_SOURCES})
    else()
        add_library(density_map STATIC ${DENSITY_MAP_SOURCES})
    endif()
    
    # Include directories
    target_include_directories(density_map PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
    
    # Link with required libraries
    if(USE_CUDA)
        target_link_libraries(density_map ${CUDA_LIBRARIES})
    endif()
endif()