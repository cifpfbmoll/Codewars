#Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).
#Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).
def hello(name = ''):
    Hi = "Hello, "
    Exclamacion = "!"
    World = "World"
    name = name.capitalize()
    if len(name) == 0:
        return Hi + World + Exclamacion
    return Hi + name + Exclamacion