## Review setup
- **Input scope** Full manuscript text (abstract, introduction, materials and methods, results, discussion, acknowledgements)
- **Assessment boundary** Scientific content and technical soundness of the claims as presented in the preprint; no assessment of editorial fit for a specific journal
- **Shared manuscript claim summary** The authors propose a bipartite mechanism for tension-dependent recruitment of LATS1/2 to adherens junctions (AJs) by LIMD1, involving the first two LIM domains binding a conserved linear motif ("LATS-LATCH") in LATS1/2, plus an N-terminal intrinsically disordered region (IDR) required for LATS1 AJ localization. The LATS-LATCH is reported as necessary and sufficient for strain-dependent recruitment.
- **Visible evidence base** Domain mapping via co-immunoprecipitation (Figure 1A–B), localization assays in LIMD1-KO MCF10A cells (Figures 1C–D, 2B–C, 3A–B, 4A, 5B–C), binding assays with LIM domain point mutants (Figure 3C), AlphaFold 2/3 modeling (Figure 4B), deletion and point mutation analysis of the LATS-LATCH (Figures 4D, 5A–B)
- **Missing materials affecting confidence** No representative Western blot images or quantification details for co-immunoprecipitation experiments; no statistical details for localization quantifications; no raw AlphaFold model confidence metrics (pLDDT, PAE) provided; no negative control data for localization assays (e.g., untransfected or GFP-only cells); no data for LATS2 endogenous localization (authors note LATS2 detection difficulty); no data on whether IDR deletion affects LIMD1 protein stability or expression levels

## Reviewer
- **Overall assessment** This manuscript addresses a significant open question in Hippo signaling: how mechanical tension at adherens junctions triggers LATS1/2 recruitment via LIMD1. The identification of a conserved linear motif (LATS-LATCH) in LATS1/2 that binds LIMD1 LIM domains is a potentially valuable contribution. The combination of AlphaFold modeling with biochemical and cell-based validation is appropriate. However, several technical concerns limit the strength of the conclusions as currently presented. The interpretation of point mutant phenotypes is complicated by the observation that mutations designed to disrupt F-actin binding also impair LATS2 binding in vitro, making it difficult to attribute the loss of LATS1 recruitment specifically to loss of strain sensing. The role of the IDR remains mechanistically undefined, and the proposed phase separation model is speculative without supporting data. The manuscript would be strengthened by additional controls, quantitative analyses, and direct binding measurements.
- **Who would be interested in the results, and why** Researchers studying Hippo pathway regulation, mechanotransduction, adherens junction biology, and LIM domain protein function. The identification of a conserved LATS-binding motif may also interest structural biologists studying protein-protein interactions in signaling pathways. The potential link to liquid-liquid phase separation could attract investigators studying biomolecular condensates in cell signaling.
- **Major strengths** 1) Addresses a mechanistically important and poorly understood aspect of Hippo signaling. 2) Combines computational prediction (AlphaFold) with experimental validation, a modern and effective approach. 3) Identifies a specific, conserved linear motif (LATS-LATCH) that is functionally validated through deletion and point mutation. 4) The finding that the IDR is required for LATS1 recruitment, independent of direct LATS binding, is novel and potentially important. 5) Clear writing and logical experimental progression.
- **Major Concerns**
- **Minor Comments**
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** **Originality**: The work is original in identifying a specific molecular interface (LATS-LATCH) and revealing an unexpected role for the IDR. However, the conceptual framework (LIMD1 as a tension sensor for Hippo) is built on prior work from the same group and others. **Scientific importance**: Potentially high, as it provides molecular insight into mechanoregulation of Hippo signaling, a topic of broad interest. The LATS-LATCH motif could be a target for therapeutic modulation. **Interdisciplinary readership**: Moderate. The topic is primarily of interest to cell and molecular biologists; structural biologists may find the AlphaFold-based interface prediction interesting. The clinical or translational relevance is not immediately apparent. **Technical soundness**: Several concerns as detailed above. The key claims are supported by the data but with caveats regarding mutant interpretation and missing controls. **Readability for nonspecialists**: The manuscript is generally well-written and accessible, with clear figures and logical flow. However, some specialized terminology (e.g., "helical hairpin," "LATS-LATCH") may require prior knowledge.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding the interpretation of point mutant phenotypes and the role of the IDR. The core finding of the LATS-LATCH interaction is likely to be of interest, but the mechanistic model requires additional experimental support.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / data interpretation
- **Claim pointer** "Point mutations that disrupt strain sensitivity in either the first or second LIM domain disrupt both binding and recruitment of LATS1/2 to AJs."
- **Evidence pointer** Figure 3A–C
- **Concern** The authors state that mutations in LIM1 (F512A) or LIM2 (F575A) disrupt both binding to LATS2 and recruitment of LATS1 to AJs. However, the authors themselves acknowledge that these mutations may affect LATS2 binding directly, independent of their effects on F-actin binding. This confound makes it impossible to conclude that the loss of LATS1 recruitment is specifically due to loss of strain sensing. The claim that "both LIM1 and LIM2 must be engaged with strained F-actin to bind LATS1" is therefore not supported by the data.
- **Why it matters** The central model of the paper is that tension-dependent F-actin binding by LIMD1 triggers LATS1/2 recruitment. If the point mutations disrupt LATS binding directly, the data cannot distinguish between a model where F-actin binding allosterically enhances LATS binding versus a model where the mutations simply impair the LATS binding interface. This distinction is critical for the proposed mechanism.
- **Resolution test** Provide direct binding assays (e.g., purified proteins, surface plasmon resonance, or pull-downs) comparing wild-type LIMD1 LIM domains with the F512A and F575A mutants for binding to both F-actin and the LATS-LATCH peptide. Alternatively, generate separation-of-function mutants that disrupt F-actin binding but retain LATS binding, or vice versa, and test their effects on LATS1 recruitment in cells.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / missing controls
- **Claim pointer** "LIMD1-(468–676), but not LIMD1-(1–467), can localize to AJs" and "both the LIM domains and IDR region are required to recruit LATS1 to adherens junctions"
- **Evidence pointer** Figure 1C–D
- **Concern** The localization experiments rely on live-cell imaging of GFP-tagged proteins expressed in LIMD1-KO cells. No data are shown for untransfected cells or cells expressing GFP alone as negative controls. Additionally, no quantification of localization efficiency is provided, making it difficult to assess the robustness of the observed differences. The authors note that GFP fluorescence did not survive fixation, which limits the ability to confirm co-localization with AJ markers.
- **Why it matters** Without proper negative controls and quantification, it is unclear whether the observed "localization" is specific to AJs or represents general cytoplasmic or membrane-associated fluorescence. The conclusion that the IDR is required for LATS1 recruitment depends on reliable scoring of AJ localization.
- **Resolution test** Include GFP-only and untransfected controls in all localization experiments. Provide quantitative analysis (e.g., percentage of cells with AJ-localized GFP, or fluorescence intensity at AJs relative to cytoplasm) with statistical comparisons. If possible, use alternative fixation/permeabilization protocols or super-resolution microscopy to confirm co-localization with AJ markers (e.g., E-cadherin, β-catenin).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / missing data
- **Claim pointer** "The LATS-LATCH is both necessary and sufficient for strain-dependent recruitment of LATS1/2 to AJs."
- **Evidence pointer** Figures 4D, 5A–C
- **Concern** The sufficiency claim is based on the observation that GFP-LATS2-LATCH alone localizes to AJs in a tension-dependent manner. However, it is unclear whether this localization represents a functional interaction with LIMD1 or simply non-specific accumulation at AJs. The necessity claim is based on deletion of the LATCH from the N-terminal region, but the authors do not show whether the deletion construct is properly folded or expressed at levels comparable to wild-type. Additionally, the point mutant (4mut) is only tested for localization and binding, not for functional effects on Hippo signaling (e.g., YAP activity).
- **Why it matters** The claim that the LATS-LATCH is the key functional motif for tension-dependent recruitment requires demonstration that the interaction is specific and functionally relevant. Without functional readouts (e.g., YAP localization or transcriptional activity), it is unclear whether the LATS-LATCH interaction is sufficient to mediate Hippo signaling outcomes.
- **Resolution test** Test whether the LATS2-LATCH-GFP fusion can rescue LATS1/2 function in cells depleted of endogenous LATS1/2 (e.g., measure YAP phosphorylation or target gene expression). Perform competition experiments with a LATS-LATCH peptide to block endogenous LIMD1-LATS interaction. Confirm that the 4mut LATS2-LATCH fails to rescue Hippo signaling in functional assays.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / data interpretation
- **Claim pointer** "AlphaFold predicts that the 3 LIM domains of LIMD1 have 2 distinct binding sites in LATS1/2... The first region (aa431–465 of LATS2) which we term the LATS LATCH is a highly conserve region... with the highest confidence scores for the regions interacting with LIM domains one and two."
- **Evidence pointer** Figure 4B–C
- **Concern** The AlphaFold model is presented as a key tool for identifying the LATS-LATCH, but no model confidence metrics (pLDDT scores, PAE values) are provided. The authors state that the LATS-LATCH is "highly conserved" but do not show a sequence alignment or conservation analysis. The second predicted binding site (helical hairpin) is dismissed based on deletion experiments, but the authors note that this region may still be relevant in vivo, citing their previous work on TRIP6-MOB1 competition.
- **Why it matters** AlphaFold predictions are only as reliable as their confidence scores. Without these metrics, readers cannot assess the validity of the predicted interface. The conservation claim requires supporting data. The potential relevance of the helical hairpin interaction introduces ambiguity about whether the LATS-LATCH is truly the sole or primary binding site.
- **Resolution test** Provide pLDDT and PAE plots for the predicted LIMD1-LATS2 complex. Show a sequence alignment of the LATS-LATCH region across species. Discuss or experimentally test whether the helical hairpin interaction contributes to LIMD1-LATS binding under any conditions (e.g., in the presence of MOB1).

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity / data presentation
- **Affected element** Figure 1A–B
- **Evidence pointer** Figure 1A–B
- **Issue** The co-immunoprecipitation data are described but no representative blots are shown in the text. The reader cannot assess the quality of the data or the specificity of the interactions.
- **Required correction** Include representative Western blot images for the co-immunoprecipitation experiments, with molecular weight markers and appropriate loading controls.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Localization quantifications
- **Evidence pointer** Figures 1C–D, 2B–C, 3A–B, 4A, 5B–C
- **Issue** No statistical analysis is reported for the localization experiments. It is unclear how many cells were scored, whether experiments were repeated, and whether differences are significant.
- **Required correction** Provide statistical details (n, mean ± SD or SEM, statistical test used, p-values) for all quantification experiments.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** LATS2 localization
- **Evidence pointer** Results section, "Note that because endogenous LATS2 is very difficult to detect, all studies involving endogenous proteins focused on LATS1."
- **Issue** The manuscript title and abstract refer to both LATS1 and LATS2, but most functional experiments focus on LATS1. The authors should clarify whether the findings are expected to apply equally to LATS2, given the high sequence similarity.
- **Required correction** Add a statement in the Discussion addressing the likely applicability of the findings to LATS2, or provide at least one experiment showing LATS2 recruitment (e.g., overexpression of tagged LATS2).

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** IDR deletion mutant
- **Evidence pointer** Figure 1C
- **Concern** The IDR deletion mutant (Δ1–467) is described as not sufficient for LATS1 recruitment, but it is unclear whether this mutant is expressed at levels comparable to wild-type LIMD1. If the mutant is unstable or poorly expressed, the result could be a trivial consequence of reduced protein levels.
- **Required correction** Show Western blot analysis of expression levels for all deletion and point mutants used in the study.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Phase separation model
- **Evidence pointer** Discussion, "One intriguing possibility is that the IDR region of LIMD1 may promote liquid-liquid phase separations (LLPS)..."
- **Issue** The phase separation hypothesis is presented without any supporting data. While speculative discussion is acceptable, the authors should clearly label this as a hypothesis and avoid overstating its likelihood.
- **Required correction** Soften the language in the Discussion and explicitly state that this is a speculative model requiring future testing.

## Risk / unsupported claims
- The claim that "both LIM1 and LIM2 must be engaged with strained F-actin to bind LATS1" is not supported because the point mutations used also disrupt LATS2 binding directly (R1-M1).
- The claim that the LATS-LATCH is "sufficient" for strain-dependent recruitment is based solely on localization of an overexpressed GFP fusion and lacks functional validation (R1-M3).
- The claim that the IDR is required for LATS1 recruitment is weakened by the lack of expression level controls for the deletion mutant (R1-m4).
- The phase separation model proposed in the Discussion is entirely speculative and not supported by any experimental evidence (R1-m5).
- The conservation of the LATS-LATCH is stated but not demonstrated with sequence alignment data (R1-M4).