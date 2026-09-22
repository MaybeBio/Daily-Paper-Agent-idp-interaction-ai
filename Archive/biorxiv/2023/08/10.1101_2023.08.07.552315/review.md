## Review setup
- **Input scope** Full manuscript text including abstract, main text, results, methods, and supplementary figure legends
- **Assessment boundary** Scientific content, technical soundness, structural biology methods, functional validation, and claims as presented in the provided manuscript
- **Shared manuscript claim summary** The authors present a cryo-EM reconstruction of an 8-subunit human KMN network subcomplex at 4.5 Å resolution, combined with AlphaFold2 modelling, to generate a comprehensive model of the KMN network. They identify and validate two interaction interfaces linking Mis12C to Ndc80C and Knl1C, demonstrate cooperative stabilization of the KMN assembly through targeted mutations and molecular dynamics simulations, and propose a mechanism for phosphorylation-regulated conformational switching of the Mis12C heads that facilitates CENP-C binding.
- **Visible evidence base** Cryo-EM reconstruction at 4.5 Å, ITC binding measurements, BLI binding measurements, cell-based localization assays, MD simulations, AlphaFold2 predictions, size-exclusion chromatography
- **Missing materials affecting confidence** The manuscript states that maps and coordinates "will be deposited in the appropriate databanks before publication" but they are not yet available for verification. Supplementary figures are referenced but not fully provided in the submitted text. The companion study by Yatskevich, Barford and co-workers is mentioned but not accessible for comparison. Specific statistical details for cell-based assays and replicate numbers are not fully described.

## Reviewer
- **Overall assessment** This manuscript addresses a fundamental question in chromosome segregation biology: how the KMN network, the core microtubule-binding machinery of the kinetochore, is assembled and how it transmits force. The authors combine cryo-EM, AlphaFold2 modelling, biophysical measurements, cell biology, and MD simulations to generate a comprehensive structural model of the human KMN network. The work is technically ambitious and the integration of multiple approaches is commendable. However, several concerns regarding the resolution of the cryo-EM map, the validation of the AlphaFold2-based conclusions, the interpretation of the MD simulations, and the strength of the functional claims need to be addressed before the case is fully established.

- **Who would be interested in the results, and why** Cell biologists studying mitosis and chromosome segregation, structural biologists interested in large macromolecular complexes, biophysicists studying force transmission in protein assemblies, and researchers working on kinetochore function and spindle assembly checkpoint signaling. The work provides a framework for understanding how the KMN network integrates mechanical and biochemical signals during cell division.

- **Major strengths** The study tackles a challenging and important problem with a multi-pronged approach. The combination of cryo-EM with AlphaFold2 predictions is timely and appropriate for a complex with inherent flexibility. The functional validation of specific interface residues through mutagenesis, both in vitro and in cells, strengthens the structural conclusions. The MD simulations provide a plausible mechanistic explanation for the observed cooperative binding. The identification of ZWINT and KNL1 as paralogs is an interesting evolutionary insight.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of structural model
- **Claim pointer** The manuscript claims a cryo-EM reconstruction of the KMN subcomplex at 4.5 Å resolution that reveals all intra-KMN interfaces relevant to assembly.
- **Evidence pointer** Results section "Structure determination of the human KMN network", Figure 1, Figure 1 – Supplement 1
- **Concern** The reconstruction is reported at 4.5 Å resolution, which is generally insufficient to unambiguously assign side-chain conformations and precise hydrogen bonding patterns at protein-protein interfaces. The authors state that the map "does not extend to this resolution in all directions due to heavily preferred orientations." This anisotropic resolution is a significant limitation. The manuscript does not provide local resolution estimates, Fourier shell correlation curves with gold-standard FSC criteria, or directional resolution assessments. Without these, it is difficult to evaluate the reliability of the interface models derived from this map. The authors rely heavily on AlphaFold2 to complement the experimental map, but the manuscript does not clearly delineate which parts of the model are experimentally constrained versus purely predicted.
- **Why it matters** The central claims of the paper rest on the accuracy of the identified interfaces between Mis12C and KNL1, and Mis12C and SPC24/SPC25. If the experimental map is of limited resolution and anisotropic, the confidence in these interfaces is correspondingly reduced. The distinction between experimentally determined and computationally predicted structural features is critical for the reader to assess the strength of the conclusions.
- **Resolution test** Provide gold-standard FSC curves, local resolution maps, and directional resolution plots. Clearly indicate in the model which regions are constrained by experimental density and which are derived from AlphaFold2. If possible, validate key interface residues with higher-resolution data on smaller subcomplexes or with cross-linking mass spectrometry.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Functional validation of the proposed conformational switch
- **Claim pointer** The manuscript proposes that phosphorylation of DSN1 at Ser100/Ser109 weakens the closed state of the Mis12C heads by modifying the charge balance in a region where the DSN1 80-112 segment binds, thereby facilitating CENP-C binding.
- **Evidence pointer** Results section "Overall appearance of KMN network", Figure 1 – Supplement 2
- **Concern** This is a key mechanistic claim, but the experimental evidence is indirect. The authors state that the experimental map is "not sufficiently well-resolved in this region to pinpoint the exact position of the DSN1 phosphorylation loop" and rely on an AlphaFold2 prediction for the critical "gluing" interaction. No direct biochemical experiment testing the effect of phosphorylation on the open-closed equilibrium of the Mis12C heads is presented. The cell-based experiments with phosphomimetic or phosphodead mutants are not described. The claim that phosphorylation "may therefore weaken the closed state" is presented as a hypothesis, but the manuscript does not clearly frame it as such in the abstract or conclusions.
- **Why it matters** The phosphorylation-regulated conformational switch is presented as a significant insight into kinetochore assembly regulation. If this is not directly tested, the claim is speculative and should be clearly labeled as such. The distinction between a structural observation and a functional mechanism is crucial for the reader.
- **Resolution test** Perform direct binding assays (e.g., ITC or BLI) comparing the affinity of CENP-C for Mis12C in the presence and absence of DSN1 phosphorylation (using phosphomimetic S>D or S>E mutants, or in vitro phosphorylation with Aurora B). Test whether phosphomimetic DSN1 mutants show enhanced CENP-C binding and whether the proposed "gluing" interaction is disrupted. Alternatively, use HDX-MS to compare the conformational dynamics of the heads in the phosphorylated and unphosphorylated states.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of MD simulations
- **Claim pointer** The MD simulations demonstrate that the mutual organization of KNL1 and Ndc80C stabilizes the KMN network, and that binding of KNL1 shifts Mis12C into an unshielded straight conformation that prepares it for binding to SPC24/SPC25.
- **Evidence pointer** Results section "Mutual influence of KNL1 and Ndc80C on their kinetochore localization stability", Figure 4, Figure 4 – Supplement 1
- **Concern** The MD simulations are performed on a truncated fragment of the Mis12C helical bundle with only the C-terminal headgroups of SPC24/SPC25 and KNL1. The simulation time is 500 ns per replica, which is short for capturing conformational transitions in large assemblies. The observed "straightening" of DSN1 upon KNL1 binding is a subtle effect, and the principal component analysis shows only ~33% of the variance captured by the first component. The manuscript does not provide error bars or statistical significance tests for the differences in RMSF or solvent accessibility between the systems. The connection between these in silico observations and the in vivo localization data is correlative.
- **Why it matters** The MD simulations are used to provide a mechanistic explanation for the cooperative binding observed experimentally. If the simulations are underpowered or the effects are not statistically robust, the mechanistic model is weakened.
- **Resolution test** Provide statistical analysis of the MD data (e.g., block averaging, bootstrapping) to demonstrate that the observed differences are significant. Consider longer simulations or enhanced sampling methods. Ideally, validate the predicted "straightening" with an experimental technique such as FRET or double electron-electron resonance (DEER) spectroscopy on labeled Mis12C constructs.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Completeness of the functional validation
- **Claim pointer** The manuscript claims that targeted interference experiments validate the two interaction interfaces linking Mis12C to Ndc80C and Knl1C.
- **Evidence pointer** Results sections "The Mis12C/KNL1 interaction" and "The Mis12C/Ndc80C interaction", Figures 2 and 3
- **Concern** The cell-based localization experiments show that mutants disrupting the Mis12C/KNL1 interface abolish KNL1 localization, and mutants disrupting the Mis12C/Ndc80C interface reduce Ndc80C levels by ~50%. However, the manuscript does not report whether these mutants affect chromosome segregation, mitotic timing, or cell viability. The functional consequence of the reduced Ndc80C recruitment is not assessed. The claim of "functional validation" is therefore limited to localization, not to function.
- **Why it matters** The title and abstract emphasize "force transmission" and "function." If the functional consequences of the identified interfaces are not tested beyond localization, the claim of functional validation is overstated.
- **Resolution test** Perform live-cell imaging to assess chromosome alignment, segregation errors, and mitotic timing in cells expressing the interface mutants. If possible, measure the strength of microtubule attachment or the response to tension using established assays.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Model completeness and generalizability
- **Claim pointer** The manuscript presents a "comprehensive model of the KMN network" and claims it "elucidates a path of microtubule-generated force transmission."
- **Evidence pointer** Results section "A comprehensive model of the KMN network", Figure 7
- **Concern** The model is built from a cryo-EM reconstruction that lacks density for ZWINT and the KNL1 region preceding the RBD domains. The ZWINT/KNL1 complex is modelled entirely by AlphaFold2. The full-length KNL1 contains a long disordered region (~700 nm contour length) that is not included in the model. The path of force transmission is inferred from the static model and the MD simulations, but no direct measurement of force transmission is presented. The model is for the human complex, and the generalizability to other species is only addressed through AlphaFold2 predictions of orthologous complexes, which are not experimentally validated.
- **Why it matters** The claim of a "comprehensive model" and "elucidation of a path of force transmission" is strong. If key components are missing or modelled purely computationally, the model is not comprehensive, and the force transmission path is a hypothesis.
- **Resolution test** Clearly state the limitations of the model in the text. If possible, obtain experimental data on the ZWINT/KNL1 complex, perhaps by using a longer KNL1 construct or by cross-linking. For the force transmission claim, either soften the language or provide direct experimental evidence, such as optical tweezers measurements or FRET-based tension sensors.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure presentation
- **Affected element** Figure 1 – Supplement 1
- **Evidence pointer** Figure 1 – Supplement 1a-d
- **Issue** The figure legend for the cryo-EM data processing workflow is not fully described in the provided text. The authors reference "Figure 1 – Supplement 1a-d" but the details of the processing pipeline, including the number of particles at each step, the final particle count, and the resolution estimation method, are not clearly stated in the main text.
- **Required correction** Provide a more detailed description of the cryo-EM data processing workflow in the main text or in the supplementary figure legend, including the number of particles, the final map resolution, and the gold-standard FSC criterion used.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figures 2, 3, and 4
- **Evidence pointer** Figures 2c, 3c, 4c
- **Issue** The ITC and BLI measurements report dissociation constants, but the number of replicates and the error bars are not clearly indicated in the figure legends. For the cell-based localization experiments, the number of cells analyzed and the statistical test used are not stated.
- **Required correction** Add the number of replicates and error bars to all quantitative measurements. State the statistical tests used and the significance thresholds in the figure legends.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract and Results
- **Evidence pointer** Abstract, Results section "Overall appearance of KMN network"
- **Issue** The term "KMN network" is used throughout, but the manuscript also introduces "KMN hub" for the truncated MD simulation system. The relationship between the "KMN hub" and the full KMN network should be clarified to avoid confusion.
- **Required correction** Define "KMN hub" clearly in the text and explain how it relates to the full KMN network.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data availability section
- **Evidence pointer** Data availability section
- **Issue** The data availability statement says maps and coordinates "will be deposited in the appropriate databanks before publication." This is not sufficient for a manuscript that relies heavily on structural data. Reviewers and readers need access to the maps and models to evaluate the claims.
- **Required correction** Deposit the maps and coordinates in a public database (e.g., EMDB and PDB) and provide the accession numbers in the manuscript.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Results and Discussion
- **Evidence pointer** Results and Discussion section
- **Issue** The manuscript does not have a dedicated Discussion section. The Results and Discussion section is combined, but the limitations of the study are not explicitly discussed. For example, the anisotropic resolution of the cryo-EM map, the reliance on AlphaFold2 for key parts of the model, and the lack of direct force measurements are not acknowledged.
- **Required correction** Add a paragraph in the Results and Discussion section that explicitly discusses the limitations of the study and the caveats of the interpretations.

## Risk / unsupported claims
- The claim that the model "elucidates a path of microtubule-generated force transmission" is not directly supported by experimental evidence. The path is inferred from the static structure and MD simulations, but no functional assay directly measuring force transmission is presented.
- The claim that phosphorylation of DSN1 "may therefore weaken the closed state of the heads" is presented as a mechanism, but no direct biochemical or cell-based experiment testing this hypothesis is described.
- The claim that the KMN model is "comprehensive" is overstated given that the ZWINT/KNL1 complex is modelled entirely by AlphaFold2 and the long disordered region of KNL1 is not included.
- The functional validation of the interfaces is limited to localization assays; the functional consequences for chromosome segregation or mitotic progression are not assessed.
- The generalizability of the model to other species is based on AlphaFold2 predictions that are not experimentally validated.