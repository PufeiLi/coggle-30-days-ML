# Coggle 30 Days of ML（21年11月）Pytorch与视觉竞赛入门

## **任务1：PyTorch张量计算与Numpy的转换**

任务要点：Pytorch基础使用、张量计算

- 步骤1：配置本地Notebook环境，或使用[天池DSW](https://dsw-dev.data.aliyun.com/#/)

- 步骤2：学习Pytorch的基础语法，并成功执行以下代码

- [基础pytorch教程](https://zhuanlan.zhihu.com/p/25572330)

- [官方教程](https://pytorch.org/tutorials/beginner/basics/intro.html)

```python
c = np.ones((3,3))
d = torch.from_numpy(c)  #numpy 转tensor
"""
c: [[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
d: tensor([[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]], dtype=torch.float64)
"""
```

## **任务2：梯度计算和梯度下降过程**

任务要点：Pytorch梯度计算、随机梯度下降

- 步骤1：学习自动求梯度原理，https://pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html

- 步骤2：学习随机梯度下降原理，https://www.cnblogs.com/BYRans/p/4700202.html

- 步骤3：

  - 使用numpy创建一个[y=10*x+4+noise(0,1)](#)的数据，其中x是0到100的范围，以0.01进行等差数列

  - 使用pytroch定义w和b，并使用随机梯度下降，完成回归拟合。

实现：[见代码](./pytorch-tutorial/task2.py)。

## **任务3：PyTorch全连接层原理和使用**

任务要点：全连接网络

- 步骤1：学习全连接网络原理，https://blog.csdn.net/xiaodong_11/article/details/82015456

- 步骤2：在pytorch中使用矩阵乘法实现全连接层

- 步骤3：在pytorch中使用nn.Linear层

实现代码：[代码](./pytorch-tutorial/task3.py)

## **任务4：PyTorch激活函数原理和使用**

任务要点：激活函数

- 步骤1：学习激活函数的原理，https://zhuanlan.zhihu.com/p/88429934

- 步骤2：在pytorch中手动实现上述激活函数

