cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE DRAW_PLACE_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc"
)

# Create static library for draw_place
if(DRAW_PLACE_SOURCES)
    add_library(draw_place STATIC ${DRAW_PLACE_SOURCES})
    
    # Include directories
    target_include_directories(draw_place PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
    
    # Link with required libraries
    target_link_libraries(drawplace ${CAIRO_LIBRARIES})
endif()