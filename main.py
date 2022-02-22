from flask import Flask
app=Flask(__name__)

@app.route("/menu.ipxe")
def menu():
  with open("menu.ipxe", "r") as f:
    return f.read()


@app.route("/tinycore.nogui")
def tinycore_nogui():
  with open("tinycore_nogui.ipxe", "r") as f:
    return f.read()
