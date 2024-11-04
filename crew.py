from agents import IndustryResearchAgent

class ResearchCrew:
    def __init__(self, company_name):
        self.agent = IndustryResearchAgent(company_name)
    
    def gather_research(self):
        # Execute the agent and gather research data
        research_data = self.agent.execute()
        return research_data