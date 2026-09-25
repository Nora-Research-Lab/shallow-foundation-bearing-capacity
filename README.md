![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Shallow Foundation Bearing Capacity
 
*For construction geologists and geotechnical engineers: enter soil strength and foundation parameters to instantly compute ultimate and allowable bearing capacity using Terzaghi's method.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Construction / Infrastructure Geology
 
A single-screen Gradio app that computes the ultimate and allowable bearing capacity of a continuous (strip) shallow foundation using Terzaghi's bearing capacity equation. Inputs: cohesion (c, kPa), internal friction angle (φ, degrees), unit weight of soil (γ, kN/m³), foundation width (B, m), foundation depth (Df, m), depth to water table below ground surface (Dw, m, optional, default 0 to indicate no water table effect), and factor of safety (FS, default 3). The core calculation: first, compute the bearing capacity factors using Terzaghi's formulas — Nq = exp(π tan φ) × tan²(45° + φ/2); Nc = (Nq - 1) / tan φ (if φ > 0, else 5.14 for φ=0); Nγ = 2 (Nq + 1) tan φ. If a water table is present and Dw < B + Df, adjust the unit weight to an effective value using a weighted average: γ_eff = γ × (Dw / (B + Df)) + (γ - γ_water) × (1 - Dw/(B + Df)), where γ_water = 9.81 kN/m³; otherwise γ_eff = γ. Then compute ultimate bearing capacity q_u = c Nc + γ_eff Df Nq + 0.5 γ_eff B Nγ. Allowable bearing capacity q_a = q_u / FS. The UI displays the intermediate N-factors in a small table, along with q_u and q_a values (rounded to 1 decimal). Additionally, the tool classifies the soil type based on φ: <5° → very soft clay; 5–10° → soft clay; 10–20° → stiff clay; 20–30° → dense sand; 30–40° → very dense sand; >40° → gravel/sand. All outputs update instantly on any input change. No AI/ML component is used.
 
## Run it
 
```bash
docker build -t shallow-foundation-bearing-capacity .
docker run -p 7860:7860 shallow-foundation-bearing-capacity
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-25.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
