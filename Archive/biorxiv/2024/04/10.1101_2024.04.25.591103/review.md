## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary figure legends as provided.
- **Assessment boundary** Scientific validity, technical soundness, and significance of the claims as presented in the provided manuscript text. No assessment of data availability or code functionality beyond what is stated.
- **Shared manuscript claim summary** The authors present a comprehensive map of specificity encoding in a PDZ domain (PDZ3 from PSD-95) by measuring over 200,000 energetic interactions between domain and ligand mutations. They identify 17 major specificity-encoding residues that control binding to six ligand positions, demonstrate that specificity can be reprogrammed combinatorially, and show that accurate prediction requires accounting for non-additive interactions both within the domain and within the ligand.
- **Visible evidence base** Abstract, full introduction, results sections with figure references (Figures 1-5, S1-S11), discussion, methods, and supplementary figure legends as provided in the manuscript text.
- **Missing materials affecting confidence** Actual figures and supplementary figures are not provided, only their legends and in-text references. Specific numerical values for key results (e.g., R² values, effect sizes, confidence intervals) are partially reported but not fully detailed. The full methods for the bindingPCA assay are referenced but not completely described in the provided text.

## Reviewer
- **Overall assessment** This manuscript presents a technically impressive and comprehensive dataset that substantially advances our understanding of how binding specificity is encoded in a protein-protein interaction. The experimental design is rigorous, combining deep mutational scanning with thermodynamic modeling to map both direct and allosteric determinants of specificity. The finding that specificity is modularly encoded and can be predictably reprogrammed is of broad interest. However, several technical concerns need to be addressed, particularly regarding the interpretation of non-additive interactions, the generalizability of the findings beyond this single PDZ domain, and the statistical rigor of some analyses.
- **Who would be interested in the results, and why** Researchers in protein engineering, computational biology, and evolutionary biology would find this work highly relevant. The demonstration that specificity can be reprogrammed through a small set of modular residues has direct implications for designing proteins with novel binding specificities. The comprehensive mapping approach also provides a template for studying other protein families. Additionally, those interested in the biophysical basis of molecular recognition and the role of allostery in protein function would find the results compelling.
- **Major strengths** 1) The scale and comprehensiveness of the dataset, with over 200,000 energetic interactions measured, is unprecedented for a PDZ domain. 2) The combination of trans-double mutant cycles with combinatorial reprogramming provides a powerful framework for dissecting both additive and non-additive contributions to specificity. 3) The identification of modular, spatially clustered specificity-encoding residues is a clean and interpretable result. 4) The validation of the model on an independent large-scale dataset (150,367 combinatorial mutants) strengthens the conclusions. 5) The inclusion of abundance controls to rule out protein stability effects is a thoughtful addition.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** The major technical concern is the interpretation of non-additive interactions and whether the two-state thermodynamic model adequately captures the complexity of binding. The authors need to more rigorously demonstrate that the identified "energetic couplings" are not artifacts of the modeling approach. Additionally, the generalizability of the findings to other PDZ domains and other protein families needs to be discussed more carefully, as the authors only study one domain with one ligand.
- **Assessment against Nature-style criteria** 
  - **Originality** High. This is the first complete map of specificity encoding for a PDZ domain, and the approach of combining comprehensive trans-mutagenesis with combinatorial reprogramming is novel.
  - **Scientific importance** High. The findings have implications for understanding molecular recognition, protein evolution, and protein engineering. The modular architecture of specificity encoding is a conceptually important result.
  - **Interdisciplinary readership** Moderate to high. The work will appeal to biochemists, structural biologists, computational biologists, and protein engineers. The conceptual framework of "specificity encoding" is broadly applicable.
  - **Technical soundness** Generally strong, but with some concerns about the interpretation of non-additive interactions and the statistical treatment of the data. The experimental design is rigorous, but the modeling assumptions need to be more thoroughly validated.
  - **Readability for nonspecialists** The manuscript is well-written and the main findings are clearly presented. However, the technical details of the thermodynamic modeling and the interpretation of energetic couplings may be challenging for nonspecialists. The figures, if well-constructed, would help, but they are not available for assessment.
- **Recommendation posture** Supportive if technical concerns are resolved. The core findings are likely correct and important, but the interpretation of non-additive interactions and the generalizability of the results need to be addressed more rigorously.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of the thermodynamic model
- **Claim pointer** The authors claim that "accurate prediction requires energetic couplings within the protein and within the ligand" and that their two-state thermodynamic model with pairwise interaction terms accurately predicts binding across >150,000 combinatorial variants.
- **Evidence pointer** Results section "Accurate prediction requires energetic couplings within the protein and within the ligand", Figure 5, Methods "Modeling phenotype to free energy with MoCHI"
- **Concern** The two-state thermodynamic model assumes a specific relationship between fitness and binding free energy. The authors need to more rigorously demonstrate that the model is correctly specified and that the identified pairwise interaction terms are not artifacts of model misspecification. Specifically, the authors should: (1) show that the model residuals are normally distributed and that the Z-score transformation is appropriate; (2) demonstrate that the model with pairwise interactions is significantly better than the additive model using appropriate statistical tests (e.g., likelihood ratio tests); (3) validate the model on held-out data more thoroughly, perhaps by predicting binding of variants not used in model fitting; (4) discuss the potential for higher-order interactions (beyond pairwise) and whether the model adequately captures these.
- **Why it matters** The central claim of the paper is that specificity can be predictably reprogrammed, and this relies on the accuracy of the thermodynamic model. If the model is misspecified, the identified "energetic couplings" may be spurious, and the predictive power may be overstated.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability of findings
- **Claim pointer** The authors state that "this approach of measuring the specificities of thousands of proteins in a single experiment will allow many different types of molecular interaction to be understood and interpretably reprogrammed."
- **Evidence pointer** Discussion section
- **Concern** The study is limited to a single PDZ domain (PDZ3 from PSD-95) binding to a single ligand (C-terminal peptide from CRIPT). The authors should more carefully discuss the extent to which their findings are likely to generalize to other PDZ domains and other protein families. Specifically, they should address: (1) whether the modular architecture of specificity encoding is likely to be a general feature of protein-protein interactions or a specific feature of this particular domain-ligand pair; (2) whether the number of specificity-encoding residues (17) is likely to be typical; (3) whether the approach would be feasible for interactions with different affinities, different binding modes, or different domain families.
- **Why it matters** The broader significance of the work depends on its generalizability. If the findings are specific to this one interaction, the impact is substantially reduced.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Statistical rigor of interaction identification
- **Claim pointer** The authors identify "over 600 non-zero energetic couplings" and "20 pairs of PDZ3-ligand residues are enriched for specificity-changing mutations."
- **Evidence pointer** Results section "Hundreds of mutations in a PDZ domain change its binding specificity", Figure 3, Methods "Analysis of residuals to quantify energetic couplings"
- **Concern** The identification of significant energetic couplings relies on a Z-test with Benjamini-Hochberg correction. The authors should provide more details on: (1) the number of tests performed and the statistical power to detect interactions; (2) the effect size distribution of the identified interactions; (3) whether the results are robust to different statistical thresholds; (4) whether the hypergeometric test for enrichment of specificity-changing mutations in domain-ligand pairs is appropriately applied, given that the number of mutations per residue varies.
- **Why it matters** The identification of specific residues and pairs as "major specificity-encoding" is a key result. If the statistical identification is not robust, the specific residues highlighted may not be reliable.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 1 and associated text
- **Evidence pointer** Results section "Quantifying an extended genetic and energetic landscape for peptide recognition", Figure 1
- **Issue** The description of the different libraries (N-terminal, C-terminal, cis double mutant, trans double mutant) is somewhat confusing. The authors should provide a clearer schematic or table summarizing the design of each library and what specific question each addresses.
- **Required correction** Add a summary table or schematic in Figure 1 or the main text that clearly delineates the purpose and design of each of the five libraries.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Interpretation of allosteric effects
- **Affected element** Discussion of allosteric encoding
- **Evidence pointer** Results section "Direct and local allosteric encoding of specificity", Discussion
- **Issue** The authors describe "allosteric" effects for residues that are not direct contacts. However, the distinction between "allosteric" and "direct but through water-mediated or long-range electrostatic interactions" is not always clear. The authors should more carefully define what they mean by allosteric in this context.
- **Required correction** Provide a clearer operational definition of "allosteric" as used in this study, and discuss the potential mechanisms by which non-contact residues might exert their effects.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Comparison to previous work
- **Affected element** Introduction and Discussion
- **Evidence pointer** Introduction, Discussion
- **Issue** The authors mention previous studies on PDZ domain specificity but do not provide a detailed quantitative comparison of their findings with those from previous high-throughput studies (e.g., phage display). A more explicit comparison would help contextualize the novelty of their results.
- **Required correction** Add a paragraph in the Discussion that directly compares the specificity-encoding residues identified here with those identified in previous studies, highlighting both agreements and discrepancies.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Methods section on library design
- **Evidence pointer** Methods "Library construction"
- **Issue** The description of the combinatorial reprogramming library design is brief. The authors state that mutations were chosen based on "residual values" and "FDR," but the exact selection criteria are not fully specified.
- **Required correction** Provide a more detailed description of the criteria used to select the 6 PDZ mutations and 18 CRIPT mutations for the combinatorial library, including the specific thresholds used.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 5
- **Evidence pointer** Results section "Accurate prediction requires energetic couplings within the protein and within the ligand", Figure 5
- **Issue** The authors show that the model with pairwise interactions performs better than the additive model, but the improvement is described as "nearly 10% increase in performance." It would be helpful to show the performance metrics (e.g., R², RMSE) for both models on the same plot for direct comparison.
- **Required correction** In Figure 5, include a panel that directly compares the predictive performance of the additive model vs. the model with pairwise interactions, showing the relevant metrics.

## Risk / unsupported claims
- The claim that this is the "first complete map of how binding specificity is encoded in the sequence of a protein domain" is strong and cannot be fully verified from the provided text alone, as it depends on the definition of "complete" and the scope of previous work. The authors should more carefully qualify this claim.
- The statement that "specificity for all six sites can be simultaneously re-programmed" is supported by the data, but the practical utility of this reprogramming (e.g., whether the reprogrammed proteins retain function in a cellular context) is not demonstrated.
- The claim that the approach "will allow many different types of molecular interaction to be understood and interpretably reprogrammed" is speculative and not directly supported by the data presented, which only covers a single PDZ domain-ligand pair.
- The assertion that "changes in specificity drive evolution, disease and therapeutic efficacy" is presented as motivation but is not directly tested or supported by the data in this manuscript.