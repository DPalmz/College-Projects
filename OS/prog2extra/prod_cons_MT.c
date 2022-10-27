#include "prod_cons_MT.h"
/*
Yuri Goto
program2
10/13/18
*/


void *produce(void *arg){
		
	queue *que = (queue*) arg;
	int threadNum;
	for(int i = 0; i<que->numProd;i++){
		if(que->producer[i] == pthread_self()){
			threadNum = i;
		}
	}
		
	int inputs[que->full*2];
	int j =0;
	printf("p%d is producing %d values\n", threadNum, (que->full*2));	
	
	for(int i=0; i < que->full*2; i++){		
		inputs[i] = rand()%10 + 1;
		pthread_mutex_lock(&que->lock);
			
		if(que->count == que->full){
			printf("Waiting for queue to be emptied\n");
			pthread_cond_wait(&que->forSpace, &que->lock);
		}
		
		printf("P%d: Writing %d to position %d\n", threadNum, inputs[j], que->input);
		que->buff[que->input] = inputs[j];
		que->input++;
		
		if(que->input == que->full)
			que->input = 0;
		
		j++;
		que->count++;
		
		pthread_mutex_unlock(&que->lock);
		pthread_cond_signal(&que->forStuff);	
	}
}

void *consume(void *arg){
	queue *que = (queue*) arg;
	int threadNum;	
	
	for(int i = 0; i<que->numCons;i++){
		if(que->consumer[i] == pthread_self()){
			threadNum = i;
			
		}
	}
	for(int i=0; i < que->full*2; i++){
		pthread_mutex_lock(&que->lock);
			
		if(que->count == 0){
			
			printf("Waiting for queue to be filled\n");
			pthread_cond_wait(&que->forStuff, &que->lock);
		}
		
		printf("C%d: Reading %d from position %d\n", threadNum, que->buff[que->output], que->output);
		que->output++;			
		if(que->output == que->full)
			que->output = 0;
		
		que->count--;
		que->whatsLeft--;
		
		pthread_mutex_unlock(&que->lock);
		pthread_cond_signal(&que->forSpace);	
	}

}


