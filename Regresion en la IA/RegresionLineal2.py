# Import libraries
from sklearn.datasets import fetch_california_housing
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

# Load California housing data
housing = fetch_california_housing()
X = housing.data
Y = housing.target

# Feature columns (check housing.feature_names)
# ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
rm = X[:, 3]  # 'AveRooms' (column 3)

# 1. Plot RM vs MEDV and calculate correlation
def relation_rm_medv(rm, means):
    plt.scatter(rm, means, alpha=0.25)
    plt.title("Average Rooms vs. Median Home Price (California)")
    plt.xlabel("Avg. Rooms per Household")
    plt.ylabel("Price ($100,000s)")
    plt.show()
    return np.corrcoef(rm, means)[0, 1]

# 2. Calculate mean price for homes with 5-6 rooms
def price_mean(rm, means):
    filtered_means = means[np.logical_and(rm > 5, rm < 6)]
    return np.mean(filtered_means) * 100_000  # Convert to dollars

# 3. Plot MEDV histogram
def medv_hist(medv):
    plt.hist(medv, bins=50)
    plt.title("Distribution of Home Prices")
    plt.xlabel("Price ($100,000s)")
    plt.ylabel("Frequency")
    plt.show()

# 4. Linear regression (manual implementation)
def lineal_regression(x, means):
    w = np.linalg.inv(x.T @ x) @ x.T @ means
    plt.scatter(rm, means, alpha=0.25)
    plt.plot(rm, x @ w, color="red")
    plt.title("Linear Regression Fit")
    plt.xlabel("Avg. Rooms per Household")
    plt.ylabel("Price ($100,000s)")
    plt.show()
    return w, x @ w

# 5. Prediction functions
def predict_from_room_number(room_number, w):
    return (w[0] + w[1] * room_number) * 100_000  # Convert to dollars

def predict_from_price(price, w):
    return (price / 100_000 - w[0]) / w[1]  # Convert from dollars

def get_mse(yp, y):
    return np.mean(np.square(np.subtract(yp, y)))

# 6. Scikit-learn comparison
def use_sklearn():
    model = linear_model.LinearRegression().fit(rm.reshape(-1, 1), Y)
    yp = model.predict(rm.reshape(-1, 1))
    
    plt.scatter(rm, Y, alpha=0.25)
    plt.plot(rm, yp, color="green")
    plt.title("Scikit-learn Linear Regression")
    plt.xlabel("Avg. Rooms per Household")
    plt.ylabel("Price ($100,000s)")
    plt.show()
    
    print("Scikit-learn Model:")
    print(f"Slope (w1): {model.coef_[0]:.2f}")
    print(f"Intercept (w0): {model.intercept_:.2f}")
    print(f"MSE: {mean_squared_error(Y, yp):.2f}")

# --- Execute all functions ---
print(f"Correlation between rooms and price: {relation_rm_medv(rm, Y):.2f}")
print(f"Mean price for 5-6 room homes: ${price_mean(rm, Y):,.2f}")
medv_hist(Y)

# Manual regression
w, yp = lineal_regression(np.c_[np.ones(rm.shape[0]), rm], Y)
print(f"\nManual Regression Weights: w0 = {w[0]:.2f}, w1 = {w[1]:.2f}")
print(f"Predicted price for 9-room home: ${predict_from_room_number(9, w):,.2f}")
print(f"Predicted rooms for $45k home: {predict_from_price(45000, w):.1f} rooms")
print(f"Manual Regression MSE: {get_mse(yp, Y):.2f}")

# Scikit-learn regression
use_sklearn()