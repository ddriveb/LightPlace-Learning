cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE DENSITY_POTENTIAL_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc" "*.cuh"
)

# Collect CUDA files if CUDA is enabled
if(USE_CUDA)
    file(GLOB DENSITY_POTENTIAL_CUDA_SOURCES "*.cu")
    list(APPEND DENSITY_POTENTIAL_SOURCES ${DENSITY_POTENTIAL_CUDA_SOURCES})
endif()

# Create static library for density_potential
if(DENSITY_POTENTIAL_SOURCES)
    if(USE_CUDA AND DENSITY_POTENTIAL_CUDA_SOURCES)
        cuda_add_library(density_potential STATIC ${DENSITY_POTENTIAL_SOURCES})
    else()
        add_library(density_potential STATIC ${DENSITY_POTENTIAL_SOURCES})
    endif()
    
    # Include directories
    target_include_directories(density_potential PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
    
    # Link with required libraries
    if(USE_CUDA)
        target_link_libraries(density_potential ${CUDA_LIBRARIES})
    endif()
endif()