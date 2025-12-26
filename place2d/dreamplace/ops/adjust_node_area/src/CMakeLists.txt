cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE ADJUST_NODE_AREA_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc"
)

# Collect CUDA files if CUDA is enabled
if(USE_CUDA)
    file(GLOB ADJUST_NODE_AREA_CUDA_SOURCES "*.cu")
    list(APPEND ADJUST_NODE_AREA_SOURCES ${ADJUST_NODE_AREA_CUDA_SOURCES})
endif()

# Create static library for adjust_node_area
if(ADJUST_NODE_AREA_SOURCES)
    if(USE_CUDA AND ADJUST_NODE_AREA_CUDA_SOURCES)
        cuda_add_library(adjust_node_area STATIC ${ADJUST_NODE_AREA_SOURCES})
    else()
        add_library(adjust_node_area STATIC ${ADJUST_NODE_AREA_SOURCES})
    endif()
    
    # Include directories
    target_include_directories(adjust_node_area PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
    
    # Link with required libraries
    if(USE_CUDA)
        target_link_libraries(adjust_node_area ${CUDA_LIBRARIES})
    endif()
endif()