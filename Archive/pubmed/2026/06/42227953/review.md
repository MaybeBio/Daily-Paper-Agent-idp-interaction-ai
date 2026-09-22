## Review setup
- **Input scope** Full manuscript text including abstract, results, discussion, methods, and supplementary figure/table references
- **Assessment boundary** Scientific claims, methodological soundness, data interpretation, and consistency with the provided evidence
- **Shared manuscript claim summary** The authors propose that intramolecular interactions between folded domains (UBL, UBA, STI1) and intrinsically disordered regions (IDRs) in ubiquilins (UBQLNs) modulate the open/closed conformational topology, and that these interactions are conserved across the UBQLN family, with functional implications for substrate binding and protein quality control.
- **Visible evidence base** NMR spectroscopy (chemical shift perturbations, peak intensity ratios, relaxation rates), SAXS with SEC-MALS, coarse-grained CALVADOS3 simulations, sequence alignments, and SLiM database analysis
- **Missing materials affecting confidence** Raw NMR spectra, SAXS curves (beyond summarized values), per-residue CSP data, simulation convergence metrics, full sequence alignment data, and statistical details for some comparisons are not fully provided in the text

## Reviewer

- **Overall assessment** This manuscript presents a comprehensive and well-integrated study combining experimental and computational approaches to dissect intramolecular interactions in ubiquilins. The central finding that STI1:IDR interactions are reciprocally coupled to UBL:UBA interactions and modulate conformational topology is novel and mechanistically insightful. The conservation analysis across diverse UBQLN homologs strengthens the generalizability of the proposed model. However, several technical aspects require clarification and additional validation to fully support the conclusions, particularly regarding the interpretation of the two-state fitting, the quantitative basis for the "STI1-interaction score," and the functional significance of the observed topology shifts.

- **Who would be interested in the results, and why** Researchers in the fields of protein biophysics, intrinsically disordered proteins, protein quality control, and ubiquitin signaling would find this work highly relevant. The study provides a framework for understanding how IDR-folded domain interactions shape multidomain protein function, which has broad implications for the many proteins containing both folded and disordered regions. The conservation analysis also makes it relevant to evolutionary biologists studying protein family diversification.

- **Major strengths** The study combines multiple orthogonal techniques (NMR, SAXS, simulations) to provide a robust characterization of conformational ensembles. The reciprocal coupling between UBL:UBA and STI1:IDR interactions is a conceptually important finding. The extension to multiple UBQLN homologs with a focus on physicochemical determinants rather than sequence identity is a sophisticated approach. The authors are transparent about limitations, including the coarse-grained nature of simulations and the two-state model assumption.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of two-state fitting
- **Claim pointer** The authors claim that fitting the experimental SAXS data as a linear combination of open and closed simulated profiles yields accurate open/closed population fractions (e.g., 6% open for Dsk2 FL, 24% for I45A).
- **Evidence pointer** Results section "Dsk2 Binding is Regulated by Protein Topology", Figures 2A-B, 4C-D, Methods "Simulated SAXS Scattering Curve"
- **Concern** The two-state fitting assumes that the experimental ensemble is a linear combination of only two predefined states (open and closed). However, the authors acknowledge in the Discussion that there is no evidence for a two-state equilibrium. The fitting could be biased by the choice of end states, and intermediate or alternative conformations are not considered. The reported uncertainties in ω are based on only three reconstructed ensembles, which may underestimate the true variability. Additionally, the open and closed simulated profiles are generated from coarse-grained simulations that may not fully capture the conformational diversity of the real system. The authors should provide a more rigorous validation of the two-state assumption, such as comparing the fit quality against a single-state model or a model with more than two states, and should report goodness-of-fit metrics (e.g., chi-squared values) for the fits.
- **Why it matters** The quantitative open/closed fractions are central to the manuscript's conclusions about topology regulation. If the two-state fitting is not robust, the reported population shifts (e.g., I45A vs FL) may not be reliable, undermining the functional interpretations.
- **Resolution test** Provide chi-squared or reduced chi-squared values for the fits, compare the two-state fit against a one-state (open-only or closed-only) fit, and test whether adding a third state (e.g., an intermediate) significantly improves the fit. Report uncertainties in ω from a larger number of bootstrap or replicate fits.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative basis for STI1-interaction score
- **Claim pointer** The authors claim that the "STI1-interaction score" derived from NMR intensity ratios and simulated occupancy fold changes shows strong correlation and consistently reveals HS3 > HS2 > HS1 interaction strength.
- **Evidence pointer** Results section "Dsk2's STI1 Domain Intramolecularly Interacts with Hotspot Regions within IDRs", Figure 3C, Methods "STI1-Interaction Score"
- **Concern** The STI1-interaction score is calculated by normalizing two different metrics (NMR intensity ratios and simulated occupancy fold changes) and averaging across residues within each hotspot. The normalization procedure is not fully described, and it is unclear how the two metrics are weighted relative to each other. The correlation between the two metrics is stated but not quantified (no correlation coefficient or statistical test is provided). Furthermore, the NMR intensity ratios are measured upon STI1 deletion, which may have indirect effects on the UBL:UBA interaction, confounding the interpretation. The authors should provide a more detailed description of the scoring method, report the correlation coefficient with a statistical test, and discuss potential confounding factors.
- **Why it matters** The ranking of hotspot interaction strengths is used to support the model of differential STI1:IDR interactions and their conservation. Without a rigorous quantitative basis, the ranking may not be robust, and the conservation claims are weakened.
- **Resolution test** Provide a detailed step-by-step description of the scoring normalization, report the Pearson or Spearman correlation coefficient with a p-value, and perform a sensitivity analysis to show that the ranking is robust to the choice of normalization or weighting.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Functional significance of topology shifts
- **Claim pointer** The authors claim that the shift toward open topology in I45A enhances binding to ubiquitin (Kd = 10.3 ± 0.6 µM vs 17.0 ± 0.8 µM for FL), suggesting that topology regulates substrate accessibility.
- **Evidence pointer** Results section "Dsk2 Binding is Regulated by Protein Topology", Figures 2G-I
- **Concern** The observed difference in ubiquitin binding affinity is modest (1.6-fold) and the authors acknowledge this. However, the functional significance of this difference is not thoroughly discussed. The NMR titration experiments were performed at a single protein concentration (50 µM), and it is unclear whether the binding is in the slow or fast exchange regime on the NMR timescale, which could affect the accuracy of the Kd determination. Additionally, the authors do not test whether the enhanced ubiquitin binding in I45A translates to functional differences in a cellular context (e.g., in protein degradation assays). The claim that topology regulates substrate accessibility would be strengthened by additional functional data.
- **Why it matters** The manuscript proposes a regulatory mechanism where topology shifts modulate UBQLN function. Without direct functional evidence, the physiological relevance of the observed affinity changes remains speculative.
- **Resolution test** Perform ubiquitin binding assays at multiple protein concentrations to confirm the Kd difference, and ideally test the effect of topology modulation on ubiquilin function in a cellular or in vitro degradation assay.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Conservation analysis methodology
- **Claim pointer** The authors claim that STI1:IDR interactions are broadly conserved across UBQLN homologs despite sequence divergence, driven by physicochemical properties (hydrophobicity) rather than primary sequence.
- **Evidence pointer** Results section "Intramolecular STI1:IDR Interactions are Conserved Across the Ubiquilin Family", Figures 5D-E, S13-S16
- **Concern** The conservation analysis relies on simulations of homologs using AlphaFold structures, but the authors do not validate these simulations against experimental data for any homolog other than Dsk2. The identification of hotspots is based on a peak-detection algorithm with parameters tuned to recapitulate Dsk2 results, which could introduce bias. The statistical significance of the hydrophobicity difference between hotspot and non-hotspot regions is reported (Welch's p = 0.0041), but the effect size and the number of hotspots compared are not clearly stated. The authors should validate the simulations for at least one additional homolog experimentally (e.g., by NMR or mutagenesis) and provide more details on the hotspot identification and statistical comparisons.
- **Why it matters** The claim of conserved regulatory mechanisms across the UBQLN family is a key conclusion. If the simulations are not validated for other homologs, the conservation claim is not well supported.
- **Resolution test** Provide experimental validation (e.g., NMR or mutagenesis) for at least one non-yeast homolog, and report the number of hotspots, effect sizes, and multiple testing corrections for the hydrophobicity comparison.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure references
- **Affected element** Results section "Dsk2 Binding is Regulated by Protein Topology"
- **Evidence pointer** Figure 2
- **Issue** The text refers to Figure 2G-I for the NMR titration data, but the figure panels are not described in the text. It is unclear which panels show the titration curves, the Kd fits, and the per-residue Kd values.
- **Required correction** Add explicit descriptions of each figure panel in the text, or ensure the figure legend provides sufficient detail for the reader to interpret the data.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results section "Dsk2's STI1 Domain Intramolecularly Interacts with Hotspot Regions within IDRs"
- **Evidence pointer** Figure 3C
- **Issue** The correlation between NMR-derived and simulation-derived STI1-interaction scores is stated as "strong" but no correlation coefficient or p-value is provided.
- **Required correction** Report the correlation coefficient (e.g., Pearson or Spearman) and the associated p-value, and state the number of data points used.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data Availability Statement
- **Evidence pointer** Data Availability Statement
- **Issue** The SAXS data are stated to be deposited in SASBDB with accession code "TBD" (to be determined). This is not acceptable for a published manuscript.
- **Required correction** Provide the actual SASBDB accession codes for all SAXS data before publication.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Methods "NMR Titration of Ubiquitin (Ub) and Kd Determination"
- **Evidence pointer** Methods section
- **Issue** The criteria for excluding residues from the Kd analysis are described (R2 < 0.3, less than three CSP points, or CSPmax exceeding ten times CSPobs), but the number of residues excluded and the total number of residues analyzed are not reported.
- **Required correction** Report the number of residues included and excluded from the analysis, and provide a representative fit for at least one residue.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The authors acknowledge the limitation of the two-state model but do not discuss the potential impact of the coarse-grained simulation resolution on the quantitative conclusions, particularly the occupancy fold changes.
- **Required correction** Add a brief discussion of how the coarse-grained resolution might affect the quantitative estimates of interaction strengths and the implications for the conclusions.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 5
- **Evidence pointer** Figure 5
- **Issue** The phylogenetic tree in Figure 5A is mentioned but not described in the text. It is unclear how the tree was constructed and what the bootstrap support values are.
- **Required correction** Describe the phylogenetic tree in the text, including the method of construction and any support values, or move it to supplementary material.

## Risk / unsupported claims
- The claim that "disrupting this closed topology enhances binding to ubiquitin" is supported by a modest 1.6-fold Kd difference, which may not be biologically significant without functional validation.
- The claim that "STI1:IDR interactions are broadly conserved" is based solely on simulations for non-yeast homologs without experimental validation.
- The quantitative open/closed population fractions (6% for FL, 24% for I45A) are dependent on the two-state fitting assumption, which is acknowledged as not proven.
- The functional significance of the proposed regulatory mechanism (e.g., modulation of substrate binding by topology) is inferred from in vitro binding data but not tested in a cellular context.
- The identification of conserved SLiMs overlapping with hotspots is based on bioinformatic predictions and lacks experimental validation.