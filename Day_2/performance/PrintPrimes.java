// A simple Java program to test CPU performance by
// generating a series of prime numbers

class PrimeTask implements Runnable {
    private long start;
    private long stop;

    public PrimeTask(long start, long stop) {
        this.start = start;
        this.stop = stop;
    }

    public boolean isPrime(long number) {
        var limit = (long)Math.sqrt(number) + 1;

        for (var d=2; d<limit; d++) {
            if (number % d == 0)
                return false;
        }
        return true;
    }

    @Override
    public void run() {
        var threadName = Thread.currentThread().getName();
        for (var i=start; i<stop; i++) {
            if (isPrime(i)) {
                System.out.printf("%s: %d\n", threadName, i);
            }
        }
    }
}

public class PrintPrimes {

    private static final int NUM_SERIES = 10_000_000;
    private static final int NUM_THREADS = 12;

    public static void main(String[] args) {
        Thread[] threads = new Thread[NUM_THREADS];
        var chunkSize = NUM_SERIES / NUM_THREADS;

        var startTime = System.currentTimeMillis();
        for (var i=0; i<NUM_THREADS; i++) {
            var start = i * chunkSize;
            var stop = start + chunkSize;
            var task = new PrimeTask(start, stop);

            threads[i] = new Thread(task);
            threads[i].start();
            System.err.printf("Created %s with start=%d, stop=%d\n", threads[i].getName(), start, stop);
        }

        for (Thread thread: threads) {
            try {
                thread.join();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                System.err.println("Thread interrupted");
            }
        }
        var duration = (System.currentTimeMillis() - startTime) / 1000.0;
        System.err.printf("%d Threads took %.6f seconds to complete\n", NUM_THREADS, duration);
    }
}
