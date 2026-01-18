import yfinance as yf

def get_ticker_object(symbol):
    """Validates and returns a yfinance Ticker object."""
    # Simple correction logic
    if symbol.lower() == 'appl':
        symbol = 'AAPL'
    return yf.Ticker(symbol), symbol

def fetch_financial_data(ticker):
    """Gathers all raw data into a dictionary."""
    return {
        "history": ticker.history(period="5y"),
        "balance_sheet": ticker.balance_sheet,
        "financials": ticker.financials,
        "cashflow": ticker.cashflow,
        "info": ticker.info,
        "news": ticker.news
    }

def analyze_prices(historical_data):
    """Calculates price metrics."""
    close = historical_data['Close']
    return {
        "avg_close": close.mean(),
        "std_dev": close.std(),
        "high": close.max(),
        "low": close.min(),
        "avg_volume": historical_data['Volume'].mean()
    }
