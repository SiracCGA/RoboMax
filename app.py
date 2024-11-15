from flask import Flask, render_template, request

app = Flask(__name__)
Alfa = True

@app.route("/")
def index():
    return render_template('index.html', durum="Her şey yolunda!", sicaklik="10°C", nem="70%")

@app.route("/settings")
def settings():
    if Alfa == True:
        return render_template('settings.html', alfa="Açık", alfa_="Askıya al")
    else:
        return render_template('settings.html', alfa="Askıda", alfa_="Aç")  



@app.route("/settings_alfa")
def alfa_():
    global Alfa
    if Alfa == True:
        Alfa = False
        return render_template('settings.html', alfa="Askıda", alfa_="Aç")  
    else:
        Alfa = True
        return render_template('settings.html', alfa="Açık", alfa_="Askıya al")
        




@app.route("/ileri")
def ileri():
    print("ileri!")
    return render_template('index.html')

@app.route("/geri")
def geri():
    print("geri!")
    return render_template('index.html')

@app.route("/sag")
def sag():
    print("sağ!")
    return render_template('index.html')

@app.route("/sol")
def sol():
    print("sol!")
    return render_template('index.html')

@app.route("/dur")
def dur():
    print("dur!")
    return render_template('index.html')






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)