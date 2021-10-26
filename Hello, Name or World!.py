def hello(name = ''):
    Hi = "Hello, "
    Exclamacion = "!"
    World = "World"
    name = name.capitalize()
    if len(name) == 0:
        return Hi + World + Exclamacion
    return Hi + name + Exclamacion