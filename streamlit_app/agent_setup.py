from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
# from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain.agents import AgentType

from .get_llm import get_llm

def create_agent(db):
    print(f"Using database dialect: {db.dialect}")  # Should output 'postgresql'

    context = db.get_context()

    llm = get_llm()
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    
    return create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        dialect="postgresql",
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        context = context,
        verbose=True,
        agent_executor_kwargs={"handle_parsing_errors": True}
    )