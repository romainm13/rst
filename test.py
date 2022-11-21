#%%
#!/home/romainm13/rst/rst_venv/bin python
# -*- coding:utf-8 -*-

from flask import Flask, request

app = Flask(__name__)
#app.debug = True
app.secret_key = '2d9-E2.)f&é,A$p@fpa+zSU03êû9_'

@app.route('/')
def racine():
    return "Le chemin de 'racine' est : " + request.path

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return("GET")
    else:
        # traiter les données reçues
        # afficher : "Merci de m'avoir laissé un message !"
        return("POST")

if __name__ == '__main__':
    app.run(debug=True)