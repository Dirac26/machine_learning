from matplotlib import pyplot as plt

class LinearModle:
    """
    class that generates linear models with one featur
    """
    def __init__(self):
        """
        init function
        """
        self.iter = 1001
        self.learning_rate = 0.01
        self.param = [0, 0]

    def fit(self, x, y):
        """
        fits the models paramters of the model based on featur x and output y
        """
        self.y_training = y
        self.x_training = x
        for i in range(self.iter):
            self.step_gradient(self.param, x, y)

    def get_param(self):
        """
        return the parameters of the model
        """
        return self.param

    def predict(self, x):
        """
        return the predected value for input list x
        """
        y_list = []
        for elm in x:
            y = self.param[1] * elm + self.param[0]
            y_list.append(y)
        return y_list

    def get_gradient_cont(self, x, y, param):
        """
        calculate gradiant value for the bias term
        """
        diff = 0
        for i in range(len(x)):
            diff += y[i] - ((param[1] * x[i]) + param[0])
        b_gradient = -(2/len(x)) * diff
        return b_gradient

    def get_gradient_param(self, x, y, param):
        """
        calculate gradiant value for the featur parameter
        """
        diff = 0
        for i in range(len(x)):
            diff += x[i] * (y[i] - ((param[1] * x[i]) + param[0]))
        m_gradient = -(2/len(x)) * diff
        return m_gradient

    def step_gradient(self, param, x, y):
        """
        update the new values for the model parameters
        """
        b = self.get_gradient_cont(x, y, param)
        m = self.get_gradient_param(x, y, param)
        param[0] = param[0] - (self.learning_rate * b)
        param[1] = param[1] - (self.learning_rate * m)

    def ploter(self):
        """
        plot predected data with training set
        """
        y_predict = self.predict(self.x_training)
        plt.plot(self.x_training, self.y_training, 'o')
        plt.plot(self.x_training, y_predict)
        plt.show()


# sample code to test the model

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
cost = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]
model = LinearModle()
model.fit(months, cost)
y = model.predict(months)
model.ploter()