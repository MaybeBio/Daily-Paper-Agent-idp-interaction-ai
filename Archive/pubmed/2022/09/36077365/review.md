## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, materials and methods, and conclusions. Supplementary materials referenced but not provided.
- **Assessment boundary** Scientific content, technical soundness, structural biology claims, biochemical functional data, and consistency of interpretation. Not assessed: language editing, formatting, or journal fit beyond general Nature-style criteria.
- **Shared manuscript claim summary** The authors report the discovery and characterization of an unusually large, single-heme cytochrome c552 (CytC552) from Thioalkalivibrio paradoxus, which copurifies with thiocyanate dehydrogenase (TcDH). They present the solution NMR structure of CytC552, demonstrate its function as an electron acceptor for TcDH in vitro, map the interaction interface via NMR chemical shift perturbations, and model the TcDH-CytC552 complex to propose an electron transfer pathway involving His528 and Tyr164 of TcDH and His83 of CytC552.
- **Visible evidence base** Full text with figures referenced (Figures 1-9), tables referenced (Tables S1-S3 in supplementary), NMR structural statistics summarized in Table S3, ITC data in Figure 1E, activity assays in Figure 1D, NMR spectra and CSP data in Figures 2, 4, 6-8, SAXS data in Figure 5, and docking results in Figures 8-9. Supplementary figures and tables not directly inspected.
- **Missing materials affecting confidence** Supplementary figures (S1-S7) and tables (S1-S3) referenced but not provided. PDB and BMRB accession codes cited (7O9U and 34618) but not independently verified. Raw NMR restraint lists, structural statistics tables, and complete CSP datasets not available for direct assessment. Details of HADDOCK protocol parameters and Pathways calculations only partially described.

## Reviewer
- **Overall assessment** This manuscript presents a structurally and functionally interesting cytochrome c552 with unusual features, including disordered histidine-rich termini and a highly solvent-exposed heme. The work combines NMR structure determination, biochemical activity assays, ITC binding measurements, and computational docking to propose a biologically plausible electron transfer complex with TcDH. The study is technically competent in its core NMR methodology, and the finding that CytC552 serves as a functional electron acceptor for TcDH is a meaningful advance for understanding thiocyanate metabolism in this organism. However, several concerns limit the strength of the conclusions. The evidence for the physiological relevance of the TcDH-CytC552 interaction is indirect, the structural basis for the proposed electron transfer pathway relies on a single computational model without experimental validation, and the functional significance of the disordered termini remains speculative. The manuscript would benefit from additional experimental support, particularly mutagenesis of key proposed residues and more quantitative analysis of the interaction dynamics.
- **Who would be interested in the results, and why** Researchers studying bacterial electron transfer chains, particularly in sulfur-oxidizing and chemolithoautotrophic bacteria, will find the identification of a native electron acceptor for TcDH valuable. Structural biologists interested in cytochrome c diversity and the role of disordered regions in protein-protein interactions will also be engaged. The work may also appeal to those studying transient protein complexes and electron transfer mechanisms in periplasmic systems, as well as investigators working on thiocyanate bioremediation who seek a molecular understanding of the degradation pathway.
- **Major strengths** The NMR structure determination appears carefully executed with appropriate validation. The discovery that CytC552 copurifies with TcDH and is encoded in the genomes of all TcDH-containing Thioalkalivibrio strains provides a strong genomic and biochemical link. The functional demonstration that CytC552 supports TcDH activity at levels comparable to artificial electron acceptors is a key result. The observation of heme axial methionine fluxionality is novel and well-supported by the NMR data. The integration of multiple biophysical techniques (NMR, SAXS, ITC, activity assays) strengthens the overall case.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (physiological relevance not established), R1-M2 (electron transfer pathway model not validated), R1-M3 (disordered region functional role unresolved), R1-M4 (pH-dependent activity interpretation incomplete).
- **Assessment against Nature-style criteria** Originality: The finding of a large cytochrome c with disordered histidine-rich termini and axial methionine fluxionality is novel and adds to the diversity of known cytochrome c structures. The identification of a putative native electron transfer partner for TcDH is an original contribution. Scientific importance: The work advances understanding of thiocyanate oxidation in an environmentally relevant organism and provides a foundation for studying this electron transfer chain. However, the broader significance beyond this specific system is not fully articulated. Interdisciplinary readership: The topic bridges structural biology, microbiology, and bioenergetics, and the findings could interest readers across these fields, though the presentation is somewhat specialized. Technical soundness: The NMR methodology is sound, and the biochemical assays are appropriate. However, the computational docking and electron transfer pathway predictions are not experimentally validated, which weakens the technical case. Readability for nonspecialists: The manuscript is clearly written but assumes familiarity with NMR spectroscopy and electron transfer theory; some concepts could be better explained for a broader audience.
- **Recommendation posture** Supportive if technical concerns are resolved. The core findings are potentially significant, but the physiological relevance of the interaction, the validity of the proposed electron transfer pathway, and the functional role of the disordered termini require additional experimental support or more cautious interpretation before the case is fully established.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Functional validation
- **Claim pointer** The authors claim that CytC552 is the putative physiological electron acceptor for TcDH based on copurification, genomic co-occurrence, and in vitro activity.
- **Evidence pointer** Section 2.1, Figures 1D-E, Table S1
- **Concern** The evidence that CytC552 is the physiological electron acceptor is circumstantial. Copurification could reflect nonspecific association or shared subcellular localization rather than a specific functional partnership. The genomic co-occurrence is suggestive but does not demonstrate a direct electron transfer relationship. The in vitro activity assay shows that CytC552 can serve as an electron acceptor, but this does not establish that it is the native partner in vivo. No genetic experiments (e.g., knockout or knockdown of cytC552 in T. paradoxus) or direct measurements of electron transfer kinetics between TcDH and CytC552 are provided.
- **Why it matters** The central claim of the manuscript is that CytC552 is the physiological electron acceptor for TcDH. Without direct evidence of in vivo relevance, the functional significance of the interaction remains uncertain. The authors themselves note that the complex is transient and low-affinity, which makes the physiological relevance even more important to establish.
- **Resolution test** Provide genetic evidence (e.g., deletion or knockdown of cytC552 in T. paradoxus and assessment of thiocyanate-dependent growth or TcDH activity), or direct kinetic measurements of electron transfer between TcDH and CytC552 (e.g., stopped-flow or photochemical reduction assays) that demonstrate specificity and physiological rates. Alternatively, clearly reframe the claim as demonstrating a potential in vitro electron transfer partner without asserting physiological relevance.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Computational model validation
- **Claim pointer** The authors propose a specific electron transfer pathway from the Cu2 ion of TcDH through His528 and Tyr164 of TcDH and His83 of CytC552 to the heme group, based on HADDOCK docking and Pathways calculations.
- **Evidence pointer** Section 2.5, Figures 8-9
- **Concern** The proposed electron transfer pathway is derived entirely from computational modeling without experimental validation. The HADDOCK docking uses NMR CSP data as restraints, which is reasonable, but the final model selection is based on the Pathways-calculated electronic coupling, creating a circular logic: the model is chosen for having a good pathway, and then the pathway is presented as a finding. No mutagenesis of the proposed key residues (His528, Tyr164 of TcDH; His83 of CytC552) is performed to test the predicted pathway. The authors also note that the HADDOCK score and the best pathway do not correspond to the same complex, which raises questions about model selection criteria.
- **Why it matters** The proposed electron transfer pathway is a major conclusion of the manuscript. Without experimental validation, the specific pathway remains speculative. The circularity in model selection undermines the strength of the claim. If the pathway is incorrect, the interpretation of the pH-dependent activity shoulder attributed to His83 protonation would also be called into question.
- **Resolution test** Perform site-directed mutagenesis of His528, Tyr164 in TcDH and His83 in CytC552, followed by activity assays and binding measurements to test whether these residues are essential for electron transfer. Alternatively, provide independent experimental evidence for the complex geometry, such as cross-linking mass spectrometry or paramagnetic NMR restraints, that supports the modeled interface.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Structural characterization completeness
- **Claim pointer** The authors describe the N- and C-terminal regions of CytC552 as intrinsically disordered and suggest they may play a role in interaction with TcDH.
- **Evidence pointer** Section 2.2, Figures 3-4
- **Concern** The disordered nature of the termini is inferred from the absence of NOE restraints and low local correlation times, which is reasonable. However, the functional significance of these regions is not experimentally addressed. The authors speculate that the disordered termini may facilitate interaction with TcDH through nonspecific contacts, but no experiments are performed to test this hypothesis. The truncation of these regions for docking is justified for technical reasons, but this also removes the very elements that might be functionally important.
- **Why it matters** The unusual disordered termini are a distinctive feature of this cytochrome and a potential source of novel functional insight. Leaving their role entirely speculative is a missed opportunity and weakens the structural-functional narrative of the manuscript.
- **Resolution test** Construct and characterize truncated variants of CytC552 lacking the N- and C-terminal extensions, and test their ability to interact with and transfer electrons to TcDH. This would directly address whether the disordered regions are required for complex formation or electron transfer.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Data interpretation
- **Claim pointer** The authors attribute the small shoulder in the acidic part of the pH-dependence curve of TcDH activity with CytC552 to protonation of His83 in CytC552.
- **Evidence pointer** Section 2.1, Figure 1D, Section 2.5
- **Concern** The interpretation of the pH-dependent activity shoulder is speculative. The pKa of 6.7 is close to that of histidine, but the shoulder could also arise from protonation of other residues in either protein, changes in protein stability, or altered binding affinity. The authors do not provide direct evidence that His83 protonation is responsible, such as pH-dependent binding measurements or mutagenesis of His83. The connection between the pH-dependent activity and the proposed electron transfer pathway is also not quantitatively established.
- **Why it matters** The pH-dependent activity data are used to support the functional relevance of the proposed electron transfer pathway. If the interpretation is incorrect, this supporting evidence is weakened. A more rigorous analysis would strengthen the manuscript.
- **Resolution test** Measure the pH dependence of TcDH activity with CytC552 variants lacking His83 (e.g., H83A) to test whether the shoulder disappears. Alternatively, perform pH-dependent ITC or NMR titrations to directly measure the effect of pH on binding affinity and correlate with the activity data.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 1D
- **Evidence pointer** Section 2.1, Figure 1D
- **Issue** The pH-dependence curves for TcDH activity with different electron acceptors are presented in a single panel, but the data for CytC552, hhCytC550, and ferricyanide are not clearly distinguished in the figure legend. The shoulder in the CytC552 curve is described but not highlighted or annotated in the figure.
- **Required correction** Clearly label each curve in Figure 1D and add an annotation or inset highlighting the shoulder in the CytC552 curve. Expand the figure legend to describe the conditions and the significance of the shoulder.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodology clarity
- **Affected element** Section 3.9
- **Evidence pointer** Section 3.9
- **Issue** The description of the HADDOCK docking protocol is brief. The authors state that "active ambiguous interaction restraints" were used but do not specify how many restraints, how they were derived from the CSP data, or what cutoff was used to define "active" residues. The criteria for selecting the final model from the 600 generated structures are also not fully described.
- **Required correction** Provide more detail on the generation of AIRs from CSP data, including the specific residues used and the distance cutoffs. Describe the scoring function and selection criteria for the final model, including how the Pathways results were integrated into the selection.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data completeness
- **Affected element** Table S3
- **Evidence pointer** Section 2.2, Table S3
- **Issue** The structural statistics for the NMR ensemble are only presented in the supplementary material. Key parameters such as the number of NOE restraints per residue, RMSD values for the structured core, and Ramachandran plot statistics are not summarized in the main text.
- **Required correction** Include a brief summary of the key structural statistics in the main text or in a main-text table, so that readers can assess the quality of the NMR structure without consulting the supplementary material.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation caution
- **Affected element** Section 2.5, Figure 9F
- **Evidence pointer** Section 2.5, Figure 9F
- **Issue** The proposed role of Trp24 and Arg95 in modulating the electron transfer through electrostatic interactions is highly speculative. The authors present this as a plausible mechanism without direct experimental support or detailed computational analysis (e.g., electrostatic calculations or molecular dynamics simulations).
- **Required correction** Soften the language when describing the proposed role of Trp24 and Arg95, or provide additional computational analysis to support the electrostatic argument. Clearly distinguish between established findings and speculative mechanistic proposals.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Section 1, Introduction
- **Evidence pointer** Section 1
- **Issue** The introduction mentions that hhCytC550 and low-molecular-weight mediators were used as artificial electron acceptors in previous studies, but does not discuss the physiological electron transfer chain of T. paradoxus in broader context. The relationship between CytC552 and other periplasmic electron carriers (e.g., cytochromes c4, c5, or copper proteins) is not addressed.
- **Required correction** Add a brief discussion of the known or predicted periplasmic electron transfer components in Thioalkalivibrio species to better contextualize the potential role of CytC552.

## Risk / unsupported claims
- The claim that CytC552 is the physiological electron acceptor for TcDH is not fully supported by the evidence presented. Copurification, genomic co-occurrence, and in vitro activity are suggestive but not conclusive.
- The specific electron transfer pathway involving His528, Tyr164 of TcDH and His83 of CytC552 is based solely on computational modeling without experimental validation and should be presented as a hypothesis rather than a finding.
- The attribution of the pH-dependent activity shoulder to His83 protonation is speculative and not directly tested.
- The proposed role of Trp24 and Arg95 in regulating electron transfer directionality is not supported by direct evidence or detailed computational analysis.
- The functional significance of the disordered N- and C-terminal regions is not experimentally addressed and remains speculative.
- The claim that the CytC552 structure is "unusual" compared to other large cytochromes c is based on limited structural comparison; a more systematic analysis of structural homologs would strengthen this claim.
- The statement that the electron transfer complex is "transient" and involves an "intermediate state" is inferred from NMR line broadening and is not directly measured.