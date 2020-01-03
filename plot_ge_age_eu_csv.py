import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

colour_dict = dict({'CON HOLD':'b',
                  'CON GAIN':'aqua',
                  'LAB HOLD': 'red',
                  'LAB GAIN': 'violet',
                  'GRN HOLD': 'g',
                  'DUP HOLD': 'sandybrown',
                  'LD HOLD': 'yellow',
                  'LD GAIN': 'orange',
                  'SNP HOLD': 'black',
                  'SNP GAIN': 'gray',
                  'PC HOLD': 'pink',
                  'SF HOLD': 'peru',
                  'SF GAIN': 'wheat',
                  'SDLP HOLD': 'salmon',
                  'SDLP GAIN': 'lightsalmon',
                  'APNI GAIN': 'lawngreen',
                  'SPE HOLD': 'navy'})

df_age = pd.read_csv('Age_by_year_data.csv')
df_con_head = pd.read_csv('constituency_headline.csv')
df_con_eu = pd.read_csv('eureferendum_constituency.csv')

age_start = 18
age_end = 50

# first get required age range
df_age_group = df_age.query(str(age_start) + " <= Age_year <= " + str(age_end)).groupby("PCON11CD")[["Age_percent"]].sum()

# filter on party if required. Comment out to show all parties. If filtering, adjust legend order list accordingly
#df_con_head.query('wp =="CON" or wp =="LAB"', inplace = True)

# join EU data with election headlines
df_eu_hd = df_con_eu.join(df_con_head.set_index(['ons']), on=['ons_code'], how='inner')

# join the result with age data
df_age_eu = df_age_group.join(df_eu_hd.set_index(['ons_code']), on=['PCON11CD'], how='inner')

# replace WIN with HOLD (not clear how it differs)
df_age_eu['headline'] = df_age_eu['flash'].apply(lambda x: ' '.join(x.split()[:2])).str.replace('WIN', 'HOLD')

# remove % sign and convert to float
df_age_eu['leave_to_use'] = df_age_eu['leave_to_use'].str.rstrip('%').astype('float') / 100.0

# round percentages
decimals = 4    
df_age_eu['leave_to_use'] = df_age_eu['leave_to_use'].apply(lambda x: round(x, decimals))
df_age_eu['Age_percent'] = df_age_eu['Age_percent'].apply(lambda x: round(x, decimals))
 
sns.lmplot(y="leave_to_use", x="Age_percent", data=df_age_eu, hue="headline", height=8.27, aspect=11.7/8.27, fit_reg=False, palette=colour_dict, legend=False)

plt.gca().set_xticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_xticks()]) 
plt.gca().set_yticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_yticks()]) 

plt.ylabel("Leave %")
age_range = str(age_start) + "-" + str(age_end)
plt.xlabel(age_range + "%")

plt.title("2019 General Election: leave vote against population aged " + age_range, fontsize=12)

handles, labels = plt.gca().get_legend_handles_labels()

# order legend using the default positions - comment out if filtering on party
order = [0,1,2,6,3,7,4,13,14,15,8,11,9,10,12,5]

# uncomment for CON and LAB only filter
#order = [0,1,2,3]

plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])

plt.tight_layout()
plt.show()

