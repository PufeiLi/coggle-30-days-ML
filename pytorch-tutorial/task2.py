#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 @FileName  :task2.py
 @Time      :2021/11/15 16:29
 @Author    :LPF
"""
import torch
import numpy as np
import matplotlib.pyplot as plt
import random

torch.manual_seed(1)

# --------------------step 1 data------------------
x1 = np.arange(0, 100, 0.01)
y1 = 10 * x1 + random.random()
x = torch.from_numpy(x1).float()  # input tensor
y = torch.from_numpy(y1).float()  # expected output
# ---------------------step 2 model-----------------
w = torch.randn(1, requires_grad=True)
b = torch.ones(1, requires_grad=True)

plt.ion()  # something about plotting
for epoch in range(1000):
    # forward
    y_pred = torch.mul(x, w) + b
    # y_pred = torch.add(torch.mul(w, x), b)
    # loss
    loss = 0.5 * torch.mean(torch.pow(y_pred - y, 2))  # MSE loss
    # backward
    loss.backward()

    # # optimizer
    # w.data.sub_(lr * w.grad)
    # b.data.sub_(lr * b.grad)
    # # 梯度清零
    # w.grad.zero_()
    # b.grad.zero_()
    # exit()
    w.data = w.data - 0.00001 * w.grad.data
    b.data = b.data - 0.00001 * b.grad.data
    w.grad.zero_()
    b.grad.zero_()
    print(loss.data)

    if epoch % 20 == 0:
        plt.cla()
        plt.scatter(x.detach().numpy(), y.detach().numpy())
        plt.plot(x.detach().numpy(), y_pred.detach().numpy().reshape(10000, ), 'r-', lw=6)
        plt.text(2, 22, 'Loss = %.5f' % loss.detach().numpy(), fontdict={'size': 20, 'color': 'red'})
        plt.pause(0.2)
        plt.show()
plt.ioff()
plt.show()

if __name__ == '__main__':

    code = 0
