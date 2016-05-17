#-*- encoding: gb2312 -*-
import threadingDemo
import time

class Test(threadingDemo.Thread):
    def __init__(self, num):
        threadingDemo.Thread.__init__(self)
        self._run_num = num

    def run(self):
        global count, mutex
        threadname = threadingDemo.currentThread().getName()

        for x in xrange(0, int(self._run_num)):
            mutex.acquire()
            count = count + 1
            mutex.release()
            print threadname, x, count
            time.sleep(1)

if __name__ == '__main__':
    global count, mutex
    threads = []
    num = 4
    count = 1
    # ������
    mutex = threadingDemo.Lock()
    # �����̶߳���
    for x in xrange(0, num):
        threads.append(Test(10))
    # �����߳�
    for t in threads:
        t.start()
    # �ȴ����߳̽���
    for t in threads:
        t.join()