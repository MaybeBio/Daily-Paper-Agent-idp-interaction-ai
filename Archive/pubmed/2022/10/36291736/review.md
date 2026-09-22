## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, methods, results, discussion, and figure/table references.
- **Assessment boundary** Scientific validity, methodological rigor, and support for claims within the provided manuscript. No external literature or unpublished data are considered.
- **Shared manuscript claim summary** The authors argue that AlphaFold2, an AI-based protein structure prediction program, has an intrinsic weakness in predicting the structure of membrane proteins and intrinsically disordered proteins (IDPs) due to the "epigenetic dimension of protein structure" (EDPS), which posits that environmental factors such as lipid interactions control protein conformation beyond the amino acid sequence. They compare AlphaFold2 and Robetta predictions for a set of membrane proteins and soluble proteins, concluding that Robetta is generally more accurate for membrane-compatible topology and that AlphaFold2 fails to account for EDPS.
- **Visible evidence base** Methods sections 2.1-2.5, Results sections 3.1-3.6, Figures 1-8, Tables 1, Supplementary Figures S1-S9, and references to PDB structures and UniProt codes.
- **Missing materials affecting confidence** No raw prediction files, no detailed parameters for Robetta or AlphaFold2 runs, no statistical analysis of TM-score/RMSD differences, no access to supplementary figures (S1-S9) or table data beyond textual description, and no explicit criteria for "membrane-compatible topology" assessment.

## Reviewer
- **Overall assessment** The manuscript addresses a relevant and timely topic, namely the limitations of AlphaFold2 for membrane protein structure prediction, and introduces the EDPS concept as a potential explanation. However, the evidence presented is largely qualitative, based on visual inspection of structural models, and lacks rigorous quantitative validation. The comparison between AlphaFold2 and Robetta is not systematically controlled, and the claims about EDPS as an "intrinsic weakness" are not fully supported by the data provided. The study has potential interest for structural biologists and computational biologists, but the current evidence base is insufficient to establish the central conclusions.
- **Who would be interested in the results, and why** Structural biologists, computational biologists, and researchers in drug design, particularly those working on membrane proteins, IDPs, and protein-lipid interactions. The study highlights practical limitations of AlphaFold2, which is widely used, and could inform choices between prediction tools. The EDPS concept may also interest researchers studying protein folding and conformational dynamics in cellular environments.
- **Major strengths** The manuscript addresses a significant gap in the evaluation of AlphaFold2, focusing on membrane proteins and IDPs, which are underrepresented in benchmark studies. The inclusion of multiple protein examples (EGFR, h-SV2C, h-SYT1, APP, BoNT/A, BoNT/B, CFH) provides a broad scope. The use of experimental structures (e.g., PDB: 4JRA, 2NP0) as references for comparison is a positive aspect. The discussion of lipid chaperone effects, particularly gangliosides, adds a novel perspective that could stimulate further research.
- **Major Concerns** The concerns are detailed below with IDs R1-M1 to R1-M5.
- **Minor Comments** The minor comments are detailed below with IDs R1-m1 to R1-m4.
- **Technical failings that need to be addressed before the case is established** R1-M1 (lack of quantitative rigor), R1-M2 (subjective topology assessment), R1-M3 (uncontrolled comparison), R1-M4 (overgeneralization of EDPS), R1-M5 (insufficient docking validation).
- **Assessment against Nature-style criteria** Originality: The EDPS concept is a novel framing, but it builds on existing knowledge of protein-lipid interactions and IDPs, so originality is moderate. Scientific importance: The topic is important, as AlphaFold2 is widely used, and understanding its limitations is valuable; however, the evidence does not yet establish a broad impact. Interdisciplinary readership: The manuscript could appeal to structural biology, computational biology, and membrane biochemistry, but the qualitative nature may limit appeal to a wider audience. Technical soundness: The methods are not rigorously applied; the lack of quantitative metrics and statistical analysis undermines technical soundness. Readability for nonspecialists: The manuscript is generally readable, but the EDPS concept is introduced without clear operational definitions, which may confuse nonspecialists.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript has potential, but the central claims require substantial additional quantitative analysis and clearer methodological controls.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "Robetta was generally more accurate than AlphaFold for ascribing a membrane-compatible topology" (Abstract) and that "Robetta models match the spatial organization of experimental structure domains better than AlphaFold2 models, as demonstrated by a lower RMSD and a higher TM-score" (Section 3.5).
- **Evidence pointer** Section 3.5, Table 1, Figures S5-S9
- **Concern** The quantitative comparison of AlphaFold2 and Robetta models relies on TM-score and RMSD values, but the manuscript does not provide the actual numerical data in the main text or a statistical analysis of these metrics. The claim of "generally more accurate" is based on a small set of proteins (n=7), and no error bars, confidence intervals, or significance tests are reported. Additionally, the selection of reference structures for comparison is not justified for all proteins (e.g., for APP, no experimental structure is cited).
- **Why it matters** Without quantitative rigor, the conclusion that Robetta outperforms AlphaFold2 cannot be reliably assessed. The lack of statistical analysis means the observed differences could be due to chance or specific to the chosen proteins, undermining the generalizability of the claim.
- **Resolution test** Provide the full TM-score and RMSD values for all proteins and domains in a supplementary table, include statistical tests (e.g., paired t-test or Wilcoxon signed-rank test) to compare AlphaFold2 and Robetta, and justify the choice of reference structures for each protein.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that AlphaFold2 predictions for EGFR, h-SYT1, and APP "looked more like globular proteins than membrane proteins" (Sections 3.1, 3.3) and that Robetta predicted "a spatial organization that was compatible with a membrane protein insertion" (Section 3.3).
- **Evidence pointer** Figures 1, 4, Section 3.1, Section 3.3
- **Concern** The assessment of "membrane-compatible topology" appears to be based on visual inspection of structural models, as no quantitative criteria (e.g., hydrophobicity profiles, orientation of transmembrane domains, or comparison with known membrane protein structures) are described. The claim that AlphaFold2 fails to predict membrane topology is not supported by a systematic evaluation, and the authors do not report any metrics to distinguish between globular and membrane-like conformations.
- **Why it matters** Visual inspection is subjective and not reproducible. Without objective criteria, the conclusion that AlphaFold2 is intrinsically weak for membrane proteins is not scientifically robust, as other studies have shown AlphaFold2 can predict membrane protein structures with reasonable accuracy.
- **Resolution test** Define explicit criteria for membrane-compatible topology (e.g., presence of transmembrane helices with correct hydrophobic length, orientation relative to the membrane plane) and apply them systematically to all models. Provide quantitative scores or use established tools (e.g., PPM server, OPM database) to assess membrane insertion.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors compare AlphaFold2 and Robetta predictions but do not control for the input parameters or versions of the algorithms. They state that "the models of the membrane proteins predicted by AlphaFold2... were retrieved from uniprot" (Section 2.1) and that "ab-initio models were generated using the web-based service Robetta" (Section 2.1).
- **Evidence pointer** Section 2.1, Section 2.2
- **Concern** The AlphaFold2 models are retrieved from UniProt, which may use a specific version of AlphaFold2 with default settings, while Robetta models are generated via a web service with potentially different parameters. The authors do not specify the exact versions, multiple sequence alignments, or any template usage, which could affect the comparison. Additionally, for the docking studies (Section 2.2), the initial conditions for AlphaFold2 and Robetta models are not described in sufficient detail to ensure a fair comparison.
- **Why it matters** Uncontrolled differences in algorithm settings or input data could bias the results. A fair comparison requires identical conditions or at least a discussion of how differences might affect the outcomes.
- **Resolution test** Specify the exact versions of AlphaFold2 and Robetta used, describe the input sequences and any alignment parameters, and ensure that both models are generated under comparable conditions. For docking, provide details on the initial docking poses and energy minimization protocols to confirm that differences are not due to methodological artifacts.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The authors propose the EDPS paradigm, stating that "the environment brings its own set of parameters that must be integrated into the algorithms" (Section 4) and that "the epigenetic dimension of a protein structure is an intrinsic weakness of AI-based protein structure prediction" (Abstract).
- **Evidence pointer** Abstract, Section 4
- **Concern** The EDPS concept is introduced as a broad paradigm, but the manuscript does not provide a clear operational definition or testable predictions. The examples given (e.g., synaptotagmin, gangliosides) are specific, but the claim that EDPS is an "intrinsic weakness" of AlphaFold2 is overgeneralized, as the study only examines a limited set of proteins and does not demonstrate that environmental factors are systematically ignored by AlphaFold2.
- **Why it matters** Overgeneralization could mislead readers into thinking AlphaFold2 is fundamentally flawed for all membrane proteins or IDPs, which is not supported by the evidence. The scientific importance of the claim depends on its generalizability, which is not established.
- **Resolution test** Provide a clear definition of EDPS with specific criteria for when it applies. Test the hypothesis on a larger, diverse set of membrane proteins and IDPs, and compare AlphaFold2 predictions with experimental structures in the presence and absence of lipid environments to demonstrate the impact of environmental factors.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "in most of the cases studied, the structures predicted by AlphaFold cannot be used as starting conditions for molecular docking analyses" (Section 1) and that Robetta structures are "directly usable for molecular docking" (Section 1).
- **Evidence pointer** Section 1, Section 2.2, Section 3.2, Figures 2-3
- **Concern** The docking analysis is only performed for the h-SV2C luminal domain with BoNT/A1, and the energy of interaction values are presented for a few residues (Figure 2D). No docking scores, binding affinities, or comparisons with experimental binding data are provided. The claim that AlphaFold2 models are not usable for docking is based on a single example and lacks validation.
- **Why it matters** Docking reliability is a practical claim with implications for drug design. Without robust docking metrics and validation against known experimental structures, the conclusion is not supported.
- **Resolution test** Perform docking with multiple protein-ligand complexes, report standard docking scores (e.g., binding free energy, enrichment factors), and validate predictions against experimental binding affinities or known complex structures. Include a statistical comparison of docking performance between AlphaFold2 and Robetta models.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.1
- **Evidence pointer** Section 2.1
- **Issue** The method for retrieving AlphaFold2 models from UniProt is not described in detail, such as whether the models were used as-is or post-processed.
- **Required correction** Specify the UniProt retrieval date, the exact AlphaFold2 version, and any post-processing steps (e.g., trimming, relaxation) applied to the models.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section 2.2
- **Evidence pointer** Section 2.2
- **Issue** The energy minimization protocol for the docking complexes is described briefly, but the software settings (e.g., number of steps, convergence criteria) are not provided.
- **Required correction** Provide full details of the energy minimization parameters, including the CHARMM force field version, step size, and termination conditions, to enable reproducibility.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Section 3.5, Table 1
- **Evidence pointer** Section 3.5, Table 1
- **Issue** The TM-score and RMSD values are mentioned but not shown in the main text, and the table is not included in the provided material.
- **Required correction** Include the full Table 1 with all values, and add a brief description of how the reference structures were selected for each protein.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Section 3.6, Figure 8
- **Evidence pointer** Section 3.6, Figure 8
- **Issue** The discussion of lipid chaperone activity is qualitative, and the figure is not provided, making it difficult to assess the evidence for the conformational changes described.
- **Required correction** Provide the figure and, if possible, quantitative data (e.g., circular dichroism spectra, NMR or MD simulation results) to support the claim that gangliosides induce specific conformational changes.

## Risk / unsupported claims
- The claim that "Robetta was generally more accurate than AlphaFold for ascribing a membrane-compatible topology" is unsupported due to lack of quantitative metrics and statistical analysis.
- The claim that AlphaFold2 predictions are "not usable as starting conditions for molecular docking" is unsupported, as only one docking example is provided without validation.
- The EDPS paradigm is presented as a general explanation for AlphaFold2's limitations, but the evidence is limited to a few examples and lacks a clear operational definition.
- The statement that "the environment brings its own set of parameters that must be integrated into the algorithms" is speculative and not directly tested in this study.
- The claim that AlphaFold2 has "difficulties in predicting elongated structures" is based on a single example (CFH) and is not systematically evaluated.