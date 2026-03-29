from agent import run_agent

def main():
    print("=" * 50)
    print("  AI CLI Agent — Financial Assistant")
    print("  Type 'quit' or 'exit' to stop")
    print("=" * 50)
    print()

    history = []

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit"):
            print("Agent: Goodbye!")
            break

        response = run_agent(user_input, history)
        print(f"\nAgent: {response}\n")

        # Save to memory
        history.append({"role": "user", "content": user_input})
        history.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()