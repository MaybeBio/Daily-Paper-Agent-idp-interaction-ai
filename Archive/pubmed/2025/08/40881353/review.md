## Review setup
- **Input scope** Full manuscript text (summary, introduction, results, discussion, methods, resource availability) as provided by the user.
- **Assessment boundary** Assessment is limited to the scientific content, methodology, and claims presented in the provided text. No external data, supplementary figures, or unpublished materials were accessed.
- **Shared manuscript claim summary** The authors claim that the dimerization domain (DD) of the SARS-CoV-2 nucleocapsid (N) protein is partially disordered in its monomeric form, adopts a dynamic conformational ensemble, and forms a high-affinity dimer (K_D ~12 nM at 23°C) through coupled folding and binding. They further propose that retained flexibility in the dimer may influence RNA interactions and phase separation.
- **Visible evidence base** The provided text includes descriptions of smFRET experiments, circular dichroism (CD) validation, all-atom Monte Carlo simulations, and van 't Hoff analysis. Specific numerical values are reported for transfer efficiencies, dissociation constants, and simulation-derived distances. Reference is made to supplementary figures and tables (e.g., Figures S1–S8, Tables S2, S5, S6) that are not included in the provided material.
- **Missing materials affecting confidence** Supplementary figures and tables (S1–S8, S2, S5, S6) are referenced but not provided. Detailed methods for smFRET data analysis, simulation parameters, and the binding model used for global fitting are not fully described in the main text. Raw data and code availability statements are incomplete.

## Reviewer
- **Overall assessment** This manuscript presents a rigorous and technically sophisticated investigation of the conformational dynamics and dimerization energetics of the SARS-CoV-2 N protein DD. The combination of single-molecule FRET, denaturant and temperature titrations, and all-atom simulations provides a compelling case for a partially disordered monomer that folds upon dimerization. The work addresses a significant gap in understanding the molecular mechanisms of N protein assembly. However, the absence of key supplementary data and some methodological details limits the ability to fully evaluate the robustness of the conclusions. The claim regarding the physiological relevance of the observed flexibility to RNA binding and phase separation is speculative and not directly tested.
- **Who would be interested in the results, and why** Structural biologists, biophysicists, and virologists studying coronavirus replication and assembly. The findings on coupled folding and binding in a viral protein with intrinsically disordered regions will also interest researchers in protein folding and phase separation. The methodological approach (smFRET combined with simulations) is broadly applicable and will appeal to the single-molecule biophysics community.
- **Major strengths**
  1. The use of single-molecule FRET at picomolar concentrations allows direct observation of monomeric and dimeric states without ensemble averaging artifacts.
  2. The combination of experimental measurements (smFRET, CD, denaturant and temperature titrations) with all-atom simulations provides complementary and mutually supportive evidence.
  3. The quantitative analysis of dimerization energetics (K_D, ΔH, ΔS, ΔC_p) is thorough and well-contextualized with previous work.
  4. The study addresses a biologically important question with direct relevance to viral replication and potential therapeutic targeting.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors report a dissociation constant of ~12 nM at 23°C for dimerization, derived from a global fit of amplitude curves to a binding model.
  - **Evidence pointer** Results section "Dimer formation induces folding of the DD"; supplemental information referenced for the binding model.
  - **Concern** The binding model used to extract K_D values is described only as "a binding model that accounts for the dimerization of labeled and unlabeled species" with details relegated to the supplemental information. Without access to the model equations, assumptions (e.g., equal activity coefficients, no aggregation, labeling efficiency), and fitting procedure, the reliability of the reported K_D values cannot be independently assessed. The discrepancy between K_D,L/U (6 ± 2 nM) and K_D,U/U (11 ± 3 nM) also requires explanation, as it suggests labeling may affect dimerization affinity.
  - **Why it matters** The quantitative K_D value is a central result of the paper and underpins the claim of "high-affinity" dimerization. If the model is flawed or the assumptions are inappropriate, the reported energetics could be systematically biased.
  - **Resolution test** Provide the full binding model equations, fitting procedure, and a sensitivity analysis in the main text or a clearly accessible supplement. Demonstrate that the model recovers known K_D values for a control system or that the results are robust to reasonable variations in model assumptions.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors state that "the addition of unlabeled protein stabilizes a folded dimer configuration with a high mean transfer efficiency, which is in agreement with predictions based on known structures."
  - **Evidence pointer** Results section "Dimer formation induces folding of the DD"; Figure 4A; Figure S1 for predicted transfer efficiency.
  - **Concern** The agreement between the observed mean transfer efficiency (0.84 ± 0.02) and the predicted value (~0.90 ± 0.06) is stated as "good agreement," but the difference (0.06) is comparable to the uncertainty in the prediction. The authors do not discuss potential sources of systematic discrepancy, such as dye orientation, linker dynamics, or local environment effects on dye photophysics. A more rigorous comparison, including a quantitative measure of agreement (e.g., overlap of confidence intervals) and a discussion of possible biases, is needed.
  - **Why it matters** The interpretation that the high-transfer-efficiency state corresponds to the folded dimer structure relies on this comparison. If the discrepancy is due to a partially unfolded dimer or dye artifacts, the structural interpretation would be weakened.
  - **Resolution test** Provide a quantitative comparison of the observed and predicted transfer efficiency distributions, including confidence intervals. Discuss and, if possible, experimentally test potential sources of discrepancy (e.g., using different dye pairs or labeling positions).
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Claim pointer** The authors propose that "the retained flexibility of the dimer can affect its interaction with RNA and phase separation propensity."
  - **Evidence pointer** Discussion section; Figure 8 (conceptual model).
  - **Concern** This claim is presented as a speculative hypothesis without direct experimental or simulation evidence linking dimer flexibility to RNA binding or phase separation. While the authors note that RNA does not affect the monomer-dimer equilibrium (Figure S6), they do not test whether dimer flexibility modulates RNA affinity or phase separation behavior.
  - **Why it matters** The broader significance of the work for understanding N protein function depends on this connection. Without direct evidence, the claim remains an untested hypothesis, which weakens the impact of the study.
  - **Resolution test** Perform experiments or simulations that directly test the effect of dimer flexibility on RNA binding affinity or phase separation propensity (e.g., using mutants that alter flexibility or varying solution conditions).
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Introduction
  - **Evidence pointer** Introduction, paragraph 2
  - **Issue** The introduction assumes familiarity with smFRET and its advantages without a brief explanation of the technique for readers outside the biophysics community.
  - **Required correction** Add one or two sentences explaining the basic principle of smFRET and why it is well-suited for studying conformational dynamics in flexible proteins.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Methods, smFRET section
  - **Evidence pointer** Methods section "smFRET"
  - **Issue** The methods state that "all measured data were analyzed using the Mathematica package Fretica" but do not specify the version or key analysis parameters (e.g., binning, background correction, FRET efficiency calculation).
  - **Required correction** Provide a more detailed description of the data analysis pipeline, including specific parameters and any corrections applied.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Results, "Temperature effect on dimer stability"
  - **Evidence pointer** Results section "Temperature effect on dimer stability"; Figure 6F
  - **Issue** The van 't Hoff analysis is performed over a limited temperature range (37°C–47°C), and the authors note a deviation from linearity when including the 23°C data point. The interpretation of ΔH and ΔS values as representative of the binding process may be overly simplistic given the observed curvature.
  - **Required correction** Discuss the limitations of the van 't Hoff analysis in the presence of heat capacity changes and consider presenting a more nuanced interpretation of the thermodynamic parameters.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Interdisciplinary readership
  - **Affected element** Discussion
  - **Evidence pointer** Discussion, paragraph 3
  - **Issue** The discussion of phase separation and LCST behavior is brief and may not be fully accessible to readers without a background in this area.
  - **Required correction** Provide a brief explanation of LCST and its relevance to N protein function, or refer readers to a review.
- **Technical failings that need to be addressed before the case is established**
  - R1-M1: The binding model used to extract K_D values is not fully described, preventing independent verification of the reported energetics.
  - R1-M2: The agreement between observed and predicted transfer efficiencies for the dimer state is not rigorously quantified, weakening the structural interpretation.
- **Assessment against Nature-style criteria**
  - **Originality** The work is original in its application of smFRET to the full-length N protein DD and in its quantitative characterization of coupled folding and binding. The finding that the monomer is a molten globule-like state is novel and significant.
  - **Scientific importance** The study provides important mechanistic insights into N protein dimerization, a key step in viral assembly. The results have implications for understanding RNA packaging and phase separation, though the direct link to these processes is not established.
  - **Interdisciplinary readership** The work will appeal to biophysicists, structural biologists, and virologists. The methods and findings are likely to be of interest to a broad readership, but the presentation may be somewhat technical for nonspecialists.
  - **Technical soundness** The experimental design and execution appear sound, but the lack of detailed methods for the binding model and data analysis limits the ability to fully assess technical rigor.
  - **Readability for nonspecialists** The manuscript is generally well-written but assumes familiarity with smFRET and related biophysical techniques. The introduction and discussion could be improved to make the work more accessible to a broader audience.
- **Recommendation posture** Supportive if technical concerns are resolved. The core findings are likely to be of significant interest, but the manuscript requires additional methodological detail and a more rigorous quantitative comparison to fully establish the case.

## Risk / unsupported claims
- The claim that "the retained flexibility of the dimer can affect its interaction with RNA and phase separation propensity" is speculative and not directly supported by the presented data.
- The reported K_D values (6 ± 2 nM and 11 ± 3 nM) cannot be fully evaluated without access to the binding model and fitting details.
- The interpretation of the high-transfer-efficiency state as the folded dimer structure relies on a qualitative agreement with predictions that is not rigorously quantified.
- The thermodynamic parameters (ΔH, ΔS) derived from the van 't Hoff analysis may be oversimplified given the observed deviation from linearity, and their interpretation should be treated with caution.