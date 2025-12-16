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

These datasets were produced by the author using **[CONEX v7.80](https://gitlab.iap.kit.edu/AirShowerPhysics/cxroot)** for extensive air shower simulations.

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

A demonstration script for reading the MC datasets.

## Requirements

To work with the datasets, you will need **[Git&nbsp;Large&nbsp;File&nbsp;Storage](https://git-lfs.com)**, **[Python&nbsp;3](https://www.python.org/downloads/)**, and the **[Awkward&nbsp;Array](https://awkward-array.org/doc/main/)** Python library.
The datasets were created and tested using Python&nbsp;3.12.7 and the Awkward&nbsp;Array&nbsp;2.8.4. To ensure reproducibility, it is recommended to use exactly these versions. 

## How to Get Started

0. Install Git LFS and Python&nbsp;3.12.7 if you haven't installed them yet. 

   Consider installing Python via [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) to easily manage software dependencies

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
   git lfs pull
   python3 utils/demo.py
   ```
   Note that the total size of .parquet files is approximately 683 MB, so `git lfs pull` may take a while. The output should be:
   ```bash
   73728 * {Fragment: string, Shower_Id: uint32, Shower_Log10Energy: float32, Shower_NumLeadingInteractions: uint8, Shower_NumSecondaryParticles: uint16, LeadingInteractions: var * {ParticleId: uint16, Log10Energy: float32, SlantDepth: float32, NumSecondaryParticles: uint16}, SecondaryParticles: var * {LeadingInteractionId: uint8, ParticleId: uint16, Log10Energy: float32}}
   19456 * {Fragment: string, Shower_Id: uint32, Shower_Log10Energy: float32, PhotonuclearReaction_Log10Energy_BinEdges: 49 * float32, MuonSlantDepth: 201 * float32, MuonNumber: 48 * 201 * float32}
   239616 * {Shower_Id: uint32, Shower_Log10Energy: float32, Shower_PrimaryParticle: string, PNRXsection_AsymptRatioModified2EGS4: float32, PNRXsection_Log10EnergyTransitionEGS42Modified: float32, MuonSlantDepth: 201 * float32, MuonNumber: 201 * float32}
   ```



