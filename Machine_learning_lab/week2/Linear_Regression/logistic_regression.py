# logistic regression

# Import standard data sets
from sklearn import datasets

# Import the Logistic regression model
from sklearn.linear_model import LogisticRegression

# Split data set into a train and test set
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

import matplotlib.pylab as plt

wine_dataset = datasets.load_wine()  # loading a data set from scikitlearn
x = wine_dataset["data"]  # defining variables
y = wine_dataset["target"]  # defining target variable values

# Splitting data set into a train and test set with 70% and 30%
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

log_reg = LogisticRegression()  # calling logistic regression model
log_reg.fit(x_train, y_train)  # fitting the model to train set

# predicting y values of test set
predictions = log_reg.predict(x_test)

print(accuracy_score(y_test, predictions))

# Todo 02

# Load the ‘digits’ data set from the scikit-learn standard data sets
digita = datasets.load_digits()
x = digita["data"]
y = digita["target"]
print(digita.keys())

# Split 80% of the data set to train and rest for the test set
x_train, x_test, y_train, y_test = train_test_split(x,y , test_size=0.2, random_state=10)

#print(y_train)
#print(y_test)

# Train a Logistic regression model and predict values for the test set.
log_reg = LogisticRegression()
log_reg.fit(x_train, y_train)  # fitting the model to train set

# predicting y values of test set
predictions_test = log_reg.predict(x_test)
predictions_training = log_reg.predict(x_train)

print(accuracy_score(y_test, predictions_test))

# Visualize the residual errors for both train and test sets in one graph. (x axis- predicted value,
# y-axis- actual value)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.set_title('Actual vs predicted')
ax1.set(ylabel='Actual', xlabel='predicted')
ax2.set(xlabel='Actual', ylabel='Residual error')
ax2.set_title('Residual error')

ax1.plot(predictions_training, y_train , color="r", marker="*", label = 'traing')  # plotting the predicted line
ax2.plot(y_train, y_train-predictions_training , color="r", marker="*",label='traing')


#print(y, '\n', x)
ax1.scatter( predictions_test,y_test, color="b", marker=".", s=500 , label = 'testing' )  # plotting the predicted line
ax2.scatter(y_test, y_test- predictions_test, color="b", marker=".", s=60 , label = 'testing' )
# axs[1].title('Simple Linear Regression')  # adding a title to the graph
# axs[0].ylabel('actual value')  # adding axis labels
# axs[0].xlabel('predicted value')
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")
plt.show()  # displaying the plot
