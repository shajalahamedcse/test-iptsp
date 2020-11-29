from flask import Flask,request

app = Flask(__name__)

@app.route("/api/v1/obd_response",methods=["POST"])
def obd_response():
    data = request.data
    print(data)
    return {"msg":"Hello"}

@app.route("/api/v1/alive")
def alive():
    return {"msg": "alive"}
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)