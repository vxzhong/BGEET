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

## 说明

我的安装顺序bug众多，推荐直接去[博德之门贴吧](http://c.tieba.baidu.com/p/9085661589)下载[刘酒](https://github.com/Lzw104522773)的整合版，BUG少、稳定。

log/WeiDU0517.log, log/WeiDU0605.txt是[刘酒](https://github.com/Lzw104522773)整合的版本的log。

## 感谢

感谢[刘酒](https://github.com/Lzw104522773)、[MephistoSatanDevil](https://github.com/MephistoSatanDevil)等人的辛苦付出，汉化了如此多的mod，让我们重回费伦大陆。
