## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methodology, results, conclusions, data availability, acknowledgements) as provided. Figures, supplementary materials, and repository contents were not accessible for review.
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims based solely on the supplied text. No assessment of code, raw data, or figures beyond what is described in the text.
- **Shared manuscript claim summary** The authors present all-atom potential-of-mean-force (PMF) calculations to characterize nucleotide-nucleotide, amino acid-amino acid, and nucleotide-amino acid interactions relevant to biomolecular condensate formation. They benchmark multiple force fields, examine the effect of salt concentration, and propose a quantitative interaction library to inform coarse-grained model parametrization.
- **Visible evidence base** Text descriptions of PMF calculations, force field comparisons, interaction energy values, and qualitative statements about figures (Fig. 1-7) and supplementary materials (Fig. S1-S7). No actual figures, numerical tables, or raw data were available.
- **Missing materials affecting confidence** All figures, supplementary figures, numerical data tables, simulation input files, and the referenced GitHub repository. Without these, quantitative claims cannot be independently verified.

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important problem: providing quantitative, atomistic interaction data to inform coarse-grained models of biomolecular condensates. The scope is ambitious and the systematic approach is commendable. However, the current text, as provided, does not allow verification of the central quantitative claims. Key methodological details are missing or ambiguous, and several conclusions appear to extend beyond what the described calculations can support. The work has clear potential, but the evidence base as presented is insufficient to establish the case.
- **Who would be interested in the results, and why** Researchers developing coarse-grained models of biomolecular condensates, particularly those using bottom-up parametrization strategies. Also of interest to experimentalists studying RNA-protein phase separation who seek molecular-level rationalization of their observations. The interaction library, if made publicly available and validated, could become a community resource.
- **Major strengths** The systematic coverage of all 20 amino acids against 4 nucleotides is a significant undertaking. The benchmarking against multiple force fields and against published results (Krainer et al.) is a good practice. The inclusion of salt concentration effects and tertiary structures like G-quadruplexes broadens the relevance. The stated goal of providing a quantitative library for model parametrization is valuable and timely.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims to provide quantitative binding free energies for nucleotide-nucleotide, amino acid-amino acid, and nucleotide-amino acid interactions.
- **Evidence pointer** Results sections A, B, C; Figures 1-7; Supplementary Figures S1-S7. Location not provided for specific values.
- **Concern** The manuscript reports numerous quantitative PMF-derived binding energies, but the provided text does not include any numerical values, error estimates, or convergence criteria. The reader cannot assess the statistical reliability of the reported minima. The text states that "the uncertainty of the PMF minimum was estimated using the Bayesian bootstrap method" but no uncertainties are reported in the text. Furthermore, the convergence of the PMF calculations is not discussed; 10 ns per window may be insufficient for converged PMFs, particularly for the G-quadruplex system with a strong force constant of 55000 kJ mol⁻¹ nm⁻².
- **Why it matters** The central claim of the paper is the provision of a quantitative interaction library. Without reported values, error bars, and convergence analysis, the quantitative claims are unverifiable and the library cannot be used by the community. The lack of convergence assessment raises the possibility that the reported energy minima are not converged, which would invalidate the quantitative conclusions.
- **Resolution test** Provide a table of all computed PMF minima with associated bootstrap errors. Include a convergence analysis, such as block averaging or splitting the simulation time, for representative systems. Show that the PMF profiles are stable with respect to simulation length.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that the AMBER03ws and CHARMM36 force fields show "notable agreement" for nucleotide-nucleotide interactions, and that AMBER03ws and a99SB-disp show "near-quantitative agreement" for amino acid interactions.
- **Evidence pointer** Section A, Figure 1A-B; Section B, Figure 4A-F. Location not provided.
- **Concern** The claim of agreement between force fields is based on visual comparison of PMF profiles, as no quantitative comparison metric is provided. The text states that AMBER03ws "consistently display slightly deeper minima" compared to CHARMM36, which suggests systematic differences rather than agreement. For the amino acid benchmark, the text states that AMBER03ws "predicts stronger binding for Arg-Asp and Tyr-Tyr" while a99SB-disp "favors attractive interactions between like-charged residues such as Arg-Arg," indicating qualitative differences in the ranking of interaction strengths. The claim of "near-quantitative agreement" is not supported by the described results.
- **Why it matters** The choice of force field is a critical methodological decision. If the two force fields produce systematically different interaction strengths and different rankings, then the choice of AMBER03ws for subsequent calculations is not neutral and may bias the results. The claim of agreement is used to justify this choice, but the described results do not support it.
- **Resolution test** Provide a quantitative comparison metric, such as the root-mean-square deviation between PMF profiles or a comparison of the ranking of interaction strengths across force fields. State explicitly whether the differences between force fields are within the estimated statistical uncertainty.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The manuscript claims that the identified interactions "provide quantitative insights to inform coarse-grained model parametrization."
- **Evidence pointer** Conclusions section. Location not provided.
- **Concern** The manuscript does not demonstrate how the reported PMF data can be used to parametrize a coarse-grained model. No mapping from atomistic interaction free energies to coarse-grained interaction parameters is described. The connection between the specific PMF calculations (e.g., between capped amino acids and capped nucleotides in isolation) and the effective interactions in a many-body condensate is not addressed. The transferability of these single-pair PMFs to the condensed phase is assumed but not tested.
- **Why it matters** The stated purpose of the work is to inform coarse-grained model parametrization. Without a clear demonstration of how the data can be used, the practical impact of the work is unclear. The gap between single-pair PMFs in dilute solution and effective interactions in a dense condensate is nontrivial and must be addressed for the library to be useful.
- **Resolution test** Provide a concrete example of how one of the computed PMFs can be mapped to a parameter in an existing coarse-grained model (e.g., a contact potential or a sticky interaction strength). Discuss the limitations of the single-pair approximation and how many-body effects might be accounted for.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that the G-quadruplex PMF calculation captures "strong cooperative interactions among the RNA strands."
- **Evidence pointer** Section A, Figure 2E. Location not provided.
- **Concern** The description of the G-quadruplex PMF calculation is insufficient. The text states that "the pulling was applied to one strand while the remaining three were treated as a rigid block," but does not specify how the rigid block was defined or constrained. The use of a rigid block may prevent realistic relaxation of the G-quadruplex structure during pulling, potentially biasing the PMF. The reported binding energy of approximately -25 kcal/mol is stated without error or comparison to experimental or other computational values.
- **Why it matters** G-quadruplexes are presented as an important tertiary interaction, and the claim of strong cooperative binding is used to support the relevance of the work. If the calculation is biased by the rigid block constraint, the reported value may not be reliable.
- **Resolution test** Provide details on the rigid block definition and constraints. Validate the G-quadruplex PMF against an alternative method, such as pulling a different strand or using a different restraint scheme. Compare the computed binding energy to available experimental or computational estimates.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The manuscript claims that the identified interactions "deepen our understanding of condensate self-assembly, nucleic acid recognition, and phase-separation regulation at submolecular scale."
- **Evidence pointer** Abstract, Conclusions. Location not provided.
- **Concern** The manuscript catalogs interaction strengths but does not provide new mechanistic insight beyond what is already known. The finding that arginine interacts strongly with nucleotides, that aromatic residues stack with bases, and that salt screens phosphate-phosphate repulsion are all qualitatively expected. The manuscript does not identify unexpected interactions, propose a new mechanism, or resolve a controversy. The value of the work appears to be primarily as a data resource, not as a source of new biological or physical insight.
- **Why it matters** For a Nature-style publication, the work must offer more than a systematic catalog. The authors should articulate what new understanding is gained from their comprehensive analysis that was not already known from more limited studies.
- **Resolution test** Identify a specific, non-obvious finding from the data that challenges or refines current understanding of condensate formation. Alternatively, demonstrate that the library enables a prediction that can be tested experimentally and that would not be possible without this data.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Methodology section
- **Evidence pointer** Section I. Location not provided.
- **Issue** The description of the simulation setup is incomplete. The text mentions "approximately 5000 water molecules" and box dimensions, but does not specify the number of ions added for the salt concentration, the method for generating initial configurations, the equilibration protocol, or the specific parameters for the umbrella sampling (e.g., the range of the reaction coordinate, the spacing between windows, the total simulation time per window beyond the stated 10 ns).
- **Required correction** Provide a complete description of the simulation protocol, including all relevant parameters, to enable reproduction of the calculations.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results section A
- **Evidence pointer** Section A, Figure 1. Location not provided.
- **Issue** The text states that the ratio of CG to AU binding energy is 0.8, which is "reasonably close to the expected 2/3 value derived from the number of hydrogen bonds." The logic is unclear. If CG has three hydrogen bonds and AU has two, the expected ratio of binding energies might be 3/2, not 2/3. The text appears to have the ratio inverted or the argument is not clearly stated.
- **Required correction** Clarify the argument. State explicitly which binding energy is divided by which, and explain why the ratio of 0.8 is consistent with the hydrogen bond count.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Readability
- **Affected element** Results section C
- **Evidence pointer** Section C, Figures 5-6. Location not provided.
- **Issue** The text states that histidine has "an effective charge of approximately +0.5 due to its partial protonation of the imidazole side chain." This is a specific claim that requires justification. The pKa of histidine is near physiological pH, but the actual protonation state depends on the local environment. The authors should either provide a reference for this value or state the assumed protonation state explicitly.
- **Required correction** Provide a reference for the effective charge of histidine or state the assumed protonation state and its justification.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Results section A
- **Evidence pointer** Section A, Figure 2. Location not provided.
- **Issue** The text states that "ribose forms transient interactions rather than driving nucleotide association or RNA phase-separation." This conclusion is based on the weak binding energies observed. However, the authors do not define what constitutes a "transient" interaction or provide a threshold for when an interaction would be considered to "drive" association. The statement is qualitative and not supported by a specific criterion.
- **Required correction** Provide a quantitative criterion for classifying interactions as "transient" versus "driving" or soften the claim to be descriptive rather than interpretive.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results section A
- **Evidence pointer** Section A, Figure 3. Location not provided.
- **Issue** The text states that "high salt concentrations effectively screen phosphate-phosphate repulsion." This is expected, but the text does not report the magnitude of the effect or compare it to theoretical predictions (e.g., Debye-Hückel screening). The claim would be strengthened by a quantitative comparison.
- **Required correction** Report the change in the phosphate-phosphate PMF minimum as a function of salt concentration and compare to a theoretical screening model.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Readability
- **Affected element** Conclusions
- **Evidence pointer** Conclusions. Location not provided.
- **Issue** The conclusions section restates the results without providing a clear synthesis or outlook. The authors do not discuss limitations of the approach, such as the use of capped monomers rather than polymers, the neglect of multivalent effects, or the potential for force field inaccuracies.
- **Required correction** Add a paragraph discussing limitations and future directions.

## Risk / unsupported claims
- The claim of "notable agreement" between AMBER03ws and CHARMM36 is unsupported without a quantitative comparison metric.
- The claim of "near-quantitative agreement" between AMBER03ws and a99SB-disp is unsupported and contradicted by the described qualitative differences.
- All reported binding free energy values are unverifiable without the actual numerical data and error estimates.
- The claim that the data "inform coarse-grained model parametrization" is unsupported without a demonstrated mapping from atomistic PMFs to coarse-grained parameters.
- The claim that the G-quadruplex PMF captures "strong cooperative interactions" is unverifiable without details on the calculation and comparison to independent estimates.
- The claim that the work "deepens our understanding of condensate self-assembly" is not supported by the described results, which largely confirm existing expectations.
- The statement that histidine has an effective charge of approximately +0.5 is unsupported without a reference or explicit justification.
- The conclusion that ribose forms "transient interactions" is unsupported without a quantitative definition of "transient."