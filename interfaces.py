import platform

version = platform.python_version_tuple()

if int(version[1]) >= 8:
    from typing import Protocol
else:
    print("Python version is less than 3.8")