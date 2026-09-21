## Review setup
- **Input scope** Full manuscript text (abstract, introduction, proposed solution, applications, roadmap, conclusion)
- **Assessment boundary** Scientific claims, technical feasibility, evidence quality, and internal consistency of the perspective article
- **Shared manuscript claim summary** The article argues that current AI-based protein structure prediction (e.g., AlphaFold) is limited by its static nature, and proposes that "World Models" (e.g., JEPA, Genie 3) applied to molecular dynamics will enable simulation of conformational trajectories, with transformative implications for oncology drug design
- **Visible evidence base** Citations to published works (AlphaFold, AlphaMissense, AlphaProteo, AlphaGenome, GeneJepa, Genie 3, Ianeselli et al.), two tables referenced but not provided, roadmap phases, and author's own reasoning
- **Missing materials affecting confidence** Tables 1 and 2 are referenced but not included; no figures; no detailed technical specifications of proposed architectures; no quantitative benchmarks or pilot data; no comparison with existing MD-enhanced AI methods (e.g., diffusion models for conformations)

## Reviewer
- **Overall assessment** This is a forward-looking perspective that identifies a genuine limitation in current AI-driven structural biology and proposes an interesting conceptual direction. The writing is clear and accessible, and the oncology applications are well-motivated. However, the article is largely speculative, with no new data, no technical depth on how World Models would be adapted to molecular dynamics, and no engagement with existing literature on conformational prediction (e.g., diffusion-based approaches, normal mode analysis, enhanced sampling combined with ML). The roadmap is plausible but lacks specificity on metrics, milestones, or fallback strategies. The article reads more as an opinion piece than a scientific perspective with testable hypotheses.
- **Who would be interested in the results, and why** Computational biologists, AI researchers working on scientific applications, structural biologists, and drug discovery scientists in oncology. The article offers a conceptual bridge between cutting-edge AI architectures and pressing problems in drug design, which may stimulate discussion and inspire new research directions.
- **Major strengths** 1) Clearly articulates a real limitation of static structure prediction. 2) Makes an accessible analogy between world models and protein dynamics. 3) Identifies relevant oncology applications (allostery, IDPs, resistance mutations) that are well-chosen and impactful. 4) Acknowledges key challenges (data scarcity, computational cost, validation) and includes a phased roadmap.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (no technical specificity), R1-M2 (no engagement with existing methods), R1-M3 (unsupported claims about Genie 3 capabilities), R1-M4 (roadmap lacks testable milestones)
- **Assessment against Nature-style criteria**  
  - *Originality*: Moderate. The core idea of applying world models to molecular dynamics is not entirely new (the authors cite Ianeselli et al.), and the article does not clearly differentiate its proposal from existing work on generative models for conformations.  
  - *Scientific importance*: Potentially high if the proposal were technically grounded, but as presented, the importance is asserted rather than demonstrated.  
  - *Interdisciplinary readership*: Good. The article is written for a broad audience and bridges AI, structural biology, and oncology.  
  - *Technical soundness*: Weak. The proposal lacks technical detail, and several claims about existing systems (e.g., Genie 3) are overstated or unverified.  
  - *Readability for nonspecialists*: Excellent. The prose is clear, the analogies are effective, and the structure is logical.
- **Recommendation posture** Currently not established from the provided evidence. The article is a thought-provoking opinion piece, but it does not meet the standard of a scientific perspective that advances a testable, technically grounded thesis. Major revisions are required to clarify the technical proposal, engage with existing literature, and temper unsupported claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The article claims that World Models such as JEPA and Genie 3 can be adapted to molecular dynamics to simulate conformational trajectories and predict induced fit.
- **Evidence pointer** Sections "The proposed solution: world models for molecular dynamics (MD)", "JEPA: learning the essence of change", "Genie 3: simulation of interactive and physically coherent worlds"; location not provided
- **Concern** The proposal is described only at a conceptual level. No details are given on how JEPA or Genie 3 would be adapted to molecular systems: what is the input representation (e.g., coordinates, internal coordinates, graphs), what is the latent space, how are forces or energies incorporated, how is temporal coherence enforced, and how would the model be trained on MD trajectories? The article does not address whether these architectures can handle the high dimensionality and physical constraints of molecular systems, nor does it discuss known limitations of world models in scientific domains.
- **Why it matters** Without technical specificity, the proposal is not actionable and cannot be evaluated for feasibility. A perspective article should provide enough detail for researchers to assess whether the proposed direction is plausible or to begin implementing it.
- **Resolution test** Provide a concrete description of the proposed architecture, including input/output representations, training objective, and how physical laws (e.g., energy conservation, Boltzmann distribution) would be incorporated. Alternatively, present pilot results on a simple system demonstrating feasibility.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific context
- **Claim pointer** The article implies that current AI-based methods are limited to static structure prediction and that World Models represent a novel direction for dynamics.
- **Evidence pointer** Sections "Introduction", "The problem: beyond static structure"; location not provided
- **Concern** The article does not engage with a substantial body of existing work on AI-based conformational prediction and molecular dynamics. Examples include diffusion models for protein conformations (e.g., AlphaFlow, Str2Str), normal mode analysis combined with machine learning, and the use of graph neural networks for molecular dynamics acceleration. The claim that World Models are the "next frontier" is weakened by the absence of a comparative discussion with these approaches.
- **Why it matters** A perspective should situate its proposal within the current research landscape. Failure to do so overstates novelty and may mislead readers about the state of the art.
- **Resolution test** Add a section reviewing existing AI methods for conformational dynamics and explicitly state how World Models differ from or improve upon them.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The article states that Genie 3 can "simulate interactive, photorealistic virtual worlds" and "maintain physical and visual coherence over time," and implies these capabilities transfer to molecular dynamics.
- **Evidence pointer** Section "Genie 3: simulation of interactive and physically coherent worlds"; location not provided
- **Concern** The description of Genie 3's capabilities is presented as established fact, but no primary source is cited for these claims. The article cites reference [9] but does not specify what it contains. Moreover, the leap from 2D video game environments to 3D molecular systems is nontrivial and is not addressed. The claim that Genie 3's "promptable world events" map directly to introducing a ligand into a protein system is an analogy, not a demonstrated capability.
- **Why it matters** The article's central argument rests on the assumption that capabilities demonstrated in one domain (video generation) transfer to another (molecular dynamics). This assumption is unsupported and may be invalid.
- **Resolution test** Provide a detailed citation for Genie 3's capabilities and discuss the specific challenges of transferring these capabilities to molecular systems, including differences in data modality, physical constraints, and evaluation metrics.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Falsifiability
- **Claim pointer** The roadmap (Phases 1-3) is presented as a path toward "proteome-scale world models" by 2035.
- **Evidence pointer** Section "Challenges and perspective toward 2035", "Roadmap toward 2035"; location not provided
- **Concern** The roadmap lacks specific, testable milestones. For example, Phase 1 aims to "demonstrate the capacity to predict induced fit for known ligands," but no criteria are given for what would constitute success (e.g., RMSD thresholds, comparison with experimental kinetics). Phase 2 mentions "first successes in de novo design of allosteric modulators," but "success" is undefined. Without measurable objectives, the roadmap cannot be evaluated or falsified.
- **Why it matters** A scientific roadmap should be structured around hypotheses that can be tested and milestones that can be assessed. The current formulation is too vague to guide research or to allow the community to track progress.
- **Resolution test** Define quantitative success criteria for each phase, such as specific accuracy thresholds for conformational prediction, benchmarks against experimental data, or clear go/no-go decision points.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Table references
- **Evidence pointer** Tables 1 and 2 are referenced in the text but not provided
- **Issue** The manuscript refers to Table 1 (limitations of current models) and Table 2 (comparison between current models and world models), but these tables are not included in the provided material. Without them, the reader cannot fully assess the comparative claims.
- **Required correction** Include the tables in the manuscript or remove the references.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Use of "dream" and "molecular radiograph"
- **Evidence pointer** Abstract, Introduction, Conclusion; location not provided
- **Issue** The metaphors "dream" and "molecular radiograph" are evocative but may be confusing in a scientific context. "Dream" is used to describe simulation, which could be misinterpreted as lacking rigor. "Molecular radiograph" is not a standard term and may obscure rather than clarify the limitation being described.
- **Required correction** Consider replacing these metaphors with more precise technical language, or define them explicitly on first use.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion of challenges
- **Evidence pointer** Section "Challenges and perspective toward 2035"; location not provided
- **Issue** The article mentions data scarcity, computational cost, and validation as challenges, but does not discuss the challenge of model interpretability. For clinical applications, understanding why a model predicts a particular conformational trajectory will be critical for regulatory approval and clinical trust.
- **Required correction** Add a brief discussion of interpretability and explainability as additional challenges.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Citation practice
- **Affected element** Reference [9] for Genie 3
- **Evidence pointer** Section "Genie 3: simulation of interactive and physically coherent worlds"; location not provided
- **Issue** The citation for Genie 3 is vague. It is unclear whether this refers to a preprint, a blog post, or a peer-reviewed publication. Given the centrality of Genie 3 to the argument, a precise citation is needed.
- **Required correction** Provide a full, accurate citation for Genie 3, including the source type and availability.

## Risk / unsupported claims
- The claim that World Models will enable simulation of conformational trajectories and predict induced fit is unsupported by any pilot data or technical analysis.
- The claim that Genie 3 maintains "physical and visual coherence over time" is presented as fact without a verifiable citation.
- The claim that "undruggable" targets such as KRAS, c-Myc, and p53 could become accessible through World Model-based approaches is speculative and not grounded in any preliminary evidence.
- The roadmap's phases and timelines are presented without justification or reference to existing technological trends.
- The statement that "AI will not merely predict structures but simulate life at the molecular level" is rhetorical and not a scientifically testable claim.