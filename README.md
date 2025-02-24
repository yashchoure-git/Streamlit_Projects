
# Stock Price Prediction using Streamlit

## Overview
This project is a Stock Price Prediction web application built using **Streamlit**, **Scikit-learn**, and **Matplotlib**. The app allows users to analyze historical stock price trends and predict future prices using Machine Learning models.

## Features
- **Stock Data Visualization**: Displays historical stock prices with interactive charts.
- **Data Preprocessing**: Handles missing values and normalizes data for better model performance.
- **Machine Learning Models**:
  - Linear Regression
  - LSTM (Long Short-Term Memory) Neural Network
- **Prediction Results**: Provides a forecast of future stock prices.
- **User-Friendly UI**: Built using Streamlit for an intuitive user experience.

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python (Scikit-learn, TensorFlow, Pandas, Matplotlib, Seaborn)
- **Data Source**: Yahoo Finance API or CSV data

## Installation
### Prerequisites
Ensure you have Python installed (>=3.7). Install required libraries using:
```bash
pip install streamlit pandas numpy scikit-learn tensorflow matplotlib seaborn yfinance
```

## Usage
1. Clone the repository:
```bash
git clone https://github.com/your-repo/stock-price-prediction.git
cd stock-price-prediction
```
2. Run the Streamlit app:
```bash
streamlit run app.py
```
3. Enter the stock ticker symbol and choose a prediction model.
4. View historical stock prices and predictions.

## Project Structure
```
├── app.py  # Main Streamlit app
├── models.py  # Machine learning models
├── data_processing.py  # Data loading and preprocessing
├── requirements.txt  # Python dependencies
├── README.md  # Project documentation
```

## Future Enhancements
- Add more ML models like Random Forest, XGBoost
- Implement real-time stock price updates
- Improve UI/UX with better visualization tools

## Contributing
Feel free to fork this repository and create a pull request for improvements!

## License
This project is licensed under the MIT License.

---
Happy Coding! 🚀


