#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 @FileName  :task3.py
 @Time      :2021/11/15 21:48
 @Author    :LPF
"""
import torch
import matplotlib.pyplot as plt
import torch.nn.functional as F


class FcLayers(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(FcLayers, self).__init__()
        # torch.nn.Parameter
        self.hidden_w = torch.nn.Parameter(torch.randn(n_feature, n_hidden), requires_grad=True)
        self.predict = torch.nn.Parameter(torch.randn(n_hidden, n_output), requires_grad=True)

    def forward(self, x):
        x = F.relu(torch.mm(x, self.hidden_w))
        # x = torch.mm(x, self.hidden_w)
        x = torch.mm(x, self.predict)
        return x


class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)  # hidden layer
        self.predict = torch.nn.Linear(n_hidden, n_output)  # output layer

    def forward(self, x):
        # x = self.hidden(x)  #
        x = F.relu(self.hidden(x))  # activation function for hidden layer
        x = self.predict(x)  # linear output
        return x


if __name__ == "__main__":
    torch.manual_seed(1)

    x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  # x data (tensor), shape=(100, 1)
    y = x.pow(2) + 0.2 * torch.rand(x.size())  # noisy y data (tensor), shape=(100, 1)

    # net = Net(n_feature=1, n_hidden=10, n_output=1)  # define the network
    net = FcLayers(1, 10, 1)
    optimizer = torch.optim.SGD(net.parameters(), lr=0.001)
    loss_func = torch.nn.MSELoss()  # this is for regression mean squared loss

    plt.ion()  # something about plotting

    for t in range(1000):
        prediction = net(x)  # input x and predict based on x

        loss = loss_func(prediction, y)  # must be (1. nn output, 2. target)

        optimizer.zero_grad()  # clear gradients for next train
        loss.backward()  # backpropagation, compute gradients
        optimizer.step()  # apply gradients

        if t % 5 == 0:
            # plot and show learning process
            plt.cla()
            plt.scatter(x.data.numpy(), y.data.numpy())
            plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
            plt.text(0.5, 0, 'Loss=%.4f' % loss.data.numpy(), fontdict={'size': 20, 'color': 'red'})
            plt.pause(0.01)
            print(loss.data)
    plt.ioff()
    plt.show()
    run_code = 0
