import platform

version = platform.python_version_tuple()

if int(version[1]) >= 8:
    from protocols import *
else:
    from datatypes import *