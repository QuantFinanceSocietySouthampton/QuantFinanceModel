import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


# Functions used to import data from Yahoo Finance
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


# Plot S&P 500 market data
plot_symbol("^GSPC", '2000-01-28', '2024-01-26', 'r')

# Predefining parameters
growthRate = 0.08
pi = np.pi
t = np.linspace(1, 100, 6036)

# Model Evolution
# To use these, remove the comment from the line you want to run, while commenting the rest, and run the program

x = np.exp(growthRate*t)

# x = np.exp(growthRate*t) + 5*np.sin(2*pi*1*t)

# x = np.exp(growthRate*t) + 0.4*np.exp(growthRate*t)*(np.sin(2*pi*0.25*t))

# x = 1000 + np.exp(growthRate*t)*(1 + 0.1*np.sin(2*pi*1*t) + 0.2*np.sin(2*pi*0.25*t) + 0.08*np.sin(2*pi*0.35*t))


# Plot evolution against market data
plt.plot(t, get_data("^GSPC", '2000-01-28', '2024-01-26')['Adj Close'], color='r', linewidth=0.7)
plt.plot(t, x, color='green', linewidth=0.7)
plt.show()

# Plot market cycles
t = t[0:int(len(t)/4)]
cycles = 0.1*np.sin(2*pi*1*t) + 0.2*np.sin(2*pi*0.25*t) + 0.08*np.sin(2*pi*0.35*t)
plt.figure(figsize=(9,5))
plt.plot(t, cycles)
plt.title("Market Cycles")
plt.show()
