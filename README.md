# Linear Regression by Least Squares with Streamlit

This is a simple Streamlit application that performs linear regression using the least squares method. It allows you to input data for x and y values, calculates the best-fitting line, and visualizes the results through a table and a scatter plot with the regression line.

## Installation

To run the Linear Regression app, you need to have Python and the following libraries installed:

- Streamlit
- NumPy
- Pandas
- Matplotlib

You can install these dependencies using pip:

```
pip install streamlit numpy pandas matplotlib
```

## Usage

1. Clone the repository or download the `linear_regression_app.py` file.

2. Open a terminal and navigate to the folder containing the `linear_regression_app.py` file.

3. Run the Streamlit app with the following command:

```
streamlit run linear_regression_app.py
```

4. Once the app is running, a browser window will open with the Streamlit interface.

5. In the sidebar, enter values for the `x` and `y` variables separated by commas. Press `Enter` after inputting each value.

6. Make sure to input an equal number of `x` and `y` values; otherwise, a warning will be displayed, and the regression won't be performed.

## Function Explanation

The linear regression is performed using the `linear_regression(x, y)` function, which utilizes the NumPy library's `polyfit` method to find the slope and y-intercept of the best-fitting line.

## Results

The app will display the following results:

1. A table showing the input data for `x` and `y`, along with the corresponding values for the regression line.

2. A scatter plot representing the data points and the regression line fitted to the data.

## Example

Suppose you have the following data:

```
x = [2,5,7,8]
y = [3,8,4,9]
```

After inputting these values into the app, the table will show:

```
   x  |  y  | Regression Line
---------------------------
0| 2| 3| 3.6667
1| 5| 8| 5.6667
2| 7| 4| 7
3| 8| 9| 7.6667
```

And the scatter plot will show the data points along with the fitted regression line.

## Requirements

- Python 3.x
- Streamlit
- NumPy
- Pandas
- Matplotlib

## Known Issues/Limitations

- The app currently supports only simple linear regression (one independent variable). It may not work as expected for more complex regression problems.

## License

This project is licensed under the [MIT License](LICENSE).

---
For updates and more projects, follow me on Twitter: [@ebukagaus](https://twitter.com/ebukagaus)
