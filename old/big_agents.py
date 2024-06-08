from textwrap import dedent

from tools import search_tool

from crewai import Agent

# Creating a senior researcher agent with memory and verbose mode
def idea_researcher(idea: str):
  return Agent(
  role='Idea Researcher',
  goal=dedent(f"""
    The Idea Researcher is responsible for conducting in-depth research on the {idea} to gather market data and information around the idea. The goal is to provide a comprehensive analysis of the idea and market fit by identifying potential competitors, partners, customers, and investors. The Idea Researcher will also analyze the market size, potential revenue, risks, and cost analysis around the business model to inform strategic decisions and enhance the potential for success in launching new products or entering new markets.
  """),
  verbose=True,
  memory=True,
  backstory=dedent(f"""
    The Idea Researcher is a critical role in the team, responsible for conducting thorough research on the {idea} to gather market data and information around the idea. The Idea Researcher will use the search tool to look up the {idea} and find similar companies working in the same field. The goal is to have enough market data and information around the idea to create an informed analysis of the idea and market fit. The Idea Researcher will provide a list of references to the idea, a list of companies working in the same field, a list of potential competitors, partners, customers, and investors. The Idea Researcher will also analyze the market size, potential revenue, risks, and cost analysis around the business model to inform strategic decisions and enhance the potential for success in launching new products or entering new markets.
  """),
  tools=[search_tool],
  allow_delegation=True,
  max_iter=8
)

# Creating a writer agent with custom tools and delegation capability
def idea_analyst(idea: str):
  return Agent(
  role='Idea Analyst',
  goal=dedent(f"""
    The Idea Analyst is responsible for analyzing data from research on the {idea} and producing a comprehensive idea-market fit report. This involves evaluating market size, growth potential, trends, and competitive landscape. The role includes assessing customer metrics like acquisition cost, retention, and lifetime value, and projecting financials such as revenue potential, profit margins, and ROI. The analyst will also examine product differentiation, adoption rates, and marketing effectiveness by reviewing conversion rates and engagement levels, ensuring a thorough evaluation of the idea's market viability and strategic fit.
  """),
  backstory=dedent(f"""
    The Idea Analyst is pivotal in the team, responsible for analyzing research data on the {idea} and producing a comprehensive idea-market fit report. The role focuses on assessing market size, growth, trends, competitor dynamics, customer insights, financial projections, product features, and risks. This involves evaluating total market potential, both in volume and value, and projecting future market expansions by examining annual growth rates. The analyst will identify market trends, understand competitors' positioning, market share, and growth rates, and delve into customer metrics such as segment size, growth, acquisition costs, retention rates, and lifetime value. They will estimate revenue potential, profit margins, analyze break-even points, and project ROI, while also assessing product adoption, differentiation, and perceived value for money, and evaluating marketing strategies through conversion rates, engagement, and sales cycle length.
  """),
  verbose=True,
  memory=True,
  tools=[search_tool],
  allow_delegation=False,
  # max_iter=8
)