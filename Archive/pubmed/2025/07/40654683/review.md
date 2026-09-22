## Review setup
- **Input scope** Full manuscript text (preprint, bioRxiv)
- **Assessment boundary** Scientific content, methodology, claims, and evidence as presented in the provided text; no external validation or replication performed
- **Shared manuscript claim summary** The authors present DIRseq, a sequence-based method for predicting drug-interacting residues in intrinsically disordered proteins (IDPs), adapted from their earlier SeqDYN method. They claim that DIRseq predictions match well with drug-interacting residues identified by NMR chemical shift perturbation (CSP) and other methods across four IDP systems, and propose applications in virtual screening, fragment design for MD/NMR studies, and elucidation of a "sequence code" for IDP-drug binding.
- **Visible evidence base** Abstract, Introduction, Results (including four case studies with figures referenced), Discussion, Computational Methods; supplementary figures and tables referenced but not provided
- **Missing materials affecting confidence** Supplementary figures (S1–S4), tables (S1, S2), actual figure content, training data details for SeqDYN, full parameter sets, and raw CSP data; these are referenced but not available in the provided material

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting and potentially useful tool for predicting drug-interacting residues in IDPs from sequence alone. The adaptation of SeqDYN to DIRseq is logical and the four case studies provide a reasonable initial validation. However, the evidence base is limited to qualitative comparisons with CSP data, and several methodological details and quantitative performance metrics are not fully described in the provided text. The claim of a "sequence code" for IDP-drug binding is intriguing but not rigorously established. The work is likely of interest to the IDP and drug discovery communities, but the current evidence does not fully support all stated claims.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins as drug targets, computational biologists developing sequence-based prediction tools, medicinal chemists involved in virtual screening against IDPs, and NMR spectroscopists seeking complementary methods for identifying drug-interacting residues. The web server availability increases practical utility.
- **Major strengths** 1) Addresses a timely and important problem: IDPs are increasingly recognized as drug targets, yet tools for identifying drug-interacting residues are limited. 2) The method is fast and sequence-based, offering a practical complement to expensive and time-consuming experimental approaches. 3) The adaptation from SeqDYN is mechanistically motivated, linking intramolecular interaction propensities to intermolecular drug binding. 4) Validation across four diverse IDP systems with CSP data is a reasonable first step. 5) The web server implementation enhances accessibility and potential adoption.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** Originality: The concept of predicting drug-interacting residues in IDPs from sequence is novel, though it builds directly on the authors' prior SeqDYN work. Scientific importance: Potentially high for the IDP drug discovery field, but the impact depends on demonstrated accuracy and generalizability beyond the four test cases. Interdisciplinary readership: Relevant to structural biology, computational chemistry, and drug discovery; the writing is accessible but some domain-specific terms may limit broader readership. Technical soundness: The approach is plausible, but the provided evidence is insufficient to fully assess robustness; quantitative metrics and statistical significance are lacking. Readability for nonspecialists: Generally clear, but the Results section assumes familiarity with NMR CSP and IDP biology; figures are referenced but not visible in the provided material.
- **Recommendation posture** Supportive if technical concerns are resolved; the core idea is promising, but the current evidence does not fully establish the method's accuracy and generalizability.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "DIRseq predictions match well with drug-interacting residues identified by NMR chemical shift perturbation and other methods" (Abstract; Introduction; Results)
- **Evidence pointer** Figures 1–4; Supplementary Figures S2–S3; location not provided for specific data points
- **Concern** The claim of good agreement between DIRseq predictions and CSP-identified residues is supported only by qualitative descriptions and correlation coefficients (r = 0.82, 0.66, 0.67, 0.51). The actual CSP data, DIRseq prediction values, and the criteria for defining "drug-interacting" residues are not presented in the provided text. The correlation coefficients are reported without confidence intervals, p-values, or a description of how many residues were included in each calculation.
- **Why it matters** Without quantitative details and statistical assessment, the reader cannot evaluate the strength of the agreement or determine whether the correlations are meaningful or could arise by chance. The claim of "match well" is central to the manuscript's thesis.
- **Resolution test** Provide the full CSP datasets and DIRseq prediction values for all four IDPs, along with scatter plots, correlation coefficients with confidence intervals, and a clear definition of the threshold used to classify residues as drug-interacting. Report sensitivity and specificity or ROC curves.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological transparency
- **Claim pointer** "We transformed SeqDYN into DIRseq by implementing four changes" (Results, "Retooling of SeqDYN into DIRseq")
- **Evidence pointer** Results section, "Retooling of SeqDYN into DIRseq"; Supplementary Figure S1; location not provided
- **Concern** The four changes to convert SeqDYN to DIRseq are described qualitatively (e.g., "reassigned four q parameters," "increased the b value"), but the specific values of the modified parameters, the rationale for each change, and the criteria for choosing them are not provided. The original SeqDYN training procedure and data are referenced but not described in sufficient detail.
- **Why it matters** The method's reproducibility depends on a complete specification of all parameters and the logic behind their adjustment. Without this, other researchers cannot implement or test DIRseq independently, and the risk of overfitting to the four test systems cannot be assessed.
- **Resolution test** Provide a complete table of all 20 q parameters (original and modified), the b value, and the sigmoid parameters s1 and s2, along with a step-by-step description of the retooling process and the rationale for each change.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability
- **Claim pointer** "DIRseq is available as a web server... and has many applications, such as virtual screening against IDPs and designing IDP fragments for in-depth NMR and MD studies" (Abstract; Discussion)
- **Evidence pointer** Discussion section; location not provided
- **Concern** The manuscript claims broad applicability of DIRseq, but validation is limited to four IDP systems with a narrow range of drug molecular weights (360 ± 130 Da). The authors acknowledge this limitation but do not provide evidence that DIRseq would perform well for IDPs with different sequence compositions, lengths, or for drugs with significantly different sizes or chemical properties.
- **Why it matters** The stated applications (virtual screening, fragment design) assume that DIRseq predictions are reliable across diverse IDP-drug systems. Without broader validation, these claims are speculative and could mislead users.
- **Resolution test** Test DIRseq on additional IDP-drug systems with diverse sequence features and drug properties, or clearly state the current limitations and avoid overgeneralized claims in the abstract and discussion.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Comparative benchmarking
- **Claim pointer** "DIRseq, a fast method for predicting drug-interacting residues from the amino-acid sequence" (Abstract); "a complement to NMR CSP and MD simulations" (Introduction)
- **Evidence pointer** Introduction; Results; location not provided
- **Concern** The manuscript does not compare DIRseq's performance against any existing sequence-based prediction methods or against a null model (e.g., random prediction, sequence composition-based baseline). The claim that DIRseq is a useful complement to CSP and MD is not supported by a quantitative comparison of accuracy, speed, or cost relative to these methods.
- **Why it matters** Without benchmarking, the reader cannot assess whether DIRseq offers a genuine advantage over existing tools or approaches. The claim of being a "complement" implies added value, which should be demonstrated.
- **Resolution test** Compare DIRseq predictions against at least one existing sequence-based predictor (if available) and against a simple baseline (e.g., aromatic residue frequency). Report runtime and accuracy metrics for all methods on the same datasets.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states "All residues contribute to the propensity of a particular residue to be drug-interacting" without explaining the mechanism or the meaning of "contribute" in this context. This is potentially confusing for readers unfamiliar with the SeqDYN framework.
- **Required correction** Briefly clarify in the abstract that the method uses a weighted sum of contributions from all residues, with weights depending on amino acid type and sequence distance.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results, "Detailed assessment of DIRseq on four IDPs"
- **Evidence pointer** Results section; Figures 1–2; location not provided
- **Issue** The text describes "drug-interacting residues" identified by CSP and DIRseq, but the exact criteria for defining these residues (e.g., CSP threshold, DIRseq P-value threshold) are only partially described. The threshold for CSP is mentioned as m+1.5 SD, but the DIRseq threshold is only implied as P≥50.
- **Required correction** Explicitly state the DIRseq P-value threshold used for classification and whether the same threshold was applied across all four IDPs.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Results, "Dependences of DIRseq prediction accuracies on model parameters"
- **Evidence pointer** Results section; Table S2; location not provided
- **Issue** The performance metrics (r sum, TP – FP) are reported as sums across the four IDPs, but individual values for each IDP are not provided in the text. This makes it difficult to assess whether performance is consistent or driven by one system.
- **Required correction** Report the individual correlation coefficients and TP – FP values for each of the four IDPs in the main text or in Table S2.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Discussion
- **Evidence pointer** Discussion; location not provided
- **Issue** The term "sequence code" is used to describe the relationship between sequence and drug-binding propensity. This is a strong claim that implies a deterministic mapping, which is not demonstrated.
- **Required correction** Soften the language to "sequence-based determinants" or "sequence features" to avoid overinterpretation.

## Risk / unsupported claims
- The claim that DIRseq predictions "match well" with CSP data is not quantitatively substantiated in the provided text (correlation coefficients reported without statistical context).
- The claim that DIRseq has "many applications" including virtual screening and fragment design is speculative, as no demonstration of these applications is provided.
- The claim of a "sequence code" for IDP-drug binding is not supported by the evidence presented.
- The performance of DIRseq relative to existing methods or baselines is not assessed.
- The generalizability of DIRseq beyond the four test systems is not established.
- The specific parameter changes from SeqDYN to DIRseq are not fully described, limiting reproducibility.