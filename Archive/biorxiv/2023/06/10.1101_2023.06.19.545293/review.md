## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods, supplementary figure legends) as provided in the submission
- **Assessment boundary** Scientific content, structural biology validity, biochemical and cellular evidence, claims versus data, and suitability for a high-impact general audience
- **Shared manuscript claim summary** The authors report crystal structures of the bacterial effector SAP05 in complex with the ZnF domain of the plant transcription factor SPL5 and with the vWA domain of the proteasomal receptor Rpn10. They propose a bimodular architecture with two distinct binding surfaces, validate key residues by mutagenesis and degradation assays, and suggest a mechanism for ubiquitin-independent targeted protein degradation via the 26S proteasome.
- **Visible evidence base** Crystal structures at 2.20 Å and 2.17 Å resolution, ITC binding data, yeast two-hybrid assays, in planta degradation assays, AlphaFold-Multimer predictions, sequence conservation analyses, structural superposition onto the spinach 26S proteasome
- **Missing materials affecting confidence** Table 1 (crystallographic statistics) not provided; Supplementary Figures 1-12 not provided; full experimental details for mutagenesis and degradation assays are abbreviated; no negative control data for degradation assays shown in the text; no quantitative degradation data (e.g., immunoblot quantification) provided

## Reviewer
- **Overall assessment** This manuscript presents a structurally and functionally compelling analysis of how a small bacterial effector protein achieves ubiquitin-independent targeted protein degradation. The bimodular architecture is clearly supported by the two crystal structures, and the mutagenesis data provide reasonable validation of the interaction surfaces. The work is of interest to the structural biology, plant-microbe interactions, and protein degradation communities. However, several technical concerns and missing data limit the strength of the mechanistic claims, particularly regarding the proposed degradation mechanism and the generalizability of the findings. The manuscript would benefit from additional functional data and clearer presentation of the structural validation.

- **Who would be interested in the results, and why** Structural biologists studying effector proteins and protein-protein interactions; plant pathologists interested in phytoplasma virulence mechanisms; researchers in the targeted protein degradation field, particularly those developing new degradation tools; and synthetic biologists seeking new molecular tools for protein depletion. The demonstration of a small protein that bridges a proteasome receptor to transcription factors via two independent surfaces has direct implications for designing novel degraders.

- **Major strengths** 1) The two crystal structures are determined at good resolution and reveal a clear bimodular architecture with spatially separated binding surfaces. 2) The combination of structural, biophysical (ITC), and cellular (degradation assays) data provides multi-layered validation. 3) The identification of specific residues mediating SPL versus GATA specificity, particularly the role of D66, is a notable advance. 4) The structural superposition onto the 26S proteasome provides a plausible mechanistic framework. 5) The potential application as a new class of E3-independent degraders is timely and significant.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that the SAP05-ZnF interaction is "dominated by electrostatic interactions" and that specific residues (D66, N77, D106) are required for SPL binding, with D66 also required for GATA binding.
- **Evidence pointer** Results section "The SAP05 'loop surface' forms electrostatic interactions with the ZnF domain"; Figure 2; Supplementary Figures 2-5
- **Concern** The mutagenesis data are presented qualitatively. The degradation assays in N. benthamiana are described as "failed to degrade" or "retained the ability to degrade," but no quantitative data (e.g., immunoblot band intensities, replicate numbers, statistical analysis) are provided. The claim that D66 is essential for both SPL and GATA binding relies on a single mutant (D66A) in a single assay system. The AlphaFold-Multimer model for the SAP05-GATA19 interaction is used to support the role of D66, but the model is not experimentally validated beyond the D66A mutant. The authors should provide quantitative degradation data with appropriate replicates and statistical analysis, and ideally test additional mutants at the D66 position (e.g., D66E, D66N) to distinguish charge effects from steric effects.
- **Why it matters** The specificity determinants of SAP05 for SPL versus GATA transcription factors are a central claim of the manuscript. Without quantitative data, the reader cannot assess the robustness of the phenotype or the relative contribution of individual residues. The distinction between loss of binding and loss of degradation is also not clearly established.
- **Resolution test** Provide quantitative immunoblot data with at least three biological replicates for each mutant, including statistical analysis. Include additional D66 mutants to establish the chemical basis of the interaction. Show that the D66A mutant retains proper folding (e.g., by circular dichroism or a control interaction).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "SAP05 binding to vWA is more stable due to the necessity of multiple mutations to break the interaction" and that the SAP05-vWA interface is "largely mediated by polar forces."
- **Evidence pointer** Results section "The SAP05 'sheet surface' forms polar interactions with vWA_Rpn10"; Figure 3; Supplementary Figures 6, 10
- **Concern** The claim that the vWA interaction is "more stable" is not supported by any quantitative binding data. The ITC experiments were only performed for the SAP05-ZnF interaction, not for the SAP05-vWA interaction. The authors state that vWA could not be purified alone due to aggregation, but this limitation is not addressed with alternative approaches (e.g., surface plasmon resonance with a stabilized vWA construct, or competition assays). The conclusion that multiple mutations are needed to disrupt the interaction is based on a limited set of double and triple mutants, and the degradation data for these mutants are again qualitative. The structural basis for the "stability" claim is not quantified (e.g., buried surface area, number of hydrogen bonds).
- **Why it matters** The relative stability of the two interfaces is used to support the bimodular architecture and the proposed mechanism. Without quantitative binding data, the claim of differential stability is speculative. This is important for understanding how SAP05 can simultaneously engage both partners and for designing engineered variants.
- **Resolution test** Provide quantitative binding data for the SAP05-vWA interaction using an alternative method (e.g., MST, SPR, or ITC with a stabilized vWA construct). Alternatively, provide a quantitative measure of interaction stability from the crystal structures (e.g., buried surface area, solvation free energy gain) and correlate with the mutagenesis data.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors propose that "positioning of the SAP05 complex on the 26S proteasome points to a mechanism of protein degradation" and that the interaction of SPL5 with the Rpt4/Rpt5 coiled-coil domains "may be involved in substrate degradation."
- **Evidence pointer** Results section "Positioning of SAP05 complex on the 26S proteasome points to a TPD mechanism"; Figure 5; Supplementary Figures 11-12
- **Concern** The mechanistic model is based solely on a structural superposition of the SAP05-vWA complex onto the spinach 26S proteasome cryo-EM structure. No experimental validation of this model is provided. The authors do not test whether mutations in the Rpt4/Rpt5 coiled-coil domains affect SAP05-mediated degradation, nor do they provide any biochemical evidence for the proposed conformational switch. The claim that the ternary complex "clashes" with the Rpt4/Rpt5 CC domains is presented as evidence for a mechanism, but this is speculative.
- **Why it matters** The proposed mechanism is a key advance of the manuscript and has implications for understanding how SAP05 bypasses the canonical ubiquitin pathway. Without experimental support, the mechanism remains a hypothesis. This is particularly important given the authors' suggestion that SAP05 could be engineered for therapeutic applications.
- **Resolution test** Provide experimental evidence for the proposed mechanism, such as: (1) mutagenesis of the Rpt4/Rpt5 CC domains and testing the effect on SAP05-mediated degradation; (2) crosslinking or pull-down experiments showing the ternary complex on the proteasome; (3) single-particle cryo-EM of the SAP05-vWA complex bound to the 26S proteasome; or (4) in vitro degradation assays with purified components.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "SAP05 did not show any significant structural similarity to experimentally determined structures in the PDB, suggesting a novel architecture."
- **Evidence pointer** Results section "Crystal structures of the SAP05-ZnF_SPL5 and SAP05-vWA_Rpn10 complexes"; Discussion
- **Concern** The claim of structural novelty is based on a statement without supporting data. No DALI or other structural similarity search results are presented. The authors should provide quantitative measures of structural similarity (e.g., Z-scores from DALI) to support the claim of novelty. Additionally, the statement that the architecture is "previously unknown" is strong and should be supported by a thorough comparison with known protein structures.
- **Why it matters** The novelty of the SAP05 architecture is a central claim of the manuscript and is used to support the significance of the work. Without quantitative structural comparison data, the claim is not verifiable.
- **Resolution test** Provide DALI or equivalent structural similarity search results, including Z-scores and RMSD values for the top hits. Discuss the significance of any similarities found.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract; Introduction
- **Issue** The abstract and introduction assume significant familiarity with the ubiquitin-proteasome system and bacterial effector biology. Terms such as "vWA domain," "ZnF domain," and "ubiquitin-independent TPD" are used without brief explanations. The significance of bypassing the canonical UPS pathway could be made clearer for a general audience.
- **Required correction** Add brief explanations of key terms and a sentence explaining why ubiquitin-independent degradation is significant (e.g., potential for orthogonal degradation tools).

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** ITC data presentation
- **Evidence pointer** Results section "The SAP05 'loop surface' forms electrostatic interactions with the ZnF domain"; Figure 2C; Supplementary Figure 3
- **Issue** The ITC data are described as showing a Kd of 0.45 ± 0.06 µM, but the number of replicates, the fitting model, and the raw thermogram are not described in the text. The stoichiometry is stated as 1:1, but the fitting parameters (e.g., ΔH, ΔS) are not provided.
- **Required correction** Provide the full ITC fitting parameters, the number of replicates, and a representative raw thermogram with integrated heats in the supplementary material.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Mutagenesis rationale
- **Evidence pointer** Results section "The SAP05 'loop surface' forms electrostatic interactions with the ZnF domain"; Supplementary Figure 2
- **Issue** The choice of mutations (e.g., D66A, N77R, D106A/R) is not fully justified. For example, why was D66 mutated to alanine rather than a conservative substitution? The authors state that residues were replaced with "neutral, similarly charged, or oppositely charged residue," but the specific rationale for each mutation is not provided.
- **Required correction** Provide a brief rationale for each mutation, including the expected effect based on the structural data.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Discussion
- **Evidence pointer** Discussion
- **Issue** The discussion of therapeutic applications is brief and somewhat speculative. The authors mention PROTACs and the potential for SAP05-based degraders, but do not discuss the challenges of adapting a bacterial effector for therapeutic use (e.g., immunogenicity, delivery, specificity).
- **Required correction** Expand the discussion of therapeutic applications to include potential challenges and how they might be addressed.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Conservation analysis
- **Evidence pointer** Results section "Conservation analyses of SAP05 residues"; Supplementary Figures 7-8
- **Issue** The conservation analysis is described qualitatively. The authors state that residues are "conserved among all or most SAP05 homologs," but no sequence identity/similarity percentages or statistical measures are provided. The swapping experiments are described, but the number of replicates and the quantitative readout are not specified.
- **Required correction** Provide quantitative measures of sequence conservation and include replicate numbers and statistical analysis for the swapping experiments.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Structural validation
- **Evidence pointer** Results section "Crystal structures of the SAP05-ZnF_SPL5 and SAP05-vWA_Rpn10 complexes"; Table 1
- **Issue** The crystallographic statistics are not provided in the manuscript text (Table 1 is referenced but not included in the provided material). The authors should ensure that the table includes Rfree, RMSD bonds/angles, Ramachandran statistics, and B-factor information.
- **Required correction** Ensure Table 1 includes all standard crystallographic validation metrics and is accessible to reviewers.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Interdisciplinary readership
- **Affected element** Methods
- **Evidence pointer** Materials and Methods
- **Issue** The methods section is written for structural biology specialists. Terms such as "single-wavelength anomalous diffraction," "molecular replacement," and "AlphaFold-Multimer" are used without brief explanations. This may limit accessibility for readers from other disciplines.
- **Required correction** Add brief explanations of key structural biology methods for non-specialist readers.

- **Technical failings that need to be addressed before the case is established** 1) Quantitative degradation data with replicates and statistics are missing (R1-M1). 2) Quantitative binding data for the SAP05-vWA interaction are absent (R1-M2). 3) The proposed degradation mechanism lacks experimental validation (R1-M3). 4) Structural novelty claim lacks quantitative support (R1-M4).

- **Assessment against Nature-style criteria** 
  - Originality: The bimodular architecture of SAP05 is novel and the structural data are original. The finding that a single small effector uses two distinct surfaces to bridge a proteasome receptor and transcription factors is a new concept. However, the overall concept of effectors hijacking the proteasome is not entirely new, and the mechanistic model requires additional validation.
  - Scientific importance: The work is important for understanding phytoplasma virulence mechanisms and for the protein degradation field. The potential for engineering SAP05-based degraders is significant. However, the importance is somewhat limited by the lack of functional validation of the proposed mechanism.
  - Interdisciplinary readership: The work will appeal to structural biologists, plant pathologists, and researchers in targeted protein degradation. The therapeutic implications may attract a broader audience, but the manuscript is currently written primarily for specialists.
  - Technical soundness: The structural determination appears sound, but the functional data are incomplete. The lack of quantitative binding and degradation data weakens the technical case.
  - Readability for nonspecialists: The manuscript is not easily accessible to non-specialists. The abstract and introduction assume significant background knowledge, and the methods are written for structural biology experts.

- **Recommendation posture** Supportive if technical concerns are resolved. The structural data are valuable and the bimodular architecture is a significant finding. However, the manuscript currently lacks the quantitative functional data needed to fully support the mechanistic claims. The authors should address the major concerns regarding quantitative degradation and binding data, and provide experimental validation of the proposed degradation mechanism. If these concerns are addressed, the manuscript would be suitable for a high-impact journal.

## Risk / unsupported claims
- The claim that SAP05 binding to vWA is "more stable" than binding to ZnF is unsupported by quantitative data.
- The proposed degradation mechanism involving Rpt4/Rpt5 coiled-coil domain interactions is speculative and not experimentally validated.
- The claim of structural novelty ("previously unknown molecular architecture") is not supported by quantitative structural comparison data.
- The statement that SAP05 "bypasses the canonical UPS cellular proteolysis pathway" is supported by prior work but the mechanistic details presented here are incomplete.
- The generalizability of the findings to all SAP05 homologs is not fully established, as the conservation analysis is qualitative.
- The therapeutic potential of SAP05-based degraders is discussed without addressing potential limitations or providing proof-of-concept data.