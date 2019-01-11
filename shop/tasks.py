from celery import task
import time

@task(name='order')
def order_process(order):
    print ('Process order %s task' % order)
    for i in range(5):
        time.sleep(1)
        print(i)

