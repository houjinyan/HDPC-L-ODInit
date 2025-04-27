import numpy as np
import torch
import torch.nn as nn

def r2(y_true, y_pred):
    return 1 - torch.sum((y_true - y_pred) ** 2) / torch.sum((y_true - torch.mean(y_pred)) ** 2)

def rmse(y_true,y_pred):
    criterion = nn.MSELoss(reduction="mean")
    return torch.sqrt(criterion(y_pred,y_true))

def explained_variance(y_true, y_pred):
    return 1 - torch.var(y_true - y_pred) / torch.var(y_true)

def smape(y_true, y_pred):
    return 2.0 * torch.mean(torch.abs(y_pred - y_true) / (torch.abs(y_pred) + torch.abs(y_true))) * 100

def accuracy(y_true,y_pred):

    return 1 - torch.linalg.norm(y_true - y_pred) / torch.linalg.norm(y_true)

def mae_torch(pred, true, mask_value=None):
    # if mask_value != None:
    #     mask = torch.gt(true, mask_value)
    #     pred = torch.masked_select(pred, mask)
    #     true = torch.masked_select(true, mask)
    return torch.mean(torch.abs(true-pred))

def mape_torch(pred, true, mask_value=None):
    # if mask_value != None:
    #     mask = torch.gt(true, mask_value)
    #     pred = torch.masked_select(pred, mask)
    #     true = torch.masked_select(true, mask)
    return torch.mean(torch.abs(torch.div((true - pred), true)))

def mae_np(pred, true, mask_value=None):
    # if mask_value != None:
    #     mask = np.where(true > (mask_value), True, False)
    #     true = true[mask]
    #     pred = pred[mask]
    return np.mean(np.absolute(pred-true))

def mape_np(pred, true, mask_value=None):
    # if mask_value != None:
    #     mask = np.where(true > (mask_value), True, False)
    #     true = true[mask]
    #     pred = pred[mask]
    return np.mean(np.absolute(np.divide((true - pred), true)))

def test_metrics(pred, true, mask1=5, mask2=5):
    # mask1 filter the very small value, mask2 filter the value lower than a defined threshold
    assert type(pred) == type(true)
    if type(pred) == np.ndarray:
        mae  = mae_np(pred, true, mask1)
        mape = mape_np(pred, true, mask2)
    elif type(pred) == torch.Tensor:
        mae  = mae_torch(pred, true, mask1).item()
        mape = mape_torch(pred, true, mask2).item()
    else:
        raise TypeError
    return mae, mape


