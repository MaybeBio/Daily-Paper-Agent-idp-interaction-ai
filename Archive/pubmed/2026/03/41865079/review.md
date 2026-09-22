## Review setup
- **Input scope** Full manuscript text, including abstract, main text, figures (descriptions only), tables, and methods.
- **Assessment boundary** Scientific content, methodological soundness, validity of claims relative to the evidence presented, and alignment with the stated scope of the journal. Editorial or formatting issues are noted only where they affect scientific clarity.
- **Shared manuscript claim summary** The authors use microsecond-level all-atom molecular dynamics simulations of 24 copies of the FUS RGG3 fragment to characterize the dense phase. They report that the system is highly dynamic with rapid partner exchange, short contact lifetimes, and heterogeneous binding interfaces, yet exhibits statistically defined interaction motifs (DRGG(F/Y)) and a robust fractal topology (dF ≈ 1.86) across scales. They further report a small configurational entropy loss upon condensation and a modest reduction in diffusion, and propose that solvent entropy release may contribute to the thermodynamics of condensate formation.
- **Visible evidence base** Main text, Tables 1 and 2, Figures 1–5 (descriptions), Methods section, and references to Supplementary Information (figures, movie, data).
- **Missing materials affecting confidence** Supplementary figures, movie, and data files were not provided. Force field parameters, simulation input files, and convergence criteria are not fully detailed. No experimental validation data are included.

## Reviewer
- **Overall assessment** This manuscript presents a detailed computational study of a biologically relevant IDR dense phase, with a level of atomistic resolution that is still relatively rare in the field. The central observation—that a highly dynamic, transiently interacting system can nevertheless exhibit statistically robust interaction motifs and scale-invariant cluster topology—is interesting and potentially significant. The use of three independent replicas and the application of a fractal framework to connect molecular parameters to mesoscale architecture are commendable. However, the strength of the conclusions is limited by the short simulation timescales, the absence of experimental validation, and the lack of a systematic analysis of force field sensitivity. The claim regarding solvent entropy compensation is intriguing but rests on indirect estimates. Overall, the work is technically sound within its stated scope, but the broader significance for understanding condensate biology would be strengthened by addressing the concerns below.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, and intrinsically disordered proteins, particularly those interested in the molecular determinants of condensate internal organization and dynamics. The methodological approach (all-atom MD combined with fractal analysis) will also be of interest to computational biophysicists developing or applying simulation-based tools to study dense protein systems.
- **Major strengths**
  1. The study addresses a timely and important question: how can disordered, dynamic systems give rise to reproducible, well-defined mesoscale properties?
  2. The use of all-atom MD with a modern force field and water model, combined with three independent replicas, provides a reasonable level of sampling for a system of this size.
  3. The application of the fractal model to translate molecular-level parameters (valency, compactness) into predictions about cluster architecture across scales is a valuable conceptual contribution.
  4. The analysis of interaction motifs and the identification of a repeating DRGG(F/Y) sequence as a driver of contacts is a concrete, testable finding.
  5. The comparison of configurational entropy and diffusion between dilute and dense phases provides quantitative insight into the thermodynamic and dynamic consequences of condensation.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / sampling convergence
- **Claim pointer** The authors claim that the system reaches a "converged state" and that the last 0.3 µs of each 1 µs trajectory is representative of the dense phase equilibrium.
- **Evidence pointer** Methods, "Dense-phase simulations"; Results, "RGG3 self-associates in the dense phase"; Table 2.
- **Concern** The manuscript does not provide a rigorous demonstration of equilibration or convergence. The valency and cluster size appear to increase over time (Figure 1C), and the authors state that the system "settles" only in the last 0.3 µs. For a system of 24 chains at ~89 g/L, 1 µs may be insufficient to achieve a well-mixed, equilibrated dense phase, especially given the slow dynamics often observed in such systems. The analysis window of 0.3 µs is short, and the authors do not show block-averaging or other convergence diagnostics for key observables (valency, Rg, SASA, entropy).
- **Why it matters** If the system is not fully equilibrated, all derived quantities (valency, fractal dimension, entropy change, diffusion coefficients) may be biased by the initial conditions and the approach to equilibrium, undermining the central claims of the paper.
- **Resolution test** Provide a clear demonstration of convergence: e.g., time evolution of block-averaged valency, Rg, and SASA with error bars; autocorrelation times for key observables; and a comparison of the first and second halves of the analysis window. If possible, extend at least one replica to 2–3 µs to show that the properties are stable.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / force field sensitivity
- **Claim pointer** The authors use the Amber99SB-ILDN force field with TIP4P-D water and state that this combination "has been shown to yield accurate modeling of IDPs in water."
- **Evidence pointer** Methods, "Single-copy simulations" and "Dense-phase simulations"; Discussion.
- **Concern** The manuscript relies on a single force field/water model combination. While TIP4P-D is a reasonable choice for IDPs, it is known to potentially over-stabilize certain interactions, and the balance between protein-protein and protein-water interactions is critical for dense phase properties. The authors do not discuss or test the sensitivity of their key findings (valency, fractal dimension, interaction motifs) to the choice of force field.
- **Why it matters** The conclusions about interaction motifs and fractal topology are presented as robust features of the RGG3 sequence. Without evidence that these features are not artifacts of the specific force field, the generality of the claims is uncertain.
- **Resolution test** Perform at least one additional simulation (or a shorter test) with an alternative force field (e.g., CHARMM36m, a99SB-disp) and compare key observables (valency, Rg, dF, contact enrichment). Alternatively, provide a detailed discussion of why the chosen force field is expected to be reliable for this specific system, supported by comparisons to experimental data where available.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance / validation
- **Claim pointer** The authors state that "solvent entropy may significantly contribute to the thermodynamics of condensate formation" and estimate a large solvent entropy increase upon condensation.
- **Evidence pointer** Results, "RGG3 dense phase is dynamic and structurally heterogeneous"; Figure 2G; Discussion.
- **Concern** The estimate of solvent entropy change is based on a simple counting of water molecules in a 1.25 nm shell and a per-molecule entropy value from the literature. This is a very rough approximation that neglects correlations, the heterogeneity of the shell, and the fact that the entropy of released water depends on its local environment. The authors acknowledge this is an upper bound, but the magnitude of the effect (~141 kcal/mol) is presented as significant without any experimental or more rigorous computational validation.
- **Why it matters** The claim about solvent entropy is one of the more novel and potentially impactful findings. If it is based on an unreliable estimate, it could mislead the field. A more careful treatment is needed to support the claim.
- **Resolution test** Either (a) perform a more rigorous calculation of solvent entropy (e.g., using the two-phase thermodynamics method or a similar approach), or (b) soften the claim and clearly state that this is a speculative estimate that requires experimental verification. If possible, compare the estimated entropy change to experimental calorimetric data for similar systems.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interdisciplinary readership / clarity
- **Claim pointer** The authors state that the fractal dimension dF ≈ 1.86 indicates a "low-dimensionality with a relatively loose organization" and that this is "robust" across replicas.
- **Evidence pointer** Results, "RGG3 clusters exhibit robust scaling"; Figure 5; Table 2.
- **Concern** The fractal dimension is derived from a model that assumes a specific relationship between valency, compactness, and cluster size. The authors do not discuss the limitations of this model or whether the derived dF is sensitive to the choice of the model parameters (e.g., the prefactor κ). The claim of "robustness" is based on the small standard deviation between replicas, but this does not address the model's systematic uncertainty.
- **Why it matters** The fractal dimension is a key output of the paper and is used to make claims about the mesoscale organization of the condensate. If the model is not well-validated, the interpretation of dF could be misleading.
- **Resolution test** Provide a sensitivity analysis of dF to the model parameters (κ, valency, Rg). Discuss the assumptions of the fractal model and its applicability to this system. If possible, validate the predicted cluster structure against an independent measure (e.g., direct analysis of cluster geometry in the simulations).

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness / statistical analysis
- **Claim pointer** The authors identify "statistically defined interaction hotspots" and a repeating DRGG(F/Y) motif as a driver of intermolecular contacts.
- **Evidence pointer** Results, "Interaction motifs in RGG3 can be statistically defined"; Figure 3.
- **Concern** The statistical significance of the identified hotspots is not rigorously established. The authors compare observed contact frequencies to expected frequencies based on amino acid abundance, but they do not provide confidence intervals or p-values. The analysis is performed on a single system (24 copies), and the number of independent observations (contacts) may be limited.
- **Why it matters** The identification of specific interaction motifs is a central claim. If the hotspots are not statistically robust, the claim that the RGG3 sequence encodes a specific interaction pattern is weakened.
- **Resolution test** Provide a statistical test for the enrichment of contacts (e.g., a bootstrap or permutation test) and report confidence intervals for the contact frequencies. Show that the identified motifs are consistently enriched across all three replicas and across different time windows.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract, Introduction.
- **Issue** The abstract and introduction use terms like "fractal formalism," "configurational entropy," and "dense phase" without defining them for a broader readership. The significance of the findings could be lost on readers not deeply familiar with the biophysics of IDPs.
- **Required correction** Briefly define key terms in the introduction and abstract, and consider adding a sentence in the abstract that explains why the findings matter for understanding condensate biology in plain language.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness / reporting
- **Affected element** Methods, "Dense-phase simulations"
- **Evidence pointer** Methods, "Dense-phase simulations"; Table 1.
- **Issue** The manuscript states that "two of the boxes were additionally simulated for 50 ns in the NVT ensemble for viscosity determination," but it is unclear why only two of the three replicas were used for this purpose. The viscosity values are used to correct diffusion coefficients, so this inconsistency should be explained.
- **Required correction** Clarify why the third replica was not used for viscosity determination, or report viscosity for all three replicas.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness / reporting
- **Affected element** Methods, "Entropy calculation"
- **Evidence pointer** Methods, "Entropy calculation"; Table 2.
- **Issue** The entropy calculation uses the MIST approximation, but the manuscript does not specify the order of the approximation or the basis set used. This makes it difficult to assess the accuracy of the reported entropy values.
- **Required correction** Provide details on the MIST implementation (e.g., order of approximation, dihedral angle definitions) and cite the relevant literature.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Scientific importance / context
- **Affected element** Discussion
- **Evidence pointer** Discussion.
- **Issue** The discussion compares the results to those of a previous study on Lge1, but does not discuss how the findings relate to the broader literature on FUS phase separation, particularly experimental studies that have mapped interaction sites or measured dynamics in FUS condensates.
- **Required correction** Add a paragraph discussing the relationship between the simulation results and experimental data on FUS, including any discrepancies or agreements.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Figure 1
- **Evidence pointer** Figure 1.
- **Issue** The figure caption for Figure 1 is dense and does not clearly explain what is shown in each panel. The reader is left to infer the meaning of the "dense phase" snapshot and the "largest cluster size" plot.
- **Required correction** Expand the figure caption to explain each panel in more detail, including the definition of "valency" and "cluster size."

## Risk / unsupported claims
- The claim that "solvent entropy may significantly contribute to the thermodynamics of condensate formation" is based on a rough estimate and is not supported by rigorous calculation or experiment. This should be presented as a hypothesis, not a finding.
- The claim that the system exhibits a "robust" fractal topology is based on a model with unvalidated assumptions and a short analysis window. The robustness is not fully established.
- The claim that the identified DRGG(F/Y) motifs are "drivers" of intermolecular contacts is based on statistical enrichment, but the statistical significance is not rigorously tested.
- The claim that the simulations represent the "interior of a biomolecular condensate" is an assumption. The system is a model dense phase, and its relationship to real condensates (which may have heterogeneous composition, RNA, etc.) is not established.
- The comparison of diffusion coefficients between the dense and dilute phases is based on a limited analysis window and may be affected by the lack of full equilibration.