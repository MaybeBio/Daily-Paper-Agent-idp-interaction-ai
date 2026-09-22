## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, methods, results, discussion, and conclusions.
- **Assessment boundary** Evaluation is limited to the scientific content, methodology, and claims presented in the provided manuscript. No external validation or replication was performed.
- **Shared manuscript claim summary** The authors used PEPstrMOD molecular dynamics simulations to predict that double phosphorylation of Ser166 and Ser168 in the intrinsically disordered C-terminal region (residues 151–174) of the human Y14 (RBM8A) protein induces a conformational shift from an extended to a compact structure, mediated by increased hydrogen bonding and salt bridge formation with nearby arginine residues.
- **Visible evidence base** Abstract, Introduction, Materials and Methods, Results and Discussion (including Figures 1–3 and Table 1), and Conclusions.
- **Missing materials affecting confidence** No supplementary data, raw simulation trajectories, force field parameter files, or validation metrics (e.g., RMSD, convergence criteria) were provided. The manuscript references figures and tables but their actual content is not included in the supplied text.

## Reviewer
- **Overall assessment** The manuscript addresses a biologically relevant question regarding the structural impact of phosphorylation on an intrinsically disordered region of a core exon–exon junction complex protein. However, the study relies on a single computational tool with limited validation, and the evidence presented is insufficient to robustly support the central claim that phosphorylation induces a compact conformation. The lack of quantitative analysis, ensemble sampling details, and comparison with experimental data weakens the case. The manuscript is technically sound in its execution of the chosen tool but falls short of the rigor expected for a high-impact journal.
- **Who would be interested in the results, and why** Researchers studying post-translational modifications of intrinsically disordered proteins, particularly phosphorylation-driven conformational changes, and those interested in the molecular mechanisms of exon–exon junction complex assembly and mRNA metabolism. The findings may also be of interest to computational biologists evaluating the utility of PEPstrMOD for modified peptide structure prediction.
- **Major strengths** The study addresses a specific and under-explored question about the structural role of double phosphorylation in a biologically important protein region. The use of PEPstrMOD, which explicitly accounts for post-translational modifications, is appropriate given the limitations of AlphaFold2 for such cases. The authors acknowledge the inherent challenges of studying IDRs and propose future experimental validation.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The claim that double phosphorylation induces a compact conformation in the Y14 C-terminal region.
  - **Evidence pointer** Section 3.2, Figure 2, Table 1
  - **Concern** The evidence for compaction is based on qualitative visual inspection of a single lowest-energy model and a count of hydrogen bonds. No quantitative metrics such as radius of gyration, end-to-end distance, or solvent-accessible surface area are provided. The five independent simulations are mentioned but not systematically analyzed for ensemble convergence or variability. The increase in hydrogen bonds from 6 to 29 in one model is presented without statistical context across all models.
  - **Why it matters** Without quantitative descriptors of conformational compactness and an assessment of ensemble variability, the central claim of a phosphorylation-induced structural shift is not rigorously established. The conclusion relies on anecdotal model selection rather than a systematic analysis of the simulation ensemble.
  - **Resolution test** Provide quantitative measures of compactness (e.g., radius of gyration, pairwise distance distributions) for all five models in both phosphorylation states, with mean and standard deviation. Include convergence analysis (e.g., RMSD over time) and a statistical comparison (e.g., t-test or bootstrap) between unphosphorylated and phosphorylated ensembles.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The use of PEPstrMOD with a 100 ps simulation time in vacuum is sufficient to predict stable conformational changes.
  - **Evidence pointer** Section 2, Materials and Methods
  - **Concern** The simulation time of 100 ps is extremely short for an intrinsically disordered region, which typically samples a broad conformational ensemble on microsecond timescales. The vacuum environment neglects solvent effects, which are known to critically influence IDR behavior. The authors acknowledge this limitation but do not justify why 100 ps is adequate for capturing meaningful structural differences.
  - **Why it matters** The conformational changes attributed to phosphorylation may be artifacts of insufficient sampling or the absence of solvent. The results may not be representative of the physiological behavior of the IDR, undermining the biological relevance of the conclusions.
  - **Resolution test** Extend simulations to at least microsecond timescales with explicit solvent, or provide a rigorous justification for the chosen simulation length and environment. Alternatively, validate the findings with an orthogonal method such as coarse-grained simulations or experimental data (e.g., SAXS, NMR).
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Claim pointer** The claim that the compact phosphorylated structure may aid in exon–exon junction complex formation and mRNA metabolism.
  - **Evidence pointer** Section 3.2, Figure 3, Conclusions
  - **Concern** The functional implications are speculative. The manuscript does not provide any experimental or structural evidence linking the predicted conformational change to EJC assembly or mRNA metabolism. The connection between the in silico model and biological function is asserted without a mechanistic framework or supporting data.
  - **Why it matters** The broader significance of the findings depends on the biological relevance of the predicted structural change. Without evidence connecting the conformational shift to functional outcomes, the impact of the study is limited to a computational prediction with uncertain physiological implications.
  - **Resolution test** Provide a clear mechanistic hypothesis linking the compact conformation to EJC assembly, supported by existing literature or preliminary experimental data. Alternatively, temper the conclusions to reflect the speculative nature of the functional implications.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Abstract and Introduction
  - **Evidence pointer** Abstract, Section 1
  - **Issue** The abstract and introduction assume familiarity with the exon–exon junction complex and intrinsically disordered regions without providing sufficient context for a general scientific audience.
  - **Required correction** Add a brief explanation of the exon–exon junction complex and its role in mRNA metabolism, and define intrinsically disordered regions in accessible terms.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Materials and Methods
  - **Evidence pointer** Section 2
  - **Issue** The methods section does not specify the number of replicates for the phosphorylated simulations or the criteria for selecting the "lowest energy" model. The reproducibility of the workflow is unclear.
  - **Required correction** Clearly state the number of independent simulations for each condition and the selection criteria for representative models. Provide access to input files or a detailed protocol for reproducibility.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Results and Discussion
  - **Evidence pointer** Section 3.2, Table 1
  - **Issue** The hydrogen bond counts are presented without a definition of the criteria used to identify hydrogen bonds (e.g., distance and angle cutoffs). The inclusion of salt bridges in the count is ambiguous.
  - **Required correction** Specify the hydrogen bond detection criteria and clarify whether salt bridges are counted separately or included in the total.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Interdisciplinary readership
  - **Affected element** Conclusions
  - **Evidence pointer** Section 4
  - **Issue** The statement about "hydrophilic environment" in the conclusions is unclear and appears to contradict the vacuum-based methods described earlier.
  - **Required correction** Clarify the intended meaning and reconcile with the methods section, or remove the statement if it is not supported by the presented data.

## Risk / unsupported claims
- The claim that double phosphorylation induces a compact conformation is not quantitatively supported by the provided evidence.
- The functional implications for exon–exon junction complex formation and mRNA metabolism are speculative and not backed by experimental or structural data.
- The assertion that the phosphorylated structure is "stable" is based on a single model and lacks ensemble-level validation.
- The statement regarding a "hydrophilic environment" in the conclusions is unsupported by the methods and appears inconsistent.

## Assessment against Nature-style criteria
- **Originality** The study addresses a specific question about double phosphorylation in an IDR of a core EJC protein, which is a niche but underexplored topic. The use of PEPstrMOD for this purpose is not novel, but the application to Y14 is original.
- **Scientific importance** The biological significance of the predicted conformational change is not established. The study provides a computational prediction without experimental validation or a clear mechanistic link to function, limiting its importance to a narrow computational audience.
- **Interdisciplinary readership** The manuscript is likely to appeal primarily to computational biologists and researchers studying IDRs or EJC biology. The lack of experimental validation and the narrow scope reduce its appeal to a broader readership.
- **Technical soundness** The methodology is appropriate for the stated goal but is undermined by the short simulation time, vacuum environment, and lack of quantitative analysis. The results are not robustly supported by the evidence presented.
- **Readability for nonspecialists** The manuscript is generally clear but assumes background knowledge in the field. The abstract and introduction could be improved to make the content more accessible to a general scientific audience.

## Recommendation posture
Currently not established from the provided evidence. The manuscript presents a plausible hypothesis but lacks the quantitative rigor and validation needed to support the central claim. Major revisions addressing the technical concerns, particularly the simulation methodology and quantitative analysis, are required before the case can be considered.