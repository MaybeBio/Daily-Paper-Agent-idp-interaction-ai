## Review setup
- **Input scope** Full manuscript text (abstract, introduction, main sections, acknowledgements)
- **Assessment boundary** Scientific content, technical claims, literature coverage, and internal consistency as presented in the provided text. No external literature verification performed.
- **Shared manuscript claim summary** The authors review recent advances in single-molecule fluorescence spectroscopy applied to intrinsically disordered regions (IDRs), covering integration with simulations, photon-statistics-based dynamics measurements, applications in biomolecular condensates, and forthcoming methodologies. They argue that these techniques are becoming increasingly accessible and that IDR biology continues to drive methodological innovation.
- **Visible evidence base** Abstract, Introduction, four main sections (Integration of smFRET and simulations; Technical and analytical improvements; Use in condensates; Forthcoming methodologies), Acknowledgements. No figures, tables, or supplementary materials were provided.
- **Missing materials affecting confidence** Figures 1–4 are cited but not available. Reference list is not provided. No experimental data or methods section is included. This is a review article, so primary data are not expected, but figure content and full reference details would aid verification of specific claims.

## Reviewer
- **Overall assessment** This is a well-structured and timely review of single-molecule fluorescence methods for studying IDRs. The authors cover a broad range of techniques and recent developments, with a clear emphasis on the integration of experiment, simulation, and theory. The writing is generally clear and accessible. However, several claims are made without sufficient supporting detail in the text, and the absence of figures and references limits full evaluation. The review would benefit from more critical discussion of limitations and unresolved controversies in the field.
- **Who would be interested in the results, and why** Researchers in biophysics, biochemistry, and molecular biology who study intrinsically disordered proteins, protein dynamics, phase separation, and single-molecule techniques. The review is also relevant to computational scientists developing force fields or machine learning models for IDR conformations, as it benchmarks their methods against experimental data.
- **Major strengths** 1. Comprehensive and up-to-date coverage of a rapidly evolving field. 2. Clear articulation of the complementary roles of experiment, simulation, and theory. 3. Good balance between established techniques and emerging methodologies. 4. The section on condensates addresses a timely and technically challenging application area. 5. The discussion of photon statistics methods is technically detailed and useful for practitioners.
- **Major Concerns** 1. Several specific quantitative claims are made without supporting data or citations in the visible text. 2. The review does not critically discuss potential artifacts or limitations of the techniques beyond brief mentions. 3. The claim that machine learning predictors might replace experiments is raised but not fully developed. 4. The section on forthcoming methodologies lists techniques but does not critically assess their feasibility for IDR studies. 5. The relationship between chain dimensions and reconfiguration times is presented as surprising, but the mechanistic implications are not discussed.
- **Minor Comments** 1. The abstract is concise but could better highlight the specific technical advances discussed. 2. Some terminology (e.g., "photon statistic analyses") could be defined more explicitly for nonspecialist readers. 3. The transition from the Introduction to the first main section is abrupt. 4. The Acknowledgements section includes a conflict of interest statement that is unusually detailed for a review article. 5. The final paragraph of the "Forthcoming methodologies" section could be strengthened by a more explicit summary of open challenges.
- **Technical failings that need to be addressed before the case is established** None identified from the supplied material. This is a review article, and the technical claims are qualitative in nature. However, the lack of figure content and references prevents full verification of specific statements.
- **Assessment against Nature-style criteria**  
  *Originality*: The review covers recent developments but does not present a novel conceptual framework. Its originality lies in the synthesis of recent literature, which is moderate for a review.  
  *Scientific importance*: The topic is of high importance to the biophysics community, and the review addresses key challenges in the field.  
  *Interdisciplinary readership*: The content is relevant to biophysicists, biochemists, cell biologists, and computational scientists, but the technical detail may limit accessibility to a broader audience.  
  *Technical soundness*: The technical descriptions appear accurate based on the visible text, but the absence of figures and references limits full assessment.  
  *Readability for nonspecialists*: The writing is generally clear, but some sections assume familiarity with single-molecule fluorescence techniques and photon statistics. A brief primer on key concepts would improve accessibility.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** No
- **Axis** Evidence sufficiency
- **Claim pointer** "For example, using multiple FRET labeling positions, excellent conformational agreement between simulations and experiments has been reported for the transcription factor Sox2 [7], the translation factor eIF4B [8], alpha synuclein [9], and the linker histone H1 bound to prothymosin α [10] and to nucleosomes [11]."
- **Evidence pointer** Section "Integration of single-molecule FRET and simulations to probe IDR conformations and interactions", location not provided
- **Concern** The claim of "excellent conformational agreement" is made for multiple systems, but the criteria for "excellent" are not defined. No quantitative metrics (e.g., RMSD, transfer efficiency differences) are provided in the text.
- **Why it matters** Without defined criteria, the reader cannot assess the strength of the agreement or compare across systems. This is central to the review's argument that experiment-simulation gaps are narrowing.
- **Resolution test** Provide quantitative measures of agreement (e.g., mean absolute error in transfer efficiencies, overlap coefficients of distance distributions) or explicitly state the qualitative criteria used.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Technical completeness
- **Claim pointer** "In a new, updated time-resolved form [44], the segment size is systematically varied over the burst duration, and kinetic rates on microsecond to millisecond time-scales are derived from the decay of FRET variance (Figure 3c)."
- **Evidence pointer** Section "Technical and analytical improvements for studying IDR dynamics", Figure 3c, location not provided
- **Concern** The description of the updated time-resolved burst variance analysis is brief. The methodological advance relative to the original approach is not clearly articulated, and the reader cannot understand what "updated" means without seeing Figure 3c or the cited reference.
- **Why it matters** This is presented as a key technical advance, but the text does not explain the novelty or the advantage over existing methods. This weakens the review's contribution to method dissemination.
- **Resolution test** Expand the description to specify the algorithmic or analytical change, and state the improvement in accuracy, time resolution, or applicability.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Critical analysis
- **Claim pointer** "In FECS, FRET correlations are generated by sorting photons pairs specific to their type (donor–donor, acceptor–acceptor, acceptor–donor, donor–acceptor) and building a histogram of photon-pair detections lag times, irrespective of the burst from which photons originate (Figure 3d)."
- **Evidence pointer** Section "Technical and analytical improvements for studying IDR dynamics", Figure 3d, location not provided
- **Concern** The description of FECS is purely methodological. The review does not discuss potential limitations, such as sensitivity to photobleaching, background, or the assumptions underlying the normalization procedure.
- **Why it matters** A review should provide balanced assessment. Without discussion of limitations, readers may overestimate the robustness of the method.
- **Resolution test** Add a paragraph discussing known limitations, validation against simulations or other methods, and conditions under which FECS may fail.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scope justification
- **Claim pointer** "Recent technical advances are poised to make single-molecule fluorescence measurements of IDRs more accessible by expanding detection range and sensitivity."
- **Evidence pointer** Section "Forthcoming methodologies to study IDRs", location not provided
- **Concern** The section lists several techniques (MINFLUX, FRET-FLIM, ABEL traps) but does not provide a clear rationale for why these particular methods were selected, nor does it compare their relative advantages for IDR studies.
- **Why it matters** The selection appears arbitrary. A more systematic comparison would help readers understand which techniques are most promising for specific IDR questions.
- **Resolution test** Provide a comparative table or structured discussion that maps each technique to specific IDR-related questions and discusses trade-offs in resolution, throughput, and sample requirements.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, location not provided
- **Issue** The phrase "photon statistic analyses" is vague and may confuse nonspecialist readers.
- **Required correction** Replace with a more specific term, such as "photon-pair correlation analyses" or "fluorescence correlation spectroscopy variants," or define the term on first use.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section "Integration of single-molecule FRET and simulations to probe IDR conformations and interactions"
- **Evidence pointer** Section text, location not provided
- **Issue** The paragraph beginning "One could argue based on the success of simulations..." introduces a counterargument but does not clearly resolve it. The logical flow is disrupted.
- **Required correction** Restructure the paragraph to state the counterargument, provide the authors' position, and then support it with specific examples.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Section "Use and challenges of single-molecule fluorescence in biomolecular condensates"
- **Evidence pointer** Section text, location not provided
- **Issue** The term "percolation" is used without definition. Nonspecialist readers may not be familiar with this concept in the context of biomolecular condensates.
- **Required correction** Add a brief parenthetical explanation, such as "percolation (the formation of a connected network of molecules)".

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section "Forthcoming methodologies to study IDRs"
- **Evidence pointer** Section text, location not provided
- **Issue** The section mentions that MINFLUX "has been shown to quantify distance distributions with Angstrom resolution" but does not specify in which system or under what conditions.
- **Required correction** Add a citation and a brief description of the demonstration system (e.g., DNA origami, labeled proteins).

## Risk / unsupported claims
- The claim of "excellent conformational agreement" between simulations and experiments for multiple systems (R1-M1) is not quantitatively supported in the visible text.
- The statement that "explicit inclusion of dyes in both coarse-grained and all-atom simulations modestly improved agreement" is presented without specific data or effect sizes.
- The claim that FECS "enormously simplifying the readout of multistate interconversion dynamics" is qualitative and not supported by comparative data in the text.
- The assertion that "recent advances demonstrate feasibility of in situ-specific labeling with synthetic dyes for characterizing IDRs" is made without describing the method or its limitations.
- The statement that ABEL traps permit "simultaneous measurements of the hydrodynamic radius from a molecule's Brownian motion within the trap" is presented without details on accuracy or precision.
- The claim that "plasmonic enhancement using DNA origami nanoantennas was demonstrated to boost the photon count rate" is not accompanied by quantitative improvement factors.