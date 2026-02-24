// A simple Rust program to test CPU performance by
// generating a series of prime numbers

use std::thread;
use std::time::Instant;

const NUM_SERIES: u64 = 10_000_000;
const NUM_THREADS: u64 = 12;

fn is_prime(number: u64) -> bool {
    let limit = (number as f64).sqrt() as u64 + 1;
    for d in 2..limit {
        if number % d == 0 {
            return false;
        }
    }
    return true;
}

fn print_primes(start: u64, stop: u64, thread_name: String) {
    let mut current = start;
    while current < stop {
        if is_prime(current) {
            println!("{}: {}", thread_name, current);
        }
        current += 1;
    }
}

fn main() {
    let mut threads = vec![];
    let chunk_size: u64 = NUM_SERIES / NUM_THREADS;

    let start_time = Instant::now();
    for i in 0..NUM_THREADS {
        let start: u64 = i * chunk_size;
        let stop: u64 = start + chunk_size;
        let thread_name = format!("Thread-{}", i + 1);

        eprintln!("Created thread {} with start={}, stop={}", thread_name, start, stop);

        let t = thread::spawn(move || {
            print_primes(start, stop, thread_name);
        });

        threads.push(t);
    }


    for t in threads {
        t.join().unwrap();
    }
    let duration = start_time.elapsed();
    eprintln!("{} Threads took {:.6} seconds to complete", NUM_THREADS, duration.as_secs_f64());
}
