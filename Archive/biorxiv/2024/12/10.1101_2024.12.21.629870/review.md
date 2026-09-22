## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no methods, figures, or supplementary material were provided
- **Shared manuscript claim summary** The authors report development of Condensate Partitioning by mRNA-Display (CPmD), a high-throughput method enabling analysis of partitioning of hundreds of thousands of peptides derived from the disordered proteome into reconstituted condensates. They claim that amino acid content, rather than specific sequence, primarily determines partitioning behavior, and that quantification of partitioning energies allows deciphering of the "molecular grammar" of interactions, enabling accurate prediction of condensate formation of diverse full-length disordered protein regions. They further claim that the results reveal how physicochemical properties of disordered regions encode biological functions through condensate formation.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary information were provided
- **Missing materials affecting confidence** Full manuscript, methods description, all figures and tables, statistical analyses, validation experiments, and any comparison with existing methods or benchmarks

## Reviewer
- **Overall assessment** The abstract presents a potentially impactful methodological advance with a striking claim of throughput improvement by several orders of magnitude. The central claims regarding the dominance of amino acid content over sequence specificity and the predictive power for full-length disordered regions are scientifically interesting but cannot be evaluated from the abstract alone. The absence of methodological detail, quantitative results, and validation data prevents assessment of technical soundness. The work, if substantiated, would be of broad interest to the phase separation and disordered protein communities.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, intrinsically disordered proteins, and the sequence determinants of protein partitioning. The method could also interest those developing high-throughput screening approaches for protein interactions and those working on predictive models of protein behavior in cellular contexts.
- **Major strengths** The claimed throughput increase by several orders of magnitude represents a substantial technical advance if verified. The focus on proteome-scale coverage addresses a recognized gap in the field. The stated goal of deriving a quantitative "molecular grammar" from partitioning energies is conceptually appealing and could provide a unifying framework.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: The concept of applying mRNA-display to condensate partitioning appears novel, but the abstract does not provide sufficient context to establish how it differs from existing approaches. Scientific importance: The questions addressed are of high importance to the phase separation field, and a quantitative proteome-scale method would be valuable. Interdisciplinary readership: The work bridges biochemistry, biophysics, and computational biology, and could attract readers across these disciplines. Technical soundness: Cannot be assessed from the abstract alone; no methodological details, controls, or validation data are presented. Readability for nonspecialists: The abstract is clearly written and accessible, with technical terms defined in context.
- **Recommendation posture** Currently not established from the provided evidence. The abstract describes a promising approach, but the absence of methodological detail and quantitative results means the core claims cannot be verified. A full manuscript with methods, controls, and validation would be required for a supportive assessment.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The method allows analysis of partitioning of hundred thousand peptides derived from the disordered proteome into reconstituted condensates, advancing experimental throughput by several orders of magnitude.
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract claims a throughput increase of several orders of magnitude but provides no description of the method, its workflow, or how throughput is quantified. No comparison with existing methods is given, and no validation data are presented to support the throughput claim.
- **Why it matters** The central value proposition of the work rests on this throughput claim. Without methodological detail and comparative benchmarks, the claim cannot be assessed, and the novelty relative to existing approaches cannot be established.
- **Resolution test** Provide a detailed methods section describing the CPmD workflow, including library construction, partitioning assay, sequencing, and data analysis. Include quantitative comparison of throughput with existing methods, and demonstrate reproducibility across replicates.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The amino acid content, rather than specific sequence, primarily determines partitioning behavior.
- **Evidence pointer** Abstract; location not provided
- **Concern** This is a strong mechanistic claim, but the abstract provides no quantitative data, statistical analysis, or examples supporting it. No information is given on how partitioning energies were derived, how sequence effects were separated from composition effects, or what fraction of variance in partitioning is explained by amino acid content.
- **Why it matters** This claim challenges sequence-centric views of condensate formation and would have significant implications for the field. Without rigorous statistical evidence and appropriate controls, the claim is unsupported and could mislead subsequent research.
- **Resolution test** Present quantitative analyses showing the correlation between amino acid composition and partitioning energies, with appropriate statistical tests. Include control experiments where sequence order is randomized while composition is preserved, and show that partitioning is unchanged. Report effect sizes and confidence intervals.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Predictive validity
- **Claim pointer** Quantification of the partitioning energies of peptides allows accurate prediction of the formation of condensates of diverse full-length disordered protein regions.
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract claims accurate prediction of full-length protein behavior from peptide-level measurements, but no predictive accuracy metrics, validation datasets, or examples are provided. The relationship between peptide partitioning and full-length protein condensation is not described, and potential confounding factors such as multivalency, cooperativity, or context-dependent effects are not addressed.
- **Why it matters** The translational value of the method depends on its ability to predict full-length protein behavior. Without demonstrated predictive accuracy on held-out proteins or independent validation, this claim is not established.
- **Resolution test** Provide a validation set of full-length disordered proteins with experimentally measured condensation behavior. Show quantitative agreement between predictions and measurements, with appropriate error metrics. Discuss limitations and cases where prediction fails.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Method description
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states the method is called "Condensate Partitioning by mRNA-Display" but does not explain how mRNA-display is adapted for condensate partitioning assays. The acronym CPmD is introduced without context.
- **Required correction** Provide a brief description of the method principle in the abstract, including how the mRNA-display library is generated, how partitioning is measured, and how sequencing data are converted to partitioning energies.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Scope definition
- **Affected element** Claim about "disordered proteome"
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract claims analysis of peptides "derived from the disordered proteome" but does not specify the source organisms, the criteria for defining disordered regions, or the coverage of the proteome. The term "hundred thousand" is imprecise.
- **Required correction** Specify the number of peptides analyzed, the source proteome(s), the definition of disorder used, and the fraction of the disordered proteome covered.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Biological interpretation
- **Affected element** Claim about encoding biological functions
- **Evidence pointer** Abstract; location not provided
- **Issue** The final claim that "physicochemical properties of disordered regions encode biological functions through formation of biomolecular condensates" is broad and goes beyond the data described. The abstract does not present any functional assays or links to specific biological processes.
- **Required correction** Either temper this claim to reflect the scope of the data presented, or provide specific examples linking predicted condensation behavior to known biological functions with experimental validation.

## Risk / unsupported claims
- The claim of throughput advancement by "several orders of magnitude" is unsupported without comparative data.
- The claim that amino acid content "primarily determines" partitioning behavior is unsupported without statistical evidence and controls.
- The claim of "accurate prediction" of full-length protein condensation is unsupported without validation metrics.
- The claim that results "reveal how physicochemical properties of disordered regions encode biological functions" is unsupported and goes beyond the described data.
- The generalizability of the findings to diverse disordered proteins and condensate types is not established from the abstract.