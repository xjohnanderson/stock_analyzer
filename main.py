from stock_utils import get_ticker_object, fetch_financial_data, analyze_prices

def run_report():
    raw_input = input("Please enter the stock ticker symbol: ")
    ticker_obj, validated_symbol = get_ticker_object(raw_input)
    
    print(f"--- Processing {validated_symbol} ---")
    
    # Fetch
    data = fetch_financial_data(ticker_obj)
    
    # Analyze
    price_metrics = analyze_prices(data['history'])
    
    # Output Example
    print(f"5-Year Average: ${price_metrics['avg_close']:.2f}")
    
    # (You would add more print or save logic here)

if __name__ == "__main__":
    run_report()
