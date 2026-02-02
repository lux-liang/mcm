#!/usr/bin/env python3
"""
TECM Framework - Detailed Model Flowchart Generator
Generates comprehensive flowchart showing all model components, equations, and feedback loops
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, ConnectionPatch
import numpy as np

# Set up figure with high DPI for quality
fig, ax = plt.subplots(1, 1, figsize=(20, 28), dpi=150)
ax.set_xlim(0, 20)
ax.set_ylim(0, 28)
ax.set_aspect('equal')
ax.axis('off')

# Color scheme (grayscale-friendly for paper)
colors = {
    'data': '#E8F4FD',      # Light blue
    'model1': '#FFF3E0',    # Light orange
    'model2': '#E8F5E9',    # Light green
    'model3': '#F3E5F5',    # Light purple
    'state': '#FFFFFF',     # White
    'output': '#FFEBEE',    # Light red
    'feedback': '#FFF8E1',  # Light yellow
    'border_data': '#1976D2',
    'border_model1': '#E65100',
    'border_model2': '#2E7D32',
    'border_model3': '#7B1FA2',
    'border_state': '#424242',
    'border_output': '#C62828',
    'arrow_direct': '#333333',
    'arrow_feedback': '#D32F2F',
}

def draw_box(ax, x, y, w, h, text, facecolor, edgecolor, fontsize=9, bold=False,
             math=False, linewidth=1.5, alpha=0.9):
    """Draw a rounded box with text"""
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                         facecolor=facecolor, edgecolor=edgecolor,
                         linewidth=linewidth, alpha=alpha)
    ax.add_patch(box)

    weight = 'bold' if bold else 'normal'
    if math:
        ax.text(x + w/2, y + h/2, text, ha='center', va='center',
                fontsize=fontsize, weight=weight)
    else:
        ax.text(x + w/2, y + h/2, text, ha='center', va='center',
                fontsize=fontsize, weight=weight, wrap=True)
    return box

def draw_arrow(ax, start, end, color='#333333', style='->', connectionstyle='arc3,rad=0',
               linewidth=1.5, linestyle='-'):
    """Draw an arrow between two points"""
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle=style, color=color,
                               connectionstyle=connectionstyle,
                               linewidth=linewidth, linestyle=linestyle))

def draw_section_title(ax, x, y, text, color, fontsize=12):
    """Draw a section title"""
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            weight='bold', color=color,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                     edgecolor=color, linewidth=2))

# ============== TITLE ==============
ax.text(10, 27.3, 'TECM Framework: Detailed Model Architecture',
        ha='center', va='center', fontsize=16, weight='bold')
ax.text(10, 26.8, 'Task–Exposure–Congestion–Market Career Evolution Model',
        ha='center', va='center', fontsize=11, style='italic', color='#555555')

# ============== DATA SOURCES (Bottom Layer) ==============
draw_section_title(ax, 10, 26, '📊 Data Sources', colors['border_data'])

data_y = 24.5
data_boxes = [
    (1.5, 'O*NET 28.3\n(Task Database)', 2.8),
    (5.0, 'BLS OEWS\n(Employment)', 2.8),
    (8.5, 'IPEDS\n(Graduates)', 2.8),
    (12.0, 'GPTs/AIOE\n(AI Exposure)', 2.8),
    (15.5, 'Industry Surveys\n(Adoption Rates)', 2.8),
]
for x, text, w in data_boxes:
    draw_box(ax, x, data_y, w, 1.0, text, colors['data'], colors['border_data'], fontsize=8)

# ============== MODEL I: Task Decomposition ==============
draw_section_title(ax, 10, 23.2, 'Model I: Task Decomposition & Risk Assessment', colors['border_model1'])

# Task decomposition process
m1_y = 21.2
draw_box(ax, 1, m1_y, 4, 1.5,
         'Task Parser\n' + r'$o = \{(\tau_k, w_k, \xi_k, p_k)\}_{k=1}^K$',
         colors['model1'], colors['border_model1'], fontsize=8)

draw_box(ax, 6, m1_y, 4, 1.5,
         'Composite Exposure\n' + r'$\Xi_o = \sum_k w_k \xi_k (1-\alpha_p p_k)$',
         colors['model1'], colors['border_model1'], fontsize=8)

draw_box(ax, 11, m1_y, 4, 1.5,
         'Physical Protection\n' + r'$P_i = \frac{\sum_k w_k p_k (1-\xi_k)}{\sum_k w_k}$',
         colors['model1'], colors['border_model1'], fontsize=8)

draw_box(ax, 16, m1_y, 3, 1.5,
         'Outputs:\n' + r'$\Xi_o, P_i, A_{cap}$',
         colors['model1'], colors['border_model1'], fontsize=8, bold=True)

# Arrows for Model I
draw_arrow(ax, (3, data_y), (3, m1_y + 1.5))
draw_arrow(ax, (5, m1_y + 0.75), (6, m1_y + 0.75))
draw_arrow(ax, (10, m1_y + 0.75), (11, m1_y + 0.75))
draw_arrow(ax, (15, m1_y + 0.75), (16, m1_y + 0.75))

# ============== MODEL II: VBC Dynamics (Main Engine) ==============
draw_section_title(ax, 10, 19.8, 'Model II: Verification-Bottleneck Congestion Dynamics', colors['border_model2'])

# State Variables Box
state_y = 17.5
ax.add_patch(FancyBboxPatch((0.5, state_y - 0.3), 19, 2.2,
                            boxstyle="round,pad=0.02,rounding_size=0.2",
                            facecolor='#F5F5F5', edgecolor='#888888',
                            linewidth=1, linestyle='--', alpha=0.5))
ax.text(10, state_y + 1.6, 'State Variables (Shared Across Models)',
        ha='center', va='center', fontsize=9, style='italic', color='#666666')

state_boxes = [
    (1, r'$A(t)$' + '\nAdoption', '#E3F2FD', '#1565C0'),
    (4.8, r'$E(t)$' + '\nEmployment', '#E8F5E9', '#2E7D32'),
    (8.6, r'$V_s(t)$' + '\nCapability', '#F3E5F5', '#7B1FA2'),
    (12.4, r'$\rho(t)$' + '\nCongestion', '#FFF3E0', '#EF6C00'),
    (16.2, r'$D(t)$' + '\nDemand', '#FFEBEE', '#C62828'),
]
for x, text, fc, ec in state_boxes:
    draw_box(ax, x, state_y, 3, 1.2, text, fc, ec, fontsize=8, linewidth=2)

# Dynamics Equations
dyn_y = 14.5
# Adoption Dynamics
draw_box(ax, 0.5, dyn_y, 5.5, 2.5,
         'Adoption Dynamics\n' +
         r'$\frac{dA}{dt} = \kappa_A A(1-\frac{A}{A_{cap}})$' + '\n' +
         r'$- \lambda_G A \max(\rho - \rho_{th}, 0)$' + '\n' +
         r'$+ A_{digital}$',
         colors['model2'], colors['border_model2'], fontsize=7)

# Congestion
draw_box(ax, 6.5, dyn_y, 4, 2.5,
         'Congestion\n' +
         r'$\rho = \frac{\theta_V A(1+\gamma_G A)}{V_{h,max}(1-\rho_V A)}$' + '\n' +
         '(Quadratic growth)',
         colors['model2'], colors['border_model2'], fontsize=7)

# Demand Rebound
draw_box(ax, 11, dyn_y, 4, 2.5,
         'Demand Rebound\n(Jevons Paradox)\n' +
         r'$D = (C/C_0)^{-\varepsilon_D}$' + '\n' +
         r'$C = C_0(1-\alpha_C A)$',
         colors['model2'], colors['border_model2'], fontsize=7)

# Employment Dynamics
draw_box(ax, 15.5, dyn_y, 4, 2.5,
         'Employment\n' +
         r'$\frac{dE}{dt} = \kappa_E \Xi_o A$' + '\n' +
         r'$\times(1-s(t) \cdot A)$' + '\n' +
         r'$\times D(t) \cdot E + \delta_0 E$',
         colors['model2'], colors['border_model2'], fontsize=7)

# Dynamic Substitution
draw_box(ax, 6.5, dyn_y - 2.8, 6.5, 1.8,
         'Dynamic Substitution Ratio (Educational Feedback)\n' +
         r'$s(t) = \max(s_{min}, \frac{s_{base}}{1+\beta_s V_s(t)})$' + '  →  ' +
         r'Tipping Point: $A^* = \frac{1}{2 \cdot s(t)}$',
         colors['feedback'], '#FF8F00', fontsize=7, linewidth=2)

# Arrows connecting dynamics to state
draw_arrow(ax, (3.25, state_y), (3.25, dyn_y + 2.5))
draw_arrow(ax, (8.5, state_y), (8.5, dyn_y + 2.5))
draw_arrow(ax, (13, state_y), (13, dyn_y + 2.5))
draw_arrow(ax, (17.5, state_y), (17.5, dyn_y + 2.5))

# Cross connections
draw_arrow(ax, (6, dyn_y + 1.25), (6.5, dyn_y + 1.25), style='->')  # A to ρ
draw_arrow(ax, (10.5, dyn_y + 1.25), (11, dyn_y + 1.25), style='->')  # ρ to D
draw_arrow(ax, (15, dyn_y + 1.25), (15.5, dyn_y + 1.25), style='->')  # D to E

# ============== MODEL III: Multi-Channel Learning ==============
draw_section_title(ax, 10, 10.8, 'Model III: Multi-Channel Learning & Educational Feedback', colors['border_model3'])

m3_y = 8.2
# Learning channels
draw_box(ax, 0.5, m3_y, 4, 2.2,
         'On-Job Learning\n' +
         r'$L_{job} = \eta_{job} A$' + '\n' +
         r'$(V_{max} - V_s) \mathbb{1}_{A>0.05}$',
         colors['model3'], colors['border_model3'], fontsize=7)

draw_box(ax, 5, m3_y, 4, 2.2,
         'Social Learning\n' +
         r'$L_{social} = \eta_{soc}$' + '\n' +
         r'$A(1-A)\sqrt{V_s}$' + '\n' +
         '(peaks at mid-adoption)',
         colors['model3'], colors['border_model3'], fontsize=7)

draw_box(ax, 9.5, m3_y, 4, 2.2,
         'Autonomous Learning\n' +
         r'$L_{auto} = \eta_{auto}$' + '\n' +
         r'$V_s(1-\frac{V_s}{V_{max}})$',
         colors['model3'], colors['border_model3'], fontsize=7)

draw_box(ax, 14, m3_y, 5.5, 2.2,
         'Capability Evolution\n' +
         r'$\frac{dV_s}{dt} = L_{job} + L_{social}$' + '\n' +
         r'$+ L_{auto} - \delta_V V_s$',
         colors['model3'], colors['border_model3'], fontsize=7, bold=True)

# Educational Intervention
draw_box(ax, 5, m3_y - 2, 9.5, 1.5,
         'Educational Intervention: ' +
         r'$V_s^{new} = V_s + \phi_{curr} \cdot N_{grad} \cdot \Delta t$' + '\n' +
         'Curriculum AI-intensity (φ) → Workforce capability boost',
         colors['feedback'], '#FF8F00', fontsize=8, linewidth=2)

# Arrows for Model III
draw_arrow(ax, (4.5, m3_y + 1.1), (5, m3_y + 1.1))
draw_arrow(ax, (9, m3_y + 1.1), (9.5, m3_y + 1.1))
draw_arrow(ax, (13.5, m3_y + 1.1), (14, m3_y + 1.1))
draw_arrow(ax, (9.75, m3_y), (9.75, m3_y - 0.3), style='->', connectionstyle='arc3,rad=0')

# ============== FEEDBACK LOOPS (highlighted) ==============
ax.text(10, 5.2, 'Key Feedback Loops', ha='center', va='center',
        fontsize=11, weight='bold', color='#C62828')

fb_y = 3.5
# Feedback loop descriptions
fb_boxes = [
    (0.5, 'VBC Feedback\n' + r'$A\uparrow \to \rho\uparrow \to dA/dt\downarrow$' + '\n(Congestion slows adoption)', '#FFCDD2'),
    (5.2, 'Demand Rebound\n' + r'$A\uparrow \to C\downarrow \to D\uparrow \to E\uparrow$' + '\n(Jevons Paradox)', '#C8E6C9'),
    (10, 'Educational Loop\n' + r'$\phi\uparrow \to V_s\uparrow \to s\downarrow \to A^*\uparrow$' + '\n(Extends augmentation)', '#E1BEE7'),
    (14.8, 'Learning Loop\n' + r'$A\uparrow \to L_{job}\uparrow \to V_s\uparrow$' + '\n(Skill accumulation)', '#B3E5FC'),
]
for x, text, fc in fb_boxes:
    draw_box(ax, x, fb_y, 4.3, 1.5, text, fc, '#666666', fontsize=7, linewidth=1)

# ============== OUTPUT LAYER ==============
draw_section_title(ax, 10, 2.2, 'Decision Outputs & Policy Recommendations', colors['border_output'])

out_y = 0.5
out_boxes = [
    (0.5, 'Enrollment\nStrategy', 3.2),
    (4.2, 'Curriculum\nRedesign (φ)', 3.2),
    (7.9, 'Tipping Point\nMonitoring', 3.2),
    (11.6, 'Supply-Demand\nProjection', 3.2),
    (15.3, 'Risk\nAssessment', 3.2),
]
for x, text, w in out_boxes:
    draw_box(ax, x, out_y, w, 1.0, text, colors['output'], colors['border_output'], fontsize=8)

# ============== MAJOR FLOW ARROWS ==============
# Model I to State Variables
draw_arrow(ax, (17.5, m1_y), (17.5, state_y + 1.2), style='-|>', linewidth=2)
ax.text(18.2, (m1_y + state_y + 1.2)/2, r'$\Xi_o, P_i$', fontsize=8, color='#666666')

# State to Outputs
draw_arrow(ax, (10, state_y - 0.3), (10, dyn_y + 2.5), style='-|>', linewidth=2)

# Dynamics to sub_ratio
draw_arrow(ax, (9.75, dyn_y), (9.75, dyn_y - 0.8), style='-|>', linewidth=1.5, color='#FF8F00')

# sub_ratio feedback to Employment
draw_arrow(ax, (13, dyn_y - 1.9), (17.5, dyn_y), style='->', linewidth=1.5,
           color='#FF8F00', connectionstyle='arc3,rad=-0.3', linestyle='--')

# Model III to State (V_s)
draw_arrow(ax, (16.75, m3_y + 2.2), (10.1, state_y), style='-|>', linewidth=2,
           connectionstyle='arc3,rad=0.2')

# Educational intervention to V_s
draw_arrow(ax, (9.75, m3_y - 0.5), (9.75, m3_y), style='->', linewidth=1.5, color='#FF8F00')

# ============== LEGEND ==============
legend_y = 0.3
ax.add_patch(FancyBboxPatch((0.2, -0.8), 19.6, 0.9,
                            boxstyle="round,pad=0.02", facecolor='#FAFAFA',
                            edgecolor='#CCCCCC', linewidth=1))

legend_items = [
    (1, '—— Direct Effect', '#333333', '-'),
    (4.5, '- - Feedback Loop', '#D32F2F', '--'),
    (8.5, '█ Model I', colors['model1'], None),
    (11, '█ Model II', colors['model2'], None),
    (13.5, '█ Model III', colors['model3'], None),
    (16.5, '█ State Var.', '#F5F5F5', None),
]

for x, text, color, ls in legend_items:
    if ls is not None:
        ax.plot([x, x+0.8], [-0.35, -0.35], color=color, linestyle=ls, linewidth=2)
        ax.text(x+1, -0.35, text, fontsize=8, va='center')
    else:
        ax.add_patch(plt.Rectangle((x, -0.5), 0.4, 0.3, facecolor=color, edgecolor='#666666'))
        ax.text(x+0.5, -0.35, text, fontsize=8, va='center')

# Save figure
plt.tight_layout()
plt.savefig('/mnt/d/f/figures/fig00_detailed_architecture.pdf',
            format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('/mnt/d/f/figures/fig00_detailed_architecture.png',
            format='png', bbox_inches='tight', dpi=300)
print("Detailed flowchart saved to figures/fig00_detailed_architecture.pdf and .png")

# Also create a simplified version for the paper
fig2, ax2 = plt.subplots(1, 1, figsize=(16, 12), dpi=150)
ax2.set_xlim(0, 16)
ax2.set_ylim(0, 12)
ax2.set_aspect('equal')
ax2.axis('off')

# Simplified version title
ax2.text(8, 11.5, 'TECM Framework Overview', ha='center', va='center',
         fontsize=14, weight='bold')

# Three model boxes
draw_box(ax2, 0.5, 7, 4.5, 3.5,
         'Model I\nTask Decomposition\n& Risk Assessment\n\n' +
         r'$\Xi_o = \sum_k w_k \xi_k (1-\alpha_p p_k)$' + '\n' +
         r'$P_i$ = Physical Protection',
         colors['model1'], colors['border_model1'], fontsize=9)

draw_box(ax2, 5.75, 7, 4.5, 3.5,
         'Model II\nVBC Dynamics\n\n' +
         r'$\frac{dA}{dt}, \frac{dE}{dt}$' + '\n' +
         r'$\rho(t)$ = Congestion' + '\n' +
         r'$D(t)$ = Demand (Jevons)',
         colors['model2'], colors['border_model2'], fontsize=9)

draw_box(ax2, 11, 7, 4.5, 3.5,
         'Model III\nMulti-Channel Learning\n\n' +
         r'$\frac{dV_s}{dt} = L_{job} + L_{soc}$' + '\n' +
         r'$+ L_{auto} - \delta_V V_s$' + '\n' +
         'Educational Feedback',
         colors['model3'], colors['border_model3'], fontsize=9)

# State variables in center
draw_box(ax2, 4, 4, 8, 2,
         'Shared State Variables\n' +
         r'$A(t)$ Adoption  |  $E(t)$ Employment  |  $V_s(t)$ Capability  |  $\rho(t)$ Congestion  |  $D(t)$ Demand',
         '#F5F5F5', '#424242', fontsize=9, linewidth=2)

# Tipping point
draw_box(ax2, 5, 1.5, 6, 1.5,
         'Tipping Point Analysis\n' +
         r'$A^*(t) = \frac{1}{2 \cdot s(t)}$ where $s(t) = \frac{s_{base}}{1+\beta_s V_s(t)}$',
         colors['feedback'], '#FF8F00', fontsize=9, linewidth=2)

# Arrows
draw_arrow(ax2, (2.75, 7), (6, 5.5), style='-|>', linewidth=2)
draw_arrow(ax2, (8, 7), (8, 6), style='-|>', linewidth=2)
draw_arrow(ax2, (13.25, 7), (10, 5.5), style='-|>', linewidth=2)
draw_arrow(ax2, (8, 4), (8, 3), style='-|>', linewidth=2)

# Feedback arrows
draw_arrow(ax2, (12, 5), (13.25, 7), style='->', linewidth=1.5, color='#D32F2F',
           connectionstyle='arc3,rad=0.3', linestyle='--')
ax2.text(13.5, 6, r'$V_s \to s\downarrow$', fontsize=8, color='#D32F2F')

draw_arrow(ax2, (4, 5), (2.75, 7), style='->', linewidth=1.5, color='#D32F2F',
           connectionstyle='arc3,rad=-0.3', linestyle='--')
ax2.text(2, 6, r'$\Xi_o, P_i$', fontsize=8, color='#D32F2F')

plt.tight_layout()
plt.savefig('/mnt/d/f/figures/fig01_architecture_v2.pdf',
            format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('/mnt/d/f/figures/fig01_architecture_v2.png',
            format='png', bbox_inches='tight', dpi=300)
print("Simplified flowchart saved to figures/fig01_architecture_v2.pdf and .png")
