import load as dp
from balance.balance import UpSampling, DownSampling
import pandas as pd

Sampling = []

def testSamping():
    dataset = dp.Load()
    df = dataset.run()

    Sampling.append(UpSampling(df))
    Sampling.append(DownSampling(df))


testSamping()

print(Sampling[1].values)
