## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no methods, figures, tables, or supplementary material were provided for verification
- **Shared manuscript claim summary** The authors use molecular dynamics simulations to compare a negatively charged small molecule (ER) with neutral small molecules (TS1, TS0) for their ability to bind and sequester Abeta42 in monomeric and pentameric states. They report that ER is more effective, inhibits primary nucleation via an entropic expansion mechanism, and induces a decrease in hydrophobic surface area (HSA) for Abeta42 oligomers but not for Abeta40 oligomers. The HSA distinction is attributed to M35-inhibitor interactions. ER preferentially binds residues in the beta1 and beta2 regions and disrupts salt bridges involving K16, K28, and D23. The authors recommend prioritizing negatively charged inhibitors for early-stage Abeta aggregation.
- **Visible evidence base** Abstract text only; no quantitative data, simulation parameters, statistical analyses, or experimental validation details are provided
- **Missing materials affecting confidence** Full methods, simulation protocols, force field parameters, convergence criteria, error bars, statistical tests, in silico and in vitro comparative data, figures, and supplementary information

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting hypothesis regarding the superiority of negatively charged small molecules over neutral ones for targeting Abeta42 aggregation. However, the claims are broad and mechanistic, and the evidence base provided is insufficient to evaluate their validity. The absence of methodological detail, quantitative results, and statistical support prevents a rigorous assessment. The central conclusion, while plausible, is not established from the supplied material.
- **Who would be interested in the results, and why** Researchers in Alzheimer's disease drug discovery, specifically those focused on protein aggregation inhibitors, molecular dynamics simulations of intrinsically disordered proteins, and the biophysics of amyloid-beta oligomers. The work may also interest medicinal chemists designing charged small-molecule therapeutics for neurodegenerative diseases.
- **Major strengths** The hypothesis is clearly stated and addresses a gap in the field, namely the underappreciation of negatively charged inhibitors. The abstract connects simulation findings to a mechanistic rationale (entropic expansion, HSA changes, salt-bridge disruption) and distinguishes between Abeta42 and Abeta40 behavior, which adds specificity. The recommendation is actionable and could guide future experimental work.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3  
  - R1-M4  
  - R1-M5
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3  
  - R1-m4
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5
- **Assessment against Nature-style criteria**  
  - Originality: Moderate. The idea of comparing charged versus neutral small molecules is not entirely new, but the specific focus on negatively charged inhibitors as underappreciated is a useful framing.  
  - Scientific importance: Potentially high for the Alzheimer's disease community, but the importance is diminished by the lack of robust evidence in the abstract.  
  - Interdisciplinary readership: The topic bridges computational chemistry, biophysics, and neuropharmacology, which could attract a broad audience if the claims are well supported.  
  - Technical soundness: Cannot be assessed from the abstract alone. No simulation details, validation, or error analysis are provided.  
  - Readability for nonspecialists: The abstract is dense and uses specialized terminology without sufficient context, which may limit accessibility.
- **Recommendation posture** Currently not established from the provided evidence. The hypothesis is interesting, but the abstract alone does not provide sufficient methodological or quantitative support. A full manuscript with detailed methods and results would be required to evaluate the claims.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors claim that ER is "more capable of binding and sequestering" Abeta42 in pentameric and monomeric states compared to neutral TS1.  
- **Evidence pointer** Abstract text; location not provided  
- **Concern** No quantitative binding data, free energy values, or comparative metrics are presented. The claim of superior binding is stated without supporting numbers or statistical significance.  
- **Why it matters** The central conclusion depends on a demonstrable difference in binding affinity or stability, which cannot be evaluated without quantitative results.  
- **Resolution test** Provide binding free energies, dissociation constants, or occupancy measures with error bars and statistical tests comparing ER, TS1, and TS0.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors claim an "entropic expansion mechanism" for inhibition of primary nucleation pathways.  
- **Evidence pointer** Abstract text; location not provided  
- **Concern** The mechanism is named but not defined or supported by any thermodynamic decomposition, entropy calculations, or pathway analysis.  
- **Why it matters** A mechanistic claim requires evidence that entropy changes dominate the free energy profile, which is not shown.  
- **Resolution test** Present entropy and enthalpy contributions from simulations, with convergence checks and comparison to control systems.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors claim that ER-involved interactions cause a "highly visible" decrease in HSA for Abeta42 oligomers, consistent with in silico and in vitro studies.  
- **Evidence pointer** Abstract text; location not provided  
- **Concern** The HSA changes are described qualitatively ("highly visible", "undetectably") without numerical values, units, or statistical analysis. The reference to in vitro studies is unverifiable without citations or data.  
- **Why it matters** Quantitative HSA differences are central to the proposed mechanism and to the distinction between Abeta42 and Abeta40. Without numbers, the claim is anecdotal.  
- **Resolution test** Provide mean HSA values with standard deviations, effect sizes, and p-values for all conditions, and include the in vitro data or explicit references.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors attribute the HSA distinction between Abeta42 and Abeta40 to "different effects of M35-inhibitor interaction, which is analogous to the effect of M35 oxidation."  
- **Evidence pointer** Abstract text; location not provided  
- **Concern** No data on M35 interactions, oxidation comparisons, or mutational analyses are presented. The analogy to M35 oxidation is speculative without supporting evidence.  
- **Why it matters** This is a mechanistic assertion that could be tested but is currently unsupported, weakening the explanatory power of the model.  
- **Resolution test** Provide interaction profiles for M35 with each inhibitor, and ideally compare with M35-oxidized or M35-mutated systems to validate the analogy.

- **Concern ID** R1-M5  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Reproducibility  
- **Claim pointer** The authors claim ER binds residues in beta1 and beta2 regions and disrupts salt bridges involving K16, K28, and D23.  
- **Evidence pointer** Abstract text; location not provided  
- **Concern** No simulation parameters, force field, system setup, or analysis methods are described. The binding site and salt-bridge disruption claims cannot be reproduced or verified.  
- **Why it matters** Reproducibility is a core requirement for computational studies. Without methodological details, the findings cannot be independently assessed.  
- **Resolution test** Provide full methods, including force field, water model, simulation length, temperature, pressure, and analysis protocols, in the main text or supplement.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Terminology  
- **Evidence pointer** Abstract text; location not provided  
- **Issue** The term "entropic expansion mechanism" is introduced without definition or context.  
- **Required correction** Define the mechanism explicitly and explain how it differs from other proposed inhibition mechanisms.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Readability  
- **Affected element** Abstract structure  
- **Evidence pointer** Abstract text; location not provided  
- **Issue** The abstract moves rapidly between simulation results, mechanistic claims, and therapeutic recommendations, which may confuse nonspecialist readers.  
- **Required correction** Consider restructuring to separate findings, mechanistic interpretation, and implications in a clearer sequence.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** References  
- **Evidence pointer** Abstract text; location not provided  
- **Issue** The abstract mentions "in silico and in vitro studies" but does not specify which studies or provide citations.  
- **Required correction** Add explicit references or clarify that these are the authors' own unpublished data.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Precision  
- **Affected element** Language  
- **Evidence pointer** Abstract text; location not provided  
- **Issue** The phrase "more promising than the neutral ones" in the title is vague and not quantitatively defined.  
- **Required correction** Specify the metric by which ER is more promising, such as binding affinity, aggregation inhibition potency, or neuroprotective effect.

## Risk / unsupported claims
- The claim that ER is "more capable" of binding and sequestering Abeta42 is unsupported without quantitative binding data.
- The "entropic expansion mechanism" is named but not defined or evidenced.
- The HSA decrease for Abeta42 and lack thereof for Abeta40 are stated without numerical or statistical support.
- The attribution of HSA differences to M35-inhibitor interactions and the analogy to M35 oxidation are speculative.
- The binding of ER to specific residues and disruption of salt bridges is unverifiable without methodological details.
- The consistency with "in silico and in vitro studies" is unverifiable without references or data.
- The therapeutic recommendation to prioritize negatively charged inhibitors is a reasonable hypothesis but is not supported by direct experimental evidence in the abstract.