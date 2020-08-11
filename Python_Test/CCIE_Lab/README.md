[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-374/)
## 背景
敲CCIE版本时，每天需要交作业，但手动获取配置太麻烦，耗时间，用CRT批量保存log时，文件名又没办法写成设备的名称，例如R1、R2，所以编写此脚本，完成自动收集的工作

## 适用范围
- K1、K1+（已测试）
- 其他的还未测试，理论上应该没问题

## 使用方法
- 系统：macOS、Linux（windows不行）
- Python 3.x
- 运行前请用CRT或Putty打开设备，处于 ">" 或 "#" 模式即可
- `python3 cofig_homework.py` 然后根据提示操作
- 请注意未收集到的设备端口，需要手动收集

## 收集好的配置在哪
在代码所在的目录内

## 目前存在的问题
- 收集不了sw 的配置，这个看情况适配
- 还不支持 windows 
- 有一部分自动获取不到，需要手动
- 功能还比较简陋，由于还要备考CCIE，所以没有那么多精力去优化了