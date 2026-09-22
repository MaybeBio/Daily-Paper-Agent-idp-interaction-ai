## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no figures, methods, or supplementary material were provided
- **Shared manuscript claim summary** The authors use coarse-grained molecular dynamics simulations to argue that negative surface charge of karyopherins (Kaps) is essential for transport through the nuclear pore complex (NPC), that Kap hydrophobicity aids translocation, and that the positive net charge of nuclear FG-Nups, particularly Nup1, is instrumental for transport, supporting a cytoplasmic-to-nuclear gradient of increasing Kap-FG-Nup binding affinity.
- **Visible evidence base** Abstract text only; no quantitative results, simulation parameters, or statistical analyses are available
- **Missing materials affecting confidence** Full manuscript, methods section, simulation details, all figures and tables, quantitative transport rate data, and any comparison with experimental or prior computational results

## Reviewer
- **Overall assessment** The abstract presents a plausible and potentially interesting computational study on the role of electrostatic and hydrophobic interactions in Kap transport through the NPC. However, the claims are stated without quantitative support, and the abstract alone does not allow assessment of the robustness of the simulation methodology, the statistical significance of the findings, or the generalizability of the conclusions. The central claim that negative Kap charge is "essential" and that Nup1 positive charge is "instrumental" requires careful validation against alternative mechanisms and parameter sensitivity, none of which can be evaluated from the supplied material.
- **Who would be interested in the results, and why** Researchers in nucleocytoplasmic transport, intrinsically disordered proteins, and computational biophysics would be interested. The study addresses a long-standing debate on Kap translocation mechanisms and proposes a specific electrostatic gradient hypothesis that could inform experimental designs and future modeling efforts.
- **Major strengths** The study tackles a mechanistically important and unresolved question in NPC biology. The use of coarse-grained molecular dynamics is appropriate for the length and time scales involved. The focus on Kap surface charge and hydrophobicity, as well as the specific attention to Nup1, provides a testable hypothesis that connects simulation to prior proposals of a binding affinity gradient.
- **Major Concerns**  
  - **Concern ID** R1-M1  
    **Severity** Major  
    **Blocking** Yes  
    **Axis** Technical soundness  
    **Claim pointer** "We found that the negative charge of the Kaps is essential for transport"  
    **Evidence pointer** Abstract, location not provided  
    **Concern** The claim that negative Kap charge is "essential" is presented without any quantitative data, such as transport rates for charge-neutralized or charge-reversed Kap variants, or a demonstration that the effect is not an artifact of the specific coarse-grained model or force field parameters.  
    **Why it matters** The word "essential" implies a binary requirement, which is a strong claim. Without evidence of a systematic parameter sweep or control simulations, the conclusion may be model-dependent and not generalizable to real NPC transport.  
    **Resolution test** Provide quantitative transport rate comparisons for Kap variants with altered charge distributions, including neutral and reversed charge states, and demonstrate that the effect is robust across reasonable variations in simulation parameters and FG-Nup compositions.  
  - **Concern ID** R1-M2  
    **Severity** Major  
    **Blocking** Yes  
    **Axis** Technical soundness  
    **Claim pointer** "the positive net charge of the nuclear Nups (especially Nup1) is instrumental for the transport of Kaps"  
    **Evidence pointer** Abstract, location not provided  
    **Concern** The specific role of Nup1 is highlighted, but no data are shown to distinguish Nup1 from other nuclear FG-Nups or to establish that the effect is due to net charge rather than other sequence-specific features such as FG-repeat spacing or hydrophobicity.  
    **Why it matters** Attributing the effect to net charge alone may be an oversimplification. If the conclusion is to support a gradient hypothesis, it must be shown that the charge effect is separable from other Nup properties and that the gradient is quantitatively correlated with transport enhancement.  
    **Resolution test** Include simulations with Nup1 charge mutations, Nup1 depletion, or chimeric Nups to isolate the charge contribution, and provide a quantitative correlation between Nup charge and transport rate across multiple nuclear Nups.  
  - **Concern ID** R1-M3  
    **Severity** Major  
    **Blocking** No  
    **Axis** Scientific importance  
    **Claim pointer** "revealing a (previously proposed) gradient of increasing binding affinity of the Kaps with FG-Nups from the cytoplasm to the nucleus"  
    **Evidence pointer** Abstract, location not provided  
    **Concern** The abstract claims to reveal a previously proposed gradient, but no comparison with prior experimental or computational data is provided. It is unclear whether the simulation results are consistent with or contradict existing measurements of Kap-FG-Nup binding affinities.  
    **Why it matters** The novelty and significance of the finding depend on how it relates to prior work. Without a quantitative comparison, the claim of "revealing" a gradient is not substantiated.  
    **Resolution test** Provide a direct comparison of simulated binding affinities or transport rates with published experimental or computational values for the same or similar Kap-Nup pairs, and discuss any discrepancies.
- **Minor Comments**  
  - **Concern ID** R1-m1  
    **Severity** Minor  
    **Axis** Readability for nonspecialists  
    **Affected element** Abstract  
    **Evidence pointer** Abstract, location not provided  
    **Issue** The abstract uses terms such as "coarse-grained molecular dynamics" and "FG-Nups" without brief definitions, which may limit accessibility for readers outside the immediate field.  
    **Required correction** Add a brief parenthetical explanation of coarse-grained molecular dynamics and define FG-Nups as phenylalanine-glycine nucleoporins at first mention.  
  - **Concern ID** R1-m2  
    **Severity** Minor  
    **Axis** Technical soundness  
    **Affected element** Abstract  
    **Evidence pointer** Abstract, location not provided  
    **Issue** The abstract states that "Kap hydrophobicity of the transport particle aids in the translocation" but does not specify whether this is a separate effect from charge or an interaction between the two properties.  
    **Required correction** Clarify whether hydrophobicity and charge act independently or synergistically, and state the magnitude of the effect relative to the charge effect.  
  - **Concern ID** R1-m3  
    **Severity** Minor  
    **Axis** Scientific importance  
    **Affected element** Abstract  
    **Evidence pointer** Abstract, location not provided  
    **Issue** The abstract does not mention the size range of cargos tested or whether the findings apply to both passive diffusion and facilitated transport regimes.  
    **Required correction** Specify the cargo sizes and transport regimes studied to clarify the scope of the conclusions.
- **Technical failings that need to be addressed before the case is established** R1-M1 and R1-M2 are blocking because the central claims of charge essentiality and Nup1 instrumentality are not supported by quantitative evidence in the supplied material. R1-M3 is non-blocking but requires additional comparative analysis to establish the novelty of the gradient claim.
- **Assessment against Nature-style criteria**  
  - Originality: The hypothesis of a charge-based gradient is not entirely new, as the abstract acknowledges prior proposal, but the specific simulation approach may offer a fresh perspective. However, originality cannot be fully assessed without seeing the full context of prior work.  
  - Scientific importance: The question of Kap transport mechanisms is of high importance to the NPC field, and a robust computational demonstration could have broad implications. The current abstract does not yet establish this importance quantitatively.  
  - Interdisciplinary readership: The topic bridges cell biology, biophysics, and computational biology, but the abstract is written in a way that may be too specialized for a general interdisciplinary audience.  
  - Technical soundness: Cannot be evaluated from the abstract alone. The lack of methodological detail and quantitative results is a major limitation.  
  - Readability for nonspecialists: The abstract is concise but uses jargon without explanation, which reduces accessibility.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents an interesting hypothesis, but the absence of quantitative data and methodological detail prevents validation of the central claims. I would be supportive if the full manuscript provides robust simulation evidence, parameter sensitivity analyses, and comparisons with prior work.

## Risk / unsupported claims
- The claim that negative Kap charge is "essential" for transport is unsupported without quantitative transport rate data for charge variants.
- The claim that Nup1 positive charge is "instrumental" is unsupported without data isolating Nup1 from other nuclear Nups.
- The claim of revealing a binding affinity gradient is unsupported without comparison to prior experimental or computational data.
- The relative contribution of hydrophobicity versus charge is not quantified and cannot be assessed.
- The applicability of the findings to different cargo sizes or transport regimes is not stated and cannot be evaluated.