import yfinance as yf

def get_stock_price(ticker: str) -> str:
    """Get the current stock price for a given ticker symbol."""
    try:
        stock = yf.Ticker(ticker)
        price = stock.fast_info['last_price']
        name = stock.info.get('longName', ticker)
        return f"{name} ({ticker.upper()}): ${price:.2f}"
    except Exception as e:
        return f"Could not retrieve data for '{ticker}'. Make sure it's a valid ticker symbol."

def calculate(expression: str) -> str:
    """Safely evaluate a math expression and return the result."""
    try:
        allowed = set("0123456789+-*/().% ")
        if not all(c in allowed for c in expression):
            return "Invalid expression. Only basic math operators are allowed."
        result = eval(expression)
        return f"{expression} = {result}"
    except Exception as e:
        return f"Could not calculate '{expression}'. Please check the expression."

def get_stock_summary(ticker: str) -> str:
    """Get a brief fundamental summary for a stock."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        name = info.get('longName', ticker)
        sector = info.get('sector', 'N/A')
        market_cap = info.get('marketCap', 0)
        pe_ratio = info.get('trailingPE', 'N/A')
        week_high = info.get('fiftyTwoWeekHigh', 'N/A')
        week_low = info.get('fiftyTwoWeekLow', 'N/A')
        cap_str = f"${market_cap:,.0f}" if market_cap else "N/A"
        return (
            f"{name} ({ticker.upper()})\n"
            f"  Sector: {sector}\n"
            f"  Market Cap: {cap_str}\n"
            f"  P/E Ratio: {pe_ratio}\n"
            f"  52-Week High: ${week_high}\n"
            f"  52-Week Low: ${week_low}"
        )
    except Exception as e:
        return f"Could not retrieve summary for '{ticker}'."