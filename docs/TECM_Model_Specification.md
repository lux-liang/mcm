# TECM Framework - Complete Model Specification

## Overview

The **Task–Exposure–Congestion–Market (TECM)** framework comprises three interconnected models that share state variables and create feedback loops to analyze Gen-AI's impact on employment across occupational categories.

---

## State Variables

| Symbol | Name | Description | Domain |
|--------|------|-------------|--------|
| $A(t)$ | Adoption Rate | Fraction of workforce using AI tools | $[0, A_{cap}]$ |
| $E(t)$ | Employment Level | Number of employed workers | $\mathbb{R}^+$ |
| $V_s(t)$ | Workforce Capability | AI skill level of workforce | $[0, V_{s,max}]$ |
| $\rho(t)$ | Congestion Ratio | Verification bottleneck severity | $[0, 1]$ |
| $D(t)$ | Demand Multiplier | Market demand response to cost | $\mathbb{R}^+$ |

---

## Model I: Task Decomposition & Risk Assessment

### Purpose
Decompose occupations into weighted task units and quantify AI susceptibility.

### Task Representation
Each occupation $o$ is represented as:
$$o = \{(\tau_k, w_k, \xi_k, p_k)\}_{k=1}^K$$

where:
- $\tau_k$: Task descriptor (from O*NET)
- $w_k$: Importance weight ($\sum_k w_k = 1$)
- $\xi_k \in [0,1]$: AI exposure score (from GPTs/AIOE)
- $p_k \in \{0,1\}$: Physical requirement indicator

### Key Equations

**Composite Exposure Index:**
$$\Xi_o = \sum_{k=1}^K w_k \cdot \xi_k \cdot (1 - \alpha_p \cdot p_k)$$

- $\alpha_p = 0.7$ (Physical Protection Effect parameter)

**Physical Protection Index:**
$$P_i = \frac{\sum_{k=1}^K w_k \cdot p_k \cdot (1 - \xi_k)}{\sum_{k=1}^K w_k}$$

### Output Values by Occupation

| Occupation | $\Xi_o$ | $P_i$ | $A_{cap}$ |
|------------|---------|-------|-----------|
| Information Security | 0.72 | 0.05 | 0.70 |
| Electricians | 0.18 | 0.78 | 0.25 |
| Graphic Designers | 0.81 | 0.12 | 0.85 |

---

## Model II: Verification-Bottleneck Congestion Dynamics

### Purpose
Model the dynamics of AI adoption, congestion, demand rebound, and employment.

### Key Equations

**1. Adoption Dynamics:**
$$\frac{dA}{dt} = \kappa_A A \left(1 - \frac{A}{A_{cap}}\right) - \lambda_G A \max(\rho - \rho_{thresh}, 0) + A_{digital}$$

- $\kappa_A$: Adoption rate coefficient
- $A_{cap}$: Adoption ceiling (from Model I)
- $\lambda_G$: Congestion sensitivity
- $\rho_{thresh}$: Congestion threshold
- $A_{digital}$: External digital push

**2. Verification Congestion:**
$$\rho(t) = \frac{\theta_V A (1 + \gamma_G A)}{V_{h,max} (1 - \rho_V A)}$$

- $\theta_V$: Verification load per unit adoption
- $\gamma_G$: Superlinearity coefficient (quadratic growth)
- $V_{h,max}$: Maximum human verification capacity
- $\rho_V$: Verification capacity reduction factor

The quadratic term $(1 + \gamma_G A)$ arises from:
1. **Selection combinatorics**: Pairwise comparisons grow $O(n^2)$
2. **Consistency maintenance**: Cross-output coherence checking

**3. Demand-Side Rebound (Jevons Paradox):**
$$D(t) = \left( \frac{C(t)}{C_0} \right)^{-\varepsilon_D}, \quad C(t) = C_0 (1 - \alpha_C A(t))$$

- $\alpha_C$: AI-induced cost reduction factor
- $\varepsilon_D$: Demand elasticity
- Higher adoption → Lower cost → Higher demand → More employment

**4. Dynamic Substitution Ratio:**
$$s(t) = \max\left( s_{min}, \frac{s_{base}}{1 + \beta_s V_s(t)} \right)$$

- $s_{base}$: Initial substitution ratio
- $\beta_s$: Skill-substitution elasticity
- $s_{min} = 0.05$: Irreducible floor
- This creates the **Educational Feedback Loop**: $V_s \uparrow \to s \downarrow \to A^* \uparrow$

**5. Employment Dynamics:**
$$\frac{dE}{dt} = \kappa_E \Xi_o A (1 - s(t) \cdot A) \cdot D(t) \cdot E + \delta_0 E$$

- $\kappa_E$: Employment elasticity
- $(1 - s(t) \cdot A)$: Augmentation-to-displacement factor
- $\delta_0$: Baseline employment growth

**6. Tipping Point:**
$$A^*(t) = \frac{1}{2 \cdot s(t)}$$

When $A > A^*$, employment effect turns negative (displacement regime).

### Parameter Values

| Parameter | Info Sec | Electricians | Design |
|-----------|----------|--------------|--------|
| $\kappa_A$ | 0.25 | 0.08 | 0.30 |
| $s_{base}$ | 0.25 | 0.10 | 0.55 |
| $\theta_V$ | 1.5 | 0.8 | 2.0 |
| $\gamma_G$ | 0.5 | 0.3 | 0.7 |
| $\varepsilon_D$ | 0.5 | 0.4 | 0.6 |
| $\alpha_C$ | 0.20 | 0.10 | 0.25 |
| $\beta_s$ | 1.0 | 0.8 | 1.2 |

---

## Model III: Multi-Channel Learning

### Purpose
Model how workforce capability evolves through multiple learning channels.

### Capability Evolution:
$$\frac{dV_s}{dt} = L_{job} + L_{social} + L_{auto} - \delta_V V_s$$

**Learning Channels:**

| Channel | Formula | Description |
|---------|---------|-------------|
| On-Job | $L_{job} = \eta_{job} A (V_{s,max} - V_s) \mathbb{1}_{A > 0.05}$ | Learning by doing; requires minimum adoption |
| Social | $L_{social} = \eta_{social} A(1-A)\sqrt{V_s}$ | Peer learning; peaks at intermediate adoption |
| Autonomous | $L_{auto} = \eta_{auto} V_s (1 - V_s/V_{s,max})$ | Self-directed; logistic saturation |

**Educational Intervention:**
$$V_s^{new} = V_s + \phi_{curr} \cdot N_{grad} \cdot \Delta t$$

- $\phi_{curr}$: Curriculum AI-intensity (0.20-0.35 recommended for RISD)
- $N_{grad}$: Number of graduates per period

---

## Feedback Loops Summary

### 1. VBC Feedback (Negative)
$$A \uparrow \to \rho \uparrow \to \frac{dA}{dt} \downarrow$$
High adoption creates congestion that slows further adoption.

### 2. Demand Rebound (Positive - Jevons Paradox)
$$A \uparrow \to C \downarrow \to D \uparrow \to E \uparrow$$
AI reduces costs, expanding demand and creating jobs.

### 3. Educational Feedback (Positive)
$$\phi \uparrow \to V_s \uparrow \to s \downarrow \to A^* \uparrow$$
Curriculum intervention raises skills, lowering substitution, extending augmentation window.

### 4. Learning Feedback (Positive)
$$A \uparrow \to L_{job} \uparrow \to V_s \uparrow \to s \downarrow$$
Adoption drives on-job learning, improving workforce capability.

---

## Simulation Parameters

- **Integration method**: 4th-order Runge-Kutta with adaptive step size
- **Time horizon**: 60 months
- **Initial conditions**: Calibrated to 2022 baseline
- **Validation**: Two-phase (2010-2022 pre-trend + 2023-2024 post-shock)

---

## Key Results

| Occupation | $A(60)$ | $E(60)/E(0)$ | $\rho_{max}$ | $V_s(60)$ | Regime |
|------------|---------|--------------|--------------|-----------|--------|
| Info Security | 70% | +17.5% | 0.32 | 0.697 | Augmentation |
| Electricians | 9.3% | +2.9% | 0.15 | 0.489 | Augmentation |
| Graphic Designers | 85% | +0.2% | 0.40 | 0.725 | Near Tipping |

---

## Data Flow Diagram

```
O*NET Tasks → Task Parser → Composite Exposure (Ξ_o) → Model II
                         → Physical Protection (P_i) → Adoption Cap

BLS OEWS → Calibration → Parameter Values
IPEDS → Graduate Counts → Educational Intervention
GPTs/AIOE → AI Exposure Scores → Task Risk Assessment

Model I ──┐
          ├──→ State Variables ──→ Tipping Point Analysis
Model II ─┤    (A, E, V_s, ρ, D)
          │         ↑
Model III─┘         │
          ←─────────┘ (Feedback)
```

---

## File Reference

| File | Description |
|------|-------------|
| `fig00_detailed_architecture.pdf` | Detailed flowchart with all equations |
| `fig01_architecture_v2.pdf` | Simplified overview diagram |
| `tikz_architecture.tex` | TikZ source (standalone, detailed) |
| `tikz_architecture_simple.tex` | TikZ source (for paper inclusion) |

