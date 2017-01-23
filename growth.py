import pandas as pd
import sqlite3
import math

conn = sqlite3.connect('factbook.db')
query = 'select * from facts'
facts = pd.read_sql_query(query, conn)
conn.close()

facts.dropna()
facts = facts[facts['area_land']!=0]

def calc_2050_pop(row):
    pop_growth = row['population_growth'] / 100
    init_pop = row['population']
    final_pop = init_pop * math.e ** (pop_growth * 35)
    return final_pop

facts['pop_2050'] = facts.apply(calc_2050_pop, axis=1)
facts = facts.sort_values('pop_2050', ascending=False)
facts = facts.reset_index()
print(facts[:10])