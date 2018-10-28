import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stat

df = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
                   'Salary':[50000,54000,50000,189000,55000,40000,59000]})

salary = df['Salary']
salary.plot.hist(title='Salary Distribution', color='lightblue', bins=25)
plt.axvline(salary.mean(), color='magenta', linestyle='dashed', linewidth=2)
plt.axvline(salary.median(), color='green', linestyle='dashed', linewidth=2)
#plt.show()

df = pd.DataFrame({'Test':[172, 174, 176, 172, 172, 173, 176, 172, 177, 174, 176, 175, 176, 169, 175, 174, 174, 174, 175, 173, 171, 171, 175, 175, 173, 175, 175]})
test = df["Test"]
test.plot.hist(title='Test')
density = stat.gaussian_kde(test)
n, x, _ = plt.hist(test, histtype='step', density=True, bins=10)
plt.plot(x, density(x)*5)
plt.show()
print(df["Test"].std())
print(df['Test'].median)
print(df.describe())