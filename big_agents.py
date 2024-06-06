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
  description=dedent(f"""
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
    The Idea Analyst is responsible for analyzing the information gathered from the research task around the {idea} and providing an idea-market fit analysis report. The Idea Analyst will focus on essential aspects such as market size and growth, trends, competitor dynamics, customer insights, financial projections, product features, and risks. The Idea Analyst will evaluate the total market potential both in terms of volume and value, and examine the annual growth rates to project future market expansions. The Idea Analyst will identify and analyze market trends, understanding the positioning, market share, and growth rates of competitors. The Idea Analyst will delve into customer metrics by assessing the size and growth of target segments, calculating the customer acquisition cost, retention rates, and customer lifetime value. The Idea Analyst will estimate the revenue potential and profit margins, analyze the break-even point and the expected return on investment. The Idea Analyst will assess the product's adoption rate, differentiation, and perceived value for money. The Idea Analyst will evaluate marketing strategies through conversion rates, engagement levels, and sales cycle length. Finally, the Idea Analyst will consider potential risks including market entry barriers, regulatory compliance costs, and technology risks to fully understand the challenges and opportunities in the market. This approach ensures a robust analysis to inform strategic decisions and enhance the potential for success in launching new products or entering new markets.
  """),
  description= dedent(f"""
    he Idea Analyst is responsible for analyzing the information gathered from the research task around the {idea} and providing an idea-market fit analysis report. The Idea Analyst will focus on essential aspects such as market size and growth, trends, competitor dynamics, customer insights, financial projections, product features, and risks. The Idea Analyst will evaluate the total market potential both in terms of volume and value, and examine the annual growth rates to project future market expansions. The Idea Analyst will identify and analyze market trends, understanding the positioning, market share, and growth rates of competitors. The Idea Analyst will delve into customer metrics by assessing the size and growth of target segments, calculating the customer acquisition cost, retention rates, and customer lifetime value. The Idea Analyst will estimate the revenue potential and profit margins, analyze the break-even point and the expected return on investment. The Idea Analyst will assess the product's adoption rate, differentiation, and perceived value for money. The Idea Analyst will evaluate marketing strategies through conversion rates, engagement levels, and sales cycle length. Finally, the Idea Analyst will consider potential risks including market entry barriers, regulatory compliance costs, and technology risks to fully understand the challenges and opportunities in the market. This approach ensures a robust analysis to inform strategic decisions and enhance the potential for success in launching new products or entering new markets.
  """)
  ,
  backstory=dedent(f"""
    The Idea Analyst is a critical role in the team, responsible for analyzing the information gathered from the research task around the {idea} and providing an idea-market fit analysis report. The Idea Analyst will take the information gathered from the research task around the {idea}, analyze it, and provide an idea-market fit analysis report by focusing on essential aspects such as market size and growth, trends, competitor dynamics, customer insights, financial projections, product features, and risks. The Idea Analyst will dive into evaluating the total market potential both in terms of volume and value, and examine the annual growth rates to project future market expansions. The Idea Analyst will identify and analyze market trends, understanding the positioning, market share, and growth rates of competitors. The Idea Analyst will delve into customer metrics by assessing the size and growth of target segments, calculating the customer acquisition cost, retention rates, and customer lifetime value. The Idea Analyst will estimate the revenue potential and profit margins, analyze the break-even point and the expected return on investment. The Idea Analyst will assess the product's adoption rate, differentiation, and perceived value for money. The Idea Analyst will evaluate marketing strategies through conversion rates, engagement levels, and sales cycle length. Finally, the Idea Analyst will consider potential risks including market entry barriers, regulatory compliance costs, and technology risks to fully understand the challenges and opportunities in the market. This approach ensures a robust analysis to inform strategic decisions and enhance the potential for success in launching new products or entering new markets.
  """),
  verbose=True,
  memory=True,
  tools=[search_tool],
  allow_delegation=False,
  max_iter=8
)