An automated financial monitoring application built with Python that tracks daily stock price fluctuations using the Alpha Vantage API and dynamically queries the News API for contextual headlines when volatility thresholds are breached.

Features

Time Series Data Parsing: Extracts and cross-references historical closing values from structured nested JSON data payloads.
Volatility Percentage Calculation: Computes mathematical variance between consecutive trading intervals to identify rapid price movements.
Conditional Event Triggering: Initiatives downstream news search routines exclusively when calculated price swings cross a configured 2% delta window.
Automated Media Aggregation: Queries topical business headlines and trims results to deliver highly contextual data snippets directly to the processing loop.
