## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no access to full manuscript, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors report development of alchemical free energy perturbation (FEP) protocols for predicting ligand binding affinity changes upon mutations in the intrinsically disordered N-terminal lid of MDM2, benchmarked against experimental data for two ligands (AM-7209 and Nutlin-3a). They claim equilibrium protocols outperform nonequilibrium protocols in precision, that force field and water model choices affect results, and that the resulting protocol accurately reproduces experimental binding affinity trends.
- **Visible evidence base** Abstract text only; no quantitative results, methodological details, or experimental comparisons are provided
- **Missing materials affecting confidence** Full methods, all numerical results, figures, tables, statistical analyses, force field and water model specifications, simulation parameters, convergence criteria, and experimental reference data

## Reviewer
- **Overall assessment** The abstract addresses a relevant and timely problem in computational drug discovery, namely the application of alchemical FEP to proteins with intrinsically disordered regions. The focus on MDM2, a therapeutically relevant target, and the systematic comparison of equilibrium versus nonequilibrium protocols are sensible. However, the abstract provides no quantitative evidence to support the central claims. Precision comparisons, accuracy metrics, and the magnitude of force field effects are all stated without numbers. The claim of an "accurate FEP protocol" cannot be evaluated from the supplied material. The work may be of interest to computational chemists and drug discovery researchers, but the case is not established from the abstract alone.
- **Who would be interested in the results, and why** Computational biophysicists and medicinal chemists working on alchemical free energy calculations, particularly those interested in extending FEP methodologies to proteins with disordered regions. The MDM2 system is relevant to oncology drug discovery, so researchers in that area may also find the results useful. Methodologists developing FEP protocols for challenging conformational ensembles would be the primary audience.
- **Major strengths** The problem is well chosen and practically important. The systematic comparison of equilibrium and nonequilibrium protocols is a useful framing. The focus on slowly varying degrees of freedom in IDRs is a specific and technically meaningful challenge. The inclusion of force field and water model effects is appropriate for a system with high conformational flexibility.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: the application of FEP to IDR-containing proteins is not entirely new, but the systematic protocol comparison for a ligand-dependent folding system is a reasonable contribution. Scientific importance: moderate, as the methodological advance is incremental and the system is specific. Interdisciplinary readership: limited, as the work is primarily of interest to computational chemists. Technical soundness: cannot be assessed from the abstract, as no quantitative results or methodological details are provided. Readability for nonspecialists: the abstract is clear and accessible, but the lack of numbers makes it difficult for any reader to judge the strength of the claims.
- **Recommendation posture** Currently not established from the provided evidence. The abstract makes strong claims without quantitative support. A full manuscript with detailed results would be required to assess whether the protocol is indeed accurate and whether the equilibrium versus nonequilibrium comparison is statistically meaningful.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "We show that the equilibrium protocol outperforms the nonequilibrium protocol in the precision of the free energy estimates obtained."
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract states that the equilibrium protocol outperforms the nonequilibrium protocol in precision, but no quantitative precision metrics are reported. No error bars, standard deviations, or statistical comparisons are given. It is unclear whether the difference is statistically significant or practically meaningful.
- **Why it matters** The central methodological conclusion of the work rests on this comparison. Without quantitative evidence, the claim cannot be verified or reproduced by other researchers.
- **Resolution test** Provide precision metrics such as standard errors or confidence intervals for both protocols across all mutants, along with a statistical test of the difference.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "Overall, our findings demonstrate an accurate FEP protocol capable of reproducing these trends."
- **Evidence pointer** Abstract, location not provided
- **Concern** The claim of accuracy is made without any numerical comparison to experimental binding affinities. No correlation coefficients, mean absolute errors, or root mean square errors are reported. The abstract does not state how many mutants were tested or how well the computed values matched experiment.
- **Why it matters** The term "accurate" is a quantitative claim that requires quantitative support. Without error metrics relative to experiment, the claim is unsupported.
- **Resolution test** Report numerical accuracy metrics against experimental binding affinities for the full mutant panel, including per-mutant errors and overall statistics.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "We demonstrate the effect of the protein force field and the water model used to simulate the highly flexible IDR region."
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract states that force field and water model choices have an effect, but no details are given on which force fields and water models were compared, how large the effects were, or whether the effects were consistent across mutants and ligands.
- **Why it matters** This claim is relevant for practitioners who need to choose simulation parameters for IDR-containing systems. Without specifics, the finding cannot be applied or evaluated.
- **Resolution test** Specify the force fields and water models tested, report the magnitude of the effects on computed binding affinities, and state whether the effects were systematic or system dependent.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract wording
- **Evidence pointer** Abstract, location not provided
- **Issue** The phrase "slowly varying degrees of freedom" is vague. It is not clear what specific degrees of freedom are meant or how they were identified.
- **Required correction** Define the relevant degrees of freedom and explain how they were characterized or measured.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Mutant panel description
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract mentions "a panel of mutants" but does not state how many mutants were studied or how they were selected.
- **Required correction** State the number of mutants and the criteria for their selection.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Protocol description
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract does not specify the alchemical transformation details, such as the number of intermediate states, the perturbation setup, or the simulation lengths.
- **Required correction** Provide these details in the full manuscript and summarize key parameters in the abstract if space permits.

## Risk / unsupported claims
- The claim that the equilibrium protocol outperforms the nonequilibrium protocol in precision is unsupported by quantitative data.
- The claim that the FEP protocol is "accurate" is unsupported by any numerical comparison to experiment.
- The claim that force field and water model choices affect results is unsupported by specific details.
- The general applicability of the protocol to "highly dynamic intrinsically disordered protein regions" is stated as a conclusion but is not supported by evidence beyond the single MDM2 system.