#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>
/*
Yuri Goto
program2
10/13/18
*/
typedef struct queue{
	int *buff;	//buffer
	int full;	//full buffer
	int output;	//head of q cons takes
	int input;	//tail of q prod enters
	int count;	//count of the variables in the q
	int whatsLeft;
	int numProd;
	int numCons;
	pthread_t *producer;	//producer thread
	pthread_t *consumer;	//consumer thread
	pthread_mutex_t lock;	//lock or unlock
	pthread_cond_t forStuff;
	pthread_cond_t forSpace;
	
}queue;

void *produce(void *que);


void *consume(void *que);

