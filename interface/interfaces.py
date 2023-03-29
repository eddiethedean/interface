import platform

version = platform.python_version_tuple()

if int(version[1]) >= 8:
    from interface.protocols import *
else:
    from interface.datatypes import *