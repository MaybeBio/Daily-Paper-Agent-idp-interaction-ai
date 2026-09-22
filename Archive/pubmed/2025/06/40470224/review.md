## Review setup
- **Input scope** Full manuscript text (preprint, Research Square, 2025-06-05, DOI 10.21203/rs.3.rs-6378534/v1)
- **Assessment boundary** Scientific content, methodology, data interpretation, and claims as presented in the provided text. No external validation or replication attempted.
- **Shared manuscript claim summary** The authors propose that biomolecular condensates formed by SARS-CoV-2 nucleocapsid protein control and are defined by RNA-RNA interactions arising during viral replication. They reconstitute condensates with N protein and viral RNA fragments, showing that high-complementarity plus/minus RNA pairs produce arrested, networked condensates, while low-complementarity pairs yield round, liquid-like condensates. They support this with molecular dynamics simulations and propose that viruses mitigate detrimental RNA-RNA interactions via genome organization, timing, sequence content, production ratios, and condensate material properties.
- **Visible evidence base** Experimental reconstitution assays (fluorescence microscopy, image quantification), RNA structure probing (DEPC with nanopore sequencing), molecular dynamics simulations (Mpipi and SIS models), bioinformatic analyses (GC content, predicted hybridization energy, G-quadruplex prediction), and cell-based bead-loading experiments.
- **Missing materials affecting confidence** No figures, tables, or extended data were provided. Statistical details (replicates, error bars, significance tests) are absent. Raw sequencing data and simulation trajectories are referenced but not accessible. Methods for some experiments (e.g., error-prone PCR details, bead-loading protocol) are incomplete. No negative controls for several key experiments are described.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question in RNA biology and virology: how RNA viruses avoid catastrophic RNA-RNA interactions during replication. The central hypothesis, that condensate material properties are modulated by RNA-RNA interaction strength, is conceptually interesting and potentially impactful. The combination of wet-lab reconstitution, sequencing-based probing, and coarse-grained simulations is ambitious and appropriate. However, the current presentation has significant gaps. The absence of figures makes it impossible to evaluate the primary data. Several claims, particularly regarding the "universal" nature of the proposed mechanisms and the interpretation of simulation results, appear to exceed what the described evidence can support. The manuscript would benefit from clearer articulation of the model, more rigorous quantitative analysis, and a more cautious framing of the evolutionary speculations. The work is potentially publishable in a high-impact venue, but substantial revisions and additional data are required before the case is established.
- **Who would be interested in the results, and why** Virologists studying RNA virus replication, particularly coronaviruses, would be interested in the proposed role of N protein condensates in subgenomic RNA synthesis. Researchers in the biomolecular condensate field would be interested in the demonstration that RNA-RNA interaction strength, rather than just protein-RNA interactions, can dictate condensate morphology. Evolutionary biologists studying RNA genome architecture may find the GC content analysis relevant. The methodological combination of experiments and simulations could also appeal to computational biophysicists.
- **Major strengths**
  1. The central question is important and under-explored: how do viruses prevent irreversible RNA entanglement during replication?
  2. The study uses a relevant model system (SARS-CoV-2 N protein and viral RNA) with a minimal reconstitution approach.
  3. The combination of experimental reconstitution, chemical probing, and coarse-grained simulations is powerful and provides complementary perspectives.
  4. The observation that plus/minus RNA pairs produce distinct condensate morphologies is potentially novel and mechanistically interesting.
  5. The authors propose a multi-faceted model (genome organization, timing, sequence content, ratios, material properties) that is testable.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that "RNA-RNA interactions... arise in viral replication" and that the observed condensate morphologies are "defined by" these interactions. The central experimental evidence for this is the morphology difference between condensates formed with plus/minus complementary RNA pairs versus single RNA species.
- **Evidence pointer** Results sections "Multiple plus and minus strand TRS-B RNA fragments are capable of driving N protein condensation" and "Reconstitution of low and high affinity viral RNA–RNA interactions in condensates"; Figures 1-3 (not provided)
- **Concern** The primary data supporting the central claim are not visible. The manuscript refers to figures and extended data that were not included in the provided text. Without these, it is impossible to assess the quality of the imaging, the reproducibility of the morphology phenotypes, the quantification methods, or the statistical significance of the differences claimed. The description of "giant arrested networks" versus "round, liquid-like condensates" is qualitative; no quantitative metrics (e.g., circularity distributions, aspect ratios, area measurements with error bars) are presented in the text. The claim that morphology is "independent of RNA structure stability" is made but the supporting data (presumably in Extended Data) are not available.
- **Why it matters** The entire thesis rests on the observation that complementary RNA pairs alter condensate morphology. If this observation is not robust, quantified, and statistically validated, the central claim collapses. The current text does not provide sufficient evidence to evaluate this.
- **Resolution test** Provide all figures and extended data. Include quantitative morphology metrics (e.g., circularity, area, solidity) with appropriate statistical tests (e.g., ANOVA with post-hoc comparisons) for at least three independent experiments. Show representative images for all conditions, including negative controls (e.g., RNA alone, protein alone, non-complementary RNA pairs). Demonstrate that the morphology difference is not due to differences in RNA length, concentration, or aggregation state prior to condensation.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of simulations
- **Claim pointer** The manuscript claims that "residue-resolution molecular dynamics simulations... support that these properties arise from degree of trans RNA contacts." Specifically, the simulations are used to argue that plus/minus RNA pairs have higher trans RNA contact density and that this drives arrested network formation.
- **Evidence pointer** Results sections "Multiple plus and minus strand TRS-B RNA fragments are capable of driving N protein condensation" and "Reconstitution of low and high affinity viral RNA–RNA interactions in condensates"; Methods "Coarse-grained Molecular Dynamics Simulations of Nucleocapsid protein and RNA (Model 1)" and "Coarse-grained Molecular Dynamics Simulations of RNA clusters (Model 2)"
- **Concern** The simulation methodology has several potential issues. First, the hybrid model (Mpipi for protein-RNA, SIS for RNA-RNA) is described as "chemically specific" but the parameters for the hybrid interactions are not provided. How are the protein-RNA interaction strengths calibrated relative to the RNA-RNA base-pairing energies? Second, the simulations use only 54 RNA chains (or 162 for Envelope), which may be too small to capture the behavior of long, multi-domain RNAs in a condensate. Third, the claim that the model captures "non-specific interactions between YYYRRY sequences and RBD 1" is not directly validated against experimental binding data. Fourth, the simulation time (up to 1.2 x 10^8 timesteps, ~1.2 microseconds) may be insufficient to equilibrate large condensate-like assemblies. Finally, the authors acknowledge a limitation in capturing RBD 2 interactions, which is a significant part of the proposed mechanism.
- **Why it matters** The simulations are used as key supporting evidence for the mechanistic claim that trans RNA contacts drive the arrested phenotype. If the model is not properly validated or the simulations are not converged, the conclusions drawn from them are unreliable. The manuscript does not provide enough detail to assess the robustness of the simulation results.
- **Resolution test** Provide full parameter files and calibration details for the hybrid model. Show convergence tests (e.g., system size dependence, simulation length dependence). Validate the model against experimental data, such as binding affinities or condensate surface tensions. Show that the simulation results are robust to initial conditions and simulation protocol. Provide error bars on simulation observables (e.g., trans contact density, diffusion exponents) from multiple independent runs.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Overinterpretation / Generalization
- **Claim pointer** The manuscript proposes that "an original purpose of RNA-binding proteins may have been to prevent spurious RNA-RNA interactions" and that "the innovation of DNA was an attempt to avoid the problem entirely." It also claims that the strategies uncovered "likely extend to all eukaryotic condensates."
- **Evidence pointer** Discussion section
- **Concern** These are broad evolutionary and general claims that go far beyond the experimental system studied. The data are from a minimal reconstitution system with SARS-CoV-2 N protein and short RNA fragments. Extrapolating to the origin of RNA-binding proteins and the evolution of DNA is highly speculative and not supported by the evidence presented. Similarly, the claim that these principles are "universal" for all eukaryotic condensates is not justified, as the authors only tested one protein (N) and one protein (FUS) in a limited set of conditions.
- **Why it matters** Overstated claims can mislead readers and detract from the solid, specific findings of the study. The manuscript would be stronger if the discussion were more measured and clearly distinguished between what is demonstrated and what is speculation.
- **Resolution test** Revise the discussion to clearly separate data-driven conclusions from hypotheses. Provide specific evidence or citations to support the evolutionary claims, or soften the language to indicate these are speculative ideas. If the "universal" claim is to be maintained, additional experiments with different proteins and RNA sequences would be needed.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Missing controls and alternative explanations
- **Claim pointer** The manuscript claims that "coating with N protein reduces trans RNA-RNA interactions" and that this is a mechanism to prevent RNA entanglement. The evidence comes from experiments where N protein is pre-incubated with plus RNA before adding minus RNA.
- **Evidence pointer** Results section "Coating with N protein reduces trans RNA-RNA interactions"; Figure 4 (not provided)
- **Concern** The interpretation of the "coating" experiments is not straightforward. The authors attribute the reduced co-localization to N protein coating preventing RNA-RNA interactions. However, alternative explanations are possible. For example, N protein binding could change the RNA conformation (e.g., by melting secondary structure) in a way that reduces the propensity for trans interactions, without necessarily "coating" the RNA. Additionally, the experiments use a fixed concentration of N protein; it is unclear if the effect is due to stoichiometric coating or a more subtle allosteric effect. The manuscript does not describe control experiments where a non-RNA-binding protein is used, or where N protein is added after the RNA-RNA interaction has formed.
- **Why it matters** The proposed mechanism of "coating" is a key part of the model. If the effect is due to a different mechanism, the model would need to be revised. The current evidence does not distinguish between coating and other possible effects of N protein on RNA conformation.
- **Resolution test** Perform control experiments with a non-RNA-binding protein (e.g., BSA) to show the effect is specific to N protein. Vary the order of addition (e.g., pre-form RNA-RNA interactions, then add N protein) to test if N protein can resolve existing interactions. Use RNA structure probing (e.g., SHAPE or DEPC) to assess whether N protein binding changes RNA secondary structure in a way that could explain the reduced trans interactions.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of writing
- **Affected element** Introduction and Discussion
- **Evidence pointer** Introduction, Discussion
- **Issue** The manuscript contains several instances of imprecise or ambiguous language. For example, "RNA-RNA interactions that arise in viral replication" is used in the title and throughout, but the precise nature of these interactions (e.g., genome dimerization, template switching, anti-genome annealing) is not clearly defined. The phrase "extent situation" in the Introduction appears to be a typo for "extreme situation." The Discussion uses terms like "sticky" and "stickiness" in a colloquial manner that may not be appropriate for a formal scientific manuscript.
- **Required correction** Define the specific RNA-RNA interactions being studied. Correct typographical errors. Replace colloquial terms with more precise scientific language (e.g., "propensity for trans base-pairing" instead of "stickiness").

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results sections describing quantitative measurements
- **Evidence pointer** Results sections "Multiple plus and minus strand TRS-B RNA fragments are capable of driving N protein condensation" and "Reconstitution of low and high affinity viral RNA–RNA interactions in condensates"
- **Issue** The manuscript reports quantitative measurements (e.g., condensate area, intensity, co-localization) but does not provide statistical details in the text. It is unclear how many independent experiments were performed, how many condensates were analyzed per condition, and what statistical tests were used to compare conditions.
- **Required correction** Add a "Statistical Analysis" subsection in Methods. For each quantitative measurement, report the number of independent experiments (n), the number of technical replicates, the statistical test used, and the resulting p-values or confidence intervals. Consider adding effect sizes.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Methods sections for cell-based experiments and error-prone PCR
- **Evidence pointer** Methods "Cell-free condensation reaction (N protein)", "Cell-free condensation reaction (N protein) with Mg2+", "Cell-free condensation reaction (FUS)", "Error prone RNA production"
- **Issue** The methods for the cell-based experiments (bead loading) are described in a single sentence and lack critical details, such as the number of cells analyzed, the concentration of RNA and protein loaded, and how the cells were imaged and quantified. The error-prone PCR method is also vague, with no information on the mutation rate, the number of PCR cycles, or how the error rate was assessed.
- **Required correction** Expand the methods to include full details for reproducibility. For bead loading, specify the bead type, the loading protocol, the cell line and culture conditions, the imaging parameters, and the image analysis pipeline. For error-prone PCR, specify the polymerase, the MnCl2 or MgCl2 concentrations, the number of cycles, and how the mutation frequency was estimated.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data and Materials Availability statement
- **Evidence pointer** Data and Materials Availability
- **Issue** The statement says "All data and/or materials are available upon request from C.A.R. or J.A.J." This is vague and does not meet the standards of many journals, which require data to be deposited in a public repository. The authors mention a Figshare link in the Methods, but it is not included in the Data Availability statement.
- **Required correction** Provide a clear Data Availability statement that includes the Figshare DOI and states that all raw data, analysis scripts, and simulation input files are available there. If any data cannot be shared, explain why.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** All figures (not provided)
- **Evidence pointer** Figures 1-7, Extended Data Figures 1-5 (not provided)
- **Issue** The figures are not provided, so it is impossible to assess their quality. However, based on the text, it is unclear whether the figures include appropriate scale bars, color scales, and annotations. The text mentions "yellow arrows" in Figure 4b, but it is not clear if these are visible in the figure.
- **Required correction** Ensure all figures are high-resolution, include scale bars, and have clear annotations. Add a legend for each figure that fully describes the experimental conditions and the data shown.

## Risk / unsupported claims
- The claim that "an original purpose of RNA-binding proteins may have been to prevent spurious RNA-RNA interactions" is speculative and not supported by the data presented.
- The claim that "the innovation of DNA was an attempt to avoid the problem entirely" is speculative and not supported by the data.
- The claim that the proposed mechanisms "likely extend to all eukaryotic condensates" is an overgeneralization based on a limited set of experiments with two proteins (N and FUS) and specific RNA fragments.
- The claim that "RNA-RNA interactions... arise in viral replication" is presented as a general statement, but the manuscript only studies a subset of potential interactions (TRS-L/TRS-B) in a reconstituted system.
- The claim that "coating with N protein reduces trans RNA-RNA interactions" is presented as a mechanism, but alternative explanations (e.g., RNA conformational changes) are not ruled out.
- The claim that "the degree of trans RNA contacts" is the primary determinant of arrested network formation is supported by simulations, but the simulations have limitations (small system size, potential lack of convergence) that are not fully addressed.
- The claim that "low GC content" is a general viral strategy to reduce RNA-RNA interactions is based on a correlation and a limited analysis of viral genomes; the causal link is not established.

## Assessment against Nature-style criteria
- **Originality** The concept that RNA-RNA interaction strength, rather than just protein-RNA interactions, dictates condensate morphology is a novel and potentially important contribution. The application of this idea to viral replication, specifically the TRS-L/TRS-B interaction, is a fresh perspective. The combination of experimental reconstitution with sequencing-based probing and coarse-grained simulations is innovative. However, the field has seen related work on RNA-RNA interactions in condensates, and the novelty of the specific claims needs to be more clearly articulated.
- **Scientific importance** The question of how RNA viruses avoid RNA entanglement is of fundamental importance to virology. The proposed mechanisms (coating, GC content, ratios) have implications for understanding viral replication strategies and could inform the design of antiviral strategies. The broader claim that RNA-RNA interactions are a general determinant of condensate properties is important for the condensate field. If the findings are robust, they could have a significant impact.
- **Interdisciplinary readership** The topic bridges virology, RNA biology, and biophysics. The use of simulations and biophysical assays will appeal to physical biologists. The viral replication context will appeal to virologists. The general principles of RNA-RNA interactions in condensates will appeal to cell biologists. The manuscript has the potential to reach a broad audience, but the writing needs to be accessible to non-specialists.
- **Technical soundness** The experimental approach is generally sound, but the lack of figures and statistical details prevents a full assessment. The simulation methodology is sophisticated but has potential limitations (hybrid model calibration, system size, convergence) that need to be addressed. The combination of methods is appropriate, but the integration of results from different approaches could be strengthened.
- **Readability for nonspecialists** The manuscript is written in a technical style that may be challenging for non-specialists. The Introduction provides some context, but the Results section is dense. The Discussion is somewhat speculative and could be more focused. The abstract and summary are clear, but the main text would benefit from more accessible explanations of key concepts (e.g., what a condensate is, why RNA-RNA interactions are a problem).

## Recommendation posture
**Supportive if technical concerns are resolved.** The central hypothesis is interesting and the experimental approach is promising. However, the manuscript is not currently publishable in its present form. The lack of figures and statistical details is a major issue. The simulation methodology needs to be more rigorously validated. The Discussion contains overinterpretations that should be tempered. If the authors can provide the missing data, address the technical concerns, and revise the manuscript to be more measured and accessible, it could be a strong contribution.