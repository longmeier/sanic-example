import environ, os 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env()
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
    DB = None
    