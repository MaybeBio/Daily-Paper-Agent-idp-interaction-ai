## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no full text, figures, or supplementary materials were provided
- **Shared manuscript claim summary** The authors propose that rotavirus NSP5 variants differ in intrinsic phase-separation propensity, that low-propensity strains require NSP5 phosphorylation to nucleate condensates, and that phosphorylation drives an allosteric switch in a high-propensity variant, establishing a context-dependent role for phosphorylation in viral replicative organelle formation
- **Visible evidence base** Machine learning predictions of phase-separation propensity; engineered variant with low-propensity signatures; in vitro phase-separation assays; recombinant virus experiments; hydrogen-deuterium exchange mass spectrometry (HDX-MS)
- **Missing materials affecting confidence** Full text, methods, figures, statistical details, sequence alignments, strain identifiers, and quantitative results are not available; the abstract alone does not permit independent verification of the experimental design or data quality

## Reviewer
- **Overall assessment** The abstract presents a compelling and potentially significant hypothesis that phosphorylation differentially regulates NSP5 condensate formation across rotavirus strains. The combination of computational prediction, in vitro assays, recombinant virus validation, and HDX-MS is ambitious and well aligned with the question. However, the abstract-level evidence is insufficient to establish the central claims, particularly the allosteric mechanism and the strain-dependent phosphorylation requirement. The work is of interest to virologists and biophysicists studying phase separation, but the current presentation does not allow a rigorous assessment of technical soundness or reproducibility.
- **Who would be interested in the results, and why** Virologists studying rotavirus replication and RNA virus organelle biogenesis; biophysicists and cell biologists investigating liquid-liquid phase separation in disease contexts; researchers using machine learning to predict IDP behavior; structural biologists employing HDX-MS to map conformational changes in disordered proteins
- **Major strengths** The study addresses a timely and important question about sequence diversity and phase-separation mechanisms in viral proteins. The use of a machine learning approach to stratify NSP5 variants is innovative and provides a rational basis for variant selection. The combination of in vitro and in vivo experiments, including recombinant viruses, strengthens the biological relevance. The HDX-MS approach to probe phosphorylation-driven conformational changes is technically sophisticated and could reveal novel regulatory mechanisms.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract does not provide quantitative data, statistical comparisons, or experimental controls. The allosteric switch claim is based on HDX-MS but no details on peptide-level resolution, phosphorylation site mapping, or reproducibility are given. The recombinant virus experiments are described only qualitatively, with no evidence that condensate formation was directly measured or that phosphorylation status was verified. The machine learning predictions are not benchmarked against experimental data in the abstract.
- **Assessment against Nature-style criteria** 
  - Originality: High. The concept of strain-dependent phosphorylation as a switch for phase separation is novel and not widely explored in viral systems.
  - Scientific importance: Potentially high, as it could redefine how phosphorylation is viewed in rotavirus replication and IDP biology, but the importance is contingent on the robustness of the evidence.
  - Interdisciplinary readership: Strong. The work bridges virology, biophysics, computational biology, and structural mass spectrometry, appealing to a broad audience.
  - Technical soundness: Not assessable from the abstract. The methods are named but not described, and no data are shown to evaluate rigor.
  - Readability for nonspecialists: The abstract is clear and well structured, but terms like "allosteric switch" and "HDX-MS" may require more context for a general audience.
- **Recommendation posture** Supportive if technical concerns are resolved. The hypothesis is interesting and the experimental strategy is appropriate, but the abstract alone does not establish the claims. A full manuscript with detailed methods, quantitative results, and statistical analysis would be needed to assess whether the case is convincing.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "Low-tendency LLPS strains require phosphorylation of NSP5 to nucleate phase separation, whereas high-tendency strains do not, suggesting distinct nucleation mechanisms."
- **Evidence pointer** Abstract; location not provided
- **Concern** The claim of a strain-dependent phosphorylation requirement is central, but the abstract provides no quantitative data, such as phosphorylation levels, phase-separation thresholds, or statistical comparisons between strains. It is unclear how "require" was defined experimentally and whether the absence of phosphorylation was directly tested in the low-tendency strains.
- **Why it matters** Without direct evidence that phosphorylation is necessary and sufficient for nucleation in low-tendency strains, and dispensable in high-tendency strains, the proposed dichotomy is not established. This is the core mechanistic claim of the study.
- **Resolution test** Provide quantitative phase-separation assays (e.g., turbidity, fluorescence recovery after photobleaching) with and without phosphorylation, for multiple strains, including statistical analysis. Show that phosphorylation is required for low-tendency variants and not for high-tendency variants, with appropriate controls.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic support
- **Claim pointer** "Hydrogen-deuterium exchange mass spectrometry revealed a phosphorylation-driven allosteric switch between binding sites on the high-propensity variant."
- **Evidence pointer** Abstract; location not provided
- **Concern** The allosteric switch is a strong mechanistic claim, but the abstract does not specify which phosphorylation sites were modified, how the switch was defined, or whether HDX-MS data were collected at peptide resolution with sufficient coverage. No comparison to a non-phosphorylated control or to low-propensity variants is described.
- **Why it matters** An allosteric switch implies a specific conformational change that alters binding site accessibility. Without detailed HDX-MS data, including differential deuterium uptake plots and statistical thresholds, the claim is not verifiable and could be an overinterpretation of limited data.
- **Resolution test** Present HDX-MS data with peptide-level resolution, identify the phosphorylation sites, and show differential deuterium uptake between phosphorylated and non-phosphorylated states. Include replicates and statistical significance. If possible, validate the switch with mutagenesis or binding assays.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Biological relevance
- **Claim pointer** "An engineered variant incorporating amino acid signatures from strains with low LLPS tendency, which failed to phase separate in vitro yet supported the formation of replicative condensates in recombinant viruses in cells."
- **Evidence pointer** Abstract; location not provided
- **Concern** The in vitro failure to phase separate is contrasted with in vivo condensate formation, but the abstract does not explain how this discrepancy was resolved. It is unclear whether the in vivo condensates were formed via phosphorylation, other cellular factors, or alternative mechanisms. The recombinant virus experiments are described without quantitative readouts.
- **Why it matters** The study's conclusion that phosphorylation is context-dependent relies on this discrepancy. If the engineered variant forms condensates in cells without phosphorylation, the in vitro result may be misleading. If phosphorylation is required, the mechanism should be demonstrated in vivo.
- **Resolution test** Show in vivo condensate formation with and without phosphorylation, using phospho-null or phospho-mimetic mutants. Quantify condensate size, number, and dynamics. Correlate in vitro and in vivo results to clarify the role of phosphorylation.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** "Machine learning approach"
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract does not specify the machine learning model, training data, or validation metrics. This makes it difficult to assess the reliability of the propensity predictions.
- **Required correction** Briefly describe the model type, training dataset, and performance metrics (e.g., AUC, accuracy) in the abstract or methods.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "Allosteric switch"
- **Evidence pointer** Abstract; location not provided
- **Issue** The term "allosteric switch" is used without defining the binding sites or the conformational change. This could confuse readers unfamiliar with the system.
- **Required correction** Define the binding sites and the nature of the switch (e.g., a change in binding partner or affinity) in the abstract.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Generalizability
- **Affected element** "Across diverse rotaviruses"
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract claims diversity but does not specify how many strains were analyzed or how representative they are of global rotavirus diversity.
- **Required correction** State the number of strains and their phylogenetic or serotype diversity to support the generalizability claim.

## Risk / unsupported claims
- The claim that "phosphorylation plays a context-dependent role" is not supported by the abstract alone, as no direct comparison of phosphorylation effects across multiple strains is shown.
- The "allosteric switch" is not defined or evidenced with specific HDX-MS data.
- The in vitro versus in vivo discrepancy for the engineered variant is not resolved, leaving the mechanism unclear.
- The machine learning predictions are not validated against experimental data in the abstract.
- The generalizability to "diverse rotaviruses" is asserted without specifying strain coverage or statistical power.