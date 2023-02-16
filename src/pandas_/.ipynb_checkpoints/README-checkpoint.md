# Pandas 
> 学习和练习的内容来自[使用python进行数据分析(第三版)](https://wesmckinney.com/book/pandas-basics.html)

## 基本属性
- DataFrame的一列一般都是同一种数据类型，使用.T进行转置的时候可能会导致数据类型不正确
- DataFrame的一列和一行在进行获取时都是Series对象

## 构造器
基本的四个参数
pandas.DataFrame(
    data=,
    index=,
    columns=,
    copy=
)

## 对DataFrame进行选择和数据过滤
> 因为筛选出来的是一个视图，可以对选择出来的数据进行赋值修改

Series和DataFrame可以通过Series/DataFrame\[整数/索引名/start:end(左闭右开)/索引序列/条件表达式\]进行索引
> 不能在没有设置非整数索引的情况下使用Series/DataFrame\[整数\]进行索引

DataFrame\[索引名\]和DataFrame\[序列\]选择的是列

DataFrame\[start:end\]切片的是行
DataFrame\[DataFrame[列] > 5 等条件表达式\]筛选的是满足条件的行

DataFrame > 5等条件表达式会查看表中每一个值是否满足表达式并返回bool的DataFrame



### **使用loc和iloc对DataFrame进行筛选**(推荐)
筛选的首选方法是使用loc和iloc（可以避免很多整数索引的陷阱）, 返回筛选后的DataFrame

- loc
>loc只对标签进行索引，也就是现在的DataFrame的index和columns是什么就按照什么索引，比如不能又通过整数坐标又通过现有索引进行索引

loc\[标签\]筛选的是行
loc\[序列\]筛选的是行
loc\[DataFrame[列] > 5等条件表达式\] 筛选满足条件的行
loc\[start : end\]切片筛选的是行
>注意loc\[start:end\]是左闭右闭区间


loc[行,列]通过行列进行筛选，行列可以使用切片、序列或单个标签

- iloc
> 只能通过整数进行索引, iloc不能在里面使用条件表达式

iloc\[整数\]筛选的是行
iloc\[整数序列\]筛选的是行
iloc\[start:end\]切片筛选的是行
iloc\[行，列\]通过行列进行筛选，行列可以使用切片、整数序列或单个整数

### 链式索引的陷阱
上述的方式都可以进行链式索引筛选\[\]\[\]...
但是在链式索引筛选后进行赋值可能会出现问题，尽量使用单个loc和iloc代替
新版本修复了这个问题




## 索引

### 索引对象
**索引对象是不可变的，不能被用户修改**

- pd.DataFrame构造器都有index参数和columns参数, 可以传入行标和列标
> 如果对构造对象填充的index和columns参数如果不是和原索引是同一类型的数据可以进行覆盖，覆盖必须从头开始全部覆盖
> 如果构造对象原本行列索引和传入的索引是同一个类型的，则传递的index和columns不能覆盖，只能控制显示，原本没有的行列为NaN

- pd.Index(\[列表等\])构造器可以单独创建一个索引对象，可以作为Series和Dataframe的参数，索引里面可以包含重复的labels

- pd.index对象是行索引的组合
> 可以通过 行索引 in dataframe.index 判断列名是否存在

- pd.columns对象是列索引的组合
> 可以通过 列索引 in dataframe.columns 判断行索引是否存在

- index和columns都有.name属性可以设置其名称

- Index索引对象是可遍历的

Index索引对象有很多方法,查看[列表](https://wesmckinney.com/book/pandas-basics.html#tbl-table_index_methods)

#### 重建索引
Series通过reindex方法可以重建索引
DataFrame通过reindex方法可以同时也可以单独重建行列索引，如果值传递一个序列则会重索引结果中的行
> 重建索引的规则和pd.DataFrame构造器中的相同

reindex有index和columns参数可以设置行列索引

reindex也传入一个序列，然后通过设置axis="columns"或"index"指定要索引的是行还是列

**reindex返回的是重建索引后的DataFrame**，对于参数传入的索引序列如果原表不存在默认则用NaN填充(使用method和fill_value参数可以设置如何填充)

更多参数详见[列表](https://wesmckinney.com/book/pandas-basics.html#tbl-table_reindex_function)


## 删除记录和列
使用del DataFrame\[列索引\]直接在原DataFrame上删除一列, 无返回
使用DataFrame/Series.drop(参数和重建索引的参数基本相同)删除列或行, 并返回删除后的DataFrame

