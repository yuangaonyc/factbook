import sqlite3
conn = sqlite3.connect('factbook.db')
cur = conn.cursor()
query = '''
    select *
    from facts
    where population != ''
    order by population asc
    limit 10;
    '''
results = cur.execute(query)
print(results)
conn.close