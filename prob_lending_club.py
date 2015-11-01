import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

#Read and clean data
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

#Create boxplot
loansData.boxplot(column='Amount.Requested')
plt.savefig('boxplot.png')

#Create histogram
loansData.hist(column='Amount.Requested')
plt.savefig('histogram.png')

#Create QQ
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig('qq.png')

#compare results with Amount.Funded.By.Investors