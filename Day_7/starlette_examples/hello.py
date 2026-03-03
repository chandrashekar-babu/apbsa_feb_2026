from starlette.applications import Starlette
from starlette.responses import JSONResponse, HTMLResponse
import uvicorn

app = Starlette(debug=True)

@app.route('/')
async def homepage(request):
    return JSONResponse({'hello': 'world'})


@app.route("/greet/{name}")
async def greet(request):
    name = request.path_params['name']
    #return JSONResponse({'message': f"Hello, {name}!"})
    return HTMLResponse(f"<h1>Hello, {name}!</h1>")

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
