import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def linear_regression(x, y):
    # linear regression function
    coeffs = np.polyfit(x, y, 1)
    m = coeffs[0]  # Slope
    b = coeffs[1]  # Y-intercept
    return m, b

def main():
    # Set up the layout of the app
    st.title("Linear Regression by Least Squares")
    st.sidebar.header("Data Input")
    st.sidebar.write("Enter values for x and y:")
    x = st.sidebar.text_input("x", value='', key='x_input')
    y = st.sidebar.text_input("y", value='', key='y_input')
    x = [float(val) for val in x.split(',') if val.strip()]
    y = [float(val) for val in y.split(',') if val.strip()]

    if len(x) != len(y):
        st.warning("The number of x and y values should be equal.")
        return

    # Perform linear regression using the function defined
    if len(x) > 0 and len(y) > 0:
        m, b = linear_regression(x, y)

        # Create DataFrame for table using pandas
        data = {'x': x, 'y': y}
        df = pd.DataFrame(data)
        df['Regression Line'] = m * df['x'] + b
        st.write(df)

        # Generate graph
        fig, ax = plt.subplots()
        ax.scatter(x, y, label='Data Points')
        ax.plot(x, m * np.array(x) + b, color='red', label='Regression Line')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend()
        st.pyplot(fig)

if __name__ == "__main__":
    main()
