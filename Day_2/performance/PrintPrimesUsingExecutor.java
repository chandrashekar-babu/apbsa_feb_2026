// A simple Java program to test CPU performance by
// generating a series of prime numbers

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class PrintPrimesUsingExecutor {

    private static final int NUM_SERIES = 1_000_000;
    private static final int NUM_THREADS = 8;

    // Method to check if a number is prime
    public static boolean isPrime(int number) {
        var limit = (long)Math.sqrt(number) + 1;

        for (var d=2; d<limit; d++) {
            if (number % d == 0)
                return false;
        }
        return true;
    }

    // Method to print primes in the given range
    public static void printPrimes(int start, int stop, String threadName) {
        for (var i=start; i<stop; i++) {
            if (isPrime(i)) {
                System.out.printf("%s: %d%n", threadName, i);
            }
        }
    }

    public static void main(String[] args) {
        var executor = Executors.newFixedThreadPool(NUM_THREADS);
        var chunkSize = NUM_SERIES / NUM_THREADS;

        var startTime = System.currentTimeMillis();

        for (var i=0; i<NUM_THREADS; i++) {
            var start = i * chunkSize;
            var stop = start + chunkSize;
            var threadName = "Thread-" + (i + 1);

            System.err.printf("Created %s with start=%d, stop=%d%n", threadName, start, stop);

            executor.submit(() -> printPrimes(start, stop, threadName));
        }

        executor.shutdown();
        try {
            executor.awaitTermination(Long.MAX_VALUE, TimeUnit.NANOSECONDS);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.err.println("Threads interrupted");
        }
        var duration = System.currentTimeMillis() - startTime;
        System.err.printf("%d Threads took %.6f seconds to complete\n", NUM_THREADS, duration / 1000.0);

    }
}