import pandas as pd


comorbidities_list = ['K75.4', 'K75.81', 'Q33.4', 'Z72.0', 'Z72.3', 'Z79.5', 'Z79.899', 'A15', 'A16', 'A17', 'A18',
                      'A19', 'B20', 'C', 'D80', 'D81', 'D82', 'D83', 'D84', 'D86', 'D89', 'E10', 'E11', 'E66', 'E84',
                      'F02', 'F03', 'F70', 'F71', 'F72', 'F73', 'F78', 'F79', 'I25', 'I26', 'I27', 'I42', 'I50', 'I60',
                      'I61', 'I62', 'I63', 'I65', 'I66', 'I67', 'I68', 'I69', 'J44', 'J47', 'J84', 'K70', 'K74', 'N18',
                      'Q90', 'Z33', 'Z34', 'Z36', 'Z37', 'Z38', 'Z39', 'Z3A', 'Z94']


def comorbidities_to_array(comorb_string):

    result = []
    if comorb_string.strip() == '':
        return [0] * 62
    else:
        for comorbidity in comorbidities_list:
            if comorbidity in comorb_string:
                result.append(1)
            else:
                result.append(0)

        return result


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
        self.comorbiditati = comorbidities_to_array(comorbiditati)

    def to_df(self):
        df = pd.DataFrame()

        df['Sex'] = [self.sex]
        df['Varsta'] = [self.varsta]
        df['TSS'] = [self.tss]

        for i in range(0, len(comorbidities_list)):
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

        return df

