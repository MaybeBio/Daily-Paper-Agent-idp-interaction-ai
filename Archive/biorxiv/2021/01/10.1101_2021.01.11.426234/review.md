## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract, with no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors use molecular dynamics simulations (over 54 µs cumulative for free oligomannose N-glycans and over 4 µs for glycosylated CD16a/FcγRIIIa) to characterize the conformational ensembles of oligomannose N-glycans and their response to a protein surface. They report that the protein surface shifts the glycan conformational equilibria toward conformers satisfying steric and hydrogen bonding requirements, that the protein does not induce conformers absent in free glycans, and that populated Man5 conformers at N45 and N162 of FcγRIIIa may relate to IgG1 Fc binding affinity and ADCC modulation.
- **Visible evidence base** Abstract text only; no simulation details, system setup, force field parameters, convergence metrics, structural ensembles, or experimental comparisons are provided
- **Missing materials affecting confidence** Full manuscript, methods section, simulation protocols, force field validation, convergence analysis, structural figures, ensemble comparisons, experimental data on glycosylation effects on binding affinity, and any statistical analyses

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting computational study on the conformational behavior of oligomannose N-glycans in free and protein-bound states, with implications for FcγRIIIa-IgG1 binding. However, the claims are broad and mechanistically specific, while the visible evidence is limited to a summary of simulation times and qualitative outcomes. The central assertion that the protein does not actively distort glycans into non-populated conformers is intriguing but cannot be evaluated without ensemble comparisons. The link between specific glycan conformations at N45 and N162 and binding affinity is speculative in the absence of direct binding or mutagenesis data. The work may appeal to glycobiology and immunology audiences, but the current abstract alone does not establish the case.
- **Who would be interested in the results, and why** Researchers in glycobiology, computational biophysics, and immunology, particularly those studying N-glycan structure and dynamics, Fc receptor function, antibody-dependent cellular cytotoxicity, and viral glycan-mediated immune evasion. The findings could inform therapeutic antibody design and glycan engineering.
- **Major strengths** The study addresses a significant gap in understanding the 3D architecture of intrinsically disordered oligomannose N-glycans. The use of extensive cumulative MD sampling (over 54 µs) is a notable effort. The comparison between free and protein-bound glycan ensembles is a valuable approach to dissect protein-induced conformational selection versus distortion. The potential connection to FcγRIIIa glycosylation and ADCC is clinically relevant.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that "the protein’s structural constraints shift the oligomannoses conformational ensemble to promote conformers that satisfy the steric requirements and hydrogen bonding networks demanded by the protein’s surface landscape" and that "the protein does not actively distort the N-glycans into structures not populated in the unlinked forms in solution."
  - **Evidence pointer** Abstract only; location not provided
  - **Concern** The abstract provides no quantitative comparison between the free and protein-bound conformational ensembles. No metrics such as root-mean-square deviation of glycan dihedral angles, population shifts, free energy differences, or overlap coefficients are reported. The claim that the protein promotes certain conformers without creating new ones requires a rigorous ensemble comparison that is not visible.
  - **Why it matters** Without such quantitative evidence, the central mechanistic conclusion cannot be distinguished from a trivial observation that any protein surface imposes steric restrictions. The claim of "no active distortion" is a strong negative statement that demands statistical power and convergence analysis to support.
  - **Resolution test** Provide ensemble overlap measures, population distributions of key dihedral angles or glycan conformers in free versus bound states, and convergence assessments (e.g., block averaging, multiple independent runs). Show that the bound ensemble is a subset of the free ensemble with shifted populations, with error bars or confidence intervals.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Scientific importance and claim support
  - **Claim pointer** The authors state that "the highly populated conformations of the Man5 linked glycans support experimental evidence of high levels of hybrid complex forms at N45 and show a specific presentation of the arms at N162, which may be involved in mediating binding affinity to the IgG1 Fc."
  - **Evidence pointer** Abstract only; location not provided
  - **Concern** The link between simulated glycan conformations and experimental observations of hybrid complex forms or binding affinity is asserted without presenting any experimental data, correlation analysis, or mechanistic model. The phrase "may be involved" is speculative, and the abstract does not clarify whether the simulations are compared to published experimental results or new data.
  - **Why it matters** The translational relevance to ADCC and IgG1 binding is a key selling point. If the connection is only correlative or speculative, the significance of the findings is substantially weakened. The reader cannot assess whether the conformational features at N45 and N162 are unique or functionally relevant.
  - **Resolution test** Include direct comparison to experimental glycosylation profiles or binding affinity measurements (e.g., from literature or new assays). Provide a structural rationale linking specific arm presentations to FcγRIIIa-IgG1 interface contacts, supported by docking or mutagenesis data.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness
  - **Claim pointer** The abstract reports "over 54 µs of cumulative sampling" for free glycans and "over 4 µs" for the glycosylated receptor, implying sufficient sampling for reliable conclusions.
  - **Evidence pointer** Abstract only; location not provided
  - **Concern** No details on force field choice, water model, temperature, pressure, ionic conditions, or system size are given. The adequacy of 54 µs for sampling the conformational space of highly flexible oligomannoses is not demonstrated. For the protein system, 4 µs may be insufficient to equilibrate multiple glycan chains on a receptor surface.
  - **Why it matters** Glycan conformational ensembles are sensitive to force field parameters, and inadequate sampling can lead to biased conclusions about population shifts. The lack of methodological transparency prevents assessment of reproducibility and robustness.
  - **Resolution test** Specify force field and validation against experimental NMR or crystallographic data. Provide convergence metrics (e.g., dihedral angle time series, cluster population stability) and justify simulation lengths relative to glycan relaxation timescales.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Abstract introduction
  - **Evidence pointer** Abstract, first paragraph
  - **Issue** The description of oligomannose N-glycan structure and the pentasaccharide unit is dense and may be difficult for nonspecialist readers to follow, particularly the notation "Man α1-6)-[Manα(1-3)]-Manβ(1-4)-GlcNAcβ(1-4)-GlcNAcβ1-Asn."
  - **Required correction** Simplify the structural description or add a brief explanatory phrase, such as "a core of two N-acetylglucosamine and three mannose residues" before the detailed notation.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Clarity of claims
  - **Affected element** Abstract results
  - **Evidence pointer** Abstract, final sentence
  - **Issue** The phrase "support experimental evidence of high levels of hybrid complex forms at N45" is ambiguous. It is unclear whether the simulations support prior experimental findings or predict new ones, and what "hybrid complex forms" means in this context.
  - **Required correction** Clarify whether the simulations are consistent with published experimental data or provide new predictions, and define "hybrid complex forms" (e.g., hybrid N-glycan types) explicitly.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Abstract methods
  - **Evidence pointer** Abstract, second paragraph
  - **Issue** The abstract states "free (not protein-linked) oligomannose N-glycans common in vertebrates" but does not specify which glycan sizes (e.g., Man5 to Man9) were simulated or how they were selected.
  - **Required correction** List the specific glycan species simulated and justify their relevance to the FcγRIIIa system.

## Risk / unsupported claims
- The claim that the protein does not actively distort N-glycans into non-populated conformers is unsupported without ensemble comparison data.
- The assertion that Man5 conformations at N45 and N162 may mediate IgG1 Fc binding affinity is speculative and not backed by direct evidence in the abstract.
- The adequacy of simulation sampling (54 µs and 4 µs) to support the conclusions is not assessable from the abstract alone.
- Any quantitative population shifts or conformational preferences are not reported, making the central mechanistic claims unverifiable from the provided material.

## Assessment against Nature-style criteria
- **Originality** The question of how protein surfaces shape glycan conformational ensembles is not entirely new, but the specific focus on FcγRIIIa and the claim of conformational selection without distortion could offer a fresh perspective. However, the abstract does not clearly differentiate this work from prior computational studies on glycan dynamics.
- **Scientific importance** The potential implications for antibody-dependent cellular cytotoxicity and therapeutic antibody design are significant, but the importance is contingent on the validity of the glycan-binding link, which is not established here.
- **Interdisciplinary readership** The topic bridges glycobiology, immunology, and computational chemistry, which could attract a broad audience. However, the abstract's technical density may limit accessibility.
- **Technical soundness** The use of extensive MD sampling is commendable, but the lack of methodological detail and quantitative ensemble analysis prevents assessment of technical rigor.
- **Readability for nonspecialists** The abstract is moderately readable but includes jargon and structural notation that may hinder nonspecialist comprehension.

## Recommendation posture
Currently not established from the provided evidence. The abstract presents an interesting hypothesis and substantial simulation effort, but the central claims regarding conformational selection, lack of distortion, and functional relevance to IgG1 binding are not supported by visible quantitative data. The manuscript could become compelling if the full text provides rigorous ensemble comparisons, methodological transparency, and direct links to experimental observations.