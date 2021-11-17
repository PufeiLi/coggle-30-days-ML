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

**实现：[见代码](./pytorch-tutorial/task2.py)。**

## **任务3：PyTorch全连接层原理和使用**

任务要点：全连接网络

- 步骤1：学习全连接网络原理，https://blog.csdn.net/xiaodong_11/article/details/82015456

- 步骤2：在pytorch中使用矩阵乘法实现全连接层

- 步骤3：在pytorch中使用nn.Linear层

**实现代码：[代码](./pytorch-tutorial/task3.py)**

## **任务4：PyTorch激活函数原理和使用**

任务要点：激活函数

- 步骤1：学习激活函数的原理，https://zhuanlan.zhihu.com/p/88429934

- 步骤2：在pytorch中手动实现上述激活函数

**实现代码：[代码](./pytorch-tutorial/task4.py)**

## **任务5：PyTorch卷积层原理和使用**

任务要点：卷积层

- 步骤1：理解卷积层的原理和具体使用

[https://blog.csdn.net/qq_37385726/article/details/81739179](https://blog.csdn.net/qq_37385726/article/details/81739179?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhY2Nlc3NfcmVzb3VyY2UiLCJleHAiOjE2MzcwNzAwOTUsImciOiJkdW1yc2V4VFJKa3FTZ0lDIiwiaWF0IjoxNjM3MDY5Nzk1LCJ1c2VySWQiOjczNzAwMjQ0fQ.CwZ8HGbf8SwdT--E9cwrvRVvWreIJV7x6g5r8a0iku4)

[https://www.cnblogs.com/zhangxiann/p/13584415.html](https://www.cnblogs.com/zhangxiann/p/13584415.html?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhY2Nlc3NfcmVzb3VyY2UiLCJleHAiOjE2MzcwNzAwOTUsImciOiJkdW1yc2V4VFJKa3FTZ0lDIiwiaWF0IjoxNjM3MDY5Nzk1LCJ1c2VySWQiOjczNzAwMjQ0fQ.CwZ8HGbf8SwdT--E9cwrvRVvWreIJV7x6g5r8a0iku4)

- 步骤2：计算下如下卷积层的参数量, [学习链接](https://blog.csdn.net/qq_25473787/article/details/100145842)

```python
nn.Conv2d(            
    in_channels=1,            
    out_channels=32,            
    kernel_size=5,            
    stride=1,            
    padding=2        
	)
```

卷积核的参数计算，一般的计算为：卷积核的参数个数：out_channel * (in_channel * keral_size * keral_size+bias)。因此该卷积层的参数量为 $32*(1*5*5+1)=832$

## **任务6：PyTorch常见的损失函数和优化器使用**

任务要点：损失函数、优化器

- 步骤1：学习损失函数的细节，[https://www.cnblogs.com/wanghui-garcia/p/10862733.html](https://www.cnblogs.com/wanghui-garcia/p/10862733.html?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhY2Nlc3NfcmVzb3VyY2UiLCJleHAiOjE2MzcwNzAwOTUsImciOiJkdW1yc2V4VFJKa3FTZ0lDIiwiaWF0IjoxNjM3MDY5Nzk1LCJ1c2VySWQiOjczNzAwMjQ0fQ.CwZ8HGbf8SwdT--E9cwrvRVvWreIJV7x6g5r8a0iku4)

- 步骤2：学习优化器的使用，[https://pytorch.org/docs/stable/optim.html](https://pytorch.org/docs/stable/optim.html?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhY2Nlc3NfcmVzb3VyY2UiLCJleHAiOjE2MzcwNzAwOTUsImciOiJkdW1yc2V4VFJKa3FTZ0lDIiwiaWF0IjoxNjM3MDY5Nzk1LCJ1c2VySWQiOjczNzAwMjQ0fQ.CwZ8HGbf8SwdT--E9cwrvRVvWreIJV7x6g5r8a0iku4)

- 步骤3：设置不同的优化器和学习率，重复任务2的回归过程

  - 损失函数MSE、优化器SGD、学习率0.1

  - 损失函数MSE、优化器SGD、学习率0.5

  - 损失函数MSE、优化器SGD、学习率0.01

**实现代码：[代码](./pytorch-tutorial/task6.py)**

## **任务7：PyTorch池化层和归一化层**

任务要点：池化层、归一化层

- 步骤1：使用pytroch代码实现2d pool中的mean-pooling、max-pooling

  - [https://pytorch.org/docs/stable/nn.html#pooling-layers](https://pytorch.org/docs/stable/nn.html#pooling-layers?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhY2Nlc3NfcmVzb3VyY2UiLCJleHAiOjE2MzcxMzExNDcsImciOiJkdW1yc2V4VFJKa3FTZ0lDIiwiaWF0IjoxNjM3MTMwODQ3LCJ1c2VySWQiOjczNzAwMjQ0fQ.nrc_p4SMZrq6qffXVA3aKqUJijRj1y8kIjleMt1ecBw)

  - [https://blog.csdn.net/shanglianlm/article/details/85313924](https://blog.csdn.net/shanglianlm/article/details/85313924?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhY2Nlc3NfcmVzb3VyY2UiLCJleHAiOjE2MzcxMzExNDcsImciOiJkdW1yc2V4VFJKa3FTZ0lDIiwiaWF0IjoxNjM3MTMwODQ3LCJ1c2VySWQiOjczNzAwMjQ0fQ.nrc_p4SMZrq6qffXVA3aKqUJijRj1y8kIjleMt1ecBw)

- 步骤2：学习归一化的原理，[https://blog.csdn.net/qq_23981335/article/details/106572171](https://blog.csdn.net/qq_23981335/article/details/106572171?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhY2Nlc3NfcmVzb3VyY2UiLCJleHAiOjE2MzcxMzExNDcsImciOiJkdW1yc2V4VFJKa3FTZ0lDIiwiaWF0IjoxNjM3MTMwODQ3LCJ1c2VySWQiOjczNzAwMjQ0fQ.nrc_p4SMZrq6qffXVA3aKqUJijRj1y8kIjleMt1ecBw)



