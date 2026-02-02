# TECM Architecture Diagram — Napkin.ai Prompt (v3.0 Publication-Grade)
# ======================================================================
# Target: Top-tier academic conference figure quality
# Style: Clean layered architecture, no decorative noise, every element meaningful

## TITLE (top center)
"TECM Framework: Task–Exposure–Congestion–Market Model"
Subtitle below: "A Closed-Loop System for Analyzing Gen-AI Employment Impact"

## OVERALL LAYOUT
Three-layer structure, reading top-to-bottom.
Clean white background. NO colored vertical bars. NO scattered annotations.
Use subtle gray (#F3F4F6) horizontal bands to separate layers.

---

## LAYER 1: INPUT & TASK ANALYSIS (Top band, gray background)
Label on left margin: "Layer 1: Data & Task Decomposition"

### Row 1 — Data Sources (4 boxes, horizontal)
All boxes: rounded rectangle, fill #DBEAFE, border #2563EB, 1.5px

Box 1: "O*NET 30.1"
  Line 2: "41 Work Activities"
  Line 3: "Task Importance Ratings"

Box 2: "BLS OEWS"
  Line 2: "Employment Statistics"
  Line 3: "2010–2024 Time Series"

Box 3: "IPEDS"
  Line 2: "Graduate Completions"
  Line 3: "CIP–SOC Crosswalk"

Box 4: "AI Exposure Indices"
  Line 2: "GPTs-are-GPTs Scores"
  Line 3: "AIOE Ratings"

### Row 2 — Task Analysis Modules (2 boxes, horizontal, below Row 1)
All boxes: rounded rectangle, fill #E0E7FF, border #4F46E5, 1.5px

Box A: "Module A: Task Decomposition"
  Line 2: "Input: Raw O*NET activities"
  Line 3: "Output: Weighted tasks {(τ_k, w_k)}"

Box B: "Module B: Risk & Protection Scoring"
  Line 2: "Input: Task features + AI exposure"
  Line 3: "Output: CE_i (exposure), P_i (physical protection)"

Arrows: All 4 data boxes → converge into Module A and Module B

---

## LAYER 2: DYNAMIC CORE ENGINE (Center band, lightest purple background #F5F3FF)
Label on left margin: "Layer 2: Core Dynamics (Closed Loop)"

This layer contains THREE modules arranged LEFT → CENTER → RIGHT,
connected as a chain: Module C/D → Module E → Module F → (feedback arrow back to C/D)

### Module C/D (LEFT): "Friction & Threshold Engine"
Shape: Rounded rectangle, fill #FDF4FF, border #7C3AED, 2px (slightly larger)

Title: "Module C/D: Friction & Threshold Engine"
Content (3 lines, noun phrases only):
  "Inputs: P_i, CE_i, w_i from Module B"
  "Computes: A_cap (adoption ceiling), s (substitution ratio)"
  "Outputs: c(A) friction function, ρ threshold, cost C_H + C_AI"

Arrow from Module A/B → Module C/D (labeled: "task features")

### Module E (CENTER, LARGEST): "Coupled ODE System"
Shape: Double-bordered rounded rectangle, fill #EDE9FE, border #7C3AED, 3px
THIS IS THE VISUAL CENTER AND LARGEST ELEMENT OF THE DIAGRAM.

Title: "Module E: Coupled Dynamics"
Subtitle: "4th-order Runge–Kutta, Δt adaptive"

Inside Module E, show 4 state variable boxes arranged in a 2×2 grid:

  ┌─────────────┐    ┌─────────────┐
  │  A(t)       │───→│  ρ(t)       │
  │  Adoption   │    │  Congestion  │
  └──────┬──────┘    └──────┬──────┘
         │                   │
         ▼                   ▼
  ┌─────────────┐    ┌─────────────┐
  │  V_s(t)     │───→│  E(t)       │
  │  Capability  │    │  Employment  │
  └─────────────┘    └─────────────┘

Internal arrows (inside the E box):
  A(t) → ρ(t): labeled "drives verification load"
  A(t) → V_s(t): labeled "enables learning"
  ρ(t) → E(t): labeled "congestion penalty"
  V_s(t) → E(t): labeled "productivity gain"
  ρ(t) ⟶ A(t): dashed, labeled "adoption drag"

Below the 2×2 grid, one line of math:
  "dA/dt = κ_A · A(1 − A/A_cap) − λ · A · max(ρ − ρ_th, 0)"

Arrow from Module C/D → Module E (labeled: "A_cap, s, c(A), ρ_th")
Arrow from Module E → right (labeled: "trajectories A(t), E(t), ρ(t), V_s(t)")

### Module F (RIGHT): "Education & Policy Feedback"
Shape: Rounded rectangle, fill #FCE7F3, border #DB2777, 2px

Title: "Module F: Institutional Feedback"
Content (3 lines):
  "Controls: curriculum intensity, enrollment Δ, regulation"
  "Mechanism: Multi-channel learning (job + social + autonomous)"
  "Effects: update θ_V, λ_ρ, A_cap, supply S(t)"

Arrow from Module E → Module F (labeled: "current state {A, E, ρ, V_s}")
Arrow from Module F → Module C/D: DASHED, CURVED, colored #DB2777
  Label: "Policy Feedback Loop (parameter update)"
  This arrow goes from Module F back to Module C/D, forming a visible closed loop.

---

## LAYER 3: DECISION OUTPUTS (Bottom band, gray background)
Label on left margin: "Layer 3: Decision Outputs"

ONE ROW of 4 output boxes. No duplicates.
All boxes: rounded rectangle, fill #ECFDF5, border #10B981, 1.5px

Box 1: "Enrollment Strategy"
  Line 2: "CMU: maintain | LCC: +10.8% | RISD: maintain"

Box 2: "Curriculum Redesign"
  Line 2: "AI integration level per institution"

Box 3: "Tipping Point Map"
  Line 2: "A* = 1/(2·s) per occupation"

Box 4: "Supply–Demand Forecast"
  Line 2: "5-year gap projection"

Arrow from Module E → all 4 output boxes (fan-out)
Arrow from Module F → output boxes (secondary path)

---

## LEFT MARGIN: CALIBRATION LOOP
One long dashed blue arrow (#2563EB) from "Decision Outputs" back up to "Data Sources"
Label: "Calibration Loop: validate against BLS 2010–2024"

## RIGHT MARGIN: THREE OCCUPATION COLOR CODING
Small legend box in bottom-right corner:
  Blue dot (#2563EB): "Info Security Analysts (SOC 15-1212)"
  Orange dot (#F59E0B): "Electricians (SOC 47-2111)"
  Green dot (#10B981): "Graphic Designers (SOC 27-1024)"

---

## STRICT STYLE RULES
- ALL text must be in correct English. No abbreviations that could be misread.
- Font: Sans-serif (Inter, Helvetica, or similar). Body 9–10pt, titles 12pt.
- Maximum 3 lines per box. Use noun phrases, not sentences.
- Every arrow must have a label explaining what flows through it.
- No decorative elements: no gradients, no drop shadows, no background patterns.
- Color usage: only the 5 layer colors defined above + occupation legend colors.
- Line weights: 1.5px for normal boxes, 3px for Module E (core), 1px for arrows.
- The closed loop (F → C/D → E → F) must be visually obvious as the central story.
