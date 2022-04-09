import pickle


def predict_state(pacient):
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
