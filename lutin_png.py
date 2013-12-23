#!/usr/bin/python
import lutinModule as module
import lutinTools as tools

def get_desc():
	return "PNG : png file reader and writer"


def create(target):
	myModule = module.Module(__file__, 'png', 'LIBRARY')
	
	myModule.add_module_depend('z')
	
	myModule.add_src_file([
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
	
	myModule.compile_flags_CC([
		'-DPNG_NO_LIMITS_H'])
	
	myModule.add_export_path(tools.get_current_path(__file__))
	
	# add the currrent module at the 
	return myModule









