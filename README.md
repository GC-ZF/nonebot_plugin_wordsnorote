<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>
<div align="center">
<h1 align="center">📕 nonebot_plugin_wordsnorote</h1>
✨ 哥们哥们，背单词么？哥们！ ✨

</div>

<p align="center">
  <a href="https://github.com/GC-ZF/nonebot_plugin_wordsnorote/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/GC-ZF/nonebot_plugin_wordsnorote" alt="license">
  </a>
  <a href="https://pypi.python.org/pypi/nonebot_plugin_wordsnorote">
    <img src="https://img.shields.io/pypi/v/nonebot_plugin_wordsnorote" alt="pypi">
  </a>
  <img src="https://img.shields.io/badge/python-3.7.3+-blue" alt="python">
  <img  src="https://visitor-badge.glitch.me/badge?page_id=nonebot_plugin_wordsnorote" /><br />
</p></br>


## 插件描述

一款基于[Nonebot2](https://github.com/nonebot/nonebot2)的插件

**不是吧，真的有人拿QQ背单词么？！**

<div align="center">
  <img height="300px" src="https://testingcf.jsdelivr.net/gh/GC-ZF/nonebot_plugin_wordsnorote/img/example1.png">
</div>

功能是朋友提的，这个功能我感觉很鸡肋， 我一直习惯于APP背单词，推荐几款软件

* 电脑：[Uahh/ToastFish: 一个利用摸鱼时间背单词的软件](https://github.com/Uahh/ToastFish)（少有且好用的电脑端单词软件！）
* 手机：扇贝单词
* 平板：欧陆词典（功能强大！）

但她说别人发消息**QQ高频**点开，这个理由好像也挺有道理，所以简单做了一个机器人插件。但无论什么方式，重在**坚持**！

py小白，如果有任何问题、建议，欢迎[issues](https://github.com/GC-ZF/nonebot_plugin_wordsnorote/issues)

## 安装
```python
pip install nonebot_plugin_wordsnorote
```
## 配置项
在`bot.py`中添加
```python
nonebot.load_plugin("nonebot_plugin_wordsnorote")
```
在`.evn`中配置参数说明

| config    | type | default | example        | usage                    |
| --------- | ---- | ------- | -------------- | ------------------------ |
| num_words | int  | 20      | num_words = 50 | 每日推送单词数量，默认20 |

每一个QQ号相当于一个ID，数据保存在`data/wordsnoreote/student.json`，其中`wordID`即所背单词数量

## 更换词库

因为我面向的是大学生，所以默认词库是考研英语，[kajweb/dict](https://github.com/kajweb/dict)仓库已将有道数据整理，包括小学到大学的课本、四六级、考研、雅思...

1. 从仓库中下载词库
2. 运行仓库中`turn_json.py`转格式（注意英标是否乱码，推荐在Mac或Linux环境下运行，微软编码默认GBK）并遍历一遍数据，查看是否有缺失
3. 运行仓库中`fix_keys.py`填补缺失数据（以考研词库缺失例句与发音为例，根据实际情况修改`try...expect`异常）

## 示例

<div align="center">
  <img height="300px" src="https://testingcf.jsdelivr.net/gh/GC-ZF/nonebot_plugin_wordsnorote/img/example2.png">
  <img height="300px" src="https://testingcf.jsdelivr.net/gh/GC-ZF/nonebot_plugin_wordsnorote/img/example3.png">
</div>

## 更新记录

2022.8.29，开始本地构建（local_test文件夹）。编写词库转格式与修复。实现插件化：修改所有文件读写路径，增加自定义单词数量、自定义词库功能

2022.8.30，反复测试，QQ合并转发不能超过100条，重构逻辑，发布至商店

202?.?.?，添加复习功能
