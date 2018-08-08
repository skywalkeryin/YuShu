import threading
import time

from werkzeug.local import Local


class A:
    b = 1


# obj = A()

obj = Local()
obj.b = 1

def worker():
    obj.b = 2


new_t = threading.Thread(target=worker)
new_t.start()
time.sleep(1)

print(obj.b)
