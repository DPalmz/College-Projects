 #include <pthread.h>
 #include <stdio.h>
 #include <stdlib.h>
#include <time.h>

pthread_mutex_t mutexbuff;
pthread_cond_t Empty;
pthread_cond_t Full;

typedef struct
{
	int capacity;
	unsigned head;
	unsigned tail;
	unsigned size;
	
} Buffer_attr;

Buffer_attr Buff;

//Thread function for Cosumer
void* Consumer(void* arg)
{
	int *buffer = (int *)arg;
	
	while (Buff.size == 0)
	{
		printf(" Consumer is waiting because buffer is EMPTY\n");
		pthread_cond_wait(&Full, &mutexbuff);
		printf(" Consumer got signal\n");
	}
	
	while (Buff.size > 0)
	{
		pthread_mutex_lock(&mutexbuff);
		int elem = buffer[Buff.head];
		printf(" Consumer: the elment %d has value %d \n", Buff.head, elem);
		Buff.head = (Buff.head + 1) % Buff.capacity;
		Buff.size--;
		printf("Consumer: the size is %d \n", Buff.size);
		pthread_cond_signal(&Empty);
		pthread_mutex_unlock(&mutexbuff);
		
	}
		
		pthread_exit(0);
}


//Thread function for Producer
void* Producer(void* arg)
{
	int *buffer = (int *)arg;
	for (int i = 0; i < Buff.capacity*2; i++)
	{
		
			while (Buff.size == Buff.capacity)
			{
				printf(" Producer is waiting because buffer is FULL\n");
				pthread_cond_wait(&Empty, &mutexbuff);
				printf(" Producer got signal\n");
			}
			if (Buff.size < Buff.capacity) {
			pthread_mutex_lock(&mutexbuff);
			buffer[Buff.tail] = rand() % 100;
			printf("Producer: the elment %d has value %d \n", Buff.tail, buffer[Buff.tail]);
			Buff.tail = (Buff.tail + 1) % Buff.capacity;
			Buff.size++;
			printf("Producer: the size is %d \n", Buff.size);
			pthread_cond_signal(&Full);
			pthread_mutex_unlock(&mutexbuff);
			
		}
	}
	pthread_exit(0);
}
 
 
 int main (int argc, char *argv[])
 {
	 if (argc < 3) {
		 printf("Usage: %s <num>\n", argv[0]);
		 exit(-1);
	 }

	 srand(time(0));


    Buff.capacity = atoll(argv[1]);
	int capacity = atoll(argv[1]);
   printf("the entered capacity is %d \n", Buff.capacity);
   
   int buffer[capacity];
     
   Buff.size = 0;
   Buff.head = 0;
   Buff.tail = 0;

     
   // Thread ID:
   int num_args = atoll(argv[2]);
   printf("the number of threads %d \n", num_args);
   pthread_attr_t attr;
   pthread_t tid[num_args];
   pthread_mutex_init(&mutexbuff, NULL);
   pthread_cond_init(&Empty, NULL);
   pthread_cond_init(&Full, NULL);

   // Create attributes
   
   pthread_attr_init(&attr);
   pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

   pthread_create(&tid[0], &attr, Producer, (void *)buffer);
   pthread_create(&tid[1], &attr, Consumer, (void *)buffer);
   pthread_attr_destroy(&attr);
   //Wait intil thread is done its work

   for (int t = 0; t < num_args; t++) {
	int rc = pthread_join(tid[t], NULL);
	   if (rc) {
		  printf("ERROR; return code from pthread_join() is %d\n", rc);
		   exit(-1);
	   }
	   printf("Main: completed join with thread %d\n",t);
   }

   pthread_mutex_destroy(&mutexbuff);
   
   pthread_cond_destroy(&Empty);
   pthread_cond_destroy(&Full);
  // pthread_exit(NULL);
   printf("Done");
   
   return 0;
 } 