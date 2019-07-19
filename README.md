# Chihiro 千寻搜索

![](https://img.shields.io/badge/version-0.2-yellowgreen.svg) ![](https://img.shields.io/pypi/pyversions/Django.svg) ![license](https://img.shields.io/github/license/mashape/apistatus.svg)


## 介绍

Chihiro(千寻)是一款的简单搜索引擎。 目的是打造一个**IT First, Privacy First**的搜索网站。

当前已完成前端搭建，以及基本的爬虫开发。如果对此感兴趣，欢迎PR，fork或者star。

## 如何使用

### 1. 安装依赖包

本项目使用[Pipenv](https://github.com/pypa/pipenv)对所需要的依赖包进行管理，因此在使用之前首先运行

~~~shell
$ pipenv install
~~~

(**注意：为了提升下载速度，pipfile中所使用的源为阿里云提供的源**)

### 2. 安装**Elasticsearch**

1. 本项目使用[elasticsearch](https://github.com/elastic/elasticsearch)对数据储存索引，因此须在运行前安装**elasticsearch**及其必要组件，并运行。
2. 索引的初始化可以调用ChihiroSpider或ChihiroSearch下的model类的初始化方法进行初始化。


### 3. 安装Redis

1. 项目采取分布式爬取，使用Redis来对URL调度，去重，因此需安装好Redis。

2. 在爬取时前使用如下命令

   ~~~
   redis-cli lpush myspider:start_urls https//urls
   ~~~

   ​
