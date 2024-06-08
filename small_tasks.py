from crewai import Task
from tools import search_tool

from textwrap import dedent

# Research task
def research_idea_task(idea: str, tools, agent):
    return Task(
  description=dedent(f"""
    Research the {idea} and get the data points of the market size, and if the idea can be converted into a real business. Create an analysis report.
    """
  ),
  expected_output=dedent(f"""
    - "A list of references to the idea"
    - "A list of companies working in the same field"
    - "Market size and potential revenue that can be generated"
    """),
  tools=tools,
  agent=agent,
)

# Writing task with language model configuration
def analyse_idea_task(idea, tools, agent, context):
    return Task(
  description=dedent(f"""
        Create an analysis report on the {idea} based on the data points provided. The report should include market size, growth potential, trends, competitor dynamics, and other relevant information.        
    """),
  expected_output=dedent(f"""
      A report that includes all the below information and analysis in a crisp and straightforward manner:
    - "Market size and growth"
    - "Trends"
    - "Competitor dynamics"
    - "Market entry barriers"
    - "Regulatory compliance costs"
   
    """),
  tools=tools,
  agent=agent,
  context=context,
  async_execution=False,
  output_file=f"{idea}.md"  # Example of output customization
)

