## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, and supplementary figure references) as provided.
- **Assessment boundary** Scientific content, methodological rigor, validity of claims, and presentation quality. No assessment of formatting, grammar, or journal policy.
- **Shared manuscript claim summary** The authors use molecular dynamics (MD) simulations to characterize the conformational flexibility of the receptor-binding domain (RBD) of SARS-CoV-2 (CoV2) and SARS-CoV (CoV1) in the unbound state, focusing on Loop 3. They report that Loop 3 is dynamically flexible, that common pandemic mutations do not perturb this flexibility, and that loop-modeling simulations identify lower-energy substates that block the ACE2 binding interface, potentially serving as therapeutic targets.
- **Visible evidence base** Abstract, Introduction, Results (Sections 2.1-2.5), Discussion, Materials and Methods, and references to supplementary figures (Fig. S1, S2, S3) and Table 1. No raw data, trajectory files, or supplementary material were provided.
- **Missing materials affecting confidence** Supplementary figures (S1, S2, S3), Table 1 (free energy values), raw MD trajectory data, convergence metrics, force field validation details, and the full mutational analysis dataset referenced from external sources. These omissions limit independent verification of quantitative claims.

## Reviewer
- **Overall assessment** The manuscript addresses a relevant question in SARS-CoV-2 biology, namely the conformational dynamics of the unbound RBD, which is underexplored relative to bound-state structures. The use of microsecond-scale MD simulations and loop-modeling is appropriate and technically sound in principle. However, the evidence presented is insufficient to fully support the central claims. The claim that lower-energy substates block the binding interface is based on limited sampling and a single free energy method (MM/GBSA) without error analysis or experimental validation. The resilience of Loop 3 flexibility to mutations is supported by only four single-point mutants, and the statistical significance of differences is not established. The manuscript would benefit from additional analyses, including convergence checks, free energy error estimates, and a clearer link between simulated substates and functional relevance.
- **Who would be interested in the results, and why** Structural biologists, computational biophysicists, and researchers in antiviral drug design would be interested. The work provides insights into the conformational landscape of a key viral protein, which could inform the design of therapeutics targeting cryptic or transient binding sites. The mutational resilience findings are relevant to ongoing efforts to track SARS-CoV-2 evolution and vaccine efficacy.
- **Major strengths** 1. The study addresses a gap in understanding the unbound state of the RBD, which is relevant to binding mechanisms and drug design. 2. The use of long-timescale MD simulations (microseconds) is appropriate for probing conformational flexibility. 3. The loop-modeling approach to explore conformations beyond the bound-state crystal structure is a creative and useful strategy. 4. The analysis of pandemic mutations in the context of dynamics is timely and practically relevant.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (lack of convergence and sampling validation), R1-M2 (insufficient statistical analysis of free energy differences), R1-M3 (limited mutational analysis without statistical comparison), R1-M4 (overinterpretation of functional relevance without experimental validation).
- **Assessment against Nature-style criteria** Originality: Moderate. The application of MD to RBD dynamics is not entirely novel, but the focus on unbound-state substates and therapeutic implications adds a new angle. Scientific importance: Moderate to high, given the pandemic context and potential for drug design, but the claims require stronger evidence. Interdisciplinary readership: The topic is of interest to virologists, structural biologists, and drug developers, but the presentation is heavily computational and may not be accessible to all. Technical soundness: Generally sound in methodology, but the analysis lacks rigor in statistical validation and convergence assessment. Readability for nonspecialists: The manuscript is reasonably clear but includes technical jargon and assumes familiarity with MD methods; the abstract is accessible, but the results section may be challenging for a broad audience.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising, but the current evidence does not fully establish the claims of lower-energy blocking substates and mutational resilience. Additional analyses and clarifications are required.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that MD simulations reveal "localized flexibility in Loop 3" and that the simulations are representative of the unbound state.
- **Evidence pointer** Section 2.1, Figure 3, Figure S2
- **Concern** The manuscript does not provide evidence that the MD simulations have converged. No time-series analysis of RMSD or RMSF is shown, and no block averaging or other convergence metrics are reported. The claim of "localized flexibility" is based on average properties over the trajectory, but without convergence assessment, it is unclear if the simulations have sampled equilibrium distributions.
- **Why it matters** Without demonstrated convergence, the reported flexibility and conformational ensembles may be biased by the initial conditions or insufficient sampling, undermining the validity of all subsequent claims.
- **Resolution test** Provide RMSD and RMSF time-series plots, split-trajectory analyses, or other convergence metrics (e.g., cosine content, block averaging) to demonstrate that the simulations have reached equilibrium and that the reported averages are stable.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The authors claim that some loop-model conformations have "lower free energy compared to the crystal structure" (Table 1).
- **Evidence pointer** Table 1, Section 2.2
- **Concern** The free energy differences (DG) are reported as single values without error bars or statistical significance testing. MM/GBSA is an approximate method, and the differences may be within the noise of the calculation. The number of conformations used for averaging is not specified, and no bootstrap or standard error estimates are provided.
- **Why it matters** The claim of lower-energy substates is central to the therapeutic targeting hypothesis. Without error estimates, the reader cannot assess whether these differences are meaningful or artifacts of the method.
- **Resolution test** Report standard errors or confidence intervals for the DG values, perform statistical tests (e.g., t-test or Mann-Whitney) comparing loop-model and crystal-structure simulations, and specify the number of frames or conformations used in the averaging.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that "mutations identified during the COVID-19 pandemic in Loop 3 do not affect this flexibility" and that Loop 3 is "resilient to perturbation by mutations."
- **Evidence pointer** Section 2.4, Figure 5, Figure S2b
- **Concern** The conclusion is based on only four single-point mutants (G476S, S477N, T478I, V483A). The RMSF profiles are compared visually, but no quantitative comparison (e.g., average RMSF difference, statistical test) is provided. The claim of resilience is too broad given the limited mutational sampling and lack of statistical analysis.
- **Why it matters** The resilience claim has implications for therapeutic design and vaccine efficacy. Overgeneralization from a small set of mutants could mislead future work.
- **Resolution test** Provide quantitative comparisons of RMSF or other flexibility metrics between wild-type and mutants, including statistical tests. Consider additional mutants or a more systematic mutational scan to support the claim of resilience.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation and significance
- **Claim pointer** The authors suggest that the identified substates "may represent new targets for therapeutic design" and that they "block key residues along the ACE2 binding interface."
- **Evidence pointer** Section 2.2, Section 3, Figure 6
- **Concern** The functional relevance of the identified substates is speculative. The simulations show conformational changes, but there is no experimental validation (e.g., mutagenesis, binding assays) to confirm that these substates are biologically relevant or that blocking the interface is functionally meaningful. The term "block" implies a functional effect that is not demonstrated.
- **Why it matters** The therapeutic targeting claim is a key motivation for the work. Without experimental support, the claim remains a hypothesis, and the significance of the findings is diminished.
- **Resolution test** Either temper the claims to be explicitly hypothetical or provide experimental evidence (e.g., binding affinity measurements, cell-based assays) linking the identified substates to functional outcomes.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.1, Figure 3
- **Evidence pointer** Figure 3a
- **Issue** The RMSF profiles are described as showing "localized flexibility in Loop 3," but the figure is not provided in the manuscript text. The reader cannot verify the claim without the figure.
- **Required correction** Ensure that all referenced figures are included in the main text or supplementary material, and describe the key features of the RMSF profiles in the text.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Section 4.3 (Molecular Dynamics Simulations)
- **Evidence pointer** Section 4.3
- **Issue** The methods state that the system was heated and equilibrated, but the total simulation time for each system is not explicitly stated in the methods (though implied in results). The number of replicas or independent simulations is not mentioned.
- **Required correction** Specify the total simulation time for each system, the number of replicas (if any), and the rationale for the chosen simulation length.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Table 1
- **Evidence pointer** Table 1
- **Issue** The table is referenced but not included in the provided text. The DG values are not described in detail, and the units are not specified.
- **Required correction** Include Table 1 in the manuscript and specify the units of DG (e.g., kcal/mol) and the method of calculation.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction, Discussion
- **Evidence pointer** Section 1, Section 3
- **Issue** The discussion of prior MD studies on RBD dynamics is brief and does not clearly differentiate the current work from previous studies, particularly regarding the unbound state.
- **Required correction** Expand the comparison with prior MD studies, highlighting what is new about the unbound-state analysis and loop-modeling approach.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section 4.1 (Preparation of Initial Structural Models)
- **Evidence pointer** Section 4.1
- **Issue** The use of the Coronavirus Structural Taskforce refined structures is mentioned, but the specific PDB entries and refinement details are not provided.
- **Required correction** Provide the PDB IDs and a brief description of the refinement process to ensure reproducibility.

## Risk / unsupported claims
- The claim that lower-energy substates "block key residues along the ACE2 binding interface" is unsupported by direct evidence; the simulations show conformational changes but not functional blocking.
- The claim that Loop 3 flexibility is "resilient to perturbation by mutations" is overgeneralized from four mutants without statistical comparison.
- The therapeutic targeting implications are speculative and not validated experimentally.
- The free energy differences in Table 1 are reported without error estimates, making the claim of lower-energy substates unverifiable.
- The convergence of MD simulations is not demonstrated, so the representativeness of the sampled ensembles is uncertain.