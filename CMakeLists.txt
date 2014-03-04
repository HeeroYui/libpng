cmake_minimum_required(VERSION 2.6)

# Declare the project
project(png)

# set output path:
set(LIBRARY_OUTPUT_PATH lib/${CMAKE_BUILD_TYPE})

include_directories(.)

#Create src file list
set(src_files
	png/png.c
	png/error.c
	png/get.c
	png/mem.c
	png/pread.c
	png/read.c
	png/rio.c
	png/rtran.c
	png/rutil.c
	png/set.c
	png/trans.c
	png/wio.c
	png/write.c
	png/wtran.c
	png/wutil.c
)

add_definitions( -DDEBUG_LEVEL=3 )
add_definitions( -DDEBUG=1 )
if (UNIX)
	add_definitions( -D__TARGET_OS__Linux )
endif(UNIX)
if (APPLE)
	add_definitions( -D__TARGET_OS__MacOs )
endif (APPLE)
if (WIN32)
	add_definitions( -D__TARGET_OS__Windows )
endif (WIN32)

#Create a static Lib:
add_library(png STATIC ${src_files} )
