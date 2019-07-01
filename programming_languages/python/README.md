# Style Guide for Python Code

## Content

### Naming Conventions (命名惯例)
#### Names to Avoid (避免以下命名)
```
- l, O, I (小写L，大写O和I)，不可单独用作字符变量名称，因为在一些字体中，这些字符无法与数字0或1区分开来
```
#### ASCII Compatibility (ASCII 兼容性)
```
- standard library (标准库) 中使用的标识符必须如PEP 3131中的policy section所述般与ASCII兼容
```
#### Package and Module Names (包和模块名)
```
- Modules names (模块名) 应当short and all-lowercased (简短且全小写). 如果使用下划线可以提高readability (可读性) ，那么下划线也是可以使用的
- Packages names (包名称) 也应该short and all-lowercased (简短且全小写)，不鼓励使用下划线
- 当用C或者C++编写的extension module (扩展模块) 有对应的提供更高级别接口的Python模块时， C/C++ 模块名会以下划线开头 (e.g. _socket)
```
#### Class Names (类名)
```
- 主要用 **CapWords** convention (首字母大写)
- 在class主要被调用且有对应的接口记录的情况下，class也可以使用函数的命名方式
- 注意，builtin names (内置名)是有单独的命名习惯的：大多数内置名都是single words (或two words 一起)， 而首字母大写(CapWords) 仅用于exception names (异常命名) 和builtin constants (内置常量) 
```
#### Type Variable Names (类型变量名)
- 
#### Exception Names (异常名)
#### Global Variable Names (全局变量名)
#### Function and Variable Names (函数和变量名)
#### Function and Method Arguments (函数与方法参数)
#### Method Names and Instance Variables (方法名与实例变量)
#### Constants (常量)
#### Designing for Inheritance (设计继承)



## References
Code standards in Python: https://www.python.org/dev/peps/pep-0008/
