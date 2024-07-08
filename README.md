# Real Estate Price Prediction Website

This project demonstrates the process of building a real estate price prediction website. We start by developing a machine learning model using sklearn and linear regression, leveraging the Bangalore home prices dataset from Kaggle.com. 

## Project Components

1. **Model Building with sklearn**
   - Utilize linear regression to predict home prices based on features like square footage, number of bedrooms, etc.
   - Cover data loading, cleaning, outlier detection, feature engineering, dimensionality reduction, and hyperparameter tuning using GridSearchCV.

2. **Python Flask Server**
   - Develop a Flask server to host the trained model.
   - Handle HTTP requests from the frontend to predict home prices.

3. **Website Development**
   - Create a frontend using HTML, CSS, and JavaScript.
   - Allow users to input home features and retrieve predicted prices from the Flask server.

## Technologies and Tools Used

- **Python**: Main programming language.
- **Numpy and Pandas**: Data cleaning and manipulation.
- **Matplotlib**: Data visualization.
- **Sklearn**: Machine learning model building.
- **Jupyter Notebook, Visual Studio Code, PyCharm**: IDEs used for development.
- **Flask**: Python micro web framework for HTTP server.
- **HTML/CSS/JavaScript**: Frontend development for user interface.

## Setup Instructions

1. **Clone the Repository**
``` 
git clone <repository_url>
cd real-estate-price-prediction 
```

2. **Install Dependencies**
`pip install -r requirements.txt`

3. **Run Flask Server**
`python app.py`

4. **Open the Website**
- Navigate to `http://localhost:5000` in your web browser.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Data source: [Bangalore home prices dataset on Kaggle](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)
- Inspiration and guidance from [codebasics.io](https://codebasics.io).

