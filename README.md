# 使用方法

## 准备

- 复制需要解析的xml文件包到static/data/下
- 其中文件文件目录格式必须为static/data/xml文件夹/xml文件

下面是一条样例

```static/data/a/0ac419a507c06fcb1323d3f6d7ed1fbd.xml```
否则无法正确将文件解析（代码暂时写成这样）

## 安装运行环境：（最好使用虚拟环境）

``` 
pip install fastapi
pip install starlette
pip install uvicorn
```
- cd 到代码目录
- 运行代码

``` 
cd XmlFastApi/
python3 api.py
```
出现以下代码及运行成功
```
INFO:     Started server process [5148]
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## 调用
+ 获取某个文件夹下的文件列表 直接在http://127.0.0.1:8000/getXmlList/后接路径就好：
`http://127.0.0.1:8000/getXmlList/static/data/a`


+ 获取xml 直接在http://127.0.0.1:8000/getXml/后接xml的路径就好：
`http://127.0.0.1:8000/getXml/static/data/a/96b67be4c5e53a299a004848b3bbb40f.xml`


以上调用方式均为http get请求，可以直接在java中发起http请求获取xml内容