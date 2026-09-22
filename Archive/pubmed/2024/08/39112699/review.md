## Review setup
- **Input scope** Full manuscript text including abstract, main text, methods, figure legends, and supplementary information descriptions
- **Assessment boundary** Scientific content, experimental design, data interpretation, theoretical modeling, and claims as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors propose that tight-junction belt formation in epithelial cells is driven by a membrane prewetting transition of ZO-1 condensates at the apical cell interface, mediated by the polarity protein PATJ, and supported by a thermodynamic model predicting constant-velocity elongation.
- **Visible evidence base** Time-resolved APEX2 proximity proteomics, live-cell imaging of endogenous knock-in cell lines, CRISPR–Cas9 deletion of PATJ L27 domain, STED super-resolution microscopy, FRAP measurements, transepithelial resistance and permeability assays, partitioning assays in HEK293 cells, and numerical solutions to a thermodynamic model
- **Missing materials affecting confidence** Full proteomics dataset tables, extended data figures, supplementary notes, source data files, uncropped western blots, and complete statistical details for all comparisons

## Reviewer
- **Overall assessment** This manuscript presents a compelling and conceptually novel mechanism for tight-junction belt formation, linking biomolecular condensate physics to epithelial morphogenesis. The combination of quantitative live imaging, genetic perturbation, and thermodynamic modeling is ambitious and largely well-executed. The central claim that a prewetting transition, rather than simple binding or classical wetting, drives ZO-1 condensate elongation is well-supported by the constant-velocity observation and the theoretical framework. However, several technical concerns regarding the specificity of the PATJ effect, the quantitative rigor of the imaging analyses, and the directness of the evidence linking the model parameters to molecular mechanisms need to be addressed before the case is fully established.

- **Who would be interested in the results, and why** Cell biologists studying tight junctions and epithelial polarity, biophysicists working on phase separation and condensate wetting phenomena, and developmental biologists interested in morphogenetic mechanisms. The work bridges a gap between condensate physics and tissue-level structure formation, which will appeal to a broad interdisciplinary audience.

- **Major strengths** The study identifies a previously unrecognized physical mechanism, membrane prewetting, as a driver of tight-junction belt formation. The use of endogenously tagged proteins and CRISPR-mediated deletion strengthens the physiological relevance. The integration of quantitative imaging with a thermodynamic model provides a mechanistic framework that goes beyond descriptive observations. The constant-velocity elongation is a striking and testable prediction that is experimentally confirmed.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental support for causal role of PATJ
- **Claim pointer** The authors claim that PATJ mediates the transition of ZO-1 into a condensed surface layer that elongates around the apical interface, and that PATJ is required for elongation of ZO-1 condensates.
- **Evidence pointer** Figure 2d–f, Extended Data Figure 3, Extended Data Figure 6
- **Concern** The ∆L27-PATJ deletion is used to establish the causal role of PATJ in condensate elongation. However, the manuscript does not provide sufficient evidence that the observed phenotype is specifically due to loss of PATJ function at the apical interface rather than a general disruption of apical polarity or off-target effects. The authors show that other apical polarity proteins (PALS-1, LIN-7) are also lost from tight junctions in ∆L27-PATJ cells, which complicates the interpretation. Rescue experiments with the L27-PDZ1-PDZ6 construct restore function, but the manuscript does not demonstrate that this construct localizes correctly or that its expression levels are comparable to endogenous PATJ. Additionally, the ∆L27-PATJ phenotype shows condensates that nucleate but fail to elongate; the authors should rule out that this is due to reduced ZO-1 expression or stability in the mutant background.
- **Why it matters** The central mechanistic claim of the paper is that PATJ-mediated apical anchoring is the key determinant of prewetting-driven elongation. If the phenotype is due to broader polarity disruption or reduced ZO-1 levels, the specific role of PATJ as the apical connector would be weakened.
- **Resolution test** Provide quantitative analysis of ZO-1 expression levels in ∆L27-PATJ versus WT cells. Show that the L27-PDZ1-PDZ6 rescue construct localizes to the apical interface at levels comparable to endogenous PATJ. Include a control where PATJ is knocked down and rescued with a construct lacking the PDZ domains to demonstrate specificity. Alternatively, tether ZO-1 directly to the apical membrane in the ∆L27-PATJ background to show that apical anchoring alone is sufficient to restore elongation.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative rigor of imaging analyses
- **Claim pointer** The authors claim that condensates elongate with a constant velocity of 0.53 ± 0.14 µm/min in WT cells, and that this is significantly slowed to 0.02 ± 0.07 µm/min in ∆L27-PATJ cells.
- **Evidence pointer** Figure 4a–c, Extended Data Figure 5
- **Concern** The manuscript reports a single mean velocity value for WT and ∆L27-PATJ condensates, but the number of condensates analyzed, the number of cells, and the statistical method used to compare the two conditions are not clearly stated in the main text. The velocity is derived from linear fits to extension traces, but the quality of these fits (R² values, residuals) is not reported. The authors also note fusion and fission events that cause fluctuations in condensate length; it is unclear how these events were handled in the velocity analysis. If fusion/fission events were excluded, the criteria for exclusion should be stated. The claim of constant velocity is central to the prewetting model, so the robustness of this measurement needs to be demonstrated.
- **Why it matters** The constant-velocity prediction is a key differentiator between prewetting and other growth mechanisms. If the velocity is not truly constant, or if the measurement is not robust, the theoretical interpretation is undermined.
- **Resolution test** Provide a detailed description of the image analysis pipeline, including segmentation parameters, tracking algorithm, and criteria for including/excluding condensates. Report the number of condensates, cells, and biological replicates for each condition. Show representative individual extension traces with fits and residuals. Perform a statistical test for linearity of the extension traces (e.g., comparison of linear vs. quadratic fits). Report the distribution of velocities across condensates, not just the mean.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Model parameterization and validation
- **Claim pointer** The authors claim that a thermodynamic model of prewetting, with parameters including binding affinity ε and bulk chemical potential μ_bulk, quantitatively reproduces the observed elongation dynamics.
- **Evidence point** Figure 4g,h, Extended Data Figure 5, Supplementary Note 1
- **Concern** The model is presented as supporting the prewetting interpretation, but the manuscript does not clearly explain how the model parameters are constrained by experimental data. The relative binding affinity Δε̄ is varied to produce different behaviors (elongation vs. no elongation), but the relationship between this dimensionless parameter and the actual molecular interactions of ZO-1 with PATJ is not established. The model predicts a threshold binding affinity for elongation; the authors should demonstrate that the experimentally measured or estimated binding affinity of ZO-1 for the apical interface in WT cells is above this threshold, and that in ∆L27-PATJ cells it is below. Without this link, the model is illustrative rather than quantitatively validated.
- **Why it matters** The claim that the system operates in a prewetting regime depends on the model being a faithful representation of the physical system. If the parameters are not constrained by data, the model cannot distinguish between prewetting and other possible mechanisms.
- **Resolution test** Provide a sensitivity analysis showing how the model predictions depend on each parameter. Estimate the binding affinity of ZO-1 for the apical membrane from independent measurements (e.g., FRAP recovery rates, partitioning coefficients) and show that these estimates fall in the predicted regime. If possible, measure the bulk concentration of ZO-1 relative to the saturation concentration to directly test the prewetting assumption.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Proteomics data interpretation
- **Claim pointer** The authors claim that time-resolved proximity proteomics reveals the recruitment of apical proteins, particularly PATJ, to ZO-1 condensates during the elongation phase.
- **Evidence point** Figure 1b,d,e, Extended Data Figure 1, Supplementary Tables 1–3
- **Concern** The proteomics data are presented as a resource, but the manuscript does not provide sufficient detail on the statistical analysis of the proteomics data. The volcano plots show selected proteins, but the criteria for selecting these proteins (fold change threshold, FDR) are not clearly stated in the main text. The heat map in Figure 1d shows normalized log2 fold changes, but the normalization method and the number of replicates are not described. The manuscript mentions that proteins matching a false positive list were removed, but this list is not provided. The authors should clarify how many proteins were identified in total, how many passed the significance thresholds, and whether the key conclusions (e.g., PATJ recruitment timing) are robust to different analysis parameters.
- **Why it matters** The proteomics data provide the temporal framework for the study, identifying PATJ as a key player. If the analysis is not rigorous, the identification of PATJ as the apical connector may be premature.
- **Resolution test** Provide a detailed description of the proteomics data analysis, including the statistical model, thresholds, and number of replicates. Show the full list of significantly enriched proteins at each time point. Perform a sensitivity analysis with different fold change and FDR thresholds to show that PATJ is consistently identified.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of the prewetting mechanism
- **Claim pointer** The authors propose that membrane prewetting by condensates is a general mechanism for shaping cellular structures, and that their findings have implications for how cells exploit condensate properties to shape higher-order structures.
- **Evidence point** Discussion section
- **Concern** The discussion extrapolates from the specific case of ZO-1 and PATJ to a general principle of condensate-driven morphogenesis. While this is an interesting speculation, the manuscript does not provide evidence that the prewetting mechanism operates in other cellular contexts. The authors mention other examples of condensate-membrane interactions but do not demonstrate that these involve prewetting transitions. The claim that the mechanism is general should be tempered or supported by additional evidence.
- **Why it matters** The broader significance of the work depends on the generalizability of the mechanism. If the prewetting transition is specific to the ZO-1/PATJ system, the impact is more limited.
- **Resolution test** Either temper the claims in the discussion or provide additional evidence (e.g., in silico predictions, preliminary data) that similar prewetting transitions occur in other condensate-membrane systems.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure labels
- **Affected element** Figure 1a
- **Evidence point** Figure 1a
- **Issue** The time points for the morphological stages (0 h, 0.5 h, 1 h, 3 h, 18 h) are mentioned in the text but not clearly indicated on the figure itself.
- **Required correction** Add time labels to the representative images in Figure 1a or to the figure legend.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure 2e
- **Evidence point** Figure 2e
- **Issue** The statistical test used for the transepithelial resistance measurements is not stated in the figure legend.
- **Required correction** State the statistical test used and the number of replicates in the figure legend.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Model accessibility
- **Affected element** Supplementary Note 1
- **Evidence point** Supplementary Note 1
- **Issue** The thermodynamic model is described in a supplementary note, but the main text does not provide a clear summary of the key equations and assumptions for readers who do not delve into the supplement.
- **Required correction** Add a brief summary of the model's key assumptions and predictions in the main text, with a pointer to the full derivation in the supplement.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Control for APEX2 specificity
- **Affected element** Extended Data Figure 1
- **Evidence point** Extended Data Figure 1
- **Issue** The manuscript does not describe a control for APEX2 labeling specificity (e.g., no biotin phenol control, or a control without H2O2).
- **Required correction** Describe the negative controls used for APEX2 labeling in the methods or figure legend.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** FRAP analysis details
- **Affected element** Extended Data Figure 6
- **Evidence point** Extended Data Figure 6
- **Issue** The FRAP analysis is mentioned in the discussion but the details of the FRAP experiments (bleach region, analysis method, number of cells) are not described in the methods.
- **Required correction** Add a description of the FRAP experiments to the methods section.

- **Technical failings that need to be addressed before the case is established** R1-M1 (causal role of PATJ), R1-M2 (quantitative rigor of imaging), R1-M3 (model parameterization)

- **Assessment against Nature-style criteria** 
  - **Originality**: High. The application of prewetting theory to tight-junction formation is novel and conceptually creative.
  - **Scientific importance**: High. The work addresses a fundamental question in cell biology, how cells shape mesoscale structures, and provides a new physical mechanism.
  - **Interdisciplinary readership**: High. The work bridges cell biology, biophysics, and physical chemistry, appealing to a broad audience.
  - **Technical soundness**: Moderate. The experimental approaches are appropriate, but the quantitative rigor of the imaging analyses and the model validation need strengthening.
  - **Readability for nonspecialists**: Good. The manuscript is generally well-written and accessible, though the model description could be clearer for non-theorists.

- **Recommendation posture** Supportive if technical concerns are resolved. The central hypothesis is compelling and the experimental system is well-suited. However, the causal role of PATJ, the robustness of the constant-velocity measurement, and the quantitative link between model parameters and molecular interactions need to be established more rigorously.

## Risk / unsupported claims
- The claim that PATJ is "necessary and sufficient" for tight-junction belt formation is not fully supported, as the rescue experiments use a chimeric construct that may not fully recapitulate endogenous PATJ function.
- The claim that the prewetting mechanism is a general principle for condensate-driven morphogenesis is speculative and not directly tested.
- The quantitative values for condensate elongation velocity and the statistical comparison between WT and ∆L27-PATJ are not fully documented.
- The relationship between the model parameter Δε̄ and the actual molecular binding affinity of ZO-1 to the apical interface is not established.
- The claim that ZO-1 bulk concentration is below the saturation concentration for phase separation is stated but not directly measured in this system.