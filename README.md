# **Stock Price Data Retrieval and Analysis**

## **Overview**

This project consists of multiple Python scripts designed to retrieve and analyze stock price data from various financial data APIs. The scripts cover different functionalities, including fetching the latest prices of specific stocks, listing the top 10 active companies from a stock market list, and summarizing data for easier interpretation. The APIs utilized in this project include Alpha Vantage, IEX Cloud, and Polygon.

## **Features**

- **Latest Price Retrieval**: Fetches the latest stock price for a given list of companies (e.g., AAPL, MSFT, GOOG) using Alpha Vantage API.
- **Top 10 Companies**: Retrieves the top 10 most active companies from IEX Cloud API.
- **Stock Price Fetch**: Gathers the stock prices for specific companies using the Polygon API.
- **Data Summarization**: Summarizes the fetched data using OpenAI's GPT-based API for concise reporting.

## **Installation**

To run these scripts, you need to install the necessary Python packages. Run the following command:

```bash
pip install requests json
```
## **Usage**

- **Alpha Vantage for Latest Prices**:
  - Set your Alpha Vantage API key.
  - Call `get_latest_price(symbol)` with the stock symbol as an argument.

- **IEX Cloud for Top 10 Companies**:
  - Initialize `IEXCloudAPI` with your IEX Cloud API key.
  - Use `get_top_10_companies()` to retrieve the list.

- **Polygon for Stock Prices**:
  - Initialize `PolygonAPI` with your Polygon API key.
  - Use `get_stock_price(symbol)` for each company symbol.

- **OpenAI for Data Summarization**:
  - Initialize `OpenAIAPI` with your OpenAI API key.
  - Use `summarize_data(data)` to get a summarized version of the input data.

## **Examples**

Refer to the script comments for detailed examples of how to use each functionality.

## **API Keys**

Please note that you need to obtain your own API keys from Alpha Vantage, IEX Cloud, Polygon, and OpenAI to use these scripts.

## **License**

Distributed under the MIT License. See `LICENSE` for more information.

## **Contact**

Pull requests and suggestions are welcome on this repository. For any questions, feedback, or if you'd like to collaborate, feel free to reach out at any time. Contact me at: [vsm220003@utdallas.edu](mailto:vsm220003@utdallas.edu)
