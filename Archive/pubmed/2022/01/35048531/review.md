## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods, accession numbers) as provided.
- **Assessment boundary** Scientific content, technical soundness, and interpretation of results as presented in the provided text. No supplementary figures, tables, or raw data were available for independent verification.
- **Shared manuscript claim summary** The authors propose that the RING domain of MUL1 (RINGMUL1) recruits the intrinsically disordered substrate p53-TAD (TADp53) as a complex with UBE2D2~UB conjugate, and that this multivalent interaction underlies the ability of RINGMUL1 to ubiquitylate TADp53.
- **Visible evidence base** NMR chemical shift perturbation (CSP) experiments, X-ray crystallography (RINGMUL1, RINGMUL1:UBE2D2, UBE2D2), ITC binding measurements, CD spectroscopy, and stability assays of UBE2D2~UB mimetics.
- **Missing materials affecting confidence** Supplementary figures and tables (e.g., Fig. S1, S2, Table S1), raw NMR spectra, crystallographic refinement statistics, ITC thermograms, and full experimental details for all biophysical assays. These are referenced but not provided in the submitted text.

## Reviewer
- **Overall assessment** The manuscript addresses a mechanistically interesting question in RING E3 ligase biology: how a RING domain alone can recruit and ubiquitylate an intrinsically disordered substrate. The authors combine structural and biophysical approaches to propose a multivalent binding model. However, the evidence presented is largely indirect, and several key claims are not fully supported by the data described. The manuscript would benefit from clearer presentation of quantitative data and additional controls to substantiate the proposed mechanism.
- **Who would be interested in the results, and why** Researchers in the fields of ubiquitin signaling, E3 ligase enzymology, and intrinsically disordered protein interactions. The proposed multivalent recruitment mechanism may be of general interest to those studying how RING E3s achieve substrate specificity without dedicated substrate-binding domains.
- **Major strengths** 1. The study addresses a significant gap in understanding how RINGMUL1 alone can ubiquitylate TADp53. 2. The combination of X-ray crystallography and NMR provides complementary structural information. 3. The use of stabilized UBE2D2~UB mimetics is a reasonable approach to study a transient conjugate. 4. The observation of accelerated oxyester hydrolysis upon RINGMUL1 binding is potentially interesting.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5.
- **Assessment against Nature-style criteria** **Originality**: Moderate. The concept of multivalent substrate recruitment by RING E3s is not entirely new, but the specific application to MUL1 and p53 is novel. **Scientific importance**: Moderate. The findings may be relevant to understanding MUL1 function in disease contexts, but the mechanistic advance is incremental. **Interdisciplinary readership**: Limited. The work is primarily of interest to structural biologists and ubiquitin field specialists. **Technical soundness**: Weak. Several key claims are based on indirect evidence or lack quantitative support. **Readability for nonspecialists**: Acceptable. The manuscript is generally well-written, though some sections assume familiarity with NMR and ubiquitin enzymology.
- **Recommendation posture** Currently not established from the provided evidence. The proposed mechanism is plausible but requires additional experimental support and clarification of several technical points.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that RINGMUL1 binding induces a closed conformation of UBE2D2RS–UBR OE and strongly accelerates its hydrolysis.
- **Evidence pointer** Results section, Figures 3, 4, 5; location not provided
- **Concern** The claim that RINGMUL1 induces a closed conformation is based on CSP patterns, but no quantitative analysis (e.g., chemical shift mapping onto a structural model) is presented. The hydrolysis acceleration is described qualitatively, and the half-life estimation method is not fully detailed.
- **Why it matters** The closed conformation and hydrolysis acceleration are central to the proposed mechanism. Without quantitative evidence, the reader cannot assess the magnitude or significance of these effects.
- **Resolution test** Provide quantitative CSP analysis with mapped residues, a clear comparison of hydrolysis rates with appropriate controls, and statistical analysis of half-life measurements.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that TADp53 exhibits enhanced binding affinity for RINGMUL1:UBE2D2RAS–UBR OE compared to RINGMUL1:UBE2D2.
- **Evidence pointer** Results section, Table 1, Figure 6; location not provided
- **Concern** The Kd values are reported, but the experimental conditions, fitting models, and error analysis are not described. The difference between Kd values (171 vs 34 µM) is presented as significant, but no statistical test or confidence intervals are provided.
- **Why it matters** The enhanced affinity is a key claim supporting the multivalent recruitment model. Without rigorous binding analysis, this claim is not substantiated.
- **Resolution test** Provide full ITC or NMR titration details, including fitting models, errors, and replicates. Perform appropriate statistical comparisons between conditions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors propose that the multivalency of TADp53 binding underlies its ubiquitylation by RINGMUL1.
- **Evidence pointer** Discussion section; location not provided
- **Concern** The multivalency model is inferred from CSP data and binding affinities, but no direct evidence (e.g., mutagenesis of TADp53 regions, crosslinking, or kinetic analysis of ubiquitylation) is provided to support this mechanism.
- **Why it matters** The proposed mechanism is the central conclusion of the manuscript. Without direct functional evidence, the model remains speculative.
- **Resolution test** Perform ubiquitylation assays with TADp53 mutants lacking specific regions, or provide kinetic evidence that multivalent binding enhances ubiquitylation efficiency.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that the N77A mutation of UBE2D2 stabilizes the closed conformation of UBE2D2RAS–UBR OE.
- **Evidence pointer** Results section, Figures 3, 4; location not provided
- **Concern** The structural basis for this claim is not clearly explained. The authors mention a hydrogen bond between N77 and the G76 carbonyl of UB, but no structural data (e.g., mutant structure or modeling) is shown to support this.
- **Why it matters** The N77A mutation is used as a tool to study the closed conformation. If the structural rationale is not established, the interpretation of experiments using this mutant is weakened.
- **Resolution test** Provide structural or modeling data showing the N77-G76 interaction, or perform additional experiments (e.g., NMR relaxation) to characterize the conformational differences.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the crystal structure of RINGMUL1:UBE2D2 reveals positional plasticity of RINGMUL1 relative to UBE2D2.
- **Evidence pointer** Results section, Figure 2; location not provided
- **Concern** The RMSD values are reported, but the significance of the positional plasticity is not discussed in the context of the proposed mechanism. It is unclear how this plasticity relates to substrate recruitment.
- **Why it matters** The structural plasticity is used to explain the CSP data and the proposed multivalent interactions. Without a clear link, this observation is descriptive rather than mechanistic.
- **Resolution test** Provide a detailed analysis of the conformational variability and its potential functional implications, possibly with molecular dynamics simulations or additional structural studies.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states that RINGMUL1 binding "strongly accelerated" hydrolysis, but the magnitude of this effect is not quantified.
- **Required correction** Provide a quantitative statement (e.g., fold-change in hydrolysis rate) in the abstract.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Materials and methods
- **Evidence pointer** Materials and methods section; location not provided
- **Issue** The NMR titration experiments for Kd determination are not described in sufficient detail (e.g., protein concentrations, titration points, data fitting).
- **Required correction** Add a detailed description of the NMR titration protocol and data analysis.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion section; location not provided
- **Issue** The authors speculate about the in vivo relevance of the proposed mechanism but do not provide any experimental evidence to support this speculation.
- **Required correction** Clearly distinguish between speculation and experimentally supported conclusions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figures
- **Evidence pointer** Figures 3, 4, 6; location not provided
- **Issue** The CSP data are presented as color gradients on structures, but the quantitative values are not easily accessible to the reader.
- **Required correction** Include a supplementary table with CSP values for all residues, or provide a more quantitative figure.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Accession numbers
- **Evidence pointer** Accession numbers section; location not provided
- **Issue** The NMR chemical shift assignments are mentioned in the text (BMRB No. 36251) but not listed in the accession numbers section.
- **Required correction** Add the BMRB accession number to the accession numbers section.

## Risk / unsupported claims
- The claim that RINGMUL1 induces a closed conformation of UBE2D2~UB is not quantitatively supported.
- The claim that TADp53 binding affinity is enhanced by the UBE2D2~UB conjugate is based on limited data without statistical analysis.
- The proposed multivalent recruitment model is speculative and lacks direct functional evidence.
- The in vivo relevance of the proposed mechanism is not experimentally addressed.
- The structural basis for the N77A mutation effect is not established.