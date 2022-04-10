import pandas as pd
import re

comorbidities_list = ['K75.4', 'K75.81', 'Q33.4', 'Z72.0', 'Z72.3', 'Z79.5', 'Z79.899', 'A15', 'A16', 'A17', 'A18',
                      'A19', 'B20', 'C', 'D80', 'D81', 'D82', 'D83', 'D84', 'D86', 'D89', 'E10', 'E11', 'E66', 'E84',
                      'F02', 'F03', 'F70', 'F71', 'F72', 'F73', 'F78', 'F79', 'I25', 'I26', 'I27', 'I42', 'I50', 'I60',
                      'I61', 'I62', 'I63', 'I65', 'I66', 'I67', 'I68', 'I69', 'J44', 'J47', 'J84', 'K70', 'K74', 'N18',
                      'Q90', 'Z33', 'Z34', 'Z36', 'Z37', 'Z38', 'Z39', 'Z3A', 'Z94']


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

    pattern = '([A-Z][0-9]{2}\.[0-9])'

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


class Pacient:
    def __init__(self, sex, varsta, tss, d_dimeri, leucocite, neutrophile, ckmb, ldh, ck, troponina, trombocite,
                 nt_probn, glicemie, uree, crp, feritina, forma_boala, comorbiditati):
        if sex == 'Male':
            self.sex = 1
        else:
            self.sex = 0
        self.varsta = int(varsta)
        self.tss = int(tss)
        self.d_dimeri = float(d_dimeri)
        if float(leucocite) == 0 or float(neutrophile) == 0:
            self.leucocite_neu = 0
        else:
            self.leucocite_neu = (float(neutrophile) / float(leucocite)) / 100
        self.ckmb = float(ckmb)
        self.ldh = float(ldh)
        self.troponina = float(troponina)
        self.ck = float(ck)
        self.trombocite = float(trombocite)
        self.nt_probn = float(nt_probn)
        self.glicemie = float(glicemie)
        self.uree = float(uree)
        self.crp = float(crp)
        self.feritina = float(feritina)
        self.forma_boala = int(forma_boala)
        self.comorbiditati = get_comorbidities(comorbiditati)

    def to_df(self):
        df = pd.DataFrame()

        df['Sex'] = [self.sex]
        df['Varsta'] = [self.varsta]
        df['TSS'] = [self.tss]

        for i in range(len(comorbidities_list)):
            df[comorbidities_list[i]] = [self.comorbiditati[i]]

        df['D-Dimeri'] = [self.d_dimeri]
        df['NEU%/LY%'] = [self.leucocite_neu]
        df['CK-MB*'] = [self.ckmb]
        df['LDH'] = [self.ldh]
        df['CK'] = [self.ck]
        df['TroponinaT'] = [self.troponina]
        df['Trombocite'] = [self.trombocite]
        df['NT-proBNP*'] = [self.nt_probn]
        df['GLICEMIE'] = [self.glicemie]
        df['UREA'] = [self.uree]
        df['ProteinaCreactiva'] = [self.crp]
        df['Feritina*'] = [self.feritina]
        df['Forma_boala'] = [self.forma_boala]

        print(df)

        return df

