## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and conclusions. No supplementary materials were provided.
- **Assessment boundary** Evaluation is limited to the scientific content, methodology, and claims as presented in the provided manuscript text. No external validation or replication of the computational results was performed.
- **Shared manuscript claim summary** The authors use molecular dynamics simulations and transition network analysis to show that glycosaminoglycans (GAGs) and POPC lipids induce distinct disorder-to-order conformational transitions in Aβ1-42, with GAGs promoting β-hairpin formation via ion descreening and lipids promoting both α-helical and β-sheet structures via hydrophobic interactions.
- **Visible evidence base** Main text figures (Figures 1-5), tables (Table 1), and equations (Equations 1-5) are referenced. Supplementary figures and tables (Figures S1-S7, Tables S1-S2) are mentioned but not provided.
- **Missing materials affecting confidence** Supplementary materials (Figures S1-S7, Tables S1-S2), simulation parameter files, force field parameter details, and raw trajectory data are not available. This limits full verification of statistical analyses and methodological reproducibility.

## Reviewer
- **Overall assessment** The manuscript presents a computationally rigorous and conceptually interesting comparison of Aβ conformational behavior under three different environmental conditions. The use of consistent descriptors across systems to build transition networks is a strength, enabling direct comparison. The proposed mechanism for GAG-induced conformational change via sodium ion descreening is novel and plausible. However, the study relies on limited sampling (single or few trajectories per system) and the statistical robustness of the transition networks is not fully demonstrated. The claim that GAGs cause conformational change with "hardly any direct interactions" requires stronger quantitative support. The manuscript is well-written and accessible, but the biological implications are somewhat speculative given the simplified model systems.
- **Who would be interested in the results, and why** Researchers in the fields of amyloid biology, intrinsically disordered proteins, computational biophysics, and Alzheimer's disease mechanisms would find this work relevant. The methodological approach of using transition networks to compare conformational ensembles under different conditions is of interest to computational chemists and biophysicists. The proposed ion-descreening mechanism for GAG action could inform experimental studies on amyloid aggregation modulators.
- **Major strengths** 1) Consistent use of three descriptors across all systems allows direct comparison of conformational landscapes. 2) The transition network approach provides an intuitive visualization of complex conformational dynamics. 3) The identification of a novel mechanism (ion descreening) for GAG-induced conformational change is mechanistically insightful. 4) The comparison between GAG and lipid effects highlights distinct pathways to ordered states. 5) The manuscript is clearly written and the methodology is described in sufficient detail for reproduction.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** R1-M1 (sampling and statistical robustness), R1-M2 (quantitative support for "hardly any direct interactions"), R1-M3 (lack of validation for transition network parameters).
- **Assessment against Nature-style criteria** **Originality**: The work is original in its application of transition networks to compare Aβ behavior under different co-solute conditions and in proposing a specific ion-descreening mechanism. However, the general concept of disorder-to-order transitions in Aβ induced by co-solutes is not new. **Scientific importance**: The findings are of moderate importance, providing mechanistic hypotheses that could guide future experimental work, but the simplified model systems limit direct biological translation. **Interdisciplinary readership**: The work bridges computational chemistry, biophysics, and neurobiology, but the technical nature may limit accessibility to a broad interdisciplinary audience. **Technical soundness**: The methodology is generally sound, but concerns about sampling convergence and parameter sensitivity need addressing. **Readability for nonspecialists**: The manuscript is well-structured and explains concepts clearly, though some sections assume familiarity with MD simulation and network analysis techniques.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding sampling convergence, quantitative support for the interaction analysis, and validation of network parameters.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the transition networks reveal significant differences in conformational preferences between Aβ-only, Aβ-GAG, and Aβ-POPC systems, with the GAG system showing a "drastic shift" toward β-sheet-rich states.
- **Evidence pointer** Figures 1, 2, 4; Table S2 (not provided)
- **Concern** The manuscript does not provide sufficient evidence that the MD simulations have converged. The Aβ-only system was simulated for 6 μs (single trajectory), while Aβ-GAG and Aβ-POPC were simulated for 4 μs each (1×4 μs and 2×2 μs, respectively). For intrinsically disordered proteins, which sample vast conformational space, these simulation lengths may be insufficient to achieve equilibrium or to capture rare transitions. The transition networks are built from these trajectories, and if the sampling is incomplete, the resulting networks may not represent the true conformational landscape. The authors do not provide convergence metrics (e.g., time-dependent free energy estimates, cluster size convergence, or replica independence checks). Without such evidence, the "drastic shift" in population could be an artifact of insufficient sampling rather than a genuine physical effect.
- **Why it matters** The central claim of the paper is that GAGs and lipids induce distinct disorder-to-order transitions in Aβ. If the simulations are not converged, the observed differences between systems could be due to sampling noise rather than genuine biophysical differences. This would undermine the primary conclusion and the proposed mechanism.
- **Resolution test** Provide convergence analysis, such as splitting trajectories into halves and comparing resulting networks, computing time-dependent free energy surfaces, or performing multiple independent simulations with different initial conditions. Show that the population distributions and network topologies are stable across these tests.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors state that "Aβ was rarely in direct contact with the GAG" and that the GAG's effect is indirect, primarily through sodium ion descreening.
- **Evidence pointer** Figure 3A; Figure S2 (not provided); Section 2.4
- **Concern** The claim that GAG induces conformational change with "hardly any direct interactions" is based on a contact map (Figure 3A) and a supplementary figure (Figure S2) that are not quantitatively analyzed in the text. The authors report that the maximum contact population is approximately 8.5%, but it is unclear what threshold defines "hardly any" and how this compares to typical protein-ligand interactions. Furthermore, the contact map appears to be a time-averaged quantity, which could obscure transient but functionally important interactions. The authors do not provide a quantitative comparison of contact frequencies between the Aβ-GAG system and a control (e.g., Aβ with a non-interacting polyanion). The proposed mechanism of ion descreening is plausible but is inferred rather than directly demonstrated. The authors do not show that sodium ion depletion near Aβ is causally linked to the observed conformational change, nor do they rule out other indirect effects (e.g., changes in water structure, excluded volume effects).
- **Why it matters** The novelty of the GAG mechanism lies in its indirect nature. If direct interactions are more significant than claimed, the mechanism would be less distinct from the lipid case. The ion descreening hypothesis needs stronger support to be convincing, as it is the primary explanation for the observed conformational change.
- **Resolution test** Provide quantitative analysis of contact frequencies with appropriate thresholds and statistical comparisons. Perform control simulations with a non-interacting polyanion or with varying salt concentrations to directly test the ion descreening hypothesis. Show that sodium ion depletion near Aβ correlates with conformational changes in a dose-dependent manner.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors use transition networks with three descriptors (Nα, Nβ, dNC) and claim that the network layout and community structure reflect the underlying free energy landscape.
- **Evidence pointer** Section 3.2; Figures 1, 2, 4
- **Concern** The choice of descriptors and the parameters used for network construction (e.g., number of states, clustering algorithm, transition counting) are not fully justified. The authors state that the number of descriptors is "up to trial and error" but do not provide a systematic analysis of how the results depend on this choice. The Force Atlas 2 layout algorithm is used for visualization, and the authors note that the coordinate system "mainly arose" from this algorithm. However, the interpretation of the network geometry (e.g., x-axis as dNC, y-axis as secondary structure) relies on this layout, which is a visualization tool rather than a quantitative analysis. The community detection using modularity class is also dependent on the network construction parameters. Without sensitivity analysis, it is unclear whether the observed differences between systems are robust to parameter choices.
- **Why it matters** The transition network is the primary analytical tool of the paper. If the results are sensitive to arbitrary parameter choices, the conclusions drawn from the network comparisons may not be reliable. The interpretation of network geometry as reflecting physical coordinates could be misleading if the layout algorithm imposes artificial structure.
- **Resolution test** Perform sensitivity analysis by varying the number of states, clustering methods, and transition counting schemes. Show that the key findings (e.g., population shifts, community structure) are robust across reasonable parameter ranges. Provide quantitative validation of the network layout by comparing to direct free energy calculations or other dimensionality reduction methods.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.4, Table 1
- **Evidence pointer** Table 1
- **Issue** The water analysis results in Table 1 are presented without error bars or statistical significance tests. The differences in order parameters and H-bond lifetimes between systems are described qualitatively as "no significant difference" or "minor," but no statistical analysis is provided.
- **Required correction** Provide standard deviations or confidence intervals for the reported values and perform appropriate statistical tests (e.g., bootstrap or block averaging) to support claims of similarity or difference.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section 3.1
- **Evidence pointer** Section 3.1
- **Issue** The manuscript states that "some of the MD simulation settings differ slightly between the simulations" but does not specify which settings differ. This lack of detail hampers reproducibility and makes it difficult to assess whether the differences could affect the results.
- **Required correction** Provide a table or detailed description of all simulation parameters for each system, including any differences in settings, and justify why these differences are negligible.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Section 2.5, Discussion
- **Evidence pointer** Section 2.5
- **Issue** The discussion of biological implications is somewhat speculative, particularly regarding the role of GAGs in Alzheimer's disease. The authors state that their findings "agree with experimental findings" but do not provide specific experimental references or quantitative comparisons.
- **Required correction** Strengthen the connection to experimental literature by citing specific studies and discussing how the simulation results quantitatively or qualitatively align with experimental observations.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figures 1, 2, 4
- **Evidence pointer** Figures 1, 2, 4
- **Issue** The transition network figures are described in the text but are not included in the provided manuscript. The reader cannot visually verify the network structures or the described differences between systems.
- **Required correction** Ensure that all figures are included in the final submission and that they are of sufficient resolution to discern network details. Consider adding labels or annotations to highlight key features described in the text.

## Risk / unsupported claims
- The claim that GAGs induce conformational change in Aβ with "hardly any direct interactions" is not quantitatively supported by the provided evidence.
- The proposed mechanism of sodium ion descreening as the primary driver of GAG-induced conformational change is inferred but not directly demonstrated.
- The assertion that the transition networks reflect the underlying free energy landscape is not validated with convergence or sensitivity analyses.
- The statement that the observed differences between systems are "remarkable" is subjective and not backed by statistical comparisons.
- The biological implications regarding Alzheimer's disease are speculative and not directly supported by the simulation data.