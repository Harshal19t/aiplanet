from crew import ResearchCrew

def main(company_name):
    # Initialize CrewAI and ResearchCrew
    research_crew = ResearchCrew(company_name)
    
    # Gather research information
    research_data = research_crew.gather_research()
    
    # Print the output for each section
    print(f"### Research Results for {company_name} ###\n")
    print("#### Industry Information:\n")
    for industry_point in research_data['industry_info']:
        print(f"- {industry_point}\n")

    print("#### Company Strategy & Focus Areas:\n")
    for company_point in research_data['company_info']:
        print(f"- {company_point}\n")

# Run the research process for a sample company
main("Google")