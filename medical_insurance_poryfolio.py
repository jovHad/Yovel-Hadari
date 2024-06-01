import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import csv

sns.set_palette("Set2")
pd.options.display.max_rows = None
pd.options.display.max_columns = None
# load in the insurance data frame
df = pd.read_csv('insurance.csv')
print(df.head())
# descriptive statistics summary
print(df.describe())

# count of smokers get insurance grouped by smokers
smokers = df['smoker'].value_counts()
print(smokers)
#countplot
sns.countplot(df, x="smoker", palette={"no": "lightgreen", "yes": "lightblue"})
plt.xlabel('is smokes')
plt.ylabel('count')
plt.title('Count by Smokers getting Health Insurance')
plt.show()
# the percentage of smokers gets insurance grouped by smokers
print(df["smoker"].describe())
smokers_presenege = df['smoker'].value_counts(normalize=True)
print(smokers_presenege)
plt.bar(smokers.index, smokers_presenege, color=['lightgreen', "lightblue"])
plt.xlabel('is smokes')
plt.ylabel('presents')
plt.title('Presents of Smokers getting Health Insurance')
plt.show()

# mean of Charges by Smoker Category
smoker__charge = df.groupby('smoker')['charges']  # mean charges by smoker group
print("smoker_mean_charge: \n", smoker__charge.describe())
# visualize relationship between mean of Charges by Smoker Category and smokers frequency
smoker_mean_charge = smoker__charge.mean()
plt.bar(smokers.index, smoker_mean_charge.values,
        color=['lightgreen', "lightblue"])  # Plot bars with smoker category and mean values
plt.xlabel('Smoker Category')
plt.ylabel('mean of Charges')
plt.title('mean of Charges by Smoker Category')
plt.show()

# The number of subjects who do not smoke is 790 higher than those who smoke and receive insurance, i.e.
# 60% more, which is interesting because non-smokers pay less 23615.97 mean.
# We can understand that those who smoke will suffer more desires.


# visualize relationship between smoker status and age frequency
smoker_age = df.groupby('smoker')['age']  # age by smoker group
print("smoker_age:\n", smoker_age.describe())
colors = {'yes': 'lightgreen', 'no': 'lightblue'}
plt.scatter(df.index, df['age'], c=df['smoker'].map(colors))
plt.xlabel('Index')
plt.ylabel('Age')
plt.title('Age Distribution by Smoker Category')
plt.legend(
    handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='lightgreen', markersize=10, label='Smoker'),
             plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='lightblue', markersize=10,
                        label='Non-Smoker')])
plt.show()
# There is no correlation between age and status of a smoker.

# visualize relationship between smoker status and BMI
smoker_bmi = df.groupby('smoker')['bmi'].mean()  # bmi by smoker group
plt.bar(smokers.index, smoker_bmi.values,
        color=['lightgreen', "lightblue"])  # Plot bars with smoker category and bmi values
plt.xlabel('Smoker Category')
plt.ylabel('BMI')
plt.title('BMI by Smoker Category')
plt.show()

# scatter of relationship between smoker status and BMI
plt.scatter(df.age, df.bmi)
plt.xlabel('Age')
plt.ylabel('BMI')
plt.title('BMI by Age')
plt.show()
#we can see there is no corallation between age and bmi to smokers


# To conclude, the only correlation between variables in this df is the status of smoker and the amount they are
# charged of.
# The number of subjects who do not smoke is 790 higher than those who smoke and receive insurance,
# i.e. 60% more, which is interesting because non-smokers pay less 23615.97 mean. We can understand that those who
# smoke will suffer more desires.

