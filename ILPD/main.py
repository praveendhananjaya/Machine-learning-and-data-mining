import load as dp
from balance.balance import UpSampling

dataset = dp.Load()
df = dataset.run()
upSample = UpSampling(df)
print(upSample.apply())
