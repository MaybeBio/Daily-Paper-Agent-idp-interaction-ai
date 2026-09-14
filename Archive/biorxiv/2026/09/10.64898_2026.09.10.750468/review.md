## Review setup
- **Input scope** Full manuscript (abstract only provided)
- **Assessment boundary** Claims and evidence presented in the abstract
- **Shared manuscript claim summary** The authors report the discovery of a new class of inherently efficient SUMOylation substrates, exemplified by the BTB domain of ZBTB38, which uses a structured surface to mimic canonical linear consensus motifs and achieves catalytic efficiency comparable to the gold-standard substrate RANGAP1.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary materials provided
- **Missing materials affecting confidence** Full manuscript, including all figures, tables, experimental methods, crystallographic data, structural models, sequence alignments, kinetic data, and cellular data

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting and novel finding regarding a new class of SUMOylation substrates. However, the provided material is insufficient to evaluate the strength of the evidence, the validity of the key claims, or the technical soundness of the work. A full manuscript is required for a meaningful assessment.
- **Who would be interested in the results, and why** Researchers in the fields of post-translational modifications, ubiquitin-like proteins, SUMO biology, structural biology, and transcriptional regulation (ZBTB proteins) would be interested. The work challenges the current paradigm that efficient SUMOylation requires linear consensus motifs in disordered regions, and may have implications for understanding SUMOylation in structured domains and for identifying new substrates.
- **Major strengths** The claim of a new class of inherently efficient SUMOylation substrates is conceptually novel and potentially significant. The use of multiple complementary approaches (X-ray crystallography, structural prediction, in-vitro assays, cellular data) is a strength, if the data are robust. The comparison to the well-characterized RANGAP1 substrate provides a meaningful benchmark.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Evidence sufficiency
    - **Claim pointer** The authors claim that ZBTB38BTB possesses a dedicated surface that recapitulates the spatial arrangement of residues found in canonical linear consensus motifs and binds UBC9 with mid-micromolar affinity.
    - **Evidence pointer** Abstract; location not provided
    - **Concern** The abstract states that this claim is supported by X-ray crystallography, structural prediction, and in-vitro UBC9 interaction and SUMOylation assays. However, no data (e.g., binding curves, crystallographic structures, or structural models) are provided in the abstract. The claim of a "dedicated surface" and its specific interaction with UBC9 cannot be evaluated.
    - **Why it matters** This is the central structural claim of the paper. Without seeing the actual structural data and binding measurements, the validity of the entire mechanistic model is unverifiable.
    - **Resolution test** Provide the crystallographic structure of ZBTB38BTB (or a complex with UBC9), the structural model, and the binding data (e.g., ITC, SPR, or fluorescence anisotropy) with proper controls and error analysis.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Evidence sufficiency
    - **Claim pointer** The authors claim that the catalytic efficiency of ZBTB38BTB and ZBTB33BTB SUMOylation is closely comparable to that of the C-terminal domain of RANGAP1.
    - **Evidence pointer** Abstract; location not provided
    - **Concern** The abstract states that kinetic analyses support this claim, but no kinetic parameters (e.g., kcat, Km, kcat/Km) or reaction conditions are provided. The claim of "closely comparable" is vague and cannot be assessed without quantitative data and appropriate statistical analysis.
    - **Why it matters** This is the key quantitative claim that defines the "inherently efficient" nature of the new substrate class. Without kinetic data, the claim is unsubstantiated.
    - **Resolution test** Provide the full kinetic data (e.g., Michaelis-Menten plots, calculated kcat and Km values with errors) for ZBTB38BTB, ZBTB33BTB, and RANGAP1 under identical conditions, along with a statistical comparison.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Evidence sufficiency
    - **Claim pointer** The authors claim that structural modelling and sequence analyses suggest that this property is shared by BTB domains of five members (10%) of the ZBTB-protein family across vertebrates.
    - **Evidence pointer** Abstract; location not provided
    - **Concern** The abstract does not describe the criteria used for the sequence analysis, the structural models, or the validation of the predictions. The claim that 10% of ZBTB proteins share this property is a broad generalization that requires robust bioinformatic and structural evidence.
    - **Why it matters** This claim extends the finding from a single example to a family-wide phenomenon. Without supporting data, it remains a speculation.
    - **Resolution test** Provide the sequence alignment, the structural models for the predicted members, and the criteria (e.g., conservation of key residues, predicted surface properties) used to define the subset.

    - **Concern ID** R1-M4
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Evidence sufficiency
    - **Claim pointer** The authors claim that higher-molecular-weight, modified forms of ZBTB38 in human cells are consistent with SUMOylation.
    - **Evidence pointer** Abstract; location not provided
    - **Concern** The abstract states that such forms were observed, but no data (e.g., western blot images, controls such as SUMO-specific antibodies, knockdown/knockout of SUMO pathway components, or mass spectrometry) are provided. The claim is weak without rigorous evidence that the observed modification is indeed SUMOylation.
    - **Why it matters** This is the only cellular evidence presented. Without proper controls, the observation could be due to other modifications or artifacts.
    - **Resolution test** Provide western blot data with appropriate controls (e.g., SUMO1/2/3 antibodies, UBC9 knockdown, SUMO protease treatment, or mass spectrometry identification of the modification site).

- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity
    - **Affected element** Abstract text
    - **Evidence pointer** Abstract; location not provided
    - **Issue** The phrase "inherently efficient" is used to describe the new class of substrates, but the abstract does not clearly define what "inherently efficient" means in a quantitative or mechanistic sense.
    - **Required correction** Define "inherently efficient" explicitly, e.g., in terms of catalytic efficiency (kcat/Km) relative to known substrates, or independence from E3 ligases.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Completeness
    - **Affected element** Abstract text
    - **Evidence pointer** Abstract; location not provided
    - **Issue** The abstract mentions "E3 ligase-independent SUMOylation substrates" but does not specify whether the in-vitro assays were performed in the absence of E3 ligases.
    - **Required correction** State explicitly whether the kinetic assays were performed with or without E3 ligases.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Clarity
    - **Affected element** Abstract text
    - **Evidence pointer** Abstract; location not provided
    - **Issue** The abstract states that the findings "may facilitate the identification of further inherently efficient targets, and, potentially, the design of SUMOylation modulators." This is a speculative statement that is not supported by any data in the abstract.
    - **Required correction** Either remove or rephrase as a more cautious speculation, or provide a brief rationale for how the findings could be used for these purposes.

- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4. The core structural, kinetic, bioinformatic, and cellular claims are all unsupported by the provided material.

- **Assessment against Nature-style criteria**
    - **Originality**: Potentially high. The concept of a structured domain mimicking a linear SUMOylation motif is novel.
    - **Scientific importance**: Potentially high, if the claims are substantiated. It could change the understanding of SUMOylation substrate recognition.
    - **Interdisciplinary readership**: Moderate to high. The work bridges structural biology, biochemistry, and cell biology.
    - **Technical soundness**: Cannot be assessed from the abstract alone. The claims require rigorous experimental validation.
    - **Readability for nonspecialists**: The abstract is well-written and accessible to a broad scientific audience.

- **Recommendation posture** Currently not established from the provided evidence. The abstract presents an interesting hypothesis, but the core claims are entirely unsupported by the data provided. A full manuscript with all figures, tables, and methods is required for a proper evaluation. The recommendation would be supportive if the technical concerns are resolved with robust data.

## Risk / unsupported claims
- The claim that ZBTB38BTB possesses a dedicated surface that recapitulates the spatial arrangement of residues found in canonical linear consensus motifs and binds UBC9 with mid-micromolar affinity is unsupported.
- The claim that the catalytic efficiency of ZBTB38BTB and ZBTB33BTB SUMOylation is closely comparable to that of RANGAP1 is unsupported.
- The claim that this property is shared by five members (10%) of the ZBTB-protein family is unsupported.
- The claim that higher-molecular-weight forms of ZBTB38 in human cells are consistent with SUMOylation is unsupported.
- The claim that the findings may facilitate the identification of further inherently efficient targets and the design of SUMOylation modulators is speculative and unsupported.