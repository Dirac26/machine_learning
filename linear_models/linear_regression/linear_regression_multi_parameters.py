from matplotlib import pyplot as plt

class LinearModleMulti:
    """
    class that generates linear models with multi featur
    """
    def __init__(self):
        """
        init function
        """
        self.iter = 1001
        self.learning_rate = 0.01
        self.param = []

    def fit(self, x, y):
        """
        fits the models paramters of the model based on featurs x and output y
        """
        self.y_training = y
        self.x_training = x
        self.dim = len(self.x_training) + 1
        self.x0 = []
        for i in range(len(self.x_training[0])):
            self.x0.append(1)
        self.x_training.insert(0, self.x0)
        for i in range(self.dim):
            self.param.append(0)
        for i in range(self.iter):
            self.step_gradient(self.param, x, y)

    def get_param(self):
        """
        return the parameters of the model
        """
        return self.param

    def predict(self, x):
        """
        return the predected value for input list of points x
        """
        x.insert(0, self.x0)
        y_list = []
        for point, _ in enumerate(x[0]):
            y = 0
            for i, featur in enumerate(x):
                y +=  featur[point] * self.param[i]
            y_list.append(y)
        return y_list

    def get_gradient_param(self, x, y, param_ind):
        """
        calculate gradiant value for the featur parameter
        """
        diff = 0
        for point, _ in enumerate(x[0]):
            xtheta = 0
            for i, featur in enumerate(x):
                xtheta += featur[point] * self.param[i]
            diff += x[param_ind][point] * (y[point] - xtheta)
        param_gradient = -(2/len(x[0])) * diff
        return param_gradient

    def step_gradient(self, param, x, y):
        """
        update the new values for the model parameters
        """
        new_param = param[:]
        grad_params = param[:]
        for par_ind, par in enumerate(param):
            grad_params[par_ind] = self.get_gradient_param(x, y, par_ind)
            new_param[par_ind] = par - (self.learning_rate * grad_params[par_ind])
        self.param = new_param[:]
    def ploter(self):
        """
        plot predected data with training set, only works if modeling one featrue
        """
        x_training = self.x_training[1:]
        y_predict = self.predict(x_training)
        plt.plot(self.x_training[1], self.y_training, 'o')
        plt.plot(self.x_training[1], y_predict)
        plt.show()


# sample code to test the model

months = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
cost = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]
model = LinearModleMulti()
model.fit(months, cost)
model.ploter()