from dotenv import load_dotenv
from langchain import SQLDatabase, SQLDatabaseChain, OpenAI
import sqlite3

load_dotenv()
# This is to create view
# conn = sqlite3.connect('sfscores.sqlite')
# cursor = conn.cursor()
# view_name = 'Test_view'
# query = 'SELECT * from violations where business_id = 10;'
# cursor.execute('CREATE VIEW {} AS {}'.format(view_name, query))
# conn.commit()
# conn.close()
############

breakpoint()
dburi = "postgresql+psycopg2://postgres:{env('OPEN_AI')}@localhost:5432/profitable_development"
db = SQLDatabase.from_uri(dburi, include_tables = ['users'] , view_support = True)
llm = OpenAI(temperature=0)

db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True, return_direct= True)

db_chain.run("give me all the violations of XOX Truffles")
db_chain.run("give me the last inspcetion score for XOX Truffles and the date on which inscpetion happened")
# db_chain.run("what is the score of that business and what is the bussiness id")

conn = sqlite3.connect('sfscores.sqlite')
cursor = conn.cursor()
view_name = 'Test_view'
# query = 'SELECT * from violations where business_id = 10;'
cursor.execute('DROP VIEW {}'.format(view_name))
conn.commit()
conn.close()
