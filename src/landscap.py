# src/landscap.py

import numpy as np
from scipy.stats import entropy
from scipy.stats import gaussian_kde
from scipy.ndimage import minimum_filter, label

def compute_energy_landscape(states, grid_size=100):
    """
    Compute the energy landscape from 2D state coordinates.

    Parameters:
        states (ndarray): (N, 2) PCA-projected EEG state vectors
        grid_size (int): resolution of the grid

    Returns:
        X, Y, energy (2D arrays): grid and energy surface
    """
    x, y = states[:, 0], states[:, 1]
    kde = gaussian_kde([x, y])

    # Define grid
    x_grid = np.linspace(x.min(), x.max(), grid_size)
    y_grid = np.linspace(y.min(), y.max(), grid_size)
    X, Y = np.meshgrid(x_grid, y_grid)

    # Compute density
    Z = kde(np.vstack([X.ravel(), Y.ravel()]))
    P = Z.reshape(X.shape)

    # Convert to energy
    energy = -np.log(P + 1e-6)

    return X, Y, energy


def count_energy_wells(energy, size=3):
    """
    Count local minima (wells) in the energy landscape.

    Parameters:
        energy (2D array): energy values over the grid
        size (int): neighborhood size for local minimum detection

    Returns:
        n_wells (int): number of local minima
        wells_mask (2D binary array): where minima are
    """
    # Find local minima
    local_min = (energy == minimum_filter(energy, size=size))
    
    # Remove edges (optional cleanup)
    border = 2
    local_min[:border, :] = 0
    local_min[-border:, :] = 0
    local_min[:, :border] = 0
    local_min[:, -border:] = 0

    # Label and count
    labeled, n_wells = label(local_min)
    return n_wells, local_min



def energy_entropy(energy):
    flat = energy.ravel()
    prob = np.exp(-flat)  # Convert back to probability
    prob /= np.sum(prob)
    return entropy(prob)