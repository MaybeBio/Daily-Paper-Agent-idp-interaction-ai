## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, data availability, author contributions, funding, conflict of interest, supplementary material link)
- **Assessment boundary** Scientific content, methodological soundness, evidence quality, and internal consistency of the reported findings. No assessment of editorial fit or journal-specific policy.
- **Shared manuscript claim summary** The authors propose that Ubiquitin Interacting Motifs (UIMs) exist in a structural duality, populating both stable helical conformations and disordered states. Using molecular dynamics simulations (REMD and well-tempered metadynamics) with multiple force fields, combined with NMR chemical shift analysis, they characterize the C-terminal UIM3 of ataxin-3 (AT-3306-361) as predominantly disordered with partial helical propensity. They extend this observation to other UIMs via bioinformatic analysis of publicly available NMR data, and propose that disordered UIMs constitute a broader class with functional implications for binding promiscuity.
- **Visible evidence base** Methods descriptions for bioinformatic prediction, REMD and WT-metaD simulation protocols, force field choices, NMR spectroscopy of AT-3182-291, secondary structure propensity prediction from chemical shifts, helical wheel projections. Results sections describing conformational ensembles, helical content estimates, bound-like conformations, and comparative analysis of UIMs. Figures referenced (Figures 1-7, Supplementary Figures S1-S4, Supplementary Text S5).
- **Missing materials affecting confidence** Figures and supplementary materials not provided. Specific numerical data (e.g., exact helical populations, RMSD distributions, free energy values) only described qualitatively. Simulation convergence metrics not fully reported. Peptide array experimental details and raw results not shown. The GitHub and OSF repositories were not accessed.

## Reviewer

### Overall assessment
The manuscript addresses a timely and interesting question regarding the structural heterogeneity of UIMs, challenging the traditional view of these motifs as constitutively helical. The combination of enhanced-sampling simulations with NMR-derived chemical shift data is appropriate and potentially powerful. However, the evidence presented in the text is largely qualitative, and key quantitative results are not shown in the provided material. The claim of a "new class of disordered UIMs" rests on a small number of examples and a sequence-based search whose statistical rigor is not fully described. The functional implications, while plausible, are speculative and not directly tested. The manuscript would benefit from clearer presentation of quantitative data, additional validation of the bioinformatic search, and a more cautious framing of the generalizability of the findings.

### Who would be interested in the results, and why
Researchers studying ubiquitin signaling, deubiquitinases, intrinsically disordered proteins, and protein-protein interaction motifs would find this work relevant. The concept that a canonical helical interaction motif can be functionally disordered in its free state has implications for understanding binding mechanisms (conformational selection vs. induced fit), for predicting interaction partners from sequence, and for the design of ubiquitin-pathway inhibitors. The methodological approach, combining enhanced-sampling MD with NMR validation, will also interest computational biophysicists working on disordered proteins.

### Major strengths
1. The central question is well-motivated and addresses a genuine gap in understanding UIM structural behavior in the unbound state.
2. The combination of multiple enhanced-sampling methods (REMD and WT-metaD) with multiple force fields is a rigorous approach to assess method-dependence of conclusions.
3. Validation of simulations against experimental NMR chemical shifts provides an important check on the computational results.
4. The extension from a single case study (AT-3 UIM3) to a broader survey of UIMs using public NMR data adds generalizability to the claim.
5. The identification of specific sequence features (beta-branched residues) that may correlate with disorder propensity is a testable hypothesis.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "We show that UIMs feature both helical and intrinsically disordered conformations" and "AT-3306-361 is characterized by a disordered ensemble, which is better described by CHARMM22*2 among the force fields tested"
- **Evidence pointer** Results sections "Conformational Ensemble of AT-3306-361 in Solution" and "Low Structural Propensity and Heterogeneous Helical Formation"; Figures 2-4
- **Concern** The quantitative basis for the central claim is not presented in the text. Helical content values are given as approximate percentages for REMD simulations, but no error estimates, convergence metrics, or statistical comparisons between force fields are provided. The WT-metaD results are described qualitatively ("more disordered conformations") without numerical free energy differences or population estimates. The claim that CHARMM22*2 "better describes" the ensemble is based on comparison to NMR chemical shifts, but the actual chi-square values are only described as "low" without showing the comparison or the range of values across force fields.
- **Why it matters** The central conclusion that UIM3 is predominantly disordered depends entirely on the quantitative reliability of the simulation ensembles and their validation against experiment. Without numerical data, error bars, and convergence assessment, the reader cannot evaluate whether the observed differences between force fields are significant or whether the simulations have adequately sampled the conformational space. The choice of CHARMM22*2 as the "best" force field is a critical methodological decision that must be transparently justified.
- **Resolution test** Provide a table or figure showing: (a) helical population estimates with standard errors for each force field and method; (b) convergence metrics (e.g., block averaging, autocorrelation times) for the helical fraction; (c) the reduced chi-square values for each force field against experimental chemical shifts, with a clear description of how the comparison was performed (which nuclei, which residues, how many data points); (d) free energy profiles from WT-metaD with error estimates.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability of claims
- **Claim pointer** "Disordered UIMs can provide versatility and new functions to the client proteins" and "disordered UIM could be a common class of SLiMs"
- **Evidence pointer** Results section "Disordered UIMs With Low Helical Propensity: A More General Class of UIMs"; Figure 7; Supplementary Figure S3; Supplementary Text S5
- **Concern** The generalization from AT-3 UIM3 to a broader class of disordered UIMs is based on (i) delta-2D predictions from chemical shifts for a small number of UIMs, and (ii) a regular expression search against Pfam that identified 1,614 hits. The delta-2D analysis is only shown as average helix populations, without per-residue profiles or uncertainty estimates. The regular expression search is described with a single comparison to a randomized dataset, but the statistical significance, false discovery rate, and biological validation of the identified candidates are not reported. The claim that disordered UIMs are "a common class" requires a more systematic and statistically rigorous analysis.
- **Why it matters** The title and abstract emphasize the "duality" and the existence of a "new class" of disordered UIMs. If the evidence for generalizability is weak, the manuscript overreaches beyond its data. The functional implications (versatility, promiscuity) are presented as consequences of this class, but no functional experiments are shown to support these claims.
- **Resolution test** (a) Show per-residue delta-2D profiles for all UIMs analyzed, with confidence intervals; (b) provide a more rigorous statistical framework for the motif search, including multiple testing correction, comparison to appropriate negative controls, and validation of a subset of predicted disordered UIMs by an independent method (e.g., CD spectroscopy, additional NMR, or orthogonal prediction algorithms); (c) either add functional data (e.g., binding assays comparing helical vs. disordered UIMs) or temper the functional claims to clearly speculative statements.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Methodological transparency
- **Claim pointer** "We used two different methods to enhance the sampling of the MD simulations based on temperature exchange or bias along with selected collective variables"
- **Evidence pointer** Materials and Methods sections "Replica-Exchange Molecular Dynamics Simulations" and "Well-Tempered-Metadynamics Simulations"
- **Concern** The description of the WT-metaD setup is incomplete. The collective variables are named (C-alpha radius of gyration and "alphabeta"), but the specific definition of the alphabeta CV is only briefly described in the Results. Key parameters such as the width of the Gaussians, the deposition stride, the bias factor (stated as 4), and the total simulation time are mentioned, but convergence criteria for the free energy surface are not described. For REMD, the number of replicas (64) and temperature range (299-360 K) are given, but the temperature distribution, exchange acceptance rates, and total sampling per replica are not reported. The choice of starting structure (modeled as a helix) and its potential bias on the results is acknowledged but not systematically addressed.
- **Why it matters** Reproducibility is a core requirement for computational studies. Without complete methodological details, other groups cannot replicate the simulations or assess the quality of the sampling. The potential bias from the helical starting structure is a particular concern for the REMD simulations, where the authors themselves note limited sampling.
- **Resolution test** Provide complete simulation parameters in the main text or supplementary material, including: (a) the full definition of the alphabee CV with equations; (b) convergence metrics for the free energy surfaces (e.g., block analysis, time evolution of the deposited bias); (c) exchange acceptance rates for REMD; (d) a discussion of how the starting structure bias was assessed (e.g., additional simulations from extended conformations).

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Experimental validation
- **Claim pointer** "a peptide SPOT arrays in which we studied the interaction of some representative UIMs with recombinant yeast ubiquitin shows that both disordered UIMs (AT-3 UIM3 and USP25 UIM1 and 2) and helical UIMs (STAM1, STAM2 and, AT-3 UIM1) interact with ubiquitin"
- **Evidence pointer** Results section "Disordered UIMs With Low Helical Propensity: A More General Class of UIMs"; Supplementary Figure S4
- **Concern** The peptide array experiment is mentioned in a single sentence with no methodological detail. The number of replicates, the peptide concentrations, the ubiquitin concentration, the detection method, and the quantification of binding are not described. The conclusion that "a disordered UIM is not a barrier to bind ubiquitin" is based on this single, under-described experiment.
- **Why it matters** This is the only direct experimental evidence linking the structural findings to function. If the experiment is not rigorously described and quantified, the functional claim is not supported. The statement that disordered UIMs bind ubiquitin is central to the argument that disorder does not preclude function.
- **Resolution test** Provide a full description of the peptide array experiment in the Methods, including: (a) peptide sequences and lengths; (b) synthesis and quality control; (c) binding conditions and washes; (d) detection and quantification method; (e) number of independent replicates; (f) appropriate positive and negative controls. Show the raw data and quantification in the main text or supplementary material.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of writing
- **Affected element** Abstract, last sentence
- **Evidence pointer** Abstract
- **Issue** The sentence "Disordered UIMs can provide versatility and new functions to the client proteins, opening new directions for research on their interactome" is vague and not directly supported by the data presented. The term "versatility" is not defined, and "new functions" are not demonstrated.
- **Required correction** Rephrase to state what is actually shown, e.g., "Our results suggest that some UIMs are partially disordered in their free state, which may have implications for their binding specificity and partner selection."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Internal consistency
- **Affected element** Results section "Low Structural Propensity and Heterogeneous Helical Formation"
- **Evidence pointer** Results, first paragraph
- **Issue** The text states "The REMD simulations with ff03w and ff03ws showed higher helical content for UIM3 (approximately 60% and 56%, respectively) than with CHARMM22*1, and CHARMM22*2 (approximately 31% and 25%, respectively)." However, the subsequent sentence states "In the case of CHARMM22*2 simulation, we observed a more disordered ensemble for UIM3, with helical content < 20% in the region Q341-L348." The relationship between the overall helical content (25%) and the region-specific value (<20%) is not clearly explained.
- **Required correction** Clarify whether the 25% refers to the entire UIM3 region or a different definition, and explain the relationship between the overall and region-specific values.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Referencing
- **Affected element** Introduction, paragraph 2
- **Evidence pointer** Introduction
- **Issue** The statement "Some functional motifs of proteins that were traditionally defined as helical elements have been recently reclassified as disordered SLiMs, such as the Bcl-2 Homology 3 motifs" is presented without a citation in the provided text.
- **Required correction** Add the appropriate reference for the BH3 motif reclassification.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Results section "Bound-Like Conformations in the Unbound AT-3306-361 Ensemble in Solution"
- **Evidence pointer** Results, Figure 5 and Supplementary Figure S1
- **Issue** The text describes "partially folded states of UIM3 (around 3 Å of RMSD)" and states that these account for "approximately 20% of the structures from the entire WT-MetaD." The threshold for defining "partially folded" and the method for calculating this percentage are not described.
- **Required correction** Define the criteria for classifying a conformation as "partially folded" and describe how the 20% figure was calculated.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results section "Disordered UIMs With Low Helical Propensity: A More General Class of UIMs"
- **Evidence pointer** Results, Supplementary Figure S3
- **Issue** The delta-2D predictions are described as showing "high helical content" or "low helical content" based on average values, but no statistical comparison (e.g., confidence intervals, hypothesis tests) is provided to support the classification of UIMs into these categories.
- **Required correction** Provide statistical measures of uncertainty for the delta-2D predictions and describe the criteria for classifying UIMs as high or low helical content.

### Technical failings that need to be addressed before the case is established
1. Quantitative data for helical populations, free energy differences, and chemical shift validation are not presented (R1-M1).
2. The statistical basis for the generalizability claim (disordered UIM class) is not established (R1-M2).
3. The peptide array experiment is under-described and not quantified (R1-M4).
4. Simulation convergence and starting structure bias are not adequately addressed (R1-M3).

### Assessment against Nature-style criteria
- **Originality** The concept of structural duality in UIMs, with some members being intrinsically disordered, is a novel contribution that challenges the prevailing view of these motifs as constitutively helical. The idea that a canonical interaction motif can be functionally disordered is not entirely new (e.g., BH3 motifs), but its application to UIMs is original.
- **Scientific importance** The findings have potential implications for understanding ubiquitin signaling, deubiquitinase function, and the design of interaction inhibitors. However, the importance is currently limited by the lack of functional validation and the small number of experimentally characterized examples.
- **Interdisciplinary readership** The work bridges structural biology, computational biophysics, and ubiquitin signaling, and would appeal to researchers in these areas. The broader cell biology community may also be interested if the functional implications are more firmly established.
- **Technical soundness** The methodological approach is appropriate in principle, but the current presentation lacks the quantitative rigor and transparency required to fully assess technical soundness. The simulation protocols are described, but convergence and validation data are missing. The NMR analysis is described but not shown in sufficient detail.
- **Readability for nonspecialists** The manuscript is generally well-written and accessible. The abstract and introduction are clear. However, some technical sections (e.g., the description of the alphabeta CV) may be challenging for nonspecialists. The discussion is somewhat speculative and could be more tightly linked to the data.

### Recommendation posture
Supportive if technical concerns are resolved. The central question is interesting and the approach is appropriate, but the current evidence is not sufficient to establish the main claims. The authors must provide quantitative data, statistical rigor, and a more complete description of the experimental validation before the case for a "new class of disordered UIMs" can be considered established.

## Risk / unsupported claims
1. The claim that "UIMs feature both helical and intrinsically disordered conformations" as a general property is not quantitatively supported by the data shown.
2. The claim that "disordered UIMs can provide versatility and new functions" is speculative and not directly tested.
3. The claim that "disordered UIM could be a common class of SLiMs" is based on a search whose statistical significance is not established.
4. The statement that "a disordered UIM is not a barrier to bind ubiquitin" is based on a single, under-described peptide array experiment.
5. The suggestion that "a combination of conformational selection and folding upon binding could be in place for UIM3" is a plausible hypothesis but is not tested in this work.
6. The claim that "the location of suboptimal residues... could play a role in gearing the low propensity of UIMs to populate stable helical conformations" is a correlative observation without direct experimental or computational validation.