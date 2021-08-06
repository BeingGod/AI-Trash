<!--
 * @Copyright: © 2021, BeingGod. All rights reserved.
 * @Author: BeingGod
 * @Date: 2021-02-28 21:25:10
 * @LastEditors: BeingGod
 * @LastEditTime: 2021-07-05 13:28:54
 * @Description: 说明文档
-->

# AI-Trash
全国大学生工程能力训练竞赛-生活垃圾分类赛道


## 声明

本软件不得用于商业用途，仅做学习交流！



## 目录结构

```bash
.
├── app
│   ├── app.py  # 主程序
│   ├── app.ui  
│   ├── conf.py # 应用配置
│   ├── model   # 加载模型路径
│   ├── test.py # 测试程序
│   ├── ui.py   # 可视化界面
│   └── video   # 宣传视频路径
├── LICENSE
├── README.md
├── tools
│   ├── dataset
│   │   ├── make_csv.py # 数据标注
│   │   └── rename.py
│   └── train
│       ├── checkpoints # 模型保存路径
│       ├── conf.py     # 训练配置
│       ├── dataset.py  # 自定义数据集类
│       ├── infer.py    # 推理
│       └── train.py    # 训练
└── requirements.txt
```



## 安装依赖

```bash
pip install -r requriements.txt
```



## 训练

1. 将图片复制到`dataset/images/`目录下(需要自己创建)
2. 运行`tools/dataset/`目录下的`make_csv.py`文件

```bash
python3 make_csv.py <dataset目录的绝对路径>
```

3. 根据实际数据集，修改`tools/train/`目录下的`conf.py`文件
4. 运行`tools/train/`目录下的`train.py`文件

```bash
python3 train.py
```



## 可视化界面

1. 更新`app/`目录下的`conf.py`文件
2. 运行`app/`目录下的`app.py`文件

```bash
python app.py
```
