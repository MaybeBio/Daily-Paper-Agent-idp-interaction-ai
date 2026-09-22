## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors report the first structural overview of the Saccharomyces cerevisiae TPS/TPP complex under heat shock (40 degrees C), using cross-linking mass spectrometry (XL-MS) and computational modeling. They claim that cross-linking data corroborate AlphaFold models for isolated subunits, that intrinsically disordered regions (IDRs) are present in regulatory subunits, that the disordered N-terminus of Tsl1 is important for complex assembly, and that phosphorylation predictions implicate Tps3 disordered regions in inhibiting Tps2 activity and halting trehalose-6-phosphate (T6P) accumulation. The stated significance is a mechanistic understanding of trehalose synthesis with implications for antifungal drug design.
- **Visible evidence base** Abstract text only; no experimental details, cross-linking spectra, model validation metrics, or statistical analyses are provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, cross-linking mass spectrometry data, AlphaFold model comparison details, phosphorylation prediction methodology, and any validation or control experiments

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting application of XL-MS and computational modeling to a biologically and clinically relevant enzyme complex. However, the claims as stated are broad and largely unsupported by the evidence visible in the abstract. The central assertions regarding complex assembly, disordered region function, and phosphorylation-mediated regulation are presented without quantitative data, methodological detail, or clear validation. The work may have merit, but the current evidence base is insufficient to establish the mechanistic conclusions.
- **Who would be interested in the results, and why** Researchers in fungal biology, trehalose metabolism, and antifungal drug discovery would be interested. Structural biologists using cross-linking mass spectrometry and computational modeling would also find the methodological application relevant. The potential therapeutic angle targeting pathogenic fungi may attract applied microbiologists and pharmaceutical researchers.
- **Major strengths** The study addresses a genuine knowledge gap in the structural organization of the TPS/TPP complex. The combination of XL-MS with AlphaFold-based modeling is a contemporary and appropriate approach. The focus on intrinsically disordered regions and phosphorylation as regulatory mechanisms is timely and mechanistically plausible.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
  - R1-M4
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1 (lack of validation for AlphaFold corroboration), R1-M2 (unsupported functional claims from cross-linking data), R1-M3 (phosphorylation prediction overinterpretation), R1-M4 (absence of quantitative evidence for complex assembly claims)
- **Assessment against Nature-style criteria** 
  - Originality: The abstract claims a first structural overview, which suggests novelty, but the extent of new insight beyond existing AlphaFold models is unclear.
  - Scientific importance: Trehalose synthesis is a relevant pathway for antifungal targets, and structural information could be valuable. However, the importance is diminished by the lack of demonstrated functional validation.
  - Interdisciplinary readership: The topic bridges structural biology, mass spectrometry, and fungal pathogenesis, which could attract a broad audience. The abstract is written in accessible language.
  - Technical soundness: Not assessable from the abstract alone. The absence of methodological detail and validation metrics prevents evaluation of technical rigor.
  - Readability for nonspecialists: The abstract is generally clear, though terms like "phosphatase-like domains" and "T6P accumulation" may require background knowledge.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents plausible hypotheses but does not provide sufficient data to support the mechanistic claims. A revised manuscript with detailed methods, validation, and quantitative results could change this assessment.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "Our cross-linking data corroborate the UniProt-available AlphaFold models for isolated subunits."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract states that cross-linking data corroborate AlphaFold models, but no details are given on how this corroboration was assessed. There is no mention of the number of cross-links mapped, the distance constraints used, the criteria for agreement, or any statistical or structural comparison metrics.
- **Why it matters** Corroboration of computational models with experimental data is a central claim of the study. Without defined criteria, the reader cannot judge whether the agreement is meaningful or coincidental. Overstated agreement could mislead the structural interpretation.
- **Resolution test** Provide a quantitative comparison between cross-linking-derived distance constraints and AlphaFold model predictions, including the fraction of satisfied cross-links, the distribution of violations, and a discussion of any discrepancies.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** "Intrinsically disordered regions are suggested for the regulatory subunits, while cross-linking analysis highlights the disordered N-terminus of Tsl1 as an important region in assembling the TPS/TPP complex."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The claim that the disordered N-terminus of Tsl1 is important for complex assembly is presented as a finding, but the abstract does not describe any functional experiments, mutagenesis, or assembly assays. Cross-linking data can indicate proximity or interaction interfaces, but they do not directly demonstrate functional importance in assembly.
- **Why it matters** The functional significance of the N-terminus is a key mechanistic claim. Without experimental perturbation or at least a clear structural rationale supported by data, the claim remains speculative.
- **Resolution test** Include experimental evidence such as deletion or mutation of the Tsl1 N-terminus with effects on complex formation, or provide structural modeling that shows a specific interaction interface supported by multiple cross-links and validated by independent methods.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation
- **Claim pointer** "The phosphorylation prediction indicates that Tps3-disordered regions at the N-terminus and the phosphatase-like domains are preferentially phosphorylated, triggering the inhibition of Tps2 activity and halting T6P accumulation."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract moves from phosphorylation prediction to a causal claim of inhibited Tps2 activity and halted T6P accumulation. No experimental evidence for phosphorylation status, enzyme activity, or metabolite levels is presented. The causal chain is entirely inferred from computational prediction.
- **Why it matters** This is the most significant functional claim in the abstract and has direct implications for the regulatory model. If unsupported, it overstates the study's contribution and could mislead subsequent research.
- **Resolution test** Provide experimental validation such as phosphoproteomic identification of the predicted sites, site-directed mutagenesis with activity assays, and measurement of T6P levels under the relevant conditions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "This study presents the first overview of the interactions within the Saccharomyces cerevisiae TPS/TPP complex following a 40 degrees C heat shock."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The claim of a "first overview" is a strong novelty statement, but the abstract does not provide any comparative context or a clear description of the interaction network resolved. The number of cross-links, the coverage of subunits, and the resolution of the interaction map are not stated.
- **Why it matters** Novelty is a key criterion for significance. Without a clear description of what was actually resolved, the claim cannot be evaluated, and the reader cannot assess the study's contribution relative to prior knowledge.
- **Resolution test** Clearly state the number of unique cross-links, the percentage of sequence coverage per subunit, and a summary of the interaction network, with a comparison to any prior structural or interaction data.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract wording
- **Evidence pointer** Abstract, first sentence
- **Issue** The phrase "including pathogenic fungi" is vague and does not specify which organisms or why this is relevant to the study.
- **Required correction** Specify the pathogenic fungi of interest or clarify the relevance to antifungal design in the context of the study.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodology transparency
- **Affected element** Computational modeling description
- **Evidence pointer** Abstract, methods mention
- **Issue** The abstract mentions "computational modeling" but does not specify the type of modeling beyond AlphaFold usage. It is unclear whether additional docking, molecular dynamics, or other approaches were used.
- **Required correction** Briefly specify the computational methods used, such as AlphaFold-based modeling, docking, or molecular dynamics simulations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "Phosphatase-like domains"
- **Evidence pointer** Abstract, phosphorylation prediction sentence
- **Issue** The term "phosphatase-like domains" is used without definition or context. It is unclear whether these are predicted domains, experimentally characterized regions, or homology-based assignments.
- **Required correction** Define the term or provide a brief explanation of how these domains were identified.

## Risk / unsupported claims
- The claim that cross-linking data corroborate AlphaFold models is unsupported without quantitative comparison metrics.
- The claim that the disordered N-terminus of Tsl1 is important for complex assembly is unsupported without functional or structural validation.
- The claim that phosphorylation of Tps3 regions triggers inhibition of Tps2 activity and halts T6P accumulation is unsupported without experimental evidence.
- The claim of a "first overview" of TPS/TPP complex interactions is unverifiable from the abstract alone.
- The significance statement regarding "novel antifungal strategies with reduced toxicity" is speculative and not supported by the data presented.