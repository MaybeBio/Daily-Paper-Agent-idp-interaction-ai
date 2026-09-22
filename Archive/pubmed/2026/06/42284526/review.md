## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as stated in the abstract; no access to methods, figures, tables, or supplementary information
- **Shared manuscript claim summary** The authors report that the 24-residue peptide p5, a selective inhibitor of the pathological CDK5-p25 complex, samples an intrinsically disordered ensemble in aqueous solution based on 350 ns REST2 molecular dynamics simulations with the CHARMM36m force field. Three dominant conformational states are identified by GMVAE clustering, with small free energy differences enabling rapid interconversion. The authors propose a coupled folding-and-binding mechanism for p5 upon CDK5 engagement and suggest the findings provide a structural framework for inhibitor design.
- **Visible evidence base** Abstract text only; no figures, tables, methods details, or supplementary materials provided
- **Missing materials affecting confidence** Full methods (simulation protocol, system setup, equilibration, convergence criteria), all figures and tables, GMVAE clustering details, free energy calculation methodology, temperature-dependent analysis details, force field validation, and any experimental validation data

## Reviewer
- **Overall assessment** The abstract presents a plausible computational study of a biologically relevant peptide inhibitor, with a clear question and a reasonable simulation approach. However, the evidence base available for review is limited to the abstract, which prevents verification of the central claims regarding conformational state identification, free energy differences, and the proposed mechanism. The conclusions are stated with confidence that exceeds what can be supported from the abstract alone, particularly regarding the "hallmarks of an intrinsically disordered peptide" and the "coupled folding-and-binding mechanism." The work is potentially of interest to the computational biophysics and neurodegeneration communities, but the case is not fully established from the provided material.
- **Who would be interested in the results, and why** Computational biophysicists studying intrinsically disordered proteins and peptide conformational ensembles; researchers investigating CDK5-p25 inhibition for Alzheimer's disease therapeutics; method developers interested in REST2 simulations and unsupervised clustering approaches for conformational analysis; structural biologists studying coupled folding-and-binding mechanisms.
- **Major strengths** The study addresses a clinically relevant target with a clear biological question. The use of REST2 enhanced sampling with a modern force field (CHARMM36m) is appropriate for disordered peptides. The application of GMVAE clustering to identify conformational states is a contemporary and potentially powerful analytical approach. The abstract explicitly reports free energy differences and temperature dependence, which are important for assessing ensemble robustness.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** "replica exchange with solute tempering (REST2) molecular dynamics simulations with explicit solvent were performed over 350 ns using the CHARMM36m force field to extensively characterize the conformational landscape of p5"
  - **Evidence pointer** Methods section, location not provided
  - **Concern** The abstract states 350 ns of simulation time, but it is unclear whether this refers to per-replica time, total aggregated time, or time per temperature replica in the REST2 scheme. For a 24-residue disordered peptide, 350 ns per replica may be insufficient to achieve converged sampling of the conformational ensemble, particularly for transitions between distinct states. The abstract provides no convergence analysis, no replica count, no temperature range, and no assessment of sampling adequacy.
  - **Why it matters** Without demonstrated convergence, the identification of three dominant states and the reported free energy differences cannot be considered reliable. Disordered peptides often require microsecond or longer timescales for adequate sampling, and the claim of "extensively characterize" is not supportable from the stated simulation length alone.
  - **Resolution test** Provide replica count, temperature range, per-replica simulation length, and convergence metrics such as block averaging, state population stability over time, or replica exchange acceptance rates. Show that the three identified states are stable across independent simulation segments.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** "Gaussian Mixture Variational Autoencoder (GMVAE) clustering identifies three dominant conformational states"
  - **Evidence pointer** Methods and Results sections, location not provided
  - **Concern** The abstract does not describe the input features used for GMVAE clustering, the number of clusters tested, the model selection criteria, or the validation of cluster assignments. It is unclear whether the three states are statistically robust or an artifact of the chosen clustering hyperparameters. The abstract also does not report the population fractions of each state, which are essential for interpreting the free energy differences.
  - **Why it matters** Unsupervised clustering results are highly sensitive to feature selection and model complexity. Without validation, the three-state description may not reflect the true conformational landscape. The subsequent free energy and mechanistic claims depend entirely on the validity of this clustering.
  - **Resolution test** Describe the GMVAE architecture, input features, number of clusters evaluated, and model selection metrics. Provide cluster populations with uncertainties and show that the three-state model is preferred over two or four states by objective criteria.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Scientific importance
  - **Claim pointer** "The absence of stable helical structure in the unbound state, combined with the peptide's backbone flexibility and transient beta-strand propensity, supports a coupled folding-and-binding mechanism upon CDK5 engagement"
  - **Evidence pointer** Results and Discussion sections, location not provided
  - **Concern** The abstract asserts a coupled folding-and-binding mechanism based solely on the unbound state ensemble. No data on the bound state, binding kinetics, or any experimental or computational evidence of induced fit or conformational selection is presented. The leap from "disordered in solution" to "folds upon binding" is a hypothesis, not a supported conclusion.
  - **Why it matters** The stated mechanism is a central claim of the abstract and is presented as a finding rather than a speculation. Overstating mechanistic conclusions from unbound-state simulations alone could mislead readers and overstate the therapeutic relevance of the work.
  - **Resolution test** Either soften the claim to a hypothesis or provide additional evidence such as bound-state simulations, binding free energy calculations, or experimental binding data that supports the folding-and-binding model.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness
  - **Claim pointer** "Temperature-dependent free energy profiles confirm that the low-energy conformational basin is robust across a wide temperature range, validating the physiological relevance of the sampled ensemble"
  - **Evidence pointer** Results section, location not provided
  - **Concern** The abstract does not specify the temperature range examined, the number of temperatures, or how the free energy profiles were computed from the REST2 simulations. The term "confirm" is strong and implies a level of certainty that requires detailed methodological support. It is also unclear whether the temperature dependence was analyzed using reweighting procedures, which can introduce significant uncertainty.
  - **Why it matters** The claim of physiological relevance rests on this temperature analysis. If the reweighting or extrapolation procedure is not described, the robustness claim cannot be evaluated. Overstatement of validation could undermine confidence in the overall conclusions.
  - **Resolution test** Specify the temperature range, the method for computing temperature-dependent free energies, and the associated uncertainties. Show that the low-energy basin remains dominant at 310 K with statistical significance.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Abstract text
  - **Evidence pointer** Abstract, location not provided
  - **Issue** The abstract uses several technical terms without definition, including "REST2," "GMVAE," and "coupled folding-and-binding mechanism." While these are standard in the field, the abstract could benefit from brief contextualization for readers outside computational biophysics.
  - **Required correction** Add brief parenthetical explanations for REST2 and GMVAE on first use, and clarify the meaning of "coupled folding-and-binding" in one sentence.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Free energy reporting
  - **Evidence pointer** Abstract, location not provided
  - **Issue** The abstract reports "DeltaDeltaG < 0.35 kcal/mol" without specifying the reference state or the uncertainty in this value. The precision implied by two decimal places is not justified without error estimates.
  - **Required correction** Report the free energy differences with associated uncertainties and specify the reference state used for the calculation.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Scientific importance
  - **Affected element** Discussion of selectivity
  - **Evidence pointer** Abstract, location not provided
  - **Issue** The abstract opens with the claim that p5 "selectively inhibits the pathological CDK5-p25 complex," but the study only characterizes the unbound peptide. The connection between the solution ensemble and the selectivity mechanism is not directly addressed.
  - **Required correction** Clarify in the abstract that the study addresses the unbound state and that the link to selectivity is inferred, not directly demonstrated.
- **Technical failings that need to be addressed before the case is established** R1-M1 (simulation time and convergence), R1-M2 (clustering validation), R1-M3 (mechanistic overreach), R1-M4 (temperature analysis details)
- **Assessment against Nature-style criteria**  
  **Originality** The application of REST2 and GMVAE to a CDK5-p25 inhibitor peptide is a reasonable combination, but the general approach of characterizing disordered peptide ensembles with enhanced sampling is well established. The specific biological target adds interest, but the methodological novelty is modest.  
  **Scientific importance** The CDK5-p25 axis is a relevant therapeutic target in neurodegeneration, and understanding the conformational behavior of a selective inhibitor has potential value. However, the abstract does not establish how the unbound ensemble informs selectivity, limiting the immediate scientific impact.  
  **Interdisciplinary readership** The work bridges computational biophysics and neuropharmacology, which could attract readers from both communities. However, the abstract is written primarily for a computational audience and may not fully engage experimentalists or clinicians.  
  **Technical soundness** The choice of CHARMM36m and REST2 is appropriate, but the lack of convergence analysis, clustering validation, and detailed free energy methodology prevents assessment of technical rigor. The 350 ns timescale is a concern for disordered peptide sampling.  
  **Readability for nonspecialists** The abstract is concise and generally clear, but several technical terms and the mechanistic conclusion require more context for a broader audience.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a plausible study with a sound overall approach, but the central claims regarding the conformational states, free energy landscape, and folding-and-binding mechanism cannot be verified from the abstract alone. The authors should provide full methodological details, convergence analyses, and cluster validation, and should temper the mechanistic conclusion to a hypothesis unless bound-state data are presented. If the full manuscript addresses these concerns, the work could be of interest to the computational biophysics community.

## Risk / unsupported claims
- The claim that p5 "extensively" samples its conformational landscape in 350 ns is unsupported without convergence analysis.
- The identification of "three dominant conformational states" is unverifiable without clustering details and validation.
- The "coupled folding-and-binding mechanism" is presented as a supported conclusion but is a hypothesis based on unbound-state simulations only.
- The statement that the ensemble "validates the physiological relevance" is overstated without detailed temperature analysis and uncertainty quantification.
- The connection between the solution ensemble and p5's selective inhibition of CDK5-p25 is asserted but not demonstrated in the abstract.