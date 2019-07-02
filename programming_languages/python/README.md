# Style Guide for Python Code

## Content

### Naming Conventions (命名惯例)
#### Names to Avoid (避免以下命名)
```
- l, O, I (小写L，大写O和I)，不可单独用作字符变量名称，因为在一些字体中，这些字符无法与数字0或1区分开来
```
#### ASCII Compatibility (ASCII 兼容性)
```
- standard library(标准库) 中使用的标识符必须如PEP 3131中的policy section所述般与ASCII兼容
```
#### Package and Module Names (包和模块名)
```
- Modules names(模块名) 应当short and all-lowercased(简短且全小写). 如果使用下划线可以提高readability(可读性) ，那么下划线也是可以使用的
- Packages names(包名称) 也应该short and all-lowercased(简短且全小写)，不鼓励使用下划线
- 当用C或者C++编写的extension module(扩展模块) 有对应的提供更高级别接口的Python模块时， C/C++ 模块名会以下划线开头(e.g. _socket)
```
#### Class Names (类名)
```
- 主要用 **CapWords** convention(首字母大写)
- 在class主要被调用且有对应的接口记录的情况下，class也可以使用函数的命名方式
- 注意，builtin names(内置名)是有单独的命名习惯的：大多数内置名都是single words(或two words 一起)， 而首字母大写(CapWords) 仅用于exception names(异常命名)和builtin constants(内置常量) 
```
#### Type Variable Names (类型变量名)
```
- PEP 484中介绍的类型变量名一般使用简短的CapWords(首字母大写)的命名，如：T, AnyStr, Num。若是在声明covariant(协变)或者contravariant(逆变)时，建议加上 _co 或 _contra 作为后缀
```
#### Exception Names (异常名)
```
- 因为Exceptions(异常)应该是类型，因此类名命名惯例在这里是适用的，但是在异常名后面应该加上‘Error’作为后缀(当异常情况是error的时候)
```
#### Global Variable Names (全局变量名)
```
- (这里提及的都是只用在一个module里的变量)，命名惯例跟函数命名方式几乎一致
- 需要通过 from M import *调用的modules (模块)应当使用 __all__ 机制来防止输出全局变量，或者用旧惯例中的用下划线对全局变量名加上前缀
```
#### Function and Variable Names (函数和变量名)
```
- 函数名应当小写，单词之间以下划线分隔以提高可读性
- 变量名遵循与函数名相同的命名惯例
- 类似于mixedCase这样的命名，只能用于它是主流命名形式的地方(e.g. threading.py)以保持向后兼容性
```
#### Function and Method Arguments (函数与方法参数)
```
- 总是使用self作为实例方法中的第一个参数
- 总是使用cls作为类方法的第一个参数
- 如果一个函数的参数名与reserved keyword (保留关键字)冲突，比起使用缩写或者改动拼写，通常在后面附加单个下划线会更好，因为class_比clss更好(或许最好的方式是用同义词来避免这样的clash--冲突)
```
#### Method Names and Instance Variables (方法名与实例变量)
```
- 用函数命名的命名规则，字母小写，单词之间以下划线间隔以提高可读性
- 仅对non-public methods(非公有方法)及instance variables(实例变量)命名时使用前导下划线
- 为避免与子类发生命名冲突，使用两个前导下划线来调用Python的名称修改规则
```
#### Constants (常量)
```
- 常量通常是在module级定义的，定义时，全大写，单词之间以下划线隔开，如 MAX_OVERFLOW 和 TOTAL
```
#### Designing for Inheritance (设计继承)
```
- 总是对‘类的方法和实例变量(属性)应该是公有的还是私有的’是确定的，如果不确定，就选择私有，在后续工作中，将私有的变成公有的比将公有的属性变成私有的容易
- Public attributes(公共属性)需要开发者保证避免向后不兼容的更改，non-public attributes(私有属性)是指不打算提供给第三方使用的属性，对于私有属性，不需要保证私有属性不会更改或者不会被删除
```

## References
Code standards in Python: https://www.python.org/dev/peps/pep-0008/
