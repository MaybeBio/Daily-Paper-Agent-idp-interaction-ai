## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, figure legends not provided)
- **Assessment boundary** Scientific claims, methodology, data interpretation, and reproducibility as presented in the provided text
- **Shared manuscript claim summary** The authors propose that selectivity and promiscuity in the human chemokine-GPCR interaction network are encoded by hierarchically organized sequence and structural determinants, including conserved, semi-conserved, and variable elements, and demonstrate this by engineering a viral chemokine with altered receptor selectivity
- **Visible evidence base** Sequence alignments (1058 chemokine, 951 receptor sequences), 16 chemokine-GPCR complex structures/models, contact analysis, logistic regression classification, saturation mutagenesis data, β-arrestin recruitment assays, calcium flux assays, binding assays, ITC, chemotaxis assays
- **Missing materials affecting confidence** Figure panels and supplementary figures/tables referenced but not provided; detailed statistical outputs; raw data for functional assays; complete methods for some assays (e.g., flow cytometry gating strategy); validation of the web resource

## Reviewer
- **Overall assessment** This manuscript presents a comprehensive and ambitious framework for understanding the molecular basis of selectivity and promiscuity in the human chemokine-GPCR network. The integration of sequence conservation, structural analysis, and functional validation is commendable. The central hypothesis, that selectivity is encoded by a hierarchy of conserved and variable determinants distributed across structured and unstructured regions, is well-supported by the presented analyses. The engineering of vMIP-II with altered receptor selectivity provides a compelling proof-of-principle. However, several technical concerns regarding the robustness of the classification approach, the generalizability of the findings, and the strength of the functional validation need to be addressed before the case is fully established.
- **Who would be interested in the results, and why** Researchers in GPCR biology, chemokine signaling, immunology, and protein engineering would find this work of high interest. The framework for understanding selectivity determinants could inform drug discovery efforts targeting chemokine receptors, which are implicated in numerous inflammatory and autoimmune diseases, cancer metastasis, and HIV infection. The web resource would be a valuable community tool.
- **Major strengths**
  1. The study addresses a fundamental and long-standing question in chemokine biology with a comprehensive, multi-faceted approach.
  2. The development of a common numbering system (CCN, CRN) for chemokines and receptors is a significant methodological contribution that will facilitate future studies.
  3. The integration of diverse data types (sequences, structures, mutations, phenotypes) into a coherent framework is elegant and powerful.
  4. The functional validation through vMIP-II engineering provides strong evidence for the practical utility of the identified principles.
  5. The identification of SLiMs in unstructured regions as key selectivity determinants is a novel and insightful finding.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness of classification approach
  - **Claim pointer** The logistic regression model identifies subfamily-predictive positions with ≥75% accuracy, and these positions are used to define subfamily-specific recognition mechanisms.
  - **Evidence pointer** Results section "Semi-preserved molecular 'sensors' guide subfamily-specific recognition"; STAR Methods "Subfamily-specific classification of chemokine and GPCR residue positions"
  - **Concern** The logistic regression classification approach relies on the assumption that CC versus CXC subfamily identity is the primary determinant of interaction specificity. However, the manuscript also demonstrates that within-subfamily selectivity is common (e.g., CCL3 vs. CCL5 both bind CCR5 but with different potencies). The model may be oversimplifying the problem by forcing a binary classification. Furthermore, the down-sampling of CC sequences to create equal class sizes could introduce bias, and the choice of 75% accuracy threshold appears arbitrary. The authors should provide a more rigorous evaluation of the model's performance, including cross-validation, and discuss the limitations of this binary classification approach.
  - **Why it matters** The subfamily-predictive positions identified by this model are central to the paper's conclusions about subfamily-specific recognition. If the model is not robust, the subsequent analyses and conclusions may be compromised.
  - **Resolution test** Provide cross-validated accuracy metrics, precision-recall curves, and a comparison with alternative classification methods. Discuss how the model handles within-subfamily selectivity and whether the 75% threshold is justified by the data distribution.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Generalizability of findings
  - **Claim pointer** The principles of hierarchical selectivity encoding are generalizable across the chemokine-GPCR network, as implied by the discussion and the proposed framework.
  - **Evidence pointer** Results sections "Customization of selectivity preferences among chemokine-GPCR complexes" and "Identification of SLiMs"; Discussion
  - **Concern** The structural analysis is based on only 16 chemokine-GPCR complexes, which represent a small fraction of the potential interaction space (46 ligands × 23 receptors). Many of these complexes involve a limited set of receptors (e.g., CCR5, CXCR4, CXCR2). The authors should address whether the identified determinants are representative of the broader network or biased toward well-studied receptors. Additionally, the functional validation is limited to vMIP-II, a viral chemokine, and its effects on CCR3, CCR5, and CXCR4. The generalizability of the engineering approach to other chemokines and receptors remains untested.
  - **Why it matters** The paper claims to uncover general principles governing the entire chemokine-GPCR network. If the analysis is biased toward a subset of well-characterized interactions, the conclusions may not be broadly applicable.
  - **Resolution test** Include a discussion of potential biases in the structural dataset. Provide additional validation, even if limited, for a different chemokine-receptor pair to demonstrate the generalizability of the engineering approach.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Strength of functional validation
  - **Claim pointer** The vMIP-II mutants with altered receptor selectivity demonstrate that the identified principles can be leveraged to design selective chemokine-GPCR interactions.
  - **Evidence pointer** Results section "Rewiring selectivity preferences of a promiscuous, viral chemokine"; Figures 6D, 6E, S7I–S7L
  - **Concern** The functional validation shows that mutations alter potency at CCR3, CCR5, and CXCR4, but the data are presented as changes in potency (EC50/IC50) rather than selectivity per se. The claim of "altered receptor selectivity" would be strengthened by demonstrating that the mutants show a clear preference for one receptor over another, rather than just a change in potency at individual receptors. Additionally, the vMIP-II triple mutant is described as a "mild partial agonist" at CCR5, which complicates the interpretation of the antagonism data. The authors should clarify the functional consequences of the mutations in terms of selectivity, not just potency.
  - **Why it matters** The proof-of-principle is a key part of the paper's impact. If the functional data do not clearly demonstrate altered selectivity, the practical utility of the framework is less compelling.
  - **Resolution test** Present data as selectivity ratios (e.g., IC50 at CCR5 vs. CCR3) and discuss the implications of partial agonism for the interpretation of the results.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity of presentation
  - **Affected element** Figure 2H
  - **Evidence pointer** Results section "Constrained plasticity in chemokine-receptor-binding mode is mediated by a minimal network of conserved residues"
  - **Issue** The comparison of mutation effects at conserved versus non-conserved positions using saturation mutagenesis data is interesting, but the statistical test used (Kruskal-Wallis with Dunn post-hoc) is not described in the figure legend or text. The authors should specify the statistical details.
  - **Required correction** Add statistical details to the figure legend or text, including the number of comparisons and the correction method used.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Web resource
  - **Evidence pointer** Data and code availability section
  - **Issue** The web resource is mentioned but not described in detail. The authors should provide a brief description of its contents and functionality.
  - **Required correction** Add a brief description of the web resource in the main text or methods.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Interpretation of results
  - **Affected element** Discussion of ACKR1 variant
  - **Evidence pointer** Results section "Altered selectivity of a common variant in the ACKR1 unstructured N terminus"
  - **Issue** The discussion of the ACKR1 Gly42Asp variant focuses on P. vivax susceptibility, but the broader implications for chemokine selectivity are not fully explored. The authors should discuss whether this variant affects binding to all chemokines or only a subset.
  - **Required correction** Add a brief discussion of the potential impact of the ACKR1 variant on chemokine selectivity beyond P. vivax susceptibility.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Technical detail
  - **Affected element** ITC experiments
  - **Evidence pointer** STAR Methods "Isothermal titration calorimetry assays"
  - **Issue** The ITC experiments use ACKR1 N-terminal peptides (residues 1-60) with alanine substitutions of cysteines. The authors should clarify whether these substitutions affect the structure or binding properties of the peptide.
  - **Required correction** Add a brief statement addressing the potential impact of cysteine-to-alanine substitutions on the peptide's structure and function.
- **Technical failings that need to be addressed before the case is established** R1-M1 (classification robustness) and R1-M2 (generalizability) are the most critical. R1-M3 is important but not necessarily blocking if the data are presented more clearly.
- **Assessment against Nature-style criteria**
  - **Originality** High. The hierarchical framework for understanding selectivity determinants in the chemokine-GPCR network is novel and provides a new conceptual model for the field.
  - **Scientific importance** High. The chemokine-GPCR system is central to immune function and disease, and understanding the molecular basis of selectivity has broad implications for therapeutic development.
  - **Interdisciplinary readership** Moderate to high. The work will appeal to structural biologists, immunologists, pharmacologists, and computational biologists. The engineering aspect may also interest synthetic biologists.
  - **Technical soundness** Moderate. The computational and structural analyses are generally sound, but the classification approach needs more rigorous validation. The functional data are supportive but not fully conclusive.
  - **Readability for nonspecialists** Moderate. The manuscript is well-written but dense, with many technical details. The use of analogies (e.g., Lego bricks) helps, but the nonspecialist may struggle with some sections.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript presents a valuable framework with significant potential impact. However, the concerns about the classification approach and generalizability need to be addressed to fully establish the case.

## Risk / unsupported claims
- The claim that "selectivity and promiscuity emerge from an ensemble of generalized and specific determinants" is well-supported by the analysis, but the relative contribution of each type of determinant to overall network specificity is not quantified.
- The claim that SLiMs in unstructured regions are key determinants of network-specific selectivity is supported by the vMIP-II data, but the analysis is limited to a small number of complexes and may not be representative of all chemokine-receptor pairs.
- The claim that the identified principles can guide the design of selective chemokine-GPCR interactions is supported by the vMIP-II engineering, but the generalizability of this approach to other chemokines and receptors is not demonstrated.
- The functional significance of the ACKR1 Gly42Asp variant for chemokine selectivity is suggested but not directly tested for all chemokines.
- The web resource is mentioned but not described, making it impossible to assess its utility.