import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import subprocess
st.set_page_config(
    page_title="Conjexure | Google Blog",
    page_icon="📈",
)
st.markdown("""
<style>
    .st-ef {
        display: flex;
        justify-content: center;
        margin-top: 160px;
    }
</style>
""", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    if st.button("RETURN TO HOME"):
        # Code to execute when the button is clicked
        subprocess.run(["streamlit", "run", "stockpricepred.py"], check=True)

with col2:
    if st.button("APPLE BLOG"):
        # Code to execute when the button is clicked
        subprocess.run(["streamlit", "run", "blog_apple.py"], check=True)
# Title and Introduction
st.title("A Journey Through Google's Stock Prices Over the Years")

st.write(
    "Google, now known as Alphabet Inc., is one of the technology giants that have shaped the digital landscape over the past two decades. Its journey from a small startup to a global tech powerhouse has been closely followed by investors. In this blog, we will delve into the historical stock prices of Google (GOOGL) and explore the key factors that have influenced its performance over the years."
)

# The Early Days (2004-2008)
st.header("The Early Days (2004-2008)")
st.markdown(
    """
- Google's Initial Public Offering (IPO): Google went public on August 19, 2004, with an IPO price of $85 per share. This marked the beginning of its journey as a publicly traded company.
- Early Success: The stock quickly gained momentum, surpassing the $100 mark in the months following the IPO. Google's innovative search technology and advertising business contributed to its growth.
- The 2008 Financial Crisis: The stock experienced a significant dip during the global financial crisis, falling below $300 per share. This downturn was a reflection of the broader economic challenges at the time.
"""
)

# The Mid-2010s (2010-2015)
st.header("The Mid-2010s (2010-2015)")
st.markdown(
    """
- Recovery and Growth: Google's stock rebounded strongly from the 2008 crisis, reaching new heights as the company expanded into various new ventures, including Android and YouTube.
- The Split: In 2014, Google underwent a stock split, creating a new class of shares, Google Class C shares, which traded under the ticker symbol GOOG, while the original shares became GOOGL. This was done to maintain control over the company.
- Hitting the $1,000 Mark: In 2017, Google's stock price surpassed the $1,000 mark for the first time, reflecting its dominant position in the online advertising industry and its growing cloud business.
"""
)

# The Recent Years (2016-2022)
st.header("The Recent Years (2016-2022)")
st.markdown(
    """
- Regulatory Scrutiny: In recent years, Google, like other tech giants, faced increased regulatory scrutiny regarding issues such as antitrust and data privacy. These concerns have occasionally put pressure on the stock.
- Competition: Google faces fierce competition in the tech industry, particularly from companies like Amazon, Facebook, and Apple. Investors closely watch how Google navigates this competitive landscape.
- COVID-19 Pandemic: The pandemic had mixed effects on Google's stock. While its advertising business faced challenges due to reduced marketing budgets, its cloud services and digital advertising platforms witnessed increased demand.
"""
)

# The Current Year (2023)
st.header("The Current Year (2023)")
st.markdown(
    """
As of the latest data available, Alphabet Inc.'s stock price was $123.441. The stock price started in 2023 at $88.73 and increased by 55% from the beginning of the year. The forecasted Google price at the end of 2023 is $1512, and some predictions even suggest it could reach $1433.
"""
)

# The Present and Future
st.header("The Present and Future")
st.markdown(
    """
- As of my last knowledge update in January 2022, Google's stock price was around $2,000 per share. However, you should check the most recent data to get an accurate picture of the current stock price.
- Alphabet Inc.'s diverse portfolio now includes Google Search, YouTube, Google Cloud, Waymo (self-driving cars), and other ventures. The company's ability to innovate and expand into new markets will continue to be a critical factor in its stock's performance.
- Investors will closely follow developments in areas like artificial intelligence, quantum computing, and regulatory matters to assess the future trajectory of Google's stock.
"""
)

# Conclusion
st.header("Conclusion")
st.markdown(
    "Google's stock prices have seen significant ups and downs over the years, reflecting the evolving tech landscape and global economic conditions. For the most current information, it's crucial to check real-time stock data and stay informed about the factors influencing Alphabet Inc.'s performance. Google's journey from a search engine startup to a multifaceted tech conglomerate continues to captivate investors and analysts alike."
)

# Disclaimer
st.markdown(
    "Disclaimer: Stock prices are subject to change rapidly, and this blog is intended for informational purposes only. Please consult a financial advisor or reliable financial sources for the most up-to-date information and investment advice."
)
