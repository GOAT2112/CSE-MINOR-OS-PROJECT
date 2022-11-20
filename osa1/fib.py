import sys
from threading import Thread

array = []

def fibseries(n=10):
    array.clear()
    x, y = 0, 1
    for _ in range(n):
        array.append(x)
        x, y = y, x+y
    return

def main():
    args = ()
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        args = n,
    th = Thread(target=fibseries, args=args)
    print("Fib thread starting...")
    th.start()
    th.join()
    print("Fib thread done")
    print(f'Fibonacci series upto {len(array)} terms is:')
    print(*array)

if __name__ == "__main__":
    main()
