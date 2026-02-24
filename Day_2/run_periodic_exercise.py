"""
Exercise:
---------
Implement the class - RunPeriodic that allows a function
to be executed at periodic intervals in a separate thread.
"""

from run_periodic import RunPeriodic

if __name__ == '__main__':

    def print_test():
        print("Running print_test...")

    def hello_world():
        print("Hello world....")

    print_thread = RunPeriodic(5, print_test)
    print_thread.start()
    # Execute print_test() function every 5 seconds

    hello_thread = RunPeriodic(2, hello_world)
    hello_thread.start()
    # Execute hello_thread() function every 2 seconds

    from time import sleep
    for i in range(20):
        print("main thread: counting", i)
        sleep(1)

    # Issue a stop request to both threads after 20 seconds
    print_thread.stop()
    hello_thread.stop()

    # Wait for both threads to finish.
    print_thread.join()
    hello_thread.join()

    print("main thread: finished.")
