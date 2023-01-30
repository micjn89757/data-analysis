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
    # !sequence转换为ndarray, 以list为例
    # 一维list
    data1:list[float] = [6, 7.5, 8, 0, 1]
    narr1: NDArray[Shape["1, 5"], Float64] = np.array(data1)
    print(narr1)
    print(narr1.ndim)
    print(narr1.shape)
    print(narr1.dtype)

    # 二维list
    data2:list[list[int]] = [[1, 2, 3, 4], [5, 6, 7, 8]]
    narr2: NDArray[Shape["1, 5"], Float64] = np.array(data2)
    print(narr2)
    print(narr2.ndim)
    print(narr2.shape)
    print(narr2.dtype)
