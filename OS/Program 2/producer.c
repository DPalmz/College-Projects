#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

read proCount;

void* Producer(void* arg){
    
    printf ("starting producer %d", 

    pthread_mutex_init (full, attr); // not sure these will be needed in the end
    pthread_mutex_init (proVsCon, attr); // unsure this condition will properly change
                                        // between producers and consumers like I want

    pthread_mutex_lock (full);
    pthread_mutex_lock (proVsCon);

    while ( !full || !proVsCon ){ // not quite sure this works
        pthread_cond_wait(prod); // specific condition for when producer needs to be
    }                           // woken up
    
    if( pthread_cond_wake(prod) ){
       int sharedSpace = rand % 100; // to be implemented later
}