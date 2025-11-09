# DeepMyco: Large Language Models for Scaling Mycoremediation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Documentation Status](https://readthedocs.org/projects/deepmyco/badge/?version=latest)](https://deepmyco.readthedocs.io/en/latest/?badge=latest)

## Overview

DeepMyco is a groundbreaking research project that leverages Large Language Models (LLMs) to extract, analyze, and scale mycoremediation knowledge from scientific literature. By systematically processing research papers, we've created the first comprehensive dataset of mycoremediation experiments and developed machine learning models to predict optimal fungal-pollutant combinations for environmental cleanup applications.

### Key Features

- **LLM-Powered Data Extraction**: Automated extraction of experimental data from mycoremediation research papers
- **Comprehensive Dataset**: 812 mycoremediation experiments with detailed metadata on fungi, pollutants, and conditions  
- **Predictive Models**: Machine learning models for forecasting degradation efficiency and recommending optimal fungal strains
- **Experimental Validation**: Laboratory validation of model predictions with spectroscopy and growth studies
- **Open Science**: Fully reproducible research with open datasets and code

### Research Impact

This project addresses the critical challenge of scaling mycoremediation—the use of fungi to clean up environmental pollutants. Traditional approaches rely on scattered literature and limited experimental data. DeepMyco systematically consolidates this knowledge and makes it accessible through predictive models, accelerating the development of effective bioremediation strategies.

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/deepmyco.git
cd deepmyco

# Create conda environment
conda env create -f environment.yml
conda activate deepmyco

# Install package in development mode
pip install -e .
```

### Basic Usage

```python
import deepmyco

# Load the mycoremediation dataset
data = deepmyco.data.load_dataset()

# Train a forecasting model
model = deepmyco.models.DecolorationForecaster()
model.fit(data)

# Get fungal recommendations for a specific dye
recommendations = deepmyco.models.recommend_fungi(
    pollutant="Methylene Blue",
    concentration=50,  # mg/L
    ph=7.0
)

print(f"Top recommended fungi: {recommendations}")
```

### Example Analysis

```python
# Analyze fungal robustness across different conditions
analysis = deepmyco.analysis.FungalRobustnessAnalysis()
robustness_scores = analysis.calculate_robustness(data)

# Create radar charts for top performers
deepmyco.analysis.create_robustness_radar(
    robustness_scores.head(5),
    save_path="fungi_robustness.png"
)
```

## Dataset

The DeepMyco dataset contains:

- **812 mycoremediation experiments** extracted from peer-reviewed literature
- **168 time-series samples** tracking degradation over time  
- **45+ fungal species** with taxonomic and enzymatic information
- **25+ pollutant types** including synthetic dyes, heavy metals, and organic compounds
- **Experimental conditions** including pH, temperature, concentration, and duration

### Data Structure

```
data/
├── processed/
│   ├── mycoremediation_dataset.csv    # Main experimental dataset
│   ├── timeseries_dataset.csv         # Time-series degradation data
│   ├── fungi_metadata.csv             # Fungal strain information  
│   └── dye_metadata.csv               # Pollutant chemical properties
└── external/
    ├── mycobank_ids.csv               # Taxonomic identifiers
    └── enzyme_commission.csv          # Enzyme classification
```

## Models

### Decoloration Forecasting

Predict pollutant removal efficiency based on:
- Fungal species and strain characteristics
- Pollutant type and concentration  
- Environmental conditions (pH, temperature)
- Experimental duration

**Available Models:**
- Random Forest Regressor (primary)
- K-Nearest Neighbors
- Linear Regression (baseline)

### Fungal Recommendation System

Recommend optimal fungal strains for specific pollutants and conditions using collaborative filtering and content-based approaches.

## Experimental Validation

Laboratory validation includes:
- **Spectroscopy measurements** for degradation confirmation
- **Plant growth studies** using treated water  
- **Chemical analysis** of pH, conductivity, and byproducts

Validation protocols are documented in `experiments/lab_protocols/`.

## Documentation

Comprehensive documentation will be available shortly!:

ractive analysis examples

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on:

- Setting up the development environment
- Code style and testing requirements  
- Submitting pull requests
- Reporting issues

### Development Setup

```bash
# Install development dependencies
pip install -e ".[dev]"

```

## Project Structure

```
DeepMyco/
├── src/ 	            # Main package source code
├── data/                   # Datasets and processing
├── experiments/            # Notebooks and results
├── models/                 # Trained model artifacts
├── docs/                   # Documentation
└──
```

## Citation

If you use DeepMyco in your research, please cite our paper:

```bibtex
@inproceedings{gupta2025deepmyco,
  title={DeepMyco: Large Language Models for Scaling Mycoremediation},
  author={Gupta, Danika},
  booktitle={2025 IEEE Conference on AI for Sustainable Innovation (IEEE AI-SI)},
  year={2025},
  organization={IEEE},
  address={San Jose, California, USA},
  note={The Harker School}
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the mycoremediation research community
- Built with Python, scikit-learn, pandas, and other open-source tools

## Contact

- **Primary Author**: [Danika Gupta] - [dan@gprof.com]
- **Project Link**: https://github.com/DanikaGupta/Deep-Myco
- **Issues**: Please use GitHub Issues for bug reports and feature requests

---

**Keywords**: mycoremediation, bioremediation, fungi, machine learning, environmental cleanup, large language models, data extraction
