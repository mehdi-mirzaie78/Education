from threading import Timer


def say_hello():
    print(" Hello World ".center(80, "*"))


timer = Timer(5, say_hello)  # Waits 5 seconds which is not really accurate and then runs the function

timer.start()
