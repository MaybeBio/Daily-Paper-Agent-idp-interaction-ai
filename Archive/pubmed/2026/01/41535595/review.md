## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results and discussion, conclusions, and methods sections, as provided.
- **Assessment boundary** Scientific content, technical soundness, and internal consistency of the presented claims based solely on the supplied material. No external literature or unpublished data were consulted.
- **Shared manuscript claim summary** The authors propose that the small molecule AM-7209 induces a disorder-to-order transition of the N-terminal intrinsically disordered "lid" region of MDM2 through a network of non-polar contacts, particularly involving residue I19 and the ligand's chlorophenyl moiety, which collectively overcome the conformational entropy cost of folding. They further claim that mutations at I19 can reduce binding affinity by up to three orders of magnitude, and that this mechanism has implications for drug resistance and ligand design.
- **Visible evidence base** Molecular dynamics simulations (equilibrium and free energy surface calculations), isothermal titration calorimetry (ITC) binding data for a panel of mutants, NMR chemical shift perturbation and relaxation measurements for WT and I19G, and supporting supplementary figures and tables referenced but not fully visible.
- **Missing materials affecting confidence** Supplementary figures (S1–S27), tables (S4), detailed methods for aMD/US/vFEP calculations, NMR assignment details, and raw ITC thermograms were not provided. These are essential for full verification of quantitative claims.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question in chemical biology: how small molecules can drive folding of intrinsically disordered regions upon binding. The combination of computational and experimental approaches is commendable, and the identification of a single residue (I19) that dramatically modulates affinity is a striking and potentially impactful finding. However, several technical concerns, particularly regarding the interpretation of the free energy calculations and the generalizability of the proposed mechanism, need to be addressed before the case is fully established. The manuscript is well-written and accessible, but the evidence for the central "hydrophobic collapse" driving force is largely indirect.
- **Who would be interested in the results, and why** Researchers in the fields of drug discovery, specifically those targeting protein-protein interactions and intrinsically disordered proteins. The work also holds interest for biophysicists studying coupled folding and binding mechanisms, and for medicinal chemists seeking new strategies for ligand optimization. The potential link to drug resistance mechanisms broadens the appeal to the oncology community.
- **Major strengths** 1) The study tackles a challenging and under-explored problem: small molecule-induced folding of an IDR. 2) The multi-technique approach (MD, ITC, NMR) provides complementary perspectives. 3) The identification of a single residue with a 1000-fold effect on affinity is a clear, testable, and impactful result. 4) The manuscript is clearly written and the figures are informative.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (interpretation of FES), R1-M2 (generality of the mechanism), R1-M3 (quantitative link between simulations and ITC).
- **Assessment against Nature-style criteria** **Originality:** High. The concept of exploiting IDR folding for small molecule binding is not new, but the detailed mechanistic dissection of a specific example, particularly the role of a single distal residue, is novel. **Scientific importance:** Potentially high. If the mechanism is general, it could inform future drug design efforts targeting IDRs. However, the demonstration of generality is currently limited to a single system. **Interdisciplinary readership:** Moderate to high. The topic bridges chemistry, biology, and biophysics, and the findings are relevant to drug discovery. **Technical soundness:** Generally sound, but with concerns about the interpretation of the FES and the lack of direct experimental validation of the proposed hydrophobic collapse. **Readability for nonspecialists:** Good. The abstract and introduction are accessible, and the results are presented in a logical manner, though some of the computational details may be dense for a general reader.
- **Recommendation posture** Supportive if technical concerns are resolved. The core finding regarding I19 is compelling, but the mechanistic interpretation requires strengthening and the generality of the claims needs to be tempered or better supported.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of computational interpretation
- **Claim pointer** The authors claim that the free energy surfaces (FES) show that in the I19G mutant, the lid remains largely disordered and does not form the helical motif, and that this is due to loss of non-polar contacts with the ligand's chlorophenyl moiety.
- **Evidence pointer** Figure 5C, 5D, and associated text in "Free energy calculations identify the structural requirements for ordering of the MDM2 lid by AM-7209" section.
- **Concern** The FES for I19G in complex with AM-7209 (Fig. 5D) is described as showing a "partially open and collapsed state" (label C11) that is "largely disordered." However, the collective variables used (lid extension and lid-core dihedral angle) may not be sufficient to distinguish between a disordered collapsed state and an ordered but differently packed state. The secondary structure analysis in Fig. 5E shows a small increase in helicity for residues 21-25 in I19G upon binding, which is not zero. The interpretation that the state is "largely disordered" appears to be an overstatement based on the presented metrics. The authors need to provide a more direct measure of disorder, such as per-residue helical propensity distributions or Ramachandran plots from the FES basins, to support this claim.
- **Why it matters** This is the central mechanistic claim of the paper. If the FES interpretation is ambiguous, the proposed "hydrophobic collapse" driving force is not convincingly established. The distinction between a disordered collapsed state and an ordered but different conformation is critical for the mechanistic narrative.
- **Resolution test** Provide additional analysis of the FES basins, such as representative structures, per-residue secondary structure probabilities, or contact maps, that clearly demonstrate the disordered nature of the I19G bound state compared to the ordered WT bound state. Alternatively, temper the claim to "does not adopt the same ordered conformation as WT" rather than "remains largely disordered."

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of the proposed mechanism
- **Claim pointer** The authors state in the abstract and conclusions that their findings "underscore the crucial role that protein IDRs can play in drug-resistance mechanisms and expand strategies available to medicinal chemists for ligand optimisation endeavours."
- **Evidence pointer** Abstract and Conclusions section.
- **Concern** The study is based on a single protein-ligand pair (MDM2 and AM-7209). While the findings are internally consistent, the leap to general principles for drug resistance and ligand optimization is not directly supported by the data presented. The authors do not demonstrate that the proposed mechanism applies to other IDRs or other ligands. The claim about drug resistance is speculative, as no direct evidence of resistance development is provided.
- **Why it matters** Overgeneralization can mislead the field. While the findings are suggestive, the broad claims in the abstract and conclusions go beyond the scope of the presented evidence. This is particularly important for a journal with broad readership.
- **Resolution test** Soften the language in the abstract and conclusions to reflect that these are potential implications of the findings, not established facts. Alternatively, add a brief discussion of how the mechanism might apply to other systems, with appropriate caveats.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative consistency between simulation and experiment
- **Claim pointer** The authors state that the ITC measurements show a ca. 3 kcal/mol less favorable entropy of binding for AM-7209 to WT than for I19G, and that their simulations estimate a ca. 2.2 kcal/mol greater entropy loss for WT, which they consider consistent.
- **Evidence pointer** "Free energy calculations identify the structural requirements for ordering of the MDM2 lid by AM-7209" section and Figure 3C.
- **Concern** The comparison between the simulated entropy difference (2.2 kcal/mol) and the experimental entropy difference (3 kcal/mol) is presented as consistent, but the discrepancy of 0.8 kcal/mol is not trivial. More importantly, the simulated entropy loss is decomposed into conformational and roto/translational components, but it is unclear how these were calculated and whether they are directly comparable to the ITC-derived entropy, which includes solvent contributions. The authors should clarify the calculation of the entropy terms and discuss the potential sources of the discrepancy.
- **Why it matters** The quantitative agreement between simulation and experiment is used to support the mechanistic interpretation. If the comparison is not rigorous, the strength of the conclusion is weakened.
- **Resolution test** Provide a more detailed explanation of the entropy calculations, including the methods used (e.g., quasi-harmonic, Schlitter) and the assumptions made. Discuss the potential contributions of solvent entropy to the experimental value and why they are not included in the simulation estimate. A more nuanced comparison, acknowledging the approximations, would be more convincing.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure presentation
- **Affected element** Figure 3D
- **Evidence pointer** Figure 3D and its caption.
- **Issue** The caption mentions "*: direct titration, ': competitive titration" but the symbols are not clearly visible or explained in the figure itself. This makes it difficult to interpret the data points.
- **Required correction** Ensure the symbols are clearly visible in the figure and that the caption fully explains the notation. Consider using distinct colors or shapes for direct and competitive titrations.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Methods section, "Molecular dynamics simulations"
- **Evidence pointer** Methods section.
- **Issue** The methods state that "Each mutant underwent two independent 0.5 µs equilibrium MD simulations" but do not specify the force field, water model, or temperature/pressure coupling parameters used. This level of detail is insufficient for reproducibility.
- **Required correction** Add the missing simulation parameters (force field, water model, salt concentration, thermostat/barostat settings) to the methods section.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of NMR data
- **Affected element** Figure 4D and associated text
- **Evidence pointer** Figure 4D and "NMR analysis upon titration of AM-7209 into samples of WT MDM2 and I19G mutant" section.
- **Issue** The authors state that the HetNOE changes for I19G are "negligible or small" for residues 1-16, but the figure shows some non-zero changes. The threshold for "negligible" is not defined. This could be seen as subjective.
- **Required correction** Define a quantitative threshold for significant HetNOE changes (e.g., based on the estimated error of the measurements) and apply it consistently to the data.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract, first sentence.
- **Issue** The term "synergestic" is misspelled. It should be "synergistic."
- **Required correction** Correct the spelling.

## Risk / unsupported claims
- The claim that the proposed mechanism is relevant to "drug-resistance mechanisms" is unsupported by direct experimental evidence in this manuscript. It is a plausible hypothesis but not demonstrated.
- The claim that the findings "expand strategies available to medicinal chemists" is a general statement that is not directly tested. It is a reasonable implication but should be framed as such.
- The quantitative agreement between simulated and experimental entropy changes (2.2 vs 3 kcal/mol) is presented as consistent, but the discrepancy and the different nature of the calculated terms (gas-phase vs solution) are not fully discussed, making the comparison potentially misleading.
- The statement that the I19G bound state is "largely disordered" is not fully supported by the presented FES and secondary structure analysis, which show a small but non-zero increase in helicity.