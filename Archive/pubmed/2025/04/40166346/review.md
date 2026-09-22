## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and figure legends as provided.
- **Assessment boundary** Scientific content, technical soundness, logical coherence, and alignment with stated claims. Not assessed: editorial style, formatting, or grammatical issues.
- **Shared manuscript claim summary** The authors propose that paraspeckle core proteins FUS and NONO preferentially bind and condense with shell-associated NEAT1 RNA domains, contrary to the prevailing model. They further propose that the shell protein TDP-43 competes for binding to these same domains and, due to immiscibility with core proteins, forms surfactant-like layers that order the core-shell architecture of paraspeckles. A coarse-grained simulation model is presented to support this mechanism.
- **Visible evidence base** Results sections describing motif analysis, EMSA binding assays, in vitro condensate assays, FRAP measurements, and coarse-grained simulations. Methods sections detailing simulation parameters, protein purification, RNA transcription, and image analysis. Figures referenced: 1–5, S1–S10 (figure panels described in text but not all images visible in this text-only submission).
- **Missing materials affecting confidence** Actual figure images and supplementary tables (e.g., Table S1 with simulation parameters) are not provided in this text-only version. Raw data files and analysis scripts are referenced but not accessible. This limits independent verification of quantitative claims and visual evidence.

## Reviewer
- **Overall assessment** This manuscript addresses a significant open question in condensate biology: how multi-layered organization arises in paraspeckles. The work combines bioinformatics, biochemistry, and simulation to challenge the prevailing model of paraspeckle assembly. The finding that core proteins FUS and NONO prefer shell-associated RNA domains is surprising and potentially important. The proposed mechanism involving competitive RNA binding and protein immiscibility is conceptually novel. However, several technical concerns must be addressed before the case is fully established, particularly regarding the quantitative interpretation of EMSA data, the physiological relevance of the in vitro condensate conditions, and the parameterization of the simulation model.
- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, RNA biology, and phase separation. The work is also relevant to those studying nuclear body organization, lncRNA function, and the biophysical principles underlying sub-compartmentalization. The proposed mechanism of competitive binding and immiscibility could have broad implications for understanding multi-domain condensates beyond paraspeckles.
- **Major strengths** 1) The study directly challenges a prevailing model with new experimental data, which is scientifically valuable. 2) The combination of informatics, biochemistry, and simulation provides a multi-pronged approach. 3) The finding that FUS and NONO prefer shell-associated RNA is unexpected and well-supported by the motif and EMSA data. 4) The proposed mechanism of competitive binding and immiscibility is conceptually elegant and testable. 5) The inclusion of co-transcriptional assembly considerations adds physiological relevance.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (EMSA quantification), R1-M2 (simulation parameterization), R1-M3 (physiological relevance of condensate assays), R1-M4 (FRAP interpretation).
- **Assessment against Nature-style criteria** **Originality:** High. The finding that core proteins prefer shell-associated RNA domains contradicts the prevailing model and offers a new conceptual framework. **Scientific importance:** High. Paraspeckles are a paradigm for multi-domain condensates, and this work could reshape understanding of their assembly. **Interdisciplinary readership:** Moderate to high. The work bridges RNA biology, biophysics, and computational modeling, appealing to a broad audience. **Technical soundness:** Moderate. The experimental approaches are generally appropriate, but several quantitative analyses and simulation parameterizations require clarification and additional controls. **Readability for nonspecialists:** Good. The manuscript is clearly written, with logical flow and accessible explanations of key concepts. However, some simulation details may be challenging for non-experts.
- **Recommendation posture** Supportive if technical concerns are resolved. The core findings are potentially important, but the quantitative rigor of the EMSA analysis, the parameterization of the simulation, and the physiological relevance of the condensate assays need to be strengthened.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that FUS and NONO bind preferentially to shell-associated NEAT1 domains (E1, E2) compared to core-associated middle domains (C1, C2, C3), based on apparent Kd values from EMSA experiments.
- **Evidence pointer** Results section "Paraspeckle core proteins exhibit unexpected binding preferences to NEAT1", Figure 2B, S2B–E
- **Concern** The apparent Kd values are derived from EMSA band intensity quantification. The manuscript does not provide sufficient detail on how the fraction of bound RNA was calculated, whether binding reached equilibrium, and how the Hill equation was fitted. The reported Kd values have large uncertainties (e.g., FUS binding to C2: 771 ± 363 nM), and it is unclear if the differences between fragments are statistically significant given the error ranges. Additionally, the use of full-length proteins with MBP tags may affect binding affinity, and the authors state that MBP does not substantially impact FUS-RNA affinity based on previous work, but this is not verified for NONO, SFPQ, or TDP-43.
- **Why it matters** The central claim of differential binding preferences rests on the quantitative reliability of these Kd measurements. If the differences are not robust, the entire model is weakened.
- **Resolution test** Provide a more detailed description of the EMSA quantification, including how B(C) was computed, the number of replicates, and statistical tests comparing Kd values between fragments. Include a control demonstrating that MBP tags do not affect binding for all proteins tested. Show representative gels with all concentrations tested.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that their updated coarse-grained simulation model, parameterized based on experimental observations, recapitulates layered core-shell organization with TDP-43 in the shell.
- **Evidence pointer** Results section "An updated model relates multicomponent biomolecular interactions to paraspeckle assembly", Figure 5, S9, Table S1
- **Concern** The simulation model is parameterized with interaction strengths (ϵij) that are chosen to reflect experimental observations, but the manuscript does not provide a systematic sensitivity analysis. It is unclear how robust the observed layered organization is to variations in these parameters. Additionally, the model treats NEAT1 as a simple triblock copolymer with equal-sized domains, which may not capture the complexity of the actual RNA structure. The simulation results are qualitative, and it is not clear if the model makes quantitative predictions that can be tested experimentally.
- **Why it matters** The simulation is used to support the proposed mechanism. If the results are highly sensitive to parameter choices or if the model is too simplistic, the conclusions may not be generalizable.
- **Resolution test** Provide a sensitivity analysis showing how the observed organization changes with variations in key interaction parameters. Discuss the limitations of the triblock copolymer representation and justify the choice of equal-sized domains. If possible, make quantitative predictions (e.g., dependence of layer thickness on protein concentration) that could be experimentally tested.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that TDP-43 forms surfactant-like shells around FUS/NONO condensates, mirroring paraspeckle organization.
- **Evidence pointer** Results section "The shell protein TDP-43 opposes FUS and NONO condensation by competing for RNA binding", Figure 4B–D, S6E–H
- **Concern** The in vitro condensate assays are performed at protein concentrations (2 μM FUS, etc.) that may not reflect physiological conditions. The manuscript does not report the concentration of TDP-43 used in the co-assembly experiments, nor does it systematically vary the TDP-43:core protein ratio to demonstrate a concentration-dependent effect. The observation of "surfactant-like" layers is qualitative, and it is not clear how the layer thickness or continuity is quantified. Additionally, the use of only one RNA fragment (E3) for TDP-43 competition experiments may not fully represent the complexity of the full-length NEAT1.
- **Why it matters** The proposed mechanism of competitive binding and immiscibility relies on the observation of TDP-43 shell formation. If this is only observed under a narrow set of conditions, the physiological relevance is questionable.
- **Resolution test** Report the concentrations of all components in the co-assembly experiments. Perform a titration of TDP-43 concentration and show that shell formation is concentration-dependent. Quantify the layer thickness and continuity, and compare with predictions from the simulation model. Test competition with additional RNA fragments, including full-length NEAT1 if possible.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that NONO reduces FUS mobility in condensates, as evidenced by a more than three-fold increase in FRAP recovery time constant.
- **Evidence pointer** Results section "A multicomponent stoichiometry modulates condensation", Figure 3F, S5G–H
- **Concern** The FRAP experiments are performed on condensates formed with FUS and RNA, with and without NONO. The manuscript does not report the mobile fraction for FUS in the absence of NONO, nor does it discuss potential artifacts due to condensate size or geometry. The recovery time constant is a single parameter that may not fully capture the complex dynamics of proteins in condensates. Additionally, the authors do not compare the FRAP behavior of FUS in the presence of NONO to that of other core proteins.
- **Why it matters** The claim that NONO forms a "relatively stable network" is based on this FRAP data. If the interpretation is flawed, the proposed role of NONO in modulating condensate properties is weakened.
- **Resolution test** Report the full FRAP recovery curves and the mobile fraction for all conditions. Discuss potential artifacts and how they were addressed. Consider performing FRAP on condensates of different sizes to ensure the effect is not size-dependent.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1D
- **Evidence pointer** Results section "Probing the current model of paraspeckle assembly"
- **Issue** The description of the five NEAT1 fragments (E1, E2, C1, C2, C3) is clear, but the figure legend for Figure 1D is not provided in the text. It would be helpful to include a schematic showing the positions of these fragments along the full-length NEAT1 RNA.
- **Required correction** Add a schematic in Figure 1D or its legend showing the genomic positions of the five fragments relative to the full-length NEAT1.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section "Coarse-grained molecular dynamics simulations"
- **Evidence pointer** Methods section, "Coarse-grained molecular dynamics simulations"
- **Issue** The description of the simulation model is brief. It would be helpful to provide more detail on the Lennard-Jones potential parameters, the criteria for determining clusters, and the specific values used for the interaction matrix (Table S1 is referenced but not shown).
- **Required correction** Expand the methods to include the full interaction matrix and a more detailed description of the simulation protocol.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion of motif analysis
- **Evidence pointer** Results section "Paraspeckle core proteins exhibit unexpected binding preferences to NEAT1", Figure 2A
- **Issue** The motif analysis is based on position weight matrices from published datasets. The authors note that motif density does not always correlate with binding affinity, which is acknowledged. However, it would be useful to discuss the limitations of this approach more explicitly, particularly the potential for false positives and the lack of consideration of RNA structure.
- **Required correction** Add a sentence in the discussion acknowledging the limitations of PWM-based motif analysis and the potential role of RNA secondary structure in binding specificity.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section "Statistics and reproducibility"
- **Evidence pointer** Methods section "Statistics and reproducibility"
- **Issue** The manuscript states that sample sizes were not predetermined and that no data were excluded. It would be helpful to report the number of independent replicates for each experiment and the statistical tests used to assess significance.
- **Required correction** Add a summary of the number of replicates for each experiment and the statistical tests used in the figure legends or methods.

## Risk / unsupported claims
- The claim that "TDP-43 competes less effectively with core proteins for the middle region" is inferred from indirect evidence (TDP-43 binding to E3 and competition assays with E1 and C2). Direct competition assays with the middle region fragments (C1, C2, C3) are not shown.
- The claim that "transcriptional bursts are required to form paraspeckle-like clusters" is based on a simplified simulation model and is not directly tested experimentally.
- The physiological relevance of the in vitro condensate conditions (e.g., protein concentrations, RNA fragment lengths) is not fully established.
- The quantitative relationship between motif density and binding affinity is correlative and may not be causal, as acknowledged by the authors.
- The simulation model's ability to predict quantitative aspects of paraspeckle organization (e.g., layer thickness, protein partitioning) is not demonstrated.