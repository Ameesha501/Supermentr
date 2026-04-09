

# Step 1: Define Tools
def search_tool(query):
    return f"Searching Google for: {query}"

def calculator_tool(expression):
    return eval(expression)

# NEW: Weather Tool (dummy API simulation)
def weather_tool(city):
    return f"Weather in {city}: 28°C, Sunny"

# NEW: File Reader Tool
def file_reader_tool(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except:
        return "File not found"

# Step 2: Memory
memory = []

# Step 3: Planner
def planner(goal):
    if "calculate" in goal:
        return ["extract math", "calculate result"]
    elif "search" in goal:
        return ["search internet"]
    elif "weather" in goal:
        return ["get weather"]
    elif "file" in goal:
        return ["read file"]
    else:
        return ["think", "respond"]

# Step 4: Execution
def execute(plan, goal):
    for step in plan:
        print("Step:", step)

        if step == "search internet":
            print(search_tool(goal))

        elif step == "calculate result":
            expr = goal.split("calculate")[-1]
            print(calculator_tool(expr))

        elif step == "get weather":
            city = goal.split("in")[-1].strip()
            print(weather_tool(city))

        elif step == "read file":
            filename = goal.split("file")[-1].strip()
            print(file_reader_tool(filename))

        else:
            print("Thinking...")

# Step 5: Agent Runner
def run_agent():
    goal = input("Enter your goal: ")
    plan = planner(goal)
    print("\nPlan:", plan)
    execute(plan, goal)

run_agent()