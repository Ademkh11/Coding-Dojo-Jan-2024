from flask import Flask  
app = Flask(__name__)    
@app.route('/')         
def hello_world():
    return 'Hello World!'  
@app.route('/Dojo')
def dojo():
    return 'Dojo'
@app.route('/say/<flask>')
def hi_flask(flask):
    return(f"Hi {flask}!")
@app.route('/repeat/<int:num>/<string:hello>')
def Hello(num,hello):
    return(f"{num*hello}")

if __name__=="__main__":       
    app.run(debug=True)   

