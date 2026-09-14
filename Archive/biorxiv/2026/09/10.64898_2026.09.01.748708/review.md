## Review setup
- **Input scope** Full manuscript (abstract and main text, including figures and tables, as provided in the bioRxiv preprint)
- **Assessment boundary** Scientific content, methodology, data analysis, and interpretation as presented in the manuscript. No assessment of formatting, grammar, or editorial style beyond what affects scientific clarity.
- **Shared manuscript claim summary** The authors claim that residue-level coarse-grained (CG) simulations of biomolecular condensates can reproduce equilibrium properties but not dynamics with a universal time-rescaling factor. They demonstrate that a composition-specific time-rescaling factor captures the ionic-strength dependence of chain reconfiguration times within a given complex coacervate, but this factor is not transferable between phases or across condensate compositions. They further show that the required time rescaling correlates with interaction energy, suggesting missing frictional effects arise from protein-protein interactions.
- **Visible evidence base** Full manuscript text, all figures (1-6), tables (1-2), and supplementary information (figures S1-S8, tables S1-S3) as provided in the bioRxiv preprint.
- **Missing materials affecting confidence** No missing materials identified. The manuscript appears complete for the scope of the study.

## Reviewer
- **Overall assessment** This manuscript addresses a critical and timely question in the field of biomolecular condensate modeling: the extent to which residue-level coarse-grained simulations can capture dynamics, beyond equilibrium properties. The study is well-designed, using a systematic set of complex coacervates formed by prothymosin α with four different cationic partners, and a combination of experimental and simulation data. The key finding—that time rescaling is not universal but correlates with interaction energy—is novel and has significant implications for the field. The manuscript is clearly written and the evidence is presented logically. However, several technical concerns regarding the robustness of the time-rescaling analysis and the interpretation of the correlation with interaction energy need to be addressed before the case is fully established.
- **Who would be interested in the results, and why** Researchers in computational biophysics, soft matter physics, and cell biology who use or interpret coarse-grained simulations of intrinsically disordered proteins and biomolecular condensates. The results are directly relevant to anyone seeking to extract kinetic or material properties (e.g., diffusion coefficients, viscosity, relaxation times) from such simulations, as they provide a clear warning against assuming a universal time rescaling and offer a potential physical basis for the rescaling factor.
- **Major strengths** 1. The study addresses a fundamental and practically important question that has been largely overlooked in the field. 2. The experimental system is well-chosen, with four distinct cationic partners providing a range of interaction strengths and dynamics. 3. The combination of experimental data (FRET, NMR, phase diagrams) and simulations is powerful and allows for direct validation. 4. The correlation between the time-rescaling factor and interaction energy is a compelling and physically plausible result that provides a path forward for kinetic calibration.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Methodology / Data Analysis
    - **Claim pointer** "A composition-specific time-rescaling factor captures the ionic-strength dependence of chain reconfiguration times within a given complex coacervate."
    - **Evidence pointer** Figure 4, Table 1
    - **Concern** The determination of the time-rescaling factor relies on comparing simulated chain reconfiguration times (τ_r) to experimental values. The experimental τ_r values are derived from FRET measurements, which have inherent uncertainties. The manuscript does not provide a clear error analysis for the experimental τ_r values, nor does it propagate these uncertainties into the determination of the rescaling factor. Furthermore, the rescaling factor is presented as a single value for each condition, but the data in Figure 4 show significant scatter, and the fit quality appears variable across conditions.
    - **Why it matters** The central claim of the paper rests on the existence and specificity of these time-rescaling factors. If the experimental uncertainties are large or the rescaling factors are not well-constrained, the claim that they are "composition-specific" and "capture the ionic-strength dependence" is weakened. The reader cannot assess the statistical significance of the differences between rescaling factors for different coacervates.
    - **Resolution test** Provide a detailed error analysis for the experimental τ_r values (e.g., standard deviations or confidence intervals from bootstrapping). Propagate these errors to the rescaling factors and present them with associated uncertainties (e.g., as error bars in Figure 4 or in Table 1). Perform a statistical test (e.g., ANOVA or pairwise t-tests) to demonstrate that the rescaling factors for different coacervates are significantly different from each other, and that the ionic-strength dependence within a coacervate is significant.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** No
    - **Axis** Interpretation / Causality
    - **Claim pointer** "the required time rescaling strongly correlates with the interaction energy of the protein chains, suggesting that the missing frictional effects arise from protein-protein interactions rather than solely from protein-solvent interactions, reminiscent of internal friction."
    - **Evidence pointer** Figure 6
    - **Concern** The correlation shown in Figure 6 is between the time-rescaling factor and the average interaction energy per chain from the simulations. This is a correlation, not a causal relationship. The interaction energy itself is a simulation output, and it is possible that both the rescaling factor and the interaction energy are correlated with a third, unmeasured variable (e.g., chain density, water content in the condensate, or the specific nature of the cationic side chains). The interpretation that the missing friction is "reminiscent of internal friction" is speculative and not directly supported by the data. Internal friction typically refers to friction within a single polymer chain due to dihedral rotations or side-chain packing, whereas the interaction energy here is inter-chain.
    - **Why it matters** The paper's proposed physical mechanism for the non-universal time rescaling is a key conceptual advance. If the correlation is spurious or the interpretation is incorrect, the paper's main conclusion is weakened. The field needs a clear, testable hypothesis, not just a correlation.
    - **Resolution test** 1. Perform a partial correlation analysis to control for potential confounding variables (e.g., dense-phase concentration, chain length, or solvent accessible surface area). 2. Test the "internal friction" hypothesis more directly. For example, does the rescaling factor correlate with the number or strength of inter-chain contacts (e.g., from a contact map analysis) rather than the total interaction energy? 3. Discuss alternative interpretations, such as the role of hydrodynamic interactions (which are absent in the CG model) or the effect of the implicit solvent model on the effective viscosity.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Methodology / Generalizability
    - **Claim pointer** "These results show that agreement with measured equilibrium observables does not imply a universally transferable timescale for conformational dynamics in residue-level coarse-grained simulations."
    - **Evidence pointer** Figures 2, 3, 4, 5
    - **Concern** The study is limited to a single protein (prothymosin α) and its complexes with four cationic partners. While this is a well-chosen system, it is a specific class of complex coacervates. The claim of "no universally transferable timescale" is strong and may not generalize to other types of condensates (e.g., those formed by folded domains, RNA-binding proteins with prion-like domains, or systems with different solvent conditions). The authors acknowledge this limitation in the discussion, but the abstract and title present the finding as a general principle.
    - **Why it matters** The paper's impact and the strength of its central message depend on its generalizability. If the finding is specific to this particular system or class of coacervates, it is still valuable but less broadly significant. The current framing may overstate the generality of the conclusion.
    - **Resolution test** 1. Explicitly state the scope of the claim in the abstract and title (e.g., "for this class of complex coacervates" or "in residue-level CG simulations of IDP-based condensates"). 2. Discuss the conditions under which the finding might or might not hold (e.g., for condensates with very different densities, or for models with explicit solvent). 3. If possible, provide preliminary data or a clear prediction for a different system (e.g., a condensate formed by a different IDP) to test the generality.

- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity / Presentation
    - **Affected element** Figure 4
    - **Evidence pointer** Figure 4
    - **Issue** The color scheme in Figure 4 is difficult to distinguish for some readers, particularly the shades of blue and green used for different ionic strengths.
    - **Required correction** Use a more distinct color palette (e.g., a sequential or diverging colormap) or different line styles (dashed, dotted) to differentiate the ionic strength conditions.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Methodology / Reporting
    - **Affected element** Methods section
    - **Evidence pointer** "Simulation Methods" section
    - **Issue** The description of the coarse-grained model (e.g., force field parameters, water model, salt treatment) is somewhat brief. For reproducibility, more details are needed, particularly regarding the treatment of long-range electrostatics and the specific implementation of the implicit solvent model.
    - **Required correction** Provide a more detailed description of the CG model, including a reference to the specific force field parameters used, the cutoff for non-bonded interactions, and the method for handling long-range electrostatics (e.g., Ewald summation or reaction field). If the model is a standard one (e.g., from a previous publication), state this explicitly and provide the key parameters in the SI.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Interpretation / Discussion
    - **Affected element** Discussion section
    - **Evidence pointer** Discussion, paragraph 3
    - **Issue** The discussion of the practical implications for the field is somewhat brief. The authors state that "thermodynamic validation" and "kinetic calibration" are needed, but do not provide concrete guidance on how to perform such calibration in practice.
    - **Required correction** Expand the discussion to provide more practical recommendations. For example, suggest that for a new condensate system, one should first validate equilibrium properties (e.g., phase diagram, chain dimensions) and then measure a single experimental dynamic observable (e.g., a diffusion coefficient or relaxation time) to calibrate the time rescaling. Discuss the limitations of this approach (e.g., the observable-dependence of the rescaling factor).

- **Technical failings that need to be addressed before the case is established** R1-M1 (error analysis for time-rescaling factors) is a blocking concern. R1-M2 (causality of the correlation) and R1-M3 (generalizability) are major concerns that need to be addressed to strengthen the case, but are not necessarily blocking.

- **Assessment against Nature-style criteria**
    - **Originality**: High. The question of time-rescaling universality in CG simulations of condensates is novel and has not been systematically addressed before. The correlation with interaction energy is a new and potentially important finding.
    - **Scientific importance**: High. The results have direct implications for the interpretation of a large and growing body of simulation work on biomolecular condensates. They provide a clear warning and a potential path forward for kinetic calibration.
    - **Interdisciplinary readership**: Moderate to High. The work is of primary interest to computational biophysicists and soft matter physicists, but the conceptual message about the limits of CG models and the need for kinetic calibration is also relevant to cell biologists and experimentalists studying condensates.
    - **Technical soundness**: Good, but with significant concerns. The simulation methodology is appropriate, and the comparison to experiments is a strength. However, the error analysis for the central claim (R1-M1) is insufficient, and the causal interpretation of the correlation (R1-M2) is not fully supported.
    - **Readability for nonspecialists**: Good. The abstract and introduction are clear and accessible. The main text is well-structured, and the figures are generally informative. The minor comments about figure clarity and discussion depth would further improve readability.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important and timely question, and the core findings are likely to be robust. However, the blocking concern regarding the error analysis for the time-rescaling factors (R1-M1) must be addressed to establish the central claim. The interpretation of the correlation with interaction energy (R1-M2) also needs to be strengthened. If these concerns are satisfactorily resolved, the manuscript would be a strong contribution to the field.

## Risk / unsupported claims
- The claim that the missing frictional effects are "reminiscent of internal friction" is not directly supported by the data and is a speculative interpretation of a correlation. The data only show a correlation with inter-chain interaction energy, not with any direct measure of intra-chain friction. This claim should be presented as a hypothesis, not a conclusion.