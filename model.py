class Model(object):
    """The description of the conservation law to be solved"""

    convex = True

    def __init__(self, n, flux, d_flux, dd_flux):
        """Define the model via the flux and its derivatives,
           and the size of the system n"""

        self.flux = flux
        self.d_flux = d_flux
        self.dd_flux = dd_flux

        assert (n >= 1)
        self.n = n
