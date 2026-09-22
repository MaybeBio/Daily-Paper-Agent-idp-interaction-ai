## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) as provided
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the supplied text. No supplementary figures, tables, or raw data were available for review.
- **Shared manuscript claim summary** The authors report that the FXR N-terminal domain (NTD) engages in interdomain contacts with the ligand-binding domain (LBD) and interacts with coregulator proteins. They identify a novel SXXLF motif (SENLF) in the NTD that mediates these interactions, supported by luciferase reporter assays, mammalian two-hybrid and one-hybrid assays, fluorescence polarization binding, and molecular dynamics simulations.
- **Visible evidence base** Results sections describing Figures 1–5, Methods section, and Discussion. Figure panels are referenced but not directly viewable. No supplementary tables (Table S1A–D) or figures (Figure S2A–E) were provided.
- **Missing materials affecting confidence** All figures and supplementary materials; raw numerical data for luciferase assays; statistical details beyond p-value thresholds; MD simulation parameters and convergence metrics; AlphaFold 3 model confidence scores beyond the single average value reported; details of the fluorescence polarization assay fitting parameters.

## Reviewer

- **Overall assessment** This manuscript addresses a relevant and understudied question in nuclear receptor biology: the functional role of the intrinsically disordered NTD of FXR. The identification of a novel SXXLF motif is potentially interesting. However, the evidence presented is largely indirect (reporter assays, hybrid assays) and the key claim that SENLF mediates both coregulator and interdomain interactions rests on a single point mutation without comprehensive validation. The MD simulations are descriptive and lack quantitative rigor in places. The manuscript would benefit from additional orthogonal validation and clearer presentation of quantitative data.

- **Who would be interested in the results, and why** Researchers in the nuclear receptor field, particularly those studying FXR biology, intrinsically disordered protein domains, and coregulator recruitment mechanisms. The potential discovery of a new interaction motif could also interest structural biologists and drug developers targeting FXR.

- **Major strengths**
  1. Addresses a poorly characterized domain (NTD) of an important nuclear receptor (FXR).
  2. Combines multiple experimental approaches (cell-based assays, binding assay, MD simulations).
  3. Identifies a specific, testable motif (SENLF) with a clear hypothesis.
  4. The observation that the NTD may interfere with LBD-coregulator interactions is a nuanced and interesting finding.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength for the central claim
- **Claim pointer** "we identify and validate a novel SXXLF motif in the NTD which mediates interactions with both coregulators and the ligand binding domain"
- **Evidence pointer** Results sections "A Novel SXXLF Motif in the FXR-NTD Mediates Interactions With the LBD" and "The SXXLF Motif Selectively Mediates NTD–Coregulator Interactions"; Figures 3 and 4
- **Concern** The central claim that SENLF is a functional interaction motif is based on a single alanine mutation (SENAA) tested in cell-based reporter and hybrid assays. The fluorescence polarization assay shows only a modest difference in EC50 (32.1 µM vs 42.3 µM) between SENLF and SENAA peptides, which is not statistically evaluated. No binding affinity measurements for the isolated motif against purified coregulator fragments are provided. The specificity of the motif is not tested (e.g., alanine scanning of flanking residues, or testing other SXXLF variants). The claim of "validation" is therefore overstated relative to the evidence.
- **Why it matters** The identification of a novel interaction motif is the primary novelty of the paper. If the evidence for this motif is weak, the central contribution of the work is undermined. A single mutation with modest effects in cell-based assays does not constitute robust validation of a new protein interaction motif.
- **Resolution test** Provide quantitative binding data (e.g., ITC, MST, or pull-down with purified proteins) showing direct interaction between the SENLF peptide and coregulator fragments or LBD. Include alanine scanning of the motif and flanking residues. Show that the SENAA mutation specifically disrupts the interaction without global misfolding (e.g., via circular dichroism or NMR). Statistical comparison of EC50 values from the fluorescence polarization assay is required.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative data presentation and statistical rigor
- **Claim pointer** "a significant decrease in response (>50%) is observed in ΔNTD for all ligands" and "a small but significant increase in fold change" and "a small but statistically significant reduction in activity"
- **Evidence pointer** Results sections "The FXR NTD Interacts With Other FXR Domains" and "The SXXLF Motif Selectively Mediates NTD–Coregulator Interactions"; Figures 1B, 1D, 4C
- **Concern** Throughout the results, the authors report "significant" differences but do not provide effect sizes, confidence intervals, or exact p-values in the text. The figures are not available for review, so the magnitude of the reported effects cannot be assessed. For the M2H assays, fold changes are described qualitatively. The normalization procedure for the coregulator experiments (normalized to no-coregulator control) is described but the raw data are not shown. The statistical tests used are mentioned in Methods but the results are not reported in a transparent manner.
- **Why it matters** The conclusions depend on the magnitude and reproducibility of the reported effects. Without clear quantitative reporting, the reader cannot evaluate whether the observed differences are biologically meaningful or merely statistically significant with small effect sizes. This is particularly important for the modest effects reported for the SENAA mutation.
- **Resolution test** Report all numerical data with effect sizes, confidence intervals, and exact p-values. Provide the raw data for all luciferase assays in supplementary material. Show individual data points in figures. For the key comparisons (WT vs SENAA, WT vs ΔNTD), provide a clear statement of the fold-change differences and their variability.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** MD simulation rigor and interpretation
- **Claim pointer** "Mutation of the motif induces large changes in conformational and allosteric coupling in FXR" and "the SENAA mutation induces a conformational rearrangement in the FXR-RXR heterodimer"
- **Evidence pointer** Results section "SXXLF Mutation Influences Interdomain Contact and Coupling in Simulations"; Figure 5
- **Concern** The MD simulations are described with limited methodological detail. The number of atoms, simulation lengths, and force field parameters are given, but no convergence metrics, error estimates, or replicate-to-replicate variability are reported. The contact map analysis is qualitative. The correlation analysis is described but the statistical significance of the differences between WT and mutant is not established. The claim of "large changes" is not supported by quantitative metrics. The AlphaFold 3 model confidence is reported as an average of 24.23, which is very low, yet the model is used as the starting point for simulations without discussion of the implications of this low confidence.
- **Why it matters** The MD simulations are used to support the mechanistic interpretation of the experimental results. If the simulations are not rigorously analyzed, the conformational conclusions are not reliable. The low confidence of the AlphaFold model raises questions about the validity of the starting structure and therefore the simulation results.
- **Resolution test** Provide convergence metrics (e.g., RMSD over time, block averaging), error bars on contact frequencies, and statistical comparison of contact maps between WT and mutant. Discuss the low AlphaFold confidence and its potential impact on the simulation results. Provide quantitative measures of conformational change (e.g., RMSD, radius of gyration, distance distributions) with uncertainties.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Functional relevance and physiological context
- **Claim pointer** "we aim to define the function of the FXR NTD" and "our work confirms two roles for the FXR-NTD: interactions with the LBD and recognition of coregulators"
- **Evidence pointer** Results sections and Discussion
- **Concern** The functional relevance of the NTD-LBD interaction and the SENLF motif is not tested in a physiological context. All experiments are performed with overexpressed constructs in HeLa cells or with purified peptides. No experiments address whether the SENLF motif is important for FXR function in a native cellular context, such as endogenous target gene expression, chromatin recruitment, or metabolic phenotypes. The claim to "define the function" of the NTD is therefore overstated.
- **Why it matters** The physiological relevance of the identified interactions is unclear. The NTD-LBD interaction and coregulator recruitment could be artifacts of overexpression or non-native assay conditions. Without functional validation in a more native context, the significance of the findings for FXR biology remains uncertain.
- **Resolution test** Perform experiments in a more physiologically relevant system, such as FXR knockout cells reconstituted with WT or SENAA mutant FXR, and measure endogenous target gene expression. Alternatively, use CRISPR-mediated mutation of the SENLF motif in a cell line and assess FXR transcriptional activity on native promoters.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure legends
- **Affected element** Figures 1–5
- **Evidence pointer** Location not provided
- **Issue** The figure legends are not available for review. Given the complexity of the assays, clear and detailed legends are essential for the reader to interpret the data.
- **Required correction** Ensure all figure legends are comprehensive, including exact sample sizes, statistical tests used, and the meaning of all error bars and significance markers.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Abstract and Results
- **Evidence pointer** Abstract, Results section "A Novel SXXLF Motif in the FXR-NTD Mediates Interactions With the LBD"
- **Issue** The abstract states "SXXLF motif" while the results section refers to "SENLF motif" and the title uses "SXXLF Motif." The relationship between the general SXXLF and the specific SENLF should be clarified early in the text.
- **Required correction** Define the SXXLF consensus and state that SENLF is the specific sequence in FXR-NTD at the first mention.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The Discussion acknowledges some limitations (e.g., absence of RXR) but does not discuss the limitations of using AlphaFold 3 models with very low confidence scores for the NTD, nor the potential for the SENAA mutation to affect NTD structure beyond the specific motif.
- **Required correction** Add a paragraph discussing the limitations of the computational models and the potential for the mutation to have broader structural effects.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Methodological detail for fluorescence polarization
- **Affected element** Methods, "Fluorescence Polarization Peptide Binding Assay"
- **Evidence pointer** Methods section
- **Issue** The assay description lacks details on the peptide concentration used, the protein concentration range tested, and the fitting model parameters. The EC50 values are reported but no error estimates are given.
- **Required correction** Provide full details of the assay conditions, including peptide concentration, protein dilution series, and the error on the EC50 values.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical analysis of MD data
- **Affected element** Results section "SXXLF Mutation Influences Interdomain Contact and Coupling in Simulations"
- **Evidence pointer** Figure 5G
- **Concern** The correlation analysis is described qualitatively. The p-value for the distance changes is mentioned (p < 0.05) but the test used is only stated as "student's t-test" without correction for multiple comparisons.
- **Required correction** Clarify the statistical approach for the correlation analysis and the distance comparisons, including whether multiple testing corrections were applied.

## Risk / unsupported claims
- The claim that SENLF is a "novel" interaction motif is supported only by sequence analysis and a single mutation; no comprehensive search for similar motifs in other proteins is presented.
- The claim that the NTD "interferes" with LBD-coregulator interaction is based on indirect reporter assays and requires direct binding studies.
- The functional significance of the NTD-LBD interaction for FXR transcriptional activity is not established in a native context.
- The MD simulation results are not quantitatively validated and the low AlphaFold confidence for the NTD is not addressed.
- The statement that "other motifs in the NTD may also interact with SRC2" is speculative and not directly tested.
- The claim that "FXR interactions with p300 may be mediated entirely by the NTD" is based on a single comparison (ΔNTD + p300 vs no-coregulator control) and requires direct binding or recruitment assays.

## Assessment against Nature-style criteria
- **Originality** Moderate. The identification of a new motif in the FXR NTD is novel, but the concept of NTD-mediated coregulator interactions is established in other nuclear receptors. The work extends this concept to FXR but does not introduce a fundamentally new paradigm.
- **Scientific importance** Moderate. FXR is an important metabolic regulator, and understanding its regulatory mechanisms is valuable. However, the physiological relevance of the identified interactions is not demonstrated, limiting the immediate impact.
- **Interdisciplinary readership** Limited. The work is primarily of interest to the nuclear receptor and transcription factor communities. The methods are standard for the field and are unlikely to attract readers from outside.
- **Technical soundness** The experimental approaches are appropriate but the quantitative rigor is insufficient. The lack of direct binding data, limited statistical reporting, and descriptive MD analysis weaken the technical foundation.
- **Readability for nonspecialists** The manuscript is generally well-written and accessible to a broad biochemical audience. The introduction and discussion are clear. However, the results section assumes familiarity with nuclear receptor assays and terminology.

## Recommendation posture
Currently not established from the provided evidence. The central claim of a novel SXXLF motif mediating both coregulator and interdomain interactions is plausible but not sufficiently validated. The evidence is largely indirect, the quantitative data are not fully reported, and the MD simulations lack rigor. The manuscript has potential but requires substantial additional experimental work, particularly direct binding studies and functional validation in a more physiological context, before the claims can be considered established.