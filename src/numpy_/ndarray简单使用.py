"""
ndarray的简单使用

"""

import numpy as np;
from nptyping import (
    NDArray, 
    Shape,
    Int64,
    Double,
    Float64,
    InvalidShapeError
)


if __name__ == "__main__":
    # 创建一个ndarray
    data:NDArray[Shape["2, 3"], Float64] = np.array([[1.5, -0.1, 3], [0, -3, 6.5]])


    print(data)

    # 所有元素都*10
    print(data * 10)
    # 两个矩阵的元素对应相加
    print(data + data)

    # data的维度: 一维，二维，三维
    print(data.ndim)
    # data的形状
    print(data.shape)
    # data内部元素的数据类型
    print(data.dtype)