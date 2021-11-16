#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 @FileName  :task4.py
 @Time      :2021/11/16 21:35
 @Author    :LPF
"""
import torch


def elu(x, alpha=1.0):
    # temp = alpha * (torch.exp(x) - 1)
    return torch.where(x > 0, x, 0) + torch.where(alpha * (torch.exp(x) - 1) > 0, 0, alpha * (torch.exp(x) - 1))


def leaky_relu(x, negative_slope=0.01):
    return torch.where(x > 0, x, 0) + negative_slope * torch.where(x < 0, x, 0)


def p_relu(x, a=0.25):
    return torch.where(x > 0, x, 0) + a * torch.where(x < 0, x, 0)


def relu(x):
    return torch.where(x > 0, x, 0)


def relu6(x):
    return torch.where(torch.where(x > 0, x, 0) < 6, torch.where(x > 0, x, 0), 6)


def selu(x):
    alpha = 1.6732632423543772848170429916717
    scale = 1.0507009873554804934193349852946
    return scale * torch.where(x > 0, x, 0) + torch.where(alpha * (torch.exp(x) - 1) > 0, 0, alpha * (torch.exp(x) - 1))


def celu(x, alpha=1.0):
    return torch.where(x > 0, x, 0) + torch.where(alpha * (torch.exp(x / alpha) - 1) > 0, 0,
                                                  alpha * (torch.exp(x / alpha) - 1))


def sigmoid(x):
    return 1 / (1 + torch.exp(-x))


def log_sigmoid(x):
    return torch.log(1 / (1 + torch.exp(-x)))


def tanh(x):
    return (torch.exp(x) - torch.exp(-x)) / (torch.exp(x) + torch.exp(-x))


def tanh_shrink(x):
    return x - tanh(x)


def soft_plus(x, beta=1):
    return (1 / beta) * torch.log(1 + torch.exp(beta * x))


def soft_shrink(x, lambd=0.5):
    return torch.where(x > lambd, x - lambd, torch.where(x < -lambd, x + lambd, 0))


if __name__ == "__main__":
    run_code = 0
