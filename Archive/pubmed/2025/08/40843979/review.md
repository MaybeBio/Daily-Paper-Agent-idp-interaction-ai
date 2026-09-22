## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, materials and methods, and supplementary figure/table references.
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided manuscript. No external validation or replication of data was performed.
- **Shared manuscript claim summary** The authors report that the GKAP scaffold protein, containing two closely spaced noncanonical LC8-binding motifs, forms a hexameric complex with LC8 dimers (2 GKAP:2 LC8 dimers). They claim the LC8-binding segment of GKAP is intrinsically disordered, the linker between binding sites retains flexibility in the complex, and molecular dynamics simulations suggest dynamic, transient interactions between LC8 dimers and flanking regions, potentially explaining the fixed stoichiometry.
- **Visible evidence base** NMR chemical shift assignments (BMRB: 52712), NMR titration data (forward and reverse), far-UV CD spectra, size exclusion chromatography, dynamic light scattering, biolayer interferometry, and molecular dynamics simulations.
- **Missing materials affecting confidence** Raw NMR spectra, detailed titration curves with peak intensity quantifications, BLI sensorgrams, DLS size distribution plots, MD simulation convergence metrics, and force field validation details. Supplementary figures and tables referenced but not provided.

## Reviewer
- **Overall assessment** The manuscript presents a well-structured study of a multivalent IDP-hub protein complex, combining experimental and computational approaches. The central claim that a hexameric complex forms with retained flexibility in the linker region is plausible and supported by the data shown. However, several technical aspects, particularly the quantitative interpretation of NMR data and the robustness of MD simulations, require clarification before the case is fully established. The study is of interest to the IDP and multivalency community, but its broader impact is limited by the lack of functional validation.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, multivalent interactions, hub proteins, and postsynaptic density organization. The work provides a detailed biophysical characterization of a specific IDP-hub complex, which is relevant to understanding how flexibility and constrained stoichiometry coexist in biological assemblies.
- **Major strengths**
  1. The combination of multiple biophysical techniques (NMR, CD, SEC, DLS, BLI) provides a comprehensive characterization of the complex.
  2. The use of both forward and reverse NMR titrations is a rigorous approach to study binding from both perspectives.
  3. The integration of MD simulations with experimental data offers mechanistic insights into dynamic interactions.
  4. The study addresses a gap in the literature by focusing on noncanonical binding motifs and longer linker regions.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that the hexameric complex (2 GKAP:2 LC8 dimers) is the dominant species formed, based on DLS and NMR data.
  - **Evidence pointer** Results section, DLS and NMR titration data (Figures 3 and 4, location not provided)
  - **Concern** The evidence for the hexameric stoichiometry is indirect. DLS provides a hydrodynamic diameter estimate, but the conversion to molecular weight relies on assumptions about shape and hydration. The NMR data show peak disappearance, which is consistent with large complex formation, but does not definitively establish the 2:2 stoichiometry. The authors mention that the calculated molecular weight from DLS is ~56.6 kDa, but the raw DLS data and the analysis method are not shown. Additionally, the possibility of higher-order oligomers or a distribution of species is not rigorously excluded.
  - **Why it matters** The stoichiometry is a central claim of the paper. If the stoichiometry is not firmly established, the interpretation of the flexibility and dynamics within the complex is compromised.
  - **Resolution test** Provide raw DLS autocorrelation functions and size distribution plots with clear peak assignments. Include a quantitative analysis of NMR peak intensities during titration to show a clear endpoint and stoichiometry. Consider using analytical ultracentrifugation or mass photometry as orthogonal methods to confirm the molecular weight of the complex.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors state that the linker region between the two LC8-binding sites remains largely flexible in the complex, based on NMR chemical shift perturbations and MD simulations.
  - **Evidence pointer** Results section, Figure 5 (location not provided)
  - **Concern** The NMR data show that peaks in the linker region remain visible, but the chemical shift perturbation values are not quantified or compared to a threshold for significant change. The statement that the linker is "largely retained" in flexibility is qualitative. The MD simulations show flexibility, but the sampling time (200 ns) may be insufficient to capture the full conformational ensemble of a 17-residue linker. The authors do not provide a quantitative measure of flexibility (e.g., order parameters, RMSF) from the simulations.
  - **Why it matters** The claim of retained flexibility is a key finding that distinguishes this system from more rigid multivalent complexes. Without quantitative evidence, the claim is not fully supported.
  - **Resolution test** Provide a plot of chemical shift perturbations as a function of residue number with a clear threshold for significance. From MD simulations, provide root-mean-square fluctuation (RMSF) or order parameter profiles for the linker region, and compare to the free state. Consider longer simulations or enhanced sampling methods to ensure convergence.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Claim pointer** The authors suggest that the dynamic interactions between LC8 dimers and flanking regions may explain the fixed stoichiometry of the complex.
  - **Evidence pointer** Discussion section, Figure 6 (location not provided)
  - **Concern** This is presented as a speculative explanation. While the MD simulations show potential contacts, there is no experimental validation of these specific interactions. The authors do not test this hypothesis, for example, by mutating residues predicted to be involved in these contacts and measuring the effect on complex formation or stoichiometry.
  - **Why it matters** The proposed mechanism is interesting but remains a hypothesis. Without experimental testing, its significance is limited.
  - **Resolution test** Perform mutagenesis on residues predicted to mediate LC8-LC8 or LC8-flanking region contacts and assess the impact on complex stoichiometry and dynamics using the same biophysical methods.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Introduction
  - **Evidence pointer** Introduction, first paragraph
  - **Issue** The introduction assumes familiarity with IDP and hub protein concepts. A brief explanation of why multivalent IDP-hub interactions are biologically important would improve accessibility.
  - **Required correction** Add a sentence or two explaining the general significance of IDP-hub interactions in cellular processes.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Materials and methods, BLI
  - **Evidence pointer** Materials and methods, Biolayer interferometry section
  - **Issue** The BLI experiment is described, but the kinetic model used for fitting is not specified. The Kd value is reported, but the association and dissociation rate constants are not given in the text.
  - **Required correction** Specify the binding model (e.g., 1:1, bivalent) and report the individual rate constants (ka, kd) with errors.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Materials and methods, MD simulations
  - **Evidence pointer** Materials and methods, Model building and MD simulations section
  - **Issue** The force field and water model are mentioned, but the temperature and pressure coupling methods, and the equilibration protocol, are not described.
  - **Required correction** Provide details on the equilibration and production run parameters, including thermostat/barostat algorithms and coupling constants.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Results, NMR titrations
  - **Evidence pointer** Results section, NMR titration description
  - **Issue** The authors state that peaks disappear but do not quantify the fraction of peaks affected or provide a residue-level map of affected vs. unaffected residues for the LC8 protein.
  - **Required correction** Provide a summary of which LC8 residues are affected by binding, perhaps as a bar chart or colored on a structure, to support the claim of widespread involvement.
- **Technical failings that need to be addressed before the case is established** R1-M1 and R1-M2 are blocking. The stoichiometry and flexibility claims require more rigorous quantitative evidence.
- **Assessment against Nature-style criteria**
  - **Originality** The study is original in its focus on a bivalent IDP with noncanonical motifs and a longer linker, which has not been characterized before. The combination of NMR and MD is not novel per se, but the application to this specific system is.
  - **Scientific importance** The findings are of moderate importance. They contribute to the understanding of multivalent IDP-hub interactions, but the broader biological implications are not explored. The study does not provide a new general principle or paradigm.
  - **Interdisciplinary readership** The work is primarily of interest to biophysicists and structural biologists. The methods and concepts are specialized, and the broader cell biology community may find the direct relevance limited.
  - **Technical soundness** The experimental design is generally sound, but the quantitative analysis of key claims (stoichiometry, flexibility) is insufficient. The MD simulations are used in a somewhat exploratory manner without rigorous validation against experimental data.
  - **Readability for nonspecialists** The manuscript is clearly written but assumes significant background knowledge. The abstract is accessible, but the results and discussion sections are dense.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is interesting and the data are suggestive, but the current evidence does not fully establish the central claims of hexameric stoichiometry and retained flexibility. The authors should be encouraged to provide more quantitative analyses and, ideally, experimental validation of the proposed dynamic interactions.

## Risk / unsupported claims
- The claim that the hexameric complex is the dominant species is not fully supported by the data presented; DLS and NMR peak disappearance are suggestive but not definitive.
- The claim that the linker region retains "largely" its flexibility is qualitative and not quantitatively supported.
- The suggestion that LC8-LC8 interactions contribute to the fixed stoichiometry is speculative and not experimentally tested.
- The statement that the C-terminal flanking region of the second binding site is "involved in the interaction" is based on peak disappearance, but the nature of this involvement (direct binding vs. conformational change) is not resolved.
- The comparison of Kd values across different studies (Table S1) is mentioned but the table is not provided, making the comparison unverifiable.