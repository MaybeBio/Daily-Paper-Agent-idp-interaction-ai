## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and figure legends
- **Assessment boundary** Scientific claims, methodological soundness, evidence consistency, and alignment with stated conclusions
- **Shared manuscript claim summary** The authors report that a mussel-derived adhesive peptide GK-16* undergoes liquid-liquid phase separation (LLPS) in seawater conditions, mediated by Dopa- and Gly-based hydrogen bonding interactions. They propose that tuning electrostatic and hydrogen bond interactions via pH and salt concentration controls coacervate properties, and demonstrate a pH-induced liquid-to-gel transition with potential for underwater adhesive delivery.
- **Visible evidence base** Experimental data from optical microscopy, CD spectroscopy, FTIR, SFA, UV-Vis, zeta potential, MALDI, and MD simulations; phase diagrams for multiple peptide variants
- **Missing materials affecting confidence** Supplementary figures and tables referenced but not provided; detailed MD simulation parameters and force field validation data; raw SFA force-distance curves; statistical analysis details for phase diagram boundaries; information on replicate numbers for some experiments

## Reviewer
- **Overall assessment** This manuscript presents a systematic investigation of LLPS in a mussel-derived adhesive peptide, combining experimental and computational approaches. The central claim that Dopa-mediated hydrogen bonds drive coacervation is supported by multiple lines of evidence, including point mutations, urea disruption, and MD simulations. However, several technical concerns regarding the interpretation of SFA data, the specificity of hydrogen bond contributions, and the generalizability of the findings to full-length Mfp-5 require clarification. The work is of interest to the biomaterials and biophysics communities, but the case for broad significance would be strengthened by addressing these issues.
- **Who would be interested in the results, and why** Researchers in biomaterials, particularly those developing bioinspired adhesives and coacervate-based systems; biophysicists studying LLPS mechanisms in proteins and peptides; marine biology groups investigating mussel adhesion; and materials scientists interested in stimuli-responsive coatings or delivery systems.
- **Major strengths** 1) The combination of experimental and computational methods provides complementary evidence for the proposed mechanism. 2) The systematic point-mutation approach effectively isolates the roles of specific residues. 3) The demonstration of pH-responsive adhesive behavior with potential practical applications is compelling. 4) The phase diagrams for multiple variants offer a comprehensive dataset.
- **Major Concerns** 1) The interpretation of SFA data for coacervate adhesion may be oversimplified, particularly regarding the calculation of interfacial energy and the attribution of adhesion changes to specific molecular interactions. 2) The claim that hydrogen bonds are "essential" is not fully established, as alternative interactions (e.g., hydrophobic effects) are not systematically excluded. 3) The relevance of the peptide model to full-length Mfp-5 is asserted but not experimentally validated. 4) The MD simulation methodology, particularly the use of a single pair of peptides to infer phase behavior, requires justification.
- **Minor Comments** 1) The phase diagram boundaries appear to be determined by visual inspection; statistical methods for boundary determination should be described. 2) The UV-Vis data for Dopa oxidation stability is presented qualitatively; quantitative analysis would strengthen the claim. 3) The manuscript would benefit from a clearer statement of the limitations of the peptide model system. 4) The relationship between the observed beta-sheet formation and LLPS is not fully clarified.
- **Technical failings that need to be addressed before the case is established** R1-M1 (SFA interpretation), R1-M2 (hydrogen bond specificity), R1-M3 (MD simulation scope)
- **Assessment against Nature-style criteria** Originality: The work offers a novel peptide model for studying mussel adhesion mechanisms, though the general concept of hydrogen-bond-driven LLPS is not entirely new. Scientific importance: The findings have potential implications for bioinspired adhesive design, but the direct relevance to natural Mfp-5 function is not fully demonstrated. Interdisciplinary readership: The work bridges materials science, biophysics, and marine biology, making it accessible to a broad audience. Technical soundness: The experimental design is generally sound, but several interpretive issues need resolution. Readability for nonspecialists: The manuscript is clearly written and well-structured, with appropriate context provided for the non-expert.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding SFA data interpretation and the specificity of hydrogen bond contributions.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence interpretation
- **Claim pointer** The authors claim that SFA measurements show "capillary adhesion caused by the GK-16* coacervate" with a calculated interfacial energy of 0.10 mJ/m2, and that increased salt concentration leads to a "liquid-to-gel transition" based on abolished adhesion force.
- **Evidence pointer** Results section, Figure 2d, 2g; Methods, SFA measurements
- **Concern** The interpretation of SFA force-distance profiles requires more careful consideration. The calculation of interfacial energy from a single adhesion measurement assumes equilibrium conditions and a specific geometry that may not hold for coacervate droplets. Additionally, the claim of a liquid-to-gel transition at high salt concentrations is inferred from the absence of adhesion force, but this could also result from changes in surface coverage, film thickness, or measurement artifacts. The authors should provide more detailed analysis of the SFA data, including multiple approach-retract cycles, and discuss alternative explanations for the observed force profiles.
- **Why it matters** The SFA data is central to the claim of tunable adhesive properties and the proposed application for underwater adhesives. If the interpretation is incorrect, the practical significance of the work is substantially weakened.
- **Resolution test** Provide additional SFA data showing reproducible force-distance curves under each condition, with analysis of multiple independent measurements. Demonstrate that the calculated interfacial energy is robust to assumptions about droplet geometry and surface coverage. Include control experiments with non-coacervating peptides to confirm the specificity of the observed adhesion.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic specificity
- **Claim pointer** The authors state that "Dopa- and Gly- mediated hydrogen-bonding interactions are essential in the coacervation process" and that Dopa functions as a "sticker" via bidentate hydrogen bonds.
- **Evidence pointer** Abstract; Results, LLPS section; Figure 3e-f; Figure 5
- **Concern** While the point-mutation experiments and urea disruption studies are consistent with hydrogen bond involvement, they do not exclude other contributions such as hydrophobic interactions, pi-pi stacking, or changes in peptide solubility. The claim that hydrogen bonds are "essential" requires more direct evidence, such as experiments at different temperatures or with hydrogen bond-disrupting agents that do not also affect hydrophobic interactions. Additionally, the MD simulations show hydrogen bond formation but do not quantify their energetic contribution relative to other interaction types.
- **Why it matters** The mechanistic claim is the core scientific contribution of the manuscript. If the role of hydrogen bonds is overstated, the conclusions about molecular design principles may be misleading.
- **Resolution test** Perform additional experiments or simulations that systematically vary hydrogen bond strength (e.g., temperature dependence, isotopic labeling) while controlling for other interactions. Quantify the free energy contribution of hydrogen bonds relative to other interaction types in the MD simulations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological scope
- **Claim pointer** The authors use MD simulations of peptide pairs to infer mechanisms of LLPS, stating that "the interaction and association behaviors between the pairs of biomolecules are closely related to their phase separation."
- **Evidence pointer** Results, MD simulations section; Figure 3; Methods, MD simulations
- **Concern** The extrapolation from pair interactions to macroscopic phase behavior is a significant leap that requires justification. LLPS is a collective phenomenon involving many molecules, and pair interactions may not capture the essential physics, particularly for systems with multivalent interactions. The authors should either perform simulations of larger systems (e.g., multiple peptides) or provide a theoretical framework connecting pair interactions to phase behavior.
- **Why it matters** The MD simulations are used to support the mechanistic claims about hydrogen bond-mediated coacervation. If the simulation approach is not appropriate for studying LLPS, the conclusions drawn from it are not well-supported.
- **Resolution test** Perform simulations with multiple peptide copies to demonstrate that pair interactions are predictive of collective behavior, or provide a theoretical argument (e.g., based on known phase behavior of similar systems) for why pair interactions are sufficient.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Phase diagrams
- **Evidence pointer** Figure 2b, 4b
- **Issue** The phase boundaries in the diagrams appear to be determined by visual inspection of microscopy images. No statistical method for boundary determination is described.
- **Required correction** Describe the method for determining phase boundaries, including the number of independent replicates and any image analysis algorithms used. Consider providing confidence intervals for the boundaries.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** UV-Vis data
- **Evidence pointer** Supplementary Figure 9
- **Issue** The claim that Dopa is protected from oxidation in the coacervate is based on qualitative observation of the UV-Vis spectrum. Quantitative analysis (e.g., peak area or absorbance ratio) would strengthen this claim.
- **Required correction** Provide quantitative analysis of the UV-Vis spectra, including peak intensities or ratios, with appropriate statistical comparisons.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** MD simulation methods
- **Evidence pointer** Methods, MD simulations
- **Issue** The description of the simulation protocol is brief, and some parameters (e.g., the specific force field modifications for Dopa, the equilibration criteria) are not fully detailed.
- **Required correction** Provide a more complete description of the simulation setup, including force field parameters for Dopa, system size, and validation of the simulation protocol.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Generalizability
- **Affected element** Discussion of biological implications
- **Evidence pointer** Results, Discussion section
- **Issue** The authors suggest that the findings have implications for natural Mfp-5 function, but the peptide model lacks several features of the full protein (e.g., longer sequence, post-translational modifications beyond Dopa, protein-protein interactions with other Mfps).
- **Required correction** Acknowledge the limitations of the peptide model more explicitly and avoid overstating the direct relevance to natural Mfp-5 function.

## Risk / unsupported claims
- The claim that hydrogen bonds are "essential" for coacervation is not fully supported, as alternative interaction types are not systematically excluded.
- The extrapolation from pair interactions in MD simulations to macroscopic LLPS behavior is not justified.
- The calculation of interfacial energy from SFA data relies on assumptions that are not fully validated.
- The claim that the findings provide "molecular design principles" for mussel-inspired adhesives is somewhat overstated given the limited scope of the peptide model.
- The biological implications for natural Mfp-5 function are asserted without direct experimental evidence.