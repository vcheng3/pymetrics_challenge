import numpy as np
import pandas as pd

sat_scores = pd.read_csv('analyst_challenge_sat_scores.csv')
print(sat_scores.head())
print(sat_scores.info())
print(sat_scores.describe())

sat = pd.DataFrame(sat_scores)
print(sat.head())


sat_no_eth = sat[np.isfinite(sat['ethnicity'])]
print(sat_no_eth)

sat_no_eth_gen = sat_no_eth[np.isfinite(sat_no_eth['gender'])]
print(sat_no_eth_gen)

sat_no_eth_gen_mth = sat_no_eth_gen[np.isfinite(sat_no_eth_gen['SATM'])]
print(sat_no_eth_gen_mth)

sat_no_eth_gen_mth_read = sat_no_eth_gen_mth[np.isfinite(sat_no_eth_gen_mth['SATR'])]
print(sat_no_eth_gen_mth_read)

sat_no_eth_gen_mth_read['total_score'] = sat_no_eth_gen_mth_read['SATM'] + sat_no_eth_gen_mth_read['SATR']
print(sat_no_eth_gen_mth_read)

sat_cleaned = sat_no_eth_gen_mth_read
print(sat_cleaned)

sat_cleaned = sat_cleaned[sat_cleaned['total_score'] <= 1600]
print(sat_cleaned)

'''
Comment after doing this once, for obvious reasons.

writer = pd.ExcelWriter('cleaned_sat_scores.xlsx', engine='xlsxwriter')
sat_cleaned.to_excel(writer)
writer.close()
'''

cleaned_sat = pd.read_excel('cleaned_sat_scores.xlsx')
print(cleaned_sat)

sorted_sat = cleaned_sat.sort_values(by='ethnicity', ascending=1)
print(sorted_sat)

sorted_sat.to_csv('sorted_sat')


eth1 = sorted_sat[sorted_sat['ethnicity'] == 1]
print(eth1)

print('-----------------------------------')

print(eth1['total_score'].max())
print(eth1['total_score'].min())
print(eth1['total_score'].mean())

print('-----------------------------------')

eth2 = sorted_sat[sorted_sat['ethnicity'] == 2]
print(eth2['total_score'].max())
print(eth2['total_score'].min())
print(eth2['total_score'].mean())

print('-----------------------------------')

eth3 = sorted_sat[sorted_sat['ethnicity'] == 3]
print(eth3['total_score'].max())
print(eth3['total_score'].min())
print(eth3['total_score'].mean())

print('-----------------------------------')

eth4 = sorted_sat[sorted_sat['ethnicity'] == 4]
print(eth4['total_score'].max())
print(eth4['total_score'].min())
print(eth4['total_score'].mean())

print('-----------------------------------')

eth5 = sorted_sat[sorted_sat['ethnicity'] == 5]
print(eth5['total_score'].max())
print(eth5['total_score'].min())
print(eth5['total_score'].mean())

print(eth1.count())
print(eth2.count())
print(eth3.count())
print(eth4.count())
print(eth5.count())

print('-----------------------------------')

#genders involved
eth1_gen1 = eth1[eth1['gender'] == 1]
eth1_gen2 = eth1[eth1['gender'] == 2]
print(eth1_gen1['total_score'].mean())
print(eth1_gen2['total_score'].mean())

print('-----------------------------------')

eth2_gen1 = eth2[eth2['gender'] == 1]
eth2_gen2 = eth2[eth2['gender'] == 2]
print(eth2_gen1['total_score'].mean())
print(eth2_gen2['total_score'].mean())

print('-----------------------------------')

eth3_gen1 = eth3[eth3['gender'] == 1]
eth3_gen2 = eth3[eth3['gender'] == 2]
print(eth3_gen1['total_score'].mean())
print(eth3_gen2['total_score'].mean())

print('-----------------------------------')

eth4_gen1 = eth4[eth4['gender'] == 1]
eth4_gen2 = eth4[eth4['gender'] == 2]
print(eth4_gen1['total_score'].mean())
print(eth4_gen2['total_score'].mean())

print('-----------------------------------')

eth5_gen1 = eth5[eth5['gender'] == 1]
eth5_gen2 = eth5[eth5['gender'] == 2]
print(eth5_gen1['total_score'].mean())
print(eth5_gen2['total_score'].mean())

#describe the data

print('-----------------------------------')

print('DATA FOR ETH1')
print(eth1.describe())

print('-----------------------------------')

print('DATA FOR ETH2')
print(eth2.describe())

print('-----------------------------------')

print('DATA FOR ETH3')
print(eth3.describe())

print('-----------------------------------')

print('DATA FOR ETH4')
print(eth4.describe())

print('-----------------------------------')

print('DATA FOR ETH5')
print(eth5.describe())

print('-----------------------------------')
