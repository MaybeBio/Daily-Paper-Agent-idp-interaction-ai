## Review setup
- **Input scope** Full manuscript text, including abstract, results, figures (referenced), methods, and supplementary figure references.
- **Assessment boundary** Scientific validity of the claims, methodological soundness, and consistency between simulation and experimental data, as presented in the provided text.
- **Shared manuscript claim summary** The authors propose that extensive phosphorylation of the C-terminal low-complexity domain (LCD) of TDP-43 converts it into a block-copolymer-like architecture, driving finite-sized micellization rather than macroscopic phase separation or fibril formation. This is supported by coarse-grained simulations and in vitro experiments on phosphorylated LCD and phosphomimetic mutants (12D, 12DD).
- **Visible evidence base** Abstract, full results section, methods, figure legends (referenced), and supplementary figure references.
- **Missing materials affecting confidence** Actual figures and supplementary figures (S1–S24) were not provided; only their legends and in-text references. Raw data, statistical analysis outputs, and simulation parameter files were not available for independent verification.

## Reviewer
- **Overall assessment** This manuscript presents a compelling and well-structured hypothesis that phosphorylation of the TDP-43 LCD acts as a switch from macroscopic phase separation to micellization. The combination of coarse-grained simulations with multiple orthogonal experimental techniques (DLS, TEM, cryo-EM, fluorescence) is a strength. However, the current evidence base, as presented, has several gaps that prevent full confidence in the conclusions. The most significant concerns are the lack of direct experimental evidence for the internal structure of the micelles (e.g., core-corona), the reliance on phosphomimetic mutants as proxies for true phosphorylation, and the absence of quantitative comparison between simulation predictions and experimental measurements beyond qualitative agreement. The manuscript is well-written and the topic is of high interest to the fields of phase separation and neurodegeneration.
- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation, protein aggregation, post-translational modification, and the molecular mechanisms of neurodegeneration (ALS, FTD). The work is also relevant to those interested in the biophysics of intrinsically disordered proteins and the design of synthetic protein-based nanomaterials.
- **Major strengths**
    1.  The central hypothesis is novel and clearly articulated, proposing a specific molecular mechanism (phosphorylation-induced block-copolymer architecture) for a functional switch in assembly behavior.
    2.  The study integrates computational predictions with a multi-technique experimental validation strategy, which is a robust approach.
    3.  The use of both a true enzymatic phosphorylation approach and phosphomimetic mutants is a thoughtful design that attempts to bridge the gap between in vitro and in vivo relevance.
    4.  The observation of a salt-dependent morphological transition (spheres to worms) for the phosphomimetic mutants adds depth and suggests a tunable system.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Experimental evidence for proposed mechanism
    - **Claim pointer** The manuscript claims that phosphorylated TDP-43 LCD forms "spherical micelles" with a "core-corona" architecture, where the hydrophobic N-terminal block forms the core and the phosphorylated C-terminal block forms the corona.
    - **Evidence pointer** Results sections 2.2, 2.3; Figures 4, 5, 6; Methods sections 4.10, 4.11.
    - **Concern** The evidence presented supports the formation of finite-sized, spherical nanoparticles, but it does not directly demonstrate the proposed internal core-corona structure. DLS and EM provide size and shape, and pyrene fluorescence indicates a hydrophobic environment, but this is not conclusive proof of a block-copolymer micelle with a distinct core and corona. The authors do not provide any data (e.g., small-angle X-ray/neutron scattering, contrast-matched cryo-EM, or fluorescence resonance energy transfer experiments) that would directly resolve the internal organization of the particles.
    - **Why it matters** The core-corona structure is central to the claim that this is a "micellization switch" and not just the formation of amorphous aggregates or oligomers. Without direct structural evidence, the interpretation of the observed nanoparticles as micelles remains a hypothesis, albeit a plausible one.
    - **Resolution test** The authors should provide direct structural evidence for the core-corona architecture. This could be achieved through techniques such as small-angle X-ray scattering (SAXS) with contrast variation, or by using site-specific labeling and FRET to demonstrate the spatial segregation of the N- and C-terminal blocks within the assembled particle.
    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Relevance of phosphomimetic mutants
    - **Claim pointer** The manuscript uses the 12D and 12DD phosphomimetic mutants to "recapitulate the phosphorylated phenotype" and draws conclusions about the behavior of the phosphorylated protein based on these mutants.
    - **Evidence pointer** Results section 2.3; Figures 6, 7; Discussion.
    - **Concern** While the authors show that 12D and 12DD form similar structures to the phosphorylated protein, they also note significant differences, such as the larger size of the mutant micelles and the observation of wormlike micelles for the mutants but not for the phosphorylated protein. The manuscript does not adequately address whether these differences are due to the chemical nature of the phosphomimetic (Asp vs. phosphoserine) or to the exact charge distribution. The claim that the mutants are "faithful charge-based mimics" is an assumption that is not fully validated.
    - **Why it matters** The conclusions about the biological role of phosphorylation are largely based on the behavior of the phosphomimetic mutants. If the mutants do not accurately replicate the properties of the true phosphorylated protein, the physiological relevance of the findings is weakened.
    - **Resolution test** The authors should perform a more detailed comparison of the biophysical properties of the phosphorylated protein and the mutants, such as measuring the exact charge and hydration of the C-terminal block. They could also test additional phosphomimetic mutants with different charge distributions or use a non-hydrolyzable phosphoserine analog to better mimic the true phosphorylated state.
    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Quantitative validation of simulations
    - **Claim pointer** The manuscript states that coarse-grained simulations "predicted" micellization and that the experimental results are in agreement with these predictions.
    - **Evidence pointer** Results section 2.1; Figures 2, S1–S6, S12–S15.
    - **Concern** The comparison between simulation and experiment is largely qualitative. The manuscript reports that simulations predict micelles of ~20-40 chains, while experiments show particles of ~20-50 nm. However, there is no quantitative comparison of, for example, the aggregation number, the critical micelle concentration, or the size distribution. The manuscript also notes discrepancies, such as the 12D mutant not micellizing in simulations but forming micelles in experiments.
    - **Why it matters** For the computational predictions to be a strong pillar of the paper's argument, they need to be quantitatively validated against the experimental data. A qualitative agreement is suggestive but not conclusive.
    - **Resolution test** The authors should perform a more rigorous quantitative comparison between simulation and experiment. This could involve calculating the CMC from simulations and comparing it to the experimentally determined value, or by directly comparing the simulated and experimental size distributions. The discrepancies, such as the 12D behavior, should be discussed in more detail.
- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity of figure presentation
    - **Affected element** Figures 4, 5, 6
    - **Evidence pointer** Results sections 2.2, 2.3
    - **Issue** The manuscript refers to "spherical nanoparticles" and "wormlike micelles" but the actual figures were not provided for review. It is unclear if the scale bars and annotations are clear enough to distinguish these morphologies.
    - **Required correction** Ensure that all EM images have clear scale bars and that the different morphologies are clearly labeled in the figure panels.
    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Statistical analysis
    - **Affected element** Figures 4, 6, 7
    - **Evidence pointer** Methods section 4.13
    - **Issue** The manuscript states that no null-hypothesis significance testing was applied. While this is acceptable for a characterization study, the large number of replicates (n=12) suggests that some statistical comparison of size distributions across conditions could strengthen the claims.
    - **Required correction** Consider adding a statistical comparison of the size distributions (e.g., a Kolmogorov-Smirnov test) to support the claim that the sizes are stable and different between conditions.
    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Discussion of alternative interpretations
    - **Affected element** Discussion section
    - **Evidence pointer** Discussion
    - **Issue** The manuscript does not discuss alternative interpretations for the observed nanoparticles, such as the formation of oligomers or small aggregates that are not true micelles.
    - **Required correction** Add a paragraph to the Discussion addressing why the observed structures are best interpreted as micelles and not other types of assemblies.
- **Technical failings that need to be addressed before the case is established**
    - R1-M1: Lack of direct structural evidence for the core-corona micelle architecture.
    - R1-M2: Insufficient validation of phosphomimetic mutants as faithful proxies for phosphorylation.
    - R1-M3: Lack of quantitative comparison between simulation and experimental data.
- **Assessment against Nature-style criteria**
    - **Originality** High. The concept of a phosphorylation-induced switch to micellization in a disease-relevant protein is novel and not a simple extension of existing work.
    - **Scientific importance** High. The findings have implications for understanding TDP-43 pathology and for the general field of IDP self-assembly. The proposed mechanism could be a target for therapeutic intervention.
    - **Interdisciplinary readership** Moderate to High. The work bridges biophysics, cell biology, and neurobiology. The clear writing makes it accessible to a broad audience, but the heavy reliance on biophysical techniques may limit its immediate appeal to purely cell-biological readers.
    - **Technical soundness** Moderate. The experimental techniques are appropriate, but the lack of direct structural evidence for the key claim and the incomplete validation of the phosphomimetic approach are significant weaknesses.
    - **Readability for nonspecialists** Good. The abstract and introduction are clear. The results are logically structured, and the methods are detailed. The main concepts are explained well.
- **Recommendation posture** Supportive if technical concerns are resolved. The core hypothesis is interesting and the work is potentially important. However, the case is not fully established from the provided evidence. The authors must provide direct structural evidence for the micelle architecture and a more rigorous quantitative link between simulations and experiments.

## Risk / unsupported claims
- The claim that the observed nanoparticles are "micelles" with a specific core-corona structure is not directly supported by the evidence presented.
- The claim that the 12D and 12DD mutants are "faithful charge-based mimics" of the phosphorylated protein is an assumption that is not fully validated.
- The claim that phosphorylation "effectively suppresses the amyloid pathway" is based on the absence of ThT signal and fibrils in EM, but this is a negative result and could be due to kinetic factors.
- The biological relevance of the wormlike micelles observed for the phosphomimetic mutants at high salt is speculative and not directly supported by data.