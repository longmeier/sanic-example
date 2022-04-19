```
this project is Sanic example!

==================================

#########环境依赖
django-environ
tortoise-orm
aiomysql
aerich
python3.10

########部署步骤
1. 设置数据库连接 .env
    DATABASE_URL="mysql://root:Bolin@1024@127.0.0.1/sanic"
    
2. pip install -r requirements.txt   // 安装依赖

3. aerich init-db  // 同步数据库

4. python run.py   // 启动项目

#########目录结构描述
|── Readme.md   // help
|── config    // 配置
|   |── settings.py   // 设置
|── handlers
|   |── index    // 模块
|       |── news.py  // 视图
|       |── urls.py  // 路由
|── migrations  // 同步数据文件
|── models    // 数据库模型
|   |── base.py    // 基础类
|   |── users.py   // 用户表
|── .env   // 环境变量
|── .gitignore    // 忽略文件
|── db.py    // 同步数据库文件
|── run.py   // 启动文件

########v1.0  版本内容
1. app注册
2. 配置
3. Blueprint/route 路由
4. ctx 上下文
5. register_listener 注册器
6. tortoise-orm/aerich 数据库
```