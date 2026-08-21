from contextlib import contextmanager
import time
import os


import contextlib

@contextmanager
def ignore_errors(*error_types):
    try:
        yield
    except error_types as e:
        print(f"Suppressed: {type(e).__name__} - {e}") 

# with ignore_errors(ZeroDivisionError, FileNotFoundError):
#     1/0
#     print("zero division error not occurred") 

with contextlib.suppress(FileNotFoundError):
    print("Trying to open a non-existent file...")
    open("non_existent_file.txt", "r")
   

# with ignore_errors( FileNotFoundError):
#     print("Trying to open a non-existent file...")
#     open("non_existent_file.txt", "r")

# class Timer():
#     def __enter__(self):
#         self.start = time.time()
#         return self
#     def __exit__(self, exc_type, exc_value, traceback):
#         self = time.time() - self.start
#         print(f"Time taken: {self:.4f} sec")

# with Timer() as t:
#     time.sleep(1)
#     raise ValueError("boom")

# def change_dir(destination):
#     try:
#         cwd = os.getcwd()
#         os.chdir(destination)
#         yield
#     finally:
#         os.chdir(cwd)

# with change_dir("D:\Python\python\modules"):
#     print(os.listdir())

# with change_dir("D:\Python\python\modules2"):
#     print(os.listdir())

# @contextmanager
# def Open_file(filename, mode):
#     try:
#         f = open(filename, mode)
#         yield f
#     finally:
#         f.close()

# with Open_file("sample.txt", "w") as f:
#     f.write('Fiza')
#     1/0

# print(f.closed)


# class Open_file():
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode

#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exec_type, exec_value, traceback):
#         self.file.close()
#         try:
#             if exec_type is ZeroDivisionError:
#                 print(f"Error occurred while closing the file: {exec_value}")
#                 return True
#         except Exception as e:
#             return False
# with Open_file("sample.txt", "w") as f:
#     f.write('Testing')
#     1/0

# print(f.closed)