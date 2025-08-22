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

## 我的整合版

直接下载通过本脚本整合好的博德之门EET版本：[百度网盘](https://pan.baidu.com/s/1g1sckBuwaS7rKaK_n8DRGg?pwd=2pkj)

注意：
1. 请备份你自己游戏的dialog.dlg，然后再下载更新到新的版本。
2. 使用patch下的zzsave，可以将旧存档升级到新的存档，这样就不需要重新开始游戏了。具体请阅读zzsave下的README。网盘下有旧版本的dialog.dlg下载，如果你没有备份你自己的dialog.dlg，建议使用这个。
3. 文档升级不可能完美，介意的话请重新开始。

* 20250821，更新了新的版本，包括了所有mod的安装文件

## 感谢

1. [刘酒](https://github.com/Lzw104522773)
2. [MephistoSatanDevil](https://github.com/MephistoSatanDevil)
3. [yoshimo](https://github.com/yoshimo0417)
4. 其它所有mod作者
感谢所有人的辛苦付出。

