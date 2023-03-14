import store
from fastapi import FastAPI # Creando nuestro entorno servidor #
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return[1,2,3]

@app.get("/contact", response_class = HTMLResponse)
def get_list():
    return """
        <h1>Hola, estoy creando mi servidor web</h1>
        <p>Jarlinzon lo esta codificando con python
        y con estornos virtuales. ;)
        Hoy tuve ayuda de mi amigo Cris. </p>
    """    

def run():
    store.get_categories()


if __name__ =="__main__":
    run()