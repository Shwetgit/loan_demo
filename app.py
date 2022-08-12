from flask import Flask, render_template, request, redirect
import pickle

app = Flask(__name__)
Filename = 'model.pkl'
with open(Filename, 'rb') as file:  
    model = pickle.load(file)

@app.route('/')
def index_page():
    print(model)
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict_logic():
    
    if request.method == 'POST':
        customerprincipalpayments = float(request.form.get('customerprincipalpayments'))
        customerpayments = float(request.form.get('customerpayments'))
        servicefees = float(request.form.get('servicefees'))
        loanmonthssinceorigination = float(request.form.get('loanmonthssinceorigination'))
        interestandfees = float(request.form.get('interestandfees'))
        loancurrentdaysdelinquent = float(request.form.get('loancurrentdaysdelinquent'))
        loanoriginalamount = float(request.form.get('loanoriginalamount'))
        monthlyloanpayment = float(request.form.get('monthlyloanpayment'))
    pred_name = model.predict([[customerprincipalpayments,customerpayments,servicefees,loanmonthssinceorigination,interestandfees,loancurrentdaysdelinquent,loanoriginalamount,monthlyloanpayment]]).tolist()[0]
    yes = "Congrats!! You can have a loan"
    no = "I'm so sorry but you can't have a loan for now"
    result = ''
    if  pred_name == '1':
        result = yes
    else:
        result = no
    return render_template('index.html', pred_name=pred_name, result=result)

if __name__ == "__main__":
    app.run(debug=True)
