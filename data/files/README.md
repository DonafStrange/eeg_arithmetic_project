Sure! Here's a clean, well-formatted version of the dataset description suitable for your GitHub `README.md` or a dataset overview file like `DATASET.md`.

You can copy and paste it directly into Markdown files used by GitHub:

---

# 🧠 EEG During Mental Arithmetic Task – Dataset Overview

**Citation**
Zyma I, Tukaev S, Seleznov I, Kiyono K, Popov A, Chernykh M, Shpenkov O.
*Electroencephalograms during Mental Arithmetic Task Performance*. Data. 2019; 4(1):14.
👉 [DOI: 10.3390/data4010014](https://doi.org/10.3390/data4010014)
🔗 [PhysioNet Dataset Link](https://physionet.org/content/eegmat/1.0.0/)

---

## 📌 Introduction

This open-access dataset contains EEG recordings from healthy individuals taken **before** and **during** a mental arithmetic task. It is ideal for studying:

* Brain responses to cognitive load
* Task-induced EEG dynamics
* Nonlinear EEG features
* Group differences based on arithmetic performance

---

## 🧪 Study Methodology

* **Device**: 23-channel Neurocom EEG system (Ukraine, XAI-MEDICA)

* **Electrodes**: Silver/silver chloride (Ag/AgCl)

* **Placement**: International 10–20 system

* **Reference**: Linked earlobe electrodes

* **Filters**:

  * High-pass: 30 Hz
  * Notch: 50 Hz (to remove power line noise)

* **Artifact removal**: ICA used to remove eye, muscle, and cardiac artifacts

* **Task**: Serial subtraction (e.g., 3141 − 42, then subtract 42 repeatedly)

* **Recording duration**: 60 seconds per condition (artifact-free)

---

## 👨‍👩‍👧 Participants

* Healthy volunteers (no neurological, psychiatric, or cognitive impairments)
* Eligibility: Normal or corrected vision, no medications, no substance use
* Subject info (age, gender, date, count quality) provided in `subject-info.csv`

---

## 📂 Data Structure

Each subject has **two EEG recordings** in `.edf` format:

| File Suffix | Description                       |
| ----------- | --------------------------------- |
| `_1.edf`    | EEG before task (resting state)   |
| `_2.edf`    | EEG during mental arithmetic task |

Example:

```
sub-001_1.edf    # Rest EEG
sub-001_2.edf    # Task EEG
```

---

## 🧮 Performance-Based Grouping

Subjects were divided into two groups based on their performance:

| Group | Description                      | Subjects | Mean Operations (4 mins) |
| ----- | -------------------------------- | -------- | ------------------------ |
| `G`   | Good counters (high performance) | 24       | 21 ± 7.4                 |
| `B`   | Bad counters (low performance)   | 12       | 7 ± 3.6                  |

Label is provided in `subject-info.csv` → `"Count quality"` column:

* `0` = Group B (Bad)
* `1` = Group G (Good)

---

## 📚 File Format & Tools

* Format: **EDF / EDF+** (European Data Format)
* Compatible with:

  * [MNE-Python](https://mne.tools/)
  * [PyEDFlib](https://github.com/holgern/pyedflib)
  * [EDFbrowser](https://www.teuniz.net/edfbrowser/)
  * [PhysioBank ATM](https://physionet.org/physiobank/atm/)
  * [WFDB tools](https://physionet.org/about/software/wfdb/)

---

## 🧑‍🔬 Contributors

* **Igor Zyma**, **Sergii Tukaev**, **Ivan Seleznov**
  National Technical University of Ukraine, Igor Sikorsky Kyiv Polytechnic Institute
  Department of Electronic Engineering
  📧 Contact: [ivan.seleznov1@gmail.com](mailto:ivan.seleznov1@gmail.com)

---

> 📝 **License**: This dataset is made available under open data principles. Please cite the above paper when using the data.

---


