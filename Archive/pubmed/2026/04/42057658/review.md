## Review setup
- **Input scope** Full manuscript text (abstract, introduction, main sections, conclusion, funding, declarations)
- **Assessment boundary** Scientific content, technical soundness, and clarity of the presented review; no assessment of editorial fit or publication decision
- **Shared manuscript claim summary** The authors review recent developments in in vitro mimetics of cellular crowding and solvation for protein folding studies, arguing that combined steric and non-steric mimetics can reproduce in-cell protein behaviors and offer practical advantages for high-throughput applications
- **Visible evidence base** Full text of the review, including descriptions of published studies, methodological approaches, and cited literature (references listed by number but not individually provided)
- **Missing materials affecting confidence** Reference list contents, figure panels, and specific experimental details of cited studies are not available; the review's claims rely on secondary descriptions of primary literature

## Reviewer
- **Overall assessment** This is a well-structured and informative review that provides a useful framework for categorizing in vitro mimetics of cellular environments for protein folding studies. The distinction between steric and non-steric interactions is clearly articulated, and the progression from simple polymer-based crowding agents to more complex systems such as GUVs, lysates, and combined mimetics is logically presented. The authors demonstrate good command of the literature and identify important gaps and future directions. However, the review would benefit from more critical evaluation of the limitations and potential artifacts of the described mimetics, and from clearer articulation of how these approaches can be validated against in-cell measurements. The claims regarding high-throughput applications and machine learning training are intriguing but underdeveloped.

- **Who would be interested in the results, and why** Researchers in protein folding, biophysics, and cellular biochemistry would find this review valuable as a synthesis of current mimetic approaches. Investigators studying protein behavior in living cells, those developing in vitro reconstitution systems, and computational biologists working on structure prediction in cellular contexts would also benefit. The review provides a practical framework for selecting mimetic systems and highlights the importance of accounting for both steric and chemical interactions.

- **Major strengths** 
  1. Clear conceptual organization around steric versus non-steric interactions
  2. Good coverage of recent methodological developments including GUVs, lysates, and combined mimetics
  3. Thoughtful discussion of organism-specific and compartment-specific differences
  4. Recognition of the importance of non-steric interactions, which are often overlooked
  5. Practical guidance for selecting mimetic systems based on cellular context

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "a mixture of 150 mg/ml Ficoll and 60% lysis buffer exactly reproduced the opposite in-cell stability of PGK and VlsE" and that "an improved, optically transparent recipe using 20% M-PER™ lysis buffer produced the in-cell stability of PGK, the fourU RNA thermometer, and a λ-repressor fragment"
- **Evidence pointer** Section "Mimetics that account for steric and non-steric interactions", location not provided
- **Concern** The claim of "exactly reproduced" in-cell stability is strong and requires careful qualification. The authors do not specify what metric of stability was matched (e.g., free energy of unfolding, melting temperature, kinetic rates) nor the precision of the match. Given the complexity of cellular environments and the simplified nature of mimetics, exact reproduction seems unlikely. The subsequent statement that the same mixture "is less accurate and even fails when specific interactions play a large role" somewhat contradicts the earlier claim of exact reproduction.
- **Why it matters** Overstating the accuracy of mimetic systems could mislead readers into overconfidence in these approaches. The field would benefit from honest assessment of the limits of current mimetics, particularly given the acknowledged failures with specific interactions.
- **Resolution test** The authors should specify the quantitative metric used to assess reproduction of in-cell stability, provide error estimates or statistical comparisons, and clearly delineate the conditions under which the mimetic succeeds versus fails.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors state that "Mimetics can further approach biological accuracy through mixtures that simultaneously account for steric and non-steric interactions" and that such mimetics "provide a convenient and cost-effective means to predict protein behavior in diverse cellular environments, which may benefit high-throughput applications, such as screening therapeutic candidates or training machine learning-based in-cell protein structure prediction models"
- **Evidence pointer** Abstract and Section "Opportunities for experimental and computational development", location not provided
- **Concern** The claimed benefits for high-throughput screening and machine learning training are presented without critical examination of the challenges. For screening applications, the throughput of current mimetic systems (particularly lysate-based approaches) is not discussed. For machine learning, the authors do not address how mimetic data would be labeled or how it would complement existing in-cell datasets. The claim that mimetics can "bridge the gap between theory and experiment" is vague.
- **Why it matters** These claims position the review as relevant to applied and computational communities, but without substantive discussion they remain aspirational. The review would be strengthened by concrete examples or feasibility assessments.
- **Resolution test** The authors should either provide specific examples of mimetic-based screening or training applications, or temper these claims to reflect current capabilities and limitations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "as no polymer is truly inert, there is no field consensus on the optimal recipe for an inert, steric crowding mimetic" and that "high concentrations of polymers may prove useful for mimicking confinement in mesh-like environments such as cytoskeletal lattices or extracellular matrix fibers"
- **Evidence pointer** Section "Mimetics of steric crowding in organisms and tissues", location not provided
- **Concern** The discussion of polymer-based crowding agents would benefit from more systematic treatment of their limitations. The authors mention that polymers "mesh at increasing concentrations" but do not discuss the concentration range over which this occurs for specific polymers, nor do they address the well-documented issue of polymer-protein interactions that can confound crowding studies. The suggestion that polymer meshing could mimic cytoskeletal lattices is interesting but speculative and not supported by specific examples.
- **Why it matters** The choice of crowding agent is central to the validity of mimetic studies. A more critical assessment of polymer limitations would help readers make informed choices and interpret literature results.
- **Resolution test** The authors should provide a more detailed comparison of polymer properties, including known interaction propensities, and either cite specific studies using polymer meshing to mimic cytoskeletal environments or clearly label this as a proposal.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Readability for nonspecialists
- **Claim pointer** The review covers "mimetics of in-cell and subcellular crowding and solvation for protein folding" and discusses "steric crowding interactions" and "non-steric chemical interactions"
- **Evidence pointer** Throughout, location not provided
- **Concern** The distinction between steric and non-steric interactions is introduced in the Introduction and used throughout, but the physical basis of these interactions is not explained in sufficient depth for nonspecialist readers. Terms such as "excluded-volume effects," "Hofmeister effect," and "liquid-liquid phase separation" are used without adequate definition or context. The relationship between crowding and solvation, which appears in the title, is never explicitly defined or discussed as a distinct concept.
- **Why it matters** The review targets a broad biochemical audience, and the title promises coverage of solvation effects. Without clear definitions and a dedicated discussion of solvation, readers may struggle to follow the arguments and the review may not fully deliver on its stated scope.
- **Resolution test** The authors should add brief explanations of key physical concepts and include a section or subsection explicitly addressing solvation effects and their relationship to crowding.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section "Mimetics of steric crowding in organisms and tissues"
- **Evidence pointer** Location not provided
- **Issue** The sentence "A few experimental studies have explored binary mixtures of crowding agents, which show nonadditive effects where the mixture is more stabilizing than the sum of the effects of the individual crowding agents" is grammatically awkward and could be clearer.
- **Required correction** Revise to something like "A few experimental studies have explored binary mixtures of crowding agents, which show nonadditive effects: the mixture is more stabilizing than the sum of the effects of the individual crowding agents."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section "Non-steric interactions differ between eukaryotic cell lines and within cellular compartments"
- **Evidence pointer** Location not provided
- **Issue** The authors mention that "there also has been work on reconstituting the endoplasmic reticulum in vitro and probing its ion dynamics" but do not provide specific examples or citations beyond the reference numbers.
- **Required correction** Add a brief description of the reconstitution approach and its relevance to protein folding mimetics.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section "Mimetics that account for steric and non-steric interactions"
- **Evidence pointer** Location not provided
- **Issue** The phrase "homogenous protein concentrated to physiological crowding levels" is ambiguous; it is unclear whether this refers to a single protein species or a mixture.
- **Required correction** Clarify whether the approach uses a single protein or a mixture and specify the protein concentration range considered "physiological."

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section "Opportunities for experimental and computational development"
- **Evidence pointer** Location not provided
- **Issue** The discussion of machine learning applications mentions "deep learning models capable of high-accuracy sequence-based structure prediction" but does not discuss how mimetic data would be integrated with these models.
- **Required correction** Add a brief discussion of how mimetic-derived data could be used in training or validation of structure prediction models.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section "Macromolecular crowding in sub-cellular compartments and transient organelles"
- **Evidence pointer** Location not provided
- **Issue** The term "biocondensates" is used without definition; the authors later use "coacervates" and "liquid-liquid phase separation" but the relationship between these terms is not made explicit.
- **Required correction** Define "biocondensates" and clarify the relationship to coacervates and membraneless organelles.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section "Chemical composition of prokaryotes versus eukaryotes"
- **Evidence pointer** Location not provided
- **Issue** The statement that "the observation that surface charge differently modifies the diffusion properties of the same protein in bacterial and mammalian cellular environments suggests inherent differences in the types and distributions of chemical interactions" is presented without discussion of alternative explanations, such as differences in viscosity or macromolecular crowding between cell types.
- **Required correction** Acknowledge alternative interpretations or provide additional evidence supporting the conclusion that chemical interactions, rather than physical differences, are responsible.

## Risk / unsupported claims
- The claim that a specific mimetic mixture "exactly reproduced" in-cell stability is not supported by quantitative data in the text; the metric and precision of the match are unspecified
- The assertion that mimetics "may benefit high-throughput applications, such as screening therapeutic candidates or training machine learning-based in-cell protein structure prediction models" is speculative and not supported by specific examples or feasibility analysis
- The suggestion that polymer meshing could mimic cytoskeletal lattices or extracellular matrix fibers is presented without supporting citations or experimental evidence
- The statement that "mimetics can further approach biological accuracy through mixtures that simultaneously account for steric and non-steric interactions" is presented as a general conclusion but the limitations of such mixtures (acknowledged later in the text) are not integrated into this claim
- The claim that "lysates should be prepared from the cell line of interest" is presented as a recommendation without discussion of practical challenges or evidence that cell-line-specific lysates are necessary for accurate mimetics