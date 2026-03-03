from aiohttp import web
routes = web.RouteTableDef()

@routes.get('/')
async def handle_get(request):
    return web.Response(text='Get request') 


@routes.post('/')
async def handle_post(request):
    return web.Response(text='Post request') 


app = web.Application()
app.router.add_routes(routes)
web.run_app(app)
