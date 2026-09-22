## Review setup

- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no access to full methods, figures, tables, or supplementary information
- **Shared manuscript claim summary** The authors report a combined experimental and computational study of rotational diffusion of gammaD-crystallin during liquid-liquid phase separation (LLPS) in vitro. They use molecular dynamics (MD) simulations, electron paramagnetic resonance (EPR) spectroscopy with spin-labeled proteins, and fluorescence anisotropy. MD predicts a 1 to 2 order of magnitude retardation of rotational diffusion in the condensed phase. EPR-based viscosity nanoprobe measurements, calibrated with sucrose solutions, are claimed to validate the MD prediction. The study is presented as demonstrating the predictive power of MD and the utility of EPR nanoprobes for measuring condensate viscosity.
- **Visible evidence base** Abstract text only; no figures, tables, methods details, or numerical data provided
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, simulation parameters, EPR data analysis details, fluorescence anisotropy data, calibration curves, error estimates, and any statistical analysis

## Reviewer

- **Overall assessment** The abstract presents a potentially interesting and timely approach to measuring rotational dynamics within biomolecular condensates, combining three complementary techniques. The central claim, that MD-predicted rotational retardation is experimentally validated by EPR-based viscosity measurements, is plausible but cannot be assessed from the abstract alone. The key quantitative link between the EPR signal and the MD-derived retardation factor is not described in sufficient detail. The work would be of interest to the biophysics and soft matter communities, but the evidence base provided is insufficient to establish the case.
- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation, biomolecular condensates, protein diffusion and viscoelasticity, and those developing or applying EPR and fluorescence spectroscopic methods to crowded or condensed protein systems. The methodological combination may also interest computational biophysicists using MD to predict experimental observables.
- **Major strengths** The combination of MD, EPR, and fluorescence anisotropy is a strong multi-technique strategy. The use of spin-labeled proteins as viscosity nanoprobes is a creative and potentially powerful approach. The explicit attempt to validate MD predictions with experimental measurements addresses a common gap in the field. The focus on rotational rather than translational diffusion is a useful and underexplored angle.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract does not provide sufficient detail to evaluate the calibration procedure, the relationship between EPR-derived viscosity and rotational correlation time, the consistency between fluorescence and EPR measurements, or the error analysis. Without these, the validation claim is not established.
- **Assessment against Nature-style criteria** 
  - Originality: The combination of techniques is not entirely novel, but the specific application to rotational dynamics in LLPS condensates with EPR nanoprobes has original elements. 
  - Scientific importance: Potentially important for understanding condensate viscoelasticity and the physical chemistry of LLPS, but the significance depends on the robustness of the validation. 
  - Interdisciplinary readership: Likely to appeal to biophysicists, physical chemists, and soft matter scientists; broader cell biology interest is plausible but not demonstrated. 
  - Technical soundness: Cannot be assessed from the abstract; the methods are not described in sufficient detail. 
  - Readability for nonspecialists: The abstract is reasonably clear but uses field-specific terms (e.g., "viscosity nanoruler") without full explanation.
- **Recommendation posture** Currently not established from the provided evidence. Supportive if the technical concerns are resolved with full data and methods.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "Aided by a viscosity nanoruler calibrated with solutions at increasing sucrose concentrations, we validated the rotational diffusion retardation predicted by MD simulations."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract states that EPR measurements validated the MD-predicted retardation, but no quantitative comparison is presented. It is unclear how the EPR-derived viscosity was converted to a rotational diffusion retardation factor, how the calibration with sucrose solutions relates to the protein condensate environment, and what level of agreement was achieved between MD and experiment.
- **Why it matters** The central claim of the paper is the experimental validation of MD predictions. Without quantitative details, the reader cannot judge whether the agreement is meaningful or coincidental, and whether the EPR nanoprobe approach is reliable in condensates.
- **Resolution test** Provide a direct comparison of MD-predicted and EPR-measured rotational correlation times or retardation factors, including error bars, and a clear description of the conversion from EPR-derived viscosity to rotational dynamics.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological clarity
- **Claim pointer** "To obtain the rotational dynamics in the dilute phase, we used fluorescence anisotropy and to extract the retardation factor in the condensed phase, we used spin-labeled gammaD-crystallin proteins as EPR viscosity nanoprobes."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract does not explain how fluorescence anisotropy and EPR measurements are reconciled. Fluorescence anisotropy reports on the rotational motion of the fluorophore, which may not report on the same timescale or the same protein region as the spin label used in EPR. The relationship between the two measurements and the MD simulations is not described.
- **Why it matters** If the two experimental techniques probe different aspects of rotational dynamics, combining them into a single retardation factor may be invalid. The reader needs to understand the assumptions and potential systematic differences.
- **Resolution test** Clarify the timescales and molecular origins of the fluorescence and EPR signals, and show that they are consistent with each other and with MD in the dilute phase before applying them to the condensed phase.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Data availability
- **Claim pointer** "MD simulations performed under dilute and crowded conditions show that the rotational diffusion of crystallin in water is retarded by 1 to 2 orders of magnitude in the condensed phase."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract reports a 1 to 2 order of magnitude retardation from MD, but no simulation details are given, such as force field, system size, simulation length, or how the condensed phase was modeled. The range of 1 to 2 orders of magnitude is broad, and it is unclear whether this reflects uncertainty, variation with conditions, or different protein regions.
- **Why it matters** The MD prediction is the benchmark against which experiments are compared. Without knowing the simulation setup and the source of the range, the prediction cannot be critically evaluated.
- **Resolution test** Provide simulation parameters, convergence checks, and a breakdown of the retardation factor by condition or protein region, with uncertainties.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "viscosity nanoruler"
- **Evidence pointer** Abstract; location not provided
- **Issue** The term "viscosity nanoruler" is not standard and is not defined in the abstract.
- **Required correction** Define the term or replace with a more standard description, such as "EPR-based viscosity probe calibrated with sucrose solutions."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Scope clarity
- **Affected element** "Changing the environmental properties with cosolutes, molecular crowders, protein partners, temperature, pressure, etc."
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract mentions cosolutes in the introduction but does not specify which cosolutes were used in the experiments or how they affected the results.
- **Required correction** Specify the cosolutes used and their role in the study, or remove the general statement if not directly relevant.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Generalizability
- **Affected element** "This study underlines the predictive power of MD simulations"
- **Evidence pointer** Abstract; location not provided
- **Issue** The claim of MD predictive power is based on a single protein system and a single observable. This is a strong generalization from limited evidence.
- **Required correction** Soften the claim to reflect the specific system studied, e.g., "for this system" or "in this case."

## Risk / unsupported claims

- The claim that EPR measurements "validated" the MD prediction is unsupported without quantitative comparison data.
- The claim that the study "underlines the predictive power of MD simulations" is overgeneralized from a single system and observable.
- The relationship between the sucrose-based calibration and the protein condensate environment is not established.
- The consistency between fluorescence anisotropy and EPR measurements is not demonstrated.
- The range of 1 to 2 orders of magnitude retardation from MD is not explained or justified.