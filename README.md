# Chihiro 千寻搜索

![](https://img.shields.io/badge/version-0.2-yellowgreen.svg) ![](https://img.shields.io/pypi/pyversions/Django.svg) ![license](https://img.shields.io/github/license/mashape/apistatus.svg)


## 介绍

Chihiro(千寻)是一款的简单搜索引擎。 目的是打造一个**IT First, Privacy First**的搜索网站。

当前已完成前端搭建，以及基本的爬虫开发。如果对此感兴趣，欢迎PR，fork或者star。

## 如何使用

### 1. 安装依赖包

本项目使用[Pipenv](https://github.com/pypa/pipenv)对所需要的依赖包进行管理，因此在使用之前可以先运行

~~~shell
$ pipenv install
~~~

(**注意：pipfile中所使用的源为阿里云提供的源**)

### 2. 安装**Elasticsearch**

1. 本项目使用[elasticsearch](https://github.com/elastic/elasticsearch)对数据储存索引，因此须在运行前安装**elasticsearch**并运行。推荐使用[elasticsearch-rtf](https://github.com/medcl/elasticsearch-rtf)（**注意：项目开发时使用的是es5.1.1，因此相应的python驱动也是对应的此版本，使用其他版本的请自行安装对应版本的驱动，以免产生不必要的麻烦。**）

2. 索引的初始化可以调用ChihiroSpider或ChihiroSearch下的model类的初始化方法进行初始化。​

