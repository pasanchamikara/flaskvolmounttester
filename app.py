from flask import Flask

app = Flask(__name__)

@app.route("/")
def root_route():
    return {"message": "this is the app calling"}

@app.route("/health")
def liveness_route():
    return {"message": "app is live"}

@app.route("/write")
def write_to_file():
    try:
        f = open("/app/my.txt", "a")
        f.write("New Content, New volume mounted, salala")
        f.close()
        return {"message": "content written to /app/my.txt"}
    except as e:
        return {"message": e}

@app.route("/efs")
def efs_route():
    try:
        with open("/efs/my.txt", "r") as txt_file:
            return {"message": "route works", "content": txt_file.read()}
    except FileNotFoundError:
        return {"message": "file not found"}
