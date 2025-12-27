#!/usr/bin/env python3
import os

# List of all missing src/CMakeLists.txt files from the analysis
missing_files = [
    "place2d/dreamplace/ops/electric_potential/src/CMakeLists.txt",
    "place2d/dreamplace/ops/fence_region/src/CMakeLists.txt", 
    "place2d/dreamplace/ops/global_swap/src/CMakeLists.txt",
    "place2d/dreamplace/ops/greedy_legalize/src/CMakeLists.txt",
    "place2d/dreamplace/ops/hpwl/src/CMakeLists.txt",
    "place2d/dreamplace/ops/independent_set_matching/src/CMakeLists.txt",
    "place2d/dreamplace/ops/k_reorder/src/CMakeLists.txt",
    "place2d/dreamplace/ops/legality_check/src/CMakeLists.txt",
    "place2d/dreamplace/ops/logsumexp_wirelength/src/CMakeLists.txt",
    "place2d/dreamplace/ops/macro_legalize/src/CMakeLists.txt",
    "place2d/dreamplace/ops/move_boundary/src/CMakeLists.txt",
    "place2d/dreamplace/ops/nctugr_binary/src/CMakeLists.txt",
    "place2d/dreamplace/ops/pin_pos/src/CMakeLists.txt",
    "place2d/dreamplace/ops/pin_utilization/src/CMakeLists.txt",
    "place2d/dreamplace/ops/place_io/src/CMakeLists.txt",
    "place2d/dreamplace/ops/rmst_wl/src/CMakeLists.txt",
    "place2d/dreamplace/ops/rudy/src/CMakeLists.txt",
    "place2d/dreamplace/ops/utility/src/CMakeLists.txt",
    "place2d/dreamplace/ops/weighted_average_wirelength/src/CMakeLists.txt",
    "place2d/thirdparty/Limbo/CMakeLists.txt",
    "place2d/thirdparty/NCTUgr.ICCAD2012/CMakeLists.txt",
    "place2d/thirdparty/flute-3.1/CMakeLists.txt",
    "place2d/thirdparty/munkres-cpp/CMakeLists.txt",
    "place2d/thirdparty/Limbo-ff81012852bf948ec7346a96a0abc088b943c5e4/limbo/thirdparty/OpenBLAS/CMakeLists.txt"
]

# Template for src/CMakeLists.txt files
src_template = """cmake_minimum_required(VERSION 3.5)

# Collect source files
file(GLOB_RECURSE {MODULE}_SOURCES 
    "*.cpp" "*.h" "*.hpp" "*.c" "*.cc" "*.cuh"
)

# Collect CUDA files if CUDA is enabled
if(USE_CUDA)
    file(GLOB {MODULE}_CUDA_SOURCES "*.cu")
    list(APPEND {MODULE}_SOURCES ${{{MODULE}_CUDA_SOURCES}})
endif()

# Create static library for {module}
if({MODULE}_SOURCES)
    if(USE_CUDA AND {MODULE}_CUDA_SOURCES)
        cuda_add_library({module} STATIC ${{{MODULE}_SOURCES}})
    else()
        add_library({module} STATIC ${{{MODULE}_SOURCES}})
    endif()
    
    # Include directories
    target_include_directories({module} PUBLIC ${{CMAKE_CURRENT_SOURCE_DIR}})
    
    # Link with required libraries
    if(USE_CUDA)
        target_link_libraries({module} ${{CUDA_LIBRARIES}})
    endif()
endif()"""

# Template for thirdparty CMakeLists.txt files
thirdparty_template = """cmake_minimum_required(VERSION 3.5)
project({PROJECT})

# Add source files
file(GLOB_RECURSE {PROJECT}_SOURCES 
    "*.c" "*.cpp" "*.h" "*.hpp"
)

# Create static library for {PROJECT}
if({PROJECT}_SOURCES)
    add_library({PROJECT} STATIC ${{{PROJECT}_SOURCES}})
    
    # Include directories
    target_include_directories({PROJECT} PUBLIC ${{CMAKE_CURRENT_SOURCE_DIR}})
endif()"""

# Create directories and files
for file_path in missing_files:
    # Extract module name from path
    parts = file_path.split('/')
    if 'ops' in parts:
        module = parts[-2]  # Get the ops module name
        content = src_template.format(MODULE=module.upper(), module=module)
    else:
        # Thirdparty module
        module = parts[-1].replace('-', '_')
        if module == 'CMakeLists.txt':
            module = parts[-2]
        project_name = parts[-2] if parts[-2] != 'thirdparty' else parts[-3]
        content = thirdparty_template.format(PROJECT=project_name)
    
    # Create directory if it doesn't exist
    dir_path = os.path.dirname(file_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory: {dir_path}")
    
    # Write file
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"Created: {file_path}")

print("All missing CMakeLists.txt files created!")