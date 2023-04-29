from glob import glob
import pandas as pd

def get_x_files():
    paths = glob('./dataset/TRAIN/*.csv')
    dfs = []
    for path in paths:
        df = pd.read_csv(path)
        dfs.append(df)
    
    return pd.concat(dfs, ignore_index=True)

def get_y_files():
    paths = glob('./dataset/TRAIN_AWS/*.csv')
    dfs = []
    for path in paths:
        df = pd.read_csv(path)
        dfs.append(df)
    
    return pd.concat(dfs, ignore_index=True)

if __name__ == '__main__':
    pass