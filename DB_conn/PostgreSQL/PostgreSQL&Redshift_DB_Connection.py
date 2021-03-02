import psycopg2 #postgre & Redshift sql connection
# conn = psycopg2.connect(database="", user='', password='', host='', port= '')
conn = psycopg2.connect(database="sprighub_db", user='sprighub_admin', password='s43pr!ghub34dOPmin+++', host='camp-st-db.cqe7xmvovcum.us-east-1.rds.amazonaws.com', port= '5432')
#cursor is used to execute postgresql in python
cursor = conn.cursor() # connection to get query data
q='''
select * from "Campaign"
'''
cursor.execute(q) # to execute the query
data = cursor.fetchall() #To fetch o/p of given query; and it has two types [fetchone() & fetchall()]
# print("Connection established to: ",data)

import pandas as pd
df = pd.DataFrame(data)
print(df)
conn.close()