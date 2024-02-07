import torch

def r2(y_true, y_pred):
    return 1 - torch.sum((y_true - y_pred) ** 2) / torch.sum((y_true - torch.mean(y_pred)) ** 2)


def explained_variance(y_true, y_pred):
    return 1 - torch.var(y_true - y_pred) / torch.var(y_true)

def smape(y_true, y_pred):
    return 2.0 * torch.mean(torch.abs(y_pred - y_true) / (torch.abs(y_pred) + torch.abs(y_true))) * 100

def accuracy(y_true,y_pred):

    return 1 - torch.linalg.norm(y_true - y_pred) / torch.linalg.norm(y_true)
