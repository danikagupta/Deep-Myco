# DeepMyco Documentation

Welcome to the comprehensive documentation for the DeepMyco project - Large Language Models for Scaling Mycoremediation.

## 📚 Documentation Structure

This documentation is organized into several key sections to help you understand, use, and contribute to the DeepMyco project:

### 🚀 [Tutorials](tutorials/)
**Start here if you're new to DeepMyco**
- **[Getting Started](tutorials/getting_started.md)** - Installation, setup, and first steps
- **[Dataset Exploration](tutorials/dataset_exploration.ipynb)** - Interactive exploration of the mycoremediation dataset
- **[Model Training](tutorials/model_training.ipynb)** - Train forecasting and recommendation models
- **[Making Predictions](tutorials/predictions.ipynb)** - Use trained models for mycoremediation predictions

### 🔬 [Methodology](methodology/)
**Deep dive into the research approach**
- **[LLM Extraction](methodology/llm_extraction.md)** - How we extracted data from 2,900+ research papers
- **[Experimental Protocols](methodology/experimental_protocols.md)** - Laboratory validation procedures
- **[Validation Procedures](methodology/validation_procedures.md)** - Data quality and model validation methods

### 📖 [API Reference](api/)
**Technical documentation for developers**
- **[Dataset API](api/dataset_api.md)** - Data loading and processing functions
- **[Models API](api/models_api.md)** - Machine learning model interfaces
- **[Utils API](api/utils_api.md)** - Utility functions and helpers

### 📄 [Research Paper](paper/)
**Published research and supplementary materials**
- **[DeepMyco Paper](paper/deepmyco_paper.pdf)** - Full IEEE AI-SI 2025 conference paper
- **[Supplementary Materials](paper/supplementary_materials.pdf)** - Additional data and analysis
- **[Figures](paper/figures/)** - High-resolution figures from the paper

## 🎯 Quick Navigation

### For Researchers
- Start with [Getting Started](tutorials/getting_started.md)
- Explore the [Dataset](tutorials/dataset_exploration.ipynb)
- Read the [Research Paper](paper/deepmyco_paper.pdf)
- Review [Experimental Protocols](methodology/experimental_protocols.md)

### For Developers
- Begin with [Getting Started](tutorials/getting_started.md)
- Check the [API Reference](api/)
- Explore [Model Training](tutorials/model_training.ipynb)
- Review [LLM Extraction Methods](methodology/llm_extraction.md)

### For Practitioners
- Read [Getting Started](tutorials/getting_started.md)
- Try [Making Predictions](tutorials/predictions.ipynb)
- Review [Validation Procedures](methodology/validation_procedures.md)
- Consult [Experimental Protocols](methodology/experimental_protocols.md)

## 📊 Key Research Contributions

### 🗄️ **First Public Mycoremediation Dataset**
- **812 experiments** extracted from research literature
- **168 time-series samples** tracking degradation over time
- **45+ fungal species** with taxonomic information
- **25+ pollutant types** including dyes and organic compounds

### 🤖 **Novel LLM-Powered Data Extraction**
- Automated extraction from **2,900+ research papers**
- **GPT-4 based** paper filtering and data extraction
- **80% precision** validated through manual review
- Open-source pipeline for reproducible research

### 📈 **Predictive ML Models**
- **Random Forest forecasting** with RMSE as low as 0.03
- **Fungal recommendation system** for unknown pollutants
- **Robustness analysis** identifying optimal fungal strains
- Validated through **laboratory experiments**

### 🔬 **Experimental Validation**
- **Spectroscopy confirmation** of decolorization predictions
- **Plant growth studies** using remediated water
- **Multiple fungal forms** tested (whole fungi and mycelium)
- **Real-world variability** assessment

## 🛠️ Technical Stack

- **Python 3.9+** with scientific computing libraries
- **Large Language Models**: GPT-4, Claude, Gemini
- **Machine Learning**: scikit-learn, XGBoost, PyTorch
- **Data Processing**: pandas, numpy, scipy
- **Visualization**: matplotlib, plotly, seaborn
- **Lab Equipment**: UV Spectroscopy (350-850nm)

## 📋 Dataset Overview

### Main Dataset Structure
```
mycoremediation_dataset.csv (812 experiments)
├── Fungal species and strain information
├── Dye/pollutant types and concentrations  
├── Experimental conditions (pH, temperature, duration)
├── Decolorization effectiveness (%)
└── Metadata (agitation, whole/mycelium, etc.)
```

### Time Series Data
```
timeseries_dataset.csv (168 samples)
├── Day-by-day degradation tracking
├── 3 fungal species × 5 dye types
├── Multiple pH conditions
└── 7-day experimental periods
```

## 🚦 Getting Started Checklist

- [ ] **Install Dependencies**: Follow [Getting Started](tutorials/getting_started.md)
- [ ] **Explore Dataset**: Run [Dataset Exploration](tutorials/dataset_exploration.ipynb)
- [ ] **Train Models**: Try [Model Training](tutorials/model_training.ipynb)
- [ ] **Make Predictions**: Use [Predictions Tutorial](tutorials/predictions.ipynb)
- [ ] **Read Research**: Review the [Full Paper](paper/deepmyco_paper.pdf)

## 🤝 Contributing to Documentation

We welcome contributions to improve this documentation! Here's how:

### 📝 **Improving Existing Docs**
1. Fork the repository
2. Edit documentation files (Markdown or Jupyter notebooks)
3. Test your changes locally
4. Submit a pull request

### ➕ **Adding New Documentation**
1. Follow the existing structure and naming conventions
2. Include code examples and clear explanations
3. Add your new files to this README's navigation
4. Update relevant cross-references

### 🧪 **Updating Tutorials**
1. Ensure notebooks run without errors
2. Include sample outputs and visualizations  
3. Test with the latest dataset versions
4. Add explanatory markdown cells

## 📞 Support and Community

### Getting Help
- **GitHub Issues**: Bug reports and feature requests
- **Discussions**: Questions and community support
- **Email**: dan@gprof.com for research collaborations

### Citation
If you use DeepMyco in your research, please cite our paper:
```bibtex
@inproceedings{gupta2025deepmyco,
  title={DeepMyco: Large Language Models for Scaling Mycoremediation},
  author={Gupta, Danika},
  booktitle={2025 IEEE Conference on AI for Sustainable Innovation},
  year={2025}
}
```

## 🏷️ Tags and Keywords

`mycoremediation` `bioremediation` `machine-learning` `large-language-models` `environmental-cleanup` `textile-dyes` `fungi` `sustainability` `water-treatment` `spectroscopy`

---

**Happy Researching! 🔬🌱**

*This documentation is continuously updated. Last updated: January 2025*
