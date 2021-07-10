# Eda

# load pandas
import pandas as pd

class Vision:
    def __init__(self):
        pass

    def load_file(self):
        # dataset
        try:
            self.df = pd.read_csv('../dataset/Indian Liver Patient Dataset (ILPD) .csv')
            return 1
        except FileNotFoundError:
            print("File not found.")
            return 0
        except pd.errors.EmptyDataError:
            print("No data")
            return 0
        except pd.errors.ParserError:
            print("Parse error")
            return 0
        except Exception:
            print("Some other exception")
            return 0
        return 0



## testing
my_vision = Vision()

my_vision.load_file()

""""
# import sweetviz
import sweetviz as sv

#analyzing the dataset
advert_report = sv.analyze(df)

#display the report
advert_report.show_html('Advertising.html')

"""