## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no methods, figures, or supplementary material were provided for evaluation
- **Shared manuscript claim summary** The authors use all-atom molecular dynamics simulations to investigate the membrane binding mechanism of the C terminal region of Mid1, an anillin related protein in fission yeast. They report that the disordered L3 loop of the C2 domain and the PH domain can each bind the membrane separately via charged lipid contacts. In simulations initiated away from the membrane, Mid1 binds through the L3 loop and adopts a vertical orientation with the PH domain away from the membrane. A configuration with both C2 and PH initially bound remains membrane associated. The authors interpret these multiple binding modes as potentially reflecting Mid1's diverse interactions and mechanical force bearing capacity.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or simulation details were provided
- **Missing materials affecting confidence** Full manuscript, simulation protocols, force field parameters, system setup details, lipid composition specifics, trajectory analyses, convergence assessments, and any quantitative results

## Reviewer
- **Overall assessment** The abstract presents a plausible and potentially interesting simulation study addressing a relevant question in cytokinetic ring organization. The central claim that Mid1 exhibits multiple membrane binding modes is supported by the described simulation outcomes, but the evidence base available for this review is limited to the abstract. The interpretation that these modes reflect adaptive biological function is speculative and not directly testable from the simulation data described. The work may be of interest to the cell division and membrane biophysics communities, but the current evidence is insufficient to fully evaluate technical soundness or the strength of the conclusions.
- **Who would be interested in the results, and why** Researchers studying cytokinesis, particularly the molecular mechanisms of contractile ring assembly and anchoring in fission yeast. The work also bears relevance to the broader anillin family and to investigators interested in protein membrane interactions involving PH and C2 domains. Computational biophysicists studying protein lipid interactions through molecular dynamics may find the simulation approach of interest.
- **Major strengths** The study addresses a specific and mechanistically important question about whether the two membrane binding regions of Mid1 can bind simultaneously. The use of a lipid composition based on experimental measurements is a positive feature. The observation of distinct binding modes depending on initial conditions is a potentially informative result that could have implications for understanding Mid1 function.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract does not provide information on simulation length, number of replicates, force field choice, or convergence criteria. Without these details, the reliability of the observed binding modes cannot be assessed. The claim that the vertical orientation is "stabilized" requires evidence of simulation convergence and stability over time, which is not presented in the abstract.
- **Assessment against Nature-style criteria**  
  Originality: The question of whether PH and C2 domains of anillin family proteins can simultaneously engage the membrane is a specific and relatively underexplored point, giving the study some originality. However, the conceptual framework of multiple membrane binding modes is not entirely novel.  
  Scientific importance: The work addresses a mechanistic detail relevant to cytokinesis, a fundamental cell biological process. The importance is moderate, as the findings are specific to Mid1 and would need to be generalized to other anillins to have broader impact.  
  Interdisciplinary readership: The topic sits at the interface of cell biology and computational biophysics. The abstract is written in a way that is largely accessible to both communities, though some simulation specific terminology is used without explanation.  
  Technical soundness: Cannot be adequately assessed from the abstract alone. The lack of methodological detail prevents evaluation of simulation quality, sampling, and analysis rigor.  
  Readability for nonspecialists: The abstract is generally clear and well structured. The biological context is introduced adequately, and the simulation findings are described in accessible language. Some terms such as "vertical orientation" could benefit from clarification.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents an interesting hypothesis and preliminary simulation results, but the evidence base is too limited to support the conclusions as stated. A full evaluation would require access to the complete manuscript, including methodological details and quantitative results.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors claim that "Mid1 binds through the L3 loop and is stabilized in a vertical orientation with the PH domain away from the membrane" based on simulations started away from the membrane.  
- **Evidence pointer** Abstract, simulation description; location not provided  
- **Concern** The abstract does not provide any information about simulation length, number of independent simulations, force field parameters, or convergence criteria. The term "stabilized" implies a stable state over a meaningful timescale, but without these details it is impossible to determine whether the observed orientation is a genuine stable state or an artifact of insufficient sampling.  
- **Why it matters** The central conclusion of the study depends on the reliability of the simulated binding modes. If the simulations are too short or not converged, the observed orientations may not represent physiologically relevant states, undermining the interpretation of multiple binding modes.  
- **Resolution test** The full manuscript must provide simulation durations, replicate numbers, convergence analyses (e.g., root mean square deviation over time, cluster analysis of orientations), and justification for the force field and system setup. The claim of stabilization should be supported by quantitative measures of orientation stability over the simulation trajectory.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence strength  
- **Claim pointer** The authors state that "a configuration with both C2 and PH initially bound to the membrane remains associated with the membrane" and interpret this as evidence for a multimodal binding mode.  
- **Evidence pointer** Abstract, simulation description; location not provided  
- **Concern** The abstract reports only that the dual bound configuration "remains associated" but provides no quantitative information on the duration of association, the stability of the contacts, or whether this state is kinetically accessible from unbound or singly bound states. The biological relevance of this state depends on whether it can form under physiologically relevant conditions, not merely whether it persists when artificially pre positioned.  
- **Why it matters** The interpretation that multiple binding modes reflect adaptive biological function requires evidence that these modes are accessible and functionally relevant. A pre positioned dual bound state that persists in a simulation does not demonstrate that this state forms spontaneously or that it has functional significance.  
- **Resolution test** The full manuscript should provide free energy calculations or enhanced sampling studies showing the relative stability and accessibility of the different binding modes. At minimum, multiple independent simulations starting from different initial conditions should be shown to converge to the same ensemble of states. The manuscript should also discuss the kinetic accessibility of the dual bound state.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** No  
- **Axis** Interpretation and overreach  
- **Claim pointer** The authors conclude that "These multiple modes of binding may reflect Mid1's multiple interactions with membranes and other node proteins, and ability to sustain mechanical forces."  
- **Evidence pointer** Abstract, concluding statement; location not provided  
- **Concern** This interpretation extends beyond what the simulation data can directly support. The simulations address membrane binding of the C terminal region in isolation. The connection to interactions with other node proteins and mechanical force bearing is speculative and not tested in the presented work.  
- **Why it matters** Overinterpretation of simulation results can mislead readers about the strength of the conclusions. While such speculation can be valuable as a discussion point, presenting it as a conclusion without supporting evidence weakens the scientific rigor of the study.  
- **Resolution test** The authors should clearly separate simulation derived findings from speculative interpretations. The discussion should frame the mechanical and protein interaction implications as hypotheses for future work, not as conclusions supported by the present data. If the authors wish to make these claims, they should provide additional simulations or experimental evidence addressing these functions.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Abstract, description of binding modes  
- **Evidence pointer** Abstract, results section; location not provided  
- **Issue** The phrase "vertical orientation" is used without definition. It is unclear what reference frame this orientation is relative to, and whether this terminology would be immediately clear to readers outside the simulation community.  
- **Required correction** Define the orientation relative to the membrane plane or provide a brief description of what vertical means in this context, such as the angle of the protein's principal axis relative to the membrane normal.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Abstract, lipid composition description  
- **Evidence pointer** Abstract, methods description; location not provided  
- **Issue** The abstract states that the lipid composition was "based on experimental measurements" but does not specify the composition or the source of these measurements. This makes it difficult to assess the physiological relevance of the simulation conditions.  
- **Required correction** Provide the specific lipid composition used in the simulations and cite the experimental source. If space constraints in the abstract prevent this, ensure the full manuscript provides this information prominently.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Contextualization  
- **Affected element** Abstract, comparison to previous work  
- **Evidence pointer** Abstract, introduction; location not provided  
- **Issue** The abstract states that "previous studies have shown that both PH and C2 domains can associate with the membrane" but does not indicate how the present findings extend or differ from these prior results beyond the question of simultaneous binding.  
- **Required correction** Briefly state what is new about the present findings relative to prior work, such as the identification of specific binding modes or the characterization of orientation preferences that were not previously described.

## Risk / unsupported claims
- The claim that Mid1 is "stabilized" in a vertical orientation is unsupported without convergence and stability data, which are not provided in the abstract.
- The interpretation that multiple binding modes relate to interactions with other node proteins and mechanical force bearing is unsupported by the simulation data described.
- The claim that the dual bound configuration "remains associated" is presented without quantitative duration or stability metrics, making the strength of this observation unassessable.
- The physiological relevance of the observed binding modes cannot be evaluated without information on the timescales of the simulations relative to biologically relevant timescales.
- The statement that the lipid composition was "based on experimental measurements" cannot be verified without specifying the composition and source.