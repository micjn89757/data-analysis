"""
ndarray的创建 
"""
import numpy as np 
from nptyping import (
    NDArray,
    Shape,
    Float64
)

if __name__ == "__main__":
    # !np.array([sequences])
    # !sequence转换为ndarray, 以list为例
    # 一维list
    data1:list[float] = [6, 7.5, 8, 0, 1]
    narr1: NDArray[Shape["1, 5"], Float64] = np.array(data1)
    # print(narr1)
    # print(narr1.ndim)
    # print(narr1.shape)
    # print(narr1.dtype)

    # 二维list
    data2:list[list[int]] = [[1, 2, 3, 4], [5, 6, 7, 8]]
    narr2: NDArray[Shape["1, 5"], Float64] = np.array(data2)
    # print(narr2)
    # print(narr2.ndim)
    # print(narr2.shape)
    # print(narr2.dtype)


    # !np.zeros，创建内部元素都为0的ndarray 
    # 一维ndarray
    # print(np.zeros(10))
    # 二维三行六列ndarray
    # print(np.zeros((3, 6)))

    # !np.zeros_like
    # 返回形状与np.arange(10)相同的zeros ndarray
    # print(np.zeros_like(np.arange(10)))
    # 规定生成的shape
    # print(np.zeros_like(np.arange(10), shape=(2, 5)))


    # !np.empty，创建为填充元素的ndarray，可能是内存的垃圾值
    # 参数和zeros相同
    # print(np.empty((2, 3, 2)))

    # !np.arange
    # numpy版本的Python range 
    # 三个参数:起始值，终止值，(前闭后开区间)，步长
    # print(np.arange(0, 10, 2))
    # 一个参数:终止值, 起始值默认为0，步长默认为1
    # print(np.arange(10))

    # !np.ones 使用1来填充ndarray，用法与zeros相同
    # print(np.ones((2, 3)))
    
    # !np.full shape是(2, 3), 填充值是6
    # print(np.full((2, 3), 6))


