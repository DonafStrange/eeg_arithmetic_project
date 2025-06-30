# preprocessing.py

import mne

def load_and_preprocess_edf(filepath):
    raw = mne.io.read_raw_edf(filepath, preload=True)
    raw.filter(1., 40., fir_design='firwin')  # Bandpass filtering
    raw.set_eeg_reference('average', projection=True)
    return raw
