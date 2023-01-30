# numpy 介绍
NumPy是Numerical Python的缩写，是Python中用于数值计算的最重要的基础包之一。
许多提供科学功能的计算包使用NumPy的数组对象作为数据交换的标准接口通用语言之一。
我所介绍的关于NumPy的许多知识也可以转移到pandas上。

## numpy的一些特性简介
- ndarray，一种高效的多维数组，提供快速的面向数组的算术操作和灵活的广播功能
- 有用于对整个数据数组进行快速操作的数学函数，而无需编写循环
- 有用于将数组数据读取/写入磁盘和使用内存映射文件的工具
- 线性代数、随机数生成和傅里叶变换功能
- C API，用于连接NumPy与用C、c++或FORTRAN编写的库

## nptyping: type hints for numpy and pandas.DataFrame
这个type hints包，静态类型检查不是很适用，mypy也检查不出来，但是用来标识类型还是可以的
包里面对np.int等类型进行了包装

## numpy ndarray
> 一个多维数组对象

NumPy的关键特性之一是它的n维数组对象(ndarray)，这是Python中用于大型数据集的快速、灵活的容器。
数组使我们能够使用类似于在标量元素之间进行等效操作的语法, 并且对整个数据块执行数学操作。

ndarray简单演示: [ndarray简单使用](ndarray简单使用.py)

>ndarray里面的所有元素必须是相同的类型
>每一个ndarray都有一个**shape**，表示每个维度大小的元组，以及一个**dtype**，描述ndarrray数据类型的对象
>如果没有指定数据类型，在许多情况下将是float64

### 创建ndarray
[ndarray的创建](ndarray的创建)
> 参数只列出常用的，其他可以查看docs

1. 创建数组最简单的方法是使用array函数,np.array
>numpy.array(\[sequence\])，它接受任何类似sequence的对象(list,tuple,bytes,range还有ndarray)，并生成一个包含数据的新NumPy数组。

除非显式指定(在ndarray的数据类型中讨论)，否则numpy.array会尝试为它创建的数组推断一个默认数据类型(默认使用np.float64)。
数据类型存储在一个特殊的**dtype**元数据对象中;
除了numpy.array,还有许多其他函数用于创建新数组。

2. numpy.zeros(\[设置几行几列, 高维情况传递一个元组，一维的情况可以只传递一个数值\])
>创建一个元素全都是0的ndarray
>numpy.zeros_like 参数接受另一个array，并生成一个具有相同形状和数据类型的zeros数组

3. numpy.empty(\[设置几行几列, 高维情况传递一个元组，一维的情况可以只传递一个数值\])
>创建数组时不将其值初始化为任何特定值，实际上就是返回未初始化的内存块，可能会包含非零的垃圾值，只有在打算用数据填充新数组时，才应该使用此函数。
>numpys.empty_like 和zeros_like原理相同

4. numpy.arrange(\[设置几行几列, 高维情况传递一个元组，一维的情况可以只传递一个数值\])
> 和python内置的range一样的用法

5. numpy.full(\[设置几行几列, 高维情况传递一个元组，一维的情况可以只传递一个数值\], \[填充值\])
> 生成生成给定形状和数据类型的数组，所有值都设置为指定的“填充值”
> numpy.full_like和zeros_like原理相同

其他一些常用的ndarray创建方法[table 4.1](https://wesmckinney.com/book/numpy-basics.html#tbl-table_array_ctor)

### ndarray的类型
数据类型或dtype是一个特殊的对象，包含ndarray需要将内存块解释为特定类型的数据的信息(或元数据，关于数据的数据)

数据类型是NumPy与来自其他系统的数据交互的灵活性的来源。

在大多数情况下，它们提供了直接到底层磁盘或内存表示的映射，这使得将二进制数据流读写到磁盘并连接到用C或FORTRAN等低级语言编写的代码成为可能。

数值数据类型以同样的方式命名:类型名称，如float或int，后面跟着一个数字，表示每个元素的位数。

一个标准的双精度浮点值(Python的float对象中底层使用的值)占用8个字节或64位。
因此，这种类型在NumPy中称为float64。

有关NumPy支持的数据类型的完整列表，请参见[table 4.2](https://wesmckinney.com/book/numpy-basics.html#tbl-table_array_dtypes)。

还有一些简写类型代码字符串可用于引用dtype, 比如dtype=np.int64 写为dtype="i8"

可以使用**ndarray的astype方法**显式地将数组从一种数据类型转换或强制转换为另一种数据类型

如果你有一个表示数字的字符串数组，你可以使用astype将它们转换为数字形式
>使用numpy.string_时请谨慎,因为NumPy中的字符串数据是固定大小的，可能会在没有警告的情况下截断输入。
>Pandas在非数值数据上有更直观的开箱即用行为。
>调用astype总是创建一个新数组(数据的副本)，即使新数据类型与旧数据类型相同

如果由于某种原因强制转换失败(比如字符串不能转换为float64)，将引发ValueError。

一个ndarray还可以使用另一个ndarray的dtype属性


### ndarray的计算


