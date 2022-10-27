#include "prod_cons_MT.h"

buffer Buff;

int main (int argc, char *argv[])
 {
	 if (argc < 4) {
		 printf("Usage: %s size n_prod n_cons\n", argv[0]);
		 exit(-1);
	 }

	 srand(time(0));


    Buff.capacity = atoll(argv[1]);
	int capacity = atoll(argv[1]);
    printf("the entered capacity is %d \n", Buff.capacity);
    Buff.buffer = malloc (capacity * sizeof (int));
    int buffer[capacity];

   Buff.size = 0;
   Buff.head = 0;
   Buff.tail = 0;


   // Thread ID:
   Buff.n_prod = atoll(argv[2]);
   printf("Number of producer threads %d \n", Buff.n_prod);
   Buff.n_cons = atoll(argv[3]);
   printf("Number of consumer threads %d \n", Buff.n_cons);
   pthread_attr_t attr;
   Buff.prod_arr = malloc (Buff.n_prod * sizeof (pthread_t));
   Buff.cons_arr = malloc (Buff.n_cons * sizeof (pthread_t));
   pthread_mutex_init(&Buff.mutexbuff, NULL);
   pthread_cond_init(&Buff.Empty, NULL);
   pthread_cond_init(&Buff.Full, NULL);

   // Create attributes

   pthread_attr_init(&attr);
   pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);
   for (int i=0; i<Buff.n_prod; i++){
       pthread_create(&Buff.prod_arr[i], &attr, Producer, (void*)&i);
   }
   for (int i=0; i<Buff.n_cons; i++){
       pthread_create(&Buff.cons_arr[i], &attr, Consumer, (void*)&i);
   }
   pthread_attr_destroy(&attr);
   //Wait until thread is done its work

   for (int t = 0; t < Buff.n_prod; t++) {
	int rc = pthread_join(Buff.prod_arr[t], NULL);
	   if (rc) {
		  printf("ERROR; return code from pthread_join() is %d\n", rc);
		   exit(-1);
	   }
	   printf("Main: completed join with thread %d\n",t);
   }

    for (int t = 0; t < Buff.n_cons; t++) {
	int rc = pthread_join(Buff.cons_arr[t], NULL);
	   if (rc) {
		  printf("ERROR; return code from pthread_join() is %d\n", rc);
		   exit(-1);
	   }
	   printf("Main: completed join with thread %d\n",t);
   }
   pthread_mutex_destroy(&Buff.mutexbuff);

   pthread_cond_destroy(&Buff.Empty);
   pthread_cond_destroy(&Buff.Full);
  // pthread_exit(NULL);
   printf("Done");

   return 0;
 }
