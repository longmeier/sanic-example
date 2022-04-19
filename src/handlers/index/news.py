
from sanic import response, Sanic
from models.users import Users 
from tortoise import Tortoise

async def bp_root(request):
    return response.json({"hello": "史豫川"})

async def get_name(request):
    user_list = await Users.filter(id=1).values()
    return response.json({"name": user_list[0]['name']})

async def get_mobile(request):
    db = request.app.ctx.db   # 上下文使用
    #db = Tortoise.get_connection('default')
    result = await db.execute_query_dict("select * from users where id=%s", [1])
    print(result)
    return response.json({"name": result[0]['name']})