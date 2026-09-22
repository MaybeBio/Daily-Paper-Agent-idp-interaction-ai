## Review setup
- **Input scope** Full manuscript text, including summary, introduction, results, discussion, methods, and figure legends (as provided).
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided text. No external data or unpublished information was consulted.
- **Shared manuscript claim summary** The authors propose that a disordered linker in the Polycomb protein Polyhomeotic (Ph) modulates phase separation and oligomerization through specific linker-SAM interactions. They use in vitro reconstitution, molecular dynamics simulations, and cell-based assays to show that replacing the Drosophila linker with the human PHC3 linker enhances phase separation, reduces condensate size, and that these effects are largely independent of SAM polymerization. They further demonstrate that these linker-dependent effects are conserved in human cells and influence growth in Drosophila imaginal discs.
- **Visible evidence base** In vitro phase separation assays (Figure 1), MD simulations (Figures 2, 3, 5), SEC-MALS and mass photometry (Figure S1), FRAP (Figure 4), cell-based imaging in Drosophila and human cells (Figure 6), CRISPaint-edited endogenous cell lines (Figure 7), and Drosophila imaginal disc growth assays (Figure 7).
- **Missing materials affecting confidence** Raw data files, full uncropped blots/gels, complete statistical output tables, and detailed simulation parameters are not provided in the text. The manuscript refers to supplementary figures and tables that were not included in the provided material.

## Reviewer
- **Overall assessment** This is a well-executed and thoughtful study that addresses an important question in the field of biomolecular condensates: how disordered linkers tune the behavior of oligomerization domains. The combination of MD simulations with experimental validation is a strength, and the use of multiple orthogonal assays (in vitro, cell-based, endogenous editing, and tissue-level growth) provides a compelling narrative. The main claims are largely supported by the data presented, though some concerns about the interpretation of FRAP data, the generalizability of the findings, and the mechanistic link between condensate properties and function remain. The work is of high quality and will be of interest to researchers studying Polycomb biology, phase separation, and protein engineering.
- **Who would be interested in the results, and why** Researchers in the fields of epigenetics and Polycomb group biology, particularly those studying the role of PRC1 in chromatin organization and gene repression. Also, the broader community of scientists interested in the molecular determinants of phase separation, the role of disordered linkers in modulating protein-protein interactions, and the design principles of synthetic condensates. The cross-species comparison and the identification of a specific linker-SAM interaction interface will be of interest to evolutionary biologists and protein engineers.
- **Major strengths**
  1. The study is well-integrated, combining computational predictions with experimental validation in a logical and rigorous manner.
  2. The use of multiple model systems (in vitro, Drosophila cells, human cells, and imaginal discs) strengthens the biological relevance of the findings.
  3. The identification of specific charged residues in the linker and SAM that mediate interactions provides a mechanistic basis for the observed differences between Drosophila and human proteins.
  4. The finding that linker effects on phase separation are largely independent of SAM polymerization is a novel and important contribution, as it separates two functions of the SAM domain.
  5. The use of CRISPaint to edit endogenous loci is a powerful approach that adds physiological relevance.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** No
  - **Axis** Interpretation of FRAP data
  - **Claim pointer** The authors state that "Oligomerization influences condensate dynamics but minimally impacts condensate formation" based on FRAP experiments.
  - **Evidence pointer** Figure 4, FRAP methods section
  - **Concern** The FRAP experiments compare proteins with and without the EH mutation, which disrupts SAM polymerization. However, the authors also show that the EH mutation changes the net charge of the SAM domain. It is therefore difficult to attribute the observed changes in FRAP recovery solely to the loss of oligomerization, as charge changes could also affect protein dynamics and interactions within the condensate. The authors acknowledge this in the discussion, but the claim as stated in the results is somewhat overreaching.
  - **Why it matters** The separation of oligomerization and phase separation is a central claim of the paper. If the FRAP data are confounded by charge effects, the conclusion that oligomerization specifically modulates dynamics (rather than formation) is weakened.
  - **Resolution test** The authors could perform FRAP experiments with a charge-neutralizing mutation that does not disrupt polymerization, or use a different approach to perturb oligomerization (e.g., a cross-linking agent) to confirm that the effect on dynamics is specifically due to oligomerization.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** No
  - **Axis** Generalizability of findings
  - **Claim pointer** The authors conclude that "linker-SAM interactions affect phase separation largely independent of SAM oligomerization" and that this is a general principle.
  - **Evidence pointer** Figures 1-5
  - **Concern** The study focuses on a single pair of linkers (Drosophila Ph and human PHC3) and a limited set of mutations. While the findings are internally consistent, it is unclear whether the proposed mechanism (linker-SAM charge interactions modulating phase separation) is a general principle applicable to other PHC family members or other SAM-containing proteins. The authors do not test other linkers or SAM domains.
  - **Why it matters** The title and abstract suggest a general principle ("tunes phase separation and oligomerization"). If the effect is specific to the Ph/PHC3 pair, the broader significance is diminished.
  - **Resolution test** The authors could test additional linker-SAM combinations (e.g., PHC1, PHC2) or perform a more systematic mutagenesis to demonstrate that the charge-based mechanism is a general feature of this protein family.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Mechanistic link to function
  - **Claim pointer** The authors state that "PHC3L and SAMsurf affect Ph function in Drosophila imaginal discs" and that this is due to altered condensate properties.
  - **Evidence pointer** Figure 7, growth assay section
  - **Concern** The growth assay shows that expression of PhPHC3L or PhSAMsurf reduces posterior compartment size compared to wild-type Ph. However, the authors do not directly demonstrate that this growth suppression is caused by the altered condensate properties (e.g., smaller size, lower threshold). It is possible that the mutations affect other functions of Ph, such as its interaction with chromatin or other proteins, independent of condensate formation.
  - **Why it matters** The paper aims to establish a link between condensate properties and function. Without a direct causal link, the functional significance of the observed condensate changes remains correlative.
  - **Resolution test** The authors could attempt to rescue the growth phenotype by expressing a construct that restores condensate size without affecting other Ph functions, or by using a separation-of-function mutation that specifically disrupts condensate formation without affecting chromatin binding.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity of figure legends
  - **Affected element** Figure 1
  - **Evidence pointer** Figure 1 legend
  - **Issue** The legend for Figure 1 is dense and does not clearly indicate which panels correspond to which experimental conditions (e.g., protein concentration, DNA presence). This makes it difficult to interpret the data without referring back to the text.
  - **Required correction** Please expand the figure legend to explicitly state the conditions for each panel, including protein concentrations, DNA concentrations, and salt conditions.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Statistical reporting
  - **Affected element** Multiple figures
  - **Evidence pointer** Figures 3, 6, 7
  - **Issue** The text states that statistical tests were performed, but the specific p-values and test types are not consistently reported in the figure legends or in the text. For example, in Figure 3, the comparison of csat values between conditions is mentioned, but the statistical significance is not stated.
  - **Required correction** Please ensure that all statistical comparisons are clearly reported, including the test used, the number of replicates, and the exact p-values or confidence intervals.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Methodological detail
  - **Affected element** MD simulations
  - **Evidence pointer** Methods section, MD simulations
  - **Issue** The description of the MD simulations is brief. It is not clear how many independent simulations were run, how the initial configurations were generated, or how the error bars on the csat values were calculated.
  - **Required correction** Please provide more detail on the simulation setup, including the number of replicates, the equilibration protocol, and the method for calculating uncertainties.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Data availability
  - **Affected element** Data and code availability section
  - **Evidence pointer** Data and code availability section
  - **Issue** The data and code availability section is incomplete. It does not state where the raw data, analysis scripts, or simulation input files can be accessed.
  - **Required correction** Please provide a clear statement on data and code availability, including accession numbers or repository links, in accordance with journal policy.
- **Technical failings that need to be addressed before the case is established**
  1. The FRAP data interpretation is confounded by potential charge effects of the EH mutation (R1-M1).
  2. The generalizability of the proposed mechanism is not established (R1-M2).
  3. The causal link between condensate properties and growth suppression is not directly demonstrated (R1-M3).
- **Assessment against Nature-style criteria**
  - **Originality** The study is original in its focus on the role of a disordered linker in modulating SAM oligomerization and phase separation. While previous work has implicated linkers in phase separation, the specific mechanistic insight into linker-SAM charge interactions and the separation of oligomerization from phase separation is novel.
  - **Scientific importance** The findings are important for understanding the molecular basis of Polycomb body formation and function. They also contribute to the broader understanding of how sequence features in disordered regions can tune condensate properties, which is a topic of high current interest.
  - **Interdisciplinary readership** The work will appeal to researchers in epigenetics, biophysics, and cell biology. The combination of computational and experimental approaches makes it accessible to a broad audience, though some familiarity with phase separation concepts is assumed.
  - **Technical soundness** The experimental design is generally sound, with appropriate controls and orthogonal assays. However, the concerns about FRAP interpretation and the lack of a direct causal link to function are technical weaknesses that need to be addressed.
  - **Readability for nonspecialists** The paper is well-written and the main concepts are explained clearly. However, the methods section is highly detailed and may be challenging for nonspecialists. The figures are informative but some legends could be clearer.
- **Recommendation posture** Supportive if technical concerns are resolved. The study presents a compelling and novel mechanism for how a disordered linker tunes phase separation and oligomerization. The main claims are largely supported by the data, but the concerns about FRAP interpretation, generalizability, and the causal link to function need to be addressed to fully establish the case.

## Risk / unsupported claims
- The claim that "Oligomerization influences condensate dynamics but minimally impacts condensate formation" is not fully supported due to the confounding charge effects of the EH mutation.
- The claim that the findings represent a "general" principle for how disordered linkers tune phase separation is not supported, as only one linker pair was tested.
- The claim that altered condensate properties cause growth suppression in imaginal discs is not directly supported; the effect could be due to other functions of Ph.
- The statement that "linker-SAM interactions affect phase separation largely independent of SAM oligomerization" is supported for the specific constructs tested, but the underlying mechanism (charge interactions) is inferred from simulations and not directly experimentally validated.