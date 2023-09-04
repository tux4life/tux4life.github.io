import eel
import os

eel.init("q1")

@eel.expose
def App():
    os.system("color a")
    print("tux4life loading...")
App()

eel.start("index.html")

