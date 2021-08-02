import pandas as pd
from sklearn.utils import resample


class Balance:
    def __init__(self, df: pd):
        self.df = df

    def apply(self) -> pd:
        pass


class UpSampling(Balance):
    def apply(self) -> pd:
        # Separate majority and minority classes
        df_majority = self.df[self.df['Liver Patient'] == 0]
        df_minority = self.df[self.df['Liver Patient'] == 1]

        # Upsample minority class
        df_minority_upsampled = resample(df_minority,
                                         replace=True,  # sample with replacement
                                         n_samples=df_majority.shape[0],  # to match majority class
                                         random_state=123)  # reproducible results

        # Combine majority class with upsampled minority class
        df_upsampled = pd.concat([df_majority, df_minority_upsampled])

        # Display new class counts
        return df_upsampled


class DownSampling(Balance):
    def apply(self) -> pd:
        # Separate majority and minority classes
        df_majority = self.df[self.df['Liver Patient'] == 0]
        df_minority = self.df[self.df['Liver Patient'] == 1]

        # Upsample minority class
        df_majority_down_sampled = resample(df_majority,
                                            replace=True,  # sample with replacement
                                            n_samples=df_minority.shape[0],  # to match minor class
                                            random_state=123)  # reproducible results

        # Combine majority class with upsampled minority class

        df_down_sampled = pd.concat([df_minority, df_majority_down_sampled])

        # Display new class counts
        return df_down_sampled


class DataSmote(Balance):
    def apply(self) -> pd:
        pass
