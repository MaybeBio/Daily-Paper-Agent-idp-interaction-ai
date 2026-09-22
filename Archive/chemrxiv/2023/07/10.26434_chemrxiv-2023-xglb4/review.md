## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no methods, figures, or supporting data were available for evaluation
- **Shared manuscript claim summary** The authors report that N-methylation of the peptide backbone in intrinsically disordered SUMO-interacting motifs (SIMs) restricts accessible conformations, predisposing these peptides for recognition by SUMO proteins. They claim that backbone N-methylation at appropriate positions increases binding affinity through faster target binding, as evidenced by fluorescence anisotropy, relaxation-based NMR experiments, and computational analysis. They further propose that the enhanced affinity arises from an increase in the energy of the unbound state and a reduction in the entropic contribution to binding and activation energies, offering a new paradigm for peptide-based PPI modulator design.
- **Visible evidence base** Abstract text only; no figures, tables, experimental protocols, or numerical data were provided
- **Missing materials affecting confidence** Full manuscript text, all figures and tables, experimental methods, NMR data and analysis details, fluorescence anisotropy measurements, computational methods and parameters, statistical analyses, and any supporting information

## Reviewer
- **Overall assessment** The abstract presents a conceptually interesting approach to a challenging problem in chemical biology, namely the targeting of β-strand-mediated protein-protein interactions using backbone-modified intrinsically disordered peptides. The central hypothesis, that N-methylation can pre-organize disordered sequences for binding, is plausible and potentially valuable. However, the abstract provides insufficient experimental and computational detail to assess the validity of the claims. Key quantitative results, control experiments, and methodological rigor cannot be evaluated from the supplied material. The mechanistic interpretation, particularly the energetic decomposition, requires substantially more evidence than is presented here.
- **Who would be interested in the results, and why** Researchers in chemical biology, peptide chemistry, and drug discovery would be interested in this work as it addresses a gap in strategies for modulating β-strand-mediated PPIs. The biophysical community studying intrinsically disordered proteins and their binding mechanisms may also find the energetic analysis of interest. Additionally, those working on SUMO biology and SUMO-SIM interactions specifically would be a relevant audience.
- **Major strengths** The work addresses an underexplored area, namely β-strand-mediated interactions, which contrasts with the more extensively studied α-helical systems. The combination of experimental biophysics (fluorescence anisotropy, NMR) with computational analysis is appropriate for the questions posed. The proposed mechanistic insight, that affinity gains arise from destabilization of the unbound state rather than stabilization of the bound complex, is conceptually interesting and potentially generalizable.
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
  Originality: The concept of using backbone N-methylation to pre-organize β-strand sequences is not entirely new, as N-methylation has been used in other peptide contexts, but its application to intrinsically disordered SIMs and the specific mechanistic claim regarding unbound state energetics may offer a fresh perspective. However, the abstract does not clearly differentiate this work from prior uses of N-methylation in peptide design.  
  Scientific importance: If the claims are fully substantiated, the work could provide a useful design principle for targeting a class of PPIs that is currently underexploited. The potential impact is moderate to high, but the current evidence base is insufficient to judge.  
  Interdisciplinary readership: The topic bridges chemistry, biophysics, and structural biology, and would likely appeal to a broad readership if the results are robust and clearly presented.  
  Technical soundness: Cannot be assessed from the abstract alone. The reliance on multiple techniques is encouraging, but no data are shown to verify the claims.  
  Readability for nonspecialists: The abstract is reasonably clear for a specialist audience, but the mechanistic statements are dense and would benefit from more explicit explanation of the energetic concepts for a broader readership.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents an interesting hypothesis and preliminary claims, but the absence of any supporting data, methodological detail, or quantitative results means that the core conclusions cannot be evaluated. A supportive posture would require access to the full manuscript and verification of the experimental and computational evidence.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** The authors claim that N-methylation of the peptide backbone "effectively restrict[s] accessible peptide conformations, predisposing them for protein recognition" and that this results in "faster target binding, and thus higher affinity."  
- **Evidence pointer** Abstract only; no figures or tables provided  
- **Concern** The abstract states that N-methylation restricts conformations and increases binding affinity, but no quantitative data are presented. No binding constants, kinetic rates, or conformational measurements are shown. The claim that "faster target binding" leads to higher affinity is not supported by any numerical values or statistical comparisons.  
- **Why it matters** Without quantitative binding data, the central claim of enhanced affinity cannot be verified. The relationship between faster binding and higher affinity is also not self-evident, as affinity is determined by both association and dissociation rates. The abstract does not address whether dissociation rates are affected.  
- **Resolution test** Provide binding affinities (e.g., Kd values) and kinetic rate constants (kon and koff) for unmodified and N-methylated peptides, with appropriate replicates and statistical analysis. Show that the observed affinity changes are statistically significant and consistent across multiple peptide variants.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Mechanistic interpretation  
- **Claim pointer** The authors claim that "higher affinities occur as a consequence of an increase in the energy of the unbound state, and a reduction in the entropic contribution to the binding and activation energies."  
- **Evidence pointer** Abstract only; no thermodynamic or kinetic data provided  
- **Concern** The energetic decomposition presented is a strong mechanistic claim that requires rigorous thermodynamic and kinetic measurements. The abstract does not describe how these energies were determined, what model was used, or what assumptions were made. The claim that the unbound state energy increases is particularly unusual and requires careful validation.  
- **Why it matters** If the proposed mechanism is incorrect, the design principle derived from it would be misleading for future applications. The energetic interpretation is central to the novelty of the work and must be supported by robust data.  
- **Resolution test** Provide a detailed thermodynamic analysis, such as van't Hoff or isothermal titration calorimetry data, and a clear description of the computational methods used to derive energy components. Show that the proposed energetic model is consistent with all experimental data and that alternative interpretations have been considered and excluded.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Methodological transparency  
- **Claim pointer** The authors state that "fluorescence anisotropy, relaxation-based NMR experiments, and computational analysis" were used to support their conclusions.  
- **Evidence pointer** Abstract only; no methods section or data provided  
- **Concern** No experimental details are given for any of the techniques mentioned. For fluorescence anisotropy, the labeling strategy, peptide concentrations, and binding partner concentrations are not described. For NMR, the specific relaxation experiments, the nuclei observed, and the analysis approach are not specified. For computational analysis, the methods, force fields, and simulation times are absent.  
- **Why it matters** Reproducibility is a fundamental requirement for scientific claims. Without methodological detail, the results cannot be replicated or independently verified. The absence of this information prevents assessment of whether the techniques were applied appropriately.  
- **Resolution test** Provide a complete methods section with sufficient detail for each technique, including sample preparation, instrument parameters, data processing, and analysis protocols. If the full manuscript contains this information, the abstract should reference it clearly.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Generalizability  
- **Claim pointer** The authors claim that their findings "offer a new paradigm for developing peptide-based PPI modulators."  
- **Evidence pointer** Abstract only; no data on other systems provided  
- **Concern** The abstract describes results for a single interaction pair, SUMO and SIMs. The claim of a "new paradigm" implies generalizability beyond this specific system, but no evidence is presented to support broader applicability. It is unclear whether the observed effects are specific to the SUMO-SIM system or represent a general principle.  
- **Why it matters** Overgeneralization from a single example could mislead other researchers attempting to apply this strategy to different PPI systems. The paradigm claim requires demonstration across multiple unrelated β-strand-mediated interactions.  
- **Resolution test** Either temper the claim to be specific to the SUMO-SIM system or provide additional examples showing that N-methylation has similar effects on other β-strand-mediated PPIs. If additional examples are not available, the abstract should be revised to avoid overstatement.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Terminology  
- **Evidence pointer** Abstract, first sentence  
- **Issue** The phrase "β-strand mediated protein-protein interactions" is used without defining what constitutes a β-strand-mediated interaction in this context. Some readers may interpret this differently.  
- **Required correction** Provide a brief definition or example of what is meant by β-strand-mediated interactions, particularly in the context of the SUMO-SIM system.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Control experiments  
- **Evidence pointer** Abstract only  
- **Issue** The abstract does not mention any control experiments, such as N-methylation at positions expected to be non-permissive or the use of scrambled sequences. Without such controls, it is difficult to rule out non-specific effects of backbone modification.  
- **Required correction** Include a statement about control experiments in the abstract or indicate where they are described in the full manuscript.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Interpretation  
- **Affected element** Entropic contribution  
- **Evidence pointer** Abstract, final sentence  
- **Issue** The claim of "a reduction in the entropic contribution to the binding and activation energies" is stated without explaining whether this reduction is favorable or unfavorable to binding. A reduction in entropic contribution could be either beneficial or detrimental depending on the context.  
- **Required correction** Clarify the sign and significance of the entropic changes and how they relate to the overall affinity enhancement.

## Risk / unsupported claims
- The claim that N-methylation "effectively restrict[s] accessible peptide conformations" is unsupported by any conformational data presented in the abstract.
- The claim that "faster target binding, and thus higher affinity" is observed is unsupported by any kinetic or equilibrium binding data.
- The mechanistic claim regarding "an increase in the energy of the unbound state, and a reduction in the entropic contribution to the binding and activation energies" is unsupported by any thermodynamic or computational data presented.
- The claim of offering "a new paradigm for developing peptide-based PPI modulators" is unsupported by evidence of generalizability beyond the single SUMO-SIM system described.
- All quantitative results, including binding affinities, kinetic rates, and energetic values, are not provided and therefore cannot be evaluated.