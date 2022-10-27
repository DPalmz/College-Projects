/*
Yuri Goto
program2
10/13/18
*/

#include "prod_cons_MT.h"

int main(int argc, char *argv[]){	
	if(argc != 4){
		printf("Re-Enter not enough inputs\n");
		return 0;
	}
	else{
		queue que;//make Q
		int bufferSize = atoi(argv[1]);
		int numProd = atoi(argv[2]);
		int numCons = atoi(argv[3]);
		int whatsLeft = numProd*bufferSize*2;
		que.numProd = numProd;
		que.numCons = numCons;
		que.full = bufferSize;
		que.buff = malloc (bufferSize * sizeof(int));//size of Q
		que.producer = malloc (numProd * sizeof (pthread_t));//# of prod
		que.consumer = malloc (numCons * sizeof (pthread_t));//# of cons
		que.output = 0;//head of Q
		que.input = 0;//tail of Q
		que.count = 0;		
		que.whatsLeft = whatsLeft;//total product that needs to be used
		pthread_mutex_init(&que.lock,NULL);
		pthread_cond_init(&que.forStuff,NULL);
		pthread_cond_init(&que.forSpace,NULL);
				
		//printf("gets to here\n");
		for(int i =0; i<numProd; i++){//makes all the prod
			printf("starting producer%d\n", i);
			pthread_create(&que.producer[i], NULL, produce, &que);
		}
		for(int i=0; i<numCons; i++){//makes all the cons
			printf("starting consumer%d\n", i);
			pthread_create(&que.consumer[i], NULL, consume, &que);
		}
		for(int i=0; i<numProd; i++){//join all the prod
			pthread_join(que.producer[i],NULL);
			printf("Ending producer%d\n", i);
		}
		for(int i=0; i<numCons; i++){//join all the cons
			pthread_join(que.consumer[i],NULL);
			printf("Ending consumer%d\n", i);
		}
		
	}
	return 0;	
}
