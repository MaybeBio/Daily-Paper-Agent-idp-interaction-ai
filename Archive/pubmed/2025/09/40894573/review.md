## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) and metadata (title, authors, preprint server, date, DOI/ID, URL)
- **Assessment boundary** Scientific content, technical soundness, and claims as presented in the provided manuscript text. No external data, code, or supplementary materials were accessed or verified.
- **Shared manuscript claim summary** The authors use AlphaFold2 multimer to predict protein-protein interaction structures for 27,711 high-confidence STRING pairs in Drosophila melanogaster, report that 3,621 are high-confidence physical interactions, and highlight the prevalence and importance of intrinsically disordered regions in mediating these interactions. They provide a web interface for exploration.
- **Visible evidence base** Main text, figure captions (Figures 1-5), supplementary figure/table references (S1-S6, Tables S1-S3), methods section, data/code availability statements
- **Missing materials affecting confidence** Supplementary figures and tables (S1-S6, S1-S4 Appendices, S1-S3 Tables), actual structural predictions, code, and the web interface were not provided for verification. No experimental validation data are included.

## Reviewer
- **Overall assessment** This manuscript presents a large-scale structural prediction effort for Drosophila protein-protein interactions, with a focus on the role of intrinsically disordered regions. The work is timely and potentially useful as a community resource. However, the core claims regarding the prevalence and functional significance of disordered region-mediated interactions rest on computational predictions that are not independently validated, and several methodological details are insufficiently described to assess robustness. The manuscript would benefit from clearer presentation of prediction confidence metrics, explicit handling of potential biases, and a more critical discussion of limitations.
- **Who would be interested in the results, and why** Researchers studying Drosophila biology, protein-protein interaction networks, intrinsically disordered proteins, and those interested in applying AlphaFold-based structural prediction to interactome-scale questions. The web resource could be valuable for hypothesis generation in these communities.
- **Major strengths** 1) Large-scale application of AlphaFold2 multimer to a non-mammalian interactome fills a gap in existing resources. 2) The integration of functional association data (STRING) with structural prediction is a pragmatic approach. 3) The focus on intrinsically disordered regions in interaction interfaces is a relevant and underexplored angle. 4) The provision of a web interface and public data deposition enhances utility.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (validation of predictions), R1-M2 (classification of disordered binding modes), R1-M3 (representativeness of protein set), R1-M4 (definition of "high confidence").
- **Assessment against Nature-style criteria** **Originality**: Moderate. The application of AlphaFold2 to a Drosophila interactome is not conceptually novel, but the specific focus on disordered regions provides some differentiation. **Scientific importance**: Potentially high as a resource, but the lack of experimental validation limits the strength of biological conclusions. **Interdisciplinary readership**: Likely to appeal to structural biologists, cell biologists, and bioinformaticians, but the presentation may be too specialized for a general audience. **Technical soundness**: The core methodology is established, but the analysis pipeline has ambiguities and potential biases that need clarification. **Readability for nonspecialists**: The manuscript is generally clear but includes jargon and assumes familiarity with AlphaFold metrics and interactome concepts.
- **Recommendation posture** Supportive if technical concerns are resolved. The resource aspect is valuable, but the biological claims about disordered regions require stronger support and clearer methodology.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation of computational predictions
- **Claim pointer** The manuscript claims that 3,621 protein pairs are "high-confidence physical interactions" based on pDockQ ≥ 0.5, and that these predictions are robust enough to support biological conclusions about disordered regions.
- **Evidence pointer** Results section "Predicted high confident D. melanogaster physical protein-protein interaction network"; Methods "Structure prediction and structural analysis"
- **Concern** The manuscript relies entirely on AlphaFold2 multimer predictions without any experimental validation. While the authors note that some predictions match known structures (e.g., Ku80/Irbp), no systematic comparison to existing experimental structures or independent validation (e.g., cross-linking, mutagenesis) is provided. The claim that 81% of high-confidence predictions align with STRING physical evidence is circular, as STRING itself includes computational predictions and homology transfer.
- **Why it matters** Without independent validation, the false-positive rate of AlphaFold2 multimer at this scale is unknown. The biological conclusions, particularly about the prevalence of disordered region-mediated interactions, depend on the accuracy of these predictions. Overstated confidence could mislead the community.
- **Resolution test** Provide a benchmark against a set of experimentally determined Drosophila complexes (or orthologous complexes) with known interaction interfaces. Report precision/recall for the pDockQ threshold. Alternatively, perform targeted experimental validation (e.g., co-immunoprecipitation or cross-linking) for a subset of novel predictions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Classification of disordered binding modes
- **Claim pointer** The manuscript claims that 98.8% of high-confidence PPIs involve intrinsically disordered regions, and that 51.7% involve "conditionally folded" binding and 21.0% involve "coil-to-order" binding.
- **Evidence pointer** Results section "Most predicted dimers involve binding through disordered regions"; Methods "Infer disordered, coil, and conditionally folded regions"
- **Concern** The classification of binding modes relies on definitions that are not fully operationalized. "Conditionally folded" is defined as regions with both high pLDDT (>70) and high disorder (ISD > 0.5), which is a specific computational proxy but may not correspond to the biological concept of conditional folding. The "coil-to-order" classification uses a Fisher exact test on secondary structure content, but the threshold and interpretation are not fully justified. The high percentages reported (98.8% involving IDRs) may be inflated by the permissive definition of disorder (5 consecutive residues with ISD > 0.5).
- **Why it matters** The central biological claim of the paper is that disordered regions are prevalent in interaction interfaces. If the classification is too permissive or the definitions are not biologically meaningful, this claim is weakened. The specific percentages (51.7%, 21.0%) are presented as quantitative findings but may be artifacts of the classification scheme.
- **Resolution test** Provide a detailed description of the classification algorithm with explicit thresholds and examples. Validate the classification against known disordered binding regions from experimental studies (e.g., from DisProt or literature). Show that the results are robust to reasonable variations in thresholds (e.g., ISD cutoff, length cutoff).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Representativeness of protein set
- **Claim pointer** The manuscript claims to examine "protein-protein interactions from both physical and functional datasets in Drosophila" and that the findings about disordered regions apply at a "genomic scale."
- **Evidence pointer** Results section "Predicted high confident D. melanogaster physical protein-protein interaction network"; Methods "Extracting representative PPIs from the STRING database"
- **Concern** The analysis is restricted to 27,711 pairs from STRING with confidence ≥ 0.9, clustered at 50% sequence identity. This set is likely biased toward well-studied, conserved proteins and may underrepresent transient interactions, membrane proteins, or proteins with long disordered regions that are difficult to predict. The claim of "genomic scale" is an overstatement given this filtering.
- **Why it matters** If the protein set is biased, the conclusions about the prevalence of disordered region-mediated interactions may not generalize to the full Drosophila proteome. The resource value is also diminished if important classes of interactions are excluded.
- **Resolution test** Compare the properties of the analyzed set (e.g., sequence length, disorder content, functional categories) to the full Drosophila proteome. Discuss potential biases and their impact on the conclusions. If possible, include a sensitivity analysis with different STRING confidence thresholds.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Definition of "high confidence"
- **Claim pointer** The manuscript uses pDockQ ≥ 0.5 as the threshold for "high-confidence" physical interactions, and pDockQ ≥ 0.23 for "acceptable" confidence.
- **Evidence pointer** Results section "Predicted high confident D. melanogaster physical protein-protein interaction network"; Methods "Structure prediction and structural analysis"
- **Concern** The choice of pDockQ thresholds is not justified. pDockQ is a proxy for model quality, but its relationship to true interaction accuracy is not established for this dataset. The authors do not report the distribution of pDockQ scores or the number of predictions at different thresholds.
- **Why it matters** The threshold determines the size and composition of the "high-confidence" set, which underpins all subsequent analyses. Without justification, the reader cannot assess whether the threshold is appropriate or whether the results are sensitive to it.
- **Resolution test** Provide a rationale for the pDockQ thresholds, citing relevant benchmarks. Report the number of predictions at various thresholds and show that the main conclusions (e.g., prevalence of IDR involvement) are robust across a range of thresholds.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure presentation
- **Affected element** Figure 1
- **Evidence pointer** Results section "AlphaFold2 multimer predicts core physical interaction networks"
- **Issue** The description of Figure 1 is brief and does not explain what is shown in panels a, b, c, etc. The text mentions "one large, connected subnetwork" and "11 relatively small" but does not describe the visual layout or how to interpret the network representation.
- **Required correction** Expand the figure legend to describe each panel explicitly, including the meaning of node colors, sizes, and edge weights. Consider adding a schematic of the analysis pipeline as a panel.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results section "Predicted high confident D. melanogaster physical protein-protein interaction network"
- **Evidence pointer** Text: "52% (1867 pairs) are supported by highest STRING confidence scores for physical interaction (≥ 0.9, S2 Fig), ~70% (2541 pairs...)"
- **Issue** The percentages are reported with varying precision (52%, ~70%, ~81%) and the denominators are not always clear. It is unclear whether these percentages are out of the 3,621 high-confidence predictions or a different subset.
- **Required correction** Report exact numbers and percentages with consistent precision. Clarify the denominator for each percentage.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion section
- **Evidence pointer** Discussion, final paragraph
- **Issue** The limitations section is brief and focuses on technical constraints (sequence length, computational resources). It does not discuss the potential for systematic biases in AlphaFold2 predictions, the lack of experimental validation, or the limitations of the STRING database itself.
- **Required correction** Add a more comprehensive limitations paragraph addressing the caveats of computational prediction, the potential for false positives/negatives, and the need for experimental follow-up.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Web interface accessibility
- **Affected element** Results section "An interactive web interface"
- **Evidence pointer** Text: "The platform is accessible at https://melppi.github.io"
- **Issue** The manuscript does not specify the browser requirements, data download options, or whether the interface supports programmatic access (e.g., API). This limits the utility for users who may want to perform large-scale analyses.
- **Required correction** Provide additional details on the web interface, including supported browsers, download options, and any API or bulk access features.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Throughout
- **Evidence pointer** Abstract: "binding interference from intrinsically disordered regions"; Results: "binding through disordered regions"
- **Issue** The term "binding interference" in the title and abstract is not clearly defined or consistently used in the text. The results describe disordered regions as "mediating" or "involved in" interactions, which is different from "interference."
- **Required correction** Define "binding interference" in the introduction and use consistent terminology throughout. If the authors mean that disordered regions can both promote and inhibit binding, this should be explicitly stated and supported by data.

## Risk / unsupported claims
- The claim that "98.8% of predicted high confidence PPIs involve intrinsically disordered regions" is not supported by the data presented, as the definition of "involve" is overly permissive and the classification method is not fully validated.
- The claim that "our predictions highlight the importance of incorporating functional associations in guiding the prediction of protein-protein interactions" is not directly tested. The authors do not compare predictions with and without functional association data.
- The statement that "the remaining 19% predictions... may still represent biologically relevant interactions" is speculative and not supported by any independent evidence.
- The claim that "the Ku80–Irbp complex simultaneously employs coil-to-order and conditionally folded binding" is based on a single example and may not be generalizable.
- The assertion that "functional associations... had similar proportions predicted as high confidence physical interactions as those supported primarily by experimental evidence" is presented without statistical testing or discussion of potential confounders.