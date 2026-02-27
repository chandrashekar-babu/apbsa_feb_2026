import time

def leak_memory():
    """Simulates a memory leak by appending to a global list."""
    container = []
    for i in range(10):
        # Allocate roughly 50MB of data per loop
        data = ["x" * 1024 * 1024] * 50 
        container.append(data)
        print(f"Allocated batch {i+1}")
        time.sleep(0.5)
    return container

def efficient_function():
    """Does work without hoarding memory."""
    return [i for i in range(1000)]

def main():
    print("Memory test started...")
    efficient_function()
    data = leak_memory()
    print("Done. Check the memray report.")

if __name__ == "__main__":
    main()