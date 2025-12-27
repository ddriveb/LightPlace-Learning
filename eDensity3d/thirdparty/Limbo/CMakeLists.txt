cmake_minimum_required(VERSION 3.5)
project(Limbo)

# Add subdirectory if src exists
if(EXISTS ${CMAKE_CURRENT_LIST_DIR}/src)
    add_subdirectory(src)
endif()

# Add subdirectories based on what exists
if(EXISTS ${CMAKE_CURRENT_LIST_DIR}/limbo)
    add_subdirectory(limbo)
endif()

# Add other thirdparty libraries
if(EXISTS ${CMAKE_CURRENT_LIST_DIR}/flute)
    add_subdirectory(flute)
endif()

if(EXISTS ${CMAKE_CURRENT_LIST_DIR}/flute-3.1)
    add_subdirectory(flute-3.1)
endif()

if(EXISTS ${CMAKE_CURRENT_LIST_DIR}/munkres-cpp)
    add_subdirectory(munkres-cpp)
endif()