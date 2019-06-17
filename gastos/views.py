from django.http import HttpResponse


def inicio(request):
    return HttpResponse("Esto se llama cuando se visita gastos/")

def hola(request):
    return HttpResponse("Ahora pediste gastos/hola")

def agregar_gasto(request):
    html = """
    <h1>Agregar gasto</h1>
    <p>Podemos mostrar HTML, pero es más interesante cuando usamos
    <strong>plantillas</strong> y motores ;)</p>
    """
    return HttpResponse(html)   