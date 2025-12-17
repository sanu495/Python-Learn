# Closure Function

def outer(msg):
    def inner():
        return f"message from : {msg}"
    return inner

say=outer("Hi User")
print(say())