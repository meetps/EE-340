INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_FULLFFT fullfft)

FIND_PATH(
    FULLFFT_INCLUDE_DIRS
    NAMES fullfft/api.h
    HINTS $ENV{FULLFFT_DIR}/include
        ${PC_FULLFFT_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    FULLFFT_LIBRARIES
    NAMES gnuradio-fullfft
    HINTS $ENV{FULLFFT_DIR}/lib
        ${PC_FULLFFT_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(FULLFFT DEFAULT_MSG FULLFFT_LIBRARIES FULLFFT_INCLUDE_DIRS)
MARK_AS_ADVANCED(FULLFFT_LIBRARIES FULLFFT_INCLUDE_DIRS)

