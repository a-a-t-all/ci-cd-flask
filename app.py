from flask import Flask, jsonify
app = Flask(__name__)

@app.get("/")
def hello():
    return jsonify(status="ok", message="Hello from CI/CD!")

@app.get("/sensors")
def sensors():
    temp = round(random.gauss(60, 2), 2)          # around 60°C ± 2
    speed = round(random.gauss(1.5, 0.1), 3)      # conveyor speed ~1.5 ± 0.1
    anomaly = abs((temp + speed) - 61.5) > 3.5    # fake anomaly detection
    return {"temperature": temp, "conveyor_speed": speed, "anomaly": anomaly}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
