# FindCairo.cmake
# Find Cairo graphics library
#
# This module defines:
#  CAIRO_FOUND - whether Cairo was found
#  CAIRO_LIBRARIES - Cairo libraries
#  CAIRO_INCLUDE_DIRS - Cairo include directories

find_package(PkgConfig QUIET)
if(PKG_CONFIG_FOUND)
    pkg_check_modules(CAIRO QUIET cairo)
endif()

if(NOT CAIRO_FOUND)
    find_path(CAIRO_INCLUDE_DIRS
        NAMES cairo.h
        PATHS
            /usr/include/cairo
            /usr/local/include/cairo
            /opt/local/include/cairo
    )

    find_library(CAIRO_LIBRARIES
        NAMES cairo
        PATHS
            /usr/lib
            /usr/local/lib
            /opt/local/lib
    )

    include(FindPackageHandleStandardArgs)
    find_package_handle_standard_args(Cairo
        REQUIRED_VARS CAIRO_INCLUDE_DIRS CAIRO_LIBRARIES
        FAIL_MESSAGE "Could NOT find Cairo"
    )
else()
    set(CAIRO_FOUND TRUE)
endif()

mark_as_advanced(CAIRO_INCLUDE_DIRS CAIRO_LIBRARIES)