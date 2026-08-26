import time
from functools import wraps

# decorators

# def my_logging(func):
#     import logging
#     logging.basicConfig(filename=f"{func.__name__}.log", level=logging.INFO)
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         logging.info(f"Running {func.__name__} with arguments {args} and keyword arguments {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper

# def my_timer(func):
#     import time
#     @wraps(func)
#     def wrapper_func(*args, **kwargs):
#         t1 = time.time()
#         t2 = time.time()- t1
#         print(f"This is a wrapper function and ran in {t2:.4f} sec")
#         return func(*args, **kwargs)
#     return wrapper_func


# @my_logging
# @my_timer


def prefix_decorator(prefix):
    def decorator_func(func):
        def wrapper_func(*args, **kwargs):
            print(prefix, "This is a wrapper function")
            return func(*args, **kwargs)
        return wrapper_func
    return decorator_func


@prefix_decorator("Hello")
def display_info(*args, **kwargs):
    print(f"my name is {args[0]} and I am {kwargs['age']} years old")
display_info("fiza", 21)

print(display_info)




# # class decorator_class(object):
# #     def __init__(self, func):
# #         self.func = func

# #     def __call__(self, *args, **kwargs):
# #          print("This is a wrapper class function")
# #          return self.func(*args, **kwargs)
    
    

# @decorator_func
# def display():
#     print("This is a decorator function")

# @decorator_func
# def display_info(*args, **kwargs):
#     print(f"my name is {args[0]} and I am {kwargs['age']} years old")


# # decorator = decorator_func(display)
# display()
# display_info("fiza", age=21)

# # closures

# def outer_func(msg):

#     """
#     A closure is a function that "remembers" variables
#     from the scope it was created in, even after that outer scope has finished running.
#     """
#     message = msg
#     t1 = time.time()
#     t2 = time.time()
#     print(f"Time taken to run outer_func: {t2-t1:.4f} sec")

#     def inner_func():
#         print(message)
#         print(f"Time taken to run inner_func: {t2-t1:.4f} sec")
#     return inner_func

# my_func = outer_func("hi")

# my_func()

