import sys

T = int(sys.stdin.readline().rstrip())
while T:
    a, b = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(f"{a + b}\n")
    T -= 1
