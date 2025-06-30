# src/features.py

import mne
import numpy as np
from sklearn.decomposition import PCA

def extract_state_space(raw, window_size=2.0, step_size=0.5, n_components=2):
    """
    Convert EEG data into a low-dimensional state space using PCA.

    Parameters:
        raw (mne.io.Raw): Preprocessed EEG object
        window_size (float): Size of each sliding window in seconds
        step_size (float): Overlap step between windows
        n_components (int): Number of PCA dimensions to retain

    Returns:
        state_coords (ndarray): [n_epochs x n_components] PCA-transformed state vectors
    """
    # Create overlapping epochs
    epochs = mne.make_fixed_length_epochs(raw, duration=window_size, overlap=(window_size - step_size), preload=True)
    
    # Shape: (n_epochs, n_channels, n_times)
    data = epochs.get_data()
    
    # Flatten each window to a single feature vector
    flattened = data.reshape(len(data), -1)

    # Run PCA
    pca = PCA(n_components=n_components)
    state_coords = pca.fit_transform(flattened)

    return state_coords
