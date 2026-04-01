from app.agents.scenario_agent import generate_scenario

def main():
    role = "AI Engineer"
    
    scenario = generate_scenario(role)

    print("\n--- SCENARIO ---\n")
    print(scenario)

if __name__ == "__main__":
    main()