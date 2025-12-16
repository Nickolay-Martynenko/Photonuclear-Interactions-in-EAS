# Readdressing the Contribution of Photonuclear Reactions to the Muon Content of Extensive Air Showers: A Heuristic Approach

**Nickolay S. Martynenko**<sup>1, 2, *</sup>

<sup>1</sup> Lomonosov Moscow State University, 1–2 Leninskie Gory, Moscow 119991, Russia  
<sup>2</sup> Institute for Nuclear Research of the Russian Academy of Sciences, 60th October Anniversary Prospect 7a, Moscow 117312, Russia  
<sup>*</sup> Corresponding author: [martynenko@inr.ac.ru](mailto:martynenko@inr.ac.ru?subject=arXiv:2412.08349)

## About This Repository

This repository provides datasets corresponding to the findings presented in the paper:  
[**arXiv:2512.12481**](https://arxiv.org/abs/2512.12481) (submitted to *Phys. Rev. D*).

## Dataset Structure

The repository contains the following main components:

### 1. `Monte-Carlo/` — Monte Carlo (MC) Datasets

These datasets were produced by the author using **[CONEX v7.80](https://gitlab.iap.kit.edu/AirShowerPhysics/cxroot/-/tree/2f795057e7d35ba2233dba77b791e51143bec3b4/)** for extensive air shower (EAS) simulations.

- **`README.md`**  
  Brief documentation for the datasets.

- **`HadCascade.parquet`**  
  Dataset for the high‑energy hadronic cascade development (proton‑induced EAS).

- **`ElmCascade.parquet`**  
  Dataset for the electromagnetic cascade development (photon‑induced EAS).

- **`MixCascade.parquet`**  
  Dataset used for model validation (photon‑ and nucleus‑induced EAS).

### 2. `utils/demo.py` — Python Demo Script


A demonstration script for reading the MC datasets and verifying their integrity.

## Requirements

To work with the datasets, you will need:

- **[Git LFS](https://git-lfs.com)** — for downloading large Parquet files.
- **[Python 3](https://www.python.org/downloads/)** (recommended: **3.12.7**) — for running the demo script.
- **[Awkward Array](https://awkward-array.org/doc/main/)** (recommended: **2.8.4**) — for handling the structured data.

> **Note:** The datasets were created and tested using **Python 3.12.7** and **Awkward Array 2.8.4**. Using these versions ensures reproducibility.

## How to Get Started

1. **Install prerequisites**  
   - Install **Git LFS** and **Python 3.12.7**
   - Consider using **[Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main)** to manage dependencies easily
   - Install **Awkward Array** (e.g. `pip install awkward==2.8.4`)

2. **Clone the repository**  
   ```bash
   git clone https://github.com/Nickolay-Martynenko/Photonuclear-Interactions-in-EAS.git
   ```

3. Navigate to the repository directory:
   ```bash
   cd Photonuclear-Interactions-in-EAS
   ```
   
4. Download the Parquet files:
   ```bash
   git lfs pull
   ```
   > Note: total size is approximately 0.68 GB. This may take some time depending on your internet speed

5. Run the demo script:
   ```bash
   python3 utils/demo.py
   ```
   Expected output (3 lines in terminal):
   ```
   73728 * {Fragment: string, Shower_Id: uint32, Shower_Log10Energy: float32,
   Shower_NumLeadingInteractions: uint8, Shower_NumSecondaryParticles: uint16,
   LeadingInteractions: var * {ParticleId: uint16, Log10Energy: float32, SlantDepth: float32,
   NumSecondaryParticles: uint16}, SecondaryParticles: var * {LeadingInteractionId: uint8,
   ParticleId: uint16, Log10Energy: float32}}

   19456 * {Fragment: string, Shower_Id: uint32, Shower_Log10Energy: float32,
   PNR_Log10Energy_BinEdges: 49 * float32, MuonSlantDepth: 201 * float32,
   MuonNumber: 48 * 201 * float32}

   239616 * {Shower_Id: uint32, Shower_Log10Energy: float32, Shower_ParticleId: uint16,
   PNR_XsMod2Std: float32, PNR_Log10Energy_Std2Mod: float32, MuonSlantDepth: 201 * float32,
   MuonNumber: 201 * float32}
   ```

## License

The code and datasets in this repository are released under the MIT License. See [**`LICENSE`**](LICENSE) for details.

## Citation

If you use this dataset or any other result of this study in your research, please cite the original paper:

    @article{Martynenko:2025zxj,
        author = "Martynenko, Nickolay S.",
        title = "{Readdressing the contribution of photonuclear reactions to the muon content of extensive air showers: a heuristic approach}",
        eprint = "2512.12481",
        archivePrefix = "arXiv",
        primaryClass = "astro-ph.HE",
        reportNumber = "INR-TH-2025-022",
        month = "12",
        year = "2025"
    }



