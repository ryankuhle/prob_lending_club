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
'''
from the box plot until that the investors funded a little less than was requested. There were a lot of outliers at the top of the field
from the histogram you can tell that the most popular investment value  was in the 10,000 range
the qq charts were very similar
'''