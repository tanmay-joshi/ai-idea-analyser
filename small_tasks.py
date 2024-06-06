from crewai import Task
from tools import search_tool

from textwrap import dedent

# Research task
def research_idea_task(idea: str, tools, agent):
    return Task(
  description=dedent(f"""
    use the search tool to look up the {idea} and find similar companies who are working in the same field
    The goal is to have enough market data and information around the idea to create an informed analysis of the idea and market fit.
    """
  ),
  expected_output=dedent(f"""
    - "A list of references to the idea"
    - "A list of companies working in the same field"
    - "Market size and potential revenue that can be generated"
    - "A list of potential risks"
    - "Cost analysis around the business model"
    """),
  tools=tools,
  agent=agent,
)

# Writing task with language model configuration
def analyse_idea_task(idea, tools, agent):
    return Task(
  description=dedent(f"""
        Take the information gathered from the research task around the {idea}, analyse it, and provide a idea-market fit analysis report by focusing on essential aspects such as market size and growth, trends, competitor dynamics, customer insights, financial projections, product features, and risks. Dive into evaluating the total market potential both in terms of volume and value, and examine the annual growth rates to project future market expansions. Identify and analyze market trends, understanding the positioning, market share, and growth rates of competitors. Delve into customer metrics by assessing the size and growth of target segments, calculating the customer acquisition cost, retention rates, and customer lifetime value. Estimate the revenue potential and profit margins, analyze the break-even point and the expected return on investment. Assess the product's adoption rate, differentiation, and perceived value for money. Evaluate marketing strategies through conversion rates, engagement levels, and sales cycle length. Finally, consider potential risks including market entry barriers, regulatory compliance costs, and technology risks to fully understand the challenges and opportunities in the market. This approach ensures a robust analysis to inform strategic decisions and enhance the potential for success in launching new products or entering new markets.            
    """),
  expected_output=dedent(f"""
    - "Market size and growth"
    - "Trends"
    - "Competitor dynamics"
    - "Customer insights"
    - "Financial projections"
    - "Product features"
    - "Risks"
    - "Total market potential"
    - "Growth rates"
    - "Customer segments"
    - "Customer acquisition cost"
    - "Retention rates"
    - "Customer lifetime value"
    - "Revenue potential"
    - "Profit margins"
    - "Break-even point"
    - "Return on investment"
    - "Product adoption rate"
    - "Differentiation"
    - "Perceived value for money"
    - "Marketing strategies"
    - "Sales cycle length"
    - "Potential risks"
    - "Market entry barriers"
    - "Regulatory compliance costs"
    A report that includes all the above information and analysis in a crisp and straightforward manner.
    """),
  tools=tools,
  agent=agent,
  async_execution=False,
  output_file="{idea}.md"  # Example of output customization
)

