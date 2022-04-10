import pickle

class Controller:
    def __init__(self, pacientRepo):
        self.pacient_repo = pacientRepo

    def get(self):
        self.pacient_repo.get_pacient()

    def save_pacient(self, pacient):
        self.pacient_repo.save(pacient)

    def predict_state(self, pacient):

        filename = 'finalized_model.sav'

        # load the model from disk
        loaded_model = pickle.load(open(filename, 'rb'))

        stare_externare = int(loaded_model.predict(pacient))

        if stare_externare == 0:
            return 'Vindecat'
        elif stare_externare == 1:
            return 'Ameliorat'
        elif stare_externare == 2:
            return 'Stationar'
        elif stare_externare == 3:
            return 'Agravat'
        elif stare_externare == 4:
            return 'Decedat'


    def empty_pacients(self):
        self.pacient_repo.empty()