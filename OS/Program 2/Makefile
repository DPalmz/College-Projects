# Makefile for building demo applications.

# Edit this file to compile extra C files into their own programs.
#TARGETS= sum_on_thread sum_on_many_threads sum_malloc
#TARGETS= main prod_cons_MT
#
#CROSS_TOOL =
#CC_CPP = $(CROSS_TOOL)g++
#CC_C = $(CROSS_TOOL)gcc
#
#CFLAGS = -Wall -g -std=c99 -Werror -pthread
#
#all: $(TARGETS)
#
#$(TARGETS):
#	$(CC_C) $(CFLAGS) $@.c -o $@

make:
	gcc prod_cons_MT.c prod_cons_MT.h -I. -pthread -Wall -g -std=c99
