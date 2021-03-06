from time import time
import contextlib

@contextlib.contextmanager
def howlong():
    try:
        start = time()
        yield ""
    finally:
        result = time() - start
        print(result)

def listgenerator(a):
    l = [l for l in range(a)]
    return l

if __name__ == "__main__":
    with howlong() as h:
        listgenerator(1231244)