## 爬虫框架使用说明
### 1.准备
#### 1.1 Mac OS 必备环境
#####a.请下载安装 Docker 软件，链接如下，https://www.docker.com/docker-mac，免费好用，值得拥有.
#####b.安装好后，请确保 Docker 处于运行状态.

### 1.2 Linux 必备环境
##### a.CentOS 7.x 安装 Docker-compose 指南：https://blog.csdn.net/JOJOY_tester/article/details/79182216
##### b.Ubuntu 16.x 安装 Docker-compose 指南：https://blog.csdn.net/omg2hei/article/details/78043571

### 2.使用
#### 1.1 框架说明以及运行
##### a.etc 目录为相关的 Docker 目录，目前集成 Python、Mongo、Redis、RockMongo. source 目录为爬虫代码目录.
##### b.运行 ./deploy.sh 即可安装运行相关的 Docker.
##### c.Docker 目前集成了定时器功能，如果爬虫脚本需要定时执行，可在 /etc/python/cron.conf 中加入需要定时执行的命令，具体格式请参考 /etc/python/cron.conf.
#### 1.2 爬虫编写
##### a.爬虫采用 Scrapy 框架，相关的教程如下说明中有.
##### b.如果脚本非定时运行，请执行以下命令：
```javascript 1.8
    // 确保爬虫docker已经运行，且进入
    docker exec -it etc_python_1 /bin/sh
    // 进入爬虫项目目录.
    cd /var/Spider/Spider
    // 执行需要运行的爬虫脚本.
    scrapy crawl xxxSpider
```
##### c.目前 Mongo 已经封装好，且数据库统一为 test，使用如下：
```javascript 1.8
    // 在文件中引入 util 模块
    import util
    import scrapy

    class xxxSpider(scrapy.Spider):
        mongo_client = null
        // python定义方法
        def xxx(self, response):
        // 向 test 库中的 user 表，插入一条数据.
            info = {'name': 'test'}
            self.mongo_client = util.MongoDB.client()
            self.mongo_client.user.insert(info)
```
#### d.目前 Redis 已经封装好，使用如下：
```javascript 1.8
    // 在文件中引入 util 模块
    import util
    import scrapy

    class xxxSpider(scrapy.Spider):
        redis_client = null
        // python定义方法
        def xxx(self, response):
        // 向 test 库中的 user 表，插入一条数据.
            self.redis_client = util.MongoDB.client()
            self.redis_client.set('name', 'test')
```
##### d.查看相关的 Mongo 数据，在浏览器中输入：http://127.0.0.1:8088, 登录用户名:admin,密码:OU9J8DICfyYW9Vtf
##### e.查看相关的 Redis 数据，Mac OS 下推荐使用 rdm 工具，使用简单、方便，还免费。链接:https://www.jianshu.com/p/214baa511f2e

### 3.相关说明
##### 3.1 框架目前只支持 Linux 和 Mac OS.
##### 3.2 Python 版本为 3.0 及以上，Python 教程：https://wizardforcel.gitbooks.io/w3school-python/content/part3.html
##### 3.3 Mongo 版本为 3.3 及以上，Mongo 教程: https://jockchou.gitbooks.io/getting-started-with-mongodb/content/
##### 3.4 Redis 版本为 3.0 及以上，Redis 教程：https://legacy.gitbook.com/book/wizardforcel/w3school-redis/details
##### 3.5 Scrapy 教程： http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html
