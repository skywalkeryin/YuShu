
import threading
import time
from werkzeug.local import LocalStack

#  Thread isolation object
#  AppCtx and  RequestCtx need to push to the localstack object
#  mul
#  线程是进程的一部分， 进程分配资源，线程 利用CPU执行代码（线程不能被分配和拥有资源， 但是可以访问进程的资源，因此
#  切换线程更加的快速。）

# 多线程是更加充分利用cpu资源， 是异步编程一种
# 单核CPU 同一时间只允许一个线程执行代码， 意义？
# 多核CPU， 可以让不同的核 执行不同的线程， 可以并行执行，充分利用CPU的性能。
# Python 没有办法利用多核CPU优势
# Python 有 GIL 全局解释器锁  同一时刻，只能在一个核上执行一个线程
# 锁： 为了线程安全

# 进程 管理资源， 一个进程多个线程  线程 共享资源，
#  线程 不安全， 例子： 主线程 A = 3, 线程2

# 只有拿到锁的线程 才能执行， 其他线程不执行

# 语言的锁 1: 细粒的锁  语言上加的  2.粗粒度的锁 解释器  一定程度保证的线程安全
#  a+=1  解释器 bytecode  可能多段， 如果执行其中一段（没有执行完） bytecode 线程可能被挂起， 执行里一个线程，
# 可能造成线程不安全。

# python  解释器 cPython（有GIL） jpython 没有
# 可以 多进程

# python多线程是不是鸡肋
# 10 线程 非常严重依赖CPU计算  CPU密集程序（如视频解码）
# 大多是 IO密集型的程序  查询数据库， 请求网络资源，读写文件

# IO密集型 大多是 等待 时间， 可以把时间让给其他线程

# Flask webK框架
# 线程隔离 原理 字典 保存数据
# 操作数据
# Local


class a:
    pass

my_obj = a()


a.b = 3

print(a.b)



def worker():
    print('')
    t = threading.current_thread()
    time.sleep(10)
    print(t.getName())

t = threading.current_thread()
print(t.getName())

new_t = threading.Thread(target=worker)
new_t.start()


# stack = LocalStack()
# stack.push(1)
# print(type(stack.top))


# def worker():
#     print('new thread: ' + str(stack.top))
#     stack.push(2)
#     stack.top
#     print('new thread: ' + str(stack.top))


# new_t = threading.Thread(target=worker)
# new_t.start()
# time.sleep(1)

#print('main thread: ' + str(stack.top))
