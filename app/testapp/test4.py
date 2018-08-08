
import threading
import time
from werkzeug.local import LocalStack

#  Thread isolation object
#  AppCtx and  RequestCtx need to push to the localstack object
#  mul
stack = LocalStack()
stack.push(1)
print(type(stack.top))


def worker():
    print('new thread: ' + str(stack.top))
    stack.push(2)
    stack.top
    print('new thread: ' + str(stack.top))


new_t = threading.Thread(target=worker)
new_t.start()
time.sleep(1)

print('main thread: ' + str(stack.top))
