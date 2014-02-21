cmake_minimum_required(VERSION 2.6)

# Declare the project
project(libpng)

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

#Create a static Lib:
add_library(png STATIC ${src_files} )
