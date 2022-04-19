### 1. gitee 地址 https://gitee.com/longmeier90/sanic_example.git
### 2. config 配置
```
a. settings.py 文件定义

    import environ, os 
    
    # 获取项目路径
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env = environ.Env()
    
    # 加载.env文件
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
    DB_URL=env('DATABASE_URL', default='mysql://localhost/bolin_dev')
    print('database_url:', DB_URL)
    
    # 数据库配置
    db_config = {
        "connections": {"default": DB_URL},
        "apps": {
            "models": {
                # models对应上面创建的models.py
                "models": ["aerich.models", "models"], 
                "default_connection": "default",
            },
        },
    }
    class BaseConfig:
        DB_CONFIG = db_config

b. run.py 文件
    from config.settings import BaseConfig
    app.update_config(BaseConfig)
    conf = app.config["DB_CONFIG"]

```
### 3. Blueprint/route
``` 
    a.文件 handlers/index/urls.py 
    # 注册蓝图
    from sanic import Blueprint, Sanic
    from .news import bp_root  # 视图
    index_bp = Blueprint('index', url_prefix='/api/index')

    index_bp.add_route(bp_root, '/hello/')
    b. 文件run.py
    from handlers.index.urls import index_bp
    app = Sanic(__name__)
    app.blueprint(index_bp)
    
```
### 4. tortoise-orm 
```
    register_tortoise(app, db_url=DB_URL, modules={"models":["models"]}, generate_schemas=True)
    register_tortoise(app, config=app.config['DB_CONFIG'])
    
    # 原生的sql
    async def init_db(app, loop):
        await Tortoise.init(config=app.config['DB_CONFIG'])
    
    app.register_listener(init_db, "before_server_start")
    db = Tortoise.get_connect('default')
```
### 5. aerich 同步数据文件
```
    1.创建db.py文件
    from config.settings import DB_URL
    TORTOISE_ORM = {
        "connections": {"default": DB_URL},
        "apps": {
            "models": {
                # models对应上面创建的models.py
                "models": ["aerich.models", "models"], 
                "default_connection": "default",
            },
        },
    }
    
    2. aerich init-db 初始化migration 
    
    3. aerich migrate 生成migrate文件；第一次会更新数据库
    
    4. aerich upgrade 同步数据库
    
    5. aerich downgrade 回退到上个版本
```