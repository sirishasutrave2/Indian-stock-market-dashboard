\# Indian Stock Market Performance Dashboard



\## Project Overview



The \*\*Indian Stock Market Performance Dashboard\*\* is a data analytics and visualization project developed to analyze stock market performance using historical stock price data. The project provides insights into top-performing and worst-performing stocks, sector-wise stock trends, cumulative returns, and market performance through interactive dashboards.



The project integrates \*\*Python, SQL, Power BI, and Streamlit\*\* to create an end-to-end stock analysis system.



\---



\## Objectives



\* Analyze historical stock market performance.

\* Identify \*\*top-performing and worst-performing stocks\*\*.

\* Perform \*\*sector-wise stock analysis\*\*.

\* Visualize stock trends using \*\*Power BI\*\* and \*\*Streamlit dashboards\*\*.

\* Store cleaned stock data in a structured format for efficient querying.



\---



\## Features



\### 1. Top 10 Gainers Analysis



\* Identifies top-performing stocks based on returns.

\* Visualized using bar charts.



\### 2. Top 10 Losers Analysis



\* Displays lowest-performing stocks.

\* Helps understand market downturns.



\### 3. Sector-wise Performance



\* Classifies stocks by sectors.

\* Calculates average sector returns.

\* Displays sector performance comparison.



\### 4. Cumulative Return Analysis



\* Shows trend of top-performing stocks over time.

\* Helps analyze long-term growth.



\### 5. Interactive Filtering



\* Sector-based filtering using Streamlit sidebar.

\* Dynamic visualizations.



\---



\## Tech Stack



\### Programming Language



\* Python



\### Database



\* Sqlite3



\### Libraries Used



\* Pandas

\* Matplotlib

\* Seaborn

\* Streamlit



\### Visualization Tools



\* Power BI

\* Streamlit



\---



\## Project Structure



```

stock-project/

│── app.py

│── stock\\\_cleaning.py

│── stock\\\_insert.py

│── stock\\\_analysis.py

│── stock.db

│── cleaned\\\_stock\\\_data.csv

│── stock\\\_dashboard.pbix

│── README.md

│── requirements.txt

│── csv\\\_output.zip



```



\---



\## Workflow



\### Step 1: Data Collection



\* Historical stock market data collected.

\* Raw dataset imported into Python.



\### Step 2: Data Cleaning



\* Missing values handled.

\* Duplicate records removed.

\* Date formatting corrected.

\* Sector mapping added.



\### Step 3: Data Processing



\* Calculated:



&#x20; \* Daily returns

&#x20; \* Cumulative returns

&#x20; \* Yearly returns

\* Sector classification performed.



\### Step 4: Database Storage



\* Cleaned dataset stored in SQL database.



\### Step 5: Data Visualization



\#### Power BI Dashboard



Created:



\* KPI Cards

\* Top 10 Gainers

\* Top 10 Losers

\* Sector Performance

\* Trend Analysis

\* Interactive Slicers



\#### Streamlit Dashboard



Created:



\* Interactive stock dashboard

\* Sector filtering

\* Dynamic charts

\* KPI metrics



\---



\## Installation \& Execution



\### Clone Repository



```bash

git clone https://github.com/Sirisha Jemene/stock\_market\_dashboard.git

cd stock\_market\_dashboard

```



\### Install Dependencies



```bash

pip install -r requirements.txt

```



\### Run Streamlit Application



```bash

python -m streamlit run app.py

```



\---



\## Dashboard Preview



\### Power BI Dashboard



Includes:



\* Total Stocks

\* Average Close Price

\* Average Volume

\* Top Gainers \& Losers

\* Sector-wise Performance



\### Streamlit Dashboard



Interactive web dashboard with:



\* Sector filter

\* Stock trends

\* Cumulative returns

\* Market insights



\---



\## Results



\* Developed a fully functional stock analysis dashboard.

\* Generated insights on market trends and sector performance.

\* Enabled interactive exploration using Power BI and Streamlit.



\---



\## Coding Standards



This project follows \*\*PEP 8 Python Coding Standards\*\*:



https://www.python.org/dev/peps/pep-0008/



\---



\## Future Enhancements



\* Real-time stock market API integration.

\* Predictive stock price analysis using Machine Learning.

\* Advanced financial indicators.

\* Live dashboard deployment.



\---



\## Author



\*\*Sirisha Jemene\*\*

