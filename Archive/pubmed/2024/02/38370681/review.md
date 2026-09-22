## Review setup
- **Input scope** Full manuscript text (preprint, bioRxiv)
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and technical soundness as presented in the provided manuscript
- **Shared manuscript claim summary** The authors present a high-throughput functional profiling approach to survey post-transcriptional regulatory activity across the yeast disordered proteome. They identify hundreds of repressive disordered peptides, characterize their genetic dependencies on 5'-3' mRNA decay machinery, define distinct classes of regulators (motif-dependent vs. composition-driven) via mutational scanning, and use machine learning to implicate aromatic residues in repressor activity.
- **Visible evidence base** Main text figures (Figures 1–6), supplementary figures (S1–S6), methods section, and data availability statements
- **Missing materials affecting confidence** Raw sequencing data, detailed computational pipelines, and full supplementary tables are referenced but not provided in the manuscript text; this limits independent verification of some quantitative claims

## Reviewer
- **Overall assessment** This manuscript presents a substantial and well-executed functional genomics effort to systematically characterize disordered regions with post-transcriptional regulatory activity. The experimental design is rigorous, combining a fluorescence-based tethering assay with high-throughput sequencing and mutational scanning. The identification of hundreds of repressive peptides, the delineation of genetic dependencies on decay machinery, and the classification into motif-dependent vs. composition-driven regulators represent meaningful advances. However, several technical concerns regarding data analysis, statistical rigor, and validation of machine learning predictions need to be addressed before the conclusions are fully established.
- **Who would be interested in the results, and why** Researchers studying post-transcriptional gene regulation, RNA-binding proteins, intrinsically disordered regions, and functional genomics. The work provides a resource for the community and establishes a framework for dissecting disordered region function that could be applied to other organisms and regulatory processes.
- **Major strengths** 1) The scale and comprehensiveness of the screen (~45,000 peptides covering the yeast disordered proteome) is impressive and provides a valuable resource. 2) The integration of multiple orthogonal approaches (tethering assay, genetic perturbations, mutational scanning, machine learning) strengthens the conclusions. 3) The distinction between motif-dependent and composition-driven repressors is conceptually important and well-supported by the scrambling experiments. 4) The validation of specific motifs in endogenous proteins (Tis11, Eap1) adds biological relevance.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** 
- **Assessment against Nature-style criteria** 
- **Recommendation posture** 

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "many repressive disordered regions converge on 5'-3' mRNA decay machinery" based on genetic dependency experiments in strains depleted of Dcp2, Pop2, or Ccr4.
- **Evidence pointer** Figure 3C–J, Methods section "Epistasis analysis"
- **Concern** The epistasis analysis relies on rescaling activity scores in degron-tagged strains using LOESS regression against wildtype scores, assuming "the true activity of most peptides does not change in the mutant relative to the wildtype." This assumption is not explicitly justified and could bias the identification of differentially active peptides. If a substantial fraction of peptides are genuinely affected by nuclease depletion, the rescaling could mask true effects or create spurious ones. The authors should provide a more detailed justification for this approach, including sensitivity analyses with different rescaling assumptions, and report the proportion of peptides affected under alternative normalization strategies.
- **Why it matters** The genetic dependency classification is central to the claim that repressors act through specific decay pathways. If the rescaling procedure introduces bias, the pathway assignments could be incorrect, undermining a key conclusion of the paper.
- **Resolution test** Provide a detailed description of the LOESS rescaling procedure, including parameters used and robustness checks. Report the number of peptides classified as dependent on each nuclease under different rescaling approaches (e.g., quantile normalization, no rescaling). Show that the main conclusions are robust to these choices.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The authors state that "900 repressive disordered peptides derived from 395 different proteins" were identified using an activity score threshold of −1.
- **Evidence pointer** Figure 2A, Results section "Identification of post-transcriptional regulatory regions within disordered regions"
- **Concern** The choice of activity score threshold (−1) is based on a comparison with individual flow cytometry measurements of 16 selected peptides. This is a small validation set, and the manuscript does not report confidence intervals or error rates for the classification. The authors should provide a more rigorous statistical framework for defining repressors, such as using a formal false discovery rate control based on the distribution of activity scores for known non-repressive controls, or reporting the sensitivity and specificity of the threshold using a larger validation set.
- **Why it matters** The number of repressive peptides and proteins is a key quantitative output of the screen. If the threshold is not well-calibrated, the reported numbers could be over- or under-estimates, affecting downstream analyses and the utility of the resource.
- **Resolution test** Provide a more extensive validation set (e.g., 50–100 peptides) with known positive and negative controls. Report receiver operating characteristic (ROC) or precision-recall curves for the activity score threshold. Alternatively, use a statistical model (e.g., mixture model) to estimate the false discovery rate at the chosen threshold.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretability of machine learning
- **Claim pointer** The authors claim that "aromatic amino acids are strongly associated with both motif-dependent and composition-driven repressors" based on logistic regression and a light attention model.
- **Evidence pointer** Figure 6E–F, Results section "Aromatic amino acids are associated with regulatory activity in disordered regions"
- **Concern** The logistic regression models use amino acid composition as features, which is appropriate for composition-driven repressors but may not capture the positional information relevant for motif-dependent repressors. The light attention model on ESM-1b embeddings improves prediction (AUPRC = 0.9), but the interpretation of attention weights as identifying "functionally important residues" is not fully validated. The authors should demonstrate that attention weights correlate with experimentally validated functional residues (e.g., from the mutational scanning data) and compare against simpler baselines (e.g., position-specific scoring matrices) to show the added value of the attention mechanism.
- **Why it matters** The machine learning analysis is used to derive biological insights about the sequence determinants of repressor activity. If the model interpretation is not well-validated, the conclusions about aromatic residues and their context may be overstated.
- **Resolution test** Validate attention weights against known functional residues from mutational scanning for a subset of repressors. Compare the light attention model's performance and interpretability against simpler models (e.g., logistic regression on k-mer features) to demonstrate the unique contribution of the attention mechanism.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** The authors suggest that their findings "define the molecular principles and biochemical mechanisms that govern post-transcriptional gene regulation by disordered regions" and extend the paradigm of transcription factor activation domains to post-transcriptional regulators.
- **Evidence pointer** Discussion section
- **Concern** The study is performed entirely in S. cerevisiae using a tethering assay with a single reporter mRNA. The generalizability of the findings to other organisms, endogenous mRNA targets, and different regulatory contexts (e.g., translation vs. decay) is not directly tested. The authors should temper their claims or provide additional evidence (e.g., analysis of orthologous sequences, validation in a second organism) to support the broader relevance of their conclusions.
- **Why it matters** The title and discussion imply broad mechanistic insights, but the experimental system is limited. Overstating the generalizability could mislead readers about the scope of the findings.
- **Resolution test** Add a discussion of the limitations of the tethering assay and the yeast system. If possible, include preliminary data on orthologous peptides from other species or validation in a different cellular context to support the generalizability claims.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1A
- **Evidence pointer** Figure 1A
- **Issue** The schematic of the tethering assay is dense and may be difficult for non-specialists to follow. The role of the λN peptide, boxB hairpins, and the reporter constructs could be explained more clearly.
- **Required correction** Consider simplifying the schematic or adding a more detailed legend that walks the reader through the assay step by step.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section "Deep sequencing processing and determination of activity and stability scores"
- **Evidence pointer** Methods section
- **Issue** The description of the maximum likelihood estimator for activity scores is brief. The custom R script is mentioned but not fully described, and the scoring function is referenced as "based on established procedures" without specific details.
- **Required correction** Provide a more detailed mathematical description of the scoring function and the maximum likelihood estimation procedure, or include the R script as a supplementary file with documentation.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 3G–H
- **Evidence pointer** Figure 3G–H
- **Issue** The Venn diagram and bar plots showing overlap of genetic dependencies are informative but could benefit from additional annotation, such as the number of peptides in each category and statistical significance of overlaps.
- **Required correction** Add counts to the Venn diagram and include statistical tests (e.g., hypergeometric test) for the significance of overlaps between dependency categories.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Validation
- **Affected element** Figure 5E
- **Evidence pointer** Figure 5E
- **Issue** The growth assay for Tis11 mutants is a single condition (iron depletion). Additional conditions or a dose-response would strengthen the conclusion that the identified motif is functionally important.
- **Required correction** Consider adding a second condition or a time-course experiment to confirm the phenotype.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Accessibility
- **Affected element** Data availability
- **Evidence pointer** Data and code availability section
- **Issue** The GitHub repository is mentioned, but it is not clear if the code is versioned, documented, and accompanied by example data. This could hinder reproducibility.
- **Required correction** Provide a more detailed description of the repository contents, including a README, example scripts, and instructions for running the analysis.

## Risk / unsupported claims
- The claim that "hundreds of regulatory sequences within intrinsically disordered regions" were identified relies on a threshold that is not rigorously validated (R1-M2).
- The classification of repressors into motif-dependent vs. composition-driven classes is based on scrambling experiments, but the statistical criteria for this classification are not fully described; the manuscript states that 65% of fragments had similar activity between wildtype and shuffled sequences, but the threshold for "similar" is not defined.
- The genetic dependency assignments (R1-M1) are based on a rescaling procedure that could introduce bias.
- The machine learning interpretation of aromatic residues as key determinants (R1-M3) is not fully validated against experimental data.
- The generalizability of the findings to other organisms and endogenous targets is claimed but not directly tested (R1-M4).
- The statement that "disordered regions within RNA binding proteins are required to control mRNA decay and protein synthesis" is presented as established fact in the summary, but the manuscript does not provide direct evidence for this requirement in the context of the identified peptides.

## Assessment against Nature-style criteria
- **Originality** High. The systematic functional profiling of the disordered proteome for post-transcriptional regulatory activity is novel and provides a resource that could enable many follow-up studies.
- **Scientific importance** High. The work addresses a fundamental question about how disordered regions in RNA-binding proteins contribute to gene regulation, and the findings have implications for understanding the mechanisms of mRNA decay and translation control.
- **Interdisciplinary readership** Moderate. The work will primarily appeal to molecular biologists, biochemists, and computational biologists. The machine learning component may attract a broader audience, but the biological focus may limit appeal to other fields.
- **Technical soundness** Moderate. The experimental design is generally rigorous, but several analytical concerns (threshold selection, rescaling procedure, machine learning validation) need to be addressed to fully support the conclusions.
- **Readability for nonspecialists** Moderate. The manuscript is well-written but dense, and the methods are complex. The summary and figures are accessible, but the detailed results may be challenging for readers outside the field.

## Recommendation posture
Supportive if technical concerns are resolved. The manuscript presents a valuable and potentially impactful resource, but the analytical concerns regarding threshold selection, genetic dependency classification, and machine learning validation need to be addressed before the conclusions are fully established.