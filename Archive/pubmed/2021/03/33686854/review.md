## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors use all-atom replica-exchange molecular dynamics simulations of the K18 construct of Tau protein to show that monomeric conformational properties, including compactness, beta-structure propensity, and intramolecular interactions, vary nonlinearly with temperature. They identify specific sequence segments that contribute to temperature-dependent beta propensity and propose that the most collapsed monomeric state at a specific temperature favors liquid-liquid phase separation. Experimental validation via CD spectra, turbidity assays, and DIC microscopy is claimed.
- **Visible evidence base** Abstract text only; no numerical data, simulation details, or experimental results are provided
- **Missing materials affecting confidence** Full manuscript, simulation parameters, convergence criteria, force field details, experimental protocols, quantitative results, statistical analyses, and all figures and tables

## Reviewer
- **Overall assessment** The abstract presents a plausible computational hypothesis linking monomeric conformational properties of Tau K18 to temperature-dependent LLPS, with a claim of experimental corroboration. However, the abstract alone provides insufficient detail to evaluate the rigor of the simulations, the robustness of the conformational analysis, or the strength of the experimental validation. The central claim that monomeric collapse encodes LLPS propensity is interesting but not established from the provided evidence.
- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation, intrinsically disordered proteins, Tau biology, and neurodegenerative disease mechanisms would find these results relevant. The proposed link between monomeric conformational states and phase separation behavior could inform both biophysical models and therapeutic strategies targeting Tau aggregation.
- **Major strengths** The study addresses a significant open question regarding the molecular determinants of Tau LLPS. The use of long accumulated simulation time (26.4 microseconds) for an all-atom simulation of an intrinsically disordered protein is notable. The identification of specific sequence segments contributing to temperature-dependent behavior provides a testable hypothesis. The combination of computational and experimental approaches is appropriate for the question.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract does not provide sufficient information to assess simulation convergence, force field accuracy, or the statistical significance of the temperature-dependent trends. The experimental corroboration is mentioned but not described in enough detail to evaluate whether it directly tests the computational predictions. The causal link between monomeric collapse and LLPS propensity is inferred from prior literature rather than directly demonstrated.
- **Assessment against Nature-style criteria** Originality: The idea that monomeric conformational properties encode LLPS behavior is not entirely new, but the specific focus on temperature-dependent nonlinearity and the identification of particular sequence segments adds a novel angle. Scientific importance: Understanding Tau LLPS is relevant to both physiology and pathology, making the topic important. Interdisciplinary readership: The work bridges computational biophysics, protein chemistry, and cell biology, which could attract a broad audience. Technical soundness: Cannot be fully assessed from the abstract; the simulation methodology and experimental validation require scrutiny. Readability for nonspecialists: The abstract is reasonably clear but uses specialized terminology that may limit accessibility.
- **Recommendation posture** Currently not established from the provided evidence. The hypothesis is interesting and the approach is appropriate, but the abstract alone does not provide enough detail to verify the claims. A full manuscript review would be needed to determine whether the technical concerns can be resolved.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The simulation demonstrates that compactness, beta-structure propensity, and intramolecular interaction of K18 monomer exhibit nonlinear temperature-dependent behavior.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract does not provide any quantitative data, statistical measures, or convergence criteria to support the claim of nonlinear temperature-dependent behavior. Without information on the number of independent simulations, error bars, or replica exchange acceptance rates, it is impossible to assess whether the observed trends are robust or artifacts of insufficient sampling.
- **Why it matters** The central computational finding underpins the entire hypothesis. If the temperature-dependent trends are not statistically reliable, the subsequent claims about specific sequence contributions and LLPS propensity are weakened.
- **Resolution test** Provide quantitative measures of conformational properties as a function of temperature with error estimates, demonstrate simulation convergence through block averaging or similar methods, and show that the nonlinear trends are reproducible across independent simulation runs.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The specific sequence segments (295)DNIKHV(300)/(326)GNIHHK(331)/(337)VEVKSE(342) make significant contributions to the temperature dependence of the beta propensity of K18 monomer.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract claims that these specific segments are important but does not describe how this was determined. No information is given about mutation studies, per-residue analysis, or comparative simulations. The experimental corroboration via CD spectra, turbidity assays, and DIC microscopy is mentioned but not linked to these specific segments in a way that can be evaluated.
- **Why it matters** The identification of specific sequence determinants is a key novel contribution. Without clear evidence linking these segments to the observed temperature-dependent behavior, the claim remains speculative.
- **Resolution test** Show per-residue beta propensity profiles at different temperatures, provide mutation or truncation data that alter the identified segments and demonstrate loss of temperature dependence, and describe how the experimental methods specifically test the role of these segments.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Logical inference
- **Claim pointer** Given that more collapsed polypeptide chains were reported to be more prone to phase separate, our results suggest that K18 monomer inherently possesses conformational characteristics favoring LLPS.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The inference from monomeric collapse to LLPS propensity relies on a prior report, but the abstract does not establish a direct causal link between the specific collapsed state observed and phase separation behavior. The temperature at which the most collapsed state occurs is not specified, nor is it shown that this temperature corresponds to conditions where LLPS is experimentally observed.
- **Why it matters** The conclusion that monomeric properties encode LLPS is the main takeaway. If the link is only correlational and based on external literature, the study does not provide direct evidence for the encoding claim.
- **Resolution test** Demonstrate that the temperature of maximum collapse coincides with conditions of maximal LLPS in experiments, or provide a mechanistic model connecting specific monomeric conformations to intermolecular interactions that drive phase separation.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Simulation time statement
- **Evidence pointer** Abstract; location not provided
- **Issue** The accumulated simulation time of 26.4 microseconds is stated, but it is unclear whether this refers to total simulation time across all replicas or per replica. This affects the interpretation of sampling adequacy.
- **Required correction** Clarify whether 26.4 microseconds is the total accumulated time or the time per replica, and specify the number of replicas used.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Experimental methods
- **Evidence pointer** Abstract; location not provided
- **Issue** The experimental methods (CD spectra, turbidity assays, DIC microscopy) are listed but no conditions are given, such as protein concentration, buffer composition, or temperature range. This limits the ability to assess whether the experiments are directly comparable to the simulation conditions.
- **Required correction** Provide key experimental conditions in the abstract or refer to a methods section with full details.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "Fibril-nucleating cores"
- **Evidence pointer** Abstract; location not provided
- **Issue** The term "fibril-nucleating cores" is used without definition or reference. It is unclear which specific regions of K18 are being referred to and how they were identified.
- **Required correction** Define the fibril-nucleating cores with residue ranges and provide a citation or evidence for their identification.

## Risk / unsupported claims
- The claim that the identified sequence segments make significant contributions to temperature-dependent beta propensity is unsupported without per-residue or mutation data.
- The claim that the monomeric collapsed state favors LLPS is inferred from external literature and not directly demonstrated in this study.
- The experimental corroboration is mentioned but not described in sufficient detail to verify that it tests the computational predictions.
- The nonlinear temperature-dependent behavior of monomeric properties is asserted without quantitative evidence.
- The relevance of the specific temperature at which the most collapsed state occurs to experimental LLPS conditions is not established.