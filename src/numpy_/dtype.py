"""
ndarray数据类型dtype
"""
from nptyping import (
    NDArray,
    Float64,
    Shape,
    Int32,
    Int64
)

import numpy as np 

if __name__ == "__main__":
    # !设置ndarray的dtype
    arr1:NDArray[Shape["1, 3"], Float64] = np.array([1, 2, 3], dtype=Float64)

    arr2:NDArray[Shape["1, 3"], Int32] = np.array([1, 2, 3], dtype=Int32)

    # print(arr1.dtype)
    # print(arr2.dtype)

    # !改变ndarray的dtype
    arr3:NDArray[Shape["1, 5"], Int64] = np.array([1, 2, 3, 4 ,5], dtype=Int64)
    # print(arr3.dtype)

    float_arr3:NDArray[Shape["1, 5"], Float64] = arr3.astype(Float64)

    # print(float_arr3)
    # print(float_arr3.dtype)

    # !你也可以使用另一个数组的dtype属性
    int_ndarr:NDArray[Shape["1, 10"], Int32] = np.arange(10, dtype=Int32)

    calibers = np.arange(0, 30, 5, dtype=Float64)

    int_ndarr.astype(calibers.dtype)

    print(int_ndarr.dtype)