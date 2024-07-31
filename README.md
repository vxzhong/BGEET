# 博德之门mod整合脚本

## 使用说明

1. 下载[博德之门增强版四部曲](https://pan.baidu.com/s/1fKn2NvcNV9GfXjtB5pt9xA?pwd=BEET)下的Baldur's Gate Enhanced Edition Tetralogy.7z，放到主目录下，不需要解压
2. 下载[BGEET](https://pan.baidu.com/s/1g1sckBuwaS7rKaK_n8DRGg?pwd=2pkj)下的downloads.7z，并解压到mod目录下
3. 执行一遍download.py
4. 执行install.py安装

## 安装顺序

1. 安装顺序文件：mod/install_order.txt
2. 不安装某个mod的某个组件：在这行的开头插入`#`，或者将这行分号分隔的最后一部分改成0000

## 增加新的mod

1. 先在mod/mods.toml模仿已有的mod定义，支持两种下载方式：wget和git，执行download.py下载
2. 在mod/install_order.txt里添加组件，执行install.py安装
