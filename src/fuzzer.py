from subprocess import Popen, PIPE, run
import os
import itertools
import string
import random

def mutate(s):
    r = random.choices(list(range(3)), weights=[0.8, 0.1, 0.1])[0]
    pos = random.randint(0, len(s) - 1)
    if r == 0:
        # Change random byte
        s[pos] = ord(random.choice(string.digits))
        return s
    elif r == 1:
        # Add random byte
        return s[:pos] + bytearray("".join(random.choices(string.digits, k=2)).encode()) + s[pos:]
    elif r == 2:
        # Delete random byte
        return s[:pos - 1] + s[pos:]

def main():
    inp = bytearray((input("sample here: ")).encode())
    for i in itertools.count():
        print(f"testing program time={i}")
        print(i)
        print(str(inp))
        a = run(["./fuzz"], stdout=PIPE, input=inp + b'\n', timeout=1)
        if a.returncode != 0:
            print("CRASHED")
            break;
        inp = mutate(inp)

if __name__ == "__main__":
    main()