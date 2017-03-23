import threading
# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student#local_school.student为线程的局部变量
    teacher = local_school.teacher
    print('hello, %s and %s (in %s)\n'%(std, teacher, threading.current_thread().name))

def process_thread(name,tcher):
    # 绑定ThreadLocal的student:
    local_school.student=name
    local_school.teacher=tcher
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice','Mike'), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob','Mikee'), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
