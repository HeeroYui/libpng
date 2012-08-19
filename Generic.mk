LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_LIBRARIES := zlib

LOCAL_CFLAGS := -DPNG_NO_LIMITS_H

LOCAL_MODULE    := libpng

LOCAL_EXPORT_C_INCLUDES := $(LOCAL_PATH)

# load the common sources file of the platform
include $(LOCAL_PATH)/file.mk

LOCAL_SRC_FILES := $(FILE_LIST)

#include $(BUILD_SHARED_LIBRARY)
include $(BUILD_STATIC_LIBRARY)
