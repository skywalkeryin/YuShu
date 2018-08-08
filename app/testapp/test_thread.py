

import threading


def worker():
    print('i am new thread')
    t = threading.current_thread()
    print(t.getName())


t = threading.current_thread()
print(t.getName())


new_t = threading.Thread(target=worker)
new_t.start()

new_t1 = threading.Thread(target=worker)
new_t1.start()