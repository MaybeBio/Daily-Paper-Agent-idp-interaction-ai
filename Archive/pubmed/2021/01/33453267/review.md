## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors propose that short glycine-capped arginine peptides (GRRG and GRRRG) can serve as predictors for the conformational behavior of longer polyarginine sequences in disordered proteins. They report that nearest-neighbor arginine interactions stabilize extended β-strand conformations over polyproline II and turn conformations, based on NMR J-coupling constants and amide I′ vibrational spectroscopy. Molecular dynamics simulations with CHARMM36m and TIP3P water reproduce experimental results only partially. Using the Ramachandran distribution of the central residue of GRRRG, they calculate end-to-end distances for polyarginines of varying lengths, obtaining a scaling coefficient of 0.66, which suggests more extended conformations than a self-avoiding random coil.
- **Visible evidence base** Abstract text only; experimental methods (NMR, vibrational spectroscopy) and simulation details are referenced but not described in the provided material
- **Missing materials affecting confidence** Full manuscript, experimental spectra, J-coupling data, simulation parameters, Ramachandran distributions, statistical analyses, and any comparison with theoretical predictions beyond the scaling coefficient

## Reviewer
- **Overall assessment** The abstract presents a focused and potentially valuable hypothesis that short arginine-containing peptides can inform the conformational preferences of longer polyarginine sequences. The combination of experimental spectroscopy and molecular dynamics simulations is appropriate for the question. However, the abstract alone provides insufficient detail to evaluate the robustness of the experimental assignments, the quality of the simulation force field comparison, or the statistical significance of the scaling coefficient. The central claim that GRRRG can predict polyarginine structure rests on a single extrapolation step that is not fully justified from the provided material.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, particularly those interested in the role of charged residues in modulating conformational ensembles. The work may also appeal to computational biophysicists developing or testing force fields for disordered peptides, and to experimentalists using NMR or vibrational spectroscopy to probe local backbone conformations.
- **Major strengths** The study addresses a relevant and under-explored question about how charged residues influence local backbone conformations in disordered contexts. The use of multiple complementary experimental techniques (NMR and vibrational spectroscopy) strengthens the empirical basis. The explicit link to scaling behavior of polyarginines provides a testable prediction that connects short peptide data to polymer physics.
- **Major Concerns** 
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The abstract claims that nearest-neighbor interactions stabilize extended β-strand conformations at the expense of polyproline II and turn conformations, based on J-coupling constants and amide I′ band profiles.
  - **Evidence pointer** Abstract, methods referenced but not provided
  - **Concern** The abstract does not provide quantitative details on the J-coupling constants or amide I′ band profiles, nor does it describe how these data were converted into conformational propensities. Without access to the actual spectra, coupling values, or the fitting procedure, the reader cannot assess whether the reported stabilization of β-strand conformations is statistically robust or whether alternative interpretations (e.g., solvent effects, end effects in short peptides) were excluded.
  - **Why it matters** The central experimental conclusion depends entirely on the interpretation of these spectroscopic data. If the assignments or the conformational analysis are flawed, the entire predictive framework collapses.
  - **Resolution test** Provide the full experimental section with J-coupling values, amide I′ band fitting parameters, and a comparison of measured versus calculated observables for each peptide. Show that the derived Ramachandran distributions are statistically distinguishable between GRG and GRRG/GRRRG.
- **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Claim extrapolation
  - **Claim pointer** The abstract claims that the Ramachandran distribution of the central residue of GRRRG can be used to calculate end-to-end distances of polyarginines of different lengths, yielding a scaling coefficient of 0.66.
  - **Evidence pointer** Abstract, scaling calculation described but not detailed
  - **Concern** The extrapolation from a single central residue distribution in a pentapeptide to a full polyarginine chain is a significant leap. The abstract does not specify how the Ramachandran distribution was propagated along the chain, whether excluded volume effects were accounted for, or how the scaling coefficient was computed. The value of 0.66 is presented without error bars or a comparison to alternative models.
  - **Why it matters** The predictive claim of the paper rests on this extrapolation. If the method is not rigorously defined or if the uncertainty is large, the conclusion that polyarginines are more extended than self-avoiding random coils is not established.
  - **Resolution test** Provide a detailed description of the chain model, the propagation of the Ramachandran distribution, and the statistical uncertainty on the scaling coefficient. Show that the result is robust to variations in the model assumptions.
- **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Simulation-experiment agreement
  - **Claim pointer** The abstract states that molecular dynamics simulations with CHARMM36m and TIP3P water reproduce the experimental results only to a limited extent.
  - **Evidence pointer** Abstract, simulation details not provided
  - **Concern** The abstract does not specify which aspects of the experimental results were reproduced and which were not. Without a quantitative comparison (e.g., J-coupling values, Ramachandran distributions, or end-to-end distances), the reader cannot judge whether the discrepancy is minor or fundamental.
  - **Why it matters** The limited agreement between simulation and experiment could indicate force field inaccuracies, which would affect the reliability of the simulation-based predictions. Alternatively, it could reflect experimental uncertainties. The current description is too vague to interpret.
  - **Resolution test** Include a figure or table comparing simulated and experimental observables for each peptide, with a clear statement of which metrics agree and which deviate, and by how much.
- **Minor Comments** 
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Abstract wording
  - **Evidence pointer** Abstract, first sentence
  - **Issue** The phrase "high preference for extended conformations" is vague. It is unclear whether "extended" refers to β-strand-like local conformations or to global chain dimensions.
  - **Required correction** Specify whether the preference is for local backbone dihedral angles or for global end-to-end distances, and define the reference state (e.g., self-avoiding random coil).
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Abstract, simulation statement
  - **Evidence pointer** Abstract, sentence on CHARMM36m
  - **Issue** The abstract does not state whether other force fields were tested or whether the limited agreement is attributed to specific force field parameters.
  - **Required correction** Add a sentence clarifying whether the limited agreement is force field specific or general, and whether alternative force fields were considered.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Statistical reporting
  - **Affected element** Scaling coefficient
  - **Evidence pointer** Abstract, scaling coefficient of 0.66
  - **Issue** The scaling coefficient is presented without any measure of uncertainty or goodness of fit.
  - **Required correction** Report the standard error or confidence interval for the scaling coefficient and the number of chain lengths used in the fit.

## Risk / unsupported claims
- The claim that nearest-neighbor arginine interactions stabilize β-strand conformations is not fully supported from the abstract alone, as the underlying spectroscopic analysis is not described.
- The claim that the scaling coefficient of 0.66 indicates more extended conformations than a self-avoiding random coil is not supported with statistical uncertainty or a comparison to theoretical predictions for self-avoiding chains.
- The statement that simulations reproduce results "only to a limited extent" is unquantified and cannot be evaluated.
- The generalizability of the GRRRG-based prediction to longer polyarginine sequences is asserted but not demonstrated with direct experimental data on longer chains.

## Assessment against Nature-style criteria
- **Originality** The idea of using short peptides as predictors for longer disordered sequences is not entirely new, but the specific focus on polyarginine and the combination of experimental and computational approaches is a reasonable contribution. The originality is moderate.
- **Scientific importance** The work addresses a relevant question in the field of intrinsically disordered proteins, where understanding how charged residues modulate conformations is important. However, the significance is limited by the narrow focus on polyarginine and the lack of direct validation on longer sequences.
- **Interdisciplinary readership** The work bridges experimental biophysics and computational simulation, which could appeal to a broad readership. However, the abstract is written in a way that assumes familiarity with both NMR and vibrational spectroscopy, which may limit accessibility.
- **Technical soundness** The technical soundness cannot be fully assessed from the abstract. The experimental and computational methods are referenced but not described in sufficient detail. The limited agreement between simulation and experiment raises questions that are not addressed.
- **Readability for nonspecialists** The abstract is reasonably clear but uses technical terms (e.g., J-coupling constants, amide I′ band profiles, CHARMM36m) without explanation. A nonspecialist would struggle to follow the logic.

## Recommendation posture
Currently not established from the provided evidence. The abstract presents an interesting hypothesis and a plausible approach, but the lack of methodological detail and the unquantified claims prevent a definitive assessment. The work could become publishable if the full manuscript provides robust experimental data, a clear description of the extrapolation method, and a quantitative comparison between simulation and experiment.