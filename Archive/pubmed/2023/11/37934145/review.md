## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no access to full text, figures, tables, or supplementary information
- **Shared manuscript claim summary** The authors propose a de novo peptide condensate design strategy using simple repeat motifs (tripeptide spacers GSG, SGS, GLG interspersed with R/H and Y). They claim that n→π* interactions in GLG backbones are a dominant factor in providing backbone structure that regulates the water interface and promotes liquid droplet formation. They further report sequence-dependent intrinsic fluorescence in R(GLG)Y and H(GLG)Y condensates, attributed to non-covalent network interactions and observable by confocal microscopy.
- **Visible evidence base** Abstract text only; no experimental details, computational methods, quantitative data, or imaging data provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, computational methodology and parameters, experimental protocols, characterization data (e.g., microscopy, spectroscopy, rheology), sequence library details, and any statistical analyses

## Reviewer
- **Overall assessment** The abstract presents an intriguing conceptual advance in peptide condensate design, linking backbone stereoelectronic effects (n→π* interactions) to phase behavior and reporting an unexpected fluorescence property. The work is potentially of broad interest to the biomolecular condensate and peptide materials communities. However, the abstract alone provides insufficient evidence to evaluate the robustness of the central claims. The mechanistic assertion regarding n→π* interactions as a "dominant factor" requires quantitative support from computational and experimental comparisons across the three spacer types. The fluorescence claim, while novel, lacks spectral characterization and control experiments in the abstract. The manuscript may merit consideration if the full evidence base substantiates these claims, but the case is not established from the supplied material.
- **Who would be interested in the results, and why** Researchers in biomolecular condensates, intrinsically disordered proteins, peptide self-assembly, and materials science would find this work relevant. The sequence-tunable phase behavior offers design rules for synthetic condensates, and the intrinsic fluorescence property could enable label-free imaging, appealing to biophysicists and bioengineers. The n→π* interaction framework may also interest computational chemists studying backbone conformational preferences.
- **Major strengths** The design strategy is conceptually simple and modular, using minimal sequence variation to probe structure–property relationships. The observation of intrinsic fluorescence in condensates is unexpected and potentially transformative for imaging applications. The combination of computation and experiment is appropriate for the mechanistic question posed.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract does not provide quantitative evidence for the dominance of n→π* interactions over other factors (e.g., hydrogen bonding, hydrophobicity, aromatic stacking). The fluorescence claim lacks spectral data, quantum yield, excitation/emission maxima, and control experiments with non-condensing or single-component systems. No evidence is shown that the observed emission is intrinsic to the non-covalent network rather than to monomeric peptides or impurities.
- **Assessment against Nature-style criteria** 
  - Originality: High. The n→π* interaction as a design handle for condensate formation and the intrinsic fluorescence observation are both novel.
  - Scientific importance: Potentially high if the mechanistic claim is robust, as it would provide a predictive design principle. The fluorescence property could enable new imaging modalities.
  - Interdisciplinary readership: The work bridges peptide chemistry, biophysics, and materials science, appealing to a broad audience.
  - Technical soundness: Cannot be assessed from the abstract. The computational and experimental methods are not described in sufficient detail.
  - Readability for nonspecialists: The abstract is concise and accessible, though terms like "n→π* interactions" may require background knowledge.
- **Recommendation posture** Currently not established from the provided evidence. Supportive if the full manuscript provides quantitative computational and experimental evidence for the n→π* dominance and rigorous characterization of the fluorescence property.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic claim
- **Claim pointer** "n→π* interactions in GLG backbones are a dominant factor in providing sufficient backbone structure, which in turn regulates the water interface, collectively promoting liquid droplet formation."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract asserts that n→π* interactions are a "dominant factor" driving droplet formation, but no quantitative comparison is shown between GLG and the other spacers (GSG, SGS). The claim implies a causal hierarchy that requires demonstration that GLG specifically enhances backbone structure and water interface regulation relative to GSG and SGS, and that this effect is attributable to n→π* interactions rather than to other physicochemical differences (e.g., side-chain hydrophobicity, flexibility, or hydrogen-bonding capacity).
- **Why it matters** The central design principle of the work rests on this mechanistic attribution. Without comparative data, the claim is not distinguishable from a correlation between sequence and phase behavior. The term "dominant" requires evidence that other interactions are subordinate, which is not provided.
- **Resolution test** Provide computational analyses (e.g., QM or MD) quantifying n→π* interaction energies in GLG versus GSG and SGS, and experimental phase diagrams showing that GLG-containing peptides form droplets under conditions where GSG and SGS do not, with controls ruling out alternative drivers.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Fluorescence claim
- **Claim pointer** "R(GLG)Y and H(GLG)Y condensates unexpectedly display sequence-dependent emission that is a consequence of their non-covalent network interactions, and readily observable by confocal microscopy."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The fluorescence property is reported without spectral characterization. No excitation and emission maxima, quantum yields, or lifetime data are provided. The attribution to "non-covalent network interactions" is speculative without control experiments, such as fluorescence measurements of monomeric peptides, non-condensing mutants, or denatured condensates. The possibility of aggregation-induced emission from aromatic residues (Y) or impurities is not excluded.
- **Why it matters** Intrinsic fluorescence in biomolecular condensates is a notable claim with potential for broad application. If the emission arises from the non-covalent network, this is a new photophysical phenomenon. If it arises from trivial causes (e.g., light scattering, impurities, or monomer emission), the claim is misleading. The sequence-dependence also requires demonstration that emission properties vary systematically with sequence.
- **Resolution test** Provide fluorescence spectra (emission and excitation), quantum yield measurements, and confocal images with appropriate controls (e.g., monomer solutions, non-condensing sequences, and denatured condensates). Show that emission is absent or different in control systems and that the spectral properties correlate with the proposed network interactions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of design framework
- **Claim pointer** "We designed peptide modules based on a simple repeat motif composed of tripeptide spacers (GSG, SGS, GLG) interspersed with adhesive amino acids (R/H and Y)."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract implies a general design framework, but only two adhesive residues (R/H and Y) and three spacers are mentioned. It is unclear whether the framework extends to other adhesive residues or spacer combinations, and whether the phase behavior is robust to sequence variations beyond the tested set. The abstract does not state the number of peptides studied or the range of conditions (e.g., pH, ionic strength, concentration) over which droplet formation was observed.
- **Why it matters** For a "conceptual framework" to be useful, its boundaries must be defined. If the design only works for a narrow sequence space, the claim of a framework is overstated. The absence of condition space information limits the reader's ability to assess practical utility.
- **Resolution test** Provide a sequence library with systematic variations and a phase diagram showing the conditions under which droplet formation occurs. Demonstrate that the design rules hold for at least a few additional adhesive residues or spacer combinations.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** "adhesive amino acids"
- **Evidence pointer** Abstract; location not provided
- **Issue** The term "adhesive" is not defined. It is unclear whether it refers to specific non-covalent interactions (e.g., cation–π, π–π, hydrogen bonding) or a general propensity to promote phase separation.
- **Required correction** Define "adhesive" in the context of the interactions being probed, or use more specific terminology.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Quantitative context
- **Affected element** "liquid droplet formation"
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract does not indicate how droplet formation was confirmed (e.g., by turbidity, microscopy, rheology) or whether the droplets are equilibrium phases or kinetically trapped states.
- **Required correction** Briefly state the characterization method and whether the droplets are reversible (e.g., by dilution or temperature cycling).

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility of fluorescence observation
- **Affected element** "readily observable by confocal microscopy"
- **Evidence pointer** Abstract; location not provided
- **Issue** The phrase "readily observable" is qualitative. It is unclear whether the emission is bright enough for standard imaging or requires special acquisition settings.
- **Required correction** Provide a quantitative measure of fluorescence intensity or a representative image with scale bar and acquisition parameters in the full manuscript.

## Risk / unsupported claims
- The claim that n→π* interactions are a "dominant factor" in promoting droplet formation is unsupported without comparative quantitative data.
- The attribution of fluorescence to "non-covalent network interactions" is unsupported without spectral and control experiments.
- The generalizability of the design framework beyond the tested sequences is unassessable from the abstract.
- The sequence-dependence of emission is asserted but not demonstrated with data.
- The term "liquid droplet" implies a specific material state that is not verified in the abstract.