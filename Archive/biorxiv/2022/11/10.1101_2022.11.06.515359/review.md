## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as stated in the abstract, without access to full text, figures, or supplementary materials
- **Shared manuscript claim summary** The authors use molecular dynamics simulations to characterize the binding of tau K19 to an acidic membrane, identify three amphipathic helices that tether the protein to the membrane, validate their simulation results against published EPR data, and propose that partial mimicry between membrane and microtubule binding of tau facilitates membrane-mediated microtubule anchoring and tau transfer from membranes to microtubules.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or simulation details provided
- **Missing materials affecting confidence** Full manuscript, simulation parameters and force fields, EPR data comparison details, contact probability definitions, statistical analyses, and any supporting figures or tables

## Reviewer
- **Overall assessment** The abstract presents an interesting hypothesis regarding partial mimicry between tau's membrane and microtubule binding, supported by molecular dynamics simulations. However, the limited information provided prevents a rigorous evaluation of the technical soundness of the simulations, the validity of the EPR comparison, and the strength of the proposed functional implications. The central claim of partial mimicry is plausible but not fully established from the abstract alone.
- **Who would be interested in the results, and why** Researchers studying tau biology, intrinsically disordered proteins, protein-membrane interactions, and microtubule-associated proteins would find these results relevant. The work also has potential interest for those investigating neurodegenerative disease mechanisms, particularly tauopathies, where membrane and microtubule interactions of tau are implicated.
- **Major strengths** The study addresses a biologically important question about how an IDP engages with two distinct but similarly charged surfaces. The use of simulations to generate residue-level contact probabilities provides a mechanistic framework that can be compared with experimental data. The explicit validation against published EPR data is a commendable effort to bridge computation and experiment.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract does not provide sufficient detail on simulation methodology, force field selection, system setup, sampling length, or convergence criteria. Without these, the reliability of the simulated membrane binding and contact probabilities cannot be assessed. The validation against EPR data is mentioned but not described in a way that allows evaluation of its rigor.
- **Assessment against Nature-style criteria** 
  - Originality: The concept of partial mimicry between tau's membrane and microtubule binding is a novel framing, though the underlying observation of similar electrostatic interactions is not entirely unexpected given the shared negative charge of both surfaces.
  - Scientific importance: The potential functional implications for microtubule anchoring and tau transfer are significant for understanding tau's cellular roles, but the abstract does not provide direct experimental evidence for these functional claims.
  - Interdisciplinary readership: The work bridges computational biophysics, membrane biology, and microtubule biology, which could appeal to a broad audience if the full paper provides accessible context.
  - Technical soundness: Cannot be adequately assessed from the abstract alone; simulation details and validation methods are not described.
  - Readability for nonspecialists: The abstract is concise and generally clear, but terms such as "amphipathic helices" and "contact probabilities" may require some background knowledge.
- **Recommendation posture** Currently not established from the provided evidence. The hypothesis is interesting and the approach is appropriate, but the abstract alone does not provide enough detail to assess the technical validity of the simulations or the strength of the EPR validation. A full manuscript with detailed methods and results would be needed to evaluate whether the claims are supported.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that molecular dynamics simulations characterize the dynamic binding of tau K19 to an acidic membrane and that the three amphipathic helices tether the protein to the membrane interface.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract provides no information on the simulation methodology, including force field parameters, water model, membrane composition, system size, simulation length, temperature, or pressure coupling. Without these details, it is impossible to evaluate whether the simulations are sufficiently converged and physically realistic to support the claimed membrane binding behavior.
- **Why it matters** Molecular dynamics simulations of IDP-membrane interactions are highly sensitive to force field choices and sampling time. Inadequate sampling or inappropriate force fields can lead to artifactual binding modes or incorrect contact probabilities, undermining the central claims of the study.
- **Resolution test** The full manuscript must provide a detailed methods section describing the simulation setup, force field validation, convergence analysis, and replicate simulations. The authors should demonstrate that the observed membrane binding is robust across multiple independent simulations and consistent with experimental data beyond the EPR comparison.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The authors claim that the separation between and membrane positioning of the amphipathic helices in the simulations are validated by published EPR data.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract states that EPR data validate the simulation results, but no details are given about which EPR measurements were used, how the comparison was performed, or what quantitative metrics were applied. It is unclear whether the EPR data were collected under similar conditions to the simulations or whether the comparison is qualitative or quantitative.
- **Why it matters** Validation against experimental data is a key strength of the study, but without a clear description of the comparison methodology, the reader cannot assess whether the validation is meaningful or whether the EPR data are being overinterpreted.
- **Resolution test** The full manuscript must include a detailed comparison between simulated and EPR-derived distances or membrane positions, including error estimates and a discussion of any discrepancies. The authors should specify the EPR labels, the measured distances, and the simulation-derived equivalents.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The authors claim that partial mimicry between membrane and microtubule binding facilitates both the membrane anchoring of microtubules by tau and the transfer of tau from membranes to microtubules.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The functional implications stated in the final sentence are presented as conclusions, but the abstract provides no direct evidence for these processes. The simulations characterize membrane binding, and the comparison with microtubule contacts is based on previously published cryo-EM data, but no simulation or experiment is described that tests the proposed facilitation of microtubule anchoring or tau transfer.
- **Why it matters** These functional claims extend beyond the direct simulation results and require additional evidence, such as co-simulation of tau with both membranes and microtubules, or experimental assays of tau-mediated membrane-microtubule interactions. Without such evidence, the claims are speculative.
- **Resolution test** The full manuscript should either provide direct evidence for the proposed functional roles or clearly frame these statements as hypotheses rather than conclusions. If experimental data are available, they should be described in sufficient detail to support the claims.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Definition of "partial mimicry"
- **Evidence pointer** Abstract; location not provided
- **Issue** The term "partial mimicry" is used to describe the similarity between membrane and microtubule binding, but the abstract does not define the criteria for partial versus complete mimicry or quantify the degree of similarity.
- **Required correction** Provide a clear definition of partial mimicry, including the specific residues or interactions that are considered similar and the threshold used to classify them as such.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Residue-level contact probabilities
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract mentions that membrane contact probabilities show similarities to and distinctions from native microtubule contacts, but does not specify which residues or regions exhibit these similarities or distinctions beyond the conserved Lys and Val.
- **Required correction** Include a summary of the key residues or regions that show similarity or distinction, or refer to a figure in the full manuscript that presents this information.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Context
- **Affected element** Biological relevance
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract does not discuss the physiological relevance of the proposed membrane-microtubule interplay, such as the cellular conditions under which tau would encounter both surfaces simultaneously.
- **Required correction** Add a brief statement in the discussion about the potential biological context, such as axonal transport or membrane-associated microtubule nucleation, to help readers understand the significance of the findings.

## Risk / unsupported claims
- The claim that partial mimicry facilitates membrane anchoring of microtubules by tau is unsupported by direct evidence in the abstract.
- The claim that partial mimicry facilitates transfer of tau from membranes to microtubules is unsupported by direct evidence in the abstract.
- The validation of simulation results against EPR data is mentioned but cannot be evaluated without details of the comparison.
- The overall reliability of the simulations cannot be assessed without methodological details.