#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	pid_t child1, child2;
	printf("Parent pid is %d\n", (int)getpid());


	child1 = fork();


	if (child1 < 0) {
		perror("Fork failed");
	}
	if (child1 == 0) {
		printf("Started child with pid %d\n", (int)getpid());
//      char *filePath[] = {"C:\Users\Dylan Palmer\Documents\(Notepad)\OS\test1.c", NULL};  //part E
//      execv(filePath[0], filePath); // Have to use your own path for test1.c, unless you want me to share those too -DP
	}

	//We must be the parent
	if (child1 > 0) {
		child2 = fork();


		if (child2 < 0) {
			perror("Fork failed");
		}
		if (child2 == 0) {
			printf("Started child with pid %d\n", (int)getpid());
//          char *filePath[] = {"C:\Users\Dylan Palmer\Documents\(Notepad)\OS\test1.c", NULL};  //part E
//          execv(filePath[0], filePath); // Have to use your own path for test1.c
		}

		if (child2 > 0) {
			wait(NULL);
			printf("Child (PID %d) finished\n", child1);
			printf("Child (PID %d) finished\n", child2);
		}
	}
// have some thoughts about how to do part E, but it needs part C to be done
	return 0;
}
