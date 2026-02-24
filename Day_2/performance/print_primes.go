// A simple Go program to test CPU performance by
// generating a series of prime numbers

package main

import (
	"fmt"
	"math"
	"sync"
	"time"
	"os"
)

const (
	NUM_SERIES  = 1_000_000
	NUM_THREADS = 4
)

// isPrime checks if a number is a prime number.
func isPrime(number int) bool {
    limit := int(math.Sqrt(float64(number))) + 1
    for d := 2; d < limit; d++ {
        if number % d == 0 {
            return false
        }
    }
    return true
}
// printPrimes prints prime numbers in the range [start, stop).
func printPrimes(start, stop int, wg *sync.WaitGroup, threadName string) {
	defer wg.Done()
	for i := start; i < stop; i++ {
		if isPrime(i) {
			fmt.Printf("%s: %d\n", threadName, i)
		}
	}
}

func main() {
	var wg sync.WaitGroup
	chunkSize := NUM_SERIES / NUM_THREADS

	startTime := time.Now()

	for i := 0; i < NUM_THREADS; i++ {
		start := i * chunkSize
		stop := start + chunkSize
		threadName := fmt.Sprintf("Thread-%d", i+1)

		fmt.Fprintf(os.Stderr, "Created %s with start=%d, stop=%d\n", threadName, start, stop)

		wg.Add(1)
		go printPrimes(start, stop, &wg, threadName)
	}

	wg.Wait()
	duration := time.Since(startTime)
	fmt.Fprintf(os.Stderr, "%d Threads took %.6f seconds to complete\n", NUM_THREADS, duration.Seconds())
}
