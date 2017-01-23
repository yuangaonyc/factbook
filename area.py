import sqlite3

conn = sqlite3.connect('factbook.db')
query_total_area = '''
    select sum(area_land)
    from facts;
    '''
query_total_water = '''
    select sum(area_water)
    from facts;
    '''
total_area = conn.execute(query_total_area).fetchall()
total_water = conn.execute(query_total_water).fetchall()
conn.close()

print(total_area[0][0]/total_water[0][0])
