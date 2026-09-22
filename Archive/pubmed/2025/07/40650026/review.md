## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodological soundness, and claims as presented in the provided text
- **Shared manuscript claim summary** The manuscript presents FINCHES, a computational framework for sequence-based prediction of intermolecular interactions in intrinsically disordered regions (IDRs), and compares it with existing computational methods including molecular dynamics, machine learning, and database-driven approaches.
- **Visible evidence base** Abstract, Introduction, sections on computational approaches, FINCHES methodology, comparative analyses, applications, limitations, and future directions. Tables 1-4 are referenced but not shown. Figures 1-14 are referenced but not shown.
- **Missing materials affecting confidence** Figures 1-14, Tables 1-4, equations in full form, validation datasets, code availability, and any primary data supporting the reported performance metrics

## Reviewer
- **Overall assessment** The manuscript provides a broad narrative review of computational methods for IDR interaction prediction, with FINCHES positioned as a novel analytical approach. However, the text reads more as a descriptive overview than a rigorous scientific paper establishing the validity and utility of FINCHES. Critical quantitative results are referenced but not presented, and the methodological details are insufficient to evaluate the framework's novelty or accuracy. The manuscript would benefit from substantial restructuring to present primary evidence rather than summary claims.

- **Who would be interested in the results, and why** Computational biologists studying protein-protein interactions, researchers working on intrinsically disordered proteins and phase separation, and scientists interested in rapid screening tools for variant analysis. The potential for proteome-scale analysis would appeal to those studying post-translational modification effects and evolutionary constraints on IDR sequences.

- **Major strengths** The manuscript covers a wide range of computational approaches and places them in context. The discussion of limitations is thoughtful and acknowledges the inherent challenges in modeling IDR interactions. The emphasis on speed and scalability for high-throughput applications addresses a genuine need in the field.

- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The manuscript claims FINCHES achieves a correlation coefficient of r = 0.91 for critical temperature prediction in FUS LCD systems and 87% accuracy for binary phase separation prediction.
  - **Evidence pointer** Section 12, Table 1, Table 3 (tables not provided)
  - **Concern** The central quantitative claims about FINCHES performance are presented as summary statements without accompanying data, methodology for benchmarking, or statistical analysis. The referenced tables are not included in the provided material, making it impossible to assess the validity of these performance metrics.
  - **Why it matters** The entire case for FINCHES as a useful tool rests on these performance numbers. Without access to the underlying data, comparison methodology, and statistical rigor, the claims cannot be verified or reproduced.
  - **Resolution test** Provide the full benchmarking data, including the datasets used, the comparison protocol, the statistical methods, and the raw results. Include confidence intervals and error analysis.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Methodological clarity
  - **Claim pointer** The manuscript states FINCHES integrates force field functions over relevant distance ranges to extract effective interaction strengths, using Mpipi-GG and CALVADOS2 force fields.
  - **Evidence pointer** Section 11, Figure 14 (figure not provided)
  - **Concern** The methodological description is insufficient to understand how FINCHES actually works. The integration procedure, the treatment of sequence context, the handling of electrostatic screening, and the derivation of the mean-field parameter are described only in general terms. No equations, algorithms, or pseudocode are provided.
  - **Why it matters** A computational framework must be described with sufficient detail for others to implement or at least understand the precise nature of the approximation. The current description does not allow this.
  - **Resolution test** Provide the full mathematical formulation, including the force field equations used, the integration limits, the treatment of sequence windows, and the algorithm pseudocode.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Novelty assessment
  - **Claim pointer** The manuscript describes FINCHES as a "groundbreaking" and "recently developed" framework but does not clearly establish what is novel relative to existing analytical approaches.
  - **Evidence pointer** Sections 1, 11
  - **Concern** The novelty of FINCHES is asserted but not demonstrated. The manuscript does not clearly articulate what specific advance FINCHES represents over existing analytical methods, nor does it provide a systematic comparison of the underlying physics with prior work.
  - **Why it matters** For a computational method paper, establishing novelty is essential. Without a clear statement of what is new and why it matters, the contribution is unclear.
  - **Resolution test** Provide a clear statement of the specific innovations in FINCHES relative to prior analytical approaches, with explicit comparisons to the closest existing methods.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Validation rigor
  - **Claim pointer** The manuscript claims FINCHES predictions agree with experimental observations across diverse systems, including FUS, TDP-43, DDX4, and p53.
  - **Evidence pointer** Section 12, Table 4 (table not provided)
  - **Concern** The validation cases are described narratively, but the quantitative comparison between predictions and experiments is not shown. For each system, the reader needs to see the predicted versus experimental values, the experimental methods used, and the uncertainty in both.
  - **Why it matters** Validation claims without data are assertions. The scientific community requires access to the actual comparison to judge whether the agreement is meaningful.
  - **Resolution test** Provide for each validation case the predicted values, the experimental values with error bars, the experimental technique used, and the statistical measure of agreement.

  - **Concern ID** R1-M5
  - **Severity** Major
  - **Blocking** No
  - **Axis** Comparative analysis
  - **Claim pointer** The manuscript compares FINCHES with molecular dynamics, machine learning, and database-driven approaches, claiming distinct advantages in speed and scalability.
  - **Evidence pointer** Sections 2-10, Tables 1-3 (tables not provided)
  - **Concern** The comparisons with other methods are qualitative and do not include systematic benchmarking on the same datasets. The claims about relative performance are not supported by head-to-head comparisons.
  - **Why it matters** A meaningful comparison requires identical test conditions, metrics, and datasets. Without this, the relative advantages claimed cannot be evaluated.
  - **Resolution test** Provide a systematic benchmark study where FINCHES and the comparison methods are evaluated on the same datasets using the same metrics.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Abstract
  - **Evidence pointer** Abstract
  - **Issue** The abstract describes FINCHES as "groundbreaking" without supporting evidence in the abstract itself.
  - **Required correction** Replace subjective descriptors with objective statements of what FINCHES does and its reported performance.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methodology
  - **Evidence pointer** Section 11
  - **Issue** No mention of code availability, software implementation, or input file formats.
  - **Required correction** Add a section on code and data availability, including where the software can be obtained and how to run it.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** References
  - **Evidence pointer** Throughout
  - **Issue** The manuscript cites many studies but does not provide a systematic comparison table of methods with their mathematical foundations as claimed in the abstract.
  - **Required correction** Either provide such a table or revise the abstract to reflect what is actually presented.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** Section 11.2
  - **Evidence pointer** Section 11.2
  - **Issue** The worked example for the charge weighting correction uses a fragment "KKKDDD" but the calculation shown is trivial and does not illustrate the method's utility.
  - **Required correction** Provide a more informative example that demonstrates how the correction changes predictions in a non-obvious way.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Scope
  - **Affected element** Section 10
  - **Evidence pointer** Section 10
  - **Issue** The section on computational assessment tools for interface prediction is not well integrated with the rest of the manuscript and reads as an add-on.
  - **Required correction** Either integrate this material more fully into the comparison framework or remove it.

## Risk / unsupported claims
- The claim that FINCHES achieves r = 0.91 for critical temperature prediction in FUS LCD systems is unsupported without the underlying data.
- The claim of 87% accuracy for binary phase separation prediction is unsupported without the benchmarking dataset and methodology.
- The claim that FINCHES is "groundbreaking" is subjective and not supported by the evidence presented.
- The claim that FINCHES can analyze all 19,702 human IDRs for phosphorylation effects in 3.2 hours is presented without details on the computational environment or the nature of the analysis.
- The claim that FINCHES predictions "provide molecular-level insights" into various biological processes is not substantiated with specific examples of new biological knowledge gained.
- The statement that FINCHES "successfully predicted experimental observations" for multiple systems is not supported by quantitative comparisons in the provided text.
- The claim that the framework "cannot predict the structured complexes formed by IDRs" is presented as a limitation but the basis for this claim is not explained.