## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Theoretical framework, analytical derivations, computational validation, and interpretation of results as presented
- **Shared manuscript claim summary** The authors propose a graph-theoretic framework, grounded in an Einstein model of thermal vibrations, to derive topological descriptors (Kirchhoff index, Randić resistance, local/global force constants) for protein structures. They apply these descriptors to MD trajectories of Trp-cage and HP-36 to characterize folded, unfolded, and misfolded states, claiming the descriptors can detect rigid misfolded conformations.
- **Visible evidence base** Main text with equations, figures referenced (Figures 1–7), and methodological descriptions. Supplementary materials mentioned but not provided.
- **Missing materials affecting confidence** Supplementary Sections S1, S2, S4; full figure contents; MD trajectory details from the original source; computational code or data availability statements

## Reviewer
- **Overall assessment** The manuscript presents an interesting conceptual bridge between graph theory and statistical mechanics, with potential utility for analyzing protein conformational ensembles. The theoretical development is largely sound, though some derivations are not fully shown in the main text. The application to Trp-cage and HP-36 is a reasonable proof of concept, but the validation is limited to a single trajectory per protein and the claims about detecting misfolded states rest on qualitative visual inspection rather than quantitative benchmarks. The work is likely to interest the protein biophysics community, but the practical advantages over existing order parameters are not yet convincingly demonstrated.
- **Who would be interested in the results, and why** Researchers in protein folding, intrinsically disordered proteins, and computational biophysics would find the graph-based descriptors potentially useful for characterizing conformational ensembles. The theoretical connection between graph topology and mechanical stiffness may also interest the broader network science community. However, the impact will depend on whether these descriptors offer practical advantages over established metrics like RMSD, radius of gyration, or contact maps.
- **Major strengths** The theoretical framework connecting graph Laplacian properties to mechanical force constants is elegant and clearly presented. The analytical result relating the Kirchhoff index to average shortest path length for linear chains is a useful contribution. The application to MD trajectories demonstrates feasibility, and the observation of distinct substates in the (K, ξ) and (K, l₀) plots is intriguing.
- **Major Concerns** The validation is limited to a single MD trajectory per protein, and the claim that the descriptors can "detect transient misfolded rigid states" is based on visual inspection of a few time points rather than a systematic comparison with known misfolded structures. The physical interpretation of the Einstein model parameters (ϵ, reference state) is not fully justified. The relationship between the graph-based descriptors and established order parameters is only partially explored, leaving the practical added value unclear.
- **Minor Comments** The notation is sometimes dense and could benefit from a summary table of symbols. The choice of cut-off radius (0.6 nm) is stated but not justified. The discussion of frustration is speculative and could be either expanded or removed. The conclusion section is brief and could better contextualize the findings within the broader protein folding literature.
- **Technical failings that need to be addressed before the case is established** The derivation of Equation (44) is not shown in the main text; the claim that it predicts the upper bound of K for all l₀ values needs more rigorous justification. The statistical significance of the differences between folded and unfolded descriptor distributions is not assessed. The sensitivity of the results to the cut-off radius and to the choice of reference state is not examined.
- **Assessment against Nature-style criteria** Originality: The conceptual link between graph topology and Einstein model thermodynamics is novel, though the individual components are established. Scientific importance: Potentially useful for characterizing disordered protein states, but the practical impact is not yet demonstrated. Interdisciplinary readership: The framework could appeal to both biophysicists and network scientists, but the presentation is somewhat specialized. Technical soundness: The theory appears sound, but key derivations are relegated to supplementary materials and validation is limited. Readability for nonspecialists: The manuscript is accessible to a technical audience but would benefit from clearer motivation and a more explicit statement of what the new descriptors offer over existing methods.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding the derivation of Equation (44), the statistical validation of the descriptors' discriminative power, and a clearer demonstration of practical advantages over existing order parameters.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that Equation (44) predicts the upper limit of K for all observed values of l₀ in the MD trajectory, and that this is "unexpected" given the derivation for a linear chain.
- **Evidence pointer** Section 2.2.2, Figure 5a
- **Concern** The derivation of Equation (44) is not shown in the main text, and the claim that it predicts the upper bound of K for all l₀ values is not rigorously justified. The authors explain this by mapping observed structures to shorter linear chains, but this mapping is not formalized. It is unclear whether this is a general property or an artifact of the specific trajectory analyzed.
- **Why it matters** This is a central theoretical claim that underpins the interpretation of the (K, l₀) plot. If the relationship is not general, the utility of the descriptor for characterizing arbitrary protein conformations is weakened.
- **Resolution test** Provide the full derivation of Equation (44) in the main text or supplementary, and demonstrate analytically or with additional simulations that the upper-bound prediction holds for a diverse set of protein conformations beyond the single trajectory analyzed.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation
- **Claim pointer** The authors claim that the graph-based descriptors "permit the detection of transient misfolded rigid states" in the unfolded ensemble.
- **Evidence pointer** Section 2.2.2, Figures 3, 5, 6
- **Concern** The identification of misfolded states is based on visual inspection of a few selected time points (e.g., t5) where K is high despite low ξ. There is no systematic comparison with known misfolded structures, no statistical test of whether the descriptor distribution in the "misfolded" region differs significantly from the unfolded background, and no assessment of how often such states occur.
- **Why it matters** The ability to detect misfolded states is a key claimed application. Without quantitative validation, the claim remains anecdotal and the practical utility of the descriptors is not established.
- **Resolution test** Provide a systematic analysis of the trajectory, identifying all time points with high K and low ξ, and compare their structural features (e.g., contact maps, secondary structure) with known misfolded conformations. Include a statistical test (e.g., permutation test) showing that the descriptor values in these regions are significantly different from the unfolded background.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** The authors state that the MD trajectory of Trp-cage was generated in a previous unrelated work, and that the trajectory of HP-36 is analyzed in the supplementary materials.
- **Evidence pointer** Section 3.2, Section 2.2
- **Concern** The manuscript does not provide sufficient details about the MD simulation parameters (force field, water model, equilibration protocol, etc.) for either protein. The HP-36 results are only in the supplementary materials, which were not provided for review. This limits the reproducibility of the results.
- **Why it matters** Reproducibility is a core requirement for computational studies. Without full simulation details and access to the HP-36 analysis, the results cannot be independently verified.
- **Resolution test** Provide full simulation parameters in the main text or supplementary, and make the HP-36 analysis available for review. Consider depositing the trajectories or providing access to the analysis scripts.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation
- **Claim pointer** The authors state that the entropic contribution to the free energy is "parameter free" and that the enthalpic term depends on a single parameter ϵ, which is treated as variable.
- **Evidence pointer** Section 2.1.4, Equations (52)–(58)
- **Concern** The physical meaning of ϵ is not discussed, and the choice of reference state (k₀, K₀) is not justified. The authors show results for ϵ = −5 but do not explore the sensitivity of the conclusions to this choice. The claim that the entropic term is "parameter free" is technically correct but the overall free energy is not, and the interpretation of the free-energy differences depends on the unknown ϵ.
- **Why it matters** The free-energy framework is a central contribution, but its practical utility depends on the ability to assign a meaningful value to ϵ or to show that conclusions are robust to its variation.
- **Resolution test** Discuss the physical interpretation of ϵ and the reference state. Perform a sensitivity analysis showing how the free-energy profiles and the identification of misfolded states change for a range of ϵ values.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Notation
- **Evidence pointer** Section 2.1
- **Issue** The manuscript uses many symbols (kᵢ, K, Kᵢⱼ, Kf, l₀, ξ, ϵ) without a consolidated notation table, which makes the text difficult to follow.
- **Required correction** Add a table of symbols and definitions, ideally at the end of the introduction or beginning of Section 2.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodology
- **Affected element** Cut-off radius
- **Evidence pointer** Section 3.1
- **Issue** The choice of cut-off radius R = 0.6 nm is stated without justification or sensitivity analysis.
- **Required correction** Provide a brief justification for this value and, if possible, show that the main conclusions are robust to reasonable variations in R.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure quality
- **Evidence pointer** Figures 3, 5, 6
- **Issue** The figures are referenced but not fully described in the text. The PDF plots in Figure 3 are mentioned but their interpretation is not fully explained.
- **Required correction** Expand the figure captions and add more explicit descriptions in the text of what the reader should observe in each panel.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Context
- **Affected element** Discussion of frustration
- **Evidence pointer** Section 2.2.2
- **Issue** The discussion of residual frustration is brief and speculative, and the connection to the graph descriptors is not made quantitative.
- **Required correction** Either expand this discussion with a more concrete analysis (e.g., correlation between frustration indices and kᵢ) or remove it to keep the focus on the main results.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** HP-36 results
- **Evidence pointer** Section 2.2, Supplementary S2
- **Issue** The HP-36 results are only mentioned in passing and are not available for review.
- **Required correction** Ensure the supplementary materials are complete and provide a summary of the HP-36 results in the main text, even if brief.

## Risk / unsupported claims
- The claim that Equation (44) predicts the upper bound of K for all l₀ values is not rigorously established (derivation not shown, mapping to shorter chains not formalized).
- The claim that the descriptors can "detect transient misfolded rigid states" is based on anecdotal visual inspection rather than systematic quantitative validation.
- The physical interpretation of ϵ and the reference state in the free-energy model is not provided, and the sensitivity of conclusions to these choices is not assessed.
- The statistical significance of differences between folded and unfolded descriptor distributions is not evaluated.
- The generalizability of the findings beyond the single MD trajectory per protein is not established.