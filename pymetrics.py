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
print(eth1['total_score'].max())
print(eth1['total_score'].min())
print(eth1['total_score'].mean())
print(eth1.loc[eth1['total_score'] == 750])


