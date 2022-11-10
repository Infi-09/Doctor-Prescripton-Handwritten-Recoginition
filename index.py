from flask import Flask, render_template, request, redirect, url_for,jsonify, session
import os
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os
import cv2
from src.tess import tesse

app  = Flask(__name__)
CORS(app)


@app.route('/about')
def about():
    return 'About Page Route'


@app.route("/upload", methods=["POST", "GET"])
def upload():
    target=os.path.join('demo','')
    if not os.path.isdir(target):
        os.mkdir(target)
    # logger.info("welcome to upload`")
    file = request.files['file'] 
    filename = secure_filename(file.filename)
    destination="/".join([target, filename])
    file.save(destination)
    session['uploadFilePath']=destination
    response="Whatever you wish too return"
    return jsonify({"message": response})

def get_result(img):
    result = []
    img = cv2.imread(img) 

    img1 = img[605:605+44, 70:70+236]
    bigger1 = cv2.resize(img1, (500, 200))
    gray1 = cv2.cvtColor(bigger1, cv2.COLOR_BGR2GRAY)

    img2 = img[648:648+44, 71:71+236]
    bigger2 = cv2.resize(img2, (500, 200))
    gray2 = cv2.cvtColor(bigger2, cv2.COLOR_BGR2GRAY)

    img3 = img[691:691+44, 71:71+236]
    bigger3 = cv2.resize(img3, (500, 200))
    gray3 = cv2.cvtColor(bigger3, cv2.COLOR_BGR2GRAY)

    img4 = img[735:735+44, 71:71+236]
    bigger4 = cv2.resize(img4, (500, 200))
    gray4 = cv2.cvtColor(bigger4, cv2.COLOR_BGR2GRAY)

    img5 = img[775:775+44, 71:71+236]
    bigger5 = cv2.resize(img5, (500, 200))
    gray5 = cv2.cvtColor(bigger5, cv2.COLOR_BGR2GRAY)

    img6 = img[819:819+44, 71:71+236]
    bigger6 = cv2.resize(img6, (500, 200))
    gray6 = cv2.cvtColor(bigger6, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("demo/test/crop1.jpg", gray1)
    cv2.imwrite("demo/test/crop2.jpg", gray2)
    cv2.imwrite("demo/test/crop3.jpg", gray3)
    cv2.imwrite("demo/test/crop4.jpg", gray4)
    cv2.imwrite("demo/test/crop5.jpg", gray5)
    cv2.imwrite("demo/test/crop6.jpg", gray6)

    lis = ["python src/predict.py demo/test/crop1.jpg",
        "python src/predict.py demo/test/crop2.jpg",
        "python src/predict.py demo/test/crop3.jpg",
        "python src/predict.py demo/test/crop4.jpg",
        "python src/predict.py demo/test/crop5.jpg",
        "python src/predict.py demo/test/crop6.jpg"]

    for i in lis:
        stream = os.popen(i)
        output = stream.read()
        print(output)
        drug = output.split(">")
        print(drug)
        if(len(drug) > 1):
            result.append(drug[1])
        else:
            result.append('')

    for i in lis:
        path = i.split(" ")[-1]
        os.remove(path)
        
    return result

@app.route("/upload/multiple", methods=["POST", "GET"])
def upload_multiple():
    target=os.path.join('demo','')
    if not os.path.isdir(target):
        os.mkdir(target)
    no_of_files = len(request.files)
    response=[]
    for i in range(0,no_of_files):
        file = request.files['file' + str(i)] 
        filename = secure_filename(file.filename)
        destination="/".join([target, filename])
        file.save(destination)
        response.append(get_result(destination))
    # session['uploadFilePath']=destination
    
    return jsonify({"message": response})

@app.route("/upload/lab-report", methods=["POST", "GET"])
def upload_lab_report():
    target=os.path.join('demo','')
    if not os.path.isdir(target):
        os.mkdir(target)
    no_of_files = len(request.files)
    response=[]
    for i in range(0,no_of_files):
        file = request.files['file' + str(i)] 
        filename = secure_filename(file.filename)
        destination="/".join([target, filename])
        file.save(destination)
        response.append(tesse(destination))
    # session['uploadFilePath']=destination
    
    return jsonify({"message": response})


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True)