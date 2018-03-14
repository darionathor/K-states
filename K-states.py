
from kmodes.util.dissim import matching_dissim, ng_dissim

class KStates():

    def __init__(self, n_clusters=8, max_iter=100, cat_dissim=matching_dissim,
                 init='Huang', n_init=1, verbose=0):

        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.cat_dissim = cat_dissim
        self.init = init
        self.n_init = n_init
        self.verbose = verbose
        if ((isinstance(self.init, str) and self.init == 'Cao') or
                hasattr(self.init, '__array__')) and self.n_init > 1:
            if self.verbose:
                print("Initialization method and algorithm are deterministic. "
                      "Setting n_init to 1.")
            self.n_init = 1

    def fit(self, X, y=None, **kwargs):
        return self

    def fit_predict(self, X, y=None, **kwargs):
        return self.fit(X, **kwargs).predict(X, **kwargs)

    def predict(self, X, **kwargs):
        return X
