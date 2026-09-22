## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) without figures, tables, or supplementary material
- **Assessment boundary** Scientific claims, methodological soundness, and evidence quality as presented in the text; figure and table contents are referenced but not directly assessable
- **Shared manuscript claim summary** The authors propose two ensemble docking protocols (AutoDock Vina and DiffDock) for predicting relative binding affinities of small molecules to intrinsically disordered proteins (IDPs), using α-synuclein C-terminal fragment as a test case. They claim accurate affinity ranking of three ligands and close reproduction of binding modes observed in long-timescale MD simulations.
- **Visible evidence base** Text descriptions of results, correlation coefficients, RMSD values, computational details, and references to figures and tables (not directly visible)
- **Missing materials affecting confidence** Figures, tables, Supporting Information (Tables S1–S6, Figures S1–S21), experimental NMR data, and MD trajectory details

## Reviewer
- **Overall assessment** The manuscript addresses an important and timely problem: whether molecular docking can be adapted for IDP drug discovery. The proposed ensemble docking protocols are computationally efficient and conceptually sound. The authors provide a careful comparison against long-timescale MD simulations and experimental NMR data. However, the evidence base is limited to three ligands on a single IDP fragment, and several methodological details require clarification. The claim of "remarkable agreement" with MD is partially undermined by the low fraction of poses with sub-3 Å RMSD and by the systematic overprediction of interactions by AutoDock Vina. The study is a useful proof-of-concept but does not yet establish general applicability.

- **Who would be interested in the results, and why** Researchers in IDP drug discovery, computational chemists developing docking methods for challenging targets, and experimentalists studying IDP-ligand interactions. The work provides a practical protocol that could be adopted by groups without access to specialized MD hardware, and it highlights limitations of current scoring functions for disordered targets.

- **Major strengths**
  - Addresses a significant gap: docking methods for IDPs are underdeveloped despite growing therapeutic interest
  - Uses experimentally validated MD ensembles as a benchmark, which is more rigorous than docking to a single static structure
  - Compares two fundamentally different docking approaches (physics-based and deep learning)
  - Provides detailed methodological descriptions that would enable reproduction
  - Honest reporting of limitations, including the small number of ligands and the failure of cross-docking

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "We show that these ensemble docking protocols accurately predict the relative binding affinities of three small molecule α-synuclein ligands measured by NMR spectroscopy"
- **Evidence pointer** Results section "Ensemble Docking Accurately Predicts the Relative Affinities of Small Molecules to α-Synuclein"; Figure 3A; Supporting Information Table S1
- **Concern** The claim of accurate affinity prediction rests on only three ligands. The authors acknowledge a one-in-six probability of correct ranking by chance. With n=3, the statistical power to distinguish genuine predictive ability from chance is minimal. Moreover, the normalization procedure (min-max scaling within the set of three ligands) guarantees that the best and worst ligands will have scores of 1 and 0, respectively, which may inflate apparent separation between ligands.
- **Why it matters** The central claim of the paper is that ensemble docking can predict relative affinities for IDP ligands. With only three compounds, the result could be fortuitous. The field requires evidence that the method can rank a larger, chemically diverse set of ligands before it can be considered useful for drug discovery campaigns.
- **Resolution test** The authors should either (a) validate on a larger set of ligands (at least 8–10) with known affinities, or (b) substantially temper the claim to "proof-of-concept" and provide a clear statistical framework for assessing significance with n=3.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Methodological validity
- **Claim pointer** "generate conformational ensembles of ligand binding modes in remarkable agreement with experimentally validated long-time scale molecular dynamics simulations of ligand binding"
- **Evidence pointer** Results section "Ensemble Docking Accurately Reproduces IDP Ligand Binding Modes"; Figures 4–6; Supporting Information Tables S3, S4
- **Concern** The agreement with MD is quantified using correlation coefficients and RMSD values, but the text reports that only 28% of AutoDock Vina poses and 21% of DiffDock poses have best-matched RMSD below 3.0 Å. The authors describe this as "remarkable agreement," but a reader might interpret 72–79% of poses being poorly matched as moderate agreement at best. The choice of thresholds and the interpretation of "agreement" need justification. Additionally, the systematic overprediction of interaction populations by AutoDock Vina (e.g., dual-residue contact probabilities with RMSE = 0.14) suggests systematic bias rather than random error.
- **Why it matters** The claim of reproducing MD binding modes is a key pillar of the paper. If the agreement is only moderate, the practical utility of the method for generating accurate binding mode ensembles is questionable. Overly strong claims could mislead other researchers attempting to use this approach.
- **Resolution test** Provide a more nuanced interpretation of the RMSD distributions, including the fraction of poses with RMSD < 2.0 Å and the median RMSD. Discuss whether the observed agreement is sufficient for the intended applications (e.g., pharmacophore identification, hit-to-lead optimization). Consider reporting the Jensen-Shannon divergence or similar metric for comparing distributions rather than only correlation coefficients.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "We find that AutoDock Vina and DiffDock generate largely similar docked ensembles for α-syn-C-term but also identify some key differences"
- **Evidence pointer** Results section "Ensemble Docking Accurately Reproduces IDP Ligand Binding Modes"; Supporting Information Figures S11–S17
- **Concern** The comparison between AutoDock Vina and DiffDock is described qualitatively. The text notes that DiffDock produces lower populations of most interaction types and less variation among clusters, but no quantitative comparison of the two methods is provided in the main text. The choice of DiffDock confidence score as a "docking score" for affinity ranking is not well justified, as this score is designed for pose confidence, not binding affinity.
- **Why it matters** A central methodological contribution is the comparison of two docking approaches. Without quantitative comparison metrics (e.g., enrichment factors, rank correlation with experimental affinities, computational cost per ligand), readers cannot assess which method is preferable for which scenario.
- **Resolution test** Add a quantitative comparison table (e.g., mean and standard deviation of correlation coefficients across clusters for each interaction type, computational wall times, success rates for pose prediction). Justify the use of DiffDock confidence score as an affinity proxy or use an alternative scoring function for ranking.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** "The first application (to our knowledge) of molecular docking to successfully predict the relative affinities of small molecules to a realistic, experimentally validated conformational ensemble of an IDP"
- **Evidence pointer** Discussion section; Methods section
- **Concern** The claim of being "the first" is difficult to verify and may be challenged. More importantly, the reproducibility of the protocol is limited by several factors: (a) the MD ensembles used as input are from proprietary Anton hardware and are not publicly available; (b) the t-SNE clustering parameters are described but the specific implementation is not fully detailed; (c) the selection of the "best" pose per residue for AutoDock Vina is based on docking score, but the criteria for choosing among 20 poses per residue are not fully specified.
- **Why it matters** For the method to be adopted by the community, it must be reproducible. If the input ensembles are not available, other groups cannot benchmark their own docking protocols against this work.
- **Resolution test** Provide access to the MD ensembles (e.g., via a public repository) or clearly state the limitations this imposes. Provide a step-by-step protocol with all parameters and code availability. Soften the "first" claim or provide a thorough literature search to support it.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The abstract states "Conventional structure-based drug design methods that rely on well-defined binding sites are, however, largely unsuitable for IDPs." This is a strong claim that could be qualified, as some IDPs do have transient binding sites or undergo coupled folding and binding.
- **Required correction** Consider revising to "are often unsuitable" or "are not directly applicable" to avoid overgeneralization.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Results, affinity prediction section
- **Evidence pointer** "there is a one in six of probability the correct ranking of these ligands by random chance"
- **Issue** The sentence contains a grammatical error ("one in six of probability") and the statistical statement could be more precise. With three ligands, there are 6 possible rankings, so the probability of correct ranking by chance is 1/6, but this assumes all rankings are equally likely, which may not hold if the ligands have very different affinities.
- **Required correction** Rewrite as "there is a one-in-six probability of obtaining the correct ranking by random chance" and consider discussing whether the observed affinity differences are large enough to make some rankings more likely than others.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods, AutoDock Vina section
- **Evidence pointer** Methods section "AutoDock Vina Ensemble Docking"
- **Issue** The description states that the search space is "a cubic volume surrounding the center-of-mass of one residue" with volume proportional to the cube of the ligand's radius of gyration. The specific scaling factor is not provided.
- **Required correction** Provide the exact formula or scaling factor used to determine the search space volume.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion, cross-docking section
- **Evidence pointer** Discussion section, paragraph on cross-docking
- **Issue** The cross-docking results are described as showing that "the ensemble averaged docking scores identify the ligand that α-syn-C-term was originally simulated with as the highest affinity binder." This is presented as a limitation, but it could also be interpreted as evidence that the method is sensitive to the specific protein ensemble used, which is expected.
- **Required correction** Clarify whether this result indicates a fundamental limitation of the method or simply reflects the expected dependence on the input ensemble.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Evidence pointer** Multiple instances
- **Issue** The term "docked ensemble" is used to describe the collection of poses from docking calculations. This could be confused with the "ensemble docking" method itself.
- **Required correction** Consider using "docking pose ensemble" or "docked pose set" for clarity.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods, DiffDock section
- **Evidence pointer** Methods section "DiffDock Ensemble Docking"
- **Issue** The description states that DiffDock was run with "all default parameters" but does not specify the version of the model weights or whether the confidence model was used for ranking as described in the original DiffDock publication.
- **Required correction** Provide the specific version and any relevant parameters that differ from the default.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Insufficient number of ligands to support the claim of accurate affinity prediction
  - R1-M2: Overstatement of agreement with MD binding modes given the reported RMSD distributions
  - R1-M3: Lack of quantitative comparison between AutoDock Vina and DiffDock
  - R1-M4: Limited reproducibility due to unavailable input ensembles and incomplete methodological details

- **Assessment against Nature-style criteria**
  - **Originality**: Moderate. The application of ensemble docking to IDPs is not entirely new, but the systematic comparison of two docking approaches against long-timescale MD on a well-validated system is a useful contribution. The claim of being "the first" is not fully substantiated.
  - **Scientific importance**: High. IDP drug discovery is a growing field, and efficient computational methods for predicting ligand binding are needed. If validated on more systems, this approach could have broad utility.
  - **Interdisciplinary readership**: Moderate. The work will appeal to computational chemists, biophysicists, and drug discovery researchers. The writing is accessible but assumes familiarity with docking and MD concepts.
  - **Technical soundness**: Adequate with reservations. The methods are mostly sound, but the statistical treatment of the affinity predictions is weak, and the comparison between docking methods lacks quantitative rigor.
  - **Readability for nonspecialists**: Good. The manuscript is clearly written, with helpful context for why IDP docking is challenging. The figures (not directly assessed) appear to be well-designed based on the text descriptions.

- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising and the study is carefully executed within its limited scope. However, the claims of accurate affinity prediction and remarkable agreement with MD are not fully supported by the evidence presented. The authors should either expand the validation set or substantially temper their conclusions. The methodological details should be enhanced to ensure reproducibility.