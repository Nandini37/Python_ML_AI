

import yfinance as yf
import streamlit as st
from datetime import datetime

# Get today's date
today = datetime.today().strftime('%Y-%m-%d')



# Use markdown to inject HTML and CSS for the background color
st.markdown(
    """
    <style>
    body {
        background-color: #ADD8E6; /* Light blue background */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Stock Price Application")

st.write("""

Enter the Ticker Symbol

""")

#define the ticker symbol
tickerSymbol = st.text_input("TickerSymbol: ")


if tickerSymbol:
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2010-5-31', end=today)
    # Open	High	Low	Close	Volume	Dividends	Stock Splits

   
    st.write(f"""

    Shown are the stock closing price and volume of {tickerSymbol}

    """)
    st.line_chart(tickerDf.Close)
    st.line_chart(tickerDf.Volume)
else:
    st.warning("Please enter a valid ticker symbol.")    