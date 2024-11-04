from tavily import TavilyClient
from crewai import CrewAI, Agent

# Initialize Tavily client for web search
tavily_client = TavilyClient(api_key='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')

# Initialize CrewAI
crew_ai = CrewAI()

class IndustryResearchAgent(Agent):
    def __init__(self, company_name):
        self.company_name = company_name

    def perform_industry_research(self):
        # Perform search for industry information based on the company name
        industry_results = tavily_client.search(f"{self.company_name} industry analysis")
        return [result['summary'] for result in industry_results[:3]]

    def perform_company_research(self):
        # Perform search to gather company-specific focus areas
        company_results = tavily_client.search(f"{self.company_name} strategy focus")
        return [result['summary'] for result in company_results[:3]]

    def execute(self):
        # Execute both tasks and return the combined research information
        industry_info = self.perform_industry_research()
        company_info = self.perform_company_research()
        return {
            "industry_info": industry_info,
            "company_info": company_info
        }