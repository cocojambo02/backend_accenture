import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle


class Model:

    def __init__(self):
        # read data from csv
        self.file = r'C:\personal\AI\backend\data\dataset_processed.csv'
        self.df = pd.read_csv(self.file)

        # balance data
        X, y = SMOTE(k_neighbors=4).fit_resample(self.df.drop('Stare_externare', axis=1), self.df['Stare_externare'])
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        # train model
        self.classifier = RandomForestClassifier(n_estimators=100, random_state=0)
        self.classifier.fit(X_train, y_train)

        # save the model to disk
        filename = 'finalized_model.sav'
        pickle.dump(self.classifier, open(filename, 'wb'))
