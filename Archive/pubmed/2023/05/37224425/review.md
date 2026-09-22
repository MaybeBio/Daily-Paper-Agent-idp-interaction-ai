## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodology, data interpretation, and conclusions as presented in the manuscript
- **Shared manuscript claim summary** The authors identify novel short linear motif (SLiM)-based ligands for the FERM domains of ezrin, radixin, moesin, and merlin using proteomic peptide-phage display, characterize binding affinities, define distinct binding sites (F3a and F3b) for different motif classes, and propose an allosteric interplay between these sites based on computational modeling and mutational analysis.
- **Visible evidence base** Abstract, Introduction, Materials and Methods, Results and Discussion, Concluding Remarks, figure legends referenced in text, supplementary table references
- **Missing materials affecting confidence** Raw phage display enrichment data, full supplementary tables (S1–S7), figure images, gel filtration/DLS raw data, and complete computational modeling output files were not provided for independent verification.

## Reviewer
- **Overall assessment** This manuscript presents a systematic and technically sound exploration of SLiM-based interactions of ERM and merlin FERM domains. The combination of phage display, affinity measurements, mutational analysis, and computational modeling is appropriate and generally well executed. The identification of a large number of novel ligands and the distinction between F3a and F3b binding motifs represent useful contributions to the field. However, the evidence for the proposed allosteric interplay between binding sites is indirect and partially speculative, and the manuscript would benefit from additional experimental validation to firmly establish this claim. The limited number of merlin ligands identified also constrains the comparative analysis between merlin and the ERMs.
- **Who would be interested in the results, and why** Researchers studying FERM domain biology, ERM protein function, merlin tumor suppressor mechanisms, SLiM-based protein-protein interactions, and scaffolding protein networks. The results may also be of interest to those studying cell adhesion, cytoskeletal dynamics, and Hippo pathway regulation.
- **Major strengths** The study uses a well-established proteomic peptide-phage display approach to comprehensively map FERM domain ligands. The combination of experimental and computational methods provides complementary evidence for binding site assignments. The validation of known interactors supports the quality of the screening approach. The identification of distinct motif classes and their differential binding site preferences adds mechanistic insight.
- **Major Concerns** The proposed allosteric communication between F3a and F3b sites is supported primarily by indirect competition experiments and computational modeling, without direct biophysical evidence such as conformational analysis or NMR studies. The functional relevance of the identified interactions in cellular contexts is not addressed. The manuscript does not fully explore the potential physiological significance of the differential binding specificities between merlin and the ERMs.
- **Minor Comments** The presentation of the computational docking results could be more detailed, particularly regarding the scoring functions and convergence criteria. The manuscript would benefit from a more explicit discussion of the limitations of the phage display approach for detecting low-affinity or transient interactions. Some figure references in the text do not clearly indicate which panels correspond to which data.
- **Technical failings that need to be addressed before the case is established** The evidence for allosteric communication between F3a and F3b sites requires additional experimental support beyond competition binding assays and computational modeling. The manuscript should include direct measurements of conformational changes or use alternative approaches such as hydrogen-deuterium exchange or NMR to substantiate this claim.
- **Assessment against Nature-style criteria** Originality: The study provides a comprehensive SLiM-based interactome map for ERM and merlin FERM domains, which extends previous knowledge. Scientific importance: The findings have implications for understanding FERM domain-mediated signaling and scaffolding, but the functional significance in cellular contexts remains to be established. Interdisciplinary readership: The work bridges structural biology, biochemistry, and cell signaling, potentially appealing to a broad audience. Technical soundness: The experimental approaches are generally well executed, but the allosteric claim requires stronger evidence. Readability for nonspecialists: The manuscript is clearly written and accessible, though some computational details may be challenging for non-experts.
- **Recommendation posture** Supportive if the allosteric communication claim is strengthened with additional experimental evidence or appropriately softened in the conclusions.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength for allosteric mechanism
- **Claim pointer** The manuscript claims that binding of F3a ligands induces conformational changes that reduce affinity for F3b ligands, based on asymmetric competition experiments and computational modeling.
- **Evidence pointer** Results and Discussion section "Unveiling the Interplay between Different Ligands", Figure 6
- **Concern** The asymmetric competition between F3a and F3b ligands is interpreted as evidence for allosteric communication. However, the competition experiments only show that F3a ligands can block F3b binding, which could also be explained by steric hindrance, overlapping binding interfaces, or indirect effects. The computational modeling using FastRelax to "open" the F3b pocket is suggestive but not conclusive evidence for a conformational change in solution.
- **Why it matters** The allosteric model is a central conclusion of the manuscript and has implications for understanding how FERM domain ligands may regulate each other's binding. If this claim is not firmly established, the broader conclusion about the FERM domain acting as a "switchable interaction hub" is weakened.
- **Resolution test** Provide direct biophysical evidence of conformational changes, such as NMR chemical shift perturbation, hydrogen-deuterium exchange mass spectrometry, or small-angle X-ray scattering, comparing the FERM domain in the presence and absence of F3a and F3b ligands. Alternatively, perform mutagenesis of residues predicted to mediate the allosteric communication and show that this disrupts the asymmetric competition.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Functional validation in cellular context
- **Claim pointer** The manuscript identifies numerous novel SLiM-based interactions and suggests they may be relevant for ERM and merlin function in cell adhesion and transcriptional regulation.
- **Evidence pointer** Results and Discussion section "Identification and Characterization of FERM Domain Ligands", Concluding Remarks
- **Concern** The study is entirely based on in vitro biochemical and computational approaches. No experiments are performed to demonstrate that the identified interactions occur in cells or have functional consequences. The GO enrichment analysis suggests potential biological relevance, but this is not experimentally tested.
- **Why it matters** The physiological significance of the identified interactions remains unclear. Without cellular validation, it is difficult to assess whether the identified ligands represent biologically relevant interactors or are primarily in vitro artifacts of the screening approach.
- **Resolution test** Perform co-immunoprecipitation experiments in relevant cell lines to confirm endogenous interactions for a subset of the identified ligands. Alternatively, use CRISPR-mediated knockout or knockdown approaches to test whether disruption of specific interactions affects cellular phenotypes such as cell adhesion, migration, or Hippo pathway activity.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Comparative analysis of merlin versus ERMs
- **Claim pointer** The manuscript states that merlin has a more limited set of ligands compared to the ERMs and that the FERM domains have partially overlapping but distinct specificities.
- **Evidence pointer** Results and Discussion section "Identification and Characterization of FERM Domain Ligands", Figure 2
- **Concern** The number of merlin ligands identified is substantially lower than for the ERMs, and the authors acknowledge that only eight medium-confidence peptides were found. This limited dataset constrains the comparative analysis and makes it difficult to draw firm conclusions about the distinct specificities of merlin versus the ERMs. The lower number of merlin ligands could reflect technical issues with the phage display screening rather than genuine biological differences.
- **Why it matters** The comparison between merlin and the ERMs is a key aspect of the manuscript, as merlin has distinct functions and is a tumor suppressor. If the merlin dataset is incomplete due to technical limitations, the conclusions about differential specificities may not be reliable.
- **Resolution test** Perform additional phage display screens with higher library coverage or use alternative screening approaches such as peptide arrays or SPOT synthesis to more comprehensively map merlin FERM domain ligands. Validate the identified merlin ligands with additional biochemical assays to confirm their specificity.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Fluorescence polarization assay
- **Evidence pointer** Materials and Methods section "Fluorescence Polarization Assay"
- **Issue** The manuscript does not specify the exact peptide concentrations used in the direct binding experiments beyond stating that the probe peptide concentration is 5 nM. It is unclear whether the peptide concentration was varied or kept constant across experiments, and how the KD values were calculated from the quadratic equation.
- **Required correction** Provide a more detailed description of the experimental setup, including the concentration ranges tested, the number of replicates, and the error analysis. Clarify whether the KD values were determined from at least three independent experiments and how the reported errors were calculated.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Computational modeling results
- **Evidence pointer** Results and Discussion section "YxV Motif Binds to the F3b Binding Site as Evidenced by Docking and Mutagenesis", Figure 4
- **Issue** The manuscript states that threading and global docking of KIRREL3 and TBX4 peptides "failed to yield conclusive results" initially, but does not provide details on what constituted failure or how the extended peptides were chosen. The criteria for convergence and success of the docking simulations are not clearly defined.
- **Required correction** Provide a more detailed description of the computational docking results, including the scoring metrics used, the criteria for identifying successful predictions, and the comparison between different starting structures. This would allow readers to better assess the reliability of the modeling.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction and Discussion
- **Evidence pointer** Introduction, Concluding Remarks
- **Issue** The manuscript does not fully discuss the relationship between the identified SLiM-based interactions and previously characterized FERM domain interactions, particularly those involving the C-terminal autoinhibitory region and known binding partners such as CD44, ICAM-2, and EBP50.
- **Required correction** Expand the discussion to place the findings in the context of existing knowledge about FERM domain interactions, highlighting what is novel and what confirms previous observations. This would strengthen the manuscript's contribution to the field.

## Risk / unsupported claims
- The claim that F3a ligand binding induces conformational changes that allosterically regulate F3b binding is not fully supported by the presented evidence and requires additional biophysical validation.
- The statement that the FERM domain acts as a "switchable interaction hub" is speculative and goes beyond the direct experimental evidence presented.
- The biological relevance of the identified interactions in cellular contexts is not experimentally demonstrated and remains an open question.
- The comparative conclusions about merlin versus ERM specificities are based on a limited number of merlin ligands and may be influenced by technical limitations of the screening approach.
- The claim that the identified ligands provide a "rich resource for exploring the molecular function of the ERM proteins in cell-cell adhesion as well as in transcriptional regulation" is not directly supported by functional experiments.