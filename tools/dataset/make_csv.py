'''
Copyright: © 2021, BeingGod. All rights reserved.
Author: BeingGod
Date: 2021-02-23 23:21:10
LastEditors: BeingGod
LastEditTime: 2021-05-06 21:19:02
Description: 生成标签文件
'''

import argparse
import cv2
from tqdm import tqdm
import numpy as np
import os
import sys


def get_dataset_label(path):
    dicts = os.listdir(os.path.join(path,"images"))
    lines = []
    m_list, s_list = [], []

    try:
        os.chdir(os.path.join(path, "images"))

        for i in range(len(dicts)):
            dic = dicts[i]
            os.chdir('{}'.format(dic))
            files = os.listdir('./')
            
            for filename in files:
                filename = list(filename)
                filename = ''.join(filename)
                label = str(i)
                
                # 计算标准差和方差
                img = cv2.imread(filename)
                img = img / 255.0
                m, s = cv2.meanStdDev(img)
                m_list.append(m.reshape((3,)))
                s_list.append(s.reshape((3,)))

                file_path = os.path.join(path, "images/{}/{}".format(path, dic, filename))
                lines.append([file_path, label])
            os.chdir('../')

    except Exception as FileNotFoundError:
        print("[ERROR] Not exists dict")
        sys.exit(-1)
    
    m_array = np.array(m_list)
    s_array = np.array(s_list)
    m = m_array.mean(axis=0, keepdims=True)
    s = s_array.mean(axis=0, keepdims=True)
    print(m[0][::-1])
    print(s[0][::-1])
    
    return lines 


def save_as_csv(data,path):
    os.chdir(path)
    with open('labels.csv', 'w') as f:
        f.write('filepath,label\n')
        for line in data:
            f.write(','.join(line))
            f.write('\n')


if __name__ == "__main__":
    path = sys.argv[1]
    data = get_dataset_label(path)
    save_as_csv(data,path)
