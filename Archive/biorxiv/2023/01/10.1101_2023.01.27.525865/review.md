## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, supplemental figure captions, movie captions, acknowledgements, footnotes)
- **Assessment boundary** Scientific content and technical soundness of the simulation study as presented; no assessment of editorial fit or publication venue
- **Shared manuscript claim summary** The authors use all-atom molecular dynamics simulations to characterize membrane binding of the fission yeast anillin-related protein Mid1, proposing that the C2 domain L3 loop mediates initial membrane attachment, that the PH domain can bind independently but is kinetically disfavored in the full C2-PH construct, and that multiple binding modes may support Mid1's anchoring and mechanical functions in the cytokinetic ring.
- **Visible evidence base** Main text figures 1-5 (referenced but not fully visible in supplied material), supplemental figures S1-S3 (referenced), table 1 (referenced), eight movie captions, methods section
- **Missing materials affecting confidence** Actual figure panels and numerical data are not provided; only figure captions and text descriptions are available. This limits quantitative verification of contact analyses, helix propensities, and orientation distributions.

## Reviewer
- **Overall assessment** The manuscript presents a systematic simulation study addressing a relevant question in cytokinetic ring biology: how Mid1 anchors to the plasma membrane. The work is technically competent in its use of all-atom MD with an experimentally informed membrane composition, and the finding that the L3 loop mediates initial binding while the PH domain is kinetically excluded in the full-length context is interesting. However, the central claims regarding "adaptive and multimodal" binding rest on limited sampling (10 replicas per condition, sub-microsecond to 1.5 microsecond timescales) and on inferences from constructs that may not fully represent the physiological state. The link to mechanical function and dimerization is speculative and not directly tested. The manuscript would benefit from clearer presentation of quantitative results and from tempering conclusions that exceed the simulation evidence.
- **Who would be interested in the results, and why** Researchers studying cytokinesis, particularly the molecular mechanisms of contractile ring assembly and anchoring in fission yeast; computational biophysicists interested in membrane-protein interactions and anillin family proteins; experimentalists studying Mid1 or anillin localization who may use these simulations to design mutation or crosslinking experiments.
- **Major strengths** 1) Use of a membrane composition informed by experimental measurements of fission yeast, increasing physiological relevance. 2) Systematic comparison of isolated domains versus the full C2-PH construct, which reveals context-dependent binding behavior. 3) Inclusion of known disease-relevant or localization-relevant mutations (4A, NM) provides a bridge to prior experimental work. 4) The proposed model in Figure 6 integrates simulation results with super-resolution data, offering a testable framework.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (sampling sufficiency), R1-M2 (PH domain construct relevance), R1-M3 (quantitative support for multimodal binding), R1-M4 (link to mechanical function)
- **Assessment against Nature-style criteria** Originality: moderate. The question of Mid1 membrane binding has been addressed experimentally, but the simulation-based exploration of binding modes and kinetics is a novel contribution. Scientific importance: moderate. The findings are relevant to cytokinesis but do not resolve a long-standing controversy or open a fundamentally new direction. Interdisciplinary readership: limited. The work is primarily of interest to biophysicists and cell biologists; the broad significance to a general scientific audience is not strongly articulated. Technical soundness: generally adequate but with sampling limitations that weaken the strongest claims. Readability for nonspecialists: the introduction and discussion are accessible, but the results section assumes familiarity with MD simulation conventions and membrane-protein interaction terminology.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding sampling sufficiency and the interpretation of PH domain behavior. Currently not fully established from the provided evidence.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "in all ten simulations, the C2-PH binds initially through the L3 loop" and that the PH domain "did not contact the membrane in any simulations" for the freely diffusing C2-PH construct.
- **Evidence pointer** Results section, Figure 3, Table 1
- **Concern** The central conclusion that the L3 loop is the primary initial membrane-binding element and that the PH domain is kinetically excluded is based on only 10 independent simulations per condition, with the C2-PH simulations run for at least 1300 ns. Given the stochastic nature of protein-membrane association, 10 replicas may be insufficient to capture rare but functionally relevant binding events, especially for the PH domain, which binds readily in isolation. The authors do not report statistical measures (e.g., confidence intervals, binding free energies, or survival analyses) that would support the generality of their observations. Without additional replicas or longer timescales, the claim that PH binding is "kinetically disfavored" in the full-length context is not robustly established.
- **Why it matters** The proposed model of Mid1 anchoring depends critically on the relative kinetics of L3 versus PH binding. If PH binding occurs on longer timescales or under conditions not sampled here, the model would need revision. The distinction between "does not bind" and "has not bound within the simulation time" is essential for the validity of the conclusions.
- **Resolution test** Provide additional independent simulations (e.g., 20-30 per condition) or enhanced sampling approaches (e.g., metadynamics, umbrella sampling) to estimate binding free energies or mean first-passage times for L3 and PH binding. Report quantitative metrics with error bars. Alternatively, temper the claim to state that PH binding was not observed within the simulation timescales, without asserting a general kinetic barrier.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the PH domain did not contact the membrane in any simulations" of the freely diffusing C2-PH, and use this to argue that the L3 loop dominates initial binding.
- **Evidence pointer** Results section, Figure 3, Methods section
- **Concern** The PH domain simulations in isolation used a construct of residues 805-900, which includes the PH domain but not the adjacent CNCT region or the L3 loop. In the full C2-PH construct, the PH domain is connected to the C2 domain via the flexible CNCT region. The authors note that "the connector region exhibits noticeable flexibility," but they do not assess whether this flexibility could allow the PH domain to sample membrane-proximal orientations that are not captured in their analysis. Furthermore, the initial placement of the C2-PH relative to the membrane may bias the observed binding mode; the authors state that "each simulation had a different rotational orientation," but the distance from the membrane and the specific orientations are not described in sufficient detail to rule out steric or electrostatic effects that disfavor PH binding.
- **Why it matters** The conclusion that the PH domain is not involved in initial binding has implications for understanding Mid1's function, particularly if PH-mediated interactions are important for protein-protein contacts rather than direct membrane binding. If the simulation setup inadvertently disfavors PH binding, the interpretation would be an artifact of the system preparation.
- **Resolution test** Provide a detailed description of the initial distances and orientations of the C2-PH relative to the membrane for all 10 replicas. Consider running additional simulations with the PH domain initially placed closer to the membrane or with the C2 domain oriented differently. Report the minimum distance between the PH domain and the membrane over time for all replicas to demonstrate that the PH domain had opportunities to bind.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The title and abstract describe Mid1 as an "adaptive and multimodal contractile ring anchoring protein," and the discussion states that "the Mid1 monomer has many modes of membrane binding."
- **Evidence pointer** Abstract, Discussion section, Figure 6
- **Concern** The evidence for "multimodal" binding is indirect. The authors observe L3-mediated binding in the freely diffusing C2-PH simulations and stable binding of L3, L0, and PH when the C2-PH is initialized in a bound configuration. However, they do not demonstrate that these different modes are functionally distinct or that they are accessed under physiologically relevant conditions. The claim of "adaptivity" is speculative, as the simulations do not test responses to mechanical force or changes in membrane composition. The model in Figure 6 is presented as a synthesis, but the supporting data for the arrangement of Mid1 relative to other node proteins is not provided in the manuscript.
- **Why it matters** The title and framing promise a broader conceptual contribution than the data deliver. If the multiple binding modes are simply alternative states that are not functionally differentiated, the "adaptive and multimodal" framing overstates the findings. This could mislead readers about the strength of the evidence.
- **Resolution test** Either provide direct simulation evidence for functional consequences of different binding modes (e.g., differential responses to membrane tension, lipid composition, or protein binding partners) or revise the title and abstract to reflect the more limited claim that Mid1 exhibits multiple membrane-binding interfaces with distinct kinetics.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the L0 loop contacts, which we observed less often in freely diffusing C2-PH simulations, but appear stable after formation, include hydrophobic residues that insert into the membrane."
- **Evidence pointer** Results section, Figure 3, Movie 4
- **Concern** The L0 loop insertion is observed in only one of ten simulations, and the authors do not provide quantitative details on the depth of insertion, the residues involved, or the stability of the interaction beyond the simulation timescale. The claim that L0 insertion is "stable" is based on a single trajectory and may not be representative. Additionally, the functional significance of L0 insertion is not established, as no mutations targeting the L0 loop are tested.
- **Why it matters** The L0 loop is presented as a novel membrane-binding interface, but the evidence is anecdotal. If this is a rare or non-physiological event, including it as a major finding could be misleading. Conversely, if it is functionally important, the authors should provide stronger evidence.
- **Resolution test** Perform additional simulations to assess the frequency and stability of L0 insertion. Test mutations in the L0 hydrophobic residues to determine if they affect membrane binding in the simulations. Provide quantitative measures of insertion depth and contact lifetimes.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 3D
- **Evidence pointer** Results section, Figure 3D
- **Issue** The description of the angle analysis in Figure 3D is unclear. The authors state that "the C2 domain explores a range of angles with respect to the membrane normal," but they do not define how this angle is calculated or what values are considered significant. The figure is not visible in the supplied material, so the reader cannot assess the data.
- **Required correction** Provide a clear definition of the angle metric (e.g., angle between the membrane normal and the principal axis of the C2 domain) and report the range of angles observed across replicas. Consider adding a schematic to illustrate the angle definition.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section, Table 1
- **Evidence pointer** Methods section, Table 1
- **Issue** The methods state that "the duration of equilibration steps was increased for individual cases if needed," but no details are provided on which cases required longer equilibration or how the decision was made. This introduces potential variability in the simulation protocol that could affect reproducibility.
- **Required correction** Specify the criteria for extending equilibration and report the actual equilibration times for each system in Table 1.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion section, paragraph on dimerization
- **Evidence pointer** Discussion section
- **Issue** The discussion of dimerization is speculative and relies on visual inspection of aligned structures (Supplemental Figure S2C-F). The authors state that "it is likely" that L3 loop binding in the dimer would prevent PH binding, but they do not provide quantitative support for this claim, such as steric clash calculations or distance measurements.
- **Required correction** Either provide quantitative analysis of the dimer alignment (e.g., minimum distances between the partner PH domain and the membrane) or clearly label this as a hypothesis that requires further testing.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results section, Figure 5
- **Evidence pointer** Results section, Figure 5
- **Issue** The authors state that "the 4A simulations quickly bound the membrane through the L3 loop on timescales similar to that of WT simulations," but they do not report the actual binding times or compare them statistically. The claim that 4A has no effect is based on qualitative similarity.
- **Required correction** Report the binding times for each simulation and perform a statistical comparison (e.g., a t-test or Mann-Whitney U test) between WT and mutant conditions.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that "these multiple modes of binding may reflect Mid1's multiple interactions with membranes and other node proteins, and ability to sustain mechanical forces." This sentence is vague and does not specify which interactions or forces are meant. It also overstates the implications of the simulation data.
- **Required correction** Revise the abstract to more precisely state what was observed (e.g., "simulations show that the L3 loop mediates rapid initial binding, while the PH domain can bind stably when pre-positioned, suggesting multiple binding modes that may be relevant for different stages of node assembly").

## Risk / unsupported claims
- The claim that Mid1 is "adaptive" and "multimodal" in its anchoring function is not directly supported by the simulation data, which do not test functional consequences of different binding modes.
- The assertion that the PH domain is "kinetically disfavored" in the full C2-PH context is based on limited sampling and may not hold over longer timescales.
- The proposed model in Figure 6, including the arrangement of Mid1 relative to other node proteins and the role of the PH domain in protein-protein interactions, is speculative and not tested in this study.
- The statement that "the L0 loop contacts... appear stable after formation" is based on a single simulation and is not statistically supported.
- The claim that mutations to the candidate helix (4A) have no effect on binding is based on qualitative comparison without statistical testing.
- The relevance of the simulation results to the in vivo behavior of Mid1, particularly regarding the effects of phosphorylation and interactions with other node proteins, is not established.