## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods, conclusions) as provided
- **Assessment boundary** Scientific content, methodological soundness, data interpretation, and claims as presented in the supplied text; no external validation or replication attempted
- **Shared manuscript claim summary** The authors propose a combined empirical and physics-based model (MCMB) that uses molecular dynamics-derived protection factors and intrinsic hydrogen/deuterium exchange rates to generate a calibration curve relating in-droplet HDX-MS reactivity to peptide structural flexibility and bias, applied to five peptides including the disease-relevant Nt17 fragment of huntingtin.
- **Visible evidence base** Main text figures (Figures 1, 2, 3, 4), tables (Tables 1, 2), supplementary figures and tables referenced (Figures S1–S15, Tables S1–S4), equations (eqs 1–6), and methods descriptions
- **Missing materials affecting confidence** Raw mass spectra, detailed HDX calculation derivations, MD force field validation data, convergence metrics for MD trajectories, statistical error analysis for experimental replicates, and full supplementary information were not available for review

## Reviewer
- **Overall assessment** This manuscript presents a novel integration of in-droplet HDX-MS with MD simulations to derive a structure-to-reactivity calibration curve for disordered peptides. The concept is timely and potentially valuable for high-throughput structural screening of intrinsically disordered regions. However, the current evidence base has several gaps that limit confidence in the central claims. The model's predictive power rests on a small peptide cohort (n=5), and the statistical treatment of experimental and computational uncertainties is insufficiently detailed. The distinction between the proposed MCMB model and prior approaches needs clearer articulation. The structural interpretations for Nt17, while intriguing, require additional experimental validation. The manuscript would benefit from more rigorous error analysis, expanded validation, and clearer presentation of the model's limitations.
- **Who would be interested in the results, and why** Researchers in structural biology, biophysics, and mass spectrometry, particularly those studying intrinsically disordered proteins and their role in disease. The potential for high-throughput screening of drug candidates targeting IDRs would interest pharmaceutical scientists. Methodologists developing HDX-MS approaches and computational chemists using MD simulations for reactivity prediction would also find value.
- **Major strengths** 1) Novel combination of in-droplet HDX-MS with MD-derived protection factors to create a calibration approach; 2) Use of a disease-relevant peptide (Nt17) with potential translational relevance; 3) Systematic treatment of side-chain exchange contributions using amino acid standards; 4) Clear presentation of model development with multiple comparison metrics (R², SS_res, % error); 5) Practical advantages of the VSSI platform for future high-throughput applications.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Statistical rigor and uncertainty quantification
  - **Claim pointer** The manuscript claims a "strong correlation" (R² ~ 0.98) between experimental and theoretical % BB exchange using the MCMB model, implying predictive utility.
  - **Evidence pointer** Figure 2C, Table 2, Results section "Combined Empirical and Physics-Based Model"
  - **Concern** The correlation is based on only five peptides, which is a very small sample size for establishing a calibration curve. No confidence intervals, prediction intervals, or cross-validation are reported. The R² value, while high, may be overly optimistic given the limited data points and potential for overfitting with multiple adjustable parameters (SASA threshold, HB criteria, kint scaling). The manuscript does not report uncertainties in the experimental % BB values or how these propagate through the model.
  - **Why it matters** Without proper uncertainty quantification and validation on independent data, the claimed predictive capability cannot be reliably assessed. A calibration curve with n=5 and no error bars cannot support the strong claims of predictive utility for high-throughput screening.
  - **Resolution test** Provide confidence intervals for the regression parameters, perform leave-one-out cross-validation, report experimental uncertainties for each peptide's % BB value, and ideally validate on at least 2–3 additional peptides not used in model development.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Model validation and generalizability
  - **Claim pointer** The manuscript states the MCMB model "well accounts for the HDX behavior of the peptides of such diverse structural flexibility" and suggests it can be extended to larger proteins and used for predicting IDR structural flexibility and bias.
  - **Evidence pointer** Discussion section "IDP/IDR Structure Determination", Conclusions
  - **Concern** The model is developed and tested on the same five peptides, with no independent validation set. The peptides, while varied, represent a limited sequence space and do not include larger proteins or IDRs with known complex structural features. The claim that the model can be extended to larger proteins is speculative without demonstration. The manuscript acknowledges this limitation but does not provide a clear pathway or preliminary evidence for scalability.
  - **Why it matters** Generalizability is central to the manuscript's stated future applications. Without independent validation, the model's utility beyond the specific peptides studied remains unproven, undermining the broader claims of predictive capability for IDR structural characterization.
  - **Resolution test** Validate the model on at least 2–3 additional peptides or protein fragments with known structural properties not used in model development. Provide a clear discussion of the sequence and structural space over which the model is expected to be valid.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Mechanistic interpretation of Nt17 behavior
  - **Claim pointer** The manuscript states that Nt17 exhibits "significant in-droplet HDX protection" and that this arises from "rapid helix formation/deformation across the mid region," suggesting a structural bias toward α-helical conformation.
  - **Evidence pointer** Figure 4, Results section "Structure and Dynamics for a Disease-Relevant Peptide", Discussion
  - **Concern** The interpretation that Nt17's reduced HDX is due to transient helix formation is plausible but not directly demonstrated. The MD simulations show helical propensity, but the link between simulated conformational preferences and experimental HDX protection is indirect. Alternative explanations, such as aggregation, intramolecular interactions not captured by the model, or differential side-chain contributions, are not fully explored. The claim that this represents "structural bias" toward α-helix upon binding is speculative without binding experiments.
  - **Why it matters** The Nt17 result is a key demonstration of the method's potential for disease-relevant peptides. Overinterpretation of the structural basis for HDX protection could mislead future applications and undermine confidence in the approach.
  - **Resolution test** Provide additional experimental evidence, such as circular dichroism or NMR under similar conditions, to support the helical propensity interpretation. Alternatively, temper the claims to reflect the indirect nature of the evidence.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Solution-phase exchange assumption
  - **Claim pointer** The manuscript asserts that "gas-phase HDX not substantially alter ion deuterium content" and that reactions occur "primarily in solution," citing prior studies.
  - **Evidence pointer** Discussion section "Evidence for a Solution Exchange Process"
  - **Concern** The evidence for solution-phase dominance is indirect and based on prior work with different analytes. The current study does not include control experiments to assess gas-phase exchange contributions for the specific peptides studied. The manuscript acknowledges "some gas-phase HDX may occur" but does not quantify this or assess its impact on the model.
  - **Why it matters** If gas-phase exchange contributes significantly, the experimental % BB values would not reflect solution-phase structure, invalidating the correlation with MD-derived solution-phase protection factors.
  - **Resolution test** Include control experiments, such as varying the distance between the D2O and analyte emitters or using non-exchangeable analogs, to directly assess gas-phase contributions for the studied peptides.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity of model description
  - **Affected element** Methods section "MD Simulations", Equations 3–5
  - **Evidence pointer** Equations 3–5, Methods section
  - **Issue** The derivation of protection factors from MD simulations is described briefly. The exact criteria for defining open and closed states, the treatment of multiple conformations, and the statistical convergence of the τ and f values are not fully specified.
  - **Required correction** Provide a more detailed description of the MD analysis pipeline, including how open/closed states are assigned, how many frames are used, and how uncertainties in the protection factors are estimated.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Data presentation
  - **Affected element** Figure 2, Table 2
  - **Evidence pointer** Figure 2B,C, Table 2
  - **Issue** The figures and table present correlation statistics but do not show individual data points with error bars. The reader cannot assess the scatter or the influence of individual peptides on the regression.
  - **Required correction** Include error bars on all data points in Figure 2 and report individual peptide values in Table 2 with associated uncertainties.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Terminology precision
  - **Affected element** Abstract, Introduction, Discussion
  - **Evidence pointer** Abstract, Introduction, Discussion
  - **Issue** The term "structural bias" is used to describe the propensity to form secondary structure elements, but this is not formally defined. The distinction between "flexibility" and "bias" could be clearer.
  - **Required correction** Define "structural bias" explicitly and explain how it differs from flexibility in the context of the model.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Literature context
  - **Affected element** Introduction, Discussion
  - **Evidence pointer** Introduction, Discussion
  - **Issue** The manuscript cites prior HDX-MS and MD studies but does not clearly position the novelty of the combined approach relative to existing methods for IDP characterization.
  - **Required correction** Add a brief comparison with existing HDX-MS approaches for IDPs and explicitly state what is new about the MCMB model.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methods section "Data Availability"
  - **Evidence pointer** Methods section, Supplementary Material
  - **Issue** No statement on data availability or code availability is provided. The custom scripts and analysis pipelines are not described in sufficient detail for reproduction.
  - **Required correction** Add a data and code availability statement, and consider depositing the analysis scripts in a public repository.

## Technical failings that need to be addressed before the case is established
- R1-M1 (statistical rigor) and R1-M2 (model validation) are blocking concerns. The small sample size and lack of independent validation mean the central claim of a predictive calibration curve is not established from the provided evidence. The absence of uncertainty quantification further weakens the case.

## Assessment against Nature-style criteria
- **Originality** Moderate to high. The combination of in-droplet HDX-MS with MD-derived protection factors in a calibration framework is a novel contribution, though individual components are established.
- **Scientific importance** Moderate. The potential for high-throughput IDR structural screening is significant, but the current demonstration is limited to five peptides and lacks validation.
- **Interdisciplinary readership** Moderate. The work bridges mass spectrometry, computational chemistry, and structural biology, which could attract a broad audience if the claims are substantiated.
- **Technical soundness** Currently insufficient. The small sample size, lack of error analysis, and indirect validation of key assumptions (solution-phase exchange, structural interpretation) undermine technical confidence.
- **Readability for nonspecialists** Good. The manuscript is generally well-written and accessible, with clear explanations of the model and its motivation.

## Recommendation posture
Currently not established from the provided evidence. The manuscript presents a promising approach, but the blocking concerns regarding statistical rigor and model validation must be addressed before the central claims can be accepted. A revised version with expanded validation, proper uncertainty quantification, and tempered claims could be reconsidered.

## Risk / unsupported claims
- The claim that MCMB provides a "strong correlation" (R² ~ 0.98) is unsupported due to the small sample size and lack of error bars.
- The assertion that Nt17's HDX protection arises from "rapid helix formation/deformation" is not directly demonstrated and is speculative.
- The statement that the model can be extended to larger proteins is unsupported by any preliminary evidence.
- The assumption that gas-phase HDX does not substantially alter results is not validated for the specific peptides studied.
- The claim that the approach could enable high-throughput screening of IDR structural changes is speculative and not demonstrated.