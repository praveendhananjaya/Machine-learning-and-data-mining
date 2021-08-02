import matplotlib
import pandas as pd
# import sweetvizear regression
import sweetviz as sv
import matplotlib as plt
import seaborn as sns

import warnings

warnings.filterwarnings('ignore')


class Process:
    def __init__(self):
        self.df = []

    def load(self):
        self.df = pd.read_csv('../dataset/Indian Liver Patient Dataset (ILPD) .csv')
        # print(self.df.head())
        return 1

    def process(self):
        # add title
        self.df.columns = ['age', 'Male', 'TB', 'DB', 'AAP', 'SAlP', 'SAsP', 'TP', 'ALBA', 'AGR', 'Liver Patient']

        # selector
        self.df['Liver Patient'] = self.df['Liver Patient'].apply(lambda x: 0 if (x == 1) else 1)

        # Male
        self.df['Male'] = self.df['Male'].apply(lambda x: 1 if (x == 'Male') else 0)

        self.df = self.df.fillna(0)

        # heat map of correlation of features
        correlation_matrix = self.df.corr()

    def mix(self):
        pass

    def analyze(self):
        # analyzing the dataset EDA
        # correlation between variables
        sns.set()
        sns.pairplot(self.df, kind='reg')

        # correlation between variables
        sns.set()
        sns.pairplot(self.df, hue='dataset', kind='reg')


if __name__ == "__main__":
    data = Process()
    data.load()
    data.process()
    data.analyze()
