from flask import Flask, send_file
app=Flask(__name__)

def send(file):
  return send_file(file,  as_attachment=True)

@app.route("/")
def index():
  return send("ipxe.iso")

@app.route("/menu.ipxe")
def menu():
  return send("menu.ipxe")

@app.route("/tinycore.nogui")
def tinycore_nogui():
  return send("tinycore_nogui.ipxe")

@app.route("/debian.stable")
def debian_stable():
  return send("debian_stable.ipxe")
