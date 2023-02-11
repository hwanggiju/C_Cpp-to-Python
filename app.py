# -*- coding: utf-8 -*-
import ctypes
import platform                         # 파이썬 아키텍처를 확인하기 위한 모듈

print(platform.architecture())          # 파이썬 아키텍처 출력

if 'Windows' == platform.system() :     # 윈도우 운영체제에서 c 모듈 로드
    path = 'C:/Users/qltjz/source/repos/Dll1/x64/Debug/Dll1.dll'
    c_module = ctypes.windll.LoadLibrary(path)
elif 'Linux' == platform.system() :     # 리눅스 운영체제에서 c 모듈 로드
    path = "./libc_module.so"
    c_module = ctypes.cdll.LoadLibrary(path)
else :
    raise OSError()

print(c_module)

stream = c_module.stream

stream