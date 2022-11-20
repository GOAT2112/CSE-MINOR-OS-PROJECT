import sys
import os

def czseq(n=10):
    while n > 1:
        print(n, end=' ')
        if n&1:
            n = 3*n + 1
        else:
            n = n >> 1
    print(n)

def main():
    args = ()
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        args = n,
    print("Starting child...")
    pid = os.fork()
    if pid == 0:
        czseq(*args)
    else:
        cpid, code  = os.wait()
        print(f'child pid {cpid} completed with exit code {code}')

if __name__ == '__main__':
    main()
