# Python

## Interpreter
- run code

### Compiler
- source code to byte code i.e. pyc files which are platform independent, low level, efficient, intermediate code and saves compilation time next time

### Virtual Machine
- read byte code line by line and execute and produce output

### Support Library
- builtin modules, functions, constants, types, exceptions, data types, file formats etc
- we can compile manually as below

# Code

## Compile
```
import py_compile
py_compile.compile("test.py")
```

## Run
```
python3 test.cpython-38.pyc
```

## Decompile
```
pip install uncompyle6
```
```
uncompyle6 test.cpython-38.pyc
```

## Disassemble
```
from dis import dis
dis(myfunc)
```