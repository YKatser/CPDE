import numpy as np
from numpy.lib.stride_tricks import as_strided
from numpy.linalg import lstsq
from numpy.linalg import inv
from numpy.linalg import slogdet #normal
from scipy.spatial.distance import pdist, squareform #rbf

from ruptures.base import BaseCost
from ruptures.costs import NotEnoughPoints


class CostNew(BaseCost):

    r"""
    Least absolute deviation.
    """

    model = "new"

    def __init__(self, order=1, metric=None):
        self.signal = None
        self.covar = None
        self.min_size = max(5, order + 1)
        self.order = order
        self.metric = metric
        self.gram = None
        self.gram_rbf = None

    def fit(self, signal):
        """Set parameters of the instance.

        Args:
            signal (array): signal. Shape (n_samples,) or (n_samples, n_features)
            metric (ndarray, optional): PSD matrix that defines a Mahalanobis-type pseudo distance. If None, defaults to the Mahalanobis matrix. Shape (n_features, n_features).


        Returns:
            self
        """
        if signal.ndim == 1:
            self.signal = signal.reshape(-1, 1)
            K = pdist(signal.reshape(-1, 1), metric="sqeuclidean")
        else:
            self.signal = signal
            K = pdist(signal, metric="sqeuclidean")
        #RBF
        K /= np.median(K)
        np.clip(K, 1e-2, 1e2, K)
        self.gram_rbf = np.exp(squareform(-K))

        # lagged covariates
        n_samples, _ = self.signal.shape
        strides = (self.signal.itemsize, self.signal.itemsize)
        shape = (n_samples - self.order, self.order)
        lagged = as_strided(self.signal, shape=shape, strides=strides)
        # pad the first columns
        lagged_after_padding = np.pad(lagged,
                                      ((self.order, 0), (0, 0)),
                                      mode="edge")
        # add intercept
        self.covar = np.c_[lagged_after_padding, np.ones(n_samples)]
        # pad signal on the edges
        self.signal[:self.order] = self.signal[self.order]
        
        
        s_ = signal.reshape(-1, 1) if signal.ndim == 1 else signal
        # Mahalanobis metric if self.metric is None
        if self.metric is None:
            covar = np.cov(s_.T)
            self.metric = inv(
                covar.reshape(1, 1) if covar.size == 1 else covar)
        self.gram = s_.dot(self.metric).dot(s_.T)
        
        return self

    def error(self, start, end):
        """Return the approximation cost on the segment [start:end].

        Args:
            start (int): start of the segment
            end (int): end of the segment

        Returns:
            float: segment cost

        Raises:
            NotEnoughPoints: when the segment is too short (less than ``'min_size'`` samples).
        """
        if end - start < self.min_size:
            raise NotEnoughPoints
        
        y, X = self.signal[start:end], self.covar[start:end]
        _, residual, _, _ = lstsq(X, y)
        
        sub = self.signal[start:end]
        med = np.median(sub, axis=0)
        
        sub_gram = self.gram[start:end, start:end]
        val = np.diagonal(sub_gram).sum()
        val -= sub_gram.sum() / (end - start)
        
        #normal
#         if self.signal.shape[1] > 1:
#             cov_normal = np.cov(sub.T)
#         else:
#             cov_normal = np.array([[sub.var()]])
#         _, val_normal = slogdet(cov_normal)
        
        #RBF
        sub_gram_rbf = self.gram_rbf[start:end, start:end]
        val_rbf = np.diagonal(sub_gram_rbf).sum()
        val_rbf -= sub_gram_rbf.sum() / (end - start)

        return [abs(sub - med).sum(),
                self.signal[start:end].var(axis=0).sum() * (end - start),
                residual.sum(),
                val,
#                 val_normal * (end - start),#normal
                val_rbf#RBF
               ]

