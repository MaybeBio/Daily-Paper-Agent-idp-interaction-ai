## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion) without supplementary information or figures
- **Assessment boundary** Scientific claims, methodological approach, and interpretation as presented in the main text; figures and tables referenced but not directly examined
- **Shared manuscript claim summary** The authors propose that the N-terminal tail (residues 218–223) of CITED2 is essential for the unidirectional displacement of HIF-1α from p300/CBP TAZ1 through negative cooperativity, and introduce a β3-amino acid backbone perturbation strategy to probe the interplay between CITED2 binding motifs without significantly altering binding thermodynamics
- **Visible evidence base** Fluorescence anisotropy competition assays, ITC binding and competition titrations with global fitting, NMR chemical shift perturbation analyses, CD spectroscopy, computational alanine scanning (BAlaS)
- **Missing materials affecting confidence** Supplementary figures and tables (Fig. S1–S20, Tables S1–S2), full NMR assignment details, experimental methods section, raw data and fitting parameters, structural coordinates

## Reviewer
- **Overall assessment** This manuscript addresses a mechanistically important question in the regulation of the hypoxic response, namely how CITED2 achieves virtually irreversible displacement of HIF-1α from p300/CBP. The authors present a clear hypothesis, a well-designed perturbation strategy, and data that collectively support a role for the N-terminal tail in mediating negative cooperativity. The β3-amino acid substitution approach is creative and potentially broadly applicable to studying IDP-mediated interactions. However, the strength of the conclusions depends critically on the quality of the global fitting analysis and the interpretation of NMR chemical shift perturbations, neither of which can be fully evaluated from the main text alone. The claim that the N-terminal tail acts as a "conformational lock" is plausible but requires stronger direct evidence linking the observed structural changes to the functional outcome.
- **Who would be interested in the results, and why** Researchers studying hypoxia signaling, IDP-mediated protein-protein interactions, allosteric regulation, and peptidomimetic design. The methodological approach may also interest investigators developing inhibitors of p300/CBP–HIF-1α for therapeutic applications in cancer and ischemic diseases.
- **Major strengths** The study addresses a well-defined mechanistic question with a combination of biophysical methods. The perturbation strategy is thoughtfully designed to separate binding affinity effects from allosteric contributions. The use of multiple CITED2 variants with controlled modifications allows systematic probing of motif contributions. The NMR data provide structural context for the functional observations.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (global fitting validation), R1-M2 (NMR interpretation), R1-M3 (causality inference)
- **Assessment against Nature-style criteria** 
  - **Originality** The β3-amino acid perturbation strategy is novel in this context, though the underlying concept of probing allostery through targeted modifications is not entirely new. The specific finding regarding the N-terminal tail's role adds to but does not fundamentally transform the existing model.
  - **Scientific importance** The hypoxic response is a central physiological pathway with clear disease relevance. Understanding the molecular basis of CITED2-mediated displacement could inform therapeutic strategies. However, the advance is incremental rather than paradigm-shifting.
  - **Interdisciplinary readership** The work bridges structural biology, biophysics, and peptide chemistry, and would appeal to a reasonably broad audience within these fields. The clinical relevance of hypoxia signaling extends the potential readership.
  - **Technical soundness** The experimental design is generally sound, but the reliance on global fitting and the interpretation of modest chemical shift changes require careful validation. The manuscript would benefit from more transparent presentation of the fitting procedures and uncertainty estimates.
  - **Readability for nonspecialists** The manuscript is clearly written and the logic is easy to follow. Technical terms are used appropriately, though some familiarity with IDP biology and biophysical methods is assumed. The figures are well-referenced in the text.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding the global fitting analysis and the causal link between structural perturbations and functional outcomes.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that global fitting of ITC data to a ternary complex model allows extraction of cooperative parameters (Δg, Δh) that distinguish between CITED2 variants with different competition efficiencies.
- **Evidence pointer** Results section, Fig. 2, Fig. 5, Table 1, Fig. S20 (referenced)
- **Concern** The global fitting approach is central to the conclusions, but the manuscript does not provide sufficient detail on the model, the fitting procedure, or the uncertainty in the extracted parameters. The Δg values for CITED2218–256 (1.2 kcal mol−1) and the variants (2.6 kcal mol−1 for compound 1) are small relative to the reported Δh values (26 kcal mol−1), and the manuscript does not discuss how robust these estimates are to model assumptions or experimental noise. The statement that CITED2ΔN has Δg > 4 kcal mol−1 with Δh = 0 suggests a fundamentally different binding mode, but the basis for this constraint is not explained.
- **Why it matters** The distinction between variants that retain negative cooperativity and those that do not is the central functional readout. If the fitting is not robust, the conclusions about which motifs are essential for allostery could be incorrect.
- **Resolution test** Provide the full fitting model, parameter uncertainties (e.g., confidence intervals from bootstrap or Monte Carlo analysis), and a demonstration that the model can distinguish between alternative mechanisms (e.g., competitive vs. allosteric). Show that the extracted parameters are stable across reasonable variations in the model assumptions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that NMR chemical shift perturbations show that the N-terminal tail of CITED2 induces conformational changes at the α1/α4 interface of p300, and that these changes are linked to the unidirectional displacement of HIF-1α.
- **Evidence pointer** Results section, Fig. 3, Fig. 6, Fig. S4–S6, S12–S19 (referenced)
- **Concern** The NMR data are used to infer structural changes, but the manuscript does not report the magnitude of the chemical shift perturbations in a quantitative way (e.g., weighted average shifts with error estimates), nor does it discuss whether the observed changes are consistent with a specific conformational rearrangement. The claim that changes at the α1/α4 interface "lock" the conformation is an interpretation that goes beyond what can be concluded from chemical shift perturbations alone. The authors also do not address whether the observed shifts could arise from direct binding effects of the modified peptides rather than allosteric changes.
- **Why it matters** The structural interpretation is key to the proposed mechanism. Without quantitative analysis and appropriate controls, the link between the observed chemical shift changes and the functional outcome remains correlative.
- **Resolution test** Provide quantitative chemical shift perturbation data with error bars, map the affected residues onto the p300 structure, and discuss whether the observed changes are consistent with a specific conformational change. Include control experiments with peptides that bind but do not induce allostery to demonstrate that the shifts are specific to the allosteric mechanism.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The authors conclude that the N-terminal tail of CITED2 is essential for negative cooperativity and that the loop region is critical for coordinating the binding motifs, based on the observed loss of competition efficiency in modified variants.
- **Evidence pointer** Results section, Fig. 2, Fig. 5, Table 1
- **Concern** The causal relationship between the structural perturbations and the functional outcome is inferred from correlation. The authors show that certain modifications reduce competition efficiency, but they do not directly demonstrate that this is due to loss of allostery rather than to other factors, such as altered binding kinetics or changes in the conformational ensemble of the free peptide. The statement that the N-terminal tail "locks" the conformation is a strong claim that requires direct evidence of a conformational change coupled to the functional outcome.
- **Why it matters** The proposed mechanism has implications for understanding how IDPs achieve specificity and efficiency in competitive binding. If the causal link is not established, the conclusions may be overinterpreted.
- **Resolution test** Perform experiments that directly probe the allosteric mechanism, such as measuring the kinetics of HIF-1α displacement, using FRET or other conformational sensors to monitor p300 structural changes in real time, or testing variants with mutations that specifically disrupt the proposed conformational lock without affecting binding affinity.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that the N-terminal tail and the rest of the binding motifs are "crucial" for the unidirectional displacement, but the specific contribution of each motif is not clearly summarized.
- **Required correction** Briefly state the distinct roles of the N-terminal tail, αA helix, loop, and C-terminus in the competition mechanism.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence pointer** Results section, Fig. 2, Fig. 5
- **Issue** The manuscript does not specify the number of replicates for the ITC and fluorescence anisotropy experiments, nor the error bars on the reported values.
- **Required correction** Include the number of independent experiments and the standard deviation or standard error for all reported binding and competition parameters.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion
- **Issue** The discussion mentions that the N-terminal tail is "more sensitive to backbone modifications" but does not quantify this sensitivity or compare it to the effects of modifications in other motifs.
- **Required correction** Provide a quantitative comparison of the effects of modifications in different motifs on binding affinity and competition efficiency.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results
- **Evidence pointer** Results section, Fig. 6
- **Issue** The NMR data are presented as chemical shift perturbations, but the authors do not report which specific residues are affected or whether the changes are localized to the expected binding interface.
- **Required correction** Include a table or figure listing the affected residues and their locations in the p300 structure.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Introduction
- **Evidence pointer** Introduction
- **Issue** The introduction states that "several experimental and molecular modelling studies" have investigated the competition mechanism, but does not clearly distinguish what is known from what remains unresolved.
- **Required correction** Briefly summarize the key findings and limitations of previous studies to better frame the novelty of the current work.

## Risk / unsupported claims
- The claim that the N-terminal tail acts as a "conformational lock" is not directly supported by the data presented; it is an interpretation that requires additional evidence.
- The statement that the β3-amino acid substitutions "maintain the native-like properties" of CITED2 is based on CD and ITC data, but the manuscript does not provide a comprehensive characterization of the modified peptides (e.g., secondary structure content, aggregation state, or conformational dynamics).
- The conclusion that the loop region is "critical for connecting the recognition elements" is inferred from the loss of competition efficiency in loop-modified variants, but the mechanism by which the loop coordinates the other motifs is not directly demonstrated.
- The generalizability of the β3-amino acid perturbation strategy to other IDP-mediated interactions is proposed but not tested; this remains a speculative claim.