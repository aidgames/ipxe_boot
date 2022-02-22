from flask import Flask, send_file, request
app=Flask(__name__)

def send(file):
  return send_file(file,  as_attachment=True)

@app.route("/")
def index():
  if request.args.get("type") == "BIOS":
    return send("ipxe.iso")
  elif request.args.get("type") == "UEFI":
    return send("ipxe_efi.iso")
  else:
    return "<br>".join([f"<a href=\"/?type={i}\"> {i} </a>" for i in ["UEFI", "BIOS"]])

@app.route("/menu.ipxe")
def menu():
  return send("menu.ipxe")

@app.route("/tinycore.nogui")
def tinycore_nogui():
  return send("tinycore_nogui.ipxe")

@app.route("/debian.stable")
def debian_stable():
  return send("debian_stable.ipxe")
