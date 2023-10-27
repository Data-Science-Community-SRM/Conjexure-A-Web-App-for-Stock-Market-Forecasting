import streamlit as st
import yfinance as yf
import subprocess
st.set_page_config(
    page_title="Conjexure | Apple Blog",
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
col1, col2= st.columns(2)

with col1:
    if st.button("RETURN TO HOME"):
        # Code to execute when the button is clicked
        subprocess.run(["streamlit", "run", "stockpricepred.py"], check=True)

with col2:
    if st.button("GOOGLE BLOG"):
        # Code to execute when the button is clicked
        subprocess.run(["streamlit", "run", "blog_google.py"], check=True)
st.title("Apple Stock Prices: A Comprehensive Analysis")

st.write("Apple Inc. is a company that needs no introduction. Over the years, it has transformed the way we live, work, and communicate. But what about the company's stock prices? How have they evolved, and what key events have shaped the trajectory of Apple's stock over time? In this comprehensive analysis, we will dive deep into the world of Apple's stock prices, exploring the historical trends, significant milestones, and the factors that have influenced its performance.")

st.header("The Journey Begins")

st.write("Apple Inc. went public on December 12, 1980, with an initial public offering (IPO) that set the stage for one of the most remarkable journeys in the history of the stock market. At that time, Apple's IPO price was $22 per share. Little did anyone know that this was just the beginning of a remarkable ascent.")

st.header("The 1980s: The Era of the Macintosh")

st.write("The 1980s were marked by the rise of the Macintosh, Apple's iconic personal computer. This innovation propelled Apple's stock prices, and by the end of the decade, Apple was trading at around $16 per share. It was clear that Apple was here to stay, and investors who believed in the company's vision were handsomely rewarded.")

st.header("The Turbulent 1990s")

st.write("The 1990s were a tumultuous period for Apple. The departure of Steve Jobs in 1985 and subsequent leadership changes left the company struggling. Apple's stock prices were on a rollercoaster, experiencing significant volatility. By the end of the decade, Apple was trading at around $3 per share, a far cry from its earlier highs.")

st.header("The Resurgence: Return of Steve Jobs")

st.write("The turning point for Apple came with the return of Steve Jobs in 1997. With the introduction of the iMac and later the revolutionary iPod, Apple's stock prices began a remarkable climb. The iPod, in particular, not only transformed the way we listened to music but also contributed significantly to Apple's financial success.")

st.header("The iPhone Revolution")

st.write("In 2007, Apple introduced the iPhone, a device that would go on to change the world. The iPhone's impact on Apple's stock prices was nothing short of phenomenal. The stock surged as the iPhone became a global sensation. By 2008, Apple's stock price had reached the $200 mark, and it continued to climb steadily.")

st.header("The Era of Innovation")

st.write("The subsequent years were marked by a series of groundbreaking products, from the iPad to the Apple Watch. Apple's relentless commitment to innovation, design, and user experience resonated with consumers and investors alike. Stock prices soared as Apple's market capitalization reached unprecedented levels.")

st.header("Stock Splits")

st.write("Apple's decision to split its stock played a role in shaping its stock prices. In 2014, Apple executed a 7-for-1 stock split, making shares more affordable for individual investors. This move boosted demand for Apple's stock and contributed to its upward trajectory.")

st.header("A Trillion-Dollar Milestone")

st.write("In August 2018, Apple became the first publicly traded company to reach a market capitalization of $1 trillion. This historic achievement was reflected in its stock price, which continued to rise steadily. Apple had firmly established itself as a tech giant, and investors reaped the rewards.")

st.header("Market Fluctuations and Challenges")

st.write("Despite its impressive run, Apple faced challenges. Economic downturns, competition from rivals, and concerns about market saturation occasionally put pressure on Apple's stock prices. Events like the U.S.-China trade tensions and the COVID-19 pandemic had their impact on the stock's performance.")

st.header("The Present and the Future")

st.write("As of my last knowledge update in January 2022, Apple's stock price was approximately $150 per share. However, it's important to note that stock prices are highly dynamic and subject to change. To get the most accurate and up-to-date information, it's crucial to check real-time stock data and stay informed about the factors influencing Apple's performance.")

st.write("Apple's future prospects remain promising. The company's diverse product portfolio now includes not only the iPhone but also the Mac, iPad, and services like Apple Music and Apple TV+. Its foray into wearables and healthcare technology demonstrates its commitment to innovation. Apple's ability to navigate regulatory challenges and evolving consumer preferences will continue to influence its stock prices.")

st.header("Conclusion")

st.write("The journey of Apple's stock prices is a testament to the power of innovation, brand loyalty, and visionary leadership. From the humble beginnings of its IPO in 1980 to becoming a trillion-dollar company, Apple's stock has been a success story that has captivated investors worldwide.")

st.write("However, it's important to remember that investing in the stock market carries inherent risks. Stock prices are influenced by a multitude of factors, including economic conditions, competition, and market sentiment. Before making any investment decisions, it's advisable to consult with a financial advisor and conduct thorough research.")

st.write("Apple's stock prices have seen both peaks and valleys, reflecting the ever-evolving landscape of technology and consumer preferences. For investors and enthusiasts alike, the journey of Apple's stock remains an exciting and dynamic narrative that will continue to unfold in the years to come.")
