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

## numpy ndarray
> 一个多维数组对象
> 
NumPy的关键特性之一是它的n维数组对象(ndarray)，这是Python中用于大型数据集的快速、灵活的容器。
数组使我们能够使用类似于在标量元素之间进行等效操作的语法, 并且对整个数据块执行数学操作。

ndarray简单演示: [ndarray简单使用](ndarray简单使用.py)

>ndarray里面的所有元素必须是相同的类型
>每一个ndarray都有一个shape，表示每个维度大小的元组，以及一个dtype，描述ndarrray数据类型的对象

### 创建ndarray
[ndarray的创建](ndarray的创建)
创建数组最简单的方法是使用array函数
> numpy.array(\[sequence\])
它接受任何类似sequence的对象(list,tuple,bytes,range还有ndarray)，并生成一个包含数据的新NumPy数组。

除非显式指定(在ndarray的数据类型中讨论)，否则numpy.array尝试为它创建的数组推断一个默认数据类型(比如浮点数默认使用np.float64)。
数据类型存储在一个特殊的**dtype**元数据对象中;