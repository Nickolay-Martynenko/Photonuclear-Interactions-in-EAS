# Dataset Documentation

This directory contains Parquet files with simulated data of extensive air showers (EAS). Below is a detailed description of each file structure and its fields.
<br>

## File Overview

The dataset comprises three main Parquet files, each focusing on different types of air shower events:
- `HadCascade.parquet` — proton‑induced (hadronic) EAS
- `ElmCascade.parquet` — photon‑induced (electromagnetic) EAS
- `MixCascade.parquet` — mixed EAS events (various primary particles
<br>

## Units
- Energy units: electronvolts (eV); values are stored as Baes-10 logarithms for numerical stability
- Slant depth: grams per square centimeter (g/cm²)
- Particle IDs: consistent with the particle identification scheme used in **[CORSIKA](https://www.iap.kit.edu/corsika/downloads/CORSIKA_GUIDE7.8010.pdf)**
<br>

## Parquet Files
### `HadCascade.parquet` (High-energy hadronic cascade development)

Contains data on proton‑induced EAS, particularily the Leading interactions tree content. See Section III A of the original manuscript for details

#### Top‑Level Fields

| Field | Data Type | Description |
|-------|---------|-------------|
| `Fragment` | `string` | <sub><sup>Dataset split indicator (`"train"`/`"test"`)</sup></sub> |
| `Shower_Id` | `uint32` | <sub><sup>Unique identifier for the proton‑induced EAS event</sup></sub> |
| `Shower_Log10Energy` | `float32` | <sub><sup>Base‑10 logarithm of primary proton energy</sup></sub> |
| `Shower_NumLeadingInteractions` | `uint8` | <sub><sup>Total count of leading interactions recorded in the event</sup></sub> |
| `Shower_NumSecondaryParticles` | `uint16` | <sub><sup>Total count of secondary particles recorded in the event</sup></sub> |


#### Nested Structures (Awkward Arrays)

##### `LeadingInteractions`
Array of leading interaction records (variable length per event).

| Field | Data Type | Description |
|-------|---------|-------------|
| &nbsp;&#8627;`ParticleId` | `uint16` | <sub><sup>ID of the parent particle</sup></sub> |
| &nbsp;&#8627;`Log10Energy` | `float32` | <sub><sup>Base‑10 logarithm of parent particle energy</sup></sub> |
| &nbsp;&#8627;`NumSecondaryParticles` | `uint16` | <sub><sup>Number of secondary particles produced in this interaction</sup></sub> |

##### `SecondaryParticles`
Array of secondary particle records (variable length per event).

| Field | Data Type | Description |
|-------|---------|-------------|
| &nbsp;&#8627;`LeadingInteractionId` | `float32` | <sub><sup>ID of the leading interaction that produced this secondary particle</sup></sub> |
| &nbsp;&#8627;`ParticleId` | `uint16` | <sub><sup>ID of the secondary particle</sup></sub> |
| &nbsp;&#8627;`Log10Energy` | `float32` | <sub><sup>Base‑10 logarithm of secondary particle energy</sup></sub> |

<br><br><br>

### `ElmCascade.parquet` (Electromagnetic cascade development)

Contains data on photon‑induced EAS, focusing on photonuclear reactions and muon production. See Section III B of the original manuscript for details

#### Fields

| Field | Data Type | Description |
|-------|---------|-------------|
| `Fragment` | `string` | <sub><sup>Dataset split indicator (`"train"`/`"test"`)</sup></sub> |
| `Shower_Id` | `uint32` | <sub><sup>Unique identifier for the photon‑induced EAS event</sup></sub> |
| `Shower_Log10Energy` | `float32` | <sub><sup>Base‑10 logarithm of primary photon energy</sup></sub> |
| `PNR_Log10Energy_BinEdges` | `49×float32` | <sub><sup>Bin edges for photonuclear reaction energy (Base‑10 log). Defines 3 extra + 45 main bins</sup></sub> |
| `MuonSlantDepth` | `201×float32` |<sub><sup> Array of slant depth values. 201 points</sup></sub> |
| `MuonNumber` | `48×201×float32` | <sub><sup>Number of muons per photonuclear energy bin at each slant depth point</sup></sub> |

<br><br><br>

### `MixCascade.parquet` (EAS with modified photonuclear cross section)

Contains EAS events with various primary particle types and with focus on the muon production assuming different photonuclear cross sections.  See Section III C of the original manuscript for details

#### Fields

| Field | Data Type | Description |
|-------|---------|-------------|
| `Shower_Id` | `uint32` | <sub><sup>Unique identifier for the EAS event</sup></sub> |
| `Shower_Log10Energy` | `float32` | <sub><sup>Base‑10 logarithm of primary particle energy</sup></sub> |
| `Shower_ParticleId` | `uint16` | <sub><sup>ID of the primary particle</sup></sub> |
| `PNR_XsMod2Std` | `float32` | <sub><sup>Asymptotic ratio of modified photonuclear cross section to EGS4 cross section</sup></sub> |
| `PNR_Log10Energy_Std2Mod` | `float32` | <sub><sup>Base‑10 logarithm of energy  above which modified cross section is used instead of EGS4</sup></sub> |
| `MuonSlantDepth` | `201×float32` | <sub><sup>Array of slant depth values. 201 points</sup></sub> |
| `MuonNumber` | `201×float32` | <sub><sup>Number of muons at each slant depth point</sup></sub> |
