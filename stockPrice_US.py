import yfinance as yf

# 定義股票代碼
ticker_symbol = 'AVUV'  # 例如 Apple Inc.

# 創建一個yfinance Ticker物件
ticker = yf.Ticker(ticker_symbol)

# 取得最新的收盤價格
closing_price = ticker.history(period='1d')['Close'].iloc[-1]

print(f'{ticker_symbol} 的最新收盤價格是: {closing_price}')
