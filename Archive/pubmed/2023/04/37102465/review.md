## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no access to full methods, figures, tables, or supplementary data
- **Shared manuscript claim summary** The authors report a computational-experimental pipeline for designing linear and stapled cyclic peptide mimotopes that mimic the hotspot residues of the EGFR third subdomain (TSD) recognized by monoclonal antibodies. They claim that a consistent binding mode exists across EGFR TSD-mAb complexes, that identified hotspot residues contribute about half of the binding potency, that OTTS-designed linear peptides are intrinsically disordered, that disulfide stapling constrains them into a double-stranded conformation, and that stapling improves binding affinity by a reported fold-change with agreement between empirical scoring and fluorescence assay.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or numerical data beyond the stated fold-change
- **Missing materials affecting confidence** Full methods, structural analysis details, hotspot residue identification criteria, peptide sequences, stapling chemistry specifics, binding assay protocols, statistical analysis, and all quantitative results

## Reviewer
- **Overall assessment** The abstract presents a plausible and potentially useful strategy for peptide mimotope design targeting EGFR TSD. However, the evidence base is insufficient to evaluate the core claims. The central quantitative claim of binding affinity improvement is presented without a specific value, and the agreement between empirical scoring and fluorescence assay is asserted without data. The structural claims about stapled peptides adopting a native-like conformation are not supported by any presented experimental or computational validation. The work may be of interest to the peptide engineering and antibody mimicry community, but the case is not established from the supplied material.
- **Who would be interested in the results, and why** Researchers in peptide-based therapeutics, antibody mimetic design, and computational protein engineering would be interested. The OTTS strategy combined with stapling could offer a generalizable approach for mimicking protein surface epitopes, which is relevant to targeted cancer therapy and diagnostic reagent development.
- **Major strengths** The abstract identifies a clear biological problem and proposes a rational design workflow that integrates structural analysis, computational design, and experimental validation. The focus on hotspot residues and the use of stapling to address conformational disorder is a logical and potentially impactful approach.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
  - R1-M4
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** 
  - Originality: The combination of OTTS design with chemical stapling for EGFR TSD mimotopes is somewhat novel, but the individual components are established. The abstract does not demonstrate a conceptual advance beyond existing peptide stapling and mimotope design literature.
  - Scientific importance: EGFR targeting is clinically relevant, and improved peptide mimotopes could have therapeutic or diagnostic value. However, the abstract does not show functional relevance beyond binding affinity, limiting the perceived importance.
  - Interdisciplinary readership: The work bridges structural biology, computational design, and biochemistry, which could appeal to a broad audience. However, the abstract is too technical and lacks accessible context for nonspecialists.
  - Technical soundness: Not assessable from the abstract. The lack of specific data, controls, and statistical details prevents evaluation of the methods and conclusions.
  - Readability for nonspecialists: The abstract uses jargon and formula placeholders without explanation, making it difficult for a general scientific audience to follow the logic or significance.
- **Recommendation posture** Currently not established from the provided evidence. The abstract suggests a potentially useful approach, but the core claims are unsupported or unquantified. A full manuscript with detailed methods and results would be required to assess technical soundness and significance.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative claim
- **Claim pointer** The abstract states that stapling improves binding affinity by a fold-change, with the value replaced by a formula placeholder.
- **Evidence pointer** Abstract, binding affinity statement; location not provided
- **Concern** The fold-change in binding affinity is not specified. The placeholder "[Formula: see text]-fold" prevents any assessment of the magnitude or significance of the improvement.
- **Why it matters** The central quantitative claim of the study is the affinity enhancement from stapling. Without a specific value, the reader cannot judge whether the improvement is meaningful, reproducible, or comparable to existing approaches.
- **Resolution test** Provide the exact fold-change with confidence intervals and statistical significance from the fluorescence assay, along with the number of replicates.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence for agreement
- **Claim pointer** The abstract claims that empirical scoring and fluorescence assay reached an agreement on the effectiveness of stapling.
- **Evidence pointer** Abstract, agreement statement; location not provided
- **Concern** No data are presented to support the claimed agreement. It is unclear whether the agreement is qualitative, quantitative, or statistical, and whether it applies to all tested mAbs or only a subset.
- **Why it matters** Agreement between computational prediction and experimental measurement is a key validation of the design strategy. Without evidence, the claim is unverifiable and the reliability of the computational approach is not established.
- **Resolution test** Show a correlation plot or table comparing empirical scores and experimental binding affinities for all peptide-mAb pairs, with statistical measures of agreement.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Structural claim
- **Claim pointer** The abstract claims that stapled cyclic peptide mimotopes spontaneously fold into a double-stranded conformation that threads through all hotspot residues and exhibits a consistent binding mode with the TSD hotspot site.
- **Evidence pointer** Abstract, conformational analysis statement; location not provided
- **Concern** The structural claim is based on "conformational analysis," but no method is specified. It is unclear whether this is computational modeling, experimental structure determination, or a combination. No structural data are presented.
- **Why it matters** The functional relevance of the stapled peptides depends on their ability to adopt a native-like conformation. Without experimental structural evidence, the claim that the peptides mimic the TSD binding mode is speculative.
- **Resolution test** Provide experimental structural data, such as NMR or X-ray structures of the stapled peptides, or at minimum, detailed computational models with validation against known TSD-mAb structures.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Hotspot contribution
- **Claim pointer** The abstract claims that several hotspot residues contribute about half of the total binding potency of mAbs to TSD.
- **Evidence pointer** Abstract, hotspot residue statement; location not provided
- **Concern** The basis for this quantitative claim is not described. No mutagenesis data, alanine scanning, or computational energy calculations are referenced.
- **Why it matters** The design of mimotopes relies on the identification of hotspot residues. If the contribution estimate is not robust, the design rationale is weakened.
- **Resolution test** Present experimental alanine scanning data or computational alanine scanning with validation, showing the per-residue contribution to binding free energy.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract, first sentence
- **Evidence pointer** Abstract, opening statement; location not provided
- **Issue** The phrase "malignant proliferation" is vague and could be more specific, such as "tumor cell proliferation."
- **Required correction** Revise to "tumor cell proliferation" or a more precise biological description.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract, "orthogonal threading-through-strand (OTTS) strategy"
- **Evidence pointer** Abstract, OTTS description; location not provided
- **Issue** The term "orthogonal" is not defined in the context of peptide design, which may confuse readers unfamiliar with the strategy.
- **Required correction** Provide a brief explanation of what "orthogonal" means in this design context, or use a more descriptive term.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Abstract, "empirical scoring"
- **Evidence pointer** Abstract, scoring method; location not provided
- **Issue** The type of empirical scoring is not specified, making it difficult to assess the method's validity.
- **Required correction** Name the specific scoring function or method used, and reference it appropriately.

## Risk / unsupported claims
- The fold-change in binding affinity is unquantified and cannot be evaluated.
- The agreement between empirical scoring and fluorescence assay is asserted without data.
- The structural claim that stapled peptides adopt a native-like double-stranded conformation is unsupported by any presented evidence.
- The hotspot residue contribution of "about half" of binding potency is not substantiated.
- The claim that linear peptides are "intrinsically disordered" is stated without experimental evidence such as circular dichroism or NMR.
- The "consistent binding mode" across EGFR TSD-mAb complexes is described qualitatively without structural superposition data or statistical analysis.