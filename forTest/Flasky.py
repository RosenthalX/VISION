from flask import Flask, request, redirect, render_template
import os
import cv2

app = Flask(__name__)
root_path = os.getcwd()
www_path = os.path.join(root_path,"www")

@app.route("/")
def home():
    print("template in : {}".format(os.path.join(www_path,"index.html")))
    return render_template("index.html")

@app.route("/upload_img", methods=["POST"])
def upload_img():
    if request.method == "POST":
        idx = request.args.get('type')
        filex = request.files["img"]
        img_dir = os.path.join(www_path,"images",filex.filename)
        print("Nuevo idx tipo "+str(idx))
        filex.save(img_dir)
        img=cv2.imread(img_dir)

        return redirect("/home")
    else:
        return "Only post accepted"

@app.route("/home")
def home2():
    return redirect("/")


def opencv_views(imagen):
    imagen = cv2.resize(imagen,(600,500))

app.run()