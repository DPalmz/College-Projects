CC = gcc
RM = rm

CFLAGS = -g -Wall -std=c99

#all: main test1 test2 test3 test4 test5

main: main_code.o
    $(CC) -o main $@ $^ $(CFLAGS)
#test1: test1.c
#    $(CC) $(CFLAGS) test1.c
#test2: test2.c
#    $(CC) $(CFLAGS) test2.c
#test3: test3.c
#    $(CC) $(CFLAGS) test3.c
#test4: test4.c
#    $(CC) $(CFLAGS) test4.c
#test5: test5.c
#    $(CC) $(CFLAGS) test5.c

clean:
	rm -f main_code.o main #test1.o test2.o test3.o test4.o test5.o all
