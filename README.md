# AI CLI Agent — Financial Assistant

A Python-based agentic CLI assistant that accepts natural language tasks, selects the appropriate tool via a reasoning model, and returns structured results. Built to demonstrate core AI agent and orchestration concepts.

## Features

- Natural language input via command line
- LLM-powered tool selection and orchestration (Groq + LLaMA 3.3 70B)
- Multi-turn conversation memory across a session
- Three built-in financial tools:
  - **Stock Price Lookup** — fetches real-time price data via yfinance
  - **Stock Summary** — returns sector, market cap, P/E ratio, and 52-week range
  - **Calculator** — evaluates natural language math expressions

## Demo
```
You: What is Apple's stock price?
Agent: The current price of Apple's stock (AAPL) is $248.80.

You: Give me a summary of Tesla
Agent: Tesla, Inc. (TSLA) is in the Consumer Cyclical sector with a
market cap of over $1.35 trillion. 52-week range: $214.25 – $498.83.

You: What is 15% of 248.80?
Agent: 15% of 248.80 is 37.32.
```

## Project Structure
```
ai-cli-agent/
├── main.py        # Entry point and chat loop
├── agent.py       # LLM integration and tool orchestration logic
├── tools.py       # Tool implementations (stock data, calculator)
├── .env           # API key storage (not tracked in git)
├── .gitignore     # Excludes .env and cache files
└── README.md      # Project documentation
```

## Setup

1. Clone the repository
```bash
   git clone https://github.com/devonboone-dev/ai-cli-agent.git
   cd ai-cli-agent
```

2. Install dependencies
```bash
   pip install groq yfinance python-dotenv
```

3. Create a `.env` file and add your Groq API key
```
   GROQ_API_KEY=your_key_here
```

4. Run the agent
```bash
   python main.py
```

## Technologies

- **Python 3.12**
- **Groq API** (LLaMA 3.3 70B) — LLM reasoning and tool selection
- **yfinance** — real-time stock market data
- **python-dotenv** — environment variable management

## Author

Devon Boone — [LinkedIn](https://www.linkedin.com/in/devonboone-22415b107/) | [GitHub](https://github.com/devonboone-dev)