from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn


app = FastAPI()


# Главная страница
@app.get("/")
async def form():
    return FileResponse("./public/html/home.html")

# Страница "Payment"
@app.get("./html/payment")
async def payment():
    return FileResponse("./public/html/payment.html")

# Страница "Settings"
@app.get("./html/settings")
async def settings():
    return FileResponse("./public/html/settings.html")

# Страница "Manager"
@app.get("./html/manager")
async def manager():
    return FileResponse("./public/html/manager.html")

# Страница "Statistics"
@app.get("./html/statistics")
async def statistics():
    return FileResponse("./public/html/statistics.html")


# JavaScript файлы
@app.get("./js/script.js")
async def script():
    return FileResponse("./public/js/menu.js")

@app.get("./js/payment.js")
async def payment_script():
    return FileResponse("./public/js/payment.js")

@app.get("./js/settings.js")
async def settings_script():
    return FileResponse("./public/js/settings.js")

@app.get("./js/manager.js")
async def manager_script():
    return FileResponse("./public/js/manager.js")

@app.get("./js/statistics.js")
async def statistics_script():
    return FileResponse("./public/js/statistics.js")


# CSS файлы
@app.get("./css/style.css")
async def style():
    return FileResponse("./public/css/menu.css")

@app.get("./css/payment.css")
async def payment_style():
    return FileResponse("./public/css/payment.css")

@app.get("./css/settings.css")
async def settings_style():
    return FileResponse("./public/css/settings.css")

@app.get("./css/manager.css")
async def manager_style():
    return FileResponse("./public/css/manager.css")

@app.get("./css/statistics.css")
async def statistics_style():
    return FileResponse("./public/css/statistics.css")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5770, reload=True)
