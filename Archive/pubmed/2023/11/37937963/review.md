## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, experimental section) as provided
- **Assessment boundary** Scientific claims, methodological soundness, and evidence quality as presented in the supplied text; no external data or supplementary materials were accessed
- **Shared manuscript claim summary** The authors present a graph convolutional network (GCN)-based deep learning approach to virtually screen large compound libraries for small molecules that modulate TDP-43 nuclear liquid-liquid phase separation (anisosomes). They report identification of ~1100 candidates from ~170,000 compounds, validation of five potent hits, and confirmation of two compounds (A2, A5) that reduce anisosome formation without affecting TDP-43 splicing function. Molecular dynamics simulations propose a binding mode for compound A2 at the TDP-43 N-terminal domain.
- **Visible evidence base** Text descriptions of fluorescence imaging-based screening, GCN model training and validation, hit confirmation in two cell lines, splicing assays, and MD simulations; references to Figures 1-5 and Figure S1-S2; GitHub repository link
- **Missing materials affecting confidence** Figures and supplementary figures not provided; quantitative data (hit rates, IC50 values, statistical analyses, model performance metrics beyond validation accuracy) not fully reported in text; GitHub repository not accessed; experimental details for imaging quantification and statistical methods incomplete

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important problem: accelerating discovery of small molecule modulators of biomolecular condensates, which are increasingly recognized as therapeutic targets in neurodegeneration and cancer. The combination of imaging-based screening with GCN-based virtual screening is conceptually appealing and practically relevant. However, the current text provides insufficient quantitative evidence to fully evaluate the claims. Key weaknesses include incomplete reporting of model performance metrics, lack of statistical details for biological validation, and limited mechanistic depth in the MD simulations. The claim of "rapid discovery" is supported by the workflow design, but the actual speed improvement is not quantified. The manuscript has potential but requires substantial additional evidence and clarification before the case is established.
- **Who would be interested in the results, and why** Researchers in chemical biology, drug discovery, and neurodegeneration would find this work relevant. The methodological combination of imaging-based phenotypic screening with graph-based deep learning offers a template for tackling "undruggable" targets lacking enzymatic activity. The identified compounds, particularly A2, could serve as chemical probes for studying TDP-43 phase separation biology. Computational chemists interested in applying GCNs to phenotypic screening data would also find the approach instructive.
- **Major strengths** 1) Addresses a significant unmet need: screening for condensate modulators is technically challenging and low-throughput; the proposed workflow directly tackles this bottleneck. 2) The use of a biologically relevant disease model (TDP-43 anisosomes) with clear phenotypic readout strengthens translational relevance. 3) Validation in multiple cell lines and assessment of TDP-43 splicing function addresses specificity concerns. 4) The inclusion of MD simulations to generate binding hypotheses provides a mechanistic starting point. 5) The authors acknowledge limitations of conventional screening and provide a practical alternative.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5
- **Assessment against Nature-style criteria** Originality: The application of GCNs to condensate-modulator discovery is novel, though the underlying methods are established. Scientific importance: High, given the therapeutic potential of condensate modulation. Interdisciplinary readership: The work bridges computational chemistry, cell biology, and drug discovery, appealing to a broad audience. Technical soundness: Currently insufficiently documented to fully assess; key metrics and statistical details are missing. Readability for nonspecialists: Generally clear, but some computational details are dense and would benefit from simplification.
- **Recommendation posture** Currently not established from the provided evidence; supportive if technical concerns are resolved with additional quantitative data and clarifications

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Model validation and performance reporting
- **Claim pointer** "our proposed model performs robustly with a validation accuracy of higher than 0.90"
- **Evidence pointer** Results section "GCN model validation"; location not provided
- **Concern** The manuscript reports only a single validation accuracy metric (0.90) without providing additional performance measures such as sensitivity, specificity, precision, recall, F1-score, or area under the ROC curve. For an imbalanced classification problem (likely the case with ~300 actives out of ~3000 training compounds), accuracy alone is insufficient and potentially misleading. No confusion matrix, cross-validation strategy, or external validation results are described.
- **Why it matters** The core claim of the manuscript is that the GCN model is sufficiently accurate to enable reliable virtual screening. Without comprehensive performance metrics and validation details, readers cannot assess whether the model is genuinely predictive or merely memorizing training data. This directly affects confidence in the identified candidates.
- **Resolution test** Provide a full set of classification metrics (sensitivity, specificity, precision, recall, F1, AUC-ROC, AUC-PR), describe the cross-validation scheme (e.g., k-fold, stratified), report performance on an independent test set, and include a confusion matrix. If possible, compare model performance against simpler baselines (e.g., random forest, logistic regression with molecular fingerprints).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Hit validation and dose-response data
- **Claim pointer** "compound A2 and A5 show strong biological activity by inhibiting the TDP-43 anisosome formation"
- **Evidence pointer** Results section "Identification of two novel candidates"; Figure 4; location not provided
- **Concern** The text states that A2 and A5 show "strong biological activity" but provides no quantitative dose-response data, no EC50 or IC50 values, no statistical significance testing, and no quantification of the imaging data. The claim of "strong" activity is subjective without numerical support. Additionally, the number of biological replicates, experimental repeats, and statistical methods are not described.
- **Why it matters** For a drug discovery manuscript, quantitative potency and efficacy data are essential. Without dose-response curves and statistical analysis, the biological relevance of the compounds cannot be evaluated. The claim of "strong" activity is unsupported and may mislead readers about the therapeutic potential.
- **Resolution test** Provide dose-response curves for A2 and A5 in both DLD1 and U2OS cells, with calculated EC50/IC50 values and confidence intervals. Include statistical analysis (e.g., ANOVA with multiple comparison correction) comparing treated vs. control conditions. Report the number of independent experiments and cells analyzed per condition.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Specificity and off-target effects
- **Claim pointer** "we confirmed that compound A2 does not change the morphology of NCOR2 droplets, suggesting that compound A2 might directly interact with TDP-43"
- **Evidence pointer** Results section "Identification of two novel candidates"; Figure 4D; location not provided
- **Concern** The specificity assessment is limited to one alternative condensate-forming protein (NCOR2). The conclusion that A2 "might directly interact with TDP-43" is an overinterpretation. Lack of effect on NCOR2 droplets does not demonstrate direct TDP-43 binding; it only shows some degree of selectivity among the tested condensates. No biochemical binding assays (e.g., surface plasmon resonance, isothermal titration calorimetry, pull-down) are presented to support direct interaction.
- **Why it matters** The manuscript claims specificity and potential direct interaction, which are important for therapeutic development. Without direct binding evidence or broader selectivity profiling, the mechanism of action remains speculative. This affects the interpretation of all downstream experiments and the translational potential.
- **Resolution test** Perform direct binding assays (e.g., MST, ITC, SPR) between A2 and TDP-43. Test A2 against a panel of other condensate-forming proteins and unrelated cellular processes to assess selectivity. If direct binding is not demonstrated, revise the claim to state that A2 shows selectivity among tested condensates without implying direct interaction.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** MD simulation validity and interpretation
- **Claim pointer** "The MD simulation predicted that compound A2 bound more likely to the N-terminal domain than the RNA-recognition motifs of TDP-43"
- **Evidence pointer** Results section "MD simulation proposes that Compound A2 may disrupt the dimerization interface of the N-terminal domain of TDP-43"; Figure 5; location not provided
- **Concern** The MD simulation section lacks critical details: force field parameters for the ligand, simulation convergence criteria, number of replicates, binding free energy values with errors, and comparison with control simulations. The claim that A2 "bound more likely" to the N-terminal domain is not supported by quantitative free energy data in the text. The functional significance of the proposed binding site (E17) is not experimentally validated.
- **Why it matters** Computational predictions are only as reliable as their validation. Without rigorous simulation protocols and quantitative results, the proposed binding mode remains a hypothesis. The claim that A2 may disrupt the dimerization interface is speculative and not tested experimentally.
- **Resolution test** Provide binding free energy calculations (e.g., MM-PBSA, FEP) with standard deviations from multiple independent simulations. Include control simulations with a known non-binder. Validate the proposed binding site by mutagenesis (e.g., E17A) and test whether A2 binding and activity are affected. If experimental validation is not feasible, clearly label the MD results as hypothesis-generating.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Screening workflow and hit rate reporting
- **Claim pointer** "GCN identified ~1100 candidates (0.65%) that were predicted to show biological activity of inhibiting anisosomes"
- **Evidence pointer** Results section "GCN model validation"; location not provided
- **Concern** The manuscript reports that ~1100 candidates were identified and ~300 were confirmed active, but the experimental validation details are incomplete. The text mentions "top five candidates" were validated, yet also states ~300 were confirmed. The relationship between these numbers is unclear. The criteria for selecting the five candidates for detailed validation, the confirmation rate for the broader set, and the false positive/negative rates are not described.
- **Why it matters** The practical utility of the virtual screening approach depends on the enrichment factor and hit rate compared to random screening. Without these metrics, the claimed advantage of the GCN method cannot be evaluated. The discrepancy between 1100 predicted, 300 confirmed, and 5 validated creates confusion about the actual performance.
- **Resolution test** Clearly describe the validation cascade: how many of the 1100 candidates were experimentally tested, the confirmation rate, and the criteria for selecting the five candidates for detailed study. Report enrichment factors and compare hit rates to the initial 7000-compound screen. Provide a flow diagram of the screening pipeline.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Data availability
- **Affected element** GitHub repository
- **Evidence pointer** Experimental section "Graph convolutional network"; location not provided
- **Issue** The GitHub link is mentioned but the repository contents are not described. Readers cannot assess the code, data, or model parameters.
- **Required correction** Describe the repository contents (code, training data, model weights, instructions) and ensure it is publicly accessible.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Experimental details
- **Affected element** Cell lines and imaging
- **Evidence pointer** Experimental section "Cell culture"; location not provided
- **Issue** The text mentions DLD1 cells were sorted to generate clones, but the selection criteria for the specific clone used are not described. Imaging quantification methods (e.g., thresholding, segmentation algorithms) are not detailed.
- **Required correction** Provide details on clone selection criteria and imaging analysis pipeline, including software and parameters used.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Splicing assay
- **Evidence pointer** Results section "Identification of two novel candidates"; Figure 4C; location not provided
- **Issue** The splicing assay results are described qualitatively ("none of the five compounds show significant inhibitory effect") without reporting statistical test results, effect sizes, or variability.
- **Required correction** Report quantitative PCR data with statistical analysis (e.g., mean ± SEM, p-values) and specify the statistical test used.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Compound characterization
- **Affected element** A1-A5 compounds
- **Evidence pointer** Results section "Identification of two novel candidates"; location not provided
- **Issue** The chemical structures, purity confirmation methods, and solubility properties of compounds A1-A5 are not described beyond a statement of >95% purity.
- **Required correction** Provide chemical structures, source or synthesis details, and analytical characterization data.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction and Discussion
- **Evidence pointer** Introduction; Discussion; location not provided
- **Issue** The manuscript does not discuss alternative computational approaches for condensate modulator discovery or compare the GCN method to other virtual screening strategies in this context.
- **Required correction** Add a brief comparison to existing computational methods for condensate-targeting compound discovery and discuss the relative advantages and limitations.

## Risk / unsupported claims
- The claim that the GCN model "performs better than other machine learning based methods" is unsupported; no comparative data are presented in the text.
- The statement that the workflow "reduced the experimental and computing task by over 10,000 times" is not quantified or justified with specific calculations.
- The claim that A2 "might directly interact with TDP-43" is unsupported by direct binding evidence.
- The assertion that anisosomes are "recognized as an LLPS state proceeding the cytoplasmic aggregates" is presented without sufficient citation or experimental support in the provided text.
- The statement that "Doxycycline... has been safely used at a similar concentration for treating millions of patients over many decades" is not directly relevant to the experimental context and may be misleading without proper context.
- The claim that the identified compounds "share common molecular moieties that could potentially target the same biological pathways" is not supported by cheminformatic analysis in the text.