## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, conclusions) for the article "Spidroins under the Influence of Alcohol: Effect of Ethanol on Secondary Structure and Molecular Level Solvation of Silk-Like Proteins" by Tolmachev et al., published in Biomacromolecules (2023).
- **Assessment boundary** Scientific content, methodological rigor, internal consistency, and support of claims by presented evidence. No assessment of formatting, grammar, or journal fit beyond Nature-style criteria.
- **Shared manuscript claim summary** The authors claim that ethanol induces ordered secondary structures (increased helices and turns) in spidroins, promotes aggregation, increases intramolecular hydrogen bonding, and alters solvation, with residue-specific effects (glutamine, serine, glycine) and implications for other intrinsically disordered proteins.
- **Visible evidence base** Abstract, full introduction, materials and methods (experimental and simulation), results sections (CD, DLS, microscopy, MD simulations), and conclusions. Figures and tables are referenced but not fully visible; supplementary material is mentioned but not provided.
- **Missing materials affecting confidence** Actual figures (Figures 1–9), tables (Tables 1–6), supplementary figures (S1–S14), and supplementary tables (S1–S2) are not provided. Detailed simulation parameters (e.g., exact box sizes post-equilibration, force field validation data) are partially described but not fully verifiable. Experimental raw data (e.g., DLS size distributions, CD spectra) are not available.

## Reviewer
- **Overall assessment** The manuscript presents a systematic combined computational and experimental study of ethanol effects on spidroin secondary structure and solvation. The topic is relevant to biomaterials and protein assembly. The integration of MD simulations with CD, DLS, and microscopy is commendable. However, the evidence base is incomplete in the provided material, and several claims, particularly regarding residue-specific effects and generalization to other proteins, are not fully supported by the visible data. The manuscript has potential but requires clarification and additional evidence to establish the case robustly.
- **Who would be interested in the results, and why** Researchers in biomaterials, protein engineering, and biophysics, particularly those studying silk proteins, intrinsically disordered proteins, and solvent effects on protein structure. The findings could inform alcohol-based processing of protein materials and guide sequence design for tunable properties.
- **Major strengths** 1) Combined use of atomistic MD simulations and multiple experimental techniques (CD, DLS, microscopy) provides complementary perspectives. 2) Focus on molecular-level mechanisms, including hydrogen bonding and solvation, adds depth beyond phenomenological observations. 3) Residue-level analysis offers potential for sequence-specific design. 4) The study addresses a practical processing step (alcohol treatment) with fundamental insights.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (simulation-experiment comparability), R1-M2 (quantitative support for residue-specific claims), R1-M3 (generalization to other IDPs), R1-M4 (aggregation mechanism interpretation).
- **Assessment against Nature-style criteria**  
  - *Originality*: Moderate. The study is not entirely novel, as alcohol effects on silk proteins are known, but the molecular-level residue-specific analysis and combined simulation-experiment approach offer some new insights.  
  - *Scientific importance*: Moderate. The findings are useful for biomaterials processing but do not represent a major conceptual advance.  
  - *Interdisciplinary readership*: Limited. The work is primarily of interest to biophysicists and biomaterials scientists, with less appeal to a broader audience.  
  - *Technical soundness*: Partially sound. The methods are appropriate, but the incomplete evidence base and some interpretive leaps reduce confidence.  
  - *Readability for nonspecialists*: Adequate. The text is generally clear, but some technical details may be challenging for nonspecialists.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding simulation-experiment comparability and quantitative support for residue-specific claims. Currently not fully established from the provided evidence.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors claim that MD simulations of AQ3 (a truncated sequence) can be directly compared with experimental results on CBM-AQ12-CBM, and that the simulation findings explain the experimental observations.  
- **Evidence pointer** Methods section "Molecular Dynamics Simulations"; Results section "Simulations vs Experimental Characterization Results on a Silk Protein Secondary Structure in Water" and "Simulations vs Experimental Characterization Results on the Silk Protein Secondary Structure in Water/Ethanol Mixtures"; Table 3.  
- **Concern** The simulation uses AQ3, a three-repeat fragment of the AQ12 midblock, while experiments use the full CBM-AQ12-CBM construct. The authors justify this by assuming ethanol has minor effects on the CBM domains, but this assumption is not directly tested. The truncation may alter conformational sampling, aggregation behavior, and solvent interactions, especially given the repetitive nature of the sequence. The comparison in Table 3 relies on subtracting estimated CBM and linker contributions, which introduces uncertainty. Without validation that AQ3 behaves equivalently to the AQ12 midblock in the context of the full protein, the direct comparability is questionable.  
- **Why it matters** The central claim that simulations reveal molecular mechanisms underlying experimental observations depends on the representativeness of the AQ3 model. If the truncation changes the system's behavior, the mechanistic conclusions may not apply to the experimental system.  
- **Resolution test** Provide additional simulations of AQ12 or a longer fragment, or experimental validation of the assumption that CBM domains are unaffected by ethanol. Alternatively, show that AQ3 and AQ12 exhibit similar secondary structure propensities and solvation patterns under identical conditions.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence strength  
- **Claim pointer** The authors claim that glutamine and serine are most influenced by ethanol, and glycine residues are most prone to be involved in ethanol-induced secondary structure changes.  
- **Evidence pointer** Results section "Simulations vs Experimental Characterization Results on the Silk Protein Secondary Structure in Water/Ethanol Mixtures"; Figure 5; Table 5.  
- **Concern** The residue-specific claims are based on simulation data, but the provided text does not include quantitative metrics (e.g., per-residue secondary structure propensities, hydrogen bond counts, or statistical significance). The claims appear qualitative, and the magnitude of effects is not reported. Without error bars or statistical tests, it is unclear whether the observed differences between residues are robust or within noise.  
- **Why it matters** These claims are presented as key findings with implications for sequence design. If not quantitatively supported, they may be overinterpreted and could mislead future work.  
- **Resolution test** Provide per-residue secondary structure fractions with standard deviations, and statistical comparisons (e.g., t-tests or confidence intervals) between residues in water vs ethanol. Show that the effects are reproducible across independent simulations or simulation repeats.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Scope of claims  
- **Claim pointer** The authors generalize their findings to "other intrinsically disordered proteins" based on the observed mechanisms.  
- **Evidence pointer** Abstract; Conclusions section.  
- **Concern** The study examines a single protein sequence (AQ3/AQ12) with a specific amino acid composition. The generalization to other IDPs is speculative, as the response to ethanol likely depends on sequence composition, length, and specific interactions. No comparative data from other IDPs are provided to support this claim.  
- **Why it matters** Overgeneralization could lead to incorrect assumptions about ethanol effects on other proteins, undermining the practical utility of the findings.  
- **Resolution test** Either temper the claim to be specific to spidroins or provide additional simulations or experiments on other IDPs to demonstrate generalizability.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Interpretation  
- **Claim pointer** The authors suggest that aggregation occurs due to the formation of interprotein H-bonds with partial transition of α-helices into β-sheets connecting different protein molecules.  
- **Evidence pointer** Conclusions section; Results section "Experimental Results on Ethanol-Induced Secondary Structure Changes: Circular Dichroism".  
- **Concern** This mechanistic interpretation is inferred from simulation data on single molecules and indirect experimental evidence (CD, DLS, microscopy). The simulations do not appear to model multiple protein molecules or aggregation directly, so the claim about interprotein H-bonds and β-sheet formation during aggregation is speculative. The CD data show increased β-sheet content, but this could arise from intramolecular changes rather than intermolecular interactions.  
- **Why it matters** The proposed aggregation mechanism is a significant conclusion, but it is not directly supported by the visible evidence. Misinterpreting the mechanism could affect how the results are applied to processing conditions.  
- **Resolution test** Perform multi-molecule simulations to directly observe aggregation and interprotein interactions, or provide experimental evidence (e.g., FTIR, solid-state NMR) that distinguishes intra- vs intermolecular β-sheets.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Methods section "Molecular Dynamics Simulations"  
- **Evidence pointer** Location not provided  
- **Issue** The description of the simulation protocol is incomplete. The text mentions equilibration and production runs but does not specify the number of independent simulations, the criteria for equilibration (beyond RMSD and hydrogen bonds), or the exact composition of the systems (e.g., number of water/ethanol molecules, salt concentration in ethanol systems).  
- **Required correction** Provide a more detailed simulation protocol, including system composition, number of replicates, and equilibration criteria, to enable reproducibility.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Data presentation  
- **Affected element** Results section "Experimental Results on Ethanol-Induced Secondary Structure Changes: Circular Dichroism"  
- **Evidence pointer** Figure 2; Table 2  
- **Issue** The CD spectra are described qualitatively, and the secondary structure fractions from BeStEl are presented in Table 2, but the text does not discuss the reliability of the BeStEl analysis for this system. The authors note challenges in distinguishing α-helices from β-sheets, but the quantitative estimates are used without caveats in the comparison with simulations.  
- **Required correction** Add a discussion of the limitations of the BeStEl analysis and how uncertainties in the experimental estimates affect the comparison with simulations.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Consistency  
- **Affected element** Results section "Distribution of H-bonds in the silk protein/water/ethanol mixtures"  
- **Evidence pointer** Figure 6; Table 6  
- **Issue** The text states that hydrogen bonding with solvent is reduced by a factor of ~1.3, but the basis for this factor (e.g., total counts, per-residue averages) is not specified. The relationship between hydrogen bond changes and secondary structure changes is discussed, but the causal link is not rigorously established.  
- **Required correction** Clarify the calculation of the reduction factor and provide a more explicit analysis of how hydrogen bond changes correlate with secondary structure changes.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Generalization  
- **Affected element** Conclusions section  
- **Evidence pointer** Location not provided  
- **Issue** The conclusion that ethanol "provides a convenient way to control the properties of silk materials" is stated without discussing potential limitations, such as concentration-dependent effects, reversibility, or applicability to different silk protein variants.  
- **Required correction** Add a brief discussion of the scope and limitations of the findings for practical applications.

## Risk / unsupported claims
- The claim that ethanol effects on AQ3 simulations directly explain experimental observations on CBM-AQ12-CBM is not fully supported due to the sequence truncation and untested assumptions about CBM behavior (R1-M1).
- The residue-specific claims about glutamine, serine, and glycine are not quantitatively supported in the provided text (R1-M2).
- The generalization to other intrinsically disordered proteins is unsupported by direct evidence (R1-M3).
- The proposed aggregation mechanism involving interprotein β-sheet formation is speculative and not directly observed in the simulations (R1-M4).
- The statement that "the work presents a systematic characterization" is partially supported, but the incomplete evidence base (missing figures, tables, and supplementary data) limits full verification.