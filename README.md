# EEG Mental Arithmetic Task Analysis

This project analyzes EEG recordings from the PhysioNet dataset: "Electroencephalograms during Mental Arithmetic Task Performance".

## 📊 Description
We explore EEG dynamics across:
- Resting vs. mental arithmetic task states
- Group G (good counters) vs. Group B (bad counters)
- Feature extraction using MNE-Python
- Nonlinear metrics such as DFA and entropy

## 📁 Data
Raw EEG files in `.edf` format should be placed in the `data/` directory (not tracked by Git).

## 📂 Structure
- `data/`: raw EEG files
- `notebooks/`: Jupyter notebooks for exploratory analysis
- `src/`: scripts for preprocessing and feature extraction
- `results/`: figures, output data

## 🚀 Getting Started
1. Create a virtual environment
2. Install dependencies:
```bash
pip install -r requirements.txt

