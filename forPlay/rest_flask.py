from flask import Flask,jsonify

app = Flask(__name__)

dato = [
    {"nombre":"nombre uno", "appellido":"appelido 1","cursos":["Curso1","Curso2","Curso3"]},
    {"nombre":"nombre dos", "appellido":"appelido 2","cursos":["Curso4","Curso5","Curso6"]}
]


@app.route("/")
def principal():
    return jsonify(dato)

@app.route("/home")   
def home():
    return "Hello world"

app.run()