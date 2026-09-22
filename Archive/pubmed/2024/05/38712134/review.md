## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods) as provided
- **Assessment boundary** Scientific claims, experimental design, data analysis, interpretation, and presentation as described in the provided text
- **Shared manuscript claim summary** The authors report the first complete map of specificity encoding for a globular protein domain (PDZ3 of PSD-95) binding a partially fuzzy peptide ligand (CRIPT). They quantify over 200,000 energetic interactions, identify 20 major coupled site pairs organized into six modules, and show that dynamic N-terminal ligand residues contribute to affinity but not specificity through the domain, while communicating with structured residues to enable specificity changes.
- **Visible evidence base** Main text figures referenced (Fig. 1-7), supplementary figures (Fig. S1-S8), tables (table S1-S4), methods descriptions, data and code availability statements
- **Missing materials affecting confidence** Actual figure images, supplementary tables, detailed statistical outputs, model fitting diagnostics, raw sequencing depth information, and complete methods for library construction and selection are not fully visible in the provided text

## Reviewer

- **Overall assessment** This manuscript presents a technically impressive and conceptually important dataset that substantially advances our understanding of how binding specificity is encoded in a protein interaction domain. The scale of the mutagenesis experiments, the integration of direct and allosteric mechanisms, and the distinction between structured and dynamic contributions to specificity are notable strengths. However, several technical aspects require clarification and additional validation before the central claims can be fully accepted. The claim of a "complete map" is ambitious and depends on the completeness of the mutagenesis coverage and the accuracy of the energetic coupling measurements, both of which need further scrutiny.

- **Who would be interested in the results, and why** Researchers studying protein-protein interactions, PDZ domains, intrinsically disordered regions, and molecular recognition mechanisms would find this work highly relevant. The methodological approach combining deep mutational scanning with thermodynamic modeling will interest the protein engineering and directed evolution communities. The findings on allosteric specificity encoding and the modular organization of specificity determinants have implications for understanding signaling network rewiring, disease-associated mutations, and the design of specific protein interaction inhibitors. The distinction between affinity and specificity contributions from dynamic regions addresses a fundamental question in molecular biophysics.

- **Major strengths**
  1. The scale and comprehensiveness of the mutagenesis dataset, with over 200,000 energetic coupling measurements, represents a substantial technical achievement.
  2. The combination of combinatorial library screening with double mutant cycle analysis provides complementary views of the binding landscape.
  3. The identification of both direct and allosteric mechanisms for specificity encoding, with 11 of 20 major couplings being allosteric, is conceptually novel and important.
  4. The systematic treatment of the "fuzzy" N-terminal region as a functional contributor to binding, rather than a passive linker, addresses an understudied aspect of SLiM-mediated interactions.
  5. The modular organization of specificity encoding, with distinct domain residues controlling each ligand position, provides a clear and testable framework.
  6. The use of thermodynamic modeling with explicit treatment of the non-linear relationship between binding energy and observed fitness is methodologically sound.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of the "complete map" claim
- **Claim pointer** The authors claim this is the "first complete map of specificity encoding for a globular protein domain" and that they have quantified ">200,000 energetic interactions between a PDZ domain and its ligand."
- **Evidence pointer** Results section "Quantifying >200,000 energetic interactions between a PDZ domain and its ligand"; Figure 3
- **Concern** The claim of completeness requires that the mutagenesis coverage is truly comprehensive. The methods describe that the combinatorial N- and C-terminal CRIPT libraries were bottlenecked to reduce the combinatorial space from 324 possible variants to 204, which means not all possible combinations were tested. For the trans double mutant library, the design includes "all possible single mutants" in PDZ3 and CRIPT, but the completeness of the double mutant combinations depends on the successful construction and sequencing of all designed variants. The manuscript does not report the fraction of designed variants that were successfully constructed and measured, nor the sequencing depth per variant. Without this information, the "complete map" claim cannot be fully evaluated.
- **Why it matters** The central claim of the paper rests on the completeness of the mutagenesis coverage. If a substantial fraction of variants were missing or poorly sampled, the identification of major specificity encoding residues could be incomplete, and the conclusion that specificity is modular could be an artifact of incomplete sampling.
- **Resolution test** The authors should report the fraction of designed variants successfully constructed and measured, the distribution of sequencing read counts across variants, and the statistical power to detect energetic couplings given the observed coverage. They should also demonstrate that the identified major specificity encoding residues are robust to the exclusion of low-coverage variants.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor of energetic coupling identification
- **Claim pointer** The authors identify 20 major energetically coupled pairs of sites and over 600 non-zero energetic couplings using a Z-test with Benjamini-Hochberg FDR correction.
- **Evidence pointer** Results section "Hundreds of mutations in a PDZ domain change its binding specificity"; Figure 3f-g; Figure 4a
- **Concern** The identification of energetic couplings relies on residuals from an additive model. The manuscript does not fully describe how the error in the residual estimates was calculated, how the Z-test was implemented, and whether the FDR correction accounts for the large number of tests performed (potentially hundreds of thousands of pairwise comparisons). The threshold for calling a coupling "non-zero" and the biological significance of the effect sizes are not clearly defined. Additionally, the authors do not report the distribution of residuals or the false discovery rate at the level of individual couplings versus the level of site pairs.
- **Why it matters** The identification of specific energetic couplings is the foundation for all subsequent claims about modularity, direct versus allosteric mechanisms, and the organization of specificity encoding. If the statistical threshold is too lenient, many false positive couplings could be identified, leading to incorrect conclusions about the number and identity of major specificity determinants.
- **Resolution test** The authors should provide a detailed description of the statistical methods, including how residual errors were estimated, how the Z-test was calibrated, and how the FDR was controlled. They should report the number of significant couplings at different FDR thresholds and demonstrate that the major specificity encoding residues are stable across different statistical cutoffs.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Validation of allosteric mechanisms
- **Claim pointer** The authors state that 11 of the 20 major energetic couplings have an allosteric mechanism of action, meaning the coupled residues do not directly contact each other.
- **Evidence pointer** Results section "Direct and allosteric reprogramming of specificity"; Figure 4b-j; Figure S5g-h
- **Concern** The classification of couplings as allosteric is based on the absence of direct contact in the crystal structure. However, the crystal structure represents a single static conformation, and PDZ domains are known to undergo conformational dynamics. Residues that are not in contact in the crystal structure could still interact transiently or through water-mediated contacts. The authors do not provide experimental validation (e.g., NMR, MD simulations beyond what is referenced, or engineered disulfide crosslinks) to confirm that the proposed allosteric couplings are indeed mediated through conformational changes rather than through dynamic contacts not captured in the crystal structure.
- **Why it matters** The distinction between direct and allosteric mechanisms is a central conceptual contribution of the paper. If the classification is incorrect, the interpretation of how specificity is encoded and how mutations propagate their effects would be substantially different.
- **Resolution test** The authors should provide additional evidence supporting the allosteric classification, such as molecular dynamics simulations showing conformational coupling between the identified residue pairs, or experimental validation using a subset of the predicted allosteric mutations to demonstrate that they affect binding through conformational changes rather than direct contacts.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of the modular encoding model
- **Claim pointer** The authors propose that specificity encoding is highly modular, with distinct domain residues determining specificity for each ligand position, and suggest this framework can be applied to other protein interaction domains.
- **Evidence pointer** Results section "Major specificity encoding residues and the modular encoding of binding specificity"; Discussion
- **Concern** The modularity claim is based on a single PDZ domain (PDZ3) binding a single peptide (CRIPT). While the authors reference previous work on other PDZ domains, the comprehensive map is limited to one domain-peptide pair. The extent to which the modular organization observed here is a general property of PDZ domains or other peptide recognition domains is unclear. The authors do not test whether the identified specificity determinants are conserved across PDZ domains or whether the modular organization holds for different peptide ligands.
- **Why it matters** The broader significance of the work depends on whether the modular encoding framework is generalizable. If the organization is specific to PDZ3-CRIPT, the implications for understanding and engineering protein interactions would be more limited.
- **Resolution test** The authors should discuss how their findings relate to known specificity determinants in other PDZ domains and ideally provide preliminary data or analysis showing that the modular organization is conserved across the PDZ family.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Functional relevance of identified specificity changes
- **Claim pointer** The authors identify mutations that change binding specificity and classify them as "class-switching" or "class-bridging" based on changes in preference for different amino acids at specific ligand positions.
- **Evidence pointer** Results section "A comprehensive map of specificity-changing mutations"; Figure 5
- **Concern** The functional relevance of the identified specificity changes is not experimentally validated in a biological context. The authors do not test whether the specificity changes observed in the binding assay translate to changes in cellular function, such as altered signaling outcomes or changes in protein-protein interaction networks. The physiological relevance of the specific amino acid preferences identified is not addressed.
- **Why it matters** The ultimate significance of mapping specificity determinants is to understand how protein interactions are regulated and evolve in biological systems. Without functional validation, the relevance of the identified specificity changes to real biological processes remains uncertain.
- **Resolution test** The authors should validate a subset of the identified specificity-changing mutations in a cellular context, for example by testing their effects on PDZ3-mediated signaling or on the interaction with known endogenous ligands.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Library construction and selection details
- **Evidence pointer** Materials and Methods "Library construction"; "Large-scale transformations of libraries into yeast and competition assays"
- **Issue** The methods section is brief and lacks sufficient detail for replication. Key parameters such as the number of yeast cells transformed, the duration of selection, the concentration of MTX used, and the number of generations of growth are not specified.
- **Required correction** Provide complete details of the experimental procedures, including all relevant parameters, to enable replication by other laboratories.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 5b
- **Evidence pointer** Results section "A comprehensive map of specificity-changing mutations"; Figure 5b
- **Issue** The claim that the diversity of specificity changes is "loosely related to the dynamicity of the ligand position" is based on a qualitative comparison. The authors do not provide a quantitative analysis or statistical test to support this relationship.
- **Required correction** Provide a quantitative analysis of the relationship between dynamicity (e.g., B-factors or order parameters) and the diversity of specificity changes, with appropriate statistical tests.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of dynamic region contributions
- **Affected element** Results section "Specificity encoding through a disordered tail"
- **Evidence pointer** Results section "Specificity encoding through a disordered tail"; Figure 6
- **Concern** The authors conclude that the dynamic N-terminal region contributes little to specificity through interactions with the domain, but they do find couplings between the dynamic region and structured residues within the peptide. The interpretation of these intra-peptide couplings is somewhat unclear, and the authors do not fully discuss the implications of these findings for understanding fuzzy interactions.
- **Required correction** Expand the discussion of the intra-peptide couplings and their potential mechanistic significance, and clarify how these findings relate to the broader understanding of fuzzy interactions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Comparison with previous work
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The authors reference previous studies on PDZ domain specificity but do not provide a systematic comparison of their findings with those from earlier deep mutational scanning or specificity profiling studies. A more detailed comparison would help contextualize the novelty of their results.
- **Required correction** Add a more comprehensive comparison with previous PDZ domain specificity studies, highlighting both consistencies and novel findings.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Accessibility of data
- **Affected element** Data availability statement
- **Evidence pointer** Data availability section
- **Issue** The data are deposited in GEO and Zenodo, but the manuscript does not provide a direct link to the processed data files or a clear description of the data format. This may hinder accessibility for researchers who wish to use the dataset.
- **Required correction** Provide a more detailed description of the deposited data files and their format, and ensure that the links are functional and accessible.

- **Technical failings that need to be addressed before the case is established**
  1. R1-M1: Incomplete reporting of mutagenesis coverage and sequencing depth undermines the "complete map" claim.
  2. R1-M2: Insufficient detail on the statistical methods for identifying energetic couplings prevents assessment of false positive rates.
  3. R1-M3: The classification of allosteric mechanisms lacks experimental validation.
  4. R1-M5: Lack of functional validation of specificity changes in a biological context.

- **Assessment against Nature-style criteria**
  - **Originality**: The work is highly original in its scale and scope. The comprehensive mapping of specificity determinants for a full PDZ domain-peptide interaction, including both structured and dynamic regions, has not been previously achieved. The identification of allosteric mechanisms for specificity encoding is conceptually novel.
  - **Scientific importance**: The findings have significant implications for understanding how protein interaction specificity is encoded, how it evolves, and how it can be engineered. The distinction between affinity and specificity contributions from dynamic regions addresses a fundamental question in molecular recognition. The dataset will be a valuable resource for the community.
  - **Interdisciplinary readership**: The work will appeal to researchers in molecular biophysics, protein engineering, systems biology, and evolutionary biology. The methodological approach combining deep mutational scanning with thermodynamic modeling is broadly applicable. However, the presentation is quite specialized and may be challenging for non-specialists.
  - **Technical soundness**: The experimental design is generally sound, with appropriate controls and replication. The use of a well-validated binding assay and thermodynamic modeling is appropriate. However, the statistical methods for identifying energetic couplings need more detail, and the completeness of the mutagenesis coverage needs to be demonstrated. The lack of experimental validation for the allosteric mechanism classification is a weakness.
  - **Readability for nonspecialists**: The manuscript is clearly written but assumes significant background knowledge in protein biophysics and deep mutational scanning. The figures are likely to be complex and may require careful explanation. The abstract is accessible, but the results section is dense.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript presents a valuable and potentially landmark dataset with important conceptual insights. However, the central claims of completeness and the identification of specific energetic couplings need to be supported by more detailed reporting of the experimental coverage and statistical methods. The classification of allosteric mechanisms would benefit from additional validation. If these concerns are addressed, the work would be suitable for publication in a high-impact journal.

## Risk / unsupported claims
- The claim of a "complete map" of specificity encoding is not fully supported by the provided evidence, as the completeness of mutagenesis coverage is not demonstrated.
- The classification of 11 of 20 major energetic couplings as allosteric is not experimentally validated and relies solely on the absence of direct contact in a static crystal structure.
- The statement that the dynamic N-terminal region "contributes little to specificity through the domain" is based on the absence of significant couplings, which could be a false negative if the statistical power is insufficient.
- The generalizability of the modular encoding framework to other PDZ domains or peptide interactions is not tested and is presented as a broader implication without direct evidence.
- The functional relevance of the identified specificity changes in a biological context is not demonstrated.