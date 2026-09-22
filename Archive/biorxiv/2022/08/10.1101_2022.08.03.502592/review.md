## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, conclusions, methods) as provided.
- **Assessment boundary** Scientific content, methodological soundness, and support of claims based solely on the supplied text. No external data, figures, or supplementary materials were available for inspection.
- **Shared manuscript claim summary** The authors use all-atom molecular dynamics (MD) simulations of the full human Kir6.2/SUR1 ATP-sensitive potassium (KATP) channel complex to characterize the dynamics of intrinsically disordered regions (IDRs). They propose functional roles for these IDRs, including involvement in inter-domain signal transfer (N-terminus of Kir6.2, L0-loop of SUR1) and modulation of ligand binding (MgADP at nucleotide-binding domains via the 900-loop).
- **Visible evidence base** Text descriptions of simulation setup (10 replicas of 0.5 μs, CHARMM36, POPC bilayer with 10% PIP2, MgADP-bound and APO models), secondary structure analysis (DSSP), contact frequency analysis, RMSD/RMSF/PCA, and references to supplementary figures (S1–S5) and main figures (1–6) that were not provided.
- **Missing materials affecting confidence** All figures, supplementary materials, and numerical data (e.g., RMSD values, contact probabilities, PCA results) are referenced but not included. This prevents independent verification of quantitative claims and visual evidence.

## Reviewer
- **Overall assessment** The manuscript addresses a relevant and underexplored topic, namely the functional role of intrinsically disordered regions in a medically important ion channel complex. The use of long-scale MD simulations of the full octameric assembly is ambitious and potentially valuable. However, the current text provides limited quantitative detail, and the central claims regarding IDR function are largely speculative, with insufficient evidence presented in the manuscript to distinguish robust findings from anecdotal observations. The lack of accessible figures and supplementary data severely hampers evaluation.
- **Who would be interested in the results, and why** Researchers in ion channel biophysics, structural biology of membrane proteins, and computational chemistry would find the simulation approach and hypotheses of interest. Clinicians and pharmacologists studying KATP channelopathies (e.g., neonatal diabetes, congenital hyperinsulinism) may also be interested in the potential mechanistic insights into channel regulation, though the translational relevance is not directly addressed.
- **Major strengths** The study tackles a genuinely difficult problem, namely the dynamics of IDRs that are invisible to conventional structural methods. The simulation setup is state-of-the-art in terms of system size and timescale. The authors integrate prior experimental and computational knowledge to formulate plausible hypotheses about IDR function, which could guide future experimental work.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (lack of quantitative evidence), R1-M2 (insufficient methodological detail for reproducibility), R1-M3 (overinterpretation of functional roles), R1-M4 (inadequate validation of modeled IDR conformations).
- **Assessment against Nature-style criteria**  
  - **Originality** Moderate. The application of full-complex MD to study IDRs in KATP is novel, but the conceptual framework (IDRs as dynamic mediators) is not new.  
  - **Scientific importance** Potentially high, given the physiological relevance of KATP channels, but the current evidence does not establish a definitive advance.  
  - **Interdisciplinary readership** The topic bridges structural biology, biophysics, and computational chemistry, but the presentation is too specialized and lacks accessible summaries for a broad audience.  
  - **Technical soundness** The simulation protocol is generally sound, but key details (e.g., force field validation, equilibration criteria, convergence assessment) are missing, and the analysis is not sufficiently rigorous to support all claims.  
  - **Readability for nonspecialists** The manuscript assumes deep familiarity with KATP channel architecture and MD methods; the abstract and introduction are dense, and the results lack clear narrative for non-experts.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript has potential, but major revisions are required to provide quantitative support, methodological transparency, and more cautious interpretation.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence quality  
- **Claim pointer** The authors claim that IDRs "affect natural ligands binding" and that the 900-loop "directly affects the MgADP binding site," with stabilizing effects on ligand dynamics.  
- **Evidence pointer** Section 2.5, Figure 6 (not provided), supplementary Figure S5 (not provided)  
- **Concern** The manuscript reports contact probabilities and RMSD values (e.g., "RMSD drops to 1.75 Å (0.1)") but provides no raw data, error estimates, or statistical tests. The claim that the 900-loop stabilizes MgADP binding is based on a single comparison of RMSD with and without ED interaction, but the variability across replicas and chains is not systematically quantified. The functional significance of a 0.3 Å RMSD difference is unclear without free energy calculations or binding affinity estimates.  
- **Why it matters** The central conclusion that IDRs modulate ligand binding is a key selling point of the paper. Without robust quantitative evidence, this claim is not convincing and could mislead readers.  
- **Resolution test** Provide per-replica and per-chain data for contact frequencies and ligand RMSD, including standard deviations and statistical comparisons (e.g., t-tests or bootstrapping). Ideally, compute binding free energies or residence times to demonstrate functional impact.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Reproducibility  
- **Claim pointer** The methods describe the use of I-TASSER and QUARK for modeling missing regions, but no details on model selection, quality assessment, or validation are given.  
- **Evidence pointer** Section 4.1, Section 4.2  
- **Concern** The manuscript states that missing regions were modeled using I-TASSER and QUARK, but does not report confidence scores, template information, or structural validation (e.g., Ramachandran plots, clash scores). The equilibration protocol is described as "as described in Walczewska-Szewc and Nowak, 2020," which is not self-contained. Additionally, the simulation length (10 × 0.5 μs) is stated, but convergence of IDR conformations is not demonstrated (e.g., via block averaging or replica similarity).  
- **Why it matters** Reproducibility is a cornerstone of computational studies. Without detailed methods, other groups cannot replicate the simulations or assess the reliability of the modeled IDRs, which are the focus of the paper.  
- **Resolution test** Provide full details of model building, including I-TASSER and QUARK output metrics, and include a supplementary methods section with equilibration parameters. Show convergence analysis (e.g., RMSD vs. time for each replica, cluster analysis of IDR conformations).

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Interpretation  
- **Claim pointer** The authors propose that the N-terminus of Kir6.2 and the L0-loop act as "conformational lock" and "mediators of signal transfer," and that the 900-loop is part of a "molecular bearing."  
- **Evidence pointer** Sections 2.3, 2.4, 2.5, Conclusions  
- **Concern** These functional interpretations go beyond the simulation data. The observation that the N-terminus moves in a confined space without stable contacts does not directly support a "lock" function; alternative explanations (e.g., non-specific steric effects) are not discussed. Similarly, the "molecular bearing" hypothesis is speculative and not tested. The authors acknowledge some limitations but do not provide a balanced discussion of alternative roles.  
- **Why it matters** Overinterpretation can lead to misleading conclusions in a field where experimental validation is challenging. The paper should clearly distinguish between observed dynamics and inferred function.  
- **Resolution test** Soften the language to describe hypotheses rather than conclusions. Add a section discussing alternative interpretations and propose specific experimental tests (e.g., mutagenesis, cross-linking) that could validate the proposed roles.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Validation  
- **Claim pointer** The authors state that the simulation model is "based on CryoEM data" and that the system "remained very stable," but no comparison to experimental data is provided.  
- **Evidence pointer** Section 2.2, Section 4.1  
- **Concern** The manuscript does not validate the simulation against known experimental observations, such as the location of ATP binding sites, the conformation of the channel pore, or the effects of known mutations. The claim of stability is based on visual inspection of RMSD, but no quantitative criteria (e.g., RMSD thresholds) are given.  
- **Why it matters** Without validation, the relevance of the simulations to the real KATP channel is uncertain. The authors should demonstrate that their model reproduces known structural and functional features.  
- **Resolution test** Compare simulation-derived properties (e.g., pore radius, residue-residue distances, ligand binding poses) with experimental structures or mutagenesis data. Provide a table of key validation metrics.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Abstract  
- **Evidence pointer** Abstract  
- **Issue** The abstract states that "our MD results confirmed the crucial role" of specific IDRs, but the word "confirmed" implies experimental validation, which is not provided.  
- **Required correction** Replace "confirmed" with "suggest" or "indicate" to reflect the computational nature of the study.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Section 2.1  
- **Evidence pointer** Section 2.1, Figure 1 (not provided)  
- **Issue** The text lists several IDRs but does not provide a clear summary table or schematic of their locations and lengths, making it hard for readers to follow the subsequent analysis.  
- **Required correction** Add a table or supplementary figure summarizing the IDR boundaries, lengths, and proposed functions.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Technical detail  
- **Affected element** Section 4.2  
- **Evidence pointer** Section 4.2  
- **Issue** The simulation temperature (310 K) and pressure (1 atm) are stated, but the choice of these conditions is not justified.  
- **Required correction** Briefly justify the physiological relevance of these conditions or cite standard practice.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Language  
- **Affected element** Section 2.5  
- **Evidence pointer** Section 2.5  
- **Issue** The phrase "molecular bearing" is used without definition or prior introduction, which may confuse readers.  
- **Required correction** Define the term and explain the analogy clearly, or use more standard terminology.

## Risk / unsupported claims
- The claim that IDRs "affect natural ligands binding" is unsupported by quantitative binding data or free energy calculations.
- The proposal that the N-terminus acts as a "conformational lock" is speculative and not directly tested.
- The "molecular bearing" hypothesis for the 600-loop and 900-loop is not substantiated by the presented data.
- The statement that the 900-loop "directly affects the MgADP binding site" is based on contact frequency analysis but lacks statistical rigor.
- The assertion that the simulation "confirmed" the role of IDRs in signal transfer is overstated given the absence of experimental validation.