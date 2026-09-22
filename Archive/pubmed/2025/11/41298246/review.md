## Review setup
- **Input scope** Full manuscript text (abstract, introduction, model, results, discussion) as provided
- **Assessment boundary** Scientific content, model development, experimental validation, and interpretation as presented in the provided text
- **Shared manuscript claim summary** The authors develop analytically tractable polymer models that account for charge patterning, counterion condensation, and dipolar interactions to predict salt-dependent intrachain distances in intrinsically disordered proteins, and validate these models against extensive single-molecule FRET data across 18 IDP sequences
- **Visible evidence base** Single-molecule FRET measurements on 16 linker IDRs and two longer IDPs (Stm, ProTα) across salt concentrations; model variants M0, M1, M2, M3; comparison with coarse-grained and atomistic simulations
- **Missing materials affecting confidence** Figures and tables referenced but not fully visible in the provided text; Supporting Information sections S1-S8 referenced but not provided; specific numerical values of fit parameters and error metrics only partially reported; details of the FRET data analysis procedures not fully described

## Reviewer
- **Overall assessment** This manuscript presents a substantial and rigorous effort to develop analytically tractable models for charge interactions in IDPs, validated against an impressive and carefully designed experimental dataset. The work addresses a fundamental and timely question in the field, and the authors' systematic approach to model selection and parameter reduction is commendable. The key advance is the demonstration that a minimal model with counterion condensation and dipolar interactions can quantitatively describe salt-dependent conformational behavior across diverse sequences. However, several technical aspects require clarification and strengthening before the case is fully established, particularly regarding the uniqueness of parameter fits, the treatment of dye effects, and the predictive power of the model for sequences outside the training set.

- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins, polymer physics, biophysics, and computational biology would be interested. The work provides a quantitative framework for understanding how sequence-encoded charge patterning and counterion condensation modulate IDP conformations, which has implications for understanding IDP function, phase separation, and interactions. The analytical nature of the model makes it accessible and potentially useful for high-throughput predictions and for interpreting experimental data in other laboratories.

- **Major strengths**
  1. The experimental dataset is extensive and thoughtfully designed, covering diverse sequence compositions, multiple labeling positions, two dye pairs, and a wide salt concentration range
  2. The theoretical framework is built on a physically motivated Hamiltonian and includes a systematic model reduction strategy, which is a rigorous approach to model selection
  3. The demonstration that counterion condensation is necessary to describe the data is an important and non-trivial finding
  4. The model's ability to predict intrachain distance maps and its internal consistency checks (e.g., similar effective charges across segments) strengthen the credibility of the approach
  5. The work addresses a long-standing question in polymer physics and extends it to heteropolymers, which broadens its impact

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that the model with counterion condensation (M1/M2) is required to describe the data, and that the minimal model is "near-predictive"
- **Evidence pointer** Results section, Figures 2-4, Tables 1-2
- **Concern** The manuscript does not provide sufficient information to assess whether the improved fit of M1/M2 over M0 could arise from overfitting. The model M1 has additional adjustable parameters (p, δ) compared to M0, and the authors do not report information criteria (e.g., AIC, BIC) or cross-validation results that would demonstrate that the added complexity is justified. Furthermore, the claim that M2 is "near-predictive" is based on a linear relationship between δ and low-salt end-to-end distance derived from the same dataset, which raises concerns about circularity.
- **Why it matters** The central conclusion of the paper is that counterion condensation is essential. If the improved fit is merely a consequence of additional free parameters, the conclusion would be weakened. The predictive claim of M2 is a key selling point, and its validation requires demonstration on data not used to establish the δ-⟨Ree2⟩ relationship.
- **Resolution test** The authors should report model comparison metrics that penalize complexity (e.g., AIC, BIC) for M0, M1, and M2. Additionally, they should perform a leave-one-out or holdout validation where the δ-⟨Ree2⟩ relationship is established on a subset of sequences and tested on the remaining ones. If the predictive performance of M2 is maintained under such validation, the claim would be substantially strengthened.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that the model can predict intrachain distance maps for any pair of residues, validated against FRET data for Stm and ProTα
- **Evidence pointer** Results section, Figure 6, Tables S4-S5
- **Concern** For Stm and ProTα, the authors fit p and δ for each protein and also fit ω2,i,j for each segment individually. This means that for each segment, there are multiple adjustable parameters, and the number of data points per segment (salt-dependent FRET measurements) may be limited. The manuscript does not report the number of salt concentrations per segment, the degrees of freedom in the fits, or the uncertainty in the fitted parameters. Without this information, it is difficult to assess whether the agreement between model and experiment is meaningful or could be achieved with any flexible model.
- **Why it matters** The validation of the model for intrachain distances is a key part of the paper. If the fits are underdetermined, the agreement with data does not provide strong evidence for the model's validity.
- **Resolution test** The authors should report the number of experimental data points per segment, the number of fitted parameters, and the resulting degrees of freedom. They should also provide confidence intervals or bootstrap estimates for the fitted parameters. If possible, they should demonstrate that the model can predict distances for segments not used in the fitting procedure.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The claim that the model provides "fundamental insight into the interactions underlying the conformational distributions of IDPs"
- **Evidence pointer** Discussion section
- **Concern** While the model is shown to describe the data well, the manuscript does not clearly articulate what new physical insight is gained beyond what was already known. The concept of counterion condensation in polyelectrolytes is well established, and the role of charge patterning in IDPs has been demonstrated in prior work. The specific quantitative predictions of the model (e.g., effective degrees of ionization as a function of sequence and salt) are interesting, but the manuscript does not discuss whether these predictions are testable by independent experimental methods (e.g., electrophoretic mobility, NMR, or direct ion binding measurements).
- **Why it matters** For a paper in a high-impact venue, the conceptual advance should be clearly articulated. If the model merely recapitulates known physics with a new formalism, the significance is limited.
- **Resolution test** The authors should explicitly state what new, testable predictions arise from their model that could not be made by existing approaches. They should also discuss how these predictions could be experimentally verified.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The claim that the model accounts for dye effects by modifying the sequence with the dye charge
- **Evidence pointer** Model section, Section S3
- **Concern** The treatment of dyes as a single bead with an effective charge is a significant simplification. The authors acknowledge this, but the manuscript does not provide a sensitivity analysis of how the results depend on the assumed dye charge or the placement of the dye bead. Given that dye effects are known to be important in FRET measurements of IDPs, and that the authors themselves note dye interactions as a potential explanation for discrepancies (e.g., for sNh-), a more thorough analysis is needed.
- **Why it matters** If the results are sensitive to the dye model, the conclusions about sequence-specific behavior could be artifacts of the dye treatment.
- **Resolution test** The authors should perform a sensitivity analysis by varying the dye charge and position within a reasonable range and assessing how the fitted parameters and model predictions change. They should also compare results with and without dye charge inclusion for a subset of sequences.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Model section, Equation 24
- **Evidence pointer** Results section, Figure 3
- **Issue** The linear relationship between δ and ⟨Ree2⟩ (Equation 24) is presented without discussion of its physical basis or its limitations. The authors state that this relationship is used to reduce model complexity, but the reader is left wondering why such a relationship should hold and whether it is expected to be universal.
- **Required correction** Add a brief discussion of the physical rationale for the δ-⟨Ree2⟩ correlation and its potential limitations. If possible, show the scatter of the data around the fitted line and discuss the outliers (e.g., sNh-, sPTBP) in more detail.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results section, comparison with simulations
- **Evidence pointer** Results section, Figure 5
- **Concern** The comparison of model-predicted distance maps with those from coarse-grained and atomistic simulations is described qualitatively ("compare well", "modest agreement", "clear deviations"). No quantitative metric is provided for these comparisons.
- **Required correction** Provide a quantitative measure of agreement (e.g., root-mean-square deviation between distance maps) and specify the criteria for "good", "modest", and "poor" agreement.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Readability
- **Affected element** Introduction and Results
- **Evidence pointer** Introduction, Results section
- **Issue** The manuscript uses several acronyms (IDP, IDR, FRET, SCD, SHD, SCDM, SHDM, SCDDM, SDDM) without a consolidated glossary. While most are defined at first use, the proliferation of acronyms makes the text difficult to follow for non-specialist readers.
- **Required correction** Consider adding a table of acronyms or reducing the number of acronyms used in the main text.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results section, model comparison
- **Evidence pointer** Tables 1-2
- **Issue** The comparison of models in Tables 1 and 2 is presented as a summary, but the specific metrics used (presumably chi-square values) are not defined in the main text. The reader is referred to Supporting Information, but the main text should be self-contained for the key results.
- **Required correction** Briefly define the metric used for model comparison in the main text and state the criteria for "better" or "worse" performance.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion of future directions is somewhat generic and does not clearly distinguish between what the model can and cannot do. For example, the statement that the model "will be of practical use in such predictions" is vague.
- **Required correction** Provide specific examples of predictions that the model can make and the types of systems or conditions where the model is expected to be most applicable or most limited.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Data availability
- **Evidence pointer** Data Availability Statement
- **Issue** The data availability statement indicates that data are available "upon reasonable request," which is less transparent than depositing data in a public repository. Given the emphasis on rigorous testing, the community would benefit from open access to the FRET data and model code.
- **Required correction** Consider depositing the experimental data and model code in a public repository (e.g., Zenodo, GitHub) and providing the accession details.

## Risk / unsupported claims
- The claim that the model is "near-predictive" (M2) is not fully supported without out-of-sample validation
- The claim that the model provides "fundamental insight" is not clearly substantiated with specific new physical predictions
- The treatment of dye effects as a single bead with effective charge is acknowledged as a simplification, but the sensitivity of results to this assumption is not assessed
- The comparison with simulation-derived distance maps is qualitative and lacks quantitative metrics
- The physical basis for the linear δ-⟨Ree2⟩ relationship (Equation 24) is not discussed
- The manuscript claims the model accounts for "charge patterning" but the specific contribution of patterning versus composition is not isolated in the analysis
- The statement that the model "can be used to predict detailed intrachain distance maps between all residues" is not demonstrated for arbitrary residue pairs; only a limited number of labeled positions were tested