[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-360/)
## 功能简介
分析 Juniper SRX 的防火墙策略，输出到 PostgreSQL 或 Excel  
分析 Juniper SRX 的 session

## 环境依赖
所需模块如下
- xlwt
- psycopg2
- xmltodict

## 文件列表
| 文件名   | 作用  |
|  ----  | ----  |
|  srx_analysis.py | 主程序 |
| srx_json.py  | 这个不用了，待删除 |

## 使用方法
由于需要连接数据库，我限制源 IP 了，所以目前不能直接下载使用

## 技术介绍
### 实现方法
1. 获取到 xml 格式的配置
2. 将 xml 转为 json
3. 分析 json，获取到结果后放到数据库
4. 用 django 呈现数据库的内容
### 数据库设计
1. 目前有3个表，分别存放策略、地址集、地址本
2. 外键  
一个 address-book 只能对应一个 address-set，多个 address-book 可以对应一个 address-set；  
一个 address-set 可以对应多个 address-book。

## 版本内容更新
**2019-11-16**
- 计划更新一下，添加外键  

**2019-11-10**
- 分析后的策略支持输出为 Excel 
