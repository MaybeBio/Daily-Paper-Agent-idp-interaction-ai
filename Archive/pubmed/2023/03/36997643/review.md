## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary figure/table legends
- **Assessment boundary** Scientific claims, methodological soundness, computational approach validity, interpretation of results, and alignment with stated conclusions
- **Shared manuscript claim summary** The authors apply a multicanonical molecular dynamics (McMD)-based dynamic docking protocol to characterize the binding mechanism between the intrinsically disordered region (IDR) of Bim and the cryptic binding site of Bcl-xL. They report that binding is initiated at the C-terminal region of Bim via a stable P4 site on Bcl-xL, followed by mutual induced-fit conformational changes in both molecules, leading to the native α-helical bound state. They also compare force fields and water models for IDR simulations and suggest new avenues for drug design targeting metastable Bcl-xL conformations.
- **Visible evidence base** Abstract, Introduction, Results (including Figures 1-5, Tables 1-3), Discussion, Methods, and references to Supplementary Figures S1-S14 and Tables S1-S9
- **Missing materials affecting confidence** Supplementary figures and tables referenced but not provided in full; specific simulation parameter details in Table S9 not visible; details of the pathing algorithm implementation not fully described; convergence metrics for McMC simulations not shown

## Reviewer
- **Overall assessment** This manuscript presents a computationally intensive study of a biologically important protein-peptide interaction system. The application of McMD-based dynamic docking to an IDP binding a cryptic site is methodologically ambitious and potentially valuable. However, several concerns regarding validation, interpretation, and the strength of the central claims need to be addressed. The claim of a "mutual induced-fit mechanism" is plausible but requires more rigorous support, particularly regarding the statistical significance of observed conformational changes and the generalizability of the findings beyond the specific simulation conditions.

- **Who would be interested in the results, and why** Researchers in computational biophysics, particularly those studying intrinsically disordered proteins and protein-protein interactions; structural biologists interested in cryptic binding sites and their role in drug discovery; and the apoptosis research community, given the therapeutic relevance of Bcl-2 family proteins in cancer. The methodological comparisons (force fields, water models) will also interest the IDP simulation community.

- **Major strengths**
  - The study addresses a challenging and biologically important problem: the binding mechanism of an IDP to a cryptic site
  - The McMD approach is well-suited for enhanced sampling of conformational space
  - The study provides a detailed, residue-level description of the binding pathway
  - The comparison of force fields and water models adds practical value for the simulation community
  - The identification of metastable Bcl-xL conformations as potential drug targets is an interesting translational insight

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation of computational predictions
- **Claim pointer** The authors claim that the McMD-based dynamic docking protocol "correctly reproduced both the IDR properties of Bim and the native bound configuration"
- **Evidence pointer** Results section, Figure 2, Table 1
- **Concern** The validation of the predicted native-like binding mode relies on comparison with a single crystal structure (PDB ID 4QVF). The RMSD of 2.79 Å for the top-ranked structure r1 is relatively high, and the authors attribute discrepancies to crystal packing effects on Phe105. However, no quantitative comparison with solution-state experimental data (e.g., NMR chemical shift perturbations, mutagenesis data) is provided to support the claim that r1 represents the solution-state native complex. The assertion that the crystal structure is "unrealistic" due to Phe105 exposure requires stronger justification, as crystal contacts are a common artifact but the specific claim here needs experimental corroboration.
- **Why it matters** The central claim of the paper is that the simulation reproduces the native binding mode. If the validation is weak, the entire mechanistic interpretation is called into question.
- **Resolution test** Provide quantitative comparison of predicted contacts with available experimental data (e.g., mutagenesis, NMR, or other biophysical data). Alternatively, perform additional simulations starting from different initial conditions to demonstrate convergence to the same native-like state. If possible, compare with other experimentally determined structures of Bcl-xL in complex with BH3 peptides.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical significance of mechanistic claims
- **Claim pointer** The authors claim a "mutual induced-fit mechanism" where "both molecules adapt to each other" during binding
- **Evidence pointer** Results section, Figure 3, Discussion
- **Concern** The description of the binding pathway is based on a single representative pathway generated by the pathing algorithm. No statistical analysis is provided to show that this pathway is representative of the ensemble of possible binding routes. The claim of "mutual induced-fit" requires demonstrating that conformational changes in Bcl-xL are induced by Bim binding (and vice versa) rather than being pre-existing conformational states that are selected. The distinction between induced-fit and conformational selection cannot be made from a single trajectory or pathway.
- **Why it matters** The mechanistic conclusion is the main scientific contribution of the paper. If the pathway is not statistically robust, the conclusion is not established.
- **Resolution test** Perform multiple independent McMD simulations or use alternative pathway sampling methods to demonstrate reproducibility of the binding mechanism. Provide quantitative analysis of the populations of open vs. closed Bcl-xL states in the absence and presence of Bim to distinguish between induced-fit and conformational selection.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Force field validation
- **Claim pointer** The authors state that the ff99SB-ILDN force field "produced a wide structural ensemble that is expected of IDPs/IDRs" and that the choice of water model had "minimal effect"
- **Evidence pointer** Results section, Figures S2-S3, S13, Tables S1-S2, S8
- **Concern** The comparison between ff14 and ff99SB-ILDN force fields is based on a single peptide (Bim) and the conclusion that ff99SB-ILDN is more appropriate for IDRs is based on the observation that it produces a more diverse ensemble. However, diversity alone does not imply accuracy. The authors note that ff99SB-ILDN produces "no preference for the structure observed in the complex," which could indicate that the force field is too unbiased or that the bound conformation is not intrinsically favored. The water model comparison is limited to a single peptide and may not generalize.
- **Why it matters** The choice of force field and water model affects the reliability of all subsequent results. If the force field is not appropriate for IDPs, the binding mechanism may be an artifact.
- **Resolution test** Validate the force field against experimental observables for Bim (e.g., chemical shifts, J-couplings, radius of gyration) if available. Compare with other IDP-specific force fields. Provide a more systematic comparison of water models across multiple IDPs.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Drug design implications
- **Claim pointer** The authors state that "our data provides new avenues to develop novel drugs by targeting newly discovered stable conformations of Bcl-xL"
- **Evidence pointer** Discussion, Figure 4-5
- **Concern** The suggestion that metastable Bcl-xL conformations (e.g., r6) could be drug targets is speculative. No analysis is provided on the druggability of these conformations, their accessibility in the cellular context, or whether small molecules could stabilize them. The relationship between the simulated conformations and those accessible in vivo is not established.
- **Why it matters** This claim extends beyond the computational results and has translational implications. Overstating the drug design potential could mislead readers.
- **Resolution test** Provide a more measured discussion of the drug design implications, or add analysis of the druggability of the identified conformations (e.g., pocket analysis, comparison with known drug binding sites).

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Methods section, Dynamic docking
- **Evidence pointer** Methods, "Dynamic docking" subsection
- **Issue** The description of the McMD implementation and the pathing algorithm is brief. The modifications made to GROMACS are mentioned but not detailed. The criteria for determining convergence of the McMD simulations are not stated.
- **Required correction** Provide additional details on the McMD implementation, convergence criteria, and the pathing algorithm. Consider including pseudocode or a more detailed algorithmic description.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical analysis
- **Affected element** Results, Tables 1-2
- **Evidence pointer** Tables 1-2
- **Issue** The tables report RMSD, R-values, and other metrics without error estimates or confidence intervals. It is unclear whether the differences between configurations are statistically significant.
- **Required correction** Provide error estimates (e.g., standard deviations from block averaging) or statistical tests to support claims of differences between configurations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 3
- **Evidence pointer** Figure 3
- **Issue** The milestone structures in Figure 3 are described in the text but the figure itself may be difficult to interpret without additional annotation. The conformational changes in Bcl-x3 and Bim are described in detail but not clearly highlighted in the figure.
- **Required correction** Add annotations or insets to Figure 3 to highlight key conformational changes and residue interactions described in the text.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction, Discussion
- **Evidence pointer** Introduction, Discussion
- **Issue** The discussion of IDP binding mechanisms could be more comprehensive. The authors mention induced-fit and conformational selection but do not cite or discuss recent work on coupled folding and binding, fuzzy complexes, or other IDP binding models.
- **Required correction** Expand the discussion to place the findings in the broader context of IDP binding mechanisms, citing relevant recent literature.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence pointer** Methods, "Computational systems"
- **Issue** The initial structure preparation is described but the specific steps for generating the 30 initial configurations (different random seeds) are not fully detailed. The equilibration protocol is also brief.
- **Required correction** Provide a more detailed description of the system preparation, equilibration, and the generation of initial configurations.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Evidence pointer** Abstract, Results
- **Issue** The term "mutual induced-fit" is used throughout but is not clearly defined. It is unclear whether this refers to a novel mechanism or a specific combination of known mechanisms.
- **Required correction** Define "mutual induced-fit" explicitly and distinguish it from other proposed mechanisms for IDP binding.

## Risk / unsupported claims
- The claim that the simulation "correctly reproduced" the native binding mode is not fully supported given the relatively high RMSD and the lack of experimental validation beyond a single crystal structure
- The claim of a "mutual induced-fit mechanism" is based on a single pathway and lacks statistical support
- The suggestion that metastable Bcl-xL conformations could be drug targets is speculative and not supported by druggability analysis
- The conclusion that ff99SB-ILDN is more appropriate than ff14 for IDR simulations is based on limited evidence (single peptide) and conflates conformational diversity with accuracy
- The claim that the water model choice had "minimal effect" is based on a single peptide comparison and may not generalize
- The statement that the pathing algorithm produces a "binding pathway" implies a kinetic interpretation that is not directly supported by the McMD approach, which provides thermodynamic rather than kinetic information