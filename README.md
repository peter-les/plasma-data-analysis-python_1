# Attachment Movement Analysis

Python reimplementation of a MATLAB project developed during PhD research in plasma physics.

## Purpose

The software analyses high-speed videos of arc attachment motion on an anode surface.

The original implementation was written in MATLAB.

This project reproduces the same workflow in Python.

## Input

Photron FASTCAM video:

- 300000 fps
- 256 x 80 px
- monochrome
- 30001 frames

## Dataset

This repository contains a **trimmed version** of the original recording (first ~30 seconds only) to reduce file size.

The full dataset used in the original MATLAB analysis is not included due to size constraints.


## Outputs

- attachment position
- attachment velocity
- restrike period
- restrike length
- uncertainty estimation

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Author

MATLAB version:
PhD plasma physics research

Python version:
MATLAB-to-Python migration project
for software development portfolio.
