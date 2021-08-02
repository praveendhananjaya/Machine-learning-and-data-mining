import matplotlib
import pandas as pd
# import sweetvizear regression
import sweetviz as sv
import matplotlib as plt
import seaborn as sns


class Load:
    def __init__(self) :
        self.df = []


    def load(self) -> bool:
        self.df = pd.read_csv('Indian Liver Patient Dataset (ILPD) .csv')
        # print(self.df.head())
        return True

    def process(self) -> pd:

        # add title
        self.df.columns = ['age', 'Male', 'TB', 'DB', 'AAP', 'SAlP', 'SAsP', 'TP', 'ALBA', 'AGR', 'Liver Patient']

        # selector
        self.df['Liver Patient'] = self.df['Liver Patient'].apply(lambda x: 0 if (x == 1) else 1)

        # Male
        self.df['Male'] = self.df['Male'].apply(lambda x: 1 if (x == 'Male') else 0)

        self.df = self.df.fillna(0)

        # heat map of correlation of features
        correlation_matrix = self.df.corr()
        return self.df

    def run(self) -> pd:
        self.load()
        self.process()
        return self.df


if __name__ == "__main__":
    load = Load()
    print(load.run())
