import numpy as np
import pandas as pd


def Get_New_Dataset(A,history,pre):
    # 假设 original_data 是你的 NxL 的数据
    N, L = A.shape

    # 创建新的数组，初始化为零
    new_data = np.zeros((N, history, L))

    # 填充新数组
    for t in range(history):
        if t == 0:
            new_data[:, t, :] = A
        else:
            new_data[:, t, t:] = A[:, :-t]

    new_data=np.expand_dims(new_data, axis=3)

    # 创建新的数组，初始化为零
    new_data_Y = np.zeros((N, pre, L))

    # 填充新数组
    for t in range(pre):
        if t == 0:
            new_data_Y[:, t, :] = A
        else:
            new_data_Y[:, t, t:] = A[:, :-t]

    new_data_Y=np.expand_dims(new_data_Y, axis=3)
    return new_data,new_data_Y

if __name__ == '__main__':
    history_len = 16
    pre_len = 4
    Haikou_in =np.array(pd.read_csv('data\Haikou\in_weighted\layer4_dataset_s.csv',header=0,index_col=0))
    Haikou_out = np.array(pd.read_csv('data\Haikou\out_weighted\layer4_dataset_s.csv',header=0,index_col=0))
    Shenzhen_in =np.array(pd.read_csv('data\Shenzhen\in_weighted\layer4_dataset_s.csv',header=0,index_col=0))
    Shenzhen_out = np.array(pd.read_csv('data\Shenzhen\out_weighted\layer4_dataset_s.csv',header=0,index_col=0))
    Haikou_in_x,Haikou_in_y=Get_New_Dataset(Haikou_in,history_len,pre_len)
    Haikou_out_x, Haikou_out_y = Get_New_Dataset(Haikou_out, history_len, pre_len)
    Shenzhen_in_x, Shenzhen_in_y = Get_New_Dataset(Shenzhen_in, history_len, pre_len)
    Shenzhen_out_x, Shenzhen_out_y = Get_New_Dataset(Shenzhen_out, history_len, pre_len)

    #Haikou_in
    Haikou_in_x_train=Haikou_in_x[:int(Haikou_in_x.shape[0]*0.7)]
    Haikou_in_y_train=Haikou_in_y[:int(Haikou_in_y.shape[0]*0.7)]
    Haikou_in_x_val=Haikou_in_x[int(Haikou_in_x.shape[0]*0.7):int(Haikou_in_x.shape[0]*0.8)]
    Haikou_in_y_val=Haikou_in_y[int(Haikou_in_y.shape[0]*0.7):int(Haikou_in_y.shape[0]*0.8)]
    Haikou_in_x_test=Haikou_in_x[int(Haikou_in_x.shape[0]*0.8):]
    Haikou_in_y_test=Haikou_in_y[int(Haikou_in_y.shape[0]*0.8):]
    np.savez('data/Haikou/in/train.npz', x=Haikou_in_x_train, y=Haikou_in_y_train)
    np.savez('data/Haikou/in/val.npz', x=Haikou_in_x_val, y=Haikou_in_y_val)
    np.savez('data/Haikou/in/test.npz', x=Haikou_in_x_test, y=Haikou_in_y_test)
    np.savez('data/Haikou/in_weighted/train.npz', x=Haikou_in_x_train, y=Haikou_in_y_train)
    np.savez('data/Haikou/in_weighted/val.npz', x=Haikou_in_x_val, y=Haikou_in_y_val)
    np.savez('data/Haikou/in_weighted/test.npz', x=Haikou_in_x_test, y=Haikou_in_y_test)

    #Haikou_out
    Haikou_out_x_train=Haikou_out_x[:int(Haikou_out_x.shape[0]*0.7)]
    Haikou_out_y_train=Haikou_out_y[:int(Haikou_out_y.shape[0]*0.7)]
    Haikou_out_x_val=Haikou_out_x[int(Haikou_out_x.shape[0]*0.7):int(Haikou_out_x.shape[0]*0.8)]
    Haikou_out_y_val=Haikou_out_y[int(Haikou_out_y.shape[0]*0.7):int(Haikou_out_y.shape[0]*0.8)]
    Haikou_out_x_test=Haikou_out_x[int(Haikou_out_x.shape[0]*0.8):]
    Haikou_out_y_test=Haikou_out_y[int(Haikou_out_y.shape[0]*0.8):]
    np.savez('data/Haikou/out/train.npz', x=Haikou_out_x_train, y=Haikou_out_y_train)
    np.savez('data/Haikou/out/val.npz', x=Haikou_out_x_val, y=Haikou_out_y_val)
    np.savez('data/Haikou/out/test.npz', x=Haikou_out_x_test, y=Haikou_out_y_test)
    np.savez('data/Haikou/out_weighted/train.npz', x=Haikou_out_x_train, y=Haikou_out_y_train)
    np.savez('data/Haikou/out_weighted/val.npz', x=Haikou_out_x_val, y=Haikou_out_y_val)
    np.savez('data/Haikou/out_weighted/test.npz', x=Haikou_out_x_test, y=Haikou_out_y_test)

    #Shenzhen_in
    Shenzhen_in_x_train=Shenzhen_in_x[:int(Shenzhen_in_x.shape[0]*0.7)]
    Shenzhen_in_y_train=Shenzhen_in_y[:int(Shenzhen_in_y.shape[0]*0.7)]
    Shenzhen_in_x_val=Shenzhen_in_x[int(Shenzhen_in_x.shape[0]*0.7):int(Shenzhen_in_x.shape[0]*0.8)]
    Shenzhen_in_y_val=Shenzhen_in_y[int(Shenzhen_in_y.shape[0]*0.7):int(Shenzhen_in_y.shape[0]*0.8)]
    Shenzhen_in_x_test=Shenzhen_in_x[int(Shenzhen_in_x.shape[0]*0.8):]
    Shenzhen_in_y_test=Shenzhen_in_y[int(Shenzhen_in_y.shape[0]*0.8):]
    np.savez('data/Shenzhen/in/train.npz', x=Shenzhen_in_x_train, y=Shenzhen_in_y_train)
    np.savez('data/Shenzhen/in/val.npz', x=Shenzhen_in_x_val, y=Shenzhen_in_y_val)
    np.savez('data/Shenzhen/in/test.npz', x=Shenzhen_in_x_test, y=Shenzhen_in_y_test)
    np.savez('data/Shenzhen/in_weighted/train.npz', x=Shenzhen_in_x_train, y=Shenzhen_in_y_train)
    np.savez('data/Shenzhen/in_weighted/val.npz', x=Shenzhen_in_x_val, y=Shenzhen_in_y_val)
    np.savez('data/Shenzhen/in_weighted/test.npz', x=Shenzhen_in_x_test, y=Shenzhen_in_y_test)

    #Shenzhen_out
    Shenzhen_out_x_train=Shenzhen_out_x[:int(Shenzhen_out_x.shape[0]*0.7)]
    Shenzhen_out_y_train=Shenzhen_out_y[:int(Shenzhen_out_y.shape[0]*0.7)]
    Shenzhen_out_x_val=Shenzhen_out_x[int(Shenzhen_out_x.shape[0]*0.7):int(Shenzhen_out_x.shape[0]*0.8)]
    Shenzhen_out_y_val=Shenzhen_out_y[int(Shenzhen_out_y.shape[0]*0.7):int(Shenzhen_out_y.shape[0]*0.8)]
    Shenzhen_out_x_test=Shenzhen_out_x[int(Shenzhen_out_x.shape[0]*0.8):]
    Shenzhen_out_y_test=Shenzhen_out_y[int(Shenzhen_out_y.shape[0]*0.8):]
    np.savez('data/Shenzhen/out/train.npz', x=Shenzhen_out_x_train, y=Shenzhen_out_y_train)
    np.savez('data/Shenzhen/out/val.npz', x=Shenzhen_out_x_val, y=Shenzhen_out_y_val)
    np.savez('data/Shenzhen/out/test.npz', x=Shenzhen_out_x_test, y=Shenzhen_out_y_test)
    np.savez('data/Shenzhen/out_weighted/train.npz', x=Shenzhen_out_x_train, y=Shenzhen_out_y_train)
    np.savez('data/Shenzhen/out_weighted/val.npz', x=Shenzhen_out_x_val, y=Shenzhen_out_y_val)
    np.savez('data/Shenzhen/out_weighted/test.npz', x=Shenzhen_out_x_test, y=Shenzhen_out_y_test)
