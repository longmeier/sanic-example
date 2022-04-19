
from sanic import Sanic
from handlers.index.urls import index_bp
from tortoise.contrib.sanic import register_tortoise
from config.settings import BaseConfig
from tortoise import Tortoise
app = Sanic("app")
app.update_config(BaseConfig)
app.blueprint(index_bp)

# 注册orm连接
register_tortoise(app, config=app.config["DB_CONFIG"])

async def init_db(app, loop):
    print('sanic 服务启动后建立mysql连接')
    await Tortoise.init(config=app.config["DB_CONFIG"])
    # 上下文赋值
    app.ctx.db = Tortoise.get_connection("default")

app.register_listener(init_db, "before_server_start")

if __name__ == "__main__":
    print('服务启动')
    app.run(host="0.0.0.0", port=8000, debug=True)