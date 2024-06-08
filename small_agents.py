from textwrap import dedent

from tools import search_tool

from crewai import Agent

# Creating a senior researcher agent with memory and verbose mode
def idea_researcher(idea: str):
  return Agent(
    role= "Senior Idea Researcher",
    goal= dedent( f"""Collect as many data points for the {idea} as possible to provide a comprehensive analysis of the idea, market fit, market size."""),
    backstory= dedent( f"""Recognized as reputed Idea researcher, I make my research reports data oriented to help understand the market around the idea: {idea}."""),
  verbose=True,
  memory=True,
  tools=[search_tool],
  allow_delegation=True
)

# Creating an Idea analyst agent with custom tools and delegation capability
def idea_analyst(idea: str):
  return Agent(
    role= "Senior Idea Analyst",
    goal= dedent( f"""Understand and expand upon the report that I got, make sure they are great and focus on real market. Expert analysis around the market of {idea}."""),
    backstory= dedent( f"""Reputed Expert Idea Analyst, I make sure to provide a comprehensive analysis of the market. Currently you are analysing the idea: {idea}."""),
  verbose=True,
  memory=True,
  tools=[search_tool],
  allow_delegation=False
)