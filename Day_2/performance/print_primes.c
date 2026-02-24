#define _GNU_SOURCE
#include "stop_watch.h"

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
#include <pthread.h>

#define NUM_SERIES 10000000
#define NUM_THREADS 12

typedef struct thread_args_struct {
	unsigned int id;
	unsigned int start;
	unsigned int stop;
} thread_args_t;


int is_prime(long long n) {
	long long i;

	long long s = (long long)sqrtl(n) + 1;

	for (i=2; i<s; i++) {
		if ((n%i) == 0)
			return 0;
	}
	return 1;
}

void* print_primes(void *args)
{
	thread_args_t *arguments = args;
	unsigned int start = arguments->start;
	unsigned int stop = arguments->stop;
	unsigned int id = arguments->id;
	unsigned int i;

	for(i=start; i<stop; i++) {
		if (is_prime(i)) {
			printf("Thread-%u: %lu\n", id, i);
		}
	}
}

int main()
{
	pthread_t threads[NUM_THREADS];
	thread_args_t thread_args[NUM_THREADS];
	unsigned int chunk_size = NUM_SERIES / NUM_THREADS;

	stop_watch_t watch;

	void *ret;
	int i;

	start_watch(&watch);
	for (i=0; i<NUM_THREADS; i++) {
		thread_args[i].id = i+1;
		thread_args[i].start = i * chunk_size;
		thread_args[i].stop = (i * chunk_size) + chunk_size;

		pthread_create(&threads[i],
				NULL,
				print_primes,
				&thread_args[i]);

		fprintf(stderr, "Created Thread-%u with start=%u, stop=%u\n",
			thread_args[i].id,
			thread_args[i].start,
			thread_args[i].stop);
	}

	for (i=0; i<NUM_THREADS; i++) {
		pthread_join(threads[i], &ret);
	}
	stop_watch(&watch);
	fprintf(stderr, "%d Threads took %3.6Lf seconds to complete.\n", NUM_THREADS, duration(&watch));

	return 0;
}
