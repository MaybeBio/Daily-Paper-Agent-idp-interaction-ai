## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodology, and conclusions as presented in the manuscript
- **Shared manuscript claim summary** The authors present a computational study using a Bayesian inference approach (MELD×MD) combined with atomistic simulations to investigate the binding ensembles of five peptides (p53 epitope, two inhibitors pdiq and ATSP-7041, and two alanine-based controls) to MDM2. They claim the method captures folding-upon-binding, differentiates binding preferences among peptides, and identifies helical propensity and interface interactions as key drivers of binding.
- **Visible evidence base** Abstract, Introduction, Results (Sections 2.1–2.5), Discussion, Materials and Methods (Sections 4.1–4.5), Conclusions, and references to figures and tables (figures not fully visible in text)
- **Missing materials affecting confidence** Figures and tables referenced (Figures 1–4, A1–A11, Tables 1–2) are not provided in the submitted text; quantitative data supporting claims (e.g., populations, RMSD values, free energy estimates) are only partially described; no convergence or error analysis details are given

## Reviewer
- **Overall assessment** The manuscript addresses a significant challenge in computational peptide drug design: modeling the binding of intrinsically disordered peptides that fold upon binding. The use of MELD×MD to integrate noisy experimental information with atomistic simulations is a novel and potentially powerful approach. The study design, including the choice of five peptides with appropriate controls, is thoughtful. However, the manuscript as presented has several critical gaps: the key figures and tables are not available for assessment, quantitative results are described qualitatively, and the central claim that the method "differentiates binding preferences" is not supported by statistical or quantitative evidence in the text. The work is promising but currently not fully established from the provided material.
- **Who would be interested in the results, and why** Computational biophysicists and chemists working on protein-peptide interactions, drug designers targeting protein-protein interactions (especially p53-MDM2), and method developers in enhanced sampling and Bayesian inference approaches. The work is relevant to those interested in intrinsically disordered proteins and folding-upon-binding mechanisms.
- **Major strengths** 
  1. Novel methodological combination: Integrating Bayesian inference (MELD×MD) with atomistic simulations to address a well-recognized challenge (folding-upon-binding of IDPs) is innovative and timely.
  2. Well-designed peptide panel: Including two known inhibitors, the native p53 epitope, and two alanine-based controls (one with and one without anchoring residues) provides a rigorous test of the method's discriminatory power.
  3. Physically meaningful decomposition: The separation of binding free energy into conformational and interaction components (ΔGbind = ΔGconformation + ΔGinteraction) provides a useful conceptual framework.
  4. Practical implications: The suggestion that helical propensity can be assessed via cheaper free-peptide simulations could accelerate peptide screening.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** "The method is able to capture the folding upon binding mechanism and differentiate binding preferences between the five peptides."
  - **Evidence pointer** Section 2.3, Figure 4, Table 2
  - **Concern** The central claim of differentiating binding preferences is supported only by qualitative descriptions of clustering and funnel plots. No quantitative metrics (e.g., populations of bound states, free energy differences, statistical uncertainties) are provided in the text. The referenced figures and tables are not available for verification.
  - **Why it matters** Without quantitative evidence, the reader cannot assess whether the observed differences between peptides are statistically significant or merely anecdotal. The claim of "differentiating binding preferences" is the core contribution of the work and must be rigorously supported.
  - **Resolution test** Provide quantitative data such as populations of the native-like bound cluster for each peptide, with error bars from replica exchange sampling; report free energy estimates (e.g., PMF along a binding coordinate) with uncertainties; make figures and tables available for inspection.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** "We ran 1 μs-long H,T-REMD simulations using OpenMM with the MELD plugin."
  - **Evidence pointer** Section 4.3
  - **Concern** The manuscript does not report convergence criteria for the replica exchange simulations. For a method claiming to sample binding/unbinding events, it is essential to demonstrate that the simulations have converged and that the observed ensembles are not biased by insufficient sampling or by the choice of restraints.
  - **Why it matters** Without convergence analysis, the ensembles presented may not be representative of the true equilibrium distribution, undermining all subsequent conclusions about binding preferences and mechanisms.
  - **Resolution test** Include convergence metrics such as replica exchange acceptance rates, time evolution of key observables (e.g., fraction of native contacts), and block error analysis for populations of interest. Show that results are robust to simulation length.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Reproducibility
  - **Claim pointer** "Parameters for the ATSP-7041 peptide are derived from the general amber force field (GAFF), deriving charges based on the AM1 model."
  - **Evidence pointer** Section 4.1
  - **Concern** The parametrization of the non-standard amino acids in ATSP-7041 is described only briefly. Details on how the stapled peptide was modeled (e.g., bond constraints, charge derivation procedure) are insufficient for reproduction.
  - **Why it matters** Reproducibility is a cornerstone of computational studies. Incomplete parametrization details prevent others from repeating the simulations and verifying the results.
  - **Resolution test** Provide full parametrization details, including the exact procedure for charge derivation, any modifications to the force field, and the structure of the stapled residue. Consider providing input files as supplementary material.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Validation
  - **Claim pointer** "The method successfully reproduces the binding of the two inhibitors and the p53 epitope, while showing that the two control peptides are unsuccessful binders."
  - **Evidence pointer** Section 2.3, Figure 4
  - **Concern** The claim of "successful reproduction" of binding is not validated against experimental data beyond qualitative agreement with known structures. No quantitative comparison (e.g., RMSD to crystal structures, binding affinity estimates) is provided.
  - **Why it matters** Without quantitative validation, the reader cannot distinguish between a method that genuinely captures the physics of binding and one that merely produces plausible-looking structures.
  - **Resolution test** Compare the most populated bound clusters to crystal structures (1ycr, 3jzs, 4n5t) with quantitative RMSD values. If possible, estimate binding free energies and compare to experimental values for the inhibitors.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Section 2.1
  - **Evidence pointer** Table 2
  - **Issue** The description of clustering results in Section 2.1 is vague ("many clusters with low populations"). Specific numbers would help the reader understand the degree of disorder.
  - **Required correction** Report the number of clusters, their populations, and the fraction of the ensemble in the top clusters for each peptide.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Section 2.5
  - **Evidence pointer** Figure A9
  - **Issue** The discussion of MDM2 conformational changes is brief and does not quantify the extent of opening/closing of the binding cavity.
  - **Required correction** Provide quantitative measures of cavity volume or key residue distances in apo vs. holo states, and how these change during simulations.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** Section 3
  - **Evidence pointer** location not provided
  - **Issue** The term "pre-bound state" is used but not precisely defined. It is unclear whether this refers to a kinetic intermediate or a thermodynamic state.
  - **Required correction** Define "pre-bound" operationally (e.g., by RMSD range or contact criteria) and clarify its physical meaning.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Presentation
  - **Affected element** Section 4.2
  - **Evidence pointer** location not provided
  - **Issue** The choice of implicit solvent (GBneck2) is justified for efficiency, but potential artifacts (e.g., over-stabilization of helices) are not discussed in the context of the results.
  - **Required correction** Add a brief discussion of known limitations of implicit solvent models for IDPs and how they might affect the conclusions.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Statistical rigor
  - **Affected element** Section 2.3
  - **Evidence pointer** Figure 4
  - **Issue** The funnel plots are described qualitatively. It is unclear how the "funneled nature" is quantified.
  - **Required correction** Define a quantitative metric for funneling (e.g., the slope of the free energy vs. RMSD profile) and report it for each peptide.

## Risk / unsupported claims
- The claim that MELD×MD "differentiates binding preferences between the five peptides" is unsupported without quantitative population or free energy data.
- The claim that the method "successfully reproduces the binding" of the inhibitors and p53 is not quantitatively validated against experimental structures.
- The statement that "the study shows the importance of capturing two driving forces to binding" (ΔGconformation and ΔGinteraction) is presented as a conclusion but is not directly demonstrated by the data shown.
- The assertion that "changing the intrinsic properties (e.g., helical propensity) can identify better binders" is an extrapolation that is not directly tested in this work.
- The claim that free-peptide simulations can assess helical propensity "at a lower computational cost" is reasonable but not demonstrated as a screening tool here.

## Assessment against Nature-style criteria
- **Originality**: High. The combination of Bayesian inference (MELD×MD) with atomistic simulations to study folding-upon-binding of IDP peptides is a novel methodological contribution. The conceptual decomposition of binding free energy into conformational and interaction terms is also a useful framing.
- **Scientific importance**: Moderate to high. The p53-MDM2 system is a well-studied and important cancer target. The challenge of modeling IDP binding is broadly relevant to drug design. However, the importance of the specific findings is diminished by the lack of quantitative validation and the absence of new biological or chemical insights beyond what is already known about this system.
- **Interdisciplinary readership**: Moderate. The work will appeal to computational chemists, biophysicists, and drug designers. The writing is accessible but assumes familiarity with enhanced sampling methods and Bayesian inference. The broader biological or clinical significance is not emphasized.
- **Technical soundness**: Currently not fully established. The methodological approach is sound in principle, but the lack of convergence analysis, quantitative results, and validation against experimental data prevents a full assessment of technical rigor.
- **Readability for nonspecialists**: Acceptable. The manuscript is generally well-written and the logic is clear. However, some sections (e.g., the description of MELD×MD) may be challenging for readers without a computational background. The abstract is accessible and conveys the main message effectively.

## Recommendation posture
Supportive if technical concerns are resolved. The manuscript presents a promising approach to a significant problem, and the study design is thoughtful. However, the current version lacks the quantitative evidence and technical details needed to fully establish the claims. If the authors can provide convergence analysis, quantitative comparisons to experimental data, and clearer statistical support for the differentiation of binding preferences, the work would be a valuable contribution to the field.