## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusion) as provided
- **Assessment boundary** Bioinformatics analysis of PRAME intrinsic disorder; no experimental validation data included
- **Shared manuscript claim summary** The authors report that PRAME contains intrinsically disordered protein regions (IDPRs), is moderately disordered overall, possesses redox-sensitive disorder-to-order transition (DOT) regions near the C-terminus, contains a droplet-promoting region and aggregation hotspots, and has a complex protein-protein interaction network. They propose these structural features may be linked to PRAME function in Class 1 uveal melanoma and could serve as therapeutic targets.
- **Visible evidence base** Computational predictions from AlphaFold, compositional profiling, ten disorder predictors, D2P2 platform, IUPred redox analysis, FuzDrop, and STRING interaction network
- **Missing materials affecting confidence** No experimental validation (biochemical, biophysical, or cellular assays); no raw prediction scores or statistical details for most predictors; no supplementary figures beyond Figure S1; no data on PRAME expression levels in the specific tumor context beyond cited literature; no functional assays linking disorder to melanoma biology

## Reviewer
- **Overall assessment** This manuscript presents a purely computational characterization of intrinsic disorder in PRAME. The authors apply a reasonable suite of established bioinformatics tools and report findings that are largely consistent with the known properties of PRAME. However, the study is descriptive and correlative in nature. The central claim that IDPRs in PRAME are "possibly linked to its functionality" in uveal melanoma is speculative and not directly tested. The connection between the computational predictions and the clinical context of Class 1 uveal melanoma is asserted rather than demonstrated. The work may be of interest to researchers studying PRAME biology or disorder-based drug targeting, but the evidence presented does not establish a mechanistic role for intrinsic disorder in PRAME function or melanoma pathogenesis.

- **Who would be interested in the results, and why** Researchers studying PRAME as a cancer/testis antigen and immunotherapeutic target, particularly in uveal melanoma; investigators interested in intrinsically disordered proteins in cancer biology; computational biologists working on disorder prediction and its functional annotation. The findings may inform future experimental designs aimed at targeting PRAME's disordered regions.

- **Major strengths** The authors use a comprehensive and appropriate set of computational tools for disorder prediction, including both established predictors and newer deep-learning methods. The multi-predictor approach with consensus interpretation is methodologically sound. The identification of specific functional features (DOT regions, PTM sites, droplet-promoting regions, aggregation hotspots) provides a useful structural annotation of PRAME. The study addresses a clinically relevant protein in a cancer type with high unmet need.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim-evidence alignment
- **Claim pointer** The authors state in the abstract and conclusion that PRAME contains IDPRs "possibly linked to its functionality in the context of Class 1 UM" and that these regions "may be targeted in developing new therapies."
- **Evidence pointer** Results sections on disorder prediction, D2P2, FuzDrop, STRING; Discussion section
- **Concern** The manuscript provides no direct evidence linking the predicted disordered regions to PRAME function in uveal melanoma. The computational predictions are descriptive annotations of the primary sequence. No experimental data (e.g., mutagenesis, deletion constructs, cellular assays, binding studies) are presented to test whether the identified IDPRs, DOT regions, or PTM sites actually contribute to PRAME's oncogenic activity, its interaction with retinoic acid receptor alpha, or its role in immune evasion. The leap from "PRAME has disordered regions" to "these regions are functionally important in uveal melanoma" is unsupported.
- **Why it matters** The stated purpose of the study, as framed in the introduction and discussion, is to understand the role of intrinsic disorder in PRAME's function in Class 1 uveal melanoma. Without functional validation, the clinical relevance of the findings remains speculative. The manuscript does not establish a causal or even correlative link between the predicted disorder features and melanoma biology.
- **Resolution test** The authors would need to provide experimental evidence, such as showing that deletion or mutation of the identified IDPRs alters PRAME function in relevant assays (e.g., effects on cell proliferation, apoptosis resistance, RARA interaction, or T-cell recognition). Alternatively, they could present data linking disorder predictions to patient outcomes or PRAME expression levels in tumor samples.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The authors report that PRAME is "significantly enriched with serine (p-value < 0.05)" and that the STRING analysis shows "significantly more interactions with other proteins than expected" (p-value < 1.0 × 10–16).
- **Evidence pointer** Results section, Compositional profiler subsection; Results section, Protein-protein interaction network subsection; Figure 2; Figure 7
- **Concern** The statistical methods for the compositional analysis are not described. The p-value for serine enrichment is reported without specifying the statistical test, the null model, the correction for multiple comparisons, or the number of amino acids tested. Similarly, the STRING p-value is reported but the methodology for its calculation and the interpretation of the network enrichment are not explained. The reader cannot assess whether these results are robust or whether they would survive multiple-testing correction.
- **Why it matters** The significance claims are central to the authors' interpretation that PRAME has disorder-promoting compositional features and a complex interaction network. Without proper statistical reporting, these claims cannot be evaluated or reproduced.
- **Resolution test** The authors should describe the statistical tests used, including the null model for compositional enrichment, whether multiple-comparison corrections were applied, and the exact procedure for STRING enrichment analysis. They should also report effect sizes and confidence intervals where appropriate.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretive caution
- **Claim pointer** The authors state that "PRAME has a complex protein-protein interaction (PPI) network that may be secondary to the structureless features of the polypeptide" and that the predicted droplet-promoting region and aggregation hotspots "may play a role in regulating the concentration of proteins in the cell."
- **Evidence pointer** Results section, Protein-protein interaction network subsection; Results section, FuzDrop subsection; Figure 6; Figure 7
- **Concern** The STRING analysis at medium confidence (0.400) shows 85 nodes and 577 edges, but the authors do not discuss the biological plausibility of these interactions or whether they are supported by experimental evidence. The claim that the PPI network is "secondary to" the disordered features is speculative and not tested. Similarly, the functional interpretation of the droplet-promoting region and aggregation hotspots as regulators of protein concentration is presented without supporting evidence or discussion of alternative interpretations.
- **Why it matters** Overinterpretation of computational predictions can mislead readers and future research directions. The authors should clearly distinguish between predictions and established facts, and should temper their functional claims accordingly.
- **Resolution test** The authors should either provide experimental or literature-based support for the proposed functional roles of the identified regions, or explicitly frame these as hypotheses requiring further testing. They should also discuss the limitations of STRING-based interaction predictions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Clinical relevance
- **Claim pointer** The authors state that "IDPRs and DOT regions in PRAME may be targeted in developing new therapies for this aggressive cancer" and that findings "may be applied" to other PRAME-expressing malignancies.
- **Evidence pointer** Discussion section; Conclusion section
- **Concern** The therapeutic implications are stated without any evidence that targeting disordered regions of PRAME is feasible or would be clinically beneficial. No discussion of druggability, delivery challenges, or potential off-target effects is provided. The connection between the computational findings and therapeutic development is entirely speculative.
- **Why it matters** The clinical framing is a major motivation for the study. Without a realistic assessment of the therapeutic potential, the manuscript overstates its translational relevance.
- **Resolution test** The authors should either provide a more measured discussion of the challenges and opportunities for targeting disordered proteins therapeutically, or present preliminary evidence (e.g., proof-of-concept in vitro data) supporting the feasibility of such an approach.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section, Protein-protein interaction network
- **Evidence pointer** Methods section, Protein-protein interaction network subsection
- **Issue** The authors state that the minimum required interaction score was set to 0.900 for the STRING analysis, but Figure 7A is described as showing medium confidence (0.400). The relationship between these two settings is unclear.
- **Required correction** Clarify whether two separate STRING analyses were performed (one at medium and one at high confidence) and describe the rationale for each.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Internal consistency
- **Affected element** Results section, Per-residue disorder prediction
- **Evidence pointer** Results section, Per-residue disorder prediction subsection; Figure 3
- **Issue** The text states that PRAME was predicted to be 28.36% disordered by PONDR VLXT, 28.02% by VL3, 30.89% by VSL2, 20.61% by PONDR-FIT, 10.31% by IUPred-Long, and 9.39% by IUPred-Short. However, the abstract reports an "average disorder score of 16.49%" across six predictors. The relationship between the per-predictor percentages and the average score is not explained, and the average is not clearly defined.
- **Required correction** Define how the average disorder score was computed and clarify whether it represents a mean of the per-predictor percentages or a different metric.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results section, FuzDrop analysis
- **Evidence pointer** Results section, FuzDrop subsection; Figure 6
- **Issue** The authors report that PRAME has one droplet-promoting region and two aggregation hotspots but do not provide the specific residue ranges for these features in the text. The figure legend may contain this information, but it is not accessible in the provided text.
- **Required correction** Include the specific residue ranges for the droplet-promoting region and aggregation hotspots in the text for clarity and reproducibility.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Results section, Protein-protein interaction network
- **Evidence pointer** Results section, Protein-protein interaction network subsection; Figure 7
- **Issue** The authors describe the STRING network at medium confidence as having 85 nodes and 577 edges, but the abstract mentions "84 different partners." The discrepancy between 85 nodes and 84 partners is not explained.
- **Required correction** Clarify whether the 85 nodes include PRAME itself, and ensure consistent reporting of the number of interaction partners.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Referencing
- **Affected element** Introduction section
- **Evidence pointer** Introduction section, paragraph 1
- **Issue** The authors state that "IDPs/IDPRs have been linked extensively to the pathogenesis of disease and malignancies" and cite references [13-17]. However, the specific relevance of these references to uveal melanoma or PRAME is not discussed.
- **Required correction** Briefly explain how the cited literature on IDPs in cancer relates to the specific context of PRAME and uveal melanoma.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 1
- **Evidence pointer** Results section, Structural assessment subsection; Figure 1
- **Issue** The authors state that Figure 1 shows regions of low model confidence indicated by yellow/orange coloring, but the figure is not available in the provided text. The description of the figure is qualitative and does not provide quantitative pLDDT values for the disordered regions.
- **Required correction** Consider providing pLDDT values or a plot of pLDDT versus residue number to support the qualitative description of disorder.

## Risk / unsupported claims
- The claim that IDPRs in PRAME are "possibly linked to its functionality in the context of Class 1 UM" is unsupported by direct experimental evidence.
- The claim that the predicted droplet-promoting region and aggregation hotspots "may play a role in regulating the concentration of proteins in the cell" is speculative and not tested.
- The claim that "IDPRs and DOT regions in PRAME may be targeted in developing new therapies" is not supported by any feasibility or efficacy data.
- The claim that PRAME has a "complex protein-protein interaction network" is based solely on computational prediction and is not validated experimentally.
- The statistical significance of serine enrichment and STRING interaction enrichment cannot be evaluated due to incomplete methodological reporting.
- The clinical relevance of the findings to uveal melanoma prognosis or treatment is asserted but not demonstrated with patient data or functional studies.