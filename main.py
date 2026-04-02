from app.agents.scenario_agent import generate_scenario
from app.agents.tutor_agent import tutor_guidance

def main():
    role = "AI Engineer"

    scenario = generate_scenario(role)
    guidance = tutor_guidance(scenario)

    print("\n--- SCENARIO ---\n")
    print(scenario)

    print("\n--- TUTOR GUIDANCE ---\n")
    print(guidance)

if __name__ == "__main__":
    main()