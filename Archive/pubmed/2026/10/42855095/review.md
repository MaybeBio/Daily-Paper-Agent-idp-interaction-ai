## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors report a systematic investigation of interactions between casein and three yogurt aroma compounds (acetoin, diacetyl, acetaldehyde) using multispectroscopic techniques and molecular simulations. They claim static quenching complex formation, binding affinity ordering, thermodynamic parameters indicating hydrophobic interactions, ligand-dependent structural remodeling of casein, and identification of beta-casein as the primary binding subunit via a hydrophobic collapse mechanism.
- **Visible evidence base** Abstract text only; no numerical data tables, spectra, simulation trajectories, or methodological details are visible
- **Missing materials affecting confidence** Full manuscript, all figures and tables, experimental methods, simulation parameters, statistical analyses, and supplementary information

## Reviewer
- **Overall assessment** The abstract presents a coherent and potentially interesting study on dairy protein-flavor interactions, a topic of relevance to food science and flavor chemistry. The combination of experimental spectroscopy with molecular simulation is commendable. However, the abstract alone provides insufficient detail to evaluate the rigor of the methods, the quality of the data, or the validity of several strong mechanistic claims. The assertion of a "hydrophobic collapse mechanism" and the identification of beta-CS as the primary binding subunit require careful scrutiny of the simulation methodology, which is not visible here. The thermodynamic interpretation and the structural remodeling claims also need supporting data that are not accessible from the abstract.
- **Who would be interested in the results, and why** Researchers in food chemistry, dairy science, flavor chemistry, and protein-ligand interaction studies would find these results relevant. The work could inform targeted flavor retention strategies in fermented dairy products, which is of practical interest to the food industry. Those studying intrinsically disordered proteins and their ligand interactions may also find the structural remodeling observations of interest.
- **Major strengths** The study addresses a relevant and under-explored question about molecular mechanisms of aroma binding to casein. The combination of multiple spectroscopic techniques with molecular dynamics simulations is a robust methodological approach. The comparative analysis of three aroma compounds with different functional groups provides a useful framework for understanding structure-activity relationships.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
  - R1-M4
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1 (simulation methodology), R1-M2 (thermodynamic interpretation), R1-M3 (structural remodeling evidence)
- **Assessment against Nature-style criteria** Originality: The topic is not entirely novel, as protein-flavor interactions have been studied previously, but the specific focus on casein with these three aroma compounds and the combined experimental-simulation approach offers some originality. Scientific importance: Moderate; the findings could have practical implications for dairy flavor management, but the broader biological significance is limited. Interdisciplinary readership: The work sits at the interface of food science, biophysics, and computational chemistry, which could attract readers from multiple fields, though the appeal to a general scientific audience is limited. Technical soundness: Cannot be fully assessed from the abstract alone; the simulation methodology and spectroscopic data analysis require careful evaluation. Readability for nonspecialists: The abstract is reasonably clear, though some terms (e.g., "hydrophobic collapse mechanism") may be opaque to readers outside the field.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents interesting claims, but the evidence base is insufficient to assess their validity. A full review of the manuscript would be required to determine whether the technical concerns can be resolved.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that molecular docking and 100-ns molecular dynamics simulations identified beta-CS as the primary binding subunit, which utilizes its highly flexible N-terminal domain to dynamically encapsulate aroma molecules via a hydrophobic collapse mechanism.
- **Evidence pointer** Abstract only; simulation details not provided
- **Concern** The abstract provides no information about the simulation methodology, including force field parameters, water model, simulation temperature and pressure coupling, equilibration protocol, or analysis methods. The claim of a "hydrophobic collapse mechanism" is a specific mechanistic assertion that requires careful validation through free energy calculations, contact analysis, or other quantitative measures. Additionally, the identification of beta-CS as the "primary binding subunit" implies a comparative analysis with other casein subunits, but no such comparison is described.
- **Why it matters** Molecular dynamics simulations are highly sensitive to methodological choices. Without details on the simulation setup and validation, the mechanistic claims cannot be evaluated. The "hydrophobic collapse" terminology implies a specific folding or binding pathway that may not be supported by a single 100-ns trajectory, which is relatively short for capturing such processes.
- **Resolution test** The full manuscript must provide complete simulation parameters, validation of system equilibration, convergence analysis, and quantitative evidence (e.g., binding free energies, contact maps, radius of gyration analysis) supporting the hydrophobic collapse mechanism. Comparative simulations with other casein subunits or a justification for focusing on beta-CS must be provided.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors report thermodynamic evaluation (DeltaG < 0, DeltaH > 0, DeltaS > 0) revealing a spontaneous, endothermic binding process driven predominantly by hydrophobic interactions.
- **Evidence pointer** Abstract only; thermodynamic data not shown
- **Concern** The thermodynamic parameters are reported as ranges across temperatures (298-310 K), but the abstract does not specify how these were derived. The interpretation of positive DeltaH and DeltaS as indicative of hydrophobic interactions is a common but potentially oversimplified interpretation. Other contributions, such as conformational changes in the protein or release of ordered water molecules, could also produce similar thermodynamic signatures. The abstract does not address potential contributions from electrostatic interactions, hydrogen bonding, or changes in protonation state.
- **Why it matters** The thermodynamic interpretation forms a central pillar of the mechanistic conclusions. If the analysis is incomplete or the interpretation is oversimplified, the conclusion that hydrophobic interactions dominate could be misleading. This has direct implications for understanding the molecular basis of aroma retention in dairy matrices.
- **Resolution test** The full manuscript must show the van't Hoff or isothermal titration calorimetry data from which the thermodynamic parameters were derived, including error estimates. A more nuanced discussion of the molecular origins of the thermodynamic signatures, potentially supported by simulation data, is required.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that spectroscopic and morphological characterizations demonstrated divergent, ligand-dependent structural remodeling within the intrinsically disordered CS matrix, with ketone ligands triggering structural uncoiling and granular aggregation, whereas acetaldehyde promoted compact intermolecular cross-linking.
- **Evidence pointer** Abstract only; spectroscopic and morphological data not shown
- **Concern** The abstract reports qualitative differences in structural remodeling without providing quantitative measures. Terms such as "significant structural uncoiling," "granular aggregation," and "compact intermolecular cross-linking" are descriptive but lack numerical support. The claim that casein is an "intrinsically disordered" matrix is itself a strong statement that requires justification, as casein has been described as having a rheomorphic or natively unfolded structure, but the degree of disorder is context-dependent.
- **Why it matters** The structural remodeling claims are central to the novelty of the work. Without quantitative data (e.g., secondary structure percentages from circular dichroism, particle size distributions, or microscopy image analysis), these claims cannot be evaluated. The distinction between the effects of ketones versus aldehyde is an important finding that needs robust statistical support.
- **Resolution test** The full manuscript must provide quantitative spectroscopic data (e.g., CD spectra with secondary structure deconvolution, FTIR amide I band analysis) and morphological data (e.g., particle size distributions, microscopy images with scale bars and statistical analysis) supporting the claimed differences. Statistical significance testing must be reported.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** The authors report binding affinities following the order acetoin > diacetyl > acetaldehyde, with K(a) ranging from 1.12 x 10(3) to 2.82 x 10(3) L.mol(-1) at 298-310 K.
- **Evidence pointer** Abstract only; binding data not shown
- **Concern** The binding constants are reported with only two significant figures and a range across temperatures, but the abstract does not specify the number of replicates, the error margins, or the fitting model used to extract these values from the fluorescence quenching data. The K(q) value of approximately 10(11) L.mol(-1).s(-1) is reported as evidence for static quenching, but the threshold for distinguishing static from dynamic quenching is typically 10(10) L.mol(-1).s(-1), so this value is close to the boundary and requires careful statistical treatment.
- **Why it matters** Binding constants are quantitative measures that underpin the comparative analysis. If the errors are large or the fitting model is inappropriate, the reported ordering of binding affinities may not be robust. The proximity of K(q) to the static-dynamic boundary raises questions about the certainty of the quenching mechanism assignment.
- **Resolution test** The full manuscript must provide the fluorescence quenching data with error bars, the fitting equations used, the number of replicates, and a statistical comparison of the binding constants across the three ligands. A discussion of the K(q) value relative to the static-dynamic quenching threshold is required.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract terminology
- **Evidence pointer** Abstract, first sentence
- **Issue** The abbreviation "CS" for casein is introduced without definition. While common in the field, the abstract should define the abbreviation at first use.
- **Required correction** Define "casein (CS)" at first mention.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Abstract methods description
- **Evidence pointer** Abstract, methods description
- **Issue** The abstract mentions "multispectroscopic techniques" without specifying which techniques were used. This is vague and does not allow the reader to assess the appropriateness of the methods.
- **Required correction** Specify the spectroscopic techniques used (e.g., fluorescence, UV-vis, circular dichroism, FTIR) in the abstract.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Precision
- **Affected element** Abstract quantitative claims
- **Evidence pointer** Abstract, binding affinity statement
- **Issue** The binding constants are reported as a range (1.12 x 10(3) to 2.82 x 10(3) L.mol(-1)) without specifying which temperature corresponds to which value or providing uncertainties. This limits the interpretability of the data.
- **Required correction** Report binding constants with uncertainties and specify the temperature for each value, or state that the range spans the temperature interval studied.

## Risk / unsupported claims
- The claim of a "hydrophobic collapse mechanism" for aroma encapsulation by beta-CS is unsupported from the abstract alone, as no simulation analysis details are provided.
- The identification of beta-CS as the "primary binding subunit" is unsupported without comparative data on other casein subunits.
- The claim that casein is an "intrinsically disordered" matrix is asserted without supporting evidence or citation.
- The thermodynamic interpretation of hydrophobic dominance is plausible but not fully supported without additional data on other interaction types.
- The structural remodeling differences between ketone and aldehyde ligands are described qualitatively and cannot be evaluated without quantitative data.
- The static quenching mechanism assignment is based on a K(q) value near the conventional threshold and requires statistical validation.