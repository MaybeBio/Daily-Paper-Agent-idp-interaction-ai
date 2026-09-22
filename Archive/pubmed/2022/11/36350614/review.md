## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Computational method development, validation, and experimental application to stress granule biology
- **Shared manuscript claim summary** The authors present rG4detector, a convolutional neural network for predicting RNA G-quadruplex (rG4) formation from sequence. They claim it outperforms existing tools in stability prediction and detection. Applying it to G3BP1 eCLIP data, they report stress-dependent enrichment of rG4s in G3BP1-bound RNAs, demonstrate G3BP1 binding to rG4-forming r(AGG)5 in vitro, show rG4 enrichment in stress granules, and find that rG4 ligands impair stress granule formation.
- **Visible evidence base** Full text including Methods, Results, Discussion, figure legends, and supplementary figure/table references
- **Missing materials affecting confidence** Actual figures, supplementary data files, and code were not provided for inspection

## Reviewer
- **Overall assessment** This manuscript presents a potentially useful computational tool for rG4 prediction and applies it to generate a biologically interesting hypothesis about rG4 involvement in stress granule biology. The computational claims are reasonably supported by the described evaluations, though the lack of access to figures and supplementary data limits full verification. The experimental work is suggestive but incomplete in establishing a direct mechanistic role for rG4s in stress granule formation. The manuscript would benefit from additional controls and a more rigorous demonstration of causality.
- **Who would be interested in the results, and why** Researchers studying RNA secondary structure prediction, RNA-binding proteins, and stress granule biology. The tool itself may be of interest to the RNA bioinformatics community, and the G3BP1-rG4 connection is relevant to those studying stress responses and neurodegeneration.
- **Major strengths** The computational approach is well-motivated, using high-throughput stability data for training. The tool appears to outperform existing methods on multiple benchmarks. The application to G3BP1 eCLIP data is a creative use of the predictor. The in vitro validation of r(AGG)5 as an rG4 and G3BP1 binding is a solid experimental contribution.
- **Major Concerns** The causal link between rG4s and stress granule formation is not firmly established. The experiments with rG4 ligands show correlation but not direct causation. The claim of "dynamic enrichment" of rG4s under stress relies on computational predictions that may carry biases. The manuscript does not adequately address potential confounding factors in the eCLIP analysis, such as differences in RNA length or expression levels between conditions.
- **Minor Comments** Several methodological details are unclear, including the exact training procedure and hyperparameter selection. The Gaussian-weighted averaging approach for detection needs more justification. The manuscript would benefit from a more detailed discussion of the limitations of the computational predictions.
- **Technical failings that need to be addressed before the case is established** The experimental evidence for rG4s regulating stress granule formation is correlative. The ligand competition experiments do not rule out off-target effects. The manuscript does not demonstrate that rG4 disruption specifically, rather than general RNA binding perturbation, is responsible for the observed effects.
- **Assessment against Nature-style criteria** Originality: The tool is novel in its use of stability data, though the architecture is not groundbreaking. Scientific importance: The potential link between rG4s and stress granules is significant if firmly established. Interdisciplinary readership: The work bridges computational biology and cell biology, which could appeal to a broad audience. Technical soundness: The computational evaluations appear sound, but the experimental evidence is not yet conclusive. Readability for nonspecialists: The manuscript is generally well-written and accessible, though some computational details may be challenging for experimental readers.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding the causal role of rG4s in stress granule formation.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental evidence for causality
- **Claim pointer** "we conclude that rG4s play a direct role in SG biology via their interactions with RNA-binding proteins"
- **Evidence pointer** Results section "SGs are colocalized with endogenous rG4s that regulate their formation"; Figure 6
- **Concern** The manuscript claims a direct role for rG4s in stress granule formation based on experiments where rG4 ligands (cPDS, QUMA-1) impair SG formation. However, these ligands may have off-target effects on other RNA structures or RNA-binding proteins. The experiments do not demonstrate that the effect is specifically due to rG4 sequestration. Additionally, the colocalization of rG4s with SGs is correlative and does not establish a functional requirement.
- **Why it matters** The central biological claim of the paper rests on this causal link. Without it, the study is primarily a computational tool paper with some preliminary biological observations. The conclusion as stated overreaches the evidence presented.
- **Resolution test** The authors should perform rescue experiments where rG4-containing RNAs are added back, or use a more specific approach such as CRISPR-based disruption of specific rG4-forming sequences. Alternatively, they could use a mutant G3BP1 that cannot bind rG4s to show that this binding is required for SG formation.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Computational prediction bias
- **Claim pointer** "rG4detector revealed a dynamic enrichment of rG4s bound by G3BP1 in response to cellular stress"
- **Evidence pointer** Results section "rG4detector reveals increased enrichment of potential rG4-containing sequences bound by G3BP1 under stress"; Figure 3
- **Concern** The eCLIP analysis relies on computational predictions of rG4 propensity. The authors note that G3BP1-bound RNAs under stress are longer on average, and they attempt to control for this. However, the analysis does not fully account for other potential confounders, such as differences in GC content, sequence composition, or RNA abundance between conditions. The threshold of 1.56 for classifying rG4FSs appears to be derived from the data itself, which could introduce circularity.
- **Why it matters** If the observed enrichment is an artifact of sequence composition or other biases, the biological conclusion would be invalid. The claim of "dynamic enrichment" is central to the paper's narrative.
- **Resolution test** The authors should perform a permutation-based analysis where rG4 predictions are randomized across transcripts to establish a null distribution. They should also validate their predictions on a subset of G3BP1-bound RNAs using an independent experimental method, such as rG4-seq or DMS-seq, under both conditions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of the tool
- **Claim pointer** "rG4detector outperforms existing methods in both predicting rG4 stability and in detecting rG4-forming sequences"
- **Evidence pointer** Results section "rG4detector improves rG4 stability prediction compared to existing methods"; Figure 1
- **Concern** The tool is trained and tested on human data, with additional validation on mouse and plant datasets. However, the performance on mouse and plant is substantially lower than on human. The authors attribute this to differences in experimental protocols, but this raises questions about the generalizability of the tool across species and experimental conditions. The manuscript does not provide a clear explanation for why the tool performs worse on non-human data.
- **Why it matters** If the tool is intended for broad use in transcriptomics, its performance across species and conditions needs to be better characterized. The current results suggest that users may need to retrain the model for non-human applications, which is not discussed.
- **Resolution test** The authors should provide a more detailed analysis of the cross-species performance, including an investigation of the features that contribute to the performance gap. They could also test whether retraining on a combined dataset improves cross-species performance.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Methodological clarity
- **Affected element** Training procedure
- **Evidence pointer** Methods section "rG4detector architecture"
- **Issue** The description of the training procedure is incomplete. The manuscript states that hyperparameters were selected using a search over 600 random combinations, but does not specify the range of values tested for each hyperparameter or the criteria for selecting the best combination.
- **Required correction** Provide a table or supplementary material listing the hyperparameter ranges and the final selected values. Also specify the exact training/validation split and how the validation set was used.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical analysis
- **Affected element** Figure 3E and 3F
- **Evidence pointer** Results section "rG4detector reveals increased enrichment of potential rG4-containing sequences bound by G3BP1 under stress"
- **Issue** The manuscript reports relative differences of 1.33 and 1.95 fold for "moderate" and "high" bins, but does not provide confidence intervals or statistical tests for these comparisons. The significance of these differences is unclear.
- **Required correction** Add statistical tests (e.g., chi-square or Fisher's exact test) for the bin comparisons and report confidence intervals for the fold differences.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Experimental details
- **Affected element** EMSA experiments
- **Evidence pointer** Methods section "Electro-mobility shift assays (EMSA)"
- **Issue** The manuscript states that cPDS and QUMA-1 were used at concentrations of 10 uM and 1 uM, respectively, for live-cell imaging, but the concentrations used in the EMSA competition experiments are not clearly specified.
- **Required correction** Clearly state the concentrations of cPDS and QUMA-1 used in each EMSA experiment, including the titration experiment shown in Figure 4E.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Code and data
- **Evidence pointer** Data Availability section
- **Issue** The manuscript states that code and processed data are available via GitHub, but does not provide a version number or DOI for the repository. This makes it difficult for readers to access the exact version used in the study.
- **Required correction** Provide a DOI or a specific version tag for the GitHub repository, and consider depositing the code in a permanent archive such as Zenodo.

## Risk / unsupported claims
- The claim that rG4s "play a direct role in SG biology" is not fully supported by the experimental evidence, which is correlative and relies on ligand-based perturbations with potential off-target effects.
- The claim of "dynamic enrichment" of rG4s in G3BP1-bound RNAs under stress is based on computational predictions that may carry biases not fully controlled for.
- The statement that rG4detector "outperforms" existing methods is supported for the tested datasets, but the generalizability of this claim across all possible applications is not established.
- The assertion that "endogenous rG4s are enriched within SGs" is based on colocalization with a small molecule probe (BioTASQ), which may have limited specificity.
- The mechanistic model proposed in the Discussion, involving rG4-mediated anchoring of RBPs and RNA-RNA interactions, is speculative and not directly tested in this study.