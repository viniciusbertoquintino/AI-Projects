from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

agent = Agent(tools=[TavilyTools()],
              show_tool_calls=True)

agent.print_response("Quem é o CEO da Sinduspharma?", 
                     markdown=True)