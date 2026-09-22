## Review setup
- **Input scope** Full manuscript text, including summary, introduction, results, discussion, and methods sections.
- **Assessment boundary** Scientific validity, technical soundness, and support of claims based solely on the provided manuscript content. No external data or literature verification performed.
- **Shared manuscript claim summary** The authors report that the E6AP AZUL domain interacts with the UBA domains of UBQLN1/2, that this interaction occurs in cells and in vitro, that it recruits E6AP to UBQLN2 condensates, and that an integrated AlphaFold-NMR structure reveals the binding interface and suggests allosteric effects on a newly identified UBAA oligomerization domain.
- **Visible evidence base** Immunoprecipitation experiments in HCT116 and ΔRAZUL cells; NMR titration, NOESY, relaxation, and saturation transfer experiments; CD spectroscopy; SEC-MALS; AlphaFold2 and AlphaFold2-Multimer predictions; Kd fitting from NMR chemical shift perturbations.
- **Missing materials affecting confidence** No supplementary figures or tables were provided. No validation statistics for the final structural ensemble (e.g., RMSD, restraint violations, Ramachandran statistics) were included. No raw NMR spectra or assignments were shown. No negative controls for the condensate recruitment assay were described. No quantification of immunoprecipitation replicates was provided.

## Reviewer
- **Overall assessment** This manuscript presents a potentially interesting interaction between E6AP and UBQLN1/2, with a plausible structural model. The combination of cellular, biophysical, and computational approaches is commendable. However, the evidence for the central claims is uneven. The cellular interaction data are convincing but lack quantification. The NMR data support a weak interaction, but the structural model relies heavily on AlphaFold predictions with limited experimental restraints. The identification and functional significance of the UBAA domain are intriguing but underdeveloped. The manuscript would benefit from stronger validation of the structural model and more direct evidence for the functional consequences of the interaction.
- **Who would be interested in the results, and why** Researchers studying ubiquitin-proteasome system biology, particularly E3 ligase regulation and proteasomal shuttle factors. The work may also interest those studying biomolecular condensates and their role in protein quality control, as well as structural biologists using integrative approaches combining prediction and experiment.
- **Major strengths** The study addresses a relevant question in proteasome biology. The use of multiple orthogonal techniques (cellular, biophysical, computational) strengthens the overall conclusions. The identification of a potential new interaction surface on UBQLN1/2 is novel. The integration of AlphaFold with NMR restraints is a modern and potentially useful approach for weak interactions.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** The structural model lacks sufficient experimental validation. The Kd values are derived from a limited set of residues and may not be robust. The functional significance of the UBAA oligomerization and its allosteric coupling to AZUL binding is speculative. The condensate recruitment data lack quantitative analysis and appropriate controls.
- **Assessment against Nature-style criteria** 
  - **Originality** Moderate. The finding of a new E6AP interaction partner is novel, but the concept of shuttle factors interacting with E3 ligases is not entirely new. The UBAA domain identification is a new contribution.
  - **Scientific importance** Moderate. The work provides a potential new link between E6AP and the UBQLN family, which could have implications for understanding E6AP function in cells. However, the physiological relevance is not established.
  - **Interdisciplinary readership** Limited. The work is primarily of interest to structural biologists and ubiquitin-proteasome researchers. The broader cell biology community may find the condensate aspect interesting, but the functional implications are not developed enough to attract wide attention.
  - **Technical soundness** The NMR and biophysical experiments appear generally well-executed, but the structural model is not sufficiently validated. The cellular experiments lack quantification.
  - **Readability for nonspecialists** The manuscript is reasonably well-written but assumes significant background knowledge in NMR spectroscopy and ubiquitin biology. The significance of the findings for a general audience is not clearly articulated.
- **Recommendation posture** Supportive if technical concerns are resolved. The core finding of an interaction is plausible, but the structural model and functional implications require stronger support.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Structural model validation
- **Claim pointer** The authors claim to present "an AlphaFold-NMR integrated structure" of the AZUL:UBA complex and use this model to propose a binding mechanism.
- **Evidence pointer** Results section "An AlphaFold-NMR integrated structure elucidates AZUL:UBQLN1 binding mechanism"; Figure 6C and S7.
- **Concern** The structural model is based on very few experimental restraints. Only three intermolecular NOEs are described (to F559, N577, E581), and these are assigned to AZUL atoms based on chemical shift matching with the apo and RAZUL-bound states, which may have shifted upon binding. The manuscript does not report the number of restraints used, the ensemble statistics, or any validation metrics (e.g., RMSD, restraint violations). The final model is essentially an AlphaFold prediction with minor adjustments from three NOEs. This is insufficient to claim an "integrated structure" with confidence.
- **Why it matters** The structural model is a central claim of the paper and is used to rationalize the binding mechanism and allosteric effects. Without proper validation, the model may be incorrect, undermining the mechanistic conclusions.
- **Resolution test** Provide a full list of experimental restraints, ensemble statistics (RMSD, restraint violations, Ramachandran analysis), and a comparison between the final model and the AlphaFold prediction. Ideally, show that the model is converged and that the NOE restraints are unambiguous. If the structure is not well-defined, the claims should be softened to a "docking model" or "model of the complex" rather than an "integrated structure."

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Kd determination
- **Claim pointer** The authors report Kd values of ~460 μM for the UBA domain and ~1 mM for the UBAA domain.
- **Evidence pointer** Results section "E6AP AZUL interacts with UBQLN1"; Figure S5A.
- **Concern** The Kd values are derived from fitting chemical shift perturbations of only a few residues (those with ΔδH > 0.02 ppm) using a 1:1 binding model. For such weak interactions, the accuracy of the Kd is highly dependent on the protein concentration range used and the completeness of the binding isotherm. The manuscript does not report the concentration range of the titration, the number of data points, or the quality of the fit. A Kd of ~1 mM for the UBAA domain is particularly concerning, as this is at the limit of what is reliably measurable by NMR and may be influenced by non-specific effects.
- **Why it matters** The Kd values are used to support the claim of a weak but specific interaction and to compare the affinities of the UBA and UBAA domains. If the Kd values are inaccurate, the interpretation of the binding data and the relative importance of the two domains may be wrong.
- **Resolution test** Provide the full titration curves, the concentration ranges used, and the fitting statistics (e.g., chi-squared, 95% confidence intervals). If possible, use a global fit of multiple residues. Alternatively, use an orthogonal method (e.g., ITC) to confirm the affinity.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Functional significance of UBAA
- **Claim pointer** The authors propose that the UBAA domain undergoes concentration-dependent oligomerization and that AZUL binding allosterically affects this self-association.
- **Evidence pointer** Results sections "UBAA undergoes concentration-dependent oligomerization" and "E6AP AZUL interacts with UBQLN1"; Figures 3D-F, 4A-F.
- **Concern** The evidence for UBAA oligomerization is indirect. The concentration-dependent chemical shift changes and R2 increases are consistent with self-association, but alternative explanations (e.g., non-specific aggregation, changes in local environment) are not excluded. The SEC-MALS data show a single peak with a mass consistent with a monomer, which argues against stable oligomer formation. The claim of allosteric coupling between AZUL binding and UBAA self-association is based on changes in R2 and Rex in the presence of AZUL, but the interpretation is complex and not fully supported. The functional relevance of this proposed oligomerization is not demonstrated.
- **Why it matters** The UBAA domain and its proposed oligomerization are presented as a novel finding with potential regulatory implications. If the oligomerization is not real or not functionally relevant, this aspect of the paper is overstated.
- **Resolution test** Provide more direct evidence for oligomerization, such as analytical ultracentrifugation or native mass spectrometry. For the allosteric effect, show that the changes in UBAA dynamics are specifically due to AZUL binding and not to the increased protein concentration or other factors. Ideally, demonstrate a functional consequence of the oligomerization or its modulation by AZUL in a cellular context.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Cellular interaction evidence
- **Claim pointer** The authors claim that "E6AP interacts with UBQLN1/2 in cellulo" based on co-immunoprecipitation experiments.
- **Evidence pointer** Results section "E6AP binds to UBQLN1 and UBQLN2 in cells"; Figure 1D-E.
- **Concern** The co-immunoprecipitation experiments are performed with a crosslinker (DSP), which can stabilize non-specific interactions. The experiments are done in cells overexpressing the proteins, which can lead to artifacts. The blots are not quantified, and no negative controls (e.g., with a non-specific antibody or with a mutant E6AP that cannot bind) are shown. The claim of a direct interaction in cells is therefore not strongly supported.
- **Why it matters** The cellular interaction is a key claim that bridges the in vitro and structural data. If the interaction is not robust in cells, the physiological relevance of the study is diminished.
- **Resolution test** Provide quantification of the co-immunoprecipitation from at least three independent experiments. Include a control with a binding-deficient mutant of E6AP or UBQLN. Consider performing the experiment without crosslinker or with a more specific crosslinker. If possible, use a proximity ligation assay or similar to confirm the interaction in cells.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 1D-E
- **Evidence pointer** Results section "E6AP binds to UBQLN1 and UBQLN2 in cells"
- **Issue** The immunoprecipitation blots are shown as single representative experiments. No quantification or statistical analysis is provided.
- **Required correction** Add quantification of the blots (e.g., band intensity normalized to input) from at least three independent experiments, with error bars and statistical tests.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 2F-G
- **Evidence pointer** Results section "E6AP AZUL is recruited to UBQLN2 condensates in vitro"
- **Issue** The condensate images are qualitative. No quantification of the fluorescence intensity inside versus outside condensates is provided.
- **Required correction** Quantify the enrichment of AZUL-mEGFP in condensates relative to the surrounding solution, with statistical analysis across multiple fields of view.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Methodology
- **Affected element** Kd fitting
- **Evidence pointer** Methods section "Kd fitting"
- **Issue** The Kd fitting uses only residues with ΔδH > 0.02 ppm. This threshold is arbitrary and may exclude residues with smaller but significant shifts.
- **Required correction** Justify the threshold or use a more inclusive approach, such as fitting all residues with observable shifts and reporting the global Kd.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion section
- **Evidence pointer** Discussion, paragraph 3
- **Issue** The authors speculate about the role of the E6AP-UBQLN interaction in condensates and disease without direct experimental support.
- **Required correction** Clearly distinguish between speculation and findings. Consider adding a "Limitations" paragraph to acknowledge what is not known.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 7C
- **Evidence pointer** Results section "An AlphaFold-NMR integrated structure elucidates AZUL:UBQLN1 binding mechanism"
- **Issue** The workflow diagram in Figure 7C is not described in the text. It is unclear what each step represents.
- **Required correction** Add a brief description of the workflow in the text or figure legend.

## Risk / unsupported claims
- The claim of an "AlphaFold-NMR integrated structure" is not fully supported due to the limited number of experimental restraints and lack of validation statistics.
- The Kd values for the UBA and UBAA interactions are based on limited data and may not be accurate.
- The functional significance of the UBAA oligomerization and its allosteric coupling to AZUL binding is speculative.
- The claim that E6AP interacts with UBQLN1/2 in cells is based on qualitative co-immunoprecipitation data without proper controls or quantification.
- The suggestion that the E6AP-UBQLN interaction may be relevant to disease is not supported by any direct evidence in this manuscript.