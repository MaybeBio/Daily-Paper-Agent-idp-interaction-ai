## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, materials and methods, and supporting information references.
- **Assessment boundary** Scientific content, methodological soundness, validity of claims relative to presented evidence, and suitability for the stated journal context. No assessment of code implementation or web server functionality beyond what is described.
- **Shared manuscript claim summary** The authors present PolyProline Predictor (PPP), a web server for sequence-based prediction of polyproline II (PPII) helices. They claim PPP identifies PPII-prone segments in diverse proteins, including glycine-rich plant proteins, mycobacterial PE_PGRS virulence factors, GroEL C-termini, and the pre-RHIM region of human RIPK3. They validate predictions using MD simulations, CD, and NMR for RIPK3, and report that PPP outperforms existing web-based tools for glycine-rich sequences.
- **Visible evidence base** Full text with figures referenced (Figures 1–6), tables (Tables 1, 2, S1–S4), and supplementary figures (S1–S23). Raw data availability statement indicates NMR data deposited in BMRB; MD and CD data available upon request.
- **Missing materials affecting confidence** Figures and tables are referenced but not provided in the submitted material. Supplementary figures and tables are mentioned but not included. This limits independent verification of quantitative results, particularly MD occupancy values, CD spectra, and NMR chemical shift data.

## Reviewer
- **Overall assessment** The manuscript describes a useful and potentially valuable web tool for PPII helix prediction, addressing a genuine gap in available bioinformatics resources. The conceptual approach of using empirical alignment against experimentally validated PPII segments is sound and offers interpretability advantages over black-box machine learning methods. The RIPK3 validation combining MD, CD, and NMR is a strength. However, several concerns limit the strength of the claims as presented. The benchmarking against existing tools is narrow and the reported performance differences, while suggestive, are not rigorously quantified. The experimental validation is limited to two short peptides from one protein, and the connection between predicted PPII propensity and functional relevance in RIPK3 assembly remains speculative. The manuscript would be strengthened by clearer presentation of the web server's output, more comprehensive benchmarking, and additional validation across the diverse protein classes claimed.

- **Who would be interested in the results, and why** Structural biologists, bioinformaticians, and researchers studying intrinsically disordered proteins, protein-protein interactions, amyloid formation, and low-complexity regions. The tool addresses a recognized gap in secondary structure prediction, and the demonstration of PPII propensity in biologically important regions (e.g., RIPK3 pre-RHIM, GroEL C-termini, PE_PGRS proteins) will interest those studying these specific systems. The interpretable nature of the predictions may appeal to experimentalists seeking hypothesis-generating tools.

- **Major strengths**
  1. Addresses a genuine gap: PPII prediction is underrepresented in available web-based tools, and the empirical alignment approach is conceptually distinct from machine learning methods.
  2. The RIPK3 validation combining MD, CD, and NMR provides multi-technique support for the prediction in a biologically relevant system.
  3. The negative control using a scrambled PE_PGRS33 sequence is a good experimental design element that strengthens the claim of sequence specificity.
  4. The tool is freely accessible as a web server, enhancing utility for the community.
  5. The discussion of limitations, including the conservative dihedral angle ranges and potential underrepresentation of dynamic PPII conformations, is honest and appropriate.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of benchmarking
- **Claim pointer** The authors claim PPP is "particularly effective at detecting glycine-rich segments that other tools overlook" and that PPP "consistently recovered" PPII-prone segments across diverse proteins.
- **Evidence pointer** Table 1, Table S3, Discussion section
- **Concern** The benchmarking against PPIIPRED and DynaMine is presented qualitatively. The authors report mean scores for each tool across seven systems but do not provide statistical analysis, confidence intervals, or a clear quantitative definition of "effective" or "overlook." The claim that PPP is superior for glycine-rich sequences appears to rest on a small number of examples, and the comparison is not controlled for threshold effects or tool-specific scoring scales. Additionally, the authors state that PolyprOnline and DSSP 4 were excluded because they require structures, which is reasonable, but this means the comparison is only against two sequence-based tools, one of which (DynaMine) is not primarily designed as a PPII predictor.
- **Why it matters** The central claim of the manuscript is that PPP fills a gap in PPII prediction. Without rigorous, quantitative benchmarking against existing tools, the added value of PPP relative to alternatives is not established. Readers cannot assess whether PPP offers genuine improvement or merely a different approach with similar performance.
- **Resolution test** Provide a systematic benchmark with a defined dataset of experimentally validated PPII and non-PPII segments, report sensitivity, specificity, and ROC-type analyses for PPP, PPIIPRED, and DynaMine, and include statistical significance testing for performance differences. Alternatively, clearly frame the manuscript as presenting a tool with a different approach rather than superior performance.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency for functional claims
- **Claim pointer** The authors state that PPII helices flanking the RIPK3 RHIM "may regulate its amyloid assembly, offering structural insight into mechanisms of functional amyloid formation" and that these motifs "could modulate RHIM amyloid formation."
- **Evidence pointer** Results section "Experimental validation of PPII helix conformation in human RIPK3", Discussion section
- **Concern** The experimental validation demonstrates that two isolated peptides from the RIPK3 pre-RHIM region adopt partially populated PPII conformations in solution. However, no experiments directly test whether these PPII elements influence RHIM amyloid formation, kinetics, or morphology. The functional claim is therefore speculative and not supported by the presented data. The connection between local PPII propensity in isolated peptides and behavior in the full-length protein or in amyloid assembly contexts is not established.
- **Why it matters** The functional significance of the identified PPII segments is a key motivation for the work and a major point of interest for readers. Overstating functional implications without direct evidence weakens the manuscript's scientific rigor and could mislead readers about the established findings.
- **Resolution test** Either temper the functional claims to clearly indicate they are hypotheses requiring direct testing, or add experiments that directly assess the role of the identified PPII segments in RHIM amyloid formation (e.g., mutagenesis studies, kinetic assays with full-length protein or larger constructs).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of validation
- **Claim pointer** The authors claim PPP "successfully identified conserved PPII motifs in diverse proteins" and that MD simulations "support" PPII predictions across plant, bacterial, and human proteins.
- **Evidence pointer** Results section "Computational validation of PPII helices in plant, viral, bacterial, and human proteins", Figures 4–5, Figures S2–S22
- **Concern** The MD validation is presented for multiple proteins, but the experimental validation (CD, NMR) is limited to two short peptides from RIPK3. The MD simulations use a single force field (CHARMM36m) and the PPII classification depends on dihedral angle criteria that may not capture the full conformational complexity. The authors acknowledge that MD results for plant proteins and RIPK3 show heterogeneous, transient PPII populations, which is consistent with weak predictions, but the distinction between "stable bundle" and "transient" is based on occupancy thresholds that are not clearly justified. The scrambled-sequence control is valuable but only addresses one protein.
- **Why it matters** The claim of broad applicability across diverse protein classes is a key selling point of the tool. Without experimental validation in at least one additional system beyond RIPK3, or a more rigorous framework for interpreting MD-derived PPII occupancy, the generalizability of PPP's predictions remains uncertain.
- **Resolution test** Add experimental validation (CD or NMR) for at least one additional predicted PPII segment from a different protein class (e.g., a plant glycine-rich protein or a PE_PGRS protein). Alternatively, provide a more detailed analysis of the MD methodology, including justification of occupancy thresholds and demonstration that results are robust across force fields or simulation conditions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Methodological transparency
- **Claim pointer** The authors describe PPP as providing "an interpretable, composition-, and position-sensitive similarity map" and state that it "aligns query sequences against a curated database of experimentally validated PPII helices."
- **Evidence pointer** Materials and Methods section "Computational overview", Figure 1
- **Concern** The description of the scoring algorithm is incomplete. The authors mention ungapped alignments and percent sequence identity thresholds, but do not specify how the similarity map is generated, how scores are normalized, how the database was curated beyond dihedral angle criteria, or how the "empirical PPII propensity cutoff" was determined. The relationship between the alignment score and the reported "PPII propensity" is not formally defined. This lack of detail prevents independent implementation or full evaluation of the method.
- **Why it matters** For a web server tool, methodological transparency is essential for users to understand the basis of predictions and for the scientific community to evaluate the approach. Incomplete method description limits reproducibility and the ability of others to build upon or compare with the tool.
- **Resolution test** Provide a complete mathematical description of the scoring algorithm, including the similarity metric, normalization procedures, and how the propensity cutoff is derived. Include a flowchart or pseudocode of the algorithm. Specify database curation criteria in full, including any filtering steps and the exact dihedral angle ranges used.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 1
- **Evidence pointer** Figure 1 (referenced in Results)
- **Issue** The workflow and example output are described in the text but the figure itself is not available for review. The description suggests the figure shows the server interface and output, but it is unclear whether the output format is intuitive and whether the similarity map is visually interpretable.
- **Required correction** Ensure Figure 1 clearly shows the input interface, the output format, and an example similarity map with annotations explaining how to interpret the results.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Table 1, Table S3
- **Evidence pointer** Table 1, Table S3
- **Issue** The benchmarking results are reported as mean scores without measures of variance or sample sizes. It is unclear how many sequences or segments were used for each system and whether the reported means are stable.
- **Required correction** Report standard deviations or confidence intervals for all mean scores, and specify the number of segments or sequences analyzed for each system.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Throughout
- **Evidence pointer** Abstract, Introduction, Discussion
- **Issue** The terms "PPII helix," "PPII helical bundle," and "PPII-prone segment" are used somewhat interchangeably. The distinction between a single PPII helix and a bundle of multiple helices is important, particularly for the discussion of glycine-rich proteins.
- **Required correction** Define these terms clearly at first use and use them consistently throughout the manuscript.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data Availability Statement
- **Evidence pointer** Data Availability Statement
- **Issue** The statement indicates that MD simulation data are available upon request but not deposited in a public repository. Given the increasing expectations for open data sharing, this is a limitation.
- **Required correction** Consider depositing MD simulation inputs, trajectories, and analysis scripts in a public repository (e.g., Zenodo, OSF) to enhance reproducibility.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction, Discussion
- **Evidence pointer** Introduction, Discussion
- **Issue** The discussion of existing PPII prediction tools is brief. The authors mention PolyprOnline, PPIIPRED, and DynaMine but do not provide a systematic comparison of their features, limitations, and performance characteristics. This limits the reader's ability to contextualize the claimed advantages of PPP.
- **Required correction** Expand the description of existing tools, including their underlying methods, input requirements, and known limitations, to provide a clearer rationale for the development of PPP.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Web server accessibility
- **Affected element** Abstract, Materials and Methods
- **Evidence pointer** Abstract, Materials and Methods
- **Issue** The web server URL is provided, but there is no mention of whether the server is freely accessible, whether registration is required, or what usage limits apply. This information is important for potential users.
- **Required correction** Add a brief statement about accessibility, registration requirements, and any usage policies.

## Risk / unsupported claims
- The claim that PPII helices flanking the RIPK3 RHIM "may regulate its amyloid assembly" is not directly supported by experimental evidence presented; this is a hypothesis requiring testing.
- The claim that PPP is "particularly effective at detecting glycine-rich segments that other tools overlook" is not rigorously established due to the limited and non-quantitative benchmarking.
- The claim that PPP "successfully identified conserved PPII motifs in diverse proteins" is based primarily on computational predictions and MD simulations, with experimental validation limited to two peptides from one protein.
- The assertion that MD simulations "support" PPII predictions across all tested proteins is weakened by the acknowledged heterogeneity and transience of PPII populations in several systems, and the lack of a clear threshold for what constitutes "support."
- The statement that "the presence of a large number of similar sequences suggests that many glycine-rich regions with propensity to form PPII helices may be present in plants" is speculative and not quantitatively supported.
- The claim that PPP "fills a critical gap in bioinformatics tools" is reasonable but not fully substantiated without more comprehensive comparison to existing and emerging methods.