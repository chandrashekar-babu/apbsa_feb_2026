// A simple C++ program to test CPU performance by
// generating a series of prime numbers

#include <thread>
#include <cmath>
#include <string>
#include <chrono>
#include <iostream>

const int NUM_SERIES = 10'000'000;
const int NUM_THREADS = 12;

// Function to check if a number is prime
bool is_prime(auto number) {
    unsigned int limit = sqrt(number) + 1;

    for (auto d=2; d<limit; d++) {
        if (number % d == 0)
            return false;
    }

    return true;
}

// Function to print primes in a given range
void print_primes(unsigned int start, unsigned int stop, const std::string& thread_name) {
    for (auto i=start; i<stop; i++) {
        if (is_prime(i)) {
            std::cout << thread_name << ": " << i << "\n";
        }
    }
}

int main() {

    std::thread threads[NUM_THREADS];
    auto chunk_size = NUM_SERIES / NUM_THREADS;

    auto start_time = std::chrono::high_resolution_clock::now();

    for (auto i=0; i<NUM_THREADS; i++) {
        auto start = i * chunk_size;
        auto stop = start + chunk_size;
        std::string thread_name = "Thread-" + std::to_string(i + 1);

        threads[i] = std::thread(print_primes, start, stop, thread_name);
        std::cerr << "Created " << thread_name << " with start=" << start << ", stop=" << stop << "\n";

    }

    for (auto& thread: threads) {
        thread.join();
    }

    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end_time - start_time;

    std::cerr << NUM_THREADS << " Threads took " << duration.count() << " seconds to complete\n";

    return 0;
}
