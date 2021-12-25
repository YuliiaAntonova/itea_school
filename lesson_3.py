from time import time


class DecorTimeCrit:
    def __init__(self, critical_time):
        self.critical_time = critical_time

    @staticmethod
    def benchmark(func, critical_time: float):
        def helper(*args, **kwargs):
            start = time()
            res = func(*args, **kwargs)
            elapsed_time = time() - start

            if elapsed_time >= critical_time:
                print(f'WARNING! {func.__name__} slow. Time = {elapsed_time} sec.')

            return res

        return helper

    def __call__(self, cls):
        def wrapper(*args, **kwargs):
            for attribute in dir(cls):
                if attribute.startswith('__'):
                    continue

                val_attr = getattr(cls, attribute)

                if callable(val_attr):
                    decor_method = self.benchmark(val_attr, self.critical_time)
                    setattr(cls, attribute, decor_method)
            return cls(*args, **kwargs)

        return wrapper


@DecorTimeCrit(critical_time=0.0000005)
class Employee:

    def __init__(self, name, salary, emp_count=0):
        self.name = name
        self.salary = salary
        self.emp_count = emp_count + 1

    def display_employee(self):
        print(f'Имя: {self.name}. Зарплата: {self.salary}')


emp1 = Employee("Андрей", 2000)
emp2 = Employee("Мария", 5000)
emp1.display_employee()
emp2.display_employee()
