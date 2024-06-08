import os
import dotenv
dotenv.load_dotenv()

import agentops
agentops.init(os.environ['AGENTOPS_API_KEY'])

from small_agents import idea_analyst as IdeaAnalyst, idea_researcher as IdeaResearcher
from small_tasks import research_idea_task as ResearchIdeaTask, analyse_idea_task as AnalyseIdeaTask
from tools import search_tool
from crewai import Crew, Process

def research_and_analyse_idea(idea):
    idea_analyst = IdeaAnalyst(idea)
    idea_researcher = IdeaResearcher(idea)

    research_idea_task = ResearchIdeaTask(idea, tools=[search_tool], agent=idea_researcher)
    analyse_idea_task = AnalyseIdeaTask(idea, tools=[search_tool], agent=idea_analyst, context=[research_idea_task])

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

    # Starting the task execution process with enhanced feedback
    result = crew.kickoff(inputs={'idea': idea})
    return result

# Example usage
# idea = "D2C brand of Fox Nut as a healthy snack"
# result = research_and_analyse_idea(idea)
# print(result)
