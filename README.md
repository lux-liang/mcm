# TECM Framework: Task-Exposure-Congestion-Market Model

[![MCM/ICM 2026](https://img.shields.io/badge/MCM%2FICM-2026%20Problem%20F-blue)](https://www.comap.com/contests/mcm-icm)
[![LaTeX](https://img.shields.io/badge/LaTeX-Paper-green)](main.tex)
[![Python](https://img.shields.io/badge/Python-3.8%2B-yellow)](code/)

## Overview

This repository contains the complete implementation of the **Task-Exposure-Congestion-Market (TECM)** framework, developed for the 2026 MCM/ICM Problem F: *"To Choose or Refuse Gen-AI"*.

The TECM framework provides a principled approach for analyzing Generative AI's differential impacts on employment across occupational categories, with actionable recommendations for educational institutions.

## Key Innovations

1. **Task-Granular Decomposition**: Disaggregates occupations into weighted task units with distinct AI susceptibility profiles
2. **Verification-Bottleneck Congestion (VBC)**: Models how finite human verification capacity constrains sustainable AI adoption
3. **Physical Protection Index ($P_i$)**: Quantifies structural resistance to AI displacement from physical task requirements
4. **Multi-Channel Learning**: Captures skill acquisition through job-based, social, and autonomous pathways
5. **Educational Feedback Loop**: Direct mapping from model outputs to institution-specific recommendations

## Target Occupations

| Category | Occupation | SOC Code | Institution |
|----------|------------|----------|-------------|
| STEM | Information Security Analysts | 15-1212 | Carnegie Mellon University |
| Trade | Electricians | 47-2111 | Lansing Community College |
| Arts | Graphic Designers | 27-1024 | Rhode Island School of Design |

## Repository Structure

```
mcm/
├── main.tex                    # Main LaTeX document
├── mcmthesis.cls              # MCM/ICM thesis class
├── refs.bib                   # Bibliography
├── sections/                  # Paper sections
│   ├── 1_introduction.tex
│   ├── 2_problem_analysis.tex
│   ├── 3_assumptions.tex
│   ├── 4_data_sources.tex
│   ├── 5_model_development.tex
│   ├── 6_results.tex
│   ├── 7_recommendations.tex
│   ├── 8_beyond_employment.tex
│   ├── 9_sensitivity.tex
│   ├── 10_strengths_limitations.tex
│   ├── 11_conclusion.tex
│   ├── 12_references.tex
│   └── 13_ai_report.tex
├── figures/                   # Generated figures (PDF/PNG)
│   ├── fig01_architecture.pdf
│   ├── fig02_task_risk_heatmap.pdf
│   ├── fig03_congestion_heatmap.pdf
│   ├── fig04_employment_surface.pdf
│   ├── fig05_policy_surface.pdf
│   ├── fig06_phase_portrait.pdf
│   ├── fig07_calibration_fan.pdf
│   ├── fig08_sensitivity_heatmap.pdf
│   ├── fig09_pareto_front.pdf
│   ├── fig10_supply_demand_gap.pdf
│   └── fig11_scenario_multiples.pdf
└── README.md
```

## Mathematical Framework

### Core Equations

**Adoption Dynamics:**
$$\frac{dA}{dt} = \kappa_A A \left(1 - \frac{A}{A_{\text{cap}}}\right) - \lambda_G A \max(\rho - \rho_{\text{thresh}}, 0) + A_{\text{digital}}$$

**Employment Dynamics:**
$$\frac{dE}{dt} = \kappa_E \Xi_o A (1 - \text{sub\_ratio} \cdot A) E + \delta_0 E$$

**Verification Congestion:**
$$\rho(t) = \frac{\theta_V A (1 + \gamma_G A)}{V_{h,\max} (1 - \rho_V A)}$$

**Tipping Point:**
$$A^* = \frac{1}{2 \cdot \text{sub\_ratio}}$$

### State Variables

| Variable | Description |
|----------|-------------|
| $A(t)$ | AI adoption rate (fraction of workforce) |
| $E(t)$ | Employment level (normalized) |
| $V_s(t)$ | Workforce capability (composite skill index) |
| $\rho(t)$ | Verification congestion ratio |

## Key Results

### Employment Outcomes (60-month simulation)

| Occupation | Adoption $A(60)$ | Employment $E(60)/E(0)$ | Tipping Point $A^*$ |
|------------|------------------|-------------------------|---------------------|
| Information Security | 70.0% | +17.5% | 200% (unreachable) |
| Electricians | 9.3% | +2.9% | 500% (unreachable) |
| Graphic Designers | 85.0% | +0.2% | 90.9% (near ceiling) |

### Recommendations

| Institution | Enrollment | Curriculum Focus |
|-------------|------------|------------------|
| CMU (Info Sec) | Maintain | Frontier AI integration |
| Lansing CC (Elec) | +10.8% | Auxiliary AI tools |
| RISD (Design) | Maintain | Creative direction pivot |

## Compilation

### Requirements

- LaTeX distribution (TeX Live 2022+ or MiKTeX)
- Required packages: `float`, `graphicx`, `booktabs`, `algorithm`, `enumitem`

### Build

```bash
# Compile paper
cd /path/to/mcm
pdflatex main.tex
pdflatex main.tex  # Run twice for references

# Or use latexmk
latexmk -pdf main.tex
```

## Validation

Model validated against BLS OEWS 2010-2024 employment trends:

| Occupation | Observed CAGR | Model CAGR | MAPE |
|------------|---------------|------------|------|
| Information Security | 7.1% | 6.8% | 4.2% |
| Electricians | 1.7% | 1.9% | 11.8% |
| Graphic Designers | -0.4% | -0.3% | 8.7% |

All occupations achieve MAPE < 15%, satisfying validation criterion.

## Data Sources

- **O*NET 28.3**: Task decomposition, work activities, physical requirements
- **BLS OEWS**: Employment and wage time series (2010-2024)
- **IPEDS**: Educational program completions
- **Supplementary**: McKinsey AI automation estimates, WEF Future of Jobs Survey

## Authors

**Team 2602828** - MCM/ICM 2026

## License

This project is submitted for the Mathematical Contest in Modeling (MCM) 2026.

## Citation

```bibtex
@article{tecm2026,
  title={The Tipping Point Paradox: When AI Augmentation Becomes Displacement},
  author={Team 2602828},
  journal={MCM/ICM 2026 Problem F},
  year={2026}
}
```

## Acknowledgments

- COMAP for organizing MCM/ICM 2026
- U.S. Department of Labor for O*NET and BLS data
- Partner institutions for educational data
