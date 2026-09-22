## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and figure legends
- **Assessment boundary** Scientific validity, technical soundness, and support of claims based solely on the provided manuscript content
- **Shared manuscript claim summary** The authors report that EGCG binds directly to p53 with micromolar affinity, primarily through the intrinsically disordered N-terminal domain, induces conformational changes including a compact subpopulation, and disrupts p53-MDM2 interaction leading to inhibition of MDM2-mediated ubiquitination in vitro
- **Visible evidence base** SPR binding data, STD NMR epitope mapping, 2D NMR titration, SAXS, AUC, atomistic MD simulations, competition SPR, fluorescence polarization anisotropy, in vitro ubiquitination assay
- **Missing materials affecting confidence** Supplementary figures and tables referenced but not provided; source data files not available; no cell-based or in vivo functional validation; no structural coordinates for MD simulations; no raw NMR assignment data

## Reviewer
- **Overall assessment** The manuscript presents a multi-technique investigation into EGCG-p53 interactions, combining biophysical binding assays with computational simulations. The work addresses an important question regarding the molecular mechanism of EGCG's anticancer activity. However, several technical concerns regarding data interpretation, experimental controls, and the quantitative rigor of binding measurements need to be addressed before the central claims can be fully established. The study is potentially interesting but requires additional validation and clarification.
- **Who would be interested in the results, and why** Researchers in cancer biology, particularly those studying p53 regulation and MDM2 inhibitors; investigators interested in drug discovery targeting intrinsically disordered proteins; natural product researchers examining the mechanisms of green tea polyphenols; structural biologists studying protein-ligand interactions involving IDPs
- **Major strengths** 1) Multi-technique approach combining SPR, NMR, SAXS, AUC, and MD simulations provides complementary perspectives on the interaction. 2) The identification of p53 NTD as a druggable target for small molecules challenges conventional views about IDPs being undruggable. 3) The extensive MD simulations (>100 μs aggregated sampling) represent a significant computational investment. 4) The study addresses a clinically relevant question about EGCG's mechanism of action.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5
- **Assessment against Nature-style criteria** Originality: The concept of targeting p53 NTD with a small molecule is novel, though EGCG-p53 interactions have been previously suggested. Scientific importance: Potentially high if the mechanism is rigorously established, as it could inform both cancer prevention strategies and IDP drug discovery. Interdisciplinary readership: The work bridges chemistry, biophysics, structural biology, and cancer biology, making it suitable for a broad audience. Technical soundness: Several technical concerns need resolution, particularly regarding binding stoichiometry, control experiments, and interpretation of conformational data. Readability for nonspecialists: The manuscript is generally well-written and accessible, though some technical sections could benefit from additional context.
- **Recommendation posture** Supportive if technical concerns are resolved

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Data interpretation
- **Claim pointer** The authors claim a direct, μM interaction between EGCG and p53 with KD = 1.6 ± 1.4 μM for full-length p53 and KD = 4 ± 2 μM for NTD
- **Evidence pointer** Figure 1a, 1b; Results section "SPR shows similar μM affinity"
- **Concern** The SPR experiments immobilize p53 or NTD on the sensor chip and flow EGCG over the surface. However, the manuscript does not report the stoichiometry of binding (n value) from the SPR fitting. For a small molecule binding to an IDP with potentially multiple binding sites, the assumption of 1:1 binding may not be valid. Additionally, the large error bars on the KD values (nearly 100% of the mean for full-length p53) suggest poor reproducibility or fitting quality. The manuscript also does not report whether mass transport limitations were considered, which is critical for small molecule-protein interactions where the analyte is much smaller than the ligand.
- **Why it matters** The KD values are central to the paper's claim of a "direct, μM interaction." If the stoichiometry is not 1:1, or if the fitting model is inappropriate, the reported affinities may be inaccurate. This would undermine the quantitative basis for subsequent experiments and the overall conclusion that EGCG binds p53 with physiologically relevant affinity.
- **Resolution test** The authors should report the stoichiometry (n) from their SPR fits, provide evidence for the appropriateness of the binding model used, include replicate experiments with error analysis, and discuss whether mass transport limitations were addressed. Alternatively, an orthogonal binding assay (e.g., ITC) should be performed to validate the KD values.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental controls
- **Claim pointer** The authors claim that EGCG disrupts p53-MDM2 interaction based on competition SPR and fluorescence anisotropy experiments
- **Evidence pointer** Figure 5; Results section "EGCG disrupts p53–MDM2 interaction"; Supplementary Figure 12
- **Concern** The competition SPR experiment pre-incubates EGCG with p53 and then flows the mixture over MDM2-immobilized chips. However, the manuscript does not report control experiments showing that EGCG alone does not bind to the MDM2-coated surface. If EGCG binds directly to MDM2, the reduced SPR signal could be due to competition for the MDM2 surface rather than EGCG-p53 binding. Similarly, the fluorescence anisotropy experiments use fluorescein-labeled MDM2, and it is unclear whether EGCG interferes with the fluorescence signal directly. The manuscript also does not report whether the DMSO vehicle control (if used) affects the interactions.
- **Why it matters** Without proper controls, the observed disruption of p53-MDM2 interaction cannot be unambiguously attributed to EGCG binding to p53. This is critical because the paper's mechanistic model depends on EGCG binding to the NTD and sterically blocking MDM2 association.
- **Resolution test** The authors should include control experiments showing EGCG does not bind to MDM2 alone (e.g., SPR with EGCG flowed over MDM2-immobilized surface without p53). They should also demonstrate that EGCG does not affect fluorescein fluorescence in the anisotropy assay, and include vehicle controls.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Data interpretation
- **Claim pointer** The authors claim that EGCG causes the emergence of a compact subpopulation of NTD conformations based on SAXS, AUC, and MD simulations
- **Evidence pointer** Figure 3; Figure 4; Results section "EGCG induces conformational heterogeneity"
- **Concern** The SAXS experiments use NTD 20-70 at 580 μM concentration, which is far above the reported KD of 4 μM. At this concentration, the binding should be saturated, yet the observed changes in the p(r) functions are modest. The manuscript does not report the fraction of bound versus unbound NTD under the SAXS conditions, nor does it provide a quantitative analysis of the SAXS data (e.g., ensemble optimization method or EOM analysis) to support the claim of a distinct compact subpopulation. The AUC data interpretation relies on Bayesian analysis with prior expectations that may bias the results. The MD simulations use a single EGCG molecule with one NTD at 2.3 mM effective concentration, which may not represent the experimental conditions.
- **Why it matters** The claim of a "compact subpopulation" is a key mechanistic finding that distinguishes this work from simple binding. If the SAXS and AUC data are not quantitatively analyzed to support this claim, the interpretation may be overreaching. The MD simulations, while extensive, may not capture the full ensemble of binding modes at physiologically relevant concentrations.
- **Resolution test** The authors should perform ensemble-based SAXS analysis (e.g., EOM) to quantitatively characterize the conformational distribution and its change upon EGCG binding. They should also report the fraction of bound NTD in the SAXS and AUC experiments and discuss how the high concentrations used affect the interpretation. For MD, they should demonstrate convergence of the observed compact states and relate the simulation conditions to experimental concentrations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative rigor
- **Claim pointer** The authors claim that EGCG inhibits MDM2-mediated ubiquitination of p53 with an IC50 of ~100 μM
- **Evidence pointer** Figure 6; Results section "EGCG disrupts p53–MDM2 interaction and inhibits MDM2-mediated p53 ubiquitination in vitro"
- **Concern** The IC50 of ~100 μM for the ubiquitination assay is two orders of magnitude higher than the KD for EGCG-p53 binding (1.6 μM). This large discrepancy is not discussed. If EGCG binds p53 with micromolar affinity and disrupts p53-MDM2 interaction with an IC50 of 0.2 μM in the competition SPR, why is the ubiquitination inhibition IC50 so much higher? Possible explanations include assay conditions, competing interactions, or that the ubiquitination inhibition is not directly related to the binding affinity. The manuscript does not address this inconsistency.
- **Why it matters** The ubiquitination data is presented as functional validation of the mechanism. If the IC50 does not correlate with the binding affinity, the physiological relevance of the observed binding may be questioned. The discrepancy also raises questions about whether the ubiquitination inhibition is truly due to direct competition for the MDM2 binding site or could involve other mechanisms.
- **Resolution test** The authors should discuss the relationship between the binding affinity and the ubiquitination IC50, considering factors such as assay conditions, enzyme concentrations, and the multi-step nature of ubiquitination. They should also perform ubiquitination assays at lower EGCG concentrations to determine whether inhibition occurs at concentrations closer to the KD.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Data interpretation
- **Claim pointer** The authors claim that NMR CSPs suggest a coil-to-helical conformational transition upon EGCG binding
- **Evidence pointer** Figure 2; Results section "Mapping EGCG-binding site on p53 NTD by 2D NMR titration"
- **Concern** The manuscript reports CSPs in 15N-13C NCO spectra but does not provide sequential assignment information or show which specific residues are affected beyond the two regions highlighted. The claim of "coil to helical transition" is based on the sign and magnitude of ∆δC' and ∆δN, but this interpretation requires careful validation. The manuscript does not show whether the CSPs are in fast, intermediate, or slow exchange on the NMR timescale, which would affect the interpretation. Additionally, the NCO experiment probes backbone carbonyl and amide nitrogen correlations, but the interpretation of secondary structure changes from these CSPs alone is not straightforward without additional data (e.g., CA or CB chemical shifts).
- **Why it matters** The secondary structure change is presented as a mechanistic consequence of EGCG binding. If the interpretation is not well-supported, the structural model of how EGCG disrupts p53-MDM2 interaction may be incorrect. The overlap with regions of high α-helical propensity in apo NTD is suggestive but not conclusive.
- **Resolution test** The authors should provide more detailed NMR analysis, including the magnitude of CSPs for individual residues, the exchange regime, and ideally additional experiments (e.g., 13Cα/13Cβ chemical shift analysis) to support the secondary structure interpretation. They should also discuss alternative explanations for the observed CSPs, such as direct binding effects versus conformational changes.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states "KD = 1.6 ± 1.4 μM" for full-length p53, but the error is nearly as large as the value itself. This suggests either high variability or poor fitting. The abstract should present the data more cautiously or provide additional context.
- **Required correction** Consider reporting the KD with a confidence interval or noting the variability in the measurement. Alternatively, present the KD as a range or with a qualifier such as "approximately 1-3 μM."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods
- **Evidence pointer** Methods section "MD simulation"
- **Issue** The MD simulation methods do not specify the force field parameters for EGCG. The authors state that EGCG was modeled with the general AMBER force field (GAFF), but do not provide details on charge derivation (e.g., RESP fitting, AM1-BCC) or how the ligand parameters were validated.
- **Required correction** Add details on EGCG parameterization, including the charge model used and any validation of the ligand force field parameters.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 1
- **Evidence pointer** Figure 1a, 1b
- **Issue** The SPR sensorgrams show binding curves but the figure legend does not specify whether the data were background-subtracted or whether reference channel subtraction was performed. This is important for assessing data quality.
- **Required correction** Add information about data processing, including reference subtraction and any blank injections used.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion states that "EGCG may thus shield the MDM2-binding site of p53-NTD to inhibit p53 degradation." However, the data only show in vitro disruption of binding and ubiquitination. The authors should be more cautious about extrapolating to cellular contexts without additional evidence.
- **Required correction** Soften the language to indicate that the data suggest a potential mechanism that requires cellular validation.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results
- **Evidence pointer** Results section "EGCG induces conformational heterogeneity"
- **Issue** The manuscript mentions PCA analysis of MD trajectories but does not provide sufficient detail on how the PCA was performed, how many principal components were retained, or how the representative structures were selected.
- **Required correction** Add methodological details for the PCA analysis, including the featurization approach, number of components, and criteria for selecting representative structures.

## Risk / unsupported claims
- The claim that EGCG binding causes a "coil to helical transition" is not fully supported by the NMR data presented, as the interpretation relies on CSP patterns without additional secondary structure probes
- The physiological relevance of the EGCG-p53 interaction is implied but not directly demonstrated, as no cellular or in vivo experiments are presented
- The statement that "EGCG may thus shield the MDM2-binding site" is speculative and not directly tested
- The relationship between the reported KD (1.6 μM) and the ubiquitination IC50 (~100 μM) is not explained, leaving a significant quantitative discrepancy unaddressed
- The claim that the NTD is "the major binding site" is based on similar KD values for full-length p53 and NTD, but the manuscript does not exclude contributions from other p53 domains
- The MD simulation results are presented as supporting evidence for conformational changes, but the relationship between simulation conditions (2.3 mM effective concentration) and experimental conditions is not discussed