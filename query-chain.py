import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain import SQLDatabase, SQLDatabaseChain
from langchain.prompts.prompt import PromptTemplate

load_dotenv()
dburi = "postgresql+psycopg2://postgres:12345@localhost:5432/profitable_development"
llm = ChatOpenAI(model = 'gpt-3.5-turbo-16k',temperature=0)

custom_table_info = {
    "users": """CREATE TABLE users (
    id SERIAL NOT NULL,
    email VARCHAR DEFAULT ''::character varying
    
/*
3 rows from users table:
id email 
1   test@example.com
2   test@example.com
3   test@example.com
*/"""
}
db = SQLDatabase.from_uri(dburi, include_tables=['users'], custom_table_info=custom_table_info)
print(db.table_info)

db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
db_chain.run("How many users are there in the users table?")
# db_chain.run("can you give me the last sign of ip of the 945 user id")
# db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True, use_query_checker=True)

# db_chain.run("Show me a list of PMS clients who don't have Tata Motors in their portfolio.")
