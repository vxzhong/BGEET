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

推荐直接去[博德之门贴吧](http://c.tieba.baidu.com/p/9085661589)下载[刘酒](https://github.com/Lzw104522773)的整合版，BUG少、稳定。

log/WeiDU0517.log, log/WeiDU0605.txt是[刘酒](https://github.com/Lzw104522773)整合的版本的log。

## 我的整合版

直接下载通过本脚本整合好的博德之门EET版本，包含大量中文mod，不支持定制：[百度网盘](https://pan.baidu.com/s/1g1sckBuwaS7rKaK_n8DRGg?pwd=2pkj)
* 2024/08/23，安装log: log/WeiDU0821.log
  1. 更新大量yoshimo0417的中文翻译，更新Lzw104522773和MephistoSatanDevil的翻译
  2. 增加mod：ToA，由yoshimo0417翻译，https://github.com/yoshimo0417/ToA26/tree/master/ToA
  3. 合并冰风谷的最新更新，可能会和bgiwdeasy不兼容导致问题，没有测试
  4. 移除TomeAndBlood的兼职术士部分，好多问题
  5. 移除ENHANCED-POWERGAMING-SCRIPTS，人物会不攻击，感谢群友“车干”测试
  6. 更新STRATAGEMS到35.19
* 2024/08/21，安装log：log/WeiDU0821.log：
  1. 修复手杖的问题
  2. 世界地图改为中文
  3. TomeAndBlood只有术士兼职，兼职术士的法术计数在穿上和脱下盔甲的时候会翻倍，我自己修复了，可能有问题，不建议兼职术士
  4. 增加mod：REFLECTIONS，命运的倒影，https://github.com/subtledoctor/Reflections-of-Destiny
  5. 增加mod：MORPHEUS562-S-KITPACK，各种职业，https://www.morpheus-mart.com/morpheus562s-kitpack
  6. 增加mod：ENHANCED-POWERGAMING-SCRIPTS，增强脚本，https://www.morpheus-mart.com/enhanced-powergaming-scripts
* 2024/08/19，安装log：log/WeiDU0819.log
  1. 修复了很多乱码的问题
  2. 更新bgiwdeasy、improvemonk等mod
  3. 增加了TOMEANDBLOOD，术士可以兼职
  4. 增加TACTICS-REMIX，巅峰之战很多增强
  5. 增加了IWD_EET_INTEGRATION，冰风谷可以独立战役
  6. 安装完冰风谷2后，修复投射文件
  7. 修复冰风谷加速的问题，移植自0605版本
* 2024/08/11: 少量更新和调整，增加崔斯特传奇、埋骨之丘、戈尔贡之眼等，安装mod的log参见：log/WeiDU0811.log

## 感谢

感谢[刘酒](https://github.com/Lzw104522773)、[MephistoSatanDevil](https://github.com/MephistoSatanDevil)等人的辛苦付出，汉化了如此多的mod，让我们重回费伦大陆。
