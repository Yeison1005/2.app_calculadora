from flask import Flask, render_template, redirect,request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/' , methods=['Get',"POST"])
def aritmetica():
    if request.method == "POST":
        num1 = float (request.form.get('n1'))
        num2 = float (request.form.get('n2'))
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2
        return render_template('index.html',total_suma=suma,
                                            total_resta=resta,
                                            total_multiplicacion=multiplicacion,
                                            total_division=division,) 
        
    return render_template('index.html')

@app.route('/fecha' , methods=['GET',"POST"])
def fechas():
    if request.method == "POST":
        año1 = int(request.form.get('año1'))
        año2 = int(request.form.get('año2'))
        años3= año2 - año1 
        return render_template('fecha.html', años_transcurridos=años3)
    
    return render_template('fecha.html')


if __name__ == "__main__":
    app.run(debug=True)