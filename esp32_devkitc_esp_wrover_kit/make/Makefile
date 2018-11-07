#
# This is a project Makefile. It is assumed the directory this Makefile resides in is a
# project subdirectory.
#

PROJECT_NAME := aws_demos

ifndef AMAZON_FREERTOS_PATH
export AMAZON_FREERTOS_PATH := $(SPN_BUILDER_SDK)
endif

ifndef IDF_PATH
export IDF_PATH := $(AMAZON_FREERTOS_PATH)/lib/third_party/mcu_vendor/espressif/esp-idf
endif

EXTRA_COMPONENT_DIRS := $(SPN_PROJECT_DIR)/common/application_code/espressif_code

include $(IDF_PATH)/make/project.mk
