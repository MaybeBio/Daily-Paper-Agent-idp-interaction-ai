## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific claims, methodology, and interpretation as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors use recombinant, isotypically pure human tubulins to show that the intrinsically disordered α-tubulin tail inhibits microtubule growth and promotes catastrophe, while detyrosination and ∆2 modification do not alter intrinsic microtubule dynamics. They further demonstrate that tyrosination quantitatively tunes CLIP-170 recruitment to microtubule plus-ends, and that CLIP-170 and EB1 synergize to selectively increase the dynamicity of tyrosinated microtubules. The authors conclude that differential in vivo stability of modified microtubule subpopulations arises exclusively from selective effector recruitment, not from changes in intrinsic polymer dynamics.
- **Visible evidence base** In vitro microtubule dynamics assays using recombinant tubulin variants; all-atom explicit solvent MD simulations and metadynamics simulations; TIRF/IRF imaging of CLIP-170 and EB1 tip-tracking; mass spectrometry validation of tubulin preparations
- **Missing materials affecting confidence** Figures, tables, and supplementary figures are referenced but not provided; no numerical data or statistical details are available; no experimental details for the tip-tracking assays beyond buffer composition; no information on replicate numbers or statistical tests used

## Reviewer
- **Overall assessment** This manuscript addresses a long-standing question in the tubulin code field: whether α-tubulin tail modifications directly alter intrinsic microtubule dynamics or act through effector recruitment. The use of recombinant, isotypically pure tubulin variants is a significant technical advance that overcomes limitations of previous work using heterogeneous brain tubulin. The finding that detyrosination and ∆2 modification do not affect intrinsic dynamics, while the full α-tail inhibits growth, is potentially important. The demonstration that tyrosination quantitatively tunes CLIP-170 recruitment and that CLIP-170/EB1 synergize to increase dynamicity of tyrosinated microtubules provides a mechanistic framework for understanding modification-dependent microtubule stability. However, the manuscript has several issues that need to be addressed, particularly regarding the interpretation of the MD simulations, the quantitative analysis of CLIP-170 recruitment, and the strength of the claim that in vivo differences are "exclusively" due to effector recruitment.
- **Who would be interested in the results, and why** Cell biologists studying microtubule dynamics and the tubulin code; researchers interested in posttranslational modification-dependent regulation of cytoskeletal function; biophysicists studying intrinsically disordered protein regions; neurobiologists studying neuronal microtubule stability and degeneration, given the clinical relevance of detyrosination and ∆2 modifications.
- **Major strengths** The use of recombinant, isotypically pure tubulin variants with defined posttranslational states is a major technical advance. The combination of in vitro reconstitution with MD simulations provides complementary approaches. The quantitative demonstration that tyrosination tunes CLIP-170 recruitment and that CLIP-170/EB1 synergize to increase dynamicity is mechanistically informative. The study directly addresses a question that has been unresolved for over three decades.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (MD simulation interpretation), R1-M2 (exclusivity claim), R1-M3 (CLIP-170 recruitment quantification)
- **Assessment against Nature-style criteria** Originality: High. The study provides the first systematic analysis of α-tail modifications on intrinsic microtubule dynamics using defined recombinant tubulins. Scientific importance: High. The findings challenge assumptions about how detyrosination and ∆2 modifications relate to microtubule stability and provide a mechanistic framework for the tubulin code. Interdisciplinary readership: Moderate to high. The work bridges cell biology, biophysics, and computational biology, and will be of interest to researchers in all three areas. Technical soundness: Generally strong for the experimental work, but the MD simulation interpretation and the exclusivity claim require further support. Readability for nonspecialists: The manuscript is well-written and accessible, though some sections on MD simulations may be challenging for readers without computational background.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding the interpretation of MD simulations, the strength of the exclusivity claim, and the quantitative analysis of CLIP-170 recruitment.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation of computational results
- **Claim pointer** The authors claim that MD simulations show the α-tubulin tail transiently occluding the longitudinal microtubule polymerization interface, and that this explains the inhibitory effect of the α-tail on microtubule growth.
- **Evidence pointer** Results section "The α-tubulin Tail Interacts Transiently with the Longitudinal Polymerization Interface"; Figure 2
- **Concern** The MD simulations are performed on free tubulin dimers or tetramers, not on tubulin incorporated into a microtubule lattice or protofilament. The authors acknowledge this in the Limitations section, but the claim that the α-tail "occludes" the longitudinal polymerization interface is presented as a mechanistic explanation for the growth inhibition. The relevance of the simulations to the actual polymerization process is not fully established. The simulations show the tail interacting with the interface in the free state, but it is unclear whether this interaction would persist or be relevant during the actual incorporation of a dimer into a growing microtubule end. The authors note that the tail associates with the interface for 83 ± 20% of the simulation time, but this is for free dimers, not for dimers in the context of a microtubule end where the interface is already engaged in longitudinal contacts.
- **Why it matters** The mechanistic interpretation of the growth inhibition is central to the paper's first major conclusion. If the tail's interaction with the interface is not relevant during polymerization, the explanation for the observed growth inhibition would be incomplete or incorrect.
- **Resolution test** The authors should either (a) provide additional simulations that model the polymerization process more directly, such as simulations of dimer addition to a protofilament or microtubule end, or (b) temper the mechanistic claim and present the tail-interface interaction as a plausible but not definitively established mechanism. Alternatively, they could provide experimental evidence that directly tests the role of the tail-interface interaction in growth inhibition.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Strength of conclusion
- **Claim pointer** The authors conclude that "the marked differential in vivo stabilities of the modified microtubule subpopulations, therefore, must result exclusively from selective effector recruitment."
- **Evidence pointer** Summary; Discussion
- **Concern** The word "exclusively" is a strong claim. The authors have shown that detyrosination and ∆2 modification do not affect intrinsic dynamics in their in vitro system using α1A/βIII tubulin. However, this does not rule out the possibility that these modifications could affect dynamics in other tubulin isotype contexts, or that other factors (e.g., microtubule-associated proteins, other posttranslational modifications) could contribute to the differential stability of modified microtubule subpopulations in cells. The authors' own data show that the full α-tail has a significant effect on growth, and it is possible that the tail length or charge density could be modulated by other modifications (e.g., polyglutamylation, polyglycylation) that were not tested here. The claim of exclusivity is not fully supported by the data presented.
- **Why it matters** The exclusivity claim is a central conclusion of the paper and has implications for how the field interprets the role of detyrosination and ∆2 modification in microtubule stability. Overstating the conclusion could mislead future research.
- **Resolution test** The authors should either (a) soften the claim to indicate that their data show no direct effect of detyrosination and ∆2 modification on intrinsic dynamics in the tested context, and that effector recruitment is sufficient to explain the differential stability, or (b) provide additional evidence that rules out other contributing factors, such as testing additional tubulin isotypes or combinations of modifications.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative analysis
- **Claim pointer** The authors claim that tyrosination "quantitatively tunes" CLIP-170 density at the growing plus-end and that CLIP-170 and EB1 synergize to selectively increase the dynamicity of tyrosinated microtubules.
- **Evidence pointer** Results section "Selective recruitment of CLIP-170 to tyrosinated microtubules increases their dynamicity"; Figure 4
- **Concern** The quantitative relationship between tyrosination level and CLIP-170 density is described, but the actual data are not shown in the provided text. The claim of "quantitative tuning" implies a dose-response relationship, but it is unclear how many tyrosination levels were tested and whether the relationship is linear or saturating. Additionally, the claim that CLIP-170 and EB1 "synergize" to increase dynamicity is based on the observation that neither factor alone increases growth or catastrophe rates, but the combination does. However, the mechanism of this synergy is not explored. The authors suggest that CLIP-170 alters EB1 association at the plus-end, but no direct evidence for this is provided.
- **Why it matters** The quantitative relationship between tyrosination and CLIP-170 recruitment, and the mechanism of CLIP-170/EB1 synergy, are key to understanding how tyrosination regulates microtubule dynamics through effector recruitment. Without a clear quantitative framework and mechanistic insight, the conclusions are incomplete.
- **Resolution test** The authors should provide the actual data showing the relationship between tyrosination level and CLIP-170 density, including the range of tyrosination levels tested and the statistical analysis. They should also provide additional experiments or analysis to support the proposed mechanism of CLIP-170/EB1 synergy, such as direct measurement of EB1 or CLIP-170 binding to differentially tyrosinated microtubules.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Statistical analysis
- **Affected element** Microtubule dynamics measurements
- **Evidence pointer** Results section "The Intrinsically Disordered α-tubulin Tail Inhibits Microtubule Growth and Dynamicity"; Figure 1
- **Issue** The manuscript reports growth rates, catastrophe frequencies, and other dynamic parameters, but does not describe the statistical methods used to compare these parameters between tubulin variants. It is unclear how many microtubules were analyzed, how many independent experiments were performed, and what statistical tests were used.
- **Required correction** The authors should add a description of the statistical analysis, including the number of replicates, the statistical tests used, and how significance was determined.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data availability
- **Affected element** MD simulation data
- **Evidence pointer** STAR Methods section "MD simulations"
- **Issue** The MD simulation methods are described, but the simulation data and analysis scripts are not mentioned as being available. Given the importance of the simulations to the paper's conclusions, it would be helpful to make the simulation parameters, trajectories, and analysis scripts available to readers.
- **Required correction** The authors should consider depositing the simulation data and analysis scripts in a public repository, or at least provide more detailed information about the simulation setup and analysis in the Methods.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of in vivo relevance
- **Affected element** Discussion section
- **Evidence pointer** Discussion
- **Issue** The authors discuss the in vivo implications of their findings, but the connection between their in vitro results and the in vivo context could be strengthened. For example, they mention that detyrosination is associated with stable microtubules in cells, but do not discuss how their finding that detyrosination does not affect intrinsic dynamics reconciles with the observation that detyrosinated microtubules are more stable in cells.
- **Required correction** The authors should expand the Discussion to more thoroughly address how their in vitro findings relate to the in vivo observations of differential stability, and what additional factors might contribute to the stability of detyrosinated microtubules in cells.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract; Introduction
- **Issue** The term "detyrosinated" is used to describe tubulin lacking the C-terminal tyrosine, and "∆2" for tubulin lacking the last two residues. However, the relationship between these modifications and the "tyrosination cycle" could be clarified for readers who are not experts in the field.
- **Required correction** The authors should briefly define the tyrosination/detyrosination cycle and the ∆2 modification in the Introduction to make the manuscript more accessible to a broader audience.

## Risk / unsupported claims
- The claim that in vivo differences in microtubule stability "must result exclusively from selective effector recruitment" is not fully supported by the data presented, as the authors have only tested one tubulin isotype combination and have not ruled out other contributing factors.
- The mechanistic interpretation of the MD simulations, specifically that the α-tail occludes the longitudinal polymerization interface, is presented as an explanation for the growth inhibition, but the simulations do not model the polymerization process directly. This is acknowledged in the Limitations section, but the claim is still presented strongly in the Results.
- The claim that CLIP-170 and EB1 "synergize" to increase dynamicity is based on the observation that neither factor alone has an effect, but the mechanism of this synergy is not directly tested.
- The quantitative relationship between tyrosination level and CLIP-170 density is described as "quantitative tuning," but the actual data are not shown in the provided text, making it difficult to assess the strength of this claim.