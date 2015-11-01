import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

#Read and clean data
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

#Load to pandas
#Create box plot, histogram, QQ for column Amount.Requested
#compare results with Amount.Funded.By.Investors