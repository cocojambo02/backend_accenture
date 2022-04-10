from flask import Flask, request, jsonify
import json
import re

from Repository.Repository import PacientRepository
from controller.Controller import Controller
from model.Model import Model
from model.Pacient import Pacient

app = Flask(__name__)

def get_comorbidities(text):
    """
    Parses the text using the pattern Regex
    Divides the text in precise_com and category_com comorbidities
    Arguments:
        text: a string
    Returns:
        The occurrences of each comorbidity in the string argument
    """

    comorbidities_dataset = "C:\\personal\\AI\\backend\\data\\comorbidities.txt"
    comorbidities = []
    try:
        with open(comorbidities_dataset, 'r') as file:
            lines = file.readlines()
            for line in lines:
                comorbidities.append(line.split(',')[0])

            precise_com = comorbidities[0:7]
            category_com = comorbidities[7:]
    except IOError:
        print(comorbidities_dataset + " not found")
        return False

    pattern = '([A-Z][0-9]{2}\.*[0-9]*)'

    coduri_com = [re.findall(pattern, text)]
    coduri_com = [item for sublist in coduri_com for item in sublist]

    end_list = []

    for com in coduri_com:
        if 'C' in com:
            end_list.append('C')
        else:
            end_list.append(com.split('.')[0])

    comorb_count_list = []

    for com in precise_com:
        comorb_count_list.append(end_list.count(com))
    for com in category_com:
        comorb_count_list.append(end_list.count(com))

    return comorb_count_list

@app.route('/predict', methods=['POST'])
def predict():
    """
    Converts the pacient string into a dataframe row
    Predicts it's outcome based on a Random Forest trained on 'dataset_processed_csv'
    Arguments:
        pacient: a string
    Returns:
        The occurrences of each comorbidity in the string argument
    """

    if request:

        form = request.form
        sex = json.loads(form["Pacient"])["sex"]
        varsta = json.loads(form["Pacient"])["varsta"]
        tss = json.loads(form["Pacient"])["tss"]
        d_dimeri = json.loads(form["Pacient"])["d_dimeri"]
        ckmb = json.loads(form["Pacient"])["ckmb"]
        ldh = json.loads(form["Pacient"])["ldh"]
        ck = json.loads(form["Pacient"])["ck"]
        troponina = json.loads(form["Pacient"])["troponina"]
        trombocite = json.loads(form["Pacient"])["trombocite"]
        nt_probn = json.loads(form["Pacient"])["nt_probn"]
        glicemie = json.loads(form["Pacient"])["glicemie"]
        urea = json.loads(form["Pacient"])["urea"]
        crp = json.loads(form["Pacient"])["crp"]
        feritina = json.loads(form["Pacient"])["feritina"]
        forma_boala = json.loads(form["Pacient"])["forma_boala"]
        leucocite = json.loads(form["Pacient"])["leucocite"]
        neutrophile = json.loads(form["Pacient"])["neutrophile"]
        lista_comorbiditati = json.loads(form["Pacient"])["lista_comorbiditati"]

        pacient = Pacient(sex, varsta, tss, d_dimeri, leucocite, neutrophile, ckmb, ldh, ck, troponina, trombocite, nt_probn,
                glicemie, urea, crp, feritina, forma_boala, lista_comorbiditati)

        return F"Starea posibilă de externare a pacientului : {controller.predict_state(pacient.to_df())}" , 200

@app.route('/get_comorbidities', methods=['GET'])
def query_records():
    with open('C:\\personal\\AI\\backend\\data\\Comorbidities.json', 'r') as f:
        data = f.read()
        records = json.loads(data)
        return jsonify(records)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    repo = PacientRepository()
    controller = Controller(repo)
    app.run(debug=True, port=5000)
