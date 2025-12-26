cmake_minimum_required(VERSION 3.12)

# Utility模块提供头文件和辅助函数，不需要Python绑定

# 包含目录，供其他模块使用
target_include_directories(utility INTERFACE
    ${CMAKE_CURRENT_SOURCE_DIR}/src
)

# 安装头文件
install(DIRECTORY src/ 
    DESTINATION dreamplace/ops/utility
    FILES_MATCHING PATTERN "*.h" PATTERN "*.cuh"
)