# Readdressing the contribution of photonuclear reactions to the muon Content of extensive air showers: a heuristic approach

**Nickolay S. Martynenko**<sup>1, 2, *</sup>

<sup>1</sup> Lomonosov Moscow State University, 1–2 Leninskie Gory, Moscow 119991, Russia  
<sup>2</sup> Institute for Nuclear Research of the Russian Academy of Sciences, 60th October Anniversary Prospect 7a, Moscow 117312, Russia  
<sup>*</sup> Corresponding author: [martynenko@inr.ac.ru](mailto:martynenko@inr.ac.ru?subject=arXiv:2412.08349)

## About This Repository

This repository provides datasets corresponding to the findings presented in the paper: [**arXiv:2512.12481**](https://arxiv.org/abs/2512.12481) (submitted to Phys. Rev. D).

## Dataset Structure

The repository contains the following main components:

### 1. `Monte-Carlo/` — Monte Carlo (MC) Datasets

These datasets were produced by the author using **[CONEX v7.80](https://gitlab.iap.kit.edu/AirShowerPhysics/cxroot)** for extensive air shower (EAS) simulations.

- **`HadCascade.parquet`**  
  Dataset for the hadronic cascade development.  
  *See Subsection IIIA of the original manuscript for details.*

- **`ElmCascade.parquet`**  
  Dataset for the electromagnetic cascade development.  
  *See Subsection IIIB of the original manuscript for details.*

- **`MixCascade.parquet`**  
  Dataset used for model validation.  
  *See Subsection IIIC of the original manuscript for details.*

### 2. `utils/demo.py` — Python Demo Script

A demonstration script for reading and working with the MC datasets.

## Requirements

To work with the datasets, you will need **[Python&nbsp;3](https://www.python.org/downloads/)** the **[Awkward&nbsp;Array](https://awkward-array.org/doc/main/)** Python library.
The datasets were created using Python&nbsp;3.12.7 and the Awkward&nbsp;Array&nbsp;2.8.4, and it is therefore recommended that these versions be used for reproducibility.

## How to Get Started

0. Install Python&nbsp;3.12.7 if you haven't installed it yet. Consider installing via [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) to easily manage software dependencies

1. Clone the repository:
   ```bash
   git clone https://github.com/Nickolay-Martynenko/Photonuclear-Interactions-in-EAS.git
   ```
2. Install the required dependency:
   ```bash
   pip install awkward==2.8.4
   ```
3. Run the demo script to ensure everything is working correctly:
   ```bash
   cd Photonuclear-Interactions-in-EAS
   python3 utils/demo.py
   ```  



