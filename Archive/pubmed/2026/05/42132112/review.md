## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusion) as provided
- **Assessment boundary** Scientific content, methodological rigor, internal consistency, and support of claims by presented evidence. Editorial or formatting issues are noted only where they affect scientific clarity.
- **Shared manuscript claim summary** The authors propose that APE1 locates AP sites via 1D diffusion along DNA, enabled by two cooperating modules: (i) Mg2+ coordination at the active site that neutralizes negative charge and stabilizes DNA contacts, and (ii) an N-terminal intrinsically disordered region (IDR) that makes transient contacts with DNA and, via a newly identified Arg177 residue in the structured domain, prolongs residence time to permit long-range sliding. The IDR is presented as a eukaryotic innovation absent in prokaryotic ExoIII.
- **Visible evidence base** smFRET binding/dissociation and translocation assays; DNA curtain single-molecule tracking; EMSA; enzyme activity assays; all-atom MD simulations (AMBER ff99SB-ILDN-phi, CUFIX); DLS for hydrodynamic radius; site-directed mutants (E96A, D210N, 0× IDR, 2× IDR)
- **Missing materials affecting confidence** Figures and supplementary figures are referenced but not provided. Supplementary Tables S1, Supplementary Movies S1–S4, and Supplementary Figures S1–S16 are not available for inspection. Exact imaging parameters (frame rate for DNA curtains, laser power, labeling stoichiometry) are partially described but not fully specified. Statistical details for some comparisons (e.g., error bars in Fig. 2H, 3B, 3C) are not fully described in the text.

## Reviewer

### Overall assessment
This manuscript addresses a significant and timely question in DNA repair: how APE1 searches for AP sites among vast excess of undamaged DNA. The combination of single-molecule assays (smFRET, DNA curtains) with MD simulations is well suited to the question, and the central claim that APE1 uses 1D diffusion, facilitated by both Mg2+ and the N-terminal IDR, is plausible and mechanistically interesting. The identification of Arg177 as a residue that may mediate IDR-dependent DNA contacts is potentially novel. However, several concerns limit the strength of the conclusions as currently presented. The evidence for the specific role of Arg177 is indirect (derived from MD contact analysis without experimental validation). The claim that the IDR is a eukaryotic innovation is weakened by the lack of direct phylogenetic analysis. The quantitative discrepancy between simulated and experimental diffusion coefficients is acknowledged but not fully reconciled. The manuscript would be strengthened by experimental validation of the Arg177 role, clearer presentation of statistical methods, and a more nuanced discussion of the limitations of the MD model.

### Who would be interested in the results, and why
Researchers in DNA repair, genome stability, and single-molecule biophysics would find this work of interest. The study provides direct visualization of APE1's search mechanism, which has been inferred but not directly observed. The proposed dual role of Mg2+ in both catalysis and search dynamics is conceptually important. The finding that an IDR can enhance processivity of a DNA repair enzyme has broader implications for understanding how other DNA-binding proteins with disordered regions achieve efficient target search. The evolutionary comparison with prokaryotic ExoIII may interest researchers studying the evolution of DNA repair pathways.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength for a central mechanistic claim
- **Claim pointer** The authors claim that "Arg177 within the structured nuclease domain" engages in "continuous interactions" that "prolong residence time and enable long-range diffusion" (Abstract, Results section "Effect of IDR on the diffusion of APE1 in molecular dynamics simulations").
- **Evidence pointer** Figure 7G (referenced, not provided); Results section "Effect of IDR on the diffusion of APE1 in molecular dynamics simulations"
- **Concern** The central claim that Arg177 is functionally important for APE1's diffusion is based solely on MD contact analysis. No experimental validation (e.g., site-directed mutagenesis of Arg177 followed by single-molecule assays) is presented. The contact fraction analysis identifies Arg177 as a high-contact residue, but this does not establish causality. The authors do not test whether mutation of Arg177 abolishes the IDR-dependent enhancement of diffusion or residence time. Without such validation, the claim that Arg177 is "unprecedented" and functionally critical is not established.
- **Why it matters** The identification of a specific residue that mediates the IDR's effect is a key part of the proposed mechanism. If Arg177 is not experimentally validated, the mechanistic model remains speculative. The claim of novelty ("unprecedented") requires experimental support.
- **Resolution test** Provide experimental data (e.g., smFRET or DNA curtain assays) using an Arg177 mutant (e.g., Arg177Ala) showing loss of IDR-dependent diffusion enhancement or reduced residence time. Alternatively, provide additional computational evidence (e.g., free energy calculations) that specifically tests the role of Arg177.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative consistency between simulation and experiment
- **Claim pointer** The authors state that simulated diffusion coefficients for the 0× IDR mutant are "markedly higher" than experimental values and attribute this to GC-rich DNA sequence (Results section "Effect of IDR on the diffusion of APE1 in molecular dynamics simulations").
- **Evidence pointer** Figure 7J (referenced, not provided); Results section "Effect of IDR on the diffusion of APE1 in molecular dynamics simulations"
- **Concern** The discrepancy between simulated and experimental diffusion coefficients for the 0× IDR mutant is acknowledged, and a single additional simulation with AT-rich DNA is presented as a partial reconciliation. However, the authors do not provide a systematic analysis of how sequence composition affects the simulated diffusion. The claim that "in more physiologically relevant, mixed-sequence contexts, Dz would more match experimental measurements" is speculative. The manuscript would benefit from a more rigorous treatment of this discrepancy, including error estimates and a discussion of other potential sources of the mismatch (e.g., force field limitations, finite-size effects, or the absence of the IDR in the 0× mutant simulation).
- **Why it matters** The quantitative agreement between simulation and experiment is important for establishing the credibility of the MD model as a tool for mechanistic interpretation. If the model cannot reproduce experimental results, its predictions (e.g., the role of Arg177) are less reliable.
- **Resolution test** Provide a more detailed analysis of the sequence dependence of simulated diffusion, including multiple sequence contexts and error bars. Discuss other potential sources of the discrepancy and how they might be addressed.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Support for an evolutionary claim
- **Claim pointer** The authors state that the N-terminal IDR is "a feature conserved only in eukaryotic homologs but absent in prokaryotic ExoIII" (Abstract) and that its presence is an "evolutionary innovation in eukaryotic DNA repair" (Abstract, Discussion).
- **Evidence pointer** Abstract; Introduction; Discussion
- **Concern** The claim that the IDR is a eukaryotic innovation is based on a single comparison with E. coli ExoIII. No systematic phylogenetic analysis is presented. The authors do not survey the presence or absence of N-terminal IDRs across a broader range of prokaryotic and eukaryotic AP endonucleases. The statement "conserved only in eukaryotic homologs" implies a level of analysis that is not documented in the text.
- **Why it matters** The evolutionary narrative is a prominent part of the abstract and discussion. If the claim is not supported by a proper comparative analysis, it should be softened or supported with additional data.
- **Resolution test** Provide a phylogenetic analysis of AP endonuclease sequences from diverse prokaryotes and eukaryotes, showing the distribution of N-terminal IDRs. Alternatively, soften the claim to state that the IDR is present in the eukaryotic homologs examined and absent in the prokaryotic ExoIII examined.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Statistical rigor and reproducibility of single-molecule data
- **Claim pointer** The authors report quantitative values for translocation probabilities, diffusion coefficients, and residence times (e.g., "probability of AP site recognition via 1D diffusion was ~66%", "diffusion coefficients were largely independent of ionic strength").
- **Evidence pointer** Figures 2G, 2H, 3B, 3C, 4D–H, 5C–E, 6G–J (referenced, not provided); Results sections "Effect of Mg2+ ions on 1D diffusion of APE1 along DNA", "Effect of IDR on the diffusion of APE1 along extended DNA", "APE1 finds AP sites via 1D diffusion"
- **Concern** The manuscript does not provide sufficient detail on the statistical treatment of single-molecule data. For example, the number of molecules analyzed, the number of independent experiments, and the methods for error estimation (e.g., standard error of the mean, confidence intervals) are not consistently described. The bootstrap method for confidence intervals is mentioned for translocation probability, but it is not clear whether this was applied to all quantitative comparisons. The criteria for including or excluding molecules from analysis are not stated.
- **Why it matters** Single-molecule assays are inherently noisy, and rigorous statistical treatment is essential for the conclusions to be reliable. Without this information, the reader cannot assess the robustness of the reported differences (e.g., between wild-type and 0× IDR mutant).
- **Resolution test** Provide a detailed description of the statistical methods, including the number of molecules/experiments, error estimation, and criteria for data inclusion. Ensure that all quantitative claims are supported by appropriate statistical tests.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Completeness of the mechanistic model
- **Claim pointer** The authors propose that Mg2+ and the IDR act "synergistically" to promote sliding (Abstract, Discussion).
- **Evidence pointer** Abstract; Discussion
- **Concern** The claim of synergy implies that the combined effect of Mg2+ and the IDR is greater than the sum of their individual effects. However, the manuscript does not present experiments that directly test this. The effects of Mg2+ and IDR are examined separately (e.g., Mg2+ titration in Fig. 2, IDR deletion in Figs. 3 and 5), but no experiment combines these perturbations in a way that would demonstrate synergy (e.g., comparing the effect of Mg2+ on wild-type vs. 0× IDR mutant). The term "synergize" is used in the abstract but is not operationally defined or tested.
- **Why it matters** The claim of synergy is a key part of the proposed model. If the two modules act independently (additively), the model is less interesting. The manuscript should either provide evidence for synergy or use more cautious language.
- **Resolution test** Perform experiments that directly test for synergy, such as measuring the effect of Mg2+ on the diffusion of wild-type vs. 0× IDR mutant. If the Mg2+ effect is similar in both backgrounds, the claim of synergy should be revised.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** "monkey bar"-like behaviors (Results section "Effect of IDR on the diffusion of APE1 in molecular dynamics simulations")
- **Evidence pointer** Results section "Effect of IDR on the diffusion of APE1 in molecular dynamics simulations"
- **Issue** The term "monkey bar"-like behaviors is informal and not defined. It is unclear what specific dynamic behavior this refers to.
- **Required correction** Define the term or replace it with a more precise description of the observed dynamics (e.g., "transient detachment and reattachment of the IDR to the DNA").

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** MD simulation details
- **Evidence pointer** Materials and methods section "MD simulation"
- **Issue** The description of the MD simulations lacks some details that would be needed for reproduction, such as the total simulation time for each system (only average times are given), the equilibration protocol, and the criteria for defining "contact" (the 1.25 nm cutoff is stated, but the reference point for the distance is not fully clear).
- **Required correction** Provide the total simulation time for each replicate, a more detailed equilibration protocol, and a precise definition of the contact criterion.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of data
- **Affected element** D210N residence time
- **Evidence pointer** Results section "Catalytic dead mutant D210N behaves similarly to wild type"; Supplementary Figure S10H
- **Issue** The authors report that D210N has a ~2.5-fold longer AP-residence time than wild-type and attribute this to reduced electrostatic repulsion. However, an alternative explanation is that wild-type APE1 cleaves the DNA and dissociates, while D210N remains bound. The authors acknowledge this but do not fully discuss the implications for the interpretation of the wild-type residence time.
- **Required correction** Add a sentence to the Discussion acknowledging that the wild-type residence time may be limited by cleavage, and that the "true" search-related residence time may be longer.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation of data
- **Affected element** Figure callouts
- **Evidence pointer** Throughout Results
- **Issue** The manuscript references many supplementary figures and tables, but the main text does not always clearly indicate what the key finding of each supplementary figure is.
- **Required correction** Briefly describe the key finding of each supplementary figure in the text where it is cited.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Consistency of terminology
- **Affected element** "1D diffusion" vs. "sliding"
- **Evidence pointer** Throughout
- **Issue** The terms "1D diffusion" and "sliding" are used interchangeably. While this is common, it would be helpful to define the terms early and use them consistently.
- **Required correction** Define "1D diffusion" and "sliding" in the Introduction and use the terms consistently throughout.

### Technical failings that need to be addressed before the case is established
R1-M1 (Arg177 validation) is the most significant technical gap. The central mechanistic claim relies on a residue identified only in silico. Without experimental validation, the case is not established. R1-M4 (statistical rigor) is also important, as the quantitative claims of the paper cannot be fully assessed without proper statistical detail.

## Risk / unsupported claims
- The claim that Arg177 is "unprecedented" and functionally critical is not supported by experimental evidence (only MD contact analysis).
- The claim that the IDR is "conserved only in eukaryotic homologs" is not supported by a systematic phylogenetic analysis.
- The claim of "synergy" between Mg2+ and the IDR is not directly tested.
- The quantitative agreement between simulated and experimental diffusion coefficients for the 0× IDR mutant is not fully established; the discrepancy is acknowledged but not rigorously resolved.
- The statement that "APE1 predominantly recognizes AP sites through 1D diffusion rather than stochastic 3D collisions" is based on the 66% figure, but the statistical uncertainty on this value is not reported.

## Assessment against Nature-style criteria
- **Originality** The study is original in its direct visualization of APE1's search dynamics and its proposal of a dual mechanism involving both Mg2+ and the IDR. The identification of Arg177 as a potential mediator of IDR function is novel, though unvalidated.
- **Scientific importance** The question of how DNA repair enzymes find rare lesions is of fundamental importance. The proposed mechanism, if validated, would have implications for understanding genome surveillance and the evolution of DNA repair. The work is likely to be of interest to a broad audience in DNA repair and biophysics.
- **Interdisciplinary readership** The study bridges single-molecule biophysics, computational biology, and DNA repair. The writing is generally accessible, but the methods sections are dense and may be challenging for non-specialists. The broader significance is clearly articulated in the abstract and discussion.
- **Technical soundness** The experimental design is generally sound, but the lack of validation for the Arg177 claim and the incomplete statistical reporting are significant weaknesses. The MD simulations are state-of-the-art but the discrepancy with experiment is not fully resolved.
- **Readability for nonspecialists** The abstract is clear and accessible. The main text is well-organized, but the results sections are detailed and may be difficult for readers outside the field. The figures (not provided) would be critical for accessibility.

## Recommendation posture
Supportive if technical concerns are resolved. The core question is important, and the combination of methods is appropriate. However, the central mechanistic claim regarding Arg177 requires experimental validation, and the statistical rigor of the single-molecule data must be improved. The evolutionary claim should be either supported with a proper phylogenetic analysis or softened. If these concerns are addressed, the manuscript would be a strong contribution. As presented, the case is not fully established from the provided evidence.