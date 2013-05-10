class Wave(object):
    """A single wave that makes up part of the solution to a Riemann problem"""

    subwaves = [] # If the wave is compound it may be made of waves
    
    def __init__(self, model, start, end, left, right, xi = [], data = []):
        """Define by the start and end of the wave in characteristic 
        coordinates, the states to the left and right of the wave,
        and the model"""

        self.model = model
        
        self.start = start
        self.end = end

        self.left = left
        self.right = right

        self.xi = xi
        self.data = data

    def plot_wave(self, xi_range):
        """Use matplotlib to plot the wave over a range"""

        import matplotlib
        import matplotlib.pyplot as plot
        import numpy as np

        xi = []
        data = []
        xi.append(xi_range[0])
        data.append(self.left)
        xi.append(self.start)
        data.append(self.left)
        xi.extend(list(self.xi))
        data.extend(list(self.data))
        xi.append(self.end)
        data.append(self.right)
        xi.append(xi_range[1])
        data.append(self.right)

        q_max = max(data)
        q_min = min(data)
        dq = q_max - q_min

        plot.plot(xi, data)
        plot.axis([xi_range[0], xi_range[1], q_min - 0.1*dq, q_max + 0.1*dq])
        plot.show()

