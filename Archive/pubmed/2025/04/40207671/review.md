## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and supplementary figure references.
- **Assessment boundary** Scientific content, methodological rigor, internal consistency, and support of claims by presented evidence. No assessment of grammar or style beyond readability for a general scientific audience.
- **Shared manuscript claim summary** The authors propose that physiologically relevant ions, particularly Ca2+ and Na+, modulate the conformational ensemble of monomeric alpha-synuclein, influence its aggregation kinetics, and bias the formation of distinct fibril polymorphs. They combine ThT fluorescence assays, NMR, SANS, HDX-MS, MD simulations, and AFM to support a model where Ca2+ binding at the C-terminus and Na+ nonspecific interactions extend the monomer, reduce water mobility in the hydration shell, and promote aggregation.
- **Visible evidence base** Full text of the manuscript, including all main figures (referenced as Figure 1 through Figure 6), methods section, and references to supplementary figures (Figure S2, Figure S15a-d). No supplementary data files were provided.
- **Missing materials affecting confidence** Supplementary figures and tables, raw data files, MD simulation parameter files, and the full HDX-MS dataset. The manuscript references several supplementary items that are essential for a complete evaluation of the methods and results.

## Reviewer
- **Overall assessment** This manuscript addresses a relevant and timely question in the field of synucleinopathies: how ionic conditions shape the conformational ensemble of monomeric alpha-synuclein and influence downstream aggregation and fibril polymorphism. The combination of multiple biophysical techniques is commendable and provides a multifaceted view of the system. However, the manuscript has several significant weaknesses. The link between monomer conformational changes, solvent dynamics, and aggregation kinetics is presented as a coherent model, but the evidence for a causal relationship is largely correlative. The MD simulations, while supportive, are not sufficiently described to assess their convergence or statistical significance. The AFM analysis of fibril polymorphism is qualitative and lacks the resolution to make strong claims about structural differences. The claim that Ca2+ slows water mobility in the hydration shell is based on a single simulation analysis and is not experimentally validated. Overall, the study is interesting but the case is not fully established from the provided evidence.

- **Who would be interested in the results, and why** Researchers studying alpha-synuclein aggregation, protein misfolding disorders, and the role of metal ions in neurodegeneration. The work may also be of interest to the biophysics community focused on intrinsically disordered proteins and the application of integrative structural biology approaches. The potential therapeutic angle, targeting the ionic environment or hydration shell, could attract a broader translational audience.

- **Major strengths** The use of orthogonal biophysical techniques to probe different aspects of the monomer ensemble is a clear strength. The combination of NMR, SANS, and HDX-MS provides complementary information on local binding, global shape, and regional dynamics. The inclusion of MD simulations to provide a mechanistic interpretation of the experimental data is valuable. The study addresses a physiologically relevant question, as ionic composition varies across cellular compartments and is altered in disease states.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that MD simulations show Ca2+ significantly slows down water mobility in the hydration shell of aSyn, and that this correlates with increased aggregation propensity.
- **Evidence pointer** Results section, "Modeling the aSyn Conformation Ensemble..." and Figure 5e.
- **Concern** The water persistence time analysis is presented as a key mechanistic finding, but the methods section does not provide sufficient detail on how this was calculated. The manuscript states that "water molecules in the hydration shell" were observed and "total displacement is measured every 5 ps over a period of 3 ns," but the definition of the hydration shell, the criteria for a water molecule to be considered "persistent," and the statistical treatment of the data are not described. Furthermore, the correlation between water persistence and aggregation kinetics is not quantitatively established. The claim that Ca2+ creates a more ordered hydration cage is speculative and not directly supported by the data presented.
- **Why it matters** This is a central mechanistic claim of the paper. If the water dynamics analysis is not robust, the proposed model linking Ca2+ binding to reduced solvent mobility and enhanced aggregation is weakened. The claim goes beyond the data, as no experimental measurement of water dynamics (e.g., THz spectroscopy) is provided.
- **Resolution test** The authors must provide a detailed description of the water analysis methodology, including the definition of the hydration shell, the calculation of persistence times, and the statistical significance of the differences between conditions. Ideally, they should provide a quantitative correlation between water persistence times and aggregation rate constants. Alternatively, they should temper the claim to be a hypothesis rather than a finding.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that AFM analysis reveals distinct fibril polymorphs formed under different ionic conditions, with Ca2+ favoring more twisted fibrils.
- **Evidence pointer** Results section, "The Presence of Different Ions Impacts Fibril Morphology" and Figure S15a-d.
- **Concern** The AFM analysis is presented as evidence for fibril polymorphism, but the data is only in the supplementary material and is described qualitatively. The manuscript states that measurements of height and periodicity were acquired, but no statistical analysis of these parameters is presented in the main text. The classification of polymorphs (p1, p2a, p2b, p3a, p3b) appears to be based on visual inspection. The claim that Ca2+ induces "more twisted" fibrils is not supported by quantitative data. The resolution of AFM is insufficient to distinguish between different molecular-level polymorphs, which typically requires cryo-EM or solid-state NMR.
- **Why it matters** The claim that ionic conditions influence fibril polymorphism is a major conclusion of the paper, with implications for understanding strain diversity in synucleinopathies. If the evidence is only qualitative and based on low-resolution AFM, the claim is not established.
- **Resolution test** The authors must provide quantitative AFM data, including distributions of height and periodicity for each condition, with statistical comparisons. They should also acknowledge the limitations of AFM for determining molecular-level polymorphism and either temper their claims or provide higher-resolution structural data (e.g., cryo-EM) to support the existence of distinct polymorphs.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that the combination of monomer extension and reduced water mobility explains the increased aggregation propensity in the presence of ions.
- **Evidence pointer** Discussion section, and Figure 6.
- **Concern** The proposed model is plausible but is not uniquely supported by the data. The manuscript does not rule out other mechanisms, such as specific ion binding to the NAC region or changes in electrostatic screening that could directly promote intermolecular interactions. The correlation between monomer extension and aggregation rate is not perfect: Na+ induces the largest extension but Ca2+ induces the fastest aggregation. The authors acknowledge this and invoke water dynamics to explain the discrepancy, but this post-hoc explanation is not tested. The model is presented as a definitive conclusion rather than a working hypothesis.
- **Why it matters** The scientific importance of the work hinges on providing a mechanistic understanding of how ions modulate aggregation. If the model is not well-supported, the contribution is incremental rather than transformative.
- **Resolution test** The authors should either provide additional experimental evidence to support the role of water dynamics (e.g., THz spectroscopy or osmotic stress experiments) or present the model more cautiously as a hypothesis that requires further testing. They should also discuss alternative mechanisms and explain why their data favor their model over others.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that MD simulations confirm the structural changes observed by biophysical techniques.
- **Evidence pointer** Results section, "Modeling the aSyn Conformation Ensemble..." and Figure 5.
- **Concern** The MD simulation methodology is not described in sufficient detail to assess its validity. The manuscript states that simulations were run for 1.5-2.7 microseconds, but does not provide information on the number of replicates, the convergence of the simulations, or the statistical uncertainty of the calculated properties. The choice of starting structures (from PDB 2N0A, 8A9L, 8ADS) is mentioned, but the rationale for these choices and the potential bias they introduce are not discussed. The comparison between simulated and experimental data appears to be qualitative.
- **Why it matters** MD simulations are used to support the experimental findings and to provide a mechanistic interpretation. If the simulations are not rigorously validated, the conclusions drawn from them are not reliable.
- **Resolution test** The authors must provide a detailed description of the simulation setup, including force field parameters, equilibration protocol, production run length, and the number of independent replicates. They should demonstrate that the simulations have converged and provide error bars for the calculated properties. They should also provide a quantitative comparison between simulated and experimental observables (e.g., Rg values from SAXS/SANS).

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction
- **Evidence pointer** Introduction, first paragraph
- **Issue** The introduction is dense and assumes significant background knowledge. The transition from the general problem of PD to the specific role of ions in aSyn aggregation could be smoother.
- **Required correction** Briefly explain why ion concentrations are physiologically relevant to aSyn aggregation (e.g., calcium dysregulation in aging neurons) before diving into the specific aims.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, ThT assay
- **Evidence pointer** Methods, "Thioflavin-T (ThT) Binding Assay"
- **Issue** The equation for fitting the aggregation kinetics is mentioned but not shown. The parameters tlag, t50, and k are defined, but the fitting procedure is not described.
- **Required correction** Include the equation and describe the fitting procedure (e.g., nonlinear least squares, software used).

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, HDX-MS
- **Evidence pointer** Methods, "Hydrogen-Deuterium Exchange Mass Spectrometry (HDX-MS)"
- **Issue** The method for correcting for back-exchange and the use of bradykinin for normalization is described, but the equation (eq 2) is not shown.
- **Required correction** Include the equation and provide more detail on the normalization procedure.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, NMR
- **Evidence pointer** Results, "The Conformational Ensemble..." and Figure 2.
- **Issue** The CSP analysis is described, but the significance threshold for identifying a "significant" CSP is not stated.
- **Required correction** State the threshold used (e.g., combined chemical shift perturbation > 0.02 ppm) and how it was determined.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Interdisciplinary readership
- **Affected element** Discussion
- **Evidence pointer** Discussion, paragraph on therapeutic implications
- **Issue** The therapeutic implications are stated briefly and vaguely. The suggestion to design molecules that stabilize compact conformations or modulate the hydration shell is not well-developed.
- **Required correction** Expand on this section, providing more specific examples of how this could be achieved and what the challenges might be.

## Risk / unsupported claims
- The claim that Ca2+ slows water mobility in the hydration shell and that this directly contributes to aggregation propensity is not fully supported. The MD analysis is not described in sufficient detail, and no experimental validation is provided.
- The claim that distinct fibril polymorphs form under different ionic conditions is based on qualitative AFM analysis and is not supported by high-resolution structural data.
- The claim that the combination of monomer extension and reduced water mobility "explains" the aggregation kinetics is an overstatement. The data are correlative, and alternative mechanisms are not ruled out.
- The statement in the abstract that "all ions speed up aggregation" is supported by the ThT data, but the mechanistic link to the observed conformational changes is not established.
- The MD simulations are used to support experimental findings, but the lack of methodological detail makes it impossible to assess their validity.