# TECM模型框架流程图 - 详细绘制提示词

## 一、总体要求

**图表类型**: 学术论文级别的模型架构流程图
**风格**: 清晰、专业、适合黑白打印
**尺寸**: 宽16cm × 高22cm（A4纸可容纳）
**字体**: 正文使用无衬线字体，数学公式使用LaTeX渲染
**配色方案**: 使用浅色填充+深色边框，确保打印友好

---

## 二、整体布局（自上而下6层结构）

```
┌────────────────────────────────────────────────────────────────┐
│ 第1层: 标题区                                                   │
├────────────────────────────────────────────────────────────────┤
│ 第2层: 数据源层 (Data Sources)                                  │
├────────────────────────────────────────────────────────────────┤
│ 第3层: 模型I - 任务分解与风险评估                                │
├────────────────────────────────────────────────────────────────┤
│ 第4层: 状态变量层 + 模型II - VBC动力学                          │
├────────────────────────────────────────────────────────────────┤
│ 第5层: 模型III - 多渠道学习                                     │
├────────────────────────────────────────────────────────────────┤
│ 第6层: 决策输出层 (Decision Outputs)                            │
└────────────────────────────────────────────────────────────────┘
```

---

## 三、各层详细规格

### 第1层: 标题区
- **主标题**: "TECM Framework: Detailed Model Architecture"
  - 字号: 16pt, 加粗, 居中
- **副标题**: "Task–Exposure–Congestion–Market Career Evolution Model"
  - 字号: 11pt, 斜体, 灰色 (#666666)

---

### 第2层: 数据源层

**层标题**: "Data Sources" (蓝色边框圆角标签)

**包含5个数据源盒子** (横向排列，等间距):

| 序号 | 名称 | 内容 | 颜色 |
|------|------|------|------|
| 1 | O*NET 28.3 | Task Database | 浅蓝填充 #E8F4FD |
| 2 | BLS OEWS | Employment Statistics | 浅蓝填充 |
| 3 | IPEDS | Graduate Counts | 浅蓝填充 |
| 4 | GPTs/AIOE | AI Exposure Scores | 浅蓝填充 |
| 5 | Industry Surveys | Adoption Rates | 浅蓝填充 |

**盒子样式**: 圆角矩形 (radius=3pt), 边框颜色 #1976D2, 高度0.8cm

---

### 第3层: 模型I - 任务分解与风险评估

**层标题**: "Model I: Task Decomposition & Risk Assessment" (橙色边框)

**包含4个处理盒子** (横向排列，箭头连接):

```
[Task Parser] → [Composite Exposure] → [Physical Protection] → [Outputs]
```

| 盒子 | 内容 | 公式 |
|------|------|------|
| Task Parser | 任务解析器 | $o = \{(\tau_k, w_k, \xi_k, p_k)\}_{k=1}^K$ |
| Composite Exposure | 复合暴露指数 | $\Xi_o = \sum_k w_k \xi_k (1-\alpha_p p_k)$ |
| Physical Protection | 物理保护指数 | $P_i = \frac{\sum_k w_k p_k (1-\xi_k)}{\sum_k w_k}$ |
| Outputs | 输出 | $\Xi_o, P_i, A_{cap}$ (加粗) |

**盒子样式**: 圆角矩形, 浅橙色填充 #FFF3E0, 边框 #E65100, 高度1.5cm

---

### 第4层: 状态变量 + 模型II

#### 4.1 状态变量区 (灰色虚线框包围)

**标题**: "State Variables (Shared Across Models)" (斜体, 灰色)

**包含5个状态变量盒子** (横向排列):

| 变量 | 名称 | 填充色 | 边框色 |
|------|------|--------|--------|
| $A(t)$ | Adoption | #E3F2FD | #1565C0 |
| $E(t)$ | Employment | #E8F5E9 | #2E7D32 |
| $V_s(t)$ | Capability | #F3E5F5 | #7B1FA2 |
| $\rho(t)$ | Congestion | #FFF3E0 | #EF6C00 |
| $D(t)$ | Demand | #FFEBEE | #C62828 |

**盒子样式**: 圆角矩形, 边框加粗(1.5pt), 高度1.2cm

#### 4.2 模型II动力学方程区

**层标题**: "Model II: Verification-Bottleneck Congestion Dynamics" (绿色边框)

**包含4个方程盒子 + 1个反馈盒子**:

| 盒子 | 标题 | 核心公式 |
|------|------|----------|
| Adoption Dynamics | 采用动力学 | $\frac{dA}{dt} = \kappa_A A(1-\frac{A}{A_{cap}}) - \lambda_G A \max(\rho-\rho_{th},0) + A_{digital}$ |
| Congestion | 拥堵 | $\rho = \frac{\theta_V A(1+\gamma_G A)}{V_{h,max}(1-\rho_V A)}$ |
| Demand Rebound | 需求反弹 (Jevons Paradox) | $D = (C/C_0)^{-\varepsilon_D}$, $C = C_0(1-\alpha_C A)$ |
| Employment | 就业动力学 | $\frac{dE}{dt} = \kappa_E \Xi_o A(1-s(t)A)D(t)E + \delta_0 E$ |

**反馈盒子** (黄色高亮, 位于方程区下方):
- 标题: "Dynamic Substitution Ratio (Educational Feedback)"
- 公式: $s(t) = \max(s_{min}, \frac{s_{base}}{1+\beta_s V_s(t)})$ → Tipping Point: $A^* = \frac{1}{2 \cdot s(t)}$
- 样式: 黄色填充 #FFF8E1, 橙色边框 #FF8F00, 边框加粗

**盒子样式**: 浅绿色填充 #E8F5E9, 边框 #2E7D32, 高度2.5cm

---

### 第5层: 模型III - 多渠道学习

**层标题**: "Model III: Multi-Channel Learning & Educational Feedback" (紫色边框)

**包含4个学习渠道盒子**:

| 盒子 | 标题 | 公式 | 说明 |
|------|------|------|------|
| On-Job Learning | 在职学习 | $L_{job} = \eta_{job} A(V_{max}-V_s)\mathbb{1}_{A>0.05}$ | 需要最低采用率 |
| Social Learning | 社会学习 | $L_{social} = \eta_{soc} A(1-A)\sqrt{V_s}$ | 中等采用率时峰值 |
| Autonomous Learning | 自主学习 | $L_{auto} = \eta_{auto} V_s(1-\frac{V_s}{V_{max}})$ | 逻辑斯蒂饱和 |
| Capability Evolution | 能力演化 | $\frac{dV_s}{dt} = L_{job}+L_{soc}+L_{auto}-\delta_V V_s$ | 加粗显示 |

**教育干预盒子** (黄色高亮):
- 公式: $V_s^{new} = V_s + \phi_{curr} \cdot N_{grad} \cdot \Delta t$
- 说明: "Curriculum AI-intensity (φ) → Workforce capability boost"

**盒子样式**: 浅紫色填充 #F3E5F5, 边框 #7B1FA2, 高度2.2cm

---

### 第6层: 决策输出层

**层标题**: "Decision Outputs & Policy Recommendations" (红色边框)

**包含5个输出盒子**:

| 输出 | 名称 |
|------|------|
| 1 | Enrollment Strategy (招生策略) |
| 2 | Curriculum Redesign φ (课程重设计) |
| 3 | Tipping Point Monitoring (临界点监控) |
| 4 | Supply-Demand Projection (供需预测) |
| 5 | Risk Assessment (风险评估) |

**盒子样式**: 浅红色填充 #FFEBEE, 边框 #C62828, 高度1.0cm

---

## 四、箭头与连接规格

### 4.1 直接效果箭头 (实线)
- **样式**: 实线, 箭头末端, 线宽1.5pt
- **颜色**: 深灰色 #333333
- **用途**: 数据流、因果关系

### 4.2 反馈回路箭头 (虚线)
- **样式**: 虚线 (dash pattern: 5pt-3pt), 箭头末端, 线宽1.5pt
- **颜色**: 红色 #D32F2F
- **用途**: 反馈机制

### 4.3 关键连接

| 起点 | 终点 | 类型 | 标注 |
|------|------|------|------|
| Data Sources → Model I | Task Parser | 实线 | - |
| Model I Outputs → State Variables | A_cap, Ξ_o, P_i | 实线 | 标注参数名 |
| State Variables → Model II | 各动力学方程 | 实线 | - |
| Model II → sub_ratio | 反馈盒子 | 实线 | - |
| sub_ratio → Employment | 反馈影响 | 虚线 | "s(t)→E" |
| Model III → V_s | 能力更新 | 实线 | - |
| V_s → sub_ratio | 教育反馈 | 虚线 | "V_s↑→s↓→A*↑" |
| State Variables → Outputs | 决策支持 | 实线 | - |

---

## 五、反馈回路标注区

在图的侧边或下方添加4个反馈回路说明盒子:

| 反馈回路 | 公式表示 | 颜色 |
|---------|---------|------|
| VBC Feedback | $A\uparrow \to \rho\uparrow \to dA/dt\downarrow$ | 浅红 #FFCDD2 |
| Demand Rebound (Jevons) | $A\uparrow \to C\downarrow \to D\uparrow \to E\uparrow$ | 浅绿 #C8E6C9 |
| Educational Loop | $\phi\uparrow \to V_s\uparrow \to s\downarrow \to A^*\uparrow$ | 浅紫 #E1BEE7 |
| Learning Loop | $A\uparrow \to L_{job}\uparrow \to V_s\uparrow$ | 浅蓝 #B3E5FC |

---

## 六、图例 (Legend)

位于图底部，包含:

```
[实线箭头] Direct Effect    [虚线箭头] Feedback Loop
[橙色盒子] Model I          [绿色盒子] Model II
[紫色盒子] Model III        [灰色盒子] State Variables
[黄色盒子] Key Feedback Mechanisms
```

---

## 七、参数表 (可选，作为子图)

### 职业参数对比表

| Parameter | Info Security | Electricians | Graphic Design |
|-----------|---------------|--------------|----------------|
| $A_{cap}$ | 0.70 | 0.25 | 0.85 |
| $\kappa_A$ | 0.25 | 0.08 | 0.30 |
| $s_{base}$ | 0.25 | 0.10 | 0.55 |
| $P_i$ | 0.05 | 0.78 | 0.12 |
| $\Xi_o$ | 0.72 | 0.18 | 0.81 |
| $\theta_V$ | 1.5 | 0.8 | 2.0 |
| $\varepsilon_D$ | 0.5 | 0.4 | 0.6 |

---

## 八、AI绘图工具专用提示词

### 简化版提示词 (用于DALL-E, Midjourney等):

```
Create a professional academic flowchart for the TECM (Task-Exposure-Congestion-Market) framework. The diagram should have 6 horizontal layers from top to bottom:

1. Title: "TECM Framework Architecture"
2. Data Sources: 5 blue boxes (O*NET, BLS, IPEDS, GPTs/AIOE, Surveys)
3. Model I (orange): Task decomposition with equations Ξ_o and P_i
4. State Variables (gray) + Model II (green): 5 state variables (A, E, V_s, ρ, D) and 4 dynamics equations
5. Model III (purple): 3 learning channels + capability evolution
6. Decision Outputs (red): 5 policy recommendations

Include:
- Solid arrows for direct effects (dark gray)
- Dashed red arrows for feedback loops
- Yellow highlighted box for "Dynamic Substitution Ratio" and "Educational Intervention"
- Mathematical equations in LaTeX style
- Clean, professional style suitable for academic paper
- Grayscale-friendly color scheme
```

### Claude Artifacts专用提示词:

```
请使用React和SVG为我创建一个TECM模型框架的交互式流程图。

要求:
1. 6层垂直结构：标题→数据源→模型I→状态变量+模型II→模型III→输出
2. 每个模型用不同颜色区分（橙/绿/紫）
3. 包含所有数学公式（使用KaTeX渲染）
4. 显示4个反馈回路（用红色虚线表示）
5. 鼠标悬停显示详细说明
6. 支持点击展开/折叠各层
7. 可导出为SVG或PNG

核心公式:
- Ξ_o = Σw_k·ξ_k·(1-α_p·p_k)
- dA/dt = κ_A·A·(1-A/A_cap) - λ_G·A·max(ρ-ρ_th,0)
- ρ = θ_V·A·(1+γ_G·A) / [V_h,max·(1-ρ_V·A)]
- s(t) = s_base / (1+β_s·V_s)
- A* = 1 / (2·s(t))
- dV_s/dt = L_job + L_social + L_auto - δ_V·V_s
```

---

## 九、文件输出格式

| 用途 | 格式 | 分辨率 |
|------|------|--------|
| 论文嵌入 | PDF (矢量) | - |
| 演示文稿 | PNG | 300 DPI |
| 网页展示 | SVG | - |
| 打印海报 | PDF | - |

---

## 十、质量检查清单

- [ ] 所有公式LaTeX渲染正确
- [ ] 箭头方向逻辑一致
- [ ] 颜色对比度足够（可用色盲模拟器检查）
- [ ] 字体大小在打印后可读（最小8pt）
- [ ] 反馈回路清晰可辨
- [ ] 图例完整
- [ ] 无拼写错误
- [ ] 黑白打印时仍可区分各层

