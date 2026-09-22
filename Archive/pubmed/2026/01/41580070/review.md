## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, conclusion) without figures or supplementary materials
- **Assessment boundary** Scientific claims, methodological soundness, and evidence consistency as presented in the provided text; web server functionality not independently tested
- **Shared manuscript claim summary** The authors present ProteoCast, a web server for predicting, validating, and interpreting missense variant effects using evolutionary constraint analysis, structural context integration, and a three-tier variant classification system. They claim state-of-the-art performance on ClinVar data, generalizability across species, novel segmentation of disordered regions for functional motif discovery, and utility of structure-aware scoring.
- **Visible evidence base** Text descriptions of evaluations against ClinVar, ProteinGym, Drosophila lethal mutations, and yeast functional sites; case study descriptions for TINF2, p27Kip1, SARS-CoV-2 spike, and PPARγ; methodological descriptions of GEMME integration, RSA modulation, and segmentation approach
- **Missing materials affecting confidence** Figures (Fig. 1-3) referenced but not provided; supplementary methods (reference 25) not available; detailed benchmark results and statistical comparisons not shown; web server interface and functionality not independently assessable

## Reviewer
- **Overall assessment** The manuscript describes a potentially useful web server that integrates existing evolutionary scoring with structural context and segmentation for disordered regions. The core methodology builds on previously published work (GEMME), and the novel contributions appear to be the integration, the three-tier classification, and the segmentation approach for IDRs. However, the evidence presented in the text is largely descriptive, with key quantitative results referenced to a separate publication (reference 25) rather than shown. The performance claims, particularly the comparison to EVE and the disordered region segmentation results, require the missing figures and supplementary data to be fully evaluated. The case studies are illustrative but not systematically validated. The manuscript would benefit from clearer presentation of benchmark statistics, error bars, and statistical significance testing.
- **Who would be interested in the results, and why** Clinical geneticists and molecular diagnosticians interpreting variants of uncertain significance; protein engineers and functional genomics researchers prioritizing mutations for experimental validation; researchers studying intrinsically disordered regions and linear motifs; computational biologists developing variant effect predictors. The web server's accessibility and unsupervised nature may appeal to experimental laboratories without specialized bioinformatics expertise.
- **Major strengths** 1) Addresses a practically important problem with a user-friendly tool; 2) Transparent, unsupervised methodology that avoids black-box limitations of deep learning approaches; 3) Novel application of segmentation to mutational sensitivity profiles for IDR functional motif discovery; 4) Integration of structural context through RSA modulation is conceptually sound; 5) Broad applicability across species and variant types.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** 
- **Recommendation posture** Supportive if technical concerns are resolved

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "ProteoCast demonstrates state-of-the-art performance in discriminating pathogenic from benign mutations in humans. Specifically, it achieves a per-protein average Area Under the Curve (AUC) of 0.923 against ~63,000 variants annotated in ClinVar, compared to 0.920 for PoET and TranceptEVE, 0.919 for GEMME, and 0.914 for EVE."
- **Evidence pointer** Results section, "Classifying variants" subsection; location not provided
- **Concern** The central performance claim relies on AUC values presented without confidence intervals, statistical significance testing, or details on the evaluation protocol. The differences between ProteoCast (0.923) and PoET/TranceptEVE (0.920) are marginal and may not be statistically significant. The text states that "comparison detailed in25" for the EVE classification comparison, but reference 25 is not provided. Without access to the full benchmark results, including per-protein performance distributions, standard errors, and the specific variant subsets used, the claim of state-of-the-art performance cannot be verified.
- **Why it matters** The primary scientific contribution of the manuscript hinges on demonstrating that ProteoCast offers competitive or superior predictive performance. If the performance differences are not statistically robust, the practical value of the tool is diminished. The comparison to EVE is particularly important because the authors claim broader coverage (99% vs. EVE's subset), but the trade-off between coverage and accuracy needs rigorous quantification.
- **Resolution test** Provide the full benchmark results with confidence intervals, per-protein performance distributions, and statistical tests comparing ProteoCast to each baseline method. Include the evaluation protocol details (e.g., variant filtering, cross-validation scheme, handling of overlapping variants). If the comparison is detailed in reference 25, that publication must be made available for review.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological validation
- **Claim pointer** "ProteoCast successfully identifies twice as many functional motifs in intrinsically disordered regions compared to conservation-based phylogenetic methods."
- **Evidence pointer** Results section, "Decrypting intrinsically disordered regions" subsection; location not provided
- **Concern** The claim of identifying twice as many functional motifs in IDRs is presented without quantitative details. The text mentions 186 out of ~500 yeast functional sites falling within segments identified by ProteoCast, compared to phylo-HMM, but the denominator, the definition of a "functional motif," the matching criteria between predicted segments and annotated sites, and the statistical significance of the enrichment are not specified. The case studies (TINF2, p27Kip1) are qualitative and may represent cherry-picked examples.
- **Why it matters** The segmentation approach for IDRs is presented as a key novel contribution. If the enrichment is not rigorously quantified with appropriate controls (e.g., random segment placement, background conservation levels), the claim of superior motif discovery is not established. The biological utility of the approach depends on its precision and recall relative to known functional elements.
- **Resolution test** Provide a systematic evaluation with clear definitions: how functional sites were annotated, how predicted segments were matched to these sites, what constitutes a "hit," and what the false discovery rate is. Include a comparison to appropriate baselines (e.g., random segments, conservation-only methods) with statistical significance testing. Present precision-recall curves or equivalent metrics.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "ProteoCast then models the predicted evolutionary score distribution with a mixture of three Gaussians. The parameters of these Gaussians are used to define thresholds for classifying variants as impactful, mild, or neutral."
- **Evidence pointer** Methods section, "Capturing variant effects from evolutionary information"; location not provided
- **Concern** The three-tier classification using a Gaussian mixture model is described without details on model fitting, initialization, convergence criteria, or handling of non-Gaussian score distributions. The choice of three components is asserted but not justified. The sensitivity of the classification to alignment quality, sequence diversity, and protein length is not discussed. The text states that "ProteoCast can leverage sparser evolutionary information" than EVE, but the mechanism for this (e.g., different quality thresholds, imputation strategies) is not explained.
- **Why it matters** The three-tier classification is a central feature of the web server and is used for the ClinVar sensitivity/specificity claims. If the GMM fitting is unstable or the thresholds are not robust across proteins, the classification results may be unreliable. The claim of handling sparse evolutionary information needs technical substantiation.
- **Resolution test** Describe the GMM fitting procedure in detail, including initialization, parameter estimation, and model selection. Provide evidence of classification stability across proteins with varying alignment depths. Explain how the method handles positions with missing or low-quality data and demonstrate that the 99% coverage claim is not achieved by assigning low-confidence variants to the "neutral" class by default.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "When complexed conformations are not available, comparing the purely evolutionary-based predictions with those modulated by RSA on the monomeric state can help users identify residues important for protein interactions and functions, but not for stability."
- **Evidence pointer** Results section, "Tuning the predictions to 3D conformations" subsection; location not provided
- **Concern** The PPARγ case study is presented as evidence that comparing evolutionary scores with and without RSA modulation can identify interaction residues. However, the text states that "two thirds of the 30 residues displaying the highest gain in mutational sensitivity upon excluding RSA establish molecular contacts with DNA and the substrate NCOA2 peptide." This is a qualitative observation without statistical evaluation. The choice of 30 residues is arbitrary, and the expected overlap by chance is not calculated. The SARS-CoV-2 spike example shows improved correlation with experimental data (ρ = 0.62 vs 0.54), but the significance of this difference is not tested.
- **Why it matters** The structure-aware scoring is presented as a distinguishing feature of ProteoCast. If the ability to identify interaction residues is not rigorously demonstrated, users may be misled about the interpretative power of the tool. The improvement in correlation for the spike protein is modest and may not generalize.
- **Resolution test** Provide a systematic evaluation of the RSA modulation approach across multiple proteins with known interaction interfaces. Calculate enrichment statistics for interaction residues among top-ranked residues with appropriate background models. Test the significance of correlation differences using appropriate methods (e.g., bootstrap or permutation tests).

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states "77% sensitivity and 87% specificity for pathogenicity prediction" but does not specify the threshold used for classification or whether this is the same threshold as the three-tier system. The relationship between the continuous score and the categorical classification is unclear.
- **Required correction** Clarify whether the sensitivity/specificity values refer to the binary classification (pathogenic vs. benign) derived from the three-tier system or to a different threshold. Specify the threshold or decision rule used.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, "Segmenting mutational sensitivity profiles"
- **Evidence pointer** Methods section; location not provided
- **Issue** The penalty term ασ²log(n) with α = 1.4 is stated, but the rationale for this specific value and the sensitivity of results to this choice are not discussed. The Hall estimator for variance is mentioned but not described.
- **Required correction** Provide justification for the choice of α and describe the Hall estimator. Include a sensitivity analysis or reference to one showing that results are robust to reasonable variations in these parameters.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results, "Classifying variants"
- **Evidence pointer** Results section; location not provided
- **Concern** The comparison to EVE is mentioned, but other state-of-the-art methods (e.g., AlphaMissense, ESM-1v, PrimateAI) are not discussed. The choice of comparators is not justified.
- **Required correction** Include a broader comparison to current state-of-the-art predictors or justify why only EVE and the ProteinGym baselines are used.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Accessibility
- **Affected element** Web server description
- **Evidence pointer** Web server description section; location not provided
- **Issue** The manuscript states the server is freely available but does not describe usage limits, data retention policies, or whether users can download results. The input size limits (e.g., maximum protein length, number of variants) are not specified.
- **Required correction** Provide details on server usage policies, including any limits on input size, data retention, and result download options.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Results, "Decrypting intrinsically disordered regions"
- **Evidence pointer** Results section; location not provided
- **Concern** The statement "ProteoCast achieved comparable overall accuracy on disordered (pLDDT<70) and ordered ClinVar mutations (0.84 vs 0.81)" presents accuracy values without confidence intervals or tests of significance.
- **Required correction** Provide confidence intervals and statistical tests for the accuracy comparison between disordered and ordered regions.

## Risk / unsupported claims
- The claim of "state-of-the-art performance" based on AUC values without confidence intervals or significance testing is not fully supported by the presented evidence.
- The claim of identifying "twice as many functional motifs" in IDRs is not quantitatively substantiated in the provided text.
- The generalizability claim across species (Drosophila) is based on a single metric (85% detection of lethal mutations) without comparison to other methods or discussion of potential biases.
- The utility of the RSA modulation for identifying interaction residues is supported only by qualitative case studies without statistical evaluation.
- The claim that ProteoCast "can leverage sparser evolutionary information" than EVE is not technically explained or demonstrated.
- The three-tier classification system's reliability and stability across diverse proteins is not established.
- The web server's usability, scalability, and practical performance are not independently verifiable from the manuscript text alone.