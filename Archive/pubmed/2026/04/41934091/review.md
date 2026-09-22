## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no figures, methods, or supplementary material were provided
- **Shared manuscript claim summary** The authors propose that polyKR motifs in centrosomal coiled-coil proteins mediate tubulin concentration within the pericentriolar matrix (PCM), based on experiments in engineered condensates, bioinformatic analyses across species, binding affinity measurements, cellular puncta assays, and purified protein condensate systems.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary data were supplied
- **Missing materials affecting confidence** Full text, all figures and tables, methods section, statistical details, and supplementary information; without these, quantitative claims and experimental rigor cannot be independently assessed

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting and broadly relevant mechanism for tubulin concentration at centrosomes, with a clear conceptual advance over existing models. The claim that polyKR motifs in coiled-coil centrosomal proteins serve as general tubulin-concentrating elements is plausible and would appeal to a wide cell biology audience. However, the abstract alone provides insufficient detail to evaluate the robustness of the experimental support. Several quantitative claims, particularly regarding binding affinities and fold-concentration values, require scrutiny of the underlying data. The evolutionary analysis and the redundancy argument are intriguing but under-specified. Overall, the work appears promising, but the case is not fully established from the abstract alone.
- **Who would be interested in the results, and why** Cell biologists studying centrosome biology, microtubule dynamics, and intracellular organization; biophysicists interested in phase separation and condensate-mediated biochemical reactions; evolutionary biologists examining conserved protein motifs; and researchers working on protein-protein interactions involving tubulin. The proposed mechanism could have implications for understanding how cells locally regulate microtubule nucleation and organization.
- **Major strengths** The conceptual framework is clear and testable, linking sequence motifs to a biophysical function in a physiologically relevant context. The use of multiple complementary approaches, including engineered condensates, bioinformatics, binding assays, cellular puncta, and purified systems, suggests a multi-pronged validation strategy. The cross-species conservation analysis adds evolutionary weight to the claim. The proposed redundancy of the mechanism is a thoughtful consideration of biological robustness.
- **Major Concerns**  
  - **Concern ID** R1-M1  
    **Severity** Major  
    **Blocking** Yes  
    **Axis** Technical soundness  
    **Claim pointer** "The tubulin binding affinity of polyKR motifs with six to 10 basic residues is approximately in the micromolar to submicromolar range."  
    **Evidence pointer** Location not provided  
    **Concern** The abstract reports a binding affinity range but provides no information on the assay method, the specific constructs used, the number of replicates, or the statistical treatment. Affinity values in this range are highly sensitive to experimental conditions such as ionic strength, pH, and the presence of crowding agents.  
    **Why it matters** The affinity range is central to the claim that polyKR motifs are physiologically relevant tubulin-binding elements. Without methodological detail, it is impossible to judge whether the measured affinities are robust or artefactual.  
    **Resolution test** Provide the binding assay details, including the method (e.g., ITC, SPR, fluorescence anisotropy), the exact peptide or protein constructs, buffer conditions, and replicate numbers, with error estimates.  
  - **Concern ID** R1-M2  
    **Severity** Major  
    **Blocking** Yes  
    **Axis** Technical soundness  
    **Claim pointer** "In purified systems, we show that TACC3 and Cep63 condensates containing polyKR motifs concentrate tubulin dimers over 10-fold."  
    **Evidence pointer** Location not provided  
    **Concern** The fold-concentration value of "over 10-fold" is presented without any indication of how it was measured, what the baseline was, or what the variability was across experiments. The choice of TACC3 and Cep63 as representative proteins is not justified in the abstract.  
    **Why it matters** This is a key quantitative result supporting the central claim. Without knowing the measurement method (e.g., fluorescence intensity ratio, partition coefficient) and the experimental variability, the reliability of the 10-fold value cannot be assessed.  
    **Resolution test** Describe the quantitative imaging or biochemical method used to measure tubulin concentration within condensates, include representative images, and report the number of independent experiments and the standard deviation or confidence interval.  
  - **Concern ID** R1-M3  
    **Severity** Major  
    **Blocking** Yes  
    **Axis** Technical soundness  
    **Claim pointer** "Bioinformatic analysis reveals that polyKR motif-containing coiled-coil proteins are highly enriched in centrosomes across species, from worms and flies to mice and humans."  
    **Evidence pointer** Location not provided  
    **Concern** The abstract does not specify the bioinformatic criteria used to define a polyKR motif, the database or proteome sets analyzed, the statistical test for enrichment, or the correction for multiple comparisons. The phrase "highly enriched" is qualitative.  
    **Why it matters** The cross-species conservation claim is a major pillar of the paper's generality. Without defined criteria and statistical rigor, the enrichment could be an artefact of sequence composition or database bias.  
    **Resolution test** Provide the motif definition, the list of centrosomal proteomes used, the enrichment statistics with p-values and effect sizes, and the number of proteins identified per species.  
  - **Concern ID** R1-M4  
    **Severity** Major  
    **Blocking** No  
    **Axis** Originality  
    **Claim pointer** "We describe a mechanism of tubulin concentration by polyKR motifs encoded in the centrosomal coiled-coil proteins."  
    **Evidence pointer** Location not provided  
    **Concern** The abstract does not discuss how this mechanism relates to previously described tubulin-binding motifs or to known centrosomal proteins that recruit tubulin. The novelty claim is therefore not contextualized.  
    **Why it matters** For a broad-audience journal, situating the finding within existing literature is essential to establish what is genuinely new. Without this, the originality claim is difficult to evaluate.  
    **Resolution test** Add a brief comparison to known tubulin-binding motifs and existing models of tubulin recruitment to the PCM, and explicitly state what is novel.  
  - **Concern ID** R1-M5  
    **Severity** Major  
    **Blocking** No  
    **Axis** Scientific importance  
    **Claim pointer** "The spatial density of polyKR motifs correlates with MT concentration, suggesting that cells can modulate tubulin concentration at the PCM by tuning the centrosomal composition."  
    **Evidence pointer** Location not provided  
    **Concern** The correlation is stated but the strength of the correlation, the number of data points, and the experimental system in which it was measured are not given. The causal interpretation ("suggesting that cells can modulate") goes beyond a correlation.  
    **Why it matters** This claim extends the mechanism to a regulatory role, which is a significant conceptual step. Without quantitative correlation data and a discussion of alternative explanations, the inference is premature.  
    **Resolution test** Provide the correlation coefficient, the number of measurements, the experimental system, and a discussion of whether the correlation is causal or could reflect a downstream effect.  
  - **Concern ID** R1-M6  
    **Severity** Major  
    **Blocking** No  
    **Axis** Technical soundness  
    **Claim pointer** "Cytoplasmic puncta containing the predicted centrosomal polyKR motifs concentrate microtubules."  
    **Evidence pointer** Location not provided  
    **Concern** The abstract does not specify the cell type, the method of puncta formation, the nature of the "predicted" motifs, or how microtubule concentration was quantified. The term "concentrate" is not defined quantitatively.  
    **Why it matters** This is the only cellular evidence presented, and it is central to the physiological relevance of the mechanism. Without details, the result cannot be evaluated.  
    **Resolution test** Describe the cell system, the construct used to generate puncta, the quantification method, and the statistical comparison to controls.  
- **Minor Comments**  
  - **Concern ID** R1-m1  
    **Severity** Minor  
    **Axis** Readability for nonspecialists  
    **Affected element** Abstract text  
    **Evidence pointer** Location not provided  
    **Issue** The term "polyKR" is used without definition. Nonspecialist readers may not know that K and R denote lysine and arginine.  
    **Required correction** Define polyKR as "poly-lysine/arginine" at first mention.  
  - **Concern ID** R1-m2  
    **Severity** Minor  
    **Axis** Readability for nonspecialists  
    **Affected element** Abstract text  
    **Evidence pointer** Location not provided  
    **Issue** The phrase "functionally redundant to ensure robust tubulin enrichment" is vague. It is unclear whether redundancy refers to multiple motifs within one protein, multiple proteins, or multiple mechanisms.  
    **Required correction** Clarify the level at which redundancy operates and provide a brief explanation of why redundancy is beneficial.  
  - **Concern ID** R1-m3  
    **Severity** Minor  
    **Axis** Scientific importance  
    **Affected element** Abstract text  
    **Evidence pointer** Location not provided  
    **Issue** The abstract does not state the potential implications of the finding for understanding centrosome-related diseases or for therapeutic targeting.  
    **Required correction** Add one sentence on the broader implications, if supported by the data.  
  - **Concern ID** R1-m4  
    **Severity** Minor  
    **Axis** Technical soundness  
    **Affected element** Abstract text  
    **Evidence pointer** Location not provided  
    **Issue** The abstract states "engineered protein condensates that mimic the protein-dense environment of the centrosome" but does not specify how the mimicry was validated.  
    **Required correction** Briefly state the validation criterion or refer to a figure that establishes the relevance of the engineered system.  
- **Technical failings that need to be addressed before the case is established** R1-M1 (binding affinity methodology), R1-M2 (fold-concentration measurement), R1-M3 (bioinformatic criteria and statistics), R1-M6 (cellular puncta quantification). These four concerns directly affect the core claims and cannot be resolved without additional data.
- **Assessment against Nature-style criteria**  
  - Originality: The proposed mechanism appears novel, but the abstract does not contextualize it against existing tubulin-binding motifs, so the degree of novelty is not fully assessable.  
  - Scientific importance: The finding has potential significance for centrosome biology and intracellular organization, but the regulatory claim based on correlation is not yet supported.  
  - Interdisciplinary readership: The topic would interest cell biologists, biophysicists, and evolutionary biologists, but the abstract is written in a specialized manner that may limit accessibility.  
  - Technical soundness: The abstract reports multiple quantitative results without methodological detail, which prevents assessment of technical rigor.  
  - Readability for nonspecialists: The abstract is concise but uses undefined terms and lacks context, which reduces accessibility.
- **Recommendation posture** Supportive if technical concerns are resolved. The conceptual framework is promising and the multi-pronged approach is commendable, but the abstract alone does not provide sufficient evidence to establish the case. The authors should provide full methodological details and quantitative data to address the blocking concerns.

## Risk / unsupported claims
- The claim that polyKR motifs are "highly enriched" in centrosomes across species is unsupported without defined bioinformatic criteria and statistics.
- The claim that TACC3 and Cep63 condensates concentrate tubulin "over 10-fold" is unsupported without measurement details.
- The claim that binding affinity is "in the micromolar to submicromolar range" is unsupported without assay details.
- The claim that "cells can modulate tubulin concentration at the PCM by tuning the centrosomal composition" is an inference from a correlation that is not quantitatively described.
- The claim that the mechanism is "functionally redundant" is not supported by any experimental evidence in the abstract.
- The claim that engineered condensates "mimic the protein-dense environment of the centrosome" is not validated in the abstract.