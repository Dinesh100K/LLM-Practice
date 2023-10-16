import os
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI



load_dotenv()
dburi = "postgresql+psycopg2://postgres:12345@localhost:5432/profitable_development"
db = SQLDatabase.from_uri(dburi)
llm = ChatOpenAI(model = 'gpt-3.5-turbo-16k',temperature=0)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)
agent_executor.run("How manys users are there in users table")

# custom_table_info = {
#     "users": """CREATE TABLE users (
#     id SERIAL NOT NULL,
#     email VARCHAR DEFAULT ''::character varying
    
# /*
# 3 rows from users table:
# id email 
# 1   test@example.com
# 2   test@example.com
# 3   test@example.com
# */"""
# }
# print(db.table_info)

# db_chain.run("How many users are there in the users table?")
# db_chain.run("can you give me the last sign of ip of the 945 user id")
# db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True, use_query_checker=True)

# db_chain.run("Show me a list of PMS clients who don't have Tata Motors in their portfolio.")
