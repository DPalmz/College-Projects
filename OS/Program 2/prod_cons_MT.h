#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h> 

typedef struct
{
	int capacity;
	unsigned head;
	unsigned tail;
	unsigned *head_c;
	unsigned *tail_c;
	unsigned size;
	pthread_mutex_t mutexbuff;
    pthread_cond_t Empty;
    pthread_cond_t Full;
    bool * occupied;
	pthread_t* prod_arr;
	pthread_t* cons_arr;
	int n_prod;
	int n_cons;
	int * buffer;
} buffer;

void *Producer(void* arg);

void *Consumer(void* arg);