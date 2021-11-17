#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 @FileName  :task6.py
 @Time      :2021/11/17 13:22
 @Author    :LPF
"""
import torch
import numpy as np
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import random


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.w = nn.Parameter(torch.tensor(9.), requires_grad=True)
        self.b = nn.Parameter(torch.tensor(0.5), requires_grad=True)

    def forward(self, x):
        return torch.mul(x, self.w) + self.b


if __name__ == "__main__":
    torch.manual_seed(1)

    # --------------------step 1 data------------------
    x1 = np.arange(0, 100, 0.01)
    y1 = 10 * x1 + random.random()
    input_x = torch.from_numpy(x1).float()  # input tensor
    target = torch.from_numpy(y1).float()  # expected output
    # ---------------------step 2 model-----------------
    my_model = Net()

    criterion = nn.MSELoss()
    optimizer1 = optim.SGD(my_model.parameters(), lr=0.0001, momentum=0.9)
    # lr = 0.5,0.1,0.01 区分不大，当lr以10的倍数改变时区别很大

    for epoch in range(200):
        optimizer1.zero_grad()
        y_pred = my_model(input_x)
        loss = criterion(y_pred, target)
        loss.backward()
        optimizer1.step()
        print(loss.data)

    run_code = 0
