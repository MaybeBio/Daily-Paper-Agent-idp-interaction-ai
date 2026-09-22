## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, supplementary information descriptions)
- **Assessment boundary** Scientific claims, methodology, data interpretation, and conclusions as presented in the provided text
- **Shared manuscript claim summary** The authors report that noncovalent lasso entanglements are common in experimentally derived intrinsically disordered protein ensembles, with prevalence strongly influenced by protein length and charge composition, and suggest potential biological relevance based on Gene Ontology enrichment analysis
- **Visible evidence base** Abstract, full methods section, results narrative, discussion, figure references (Figures 1-5), table reference (Table 1), supplementary data file descriptions
- **Missing materials affecting confidence** Figures and tables themselves are not provided; supplementary data files (SI DATA 1-3) are not accessible; specific numerical values for key results are not fully reported in the text; details of the Gaussian double integral implementation and validation are not fully described

## Reviewer
- **Overall assessment** This manuscript addresses a novel and potentially important question about the prevalence of noncovalent lasso entanglements in intrinsically disordered proteins. The combination of experimental ensemble analysis and coarse-grained simulations is appropriate and the scope is ambitious. However, the current presentation has several technical gaps that prevent full evaluation of the claims. The threshold choice for entanglement detection, the validation of the method on IDP ensembles, the treatment of chain length effects in the human proteome analysis, and the interpretation of the GO analysis all require clarification. The core finding that entanglements are common in IDPs is interesting but the mechanistic and functional implications remain speculative at this stage.

- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins, protein biophysics, polymer physics, and computational biology would be interested. The work connects topological concepts from folded proteins to the disordered protein field, which could have implications for understanding IDP function, phase separation, and molecular recognition. The methodological approach could also be of interest to those developing analysis tools for conformational ensembles.

- **Major strengths** The manuscript addresses a genuinely under-explored question in the IDP field. The use of experimentally derived ensembles from the PED database provides a strong empirical foundation. The systematic variation of sequence length and charge composition in simulations is well designed. The connection to the human proteome and GO analysis adds a potentially functional dimension. The writing is generally clear and accessible.

- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness
    - **Claim pointer** The claim that 48% of PED entries contain subpopulations with entangled conformations depends entirely on the choice of the maxG threshold of 0.6.
    - **Evidence pointer** Methods section, Entanglement Analysis; Results section, first paragraph
    - **Concern** The threshold of maxG ≥ 0.6 is stated to be based on "a thorough manual examination of a substantial number of conformations" with reference to a previous study. However, no information is provided about the sensitivity of the results to this threshold. Given that the main quantitative claim (48% of entries) hinges on this single value, it is essential to demonstrate that the conclusions are robust to reasonable variations in the threshold. A small change in threshold could substantially alter the reported percentages.
    - **Why it matters** The central quantitative finding of the paper is directly determined by this arbitrary threshold. Without a sensitivity analysis, the reader cannot assess whether the reported prevalence is a robust property of IDP ensembles or an artifact of the specific cutoff chosen.
    - **Resolution test** Provide a sensitivity analysis showing how the percentage of entangled entries in the PED database varies as a function of the maxG threshold (e.g., 0.4 to 0.8). Additionally, provide a justification for the chosen threshold based on validation against known entangled structures or visual inspection of representative conformations.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness
    - **Claim pointer** The claim that entanglements are "common" in IDPs and that the vast majority involve disordered regions.
    - **Evidence pointer** Results section, first paragraph; Methods section, Entanglement Analysis
    - **Concern** The method requires defining a loop closed by noncovalent interactions. The text does not specify how these contacts are defined (e.g., distance cutoff, residue types involved, whether backbone or sidechain contacts are considered). The definition of the "loop" and "threading" segments is also unclear. For example, can a loop be formed by a single contact or must it be a stable contact? How is the threading segment defined relative to the loop? These details are critical for reproducibility and for interpreting the biological meaning of the results.
    - **Why it matters** Without a precise definition of the entanglement criteria, the results cannot be reproduced or compared with other studies. The biological interpretation of the findings depends on what exactly constitutes an "entanglement" in this context.
    - **Resolution test** Provide a complete and unambiguous description of the algorithm, including the definition of a contact, the minimum loop size, the criteria for a threading event, and any other relevant parameters. Ideally, provide pseudocode or a flowchart of the algorithm.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific importance
    - **Claim pointer** The claim that GO analysis reveals functional enrichment of entangled IDPs/IDRs.
    - **Evidence pointer** Results section, Gene Ontology Analysis; Figure 5
    - **Concern** The GO analysis is presented as revealing functional correlations, but the effect sizes are described as "small" (|Cliff's δ| < 0.33). The biological significance of such small effect sizes is questionable, even if statistically significant. Furthermore, the interpretation that nuclear localization or transcription-related functions are associated with higher entanglement is speculative. The causal direction is unclear: do these functions require entanglement, or do these proteins simply tend to be longer or have different charge compositions? The analysis does not appear to control for protein length or charge, which the authors themselves identify as major determinants of entanglement probability.
    - **Why it matters** The claim of potential biological relevance is a key part of the paper's significance. If the GO enrichment is confounded by length or charge, the functional interpretation is not supported.
    - **Resolution test** Repeat the GO analysis controlling for protein length and charge composition (e.g., by matching or stratification). Report effect sizes and confidence intervals. Discuss whether the observed enrichments are independent of these known determinants.

    - **Concern ID** R1-M4
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical soundness
    - **Claim pointer** The claim that entanglement probability positively correlates with chain compaction, based on the human proteome analysis.
    - **Evidence pointer** Results section, Estimating How Widespread this Phenomenon is in the Human Proteome; Figure 4b,c
    - **Concern** The correlation between entanglement probability and the Flory scaling exponent ν is presented as strong, but no correlation coefficients or statistical significance values are provided in the text. The figure is not available for inspection. It is also unclear whether this correlation is simply a consequence of the known relationship between compaction and contact formation, or whether it provides additional insight beyond what is already known about IDP compaction.
    - **Why it matters** The claim of a strong correlation is a key result, but without quantitative support, it cannot be evaluated.
    - **Resolution test** Provide the correlation coefficient (e.g., Spearman's ρ) and associated p-value for the relationship between entanglement probability and ν. Discuss whether this correlation is expected given the known relationship between compaction and contact probability.

- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Readability
    - **Affected element** Introduction, first paragraph
    - **Evidence pointer** Introduction, first paragraph
    - **Issue** The introduction could benefit from a brief explanation of why noncovalent lasso entanglements might be expected or unexpected in IDPs, given their lack of stable structure. This would help frame the significance of the question for a broader audience.
    - **Required correction** Add one or two sentences in the introduction discussing the theoretical or conceptual reasons why IDPs might or might not form such entanglements, connecting to polymer physics concepts.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Methods, Coarse-Grained Simulations
    - **Evidence pointer** Methods section, Coarse-Grained Simulations of Synthetic Polymers
    - **Issue** The simulation details are sparse. The force field is described as using the "Urry hydropathy scale" with a "one-bead-per-residue representation," but no details are given about the functional form of the potential, the treatment of electrostatics, or the simulation protocol (e.g., equilibration time, number of replicates, error estimation).
    - **Required correction** Provide a more complete description of the simulation model and protocol, including the functional form of the potential, the treatment of long-range interactions, the number of independent simulations, and how statistical uncertainties were estimated.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Readability
    - **Affected element** Results, first paragraph
    - **Evidence pointer** Results section, first paragraph
    - **Issue** The text states that "9, 33, and 24% of entries meet this condition" for having at least 50% entangled conformations, but the order of categories (fully IDP, long IDR, short IDR) is not explicitly stated in the sentence. This creates ambiguity.
    - **Required correction** Rewrite the sentence to explicitly list the categories in the same order as the percentages, e.g., "9% of fully IDPs, 33% of long IDRs, and 24% of short IDRs."

    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Methods, Gene Ontology Analysis
    - **Evidence pointer** Methods section, Gene Ontology Analysis
    - **Issue** The GO analysis is described, but the specific statistical test and multiple testing correction are mentioned only briefly. It is unclear how the "significantly enriched" threshold was applied and whether the analysis was performed at the level of individual GO terms or grouped categories.
    - **Required correction** Provide more detail on the statistical methodology, including the exact test used, how the Benjamini-Hochberg correction was applied, and how the GO terms were selected for analysis.

- **Technical failings that need to be addressed before the case is established** R1-M1 (threshold sensitivity), R1-M2 (algorithm definition), R1-M3 (confounding in GO analysis), R1-M4 (missing quantitative support for correlation)

- **Assessment against Nature-style criteria**
    - **Originality** The question of noncovalent lasso entanglements in IDPs is novel and has not been systematically addressed before. The combination of experimental ensembles and simulations is a fresh approach. This criterion is met.
    - **Scientific importance** The finding that entanglements are common in IDPs could have implications for understanding IDP function, but the functional significance is not yet established. The small effect sizes in the GO analysis weaken the case for immediate biological importance. This criterion is partially met.
    - **Interdisciplinary readership** The topic bridges polymer physics, biophysics, and molecular biology. The writing is generally accessible, but the methods section assumes familiarity with specific computational techniques. The broader significance for cell biology or disease is only briefly mentioned. This criterion is partially met.
    - **Technical soundness** The core methodology is appropriate, but the lack of a threshold sensitivity analysis, incomplete algorithm description, and potential confounding in the GO analysis are significant gaps. This criterion is not fully met.
    - **Readability for nonspecialists** The abstract and introduction are clear, but the results section becomes dense and assumes knowledge of IDP-specific concepts (e.g., charge regions, Flory exponent). The figures are referenced but not available for review. This criterion is partially met.

- **Recommendation posture** Supportive if technical concerns are resolved. The core question is interesting and the approach is sound in principle, but the current manuscript does not fully establish the robustness of the main quantitative claims or the biological significance of the findings. The authors should address the threshold sensitivity, provide a complete algorithm description, control for confounding variables in the GO analysis, and provide quantitative support for the correlation claims.

## Risk / unsupported claims
- The claim that 48% of PED entries contain entangled conformations is not robustly supported without a threshold sensitivity analysis.
- The claim that "most IDPs/IDRs in the human proteome exhibit entangled conformations" (85.18%) is based on a single simulation model and may not be generalizable.
- The GO analysis claims of functional enrichment are potentially confounded by protein length and charge, and the small effect sizes limit the strength of the conclusions.
- The speculation that entanglements "may influence molecular recognition, transcriptional regulation, and phase separation" is not directly supported by the data presented.
- The statement that "at least 75% of known IDPs are polyampholytes" is cited but not verified in the text.