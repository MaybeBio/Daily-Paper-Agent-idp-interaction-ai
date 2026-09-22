## Review setup
- **Input scope** Full manuscript text (abstract, results, discussion, experimental section) without supplementary information
- **Assessment boundary** Scientific claims, methodology, and interpretation as presented in the main text; supplementary figures and methods referenced but not independently verifiable
- **Shared manuscript claim summary** The authors report that native ion mobility mass spectrometry (nMS/IM-MS) of three hnRNPs (FUS, TDP-43, hCPEB3) fused to a charge-engineered spider silk domain (NT*) reveals distinct conformational states and assembly mechanisms during pH-induced liquid-liquid phase separation (LLPS). FUS undergoes an unfolded-to-globular transition, TDP-43 forms partially disordered oligomers via N-terminal domain interactions, and hCPEB3 favors fibrillar aggregation over LLPS. Molecular dynamics simulations support these interpretations.
- **Visible evidence base** Main text figures (Figures 1-5), representative mass spectra, charge state distributions, collision cross section data, microscopy images, and simulation snapshots as described; supplementary information referenced but not provided
- **Missing materials affecting confidence** Supplementary Information (SI) containing full experimental methods, design and characterization of NT* fusion proteins, additional spectra, simulation details, and supporting analyses; raw data files; validation of NT* tag neutrality on LLPS behavior

## Reviewer
- **Overall assessment** This manuscript presents a technically ambitious application of native mass spectrometry to study protein conformations under LLPS conditions, a challenging and underexplored area. The central observation that FUS, TDP-43, and hCPEB3 exhibit distinct conformational signatures during pH-induced phase separation is potentially significant. However, several methodological concerns regarding the interpretation of nMS data for phase-separating systems, the role of the NT* tag, and the strength of the simulation-to-experiment link require careful consideration. The claims are intriguing but not fully established from the provided evidence.
- **Who would be interested in the results, and why** Researchers studying LLPS and membraneless organelles, biophysicists interested in protein conformational dynamics, mass spectrometrists developing methods for challenging protein systems, and structural biologists studying hnRNP assembly. The work could inform understanding of how sequence and domain architecture dictate assembly outcomes in neurodegeneration-related proteins.
- **Major strengths** 
  1. Addresses a significant gap: structural information on proteins during LLPS is scarce, and nMS offers a unique window into soluble species in equilibrium with condensates.
  2. The use of a pH-responsive NT* fusion tag to enable native purification of aggregation-prone hnRNPs is creative and potentially broadly useful.
  3. The comparative approach across three hnRNPs with similar domain architectures but distinct assembly behaviors is well conceived.
  4. Integration of experimental nMS data with MD simulations provides a multi-scale perspective.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental design and controls
- **Claim pointer** "We found that fusion of hnRNPs to a charge-engineered NT domain (NT*) prevented unwanted aggregation yet did not have a discernable effect on LLPS"
- **Evidence pointer** Results section "Assembly of FUS and TDP-43 into Liquid Droplets Can Be Observed by nMS"; reference to SI for details
- **Concern** The claim that NT* does not affect LLPS is central to the validity of all subsequent measurements, yet the evidence is relegated to the SI and not presented in the main text. The authors state that NT* "prevented unwanted aggregation" but do not show comparative data on untagged proteins or demonstrate that the phase behavior of NT*-tagged proteins faithfully recapitulates that of the native proteins. Given that the tag is charge-engineered and pH-responsive, it could plausibly alter the very conformational equilibria being measured.
- **Why it matters** If NT* alters the conformational preferences or assembly pathways of the hnRNPs, then the distinct behaviors attributed to FUS, TDP-43, and hCPEB3 may be artifacts of the tag rather than intrinsic properties. The entire comparative framework depends on NT* being a neutral observer.
- **Resolution test** Provide quantitative comparison of LLPS phase diagrams (e.g., saturation concentrations, droplet morphology, reversibility) for NT*-tagged versus untagged proteins where feasible, or for NT* alone. Show that NT* does not itself undergo pH-dependent conformational changes that could confound the nMS measurements. Present this data in the main text or make the SI evidence compelling and explicitly referenced.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Data interpretation and methodology
- **Claim pointer** "By combining nMS with IM, we can determine the collision cross section (CCS) of the ionized proteins, and in this manner obtain insights into the conformational preferences and relative stabilities of disordered proteins in the gas phase, and how they are related to solution structures"
- **Evidence pointer** Results section "FUS and TDP-43 Exhibit Distinct Conformational Signatures during LLPS"; Figures 2a-d
- **Concern** The interpretation of nMS/IM-MS data for proteins that are in equilibrium with a condensed phase is not straightforward. The authors state that at pH 7.5, "the majority of the protein is incorporated into droplets while leaving a small population of soluble monomers" for FUS, yet they also report that the nMS signal at this pH was too low for reliable CCS determination. For TDP-43, they interpret the presence of dimers and trimers as "soluble species in equilibrium with the condensed state." However, the electrospray process can itself induce oligomerization or compaction artifacts, and the relationship between gas-phase CCS and solution-phase conformation is particularly uncertain for disordered proteins. The authors do not address how the act of electrospraying from a solution near the phase boundary might perturb the equilibrium or produce artifactual species.
- **Why it matters** The central claims about distinct conformational states during LLPS rest on the assumption that nMS faithfully reports on solution-phase populations. If electrospray ionization selectively enriches certain conformers or induces assembly artifacts, the conclusions about FUS compaction and TDP-43 oligomerization could be incorrect.
- **Resolution test** Provide control experiments demonstrating that the observed charge state distributions and CCS values are stable across different electrospray conditions (e.g., varying capillary voltage, source temperature, concentration). Show that the oligomers observed for TDP-43 are not formed during the electrospray process by, for example, varying the distance between the sample and the ionization source or using a different ionization method. Discuss how the gas-phase measurements relate to solution-phase conformations, citing relevant validation studies.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Computational modeling validation
- **Claim pointer** "To understand how the specific structural preferences of FUS and TDP-43 mediate self-assembly, we devised a hybrid strategy combining AlphaFold2 (AF2) structure prediction and molecular dynamics (MD) simulations"
- **Evidence pointer** Results section "Structural Modeling Reveals Assembly Mechanisms"; Figures 3a-b, S4
- **Concern** The MD simulations are used to support mechanistic interpretations, but the validation of these simulations is not described in the main text. For FUS, a single 500 ns all-atom simulation is mentioned, which is short for a disordered protein of this size. For TDP-43, coarse-grained simulations with the AWSEM force field are described, but the choice of force field parameters, the equilibration protocol, and the convergence criteria are not stated. The authors claim that "the C-terminal LCDs consistently fold into β-sheet-rich structures," but without information on the number of independent simulations, the statistical significance of this observation cannot be assessed.
- **Why it matters** The simulations are used to propose specific structural models (e.g., the "corkscrew" arrangement of TDP-43 NTDs, the polar organization of FUS). If the simulations are not well-converged or validated, these models are speculative and could mislead the interpretation of the experimental data.
- **Resolution test** Provide details on simulation convergence (e.g., RMSD vs. time, replica analysis), the number of independent runs, and validation against known experimental data (e.g., SAXS profiles for TDP-43, chemical shift data for FUS). Show that the key structural features (β-sheet formation in TDP-43 LCDs, FUS compaction) are robust across multiple simulation conditions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability and scope of claims
- **Claim pointer** "The divergent assembly mechanisms revealed by ion mobility mass spectrometry of soluble protein species that exist under LLPS conditions suggest structurally distinct complexes inside liquid droplets that may impact RNA processing and translation depending on biological context."
- **Evidence pointer** Abstract; Discussion section
- **Concern** The authors extrapolate from soluble species detected by nMS to the structure of complexes "inside liquid droplets." This is a significant inferential leap. The nMS measurements are performed on the soluble fraction, not on material within droplets. The relationship between the conformations of soluble species and the organization of proteins within a condensed phase is not established. Additionally, the claim that these distinct assembly mechanisms "may impact RNA processing and translation" is speculative and not supported by any functional data in the manuscript.
- **Why it matters** The broader significance of the work depends on the relevance of the observed soluble species to the functional properties of phase-separated compartments. If the soluble species are not representative of the assembled state, the biological implications are unclear.
- **Resolution test** Either provide direct evidence linking the soluble species to droplet structure (e.g., by comparing nMS data with measurements on material extracted from droplets, or by using complementary techniques such as solid-state NMR or cryo-EM on condensed phases) or temper the claims to be explicitly about soluble species in equilibrium with condensates, without asserting direct structural relevance to the droplet interior.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and reproducibility
- **Affected element** Experimental methods
- **Evidence pointer** Experimental Section; "Full experimental methods are given in the Supplementary Information File"
- **Issue** The main text provides no experimental details whatsoever, including protein expression and purification conditions, nMS instrument parameters, or simulation software versions. While SI is common for methods, the complete absence of any methodological detail in the main text makes it difficult for a reader to assess the quality of the work without accessing the SI.
- **Required correction** Include a brief summary of key experimental conditions in the main text (e.g., protein concentrations, buffer compositions, nMS instrument type, simulation packages) and ensure the SI is comprehensive and accessible.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Figure quality and data presentation
- **Affected element** Figures 1-5
- **Evidence pointer** Results section; Figures 1-5
- **Issue** The figures are described in the text but not shown in the provided manuscript. It is not possible to assess the quality of the mass spectra, the clarity of the microscopy images, or the interpretability of the simulation snapshots. Additionally, the authors reference Figure S4 multiple times but do not describe its content in the main text.
- **Required correction** Ensure all figures are of publication quality with clear labels and legends. Provide a brief description of each supplementary figure in the main text when referenced.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical analysis
- **Affected element** Quantitative claims
- **Evidence pointer** Results section; "we found that around 60% of the protein remains in the dilute phase after centrifugation at pH 7.5"
- **Issue** The manuscript reports quantitative values (e.g., 60% dilute phase, CCS values) without error bars, number of replicates, or statistical tests. It is unclear whether these values are from single experiments or represent averages with associated variability.
- **Required correction** Provide measures of variability (e.g., standard deviation, standard error) and the number of independent replicates for all quantitative claims. Where appropriate, apply statistical tests to support comparative statements.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction and Discussion
- **Evidence pointer** Introduction; Discussion
- **Issue** The authors state that "structural information about their assembled states is still lacking" and that "NMR spectroscopy has provided valuable information," but the discussion of prior structural work on FUS, TDP-43, and hCPEB3 is brief. A more thorough comparison with existing structural and biophysical data on these proteins would strengthen the novelty claims.
- **Required correction** Expand the discussion of prior structural studies on these hnRNPs, including NMR, cryo-EM, and computational work, and explicitly state how the current findings advance beyond what is known.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology precision
- **Affected element** Abstract and Discussion
- **Evidence pointer** Abstract; Discussion
- **Issue** The term "droplet architectures" in the title and abstract implies a detailed structural characterization of the condensed phase, but the manuscript primarily reports on soluble species. This overstates the scope of the findings.
- **Required correction** Revise the title and abstract to more accurately reflect that the work describes conformational states of soluble species under LLPS conditions, rather than the architecture of the droplets themselves.

## Risk / unsupported claims
- The claim that NT* has "no discernable effect on LLPS" is not verifiable from the main text and is only referenced to the SI.
- The assertion that nMS-detected soluble species are representative of the structure of proteins within liquid droplets is unsupported.
- The statement that "the observed structural plasticities are specific for each hnRNP and unlikely to be affected by the NT* domain" is an assertion without direct comparative evidence.
- The functional implications for "RNA processing and translation depending on biological context" are speculative and not tested.
- The claim that TDP-43 dimers and trimers represent "biologically relevant assembly intermediates" is inferred from in vitro data and MD simulations without direct biological validation.
- The MD simulation results, including the "corkscrew" arrangement and β-sheet formation in LCDs, are presented without sufficient validation details to assess their reliability.