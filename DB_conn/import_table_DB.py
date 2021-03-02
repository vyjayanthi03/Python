import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import io
import os
import re

dbname = 'devops'
port = 5432
user = os.getenv('dbuser')
password = os.getenv('dbpassword')
host = os.getenv('dbhost')
engine = create_engine('postgresql+psycopg2://{0}:{1}@{2}:5432/{3}'.format(user, password, host, dbname))
token = os.getenv('token')

df = pd.read_excel (r'fl solutions.xlsx')
columnnames = [col.strip().replace(" ", "_").lower() for col in list(df.columns.values)]
columnnames = [re.sub(r"[^a-zA-Z0-9]+", '_', k) for k in columnnames]
print(columnnames)
df.columns = columnnames
#df = df.replace(r'\n', r' ', regex=True)
#df = df.replace(r'\\n',' ', regex=True)
print(df)
df.head(0).to_sql('solutions_import', engine, schema='devops', if_exists='replace',index=False) #drops old table and creates new empty table

conn = engine.raw_connection()
cur = conn.cursor()
output = io.StringIO()
df.to_csv(output, sep='\t', header=False, index=False)
output.seek(0)
contents = output.getvalue()
cur.copy_from(output, 'devops.solutions_import', null="") # null values become ''
conn.commit()