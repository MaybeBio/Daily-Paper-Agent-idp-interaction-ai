## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methodology, results, discussion, concluding remarks) without figures, tables, or supplementary material
- **Assessment boundary** Computational and in silico analyses only; no experimental validation data
- **Shared manuscript claim summary** The authors propose that intrinsically disordered regions (IDRs) in NLRP1, NLRP3, and NLRP14 act as regulatory hubs for inflammasome condensation and activation, based on computational predictions of disorder, phase separation propensity, protein-protein interactions, and structural analyses
- **Visible evidence base** Text descriptions of computational predictions using DisEMBL, IUPRED, MobiDB, AlphaFold2/3, FuzDrop, InterProSurf, STRING, HDOCK, ClusPro, PremPs; references to figures and tables not directly viewable
- **Missing materials affecting confidence** All figures, tables, supplementary figures, and supplementary tables; specific numerical outputs from prediction tools; docking scores and confidence values beyond stated thresholds; structural alignment details; RMSD values referenced but not fully contextualized

## Reviewer
- **Overall assessment** This manuscript presents a purely computational analysis of IDRs in NLRP family members, proposing a regulatory role in inflammasome assembly. The topic is timely and of potential interest to the inflammasome and phase separation communities. However, the manuscript is entirely hypothesis-generating with no experimental validation, and the computational evidence presented has significant limitations that are not adequately addressed. The claims extend beyond what the in silico data can support, particularly regarding functional roles and disease relevance. The manuscript would benefit from substantial revision to temper claims, address methodological limitations, and provide clearer presentation of the computational results.

- **Who would be interested in the results, and why** Researchers studying inflammasome biology, particularly NLRP1, NLRP3, and NLRP14 activation mechanisms; investigators interested in the role of intrinsically disordered regions and phase separation in immune signaling; computational biologists working on protein structure prediction and disorder analysis; clinicians interested in inflammatory diseases linked to NLRP mutations. The potential connection between IDRs and disease-associated mutations could attract translational researchers.

- **Major strengths**
  1. The manuscript addresses a timely and under-explored question regarding the role of IDRs in NLRP family function and inflammasome assembly
  2. The use of multiple complementary computational tools (disorder predictors, phase separation predictors, docking servers) is methodologically thorough
  3. The authors appropriately acknowledge the hypothesis-generating nature of their work in the concluding remarks
  4. The discussion integrates existing experimental literature with computational predictions, providing context for the proposed model
  5. The focus on NLRP14, a less-studied family member, adds novelty

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The central claim that IDRs in NLRP1, NLRP3, and NLRP14 "act as regulatory hubs for inflammasome condensation and activation" is presented as a finding rather than a hypothesis
- **Evidence pointer** Abstract; Results sections throughout; Concluding remarks
- **Concern** The manuscript presents purely computational predictions as evidence for functional roles. No experimental validation is provided for any of the proposed interactions, phase separation behavior, or functional consequences. The abstract states the authors "uncover a critical role" for IDRs, which overstates what computational analysis alone can establish. The concluding remarks acknowledge this limitation, but the framing throughout the manuscript, including the title and abstract, does not consistently reflect the hypothesis-generating nature of the work.
- **Why it matters** The scientific literature is replete with computational predictions that do not hold up experimentally. Presenting in silico predictions as "uncovering" functional roles without experimental support risks misleading readers and cannot establish the proposed mechanisms. The distinction between prediction and demonstration is fundamental to scientific rigor.
- **Resolution test** The authors must either provide experimental validation (e.g., mutagenesis, biochemical assays, cellular imaging) or substantially reframe the manuscript as a computational hypothesis-generating study with all claims explicitly qualified as predictions requiring experimental testing. The title and abstract must be revised to reflect this framing.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that AlphaFold 2 was selected over AlphaFold 3 because it "more accurately preserved the extended and flexible characteristics expected in IDRs" and that AlphaFold 3 "tended to generate more compact conformations"
- **Evidence pointer** Methodology section, "Prediction of protein structures by AlphaFold"; Supplementary Figure 2
- **Concern** The rationale for preferring AlphaFold 2 over AlphaFold 3 is based on the assumption that AlphaFold 2 predictions of extended conformations are more accurate for IDRs. However, AlphaFold 3 represents a significant advance and the authors' justification relies on the very assumption they are trying to test, namely that these regions are disordered and extended. The comparison between AlphaFold 2 and 3 models is described but the actual data (Supplementary Figure 2) is not available for assessment. The choice of AlphaFold 2 may introduce systematic bias in the structural predictions that underpin subsequent analyses.
- **Why it matters** The entire structural analysis depends on the choice of prediction tool. If the justification for this choice is circular or based on unverified assumptions, the downstream conclusions about IDR structure, interaction surfaces, and mutation effects may be compromised. The field needs clarity on whether AlphaFold 2 genuinely provides more reliable IDR predictions or whether this is a post hoc rationalization.
- **Resolution test** Provide quantitative comparison data between AlphaFold 2 and AlphaFold 3 predictions for these specific proteins, including confidence metrics (pLDDT, PAE) for the IDR regions. Justify the choice based on established benchmarks for IDR prediction rather than expected conformational properties. If AlphaFold 3 predictions are more reliable overall, the analysis should be repeated with those models.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The claim that disease-associated mutations in NLRP1 and NLRP3 occur within the identified IDRs, "underscoring their functional relevance in inflammatory disorders"
- **Evidence pointer** Results section, "Exploring the impact of mutations in IDRs of NLRPs on protein stability and interaction"; Table 2; Figure 6
- **Concern** The manuscript reports that mutations associated with diseases fall within IDRs and that some affect predicted stability, but the analysis appears limited to computational predictions of stability changes (PremPs) and docking. The claim that this "underscores functional relevance" is a logical leap. Many disease-associated mutations occur throughout proteins, and their presence in IDRs does not establish that the IDR itself is functionally important for the disease mechanism. The mutations could affect protein stability, folding, or interactions through mechanisms unrelated to IDR-specific functions.
- **Why it matters** The disease relevance framing is a key selling point of the manuscript. If the connection between IDR location and disease mechanism is not established, this aspect of the manuscript is overstated. The clinical significance implied by the abstract and introduction requires stronger evidence than co-localization of mutations with predicted disordered regions.
- **Resolution test** Provide a more nuanced analysis of how each mutation might affect IDR function specifically (e.g., changes in phase separation propensity, phosphorylation site disruption, altered interaction motifs). If experimental data on these mutations exist in the literature, incorporate it. Alternatively, temper the claims to state that mutations occur within predicted IDRs, and that the functional consequences require experimental investigation.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The claim that molecular docking predictions with HDOCK (and validation with ClusPro) demonstrate interactions between NLRP IDRs and partner proteins (ASC, TXNIP, TBK1, NEK7)
- **Evidence pointer** Results sections for NLRP1, NLRP3, and NLRP14; Figures 5 and 7; Supplementary Figures 3, 4, 5, 7, 8, 10
- **Concern** The docking analysis uses predicted structures from AlphaFold 2, which may not accurately represent the conformational ensemble of IDRs. Docking of intrinsically disordered regions is particularly challenging because these regions sample multiple conformations, and docking tools typically assume relatively rigid structures. The high RMSD values reported (56-122 Å) for some predicted complexes suggest poor structural convergence and may indicate unreliable predictions. The authors acknowledge this for some cases but proceed to draw conclusions from these results.
- **Why it matters** The proposed interaction networks and the functional model depend critically on the docking predictions. If the docking results are unreliable due to the inherent challenges of docking disordered regions, the entire interaction model is called into question. The high RMSD values suggest the predictions may not be physically meaningful.
- **Resolution test** Provide a more rigorous assessment of docking reliability, including comparison with known experimental structures or complexes where available, analysis of the interface residues in the context of the IDR conformational ensemble, and discussion of the limitations of docking IDRs. Consider using ensemble docking approaches or molecular dynamics simulations to account for IDR flexibility.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The claim that this work provides "a new framework for understanding the regulation of inflammasomes" and that targeting "the dynamics of phase transitions could open novel therapeutic avenues"
- **Evidence pointer** Abstract; Concluding remarks
- **Concern** While the idea that IDRs in NLRPs may contribute to phase separation and inflammasome assembly is interesting, the manuscript does not provide direct evidence for phase separation of these proteins or demonstrate that the proposed mechanism operates in cells. The connection between computational predictions of phase separation propensity and actual cellular behavior is not established. The therapeutic implications are speculative and not supported by any data in the manuscript.
- **Why it matters** The claimed novelty and significance of the work rest on the phase separation model. Without experimental evidence for phase separation of NLRP proteins or functional consequences of disrupting IDR-mediated interactions, the framework remains entirely speculative. The therapeutic claims are premature and could mislead readers about the translational potential.
- **Resolution test** Either provide experimental evidence for phase separation (e.g., in vitro droplet formation assays, cellular imaging of condensates) or substantially revise the claims to clearly state that the phase separation model is a hypothesis generated from computational predictions that requires experimental testing. Remove or significantly temper the therapeutic implications.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and presentation
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states the authors "uncover a critical role" for IDRs, which overstates the nature of the evidence. The abstract should reflect that this is a computational analysis generating hypotheses.
- **Required correction** Revise the abstract to use language such as "we identify predicted IDRs" or "our computational analysis suggests" rather than "we uncover a critical role."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methodology, "Determination of liquid-liquid phase separation propensity index"
- **Evidence pointer** Methodology section
- **Concern** The threshold for pLLPS (≥0.60) is stated, but the rationale for this threshold and the limitations of FuzDrop predictions are not discussed. The relationship between predicted phase separation propensity and actual cellular phase separation behavior is not addressed.
- **Required correction** Add a brief discussion of the limitations of computational phase separation prediction and the relationship between predicted propensity and experimental observations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results and discussion, NLRP1 section
- **Evidence pointer** Results section, NLRP1 subsection
- **Concern** The discussion of NLRP1 IDRs and their potential role in activation is somewhat disjointed, moving between different interaction partners and functional contexts without a clear logical flow.
- **Required correction** Restructure the NLRP1 section to present a clearer narrative, perhaps organized by the proposed functional stages of NLRP1 activation.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity and presentation
- **Affected element** Results and discussion, NLRP3 section
- **Evidence pointer** Results section, NLRP3 subsection
- **Concern** The discussion of NLRP3 regulation is dense and covers many potential interaction partners and post-translational modifications. The connection between the computational predictions and the proposed regulatory model could be clearer.
- **Required correction** Consider adding a summary figure or table that integrates the proposed interactions and modifications into a coherent model of NLRP3 regulation.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methodology, "Molecular docking"
- **Evidence pointer** Methodology section
- **Concern** The docking methodology description is brief. Details on the preparation of structures, definition of binding sites, number of docking runs, and selection criteria for final models are not provided.
- **Required correction** Expand the methodology to include sufficient detail for reproducibility, including specific parameters used in HDOCK and ClusPro.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results and discussion, NLRP14 section
- **Evidence pointer** Results section, NLRP14 subsection
- **Concern** The NLRP14 section is relatively brief compared to NLRP1 and NLRP3, and the functional implications of the IDR in fertilization are not fully developed.
- **Required correction** Expand the discussion of how the predicted IDR in NLRP14 might contribute to its role in fertilization and how this relates to the broader theme of the manuscript.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Clarity and presentation
- **Affected element** Concluding remarks
- **Evidence pointer** Concluding remarks
- **Concern** The concluding remarks appropriately acknowledge the hypothesis-generating nature of the work, but this acknowledgment comes after the results have been presented with more definitive language. The transition could be smoother.
- **Required correction** Consider adding a brief statement at the beginning of the results section noting that all findings are computational predictions requiring experimental validation.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results and discussion, "Phosphorylation at the IDRs" section
- **Evidence pointer** Results section, phosphorylation subsection; Supplementary Figure 9
- **Concern** The claim that phosphorylation at Thr659 in NLRP3 "promoted the formation of an α-helix within IDR3" is based on AlphaFold 3 predictions. The reliability of AlphaFold 3 for predicting conformational changes upon phosphorylation is not established, and the authors previously argued that AlphaFold 3 produces artifacts in IDRs.
- **Required correction** Acknowledge the limitation that AlphaFold 3 may not reliably predict phosphorylation-induced conformational changes in IDRs, and consider whether the analysis should be repeated with alternative methods or interpreted with greater caution.

- **Concern ID** R1-m9
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results and discussion, "Exploring the impact of mutations" section
- **Evidence pointer** Results section, mutations subsection; Table 2
- **Concern** The analysis of disease-associated mutations is limited to a small number of variants. A more comprehensive analysis of all known disease-associated mutations in NLRP1, NLRP3, and NLRP14 and their positions relative to predicted IDRs would strengthen the claims.
- **Required correction** Consider expanding the analysis to include a broader set of mutations and provide a statistical assessment of whether disease-associated mutations are enriched in IDRs compared to structured regions.

- **Concern ID** R1-m10
- **Severity** Minor
- **Axis** Clarity and presentation
- **Affected element** Results and discussion, "The DDX3X protein" section
- **Evidence pointer** Results section, DDX3X subsection; Figure 7
- **Concern** The DDX3X analysis appears somewhat tangential to the main focus of the manuscript. The connection between DDX3X interactions and the proposed IDR-mediated regulatory mechanism could be made more explicit.
- **Required correction** Clarify how the DDX3X interaction data supports the overall model of IDR-mediated regulation of NLRP3, or consider moving this analysis to supplementary material.

## Risk / unsupported claims
- The claim that IDRs in NLRP1, NLRP3, and NLRP14 "act as regulatory hubs for inflammasome condensation and activation" is unsupported by experimental evidence and overstates what computational predictions can establish
- The claim that disease-associated mutations within IDRs "underscore their functional relevance" is a logical leap from co-localization to functional significance
- The claim that phosphorylation at specific residues induces conformational changes in IDRs is based on AlphaFold 3 predictions, whose reliability for this purpose is not established
- The proposed model of IDR-mediated phase separation driving inflammasome condensation at the perinuclear membrane is entirely speculative with no direct experimental support
- The therapeutic implications suggested in the abstract and concluding remarks are premature and unsupported by the data presented
- The selection of AlphaFold 2 over AlphaFold 3 is justified on grounds that may introduce bias and is not adequately validated
- The docking predictions with high RMSD values (56-122 Å) are presented as meaningful despite these values suggesting poor structural convergence
- The claim that NLRP14 IDR mediates interactions with TBK1 relevant to fertilization is based solely on computational predictions without experimental validation