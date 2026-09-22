## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to full manuscript, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors report development and systematic assessment of equilibrium and non-equilibrium relative alchemical binding free energy (FEP) protocols for predicting the impact of mutations in the N-terminal intrinsically disordered region (IDR) lid of MDM2 on binding affinities for two ligands, AM-7209 and Nutlin-3a. They claim the equilibrium protocol outperforms the non-equilibrium protocol in precision, that results are sensitive to protein force field and water model choices, and that the optimized protocol accurately reproduces experimental binding affinity trends.
- **Visible evidence base** Abstract text only; no numerical data, methodological details, or experimental comparisons are provided
- **Missing materials affecting confidence** Full manuscript text, all figures and tables, computational protocol details, force field and water model specifications, statistical error estimates, experimental binding affinity data, and any comparison with prior FEP studies

## Reviewer
- **Overall assessment** The abstract presents a timely and potentially valuable contribution to computational drug discovery, addressing a recognized gap in FEP methodology for proteins with intrinsically disordered regions. The focus on MDM2, a therapeutically relevant target, and the systematic comparison of equilibrium versus non-equilibrium protocols are sensible. However, the abstract provides insufficient quantitative evidence to evaluate the central claims. Key metrics such as accuracy relative to experiment, precision differences, and the magnitude of force field effects are not reported. The claim of an "accurate FEP protocol" is not substantiated from the supplied material. The work may be of interest to computational chemists and drug discovery researchers, but the current evidence base is too limited to assess technical soundness or establish the case.
- **Who would be interested in the results, and why** Computational chemists and biophysicists working on alchemical free energy methods, particularly those addressing flexible or disordered protein systems. Drug discovery scientists interested in resistance mutations in the MDM2-p53 axis and in improving predictive tools for ligand binding in challenging targets would also find the work relevant.
- **Major strengths** The problem is well chosen and practically important, as IDR-containing proteins are underrepresented in FEP benchmarking. The systematic comparison of equilibrium and non-equilibrium protocols is a useful design. The focus on slowly-varying degrees of freedom in mutations is a thoughtful consideration that addresses a known technical challenge.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality is moderate to high, as extending FEP to IDRs is a relatively underexplored area. Scientific importance is potentially high given the relevance to drug resistance and the prevalence of disordered regions in the proteome. Interdisciplinary readership is plausible, spanning chemistry, biophysics, and structural biology. Technical soundness cannot be assessed from the abstract alone, as no quantitative results or methodological details are provided. Readability for nonspecialists is adequate, though the abstract assumes familiarity with FEP terminology. Overall, the work has promise but the current evidence does not meet the standard required to establish the claims.
- **Recommendation posture** Currently not established from the provided evidence. The abstract suggests a potentially valuable study, but the absence of quantitative results and methodological detail prevents any assessment of validity. A revised submission with full data and clear reporting of accuracy and precision metrics would be needed to evaluate the claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that the equilibrium protocol outperforms the non-equilibrium protocol in the precision of free energy estimates.
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract states that the equilibrium protocol outperforms the non-equilibrium protocol in precision, but no quantitative measures are given. No error bars, standard deviations, or statistical comparisons are reported. Without such data, the claim is unverifiable.
- **Why it matters** The central methodological conclusion of the work rests on this comparison. If the precision difference is small or within noise, the conclusion may not hold. The reader cannot judge the robustness of the finding.
- **Resolution test** Provide quantitative precision metrics for both protocols, such as standard errors or confidence intervals across multiple independent runs, and a statistical test of the difference.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that the optimized FEP protocol accurately reproduces experimental binding affinity trends for the mutant panel.
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract does not report any numerical comparison between computed and experimental binding affinities. No correlation coefficients, mean unsigned errors, or rank-order agreement metrics are provided. The term "accurate" is undefined in this context.
- **Why it matters** The primary claim of the paper is that the protocol can predict drug resistance mutations. Without quantitative accuracy metrics, the reader cannot assess whether the predictions are useful for practical applications.
- **Resolution test** Report correlation coefficients, mean unsigned errors, and rank-order statistics comparing computed and experimental affinities for the full mutant panel, with uncertainties.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that the choice of protein force field and water model significantly affects simulation of the IDR region.
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract states that the effect of force field and water model is demonstrated, but no details are given on which models were tested, how large the effects were, or whether the effects were consistent across mutations and ligands.
- **Why it matters** This claim is important for guiding future FEP studies on IDR-containing proteins. Without specific results, the reader cannot determine which force field and water model combinations are recommended or how sensitive the conclusions are to these choices.
- **Resolution test** Provide a table or figure showing computed affinities or free energy differences for each force field and water model tested, with a clear statement of the magnitude of the effects and their impact on the final conclusions.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract wording
- **Evidence pointer** Abstract, location not provided
- **Issue** The phrase "slowly-varying degrees of freedom" is vague and not defined. It is unclear which specific degrees of freedom are meant and how they were identified.
- **Required correction** Define the term explicitly, for example by referring to specific dihedral angles or conformational coordinates, and explain how they were monitored or constrained.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Experimental context
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract does not state how many mutations were studied or how many experimental measurements were used for comparison. This information is essential for judging the statistical power of the study.
- **Required correction** Include the number of mutations and the source of experimental data in the abstract or indicate that this is provided in the full manuscript.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Protocol description
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract does not specify the software package, simulation length, or number of replicates used. These details are critical for reproducibility.
- **Required correction** Add key simulation parameters to the abstract or state that full details are in the methods section.

## Risk / unsupported claims
- The claim that the equilibrium protocol outperforms the non-equilibrium protocol in precision is unsupported due to lack of quantitative data.
- The claim that the protocol accurately reproduces experimental binding affinity trends is unsupported due to absence of any numerical comparison.
- The claim that force field and water model choices have a demonstrated effect is unsupported due to lack of specific results.
- The general applicability of the protocol to other IDR-containing proteins is stated but not evidenced.