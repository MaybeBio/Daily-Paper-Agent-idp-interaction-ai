## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the supplied abstract
- **Shared manuscript claim summary** The authors analyse human protein sequences lacking the charged residues Asp, Glu, Lys, and Arg (termed charge-absent regions) and report that such regions are longer on average in scaffold proteins involved in liquid-liquid phase separation (LLPS), are enriched in Ala, Gly, Pro, and Ser, have relatively high hydropathy scores, and may facilitate condensation through homomeric interactions due to reduced charged group desolvation energy and hydrophobic composition.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or statistical details provided
- **Missing materials affecting confidence** Full manuscript, sequence datasets, statistical analyses, definitions of charge-absent regions, annotation criteria for LLPS involvement, clustering methodology, and any experimental validation

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting bioinformatic observation linking charge-absent sequence regions to LLPS scaffold proteins. However, the evidence base is limited to a summary with no quantitative details, no methodological description, and no validation. The central claims are plausible but currently not assessable for robustness or generalisability. The hypothesis regarding desolvation energy and homomeric interactions is speculative and lacks direct support.
- **Who would be interested in the results, and why** Researchers studying protein phase separation, particularly those interested in sequence determinants of condensate formation, protein engineering for modulating LLPS, and biophysical chemistry of intrinsically disordered regions. The potential link to pH-sensing engineering could also interest synthetic biologists and protein designers.
- **Major strengths** The abstract addresses a clear gap in the LLPS field by focusing on charge-absent regions rather than charge neutralisation. The distinction between scaffold and non-scaffold proteins is a useful framing. The hypothesis is mechanistically motivated and testable.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality is moderate; the focus on charge-absent regions is a novel angle but builds on extensive existing LLPS sequence analyses. Scientific importance is potentially high if the findings are robust and generalisable, but the abstract does not establish this. Interdisciplinary readership is plausible given the biophysical and protein engineering implications. Technical soundness cannot be evaluated from the abstract alone. Readability for nonspecialists is adequate but the abstract assumes familiarity with LLPS terminology.
- **Recommendation posture** Currently not established from the provided evidence. Supportive if the full manuscript provides rigorous statistical analysis, clear definitions, and validation of the hypothesis.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical robustness
- **Claim pointer** "Scaffold proteins, central to condensate formation, on average possess longer charge-absent regions than those not key for LLPS."
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract reports a difference in average length of charge-absent regions between scaffold and non-scaffold proteins but provides no effect size, variance, sample size, statistical test, or significance threshold. Without these, the claim cannot be evaluated for reliability or biological relevance.
- **Why it matters** The central conclusion of the paper rests on this comparison. A weak or confounded difference could arise from sequence length biases, protein family composition, or annotation quality, none of which are addressed.
- **Resolution test** Provide the full statistical analysis including distributions, confidence intervals, effect sizes, and appropriate controls for confounding variables such as protein length and sequence composition.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Definitional clarity
- **Claim pointer** "sequences within human proteins that lack the charge-bearing residues Asp, Glu, Lys, and Arg (termed charge-absent) are analysed"
- **Evidence pointer** Abstract; location not provided
- **Concern** The definition of a charge-absent region is ambiguous. It is unclear whether these are contiguous stretches with zero charged residues, windows of a certain length, or regions with a threshold frequency. The minimum length threshold for a "region" is not stated. This ambiguity affects all downstream analyses.
- **Why it matters** Without a precise operational definition, the results cannot be reproduced or compared with other sequence features. Different definitions could yield substantially different sets of regions and alter the reported enrichment patterns.
- **Resolution test** State the exact algorithm for defining charge-absent regions, including length thresholds, gap handling, and whether charged residues at boundaries are excluded.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Hypothesis support
- **Claim pointer** "a lack of charged group desolvation energy, together with a relatively hydrophobic sequence composition, may facilitate condensation through homomeric interactions"
- **Evidence pointer** Abstract; location not provided
- **Concern** The hypothesis is presented as a plausible mechanism but no direct evidence is provided. The abstract does not report any experiments, simulations, or quantitative biophysical measurements linking charge-absent regions to desolvation energetics or homomeric interactions. The connection to pH-sensing is also speculative.
- **Why it matters** The hypothesis is the proposed explanatory framework for the observed sequence patterns. Without any validation, it remains an untested conjecture, which limits the paper's impact and the utility of the findings for engineering.
- **Resolution test** Provide experimental or computational evidence, such as mutagenesis of charge-absent regions, measurements of phase separation under varying pH, or molecular simulations of homomeric interactions, that directly tests the proposed mechanism.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of reporting
- **Affected element** Amino acid enrichment claim
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states that charge-absent regions are enriched in Ala, Gly, Pro, and Ser, but does not specify the baseline used for enrichment (e.g., human proteome average, disordered region average, or random expectation).
- **Required correction** Specify the reference set and the statistical method used to determine enrichment.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Generalisability
- **Affected element** Scope of analysis
- **Evidence pointer** Abstract; location not provided
- **Issue** The analysis is limited to human proteins. It is unclear whether the findings are specific to humans or generalisable across eukaryotes, which would affect the broader relevance of the claim.
- **Required correction** State whether the analysis was extended to other species or justify the human-only focus.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Use of "scaffold proteins"
- **Evidence pointer** Abstract; location not provided
- **Issue** The term "scaffold proteins" is used without a clear definition of how LLPS involvement was annotated. Different databases or criteria could classify proteins differently.
- **Required correction** Provide the annotation source and criteria used to define scaffold proteins and LLPS involvement.

## Risk / unsupported claims
- The claim that charge-absent regions are longer in scaffold proteins is unsupported without statistical details.
- The claim that charge-absent regions are enriched in specific amino acids is unsupported without a defined baseline.
- The claim that charge-absent regions may facilitate condensation through desolvation and hydrophobic interactions is speculative and not supported by any direct evidence in the abstract.
- The claim that modulation through pH-sensing is feasible is speculative and not supported by any data.