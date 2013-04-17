#!/usr/bin/python
import module
import buildTools

myModule = module.module(__file__, 'libpng', 'LIBRARY')

myModule.AddModuleDepend('zlib')

myModule.AddSrcFile([
	'png/png.c',
	'png/error.c',
	'png/get.c',
	'png/mem.c',
	'png/pread.c',
	'png/read.c',
	'png/rio.c',
	'png/rtran.c',
	'png/rutil.c',
	'png/set.c',
	'png/trans.c',
	'png/wio.c',
	'png/write.c',
	'png/wtran.c',
	'png/wutil.c'])

myModule.CompileFlags_CC([
	'-DPNG_NO_LIMITS_H'])

myModule.AddExportPath(buildTools.GetCurrentPath(__file__))

# add the currrent module at the 
module.AddModule(myModule)









