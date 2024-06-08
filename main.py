import os
import dotenv
dotenv.load_dotenv()

import agentops
agentops.init(os.environ['AGENTOPS_API_KEY'])

from small_agents import idea_analyst, idea_researcher
from small_tasks import research_idea_task, analyse_idea_task

from tools import search_tool

from crewai import Crew, Process

print("Hello, World!")
print("welcome to crewai-2")
print("-------------------")
idea= input("Enter the idea you want to research and analyse: ")

idea_analyst = idea_analyst(idea)
idea_researcher = idea_researcher(idea)

research_idea_task = research_idea_task(idea, tools=[search_tool], agent=idea_researcher)
analyse_idea_task = analyse_idea_task(idea, tools=[search_tool], agent=idea_analyst,context=[research_idea_task])

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[idea_researcher, idea_analyst],
  tasks=[research_idea_task, analyse_idea_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  # max_rpm=100,
  share_crew=True
)

#  inputs = { 'idea': 'D2C brand of Fox Nut as a healthy snack' }
# Starting the task execution process with enhanced feedback
result = crew.kickoff(inputs={'idea': idea})
print(result)
