#define _GNU_SOURCE

#include <time.h>
#include <execinfo.h>

typedef struct stop_watch_struct {
	long double start_time;
	long double stop_time;
} stop_watch_t;

static inline long double timespec_to_sec(struct timespec ts)
{
	return (long double) ts.tv_sec + (long double) ts.tv_nsec * 1.0e-9;
}

static inline long double duration(stop_watch_t *watch)
{
	return watch->stop_time - watch->start_time;
}

static inline void start_watch(stop_watch_t *watch)
{
	struct timespec ts;
	clock_gettime(CLOCK_BOOTTIME, &ts);
	watch->start_time = timespec_to_sec(ts);
}

static inline long double stop_watch(stop_watch_t *watch)
{
	struct timespec ts;
	clock_gettime(CLOCK_BOOTTIME, &ts);
	watch->stop_time = timespec_to_sec(ts);
	return duration(watch);
}
