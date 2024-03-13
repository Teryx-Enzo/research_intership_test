# Datasets for the ICPE 2024 Data Challenge track

Information about the track:
[https://icpe2024.spec.org/tracks-and-submissions/data-challenge-track](https://icpe2024.spec.org/tracks-and-submissions/data-challenge-track/)

The dataset comprises 560 CSV files containing pre-processed execution traces.  These traces originate from two  open-source microservices systems: [Train-Ticket](https://github.com/FudanSELab/train-ticket) and [E-Shopper](https://github.com/SEALABQualityGroup/E-Shopper).


This notebook tries to re-implement the De-Lag framework.

## Usage example

To run the notebooks, ensure you have `pandas`, `scikit-learn`, `seaborn`, `bitstring` , and `notebook` installed. You can set up the environment and install these packages using the following commands:
```
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

---

The dataset was originally created for the paper:

L. Traini and V. Cortellessa, ***DeLag: Using Multi-Objective Optimization to Enhance the Detection of Latency Degradation Patterns in Service-Based Systems***, in IEEE Transactions on Software Engineering, vol. 49, no. 6, pp. 3554-3580, 1 June 2023, [DOI: 10.1109/TSE.2023.3266041](https://doi.org/10.1109/TSE.2023.3266041).


```
@ARTICLE{delag,
  author={Traini, Luca and Cortellessa, Vittorio},
  journal={IEEE Transactions on Software Engineering}, 
  title={DeLag: Using Multi-Objective Optimization to Enhance the Detection of Latency Degradation Patterns in Service-Based Systems}, 
  year={2023},
  volume={49},
  number={6},
  pages={3554-3580},
  doi={10.1109/TSE.2023.3266041}}
```
