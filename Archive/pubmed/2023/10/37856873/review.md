## Review setup
- **Input scope** Full manuscript text including abstract, main text, and figure references, but excluding actual figures and supplementary material.
- **Assessment boundary** Evaluation is limited to the scientific claims, methodology, and interpretations presented in the provided text. No assessment of data quality beyond what is described in the text.
- **Shared manuscript claim summary** The authors use coarse-grained molecular simulations of hydrophobic homopolymers and two natural IDPs (FUS LC, LAF-1 RGG) to show that polymer chains become compact at droplet interfaces, chain ends are enriched at the interface, and most segments orient tangentially while ends tend perpendicular. These findings are proposed as general principles for IDP behavior in biomolecular condensates.
- **Visible evidence base** Text descriptions of simulation results, including radius of gyration distributions, contact analysis, segmental analysis, orientation angles, and comparisons to bulk systems. Figures referenced but not directly viewable.
- **Missing materials affecting confidence** Actual figures, simulation parameters, force field details, system sizes, equilibration protocols, and statistical error analysis are not provided in the visible text. Supplementary material is referenced but not available for review.

## Reviewer
- **Overall assessment** The manuscript presents a systematic computational study of polymer conformations at droplet interfaces, addressing an important gap in understanding IDP behavior in biomolecular condensates. The work builds logically on prior studies and offers a clear conceptual model. However, the evidence as presented in text form is insufficient to fully evaluate the robustness of the claims, particularly regarding statistical significance, model transferability, and the interpretation of orientation data. The study is potentially valuable but requires additional detail and analysis to establish its conclusions firmly.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, intrinsically disordered proteins, and polymer physics at interfaces. The findings could inform understanding of surface properties of condensates, which are increasingly recognized as functionally important. The use of simple polymer models to extract general principles will appeal to theorists and experimentalists seeking mechanistic insight.
- **Major Strengths** The study addresses a timely and important question about conformational behavior at condensate interfaces. The use of a minimal homopolymer model to extract general principles is elegant and complements prior lattice-based work. The segmental analysis provides a more detailed picture than chain-level descriptions alone. The extension to two natural IDPs strengthens the generality of the conclusions. The proposed model in Figure 4 offers a clear conceptual framework.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
  - R1-M4
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
  - R1-m4
  - R1-m5
- **Technical failings that need to be addressed before the case is established** R1-M1 (statistical robustness), R1-M2 (model transferability), R1-M3 (orientation interpretation)
- **Assessment against Nature-style criteria** Originality is moderate; the question is important but builds directly on prior work by Farag et al. Scientific importance is potentially high given the functional relevance of condensate interfaces. Interdisciplinary readership is plausible, spanning soft matter physics, biophysics, and cell biology. Technical soundness cannot be fully assessed from text alone, but the methodology appears appropriate. Readability for nonspecialists is good, with clear explanations of concepts, though some terms assume familiarity with polymer physics.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding statistical robustness and model transferability. The core conceptual model is appealing, but the evidence as presented is not yet fully convincing.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical robustness
- **Claim pointer** The authors claim that Rg distributions shift to smaller values at the interface and that segmental Rg exhibits nonmonotonic trends for short end segments.
- **Evidence pointer** Figure 2a, Figure 3c, Figure 3d, location not provided
- **Concern** The manuscript reports differences in Rg distributions and segmental Rg values between interface and interior regions, but no statistical error bars, confidence intervals, or replicate information are provided in the text. It is unclear how many independent simulations were performed, how many chains were averaged, or whether the observed differences are statistically significant given the expected thermal fluctuations.
- **Why it matters** Without statistical analysis, the reported conformational differences could arise from insufficient sampling or finite-size effects rather than genuine physical behavior. This is particularly critical for the subtle nonmonotonic trends in short segment Rg, which may be within noise.
- **Resolution test** Provide error bars or confidence intervals for all reported Rg values, specify the number of independent simulation runs and chains sampled, and perform statistical tests (e.g., bootstrap or block averaging) to confirm that the observed differences are significant.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Model transferability
- **Claim pointer** The authors claim that findings from hydrophobic homopolymers translate to natural IDPs, specifically FUS LC and LAF-1 RGG.
- **Evidence pointer** Figure 5, location not provided
- **Concern** The homopolymer model is purely hydrophobic, while FUS LC and LAF-1 RGG have complex sequence-specific interactions including charged, aromatic, and polar residues. The HPS-Urry model used for the natural proteins is distinct from the homopolymer model. The text states that similar trends hold for the natural proteins, but no quantitative comparison is shown. It is unclear whether the compaction magnitude, segmental enrichment, or orientation preferences are quantitatively similar or merely qualitatively consistent.
- **Why it matters** The central claim of the paper is that simple polymer models capture general principles applicable to real IDPs. If the transferability is only qualitative or if the natural proteins show different magnitudes of effects, the generality of the conclusions is weakened.
- **Resolution test** Provide a direct quantitative comparison between homopolymer and natural protein results, including Rg values, segmental enrichment profiles, and orientation distributions. Discuss any differences in magnitude or trend and their implications for the proposed model.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation of orientation data
- **Claim pointer** The authors claim that chain ends tend to align perpendicular to the interface while the majority of segments remain tangential.
- **Evidence pointer** Figure 3e, Figure S4, location not provided
- **Concern** The orientation analysis relies on the angle θ between the segment-to-droplet COM vector and the segment end-to-end vector. The interpretation of "perpendicular" and "tangential" depends on the definition of the reference vector and the treatment of the droplet curvature. For finite-size segments at a curved interface, the geometric relationship between the segment vector and the radial direction may be more complex than implied. The text states that angles close to π correspond to perpendicular, but the maximum observed angles are described as "closer to the isotropic value than perpendicular," suggesting the effect is weak. The claim that ends "tend to align perpendicular" may be overstated given the modest deviation from isotropy.
- **Why it matters** The orientation preference is a key part of the proposed model. If the effect is weak or the interpretation is ambiguous, the conceptual model may need revision.
- **Resolution test** Provide a more detailed analysis of the orientation distributions, including the full angular distribution rather than just average values. Clarify the geometric definitions and consider whether the observed angles are significantly different from isotropic expectations. Discuss the magnitude of the effect in the context of the proposed model.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Comparison to prior work
- **Claim pointer** The authors state that Farag et al. reported chains being most expanded at the interface and oriented perpendicular, which contrasts with the current findings of compaction and predominantly tangential orientation.
- **Evidence pointer** Main text, paragraph 3, location not provided
- **Concern** The discrepancy with prior lattice-based Monte Carlo simulations by Farag et al. is mentioned but not discussed in detail. The authors do not explain why their off-lattice model might yield different results, whether the difference arises from model resolution, interaction details, or analysis methods. This is a significant unresolved issue that bears on the validity of the current conclusions.
- **Why it matters** A direct contradiction with prior published work requires explicit discussion and resolution. Without addressing this, readers cannot assess which result is more reliable or what conditions lead to different behaviors.
- **Resolution test** Add a dedicated discussion section comparing the current results with Farag et al., identifying potential sources of discrepancy (e.g., model resolution, interaction range, system size, analysis definitions) and explaining why the current findings should be considered more reliable or applicable to specific conditions.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Simulation details
- **Evidence pointer** Main text, paragraph 4, location not provided
- **Issue** The text states that model details are provided in the Supporting Information, but key parameters such as chain length, number of chains, box size, and simulation time are not mentioned in the main text. This makes it difficult to assess the relevance and scale of the simulations.
- **Required correction** Include key simulation parameters in the main text or provide a summary table, including chain length, number of chains, system size, and simulation duration.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Definition of interface region
- **Affected element** Interface width and positioning
- **Evidence pointer** Figure 1, location not provided
- **Issue** The interface region is defined by fitting the concentration profile to a hyperbolic tangent function, but the exact boundaries of the "interface region" used for analysis are not specified. It is unclear how the interface width δ is used to assign chains to the interface versus interior.
- **Required correction** Clearly define the criteria for assigning chains or segments to the interface region, including the range of dCOM values considered and how the interface width is used.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical sampling
- **Affected element** Number of chains and time averaging
- **Evidence pointer** Figure 2, location not provided
- **Issue** The number of chains used for averaging Rg distributions is not stated. Given that the droplet contains many chains, it is important to know how many were sampled and whether the distributions are converged.
- **Required correction** Specify the number of chains included in the analysis and the time period over which averages were computed.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "Expanded" vs "compact" at interface
- **Evidence pointer** Abstract and main text, location not provided
- **Issue** The abstract states chains become "compact" at the interface, but the discussion of short segments mentions they are "more expanded" than middle segments. This could confuse readers about the overall trend.
- **Required correction** Clarify that the chain-level compaction is driven by middle segments, while end segments may behave differently. Use consistent terminology throughout.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Generalizability
- **Affected element** Sequence-specific effects
- **Evidence pointer** Main text, final paragraph, location not provided
- **Issue** The authors acknowledge that charged IDPs may behave differently, but this caveat is brief. Given the growing interest in sequence-specific phase behavior, a more explicit statement about the limits of the homopolymer model would be helpful.
- **Required correction** Expand the discussion of how sequence complexity, charge patterning, or aromatic content might alter the interfacial conformational preferences.

## Risk / unsupported claims
- The claim that "chain ends are enriched at the interface to maximize conformational entropy" is presented as an explanation but is not directly tested or supported by free energy calculations.
- The statement that "the majority of chain segments lie tangential to the droplet surface" is based on average angles but the full distribution is not shown, making it difficult to assess the strength of this preference.
- The transferability of homopolymer findings to FUS LC and LAF-1 RGG is asserted but not quantitatively demonstrated in the visible text.
- The speculation that lower monomer concentration at the interface leads to decreased solvent quality and chain collapse is plausible but not directly tested.
- The comparison with Farag et al. is mentioned but not analyzed, leaving the discrepancy unresolved.