## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no figures, methods, or supplementary material provided
- **Shared manuscript claim summary** The authors report that the engineered mycobacterial porin M2MspA can serve as a nanopore probe for the intrinsically disordered protein α-Synuclein, reproducing qualitative features previously observed with VDAC. They report voltage-dependent capture rates, a residence time crossover at >50 mV indicating translocation, and direct confirmation of translocation via a selectivity tag method. They conclude that their physical model and the selectivity tag technique are broadly applicable to nanopore-based protein detection.
- **Visible evidence base** Abstract text only; no quantitative data, experimental protocols, or statistical analyses are available
- **Missing materials affecting confidence** Full manuscript, figures, tables, methods, and any supplementary information; without these, quantitative claims and mechanistic interpretations cannot be independently verified

## Reviewer
- **Overall assessment** The abstract presents a conceptually interesting extension of nanopore sensing to a different pore protein, with a potentially useful methodological innovation in the selectivity tag approach. However, the evidence base is limited to a summary of qualitative findings, and several quantitative claims are stated without supporting data. The central conclusion of broad applicability is plausible but not established from the supplied material. The work may be of interest to the nanopore sensing and protein biophysics communities, but the current abstract alone does not provide sufficient evidence to assess technical soundness or reproducibility.
- **Who would be interested in the results, and why** Researchers in nanopore sensing, single-molecule biophysics, and protein translocation studies would be interested because the work suggests a generalizable platform for probing membrane-bound and disordered proteins. Those developing protein detection and separation technologies may also find the selectivity tag method relevant as a potential tool for distinguishing translocation from retraction.
- **Major strengths** The abstract clearly identifies a specific hypothesis, namely that the αSyn/nanopore interaction is largely independent of pore identity, and tests it by comparing VDAC and M2MspA. The use of a selectivity tag method to directly discriminate translocation from retraction is a notable methodological contribution. The writing is concise and accessible to a broad scientific audience.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract lacks quantitative data for capture rates, residence times, and selectivity changes. The crossover behavior at >50 mV is described but not supported by numerical values or error estimates. The claim of direct confirmation via the selectivity tag method requires experimental details and representative traces. Without these, the core mechanistic conclusions are not verifiable.
- **Assessment against Nature-style criteria** Originality is moderate, as the work extends an existing approach rather than introducing a fundamentally new concept. Scientific importance is potentially high for nanopore sensing applications, but the abstract does not demonstrate a significant advance beyond the prior VDAC work. Interdisciplinary readership is plausible, given relevance to biophysics, nanoscience, and protein chemistry. Technical soundness cannot be assessed from the abstract alone, as no methods or data are provided. Readability for nonspecialists is good, with clear explanations of key concepts, though some terms such as "selectivity tag method" are introduced without definition.
- **Recommendation posture** Currently not established from the provided evidence. The abstract is promising, but the lack of quantitative data and methodological detail prevents a supportive recommendation. If the full manuscript provides robust evidence, the work could be considered supportive.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The abstract claims that "the rate of αSyn capture by M2MspA rises exponentially with the applied field" and that "the residence time displays a crossover behavior, indicating that at voltages >50 mV M2MspA-bound αSyn largely undergoes translocation."
- **Evidence pointer** Abstract text; location not provided
- **Concern** The abstract states these quantitative relationships without presenting any numerical data, fits, or statistical measures. No figures or tables are referenced, and no error bars or sample sizes are mentioned.
- **Why it matters** Exponential voltage dependence and a residence time crossover are specific quantitative claims that underpin the mechanistic interpretation. Without supporting data, readers cannot evaluate the strength of the effect, the quality of the fits, or whether the crossover is statistically significant.
- **Resolution test** Provide plots of capture rate versus voltage with fitted exponential curves and confidence intervals, and residence time distributions at multiple voltages showing the crossover. Include statistical tests comparing behavior below and above 50 mV.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological clarity
- **Claim pointer** The abstract claims that "the translocation is directly confirmed using the selectivity tag method, in which the polyanionic C-terminal and neutral N-terminal regions of αSyn alter the selectivity of the M2MspA channel differently, allowing direct discrimination of translocation vs retraction for single αSyn molecules."
- **Evidence pointer** Abstract text; location not provided
- **Concern** The selectivity tag method is described only in a single sentence. No details are given on how selectivity is measured, how the tags are attached, how the discrimination is performed, or how potential artifacts are controlled. The term "directly confirmed" implies a high level of certainty that is not supported by the abstract.
- **Why it matters** The selectivity tag method is presented as a key innovation and the basis for the central conclusion. If the method is not clearly described and validated, the claim of direct confirmation cannot be assessed, and the broader applicability of the technique remains unsubstantiated.
- **Resolution test** Include a detailed methods section describing the tagging strategy, the selectivity measurement protocol, and control experiments (e.g., with untagged αSyn or with a pore lacking the selectivity properties). Show representative single-molecule traces and a statistical analysis of discrimination accuracy.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability claim
- **Claim pointer** The abstract concludes that "the physical model of the motion of disordered protein chains in the nanopore confinement and the selectivity tag technique are not limited to VDAC but are broadly applicable to nanopore-based protein detection, analysis, and separation technologies."
- **Evidence pointer** Abstract text; location not provided
- **Concern** The conclusion of broad applicability is based on a single comparison between VDAC and M2MspA. No other pores, proteins, or experimental conditions are tested. The abstract does not discuss potential limitations, such as pore-specific properties that might affect the interaction.
- **Why it matters** A claim of broad applicability requires evidence of generalizability across multiple systems. Without additional examples or a discussion of boundary conditions, the conclusion overreaches the data presented.
- **Resolution test** Either provide additional experiments with other pores or proteins, or temper the conclusion to state that the model and method are applicable to at least two distinct pores, with further testing needed for broader claims.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** "selectivity tag method"
- **Evidence pointer** Abstract text; location not provided
- **Issue** The term "selectivity tag method" is introduced without definition or context, which may confuse nonspecialist readers.
- **Required correction** Define the term at first use, for example by explaining that tags are attached to specific regions of αSyn to alter ion selectivity in a measurable way.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Contextual framing
- **Affected element** Comparison with prior VDAC work
- **Evidence pointer** Abstract text; location not provided
- **Issue** The abstract references prior work with VDAC but does not specify the key qualitative features that are preserved. This makes it difficult to judge the significance of the replication.
- **Required correction** List the specific qualitative features (e.g., voltage dependence, capture kinetics, conductance states) that are preserved when switching from VDAC to M2MspA.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Quantitative reporting
- **Affected element** Voltage threshold of 50 mV
- **Evidence pointer** Abstract text; location not provided
- **Issue** The threshold of 50 mV is stated without justification or uncertainty. It is unclear whether this is a fitted parameter or an arbitrary cutoff.
- **Required correction** Provide the basis for the 50 mV threshold, such as a crossover analysis or a model prediction, and report any associated uncertainty.

## Risk / unsupported claims
- The exponential voltage dependence of capture rate is stated without data.
- The residence time crossover at >50 mV is stated without data or statistical support.
- The claim of "direct confirmation" of translocation via the selectivity tag method is unsupported without methodological details.
- The conclusion of broad applicability to nanopore-based technologies is not supported by the limited evidence presented.
- The qualitative preservation of features between VDAC and M2MspA is asserted but not specified or demonstrated.