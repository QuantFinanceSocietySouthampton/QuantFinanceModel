import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


def get_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data


def get_data(ticker, start_date, end_date):
    data = yf.download(ticker, start_date, end_date)
    return data


def plot_symbol(symbol, start, end, color='black'):
    ticker = get_data(symbol, start, end)
    name = yf.Ticker(symbol).info['shortName']
    plt.plot(ticker['Adj Close'], color=color)
    plt.xlabel("Date")
    plt.ylabel(f"{name} Price")
    plt.title(f"{name} Over Time")
    plt.show()


# Plot stock data
# plot_symbol("^GSPC", '2000-01-28', '2024-01-26', 'r')

growthRate = 0.08
pi = np.pi

t = np.linspace(1, 100, 6036)

# Evolution
# x = np.exp(growthRate*t)

# x = np.exp(growthRate*t) + np.sin(2*pi*1*t)

# x = np.exp(growthRate*t) + (np.exp(growthRate*t)*(np.sin(2*pi*1*t)))/2
# plt.plot(t, np.exp(growthRate*t), linestyle='--', color='k')

# x = 1000+ np.exp(growthRate*t) + 0.2*np.exp(growthRate*t)*(np.sin(2*pi*0.25*t))
# plt.plot(t, 0.5*np.exp(growthRate*t), linestyle='--', color='k')
# plt.plot(t, 1.5*np.exp(growthRate*t), linestyle='--', color='k')

# x = np.exp(growthRate*t) + np.exp(growthRate*t)*( 0.035*np.sin(2*pi*4*t) + 0.1*np.sin(2*pi*0.25*t) )

x = 1000 + np.exp(growthRate*t) + 0.1*np.exp(growthRate*t)*(np.sin(2*pi*1*t) + np.sin(2*pi*0.25*t) + np.sin(2*pi*0.35*t))

plt.plot(t, get_data("^GSPC", '2000-01-28', '2024-01-26')['Adj Close'], color='r', linewidth=0.7)
plt.plot(t, x, color='green', linewidth=0.7)
plt.show()

# Plot market cycles
# plt.plot(t, (np.sin(2*pi*1*t) + np.sin(2*pi*0.25*t) + np.sin(2*pi*0.35*t)))
plt.plot(t, ( 0.035*np.sin(2*pi*5*t) + 0.1*np.sin(2*pi*0.25*t) + 0.15*np.sin(2*pi*0.4*t) ))
plt.show()
