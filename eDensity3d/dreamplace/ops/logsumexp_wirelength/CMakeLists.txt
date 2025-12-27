cmake_minimum_required(VERSION 3.12)

# 收集logsumexp_wirelength操作源文件
set(LOGSUMEXP_WIRELENGTH_SOURCES
    src\logsumexp_wirelength_cuda_atomic.cpp
    src\logsumexp_wirelength_cuda_merged.cpp
    src\logsumexp_wirelength_merged.cpp
)

if(CUDA_FOUND)
    list(APPEND LOGSUMEXP_WIRELENGTH_SOURCES
        src\integrate_net_weights_cuda_kernel.cu
        src\logsumexp_wirelength_cuda_atomic_kernel.cu
        src\logsumexp_wirelength_cuda_merged_kernel.cu
    )
endif()

# 创建Python绑定
pybind11_add_module(logsumexp_wirelength_cpp SHARED ${LOGSUMEXP_WIRELENGTH_SOURCES})

# 链接库
target_link_libraries(logsumexp_wirelength_cpp PRIVATE 
    torch
    ${Boost_LIBRARIES}
)

# 设置编译属性
set_target_properties(logsumexp_wirelength_cpp PROPERTIES
    CXX_STANDARD 14
    POSITION_INDEPENDENT_CODE ON
)

# 设置CUDA属性
if(CUDA_FOUND)
    set_target_properties(logsumexp_wirelength_cpp PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
    )
    target_include_directories(logsumexp_wirelength_cpp PRIVATE ${CUDA_INCLUDE_DIRS})
endif()

# 包含目录
target_include_directories(logsumexp_wirelength_cpp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/utility/src
    ${TORCH_INCLUDE_DIRS}
)

# 如果有CUDA，创建CUDA版本
if(CUDA_FOUND)
    pybind11_add_module(logsumexp_wirelength_cuda SHARED
    )
    target_link_libraries(logsumexp_wirelength_cuda PRIVATE torch ${Boost_LIBRARIES})
    set_target_properties(logsumexp_wirelength_cuda PROPERTIES CXX_STANDARD 14 CUDA_SEPARABLE_COMPILATION ON)
    target_include_directories(logsumexp_wirelength_cuda PRIVATE ${CUDA_INCLUDE_DIRS} ${TORCH_INCLUDE_DIRS})
endif()

# 安装模块
install(TARGETS logsumexp_wirelength_cpp DESTINATION dreamplace/ops/logsumexp_wirelength)
if(CUDA_FOUND)
    install(TARGETS logsumexp_wirelength_cuda DESTINATION dreamplace/ops/logsumexp_wirelength)
endif()
