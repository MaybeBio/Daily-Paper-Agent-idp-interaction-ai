## Review setup
- **Input scope** Full manuscript text including abstract, main text, and references to supplementary material
- **Assessment boundary** Scientific claims, methodology, evidence quality, and alignment with Nature-style criteria based solely on the provided manuscript
- **Shared manuscript claim summary** The authors propose a two-stage assembly strategy for DNA origami where partial staple subsets create metastable, disordered intermediates that can be induced to fold into complete triangular structures at room temperature within 2 hours, mimicking disorder-to-order transitions in intrinsically disordered proteins
- **Visible evidence base** Abstract, main text sections (Introduction, Results and Discussion, Conclusions), figure descriptions (Figures 1-4), and references to supplementary tables and figures
- **Missing materials affecting confidence** Supplementary figures (S1-S8), supplementary tables (S1-S4), detailed experimental methods, molecular dynamics simulation parameters, raw AFM image data, and statistical analysis details

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting approach to DNA origami assembly that draws an analogy to intrinsically disordered proteins. The two-stage assembly strategy is clearly described, and the combination of AFM imaging with molecular dynamics simulations provides complementary evidence. However, the current evidence base is insufficient to fully establish the central claims. Key limitations include the lack of detailed experimental protocols, incomplete statistical reporting, and the absence of direct evidence for the proposed "activating effect" mechanism. The work has potential interest for the DNA nanotechnology community, but the case for broad significance and mechanistic novelty is not fully developed from the provided materials.
- **Who would be interested in the results, and why** Researchers in DNA nanotechnology, particularly those working on DNA origami assembly mechanisms, dynamic DNA nanostructures, and molecular machines. The work may also appeal to scientists studying biomimetic folding processes and those interested in isothermal assembly strategies for practical applications. The analogy to intrinsically disordered proteins could attract interest from the broader biophysics community, though this connection is currently more suggestive than demonstrated.
- **Major strengths** The two-stage assembly concept is clearly articulated and experimentally tractable. The use of multiple staple subsets (intradomain, interdomain, random) provides a systematic comparison. The combination of AFM and oxDNA simulations offers complementary perspectives on structure and energetics. The reported yields for the intradomain and interdomain subsets are comparable to conventional assembly, which is encouraging for practical utility.
- **Major Concerns** The following concerns are identified
- **Minor Comments** The following comments are identified
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** Originality: The concept of using partial staple subsets to create metastable intermediates is a novel contribution to DNA origami assembly, though the analogy to IDPs is more inspirational than mechanistically established. Scientific importance: The work addresses a real challenge in isothermal DNA origami assembly, but the demonstrated scope is limited to a single triangular structure, and the practical advantages over existing methods are not fully quantified. Interdisciplinary readership: The IDP analogy and potential applications in molecular computing and diagnostics could attract interest beyond DNA nanotechnology, but the current presentation is too specialized for broad appeal. Technical soundness: The experimental design is reasonable, but the lack of detailed methods and statistical rigor undermines confidence in the quantitative claims. Readability for nonspecialists: The manuscript is generally well-written and accessible, though the mechanistic discussion assumes familiarity with DNA origami terminology.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding experimental detail, statistical reporting, and mechanistic evidence

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental methodology
- **Claim pointer** The authors claim that Stage 1 products are "metastable assemblies with disordered morphologies" and that Stage 2 induces "disorder-to-order transitions" at room temperature within 2 hours
- **Evidence pointer** Results and Discussion, Figures 2-3, location not provided
- **Concern** The manuscript lacks detailed experimental protocols for the two-stage assembly process. Critical parameters such as staple-to-scaffold ratios, buffer conditions, incubation times, and temperature control during Stage 2 are not specified in the main text. The supplementary material is referenced but not provided, making it impossible to assess the reproducibility of the experiments.
- **Why it matters** Without detailed methods, the scientific community cannot replicate or build upon these findings. The claim of isothermal assembly at room temperature is central to the paper's significance, and the experimental conditions under which this is achieved must be fully documented.
- **Resolution test** Provide complete experimental methods in the main text or supplementary material, including all buffer compositions, concentrations, incubation times, and temperature profiles. The methods should be detailed enough for independent replication.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical analysis
- **Claim pointer** The authors report specific yields (e.g., "approximately 59.6%, 55.9%, and 37.8%") and mean areas with standard deviations (e.g., "7002 ± 987 nm2") for Stage 2 products
- **Evidence pointer** Results and Discussion, Figures 2-3, location not provided
- **Concern** The manuscript does not report the number of independent experiments, the number of AFM images analyzed, or the number of structures counted for each yield and area measurement. Statistical significance testing between conditions is also absent. The standard deviations are reported but without context for how many measurements they are based on.
- **Why it matters** The quantitative claims about yields and structural quality are central to demonstrating the effectiveness of the two-stage approach. Without proper statistical reporting, it is unclear whether the differences between subsets are meaningful or within experimental noise.
- **Resolution test** Report the number of independent replicates, the total number of structures analyzed per condition, and appropriate statistical tests (e.g., t-tests or ANOVA) comparing yields and areas across conditions. Provide this information in the main text or supplementary material.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic evidence
- **Claim pointer** The authors propose that Stage 1 products exert an "activating effect" on the scaffold, resulting in a molecular conformation conducive for further folding
- **Evidence pointer** Conclusions, location not provided
- **Concern** The "activating effect" is presented as a mechanistic explanation, but no direct evidence is provided to support this claim. The molecular dynamics simulations show energy levels and fluctuations, but they do not demonstrate a specific activating mechanism. The authors reference their previous work showing that room-temperature assembly without Stage 1 activation rarely yields complete structures, but this is not shown in the current manuscript.
- **Why it matters** The proposed mechanism is central to the paper's conceptual framing and its analogy to IDP-induced folding. Without direct evidence, the mechanism remains speculative, and the significance of the work is diminished.
- **Resolution test** Provide direct experimental or simulation evidence for the activating effect, such as structural characterization of Stage 1 intermediates showing specific conformational features that facilitate subsequent folding, or comparative experiments with and without Stage 1 activation under identical conditions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Simulation-experiment correspondence
- **Claim pointer** The authors state that "the morphology observed via AFM generally corresponds with the simulation prediction" for each Stage 1 product
- **Evidence pointer** Results and Discussion, Figure 2, location not provided
- **Concern** The correspondence between AFM images and simulation snapshots is described qualitatively without quantitative comparison metrics. The AFM images show 2D projections of dried structures, while simulations provide 3D conformational ensembles. The criteria for "correspondence" are not defined, and the possibility of AFM artifacts (e.g., drying effects, tip convolution) is not discussed.
- **Why it matters** The claim of simulation-experiment agreement is used to validate the computational model and support the energetic interpretations. Without quantitative comparison, the strength of this validation is unclear.
- **Resolution test** Provide quantitative measures of shape similarity between AFM and simulation structures (e.g., radius of gyration, shape anisotropy, or image correlation metrics). Discuss potential AFM artifacts and how they were accounted for in the comparison.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1 description
- **Evidence pointer** Results and Discussion, Figure 1, location not provided
- **Issue** The description of the three staple subsets (intradomain, interdomain, random) is clear conceptually, but the figure itself is not provided. The text refers to "Figure 1b" for the subset definitions, but without seeing the figure, it is difficult to assess whether the spatial distributions are accurately represented.
- **Required correction** Ensure that Figure 1 clearly illustrates the spatial distribution of each subset on the triangular origami structure, with color coding or other visual distinctions that match the text descriptions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Yield comparison
- **Evidence pointer** Results and Discussion, Figure 3c, location not provided
- **Issue** The yields for Stage 2 products are reported as approximately 59.6%, 55.9%, and 37.8% for intradomain, interdomain, and random subsets, respectively. The full set control yield is reported as approximately 56.5%. It would be helpful to know whether the differences between these yields are statistically significant.
- **Required correction** Add statistical significance testing for yield comparisons and report p-values or confidence intervals.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Free energy discussion
- **Evidence pointer** Results and Discussion, Figure 4, location not provided
- **Issue** The free energy values are reported in units of kBT, but the absolute values are not placed in context. It is unclear how these energy differences translate to practical differences in folding kinetics or stability.
- **Required correction** Provide a brief discussion of the physical significance of the energy differences, perhaps by comparing to thermal energy scales or known DNA hybridization energies.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction
- **Evidence pointer** Introduction, location not provided
- **Issue** The introduction mentions recent reports of room-temperature DNA origami folding but does not cite specific references. The statement "Recent reports indicate that this folding process can also occur at room temperature27−31" is vague without details on what these reports achieved.
- **Required correction** Briefly summarize the key findings of the cited reports to provide context for how the current work advances beyond them.

## Risk / unsupported claims
- The claim that Stage 1 products are analogous to intrinsically disordered proteins is not directly supported by experimental evidence; the analogy is conceptual rather than mechanistic
- The "activating effect" proposed as the mechanism for successful Stage 2 folding is speculative and lacks direct evidence
- The claim that the two-stage strategy "robustly" converges on the global energy minimum is based on limited data from a single structure type and a single set of conditions
- The assertion that this method "theoretically enables more flexible and diverse structural transformations" is presented as a logical extension but is not demonstrated
- The quantitative yields and area measurements lack sufficient statistical context to assess their reliability
- The correspondence between AFM and simulation morphologies is claimed but not quantitatively demonstrated