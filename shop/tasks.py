from celery import task

@task()
def order_process():
    print ('Process order task')

