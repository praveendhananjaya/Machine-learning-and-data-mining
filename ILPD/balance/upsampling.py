
import balance
import pandas as pd
from sklearn.utils import resample
from pathlib import Path
import sys


# sys.path.append("..")
# from load import Load



if __name__ == "__main__":
    load = Load()
    df = load.run()
    upSample = UpSampling(df)
