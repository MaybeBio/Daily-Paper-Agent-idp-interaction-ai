## Review setup
- **Input scope** Full manuscript text including abstract, methods, results, discussion, and data availability statements
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided manuscript
- **Shared manuscript claim summary** The authors identify YbiB as a novel interactor of the E. coli GTPase ObgE, characterize the interaction biochemically and structurally, and demonstrate that ObgE competes with DNA for binding to YbiB, suggesting a potential link to the SOS response and bacterial persistence
- **Visible evidence base** Photocrosslinking, bacterial two-hybrid, pull-down assays, ITC, SEC-MALS, SEC-SAXS, CD spectroscopy, molecular docking, X-ray crystallography, steady-state kinetics, EMSA, and persistence assays
- **Missing materials affecting confidence** Supplementary figures, tables, and methods referenced but not provided; raw data and statistical details for several experiments; full details of photocrosslinking procedure and mass spectrometry results

## Reviewer
- **Overall assessment** This manuscript presents a thorough and well-executed characterization of a novel protein-protein interaction between ObgE and YbiB. The combination of in vivo and in vitro approaches, along with structural and biophysical methods, provides strong evidence for the interaction and its molecular basis. The finding that ObgE competes with DNA for binding to YbiB is intriguing and potentially significant for understanding ObgE's cellular roles. However, several concerns regarding the quantitative interpretation of binding data, the physiological relevance of the interaction, and the functional implications require clarification. The manuscript is generally well-written and accessible, though some sections could benefit from additional context for non-specialist readers.

- **Who would be interested in the results, and why** Researchers studying bacterial GTPases, particularly the Obg family, will find this work directly relevant. The study also appeals to those interested in protein-DNA interactions, bacterial stress responses, and persistence mechanisms. Structural biologists studying protein-peptide interactions and intrinsically disordered regions may also find the combined docking and crystallographic approach of interest. The potential link to antibiotic persistence could attract researchers in antimicrobial development.

- **Major strengths** The study employs a comprehensive multi-technique approach, combining in vivo photocrosslinking with in vitro biophysical and structural methods. The identification of the C-terminal domain of ObgE as the key interaction driver, with specific tryptophan residues playing a critical role, is well-supported by mutagenesis and peptide studies. The crystal structure of YbiB with a bound ObgE peptide fragment provides direct structural evidence. The demonstration that ObgE competes with DNA for binding to YbiB is a significant finding with potential functional implications.

- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Data interpretation and quantitative analysis
  - **Claim pointer** The manuscript claims a biphasic binding interaction between ObgE and YbiB with KD values of 22 ± 1 nM and 5 ± 1 μM, interpreted as two sequential binding events of ObgE monomers to the YbiB dimer.
  - **Evidence pointer** Results section, ITC experiments, Figure 2B, Supplementary Table S6
  - **Concern** The interpretation of the biphasic ITC isotherm as two independent binding events with a stoichiometry of approximately 0.5 per event is not fully justified. The authors do not provide sufficient details on the fitting model, the statistical significance of the two-site model compared to alternative models, or how the stoichiometry was constrained. The claim that one ObgE monomer binds per YbiB subunit during each event requires more rigorous validation, particularly given the partial dissociation observed in SEC-MALS.
  - **Why it matters** The quantitative binding parameters are central to the manuscript's conclusions about the interaction mechanism. If the biphasic behavior is misinterpreted, the proposed model of sequential binding with negative cooperativity or overlapping sites may be incorrect, affecting the overall interpretation of the interaction.
  - **Resolution test** Provide a detailed description of the ITC fitting procedure, including the specific model equations, whether stoichiometry was fixed or floated, and statistical comparison of one-site versus two-site models. Include representative raw ITC data and fits. Consider performing ITC with the YbiB mutants to directly test the binding model.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Functional significance and physiological relevance
  - **Claim pointer** The manuscript suggests that the ObgE-YbiB interaction may link ObgE to the SOS response and bacterial persistence, based on the observation that ybiB overexpression increases persister frequency.
  - **Evidence pointer** Results section, Figure 1, Discussion
  - **Concern** The persistence data are presented with minimal statistical detail, and the physiological relevance of the interaction is not directly tested. The claim that YbiB may form a link between ObgE and the SOS response is speculative and not supported by direct experimental evidence. The authors do not test whether the interaction is required for the observed persistence phenotype, nor do they examine the effects of the interaction on SOS response activation or DNA damage repair.
  - **Why it matters** The potential link to persistence and the SOS response is a major motivation for the study and a key point of interest for the broader audience. Without direct functional experiments, the significance of the interaction beyond its biochemical characterization remains unclear.
  - **Resolution test** Perform experiments to directly test the functional relevance, such as measuring SOS response activation in wild-type versus ybiB deletion strains, examining the effect of ObgE on YbiB DNA binding in vivo, or testing whether the interaction affects persistence under DNA-damaging conditions. Provide statistical analysis of the persistence data with appropriate replicates.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Structural interpretation
  - **Claim pointer** The manuscript claims that the crystal structure of YbiB with a bound ObgE peptide fragment (residues 375-380) supports the docking predictions and reveals the binding site within the positively charged grooves.
  - **Evidence pointer** Results section, X-ray crystallography, Figure 4, Supplementary Table S5
  - **Concern** The crystal structure only shows a short peptide fragment (6 residues) bound to YbiB, and the authors acknowledge that the rest of the peptide is not visible in the electron density. The interpretation that this represents the full binding mode of the ObgE C-terminus may be an oversimplification, particularly given the proposed role of tryptophan residues at positions 372 and 376, which are not fully resolved in the structure.
  - **Why it matters** The structural data are used to support the proposed binding mechanism and the role of specific residues. If the visible peptide fragment does not represent the complete binding interface, the conclusions about the molecular basis of the interaction may be incomplete or potentially misleading.
  - **Resolution test** Provide a more detailed analysis of the electron density and the confidence in the placement of the peptide fragment. Discuss the limitations of the structural model and how it relates to the full-length interaction. Consider additional experiments, such as mutagenesis of residues outside the visible fragment, to validate the proposed binding mode.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Experimental detail and reproducibility
  - **Affected element** Photocrosslinking methodology
  - **Evidence pointer** Materials and Methods, Identification of ObgE interaction partners
  - **Issue** The photocrosslinking procedure is described only briefly in the main text, with details relegated to Supplementary Methods. The authors do not provide information on the efficiency of pBpa incorporation, the number of biological replicates, or the criteria for identifying YbiB as a candidate interactor from the mass spectrometry data.
  - **Required correction** Provide a summary of the photocrosslinking results, including the number of identified candidates, the confidence in YbiB identification, and any validation steps. Ensure that the Supplementary Methods contain sufficient detail for replication.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Data presentation and statistical analysis
  - **Affected element** Persistence assays
  - **Evidence pointer** Results section, Figure 1
  - **Issue** The persistence data are presented as bar graphs without indication of individual data points, error bars, or statistical significance. The number of independent experiments is not stated.
  - **Required correction** Include individual data points, error bars representing standard deviation or standard error, and statistical analysis with p-values. State the number of biological replicates.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Clarity and accessibility
  - **Affected element** Discussion of the biphasic binding model
  - **Evidence pointer** Discussion section
  - **Issue** The discussion of the possible mechanisms for the biphasic binding behavior (overlapping sites vs. allosteric regulation) is somewhat dense and may be difficult for non-specialists to follow. The authors could benefit from a clearer explanation of the models and the evidence for and against each.
  - **Required correction** Simplify the explanation of the competing models, perhaps with a schematic figure, and clearly state which model is favored and why.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Completeness of structural analysis
  - **Affected element** Crystal structure comparison
  - **Evidence pointer** Results section, X-ray crystallography
  - **Issue** The authors do not compare their apo YbiB structure with the previously published structure (PDB: 4MUO) in detail, beyond noting the resolution improvement. A quantitative comparison of the two structures would strengthen the claim of an improved model.
  - **Required correction** Provide a structural alignment and RMSD calculation between the new apo structure and 4MUO, and discuss any significant differences.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Interpretation of competition experiments
  - **Affected element** EMSA experiments
  - **Evidence pointer** Results section, Figure 6
  - **Issue** The EMSA experiments show that ObgE inhibits DNA binding to YbiB, but the authors do not test whether this inhibition is competitive or allosteric. The claim that ObgE competes with DNA for binding in the same site is inferred but not directly demonstrated.
  - **Required correction** Consider performing competition experiments with varying concentrations of both ObgE and DNA to establish the mechanism of inhibition, or acknowledge this limitation in the discussion.

## Risk / unsupported claims
- The claim that YbiB is involved in bacterial persistence is based on a single overexpression experiment with limited statistical detail; the physiological relevance is not established.
- The suggestion that the ObgE-YbiB interaction links ObgE to the SOS response is speculative and not directly tested.
- The interpretation of the biphasic ITC binding as sequential binding of two ObgE monomers with specific stoichiometry is not fully validated by the presented data.
- The functional significance of the ObgE-YbiB interaction in the context of ObgE's known cellular roles is not experimentally addressed.
- The claim that the crystal structure supports the full binding mode of the ObgE C-terminus is only partially supported, as only a short peptide fragment is visible in the electron density.