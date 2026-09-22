## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, technical soundness, and presentation quality of the review article
- **Shared manuscript claim summary** The manuscript presents a systematic survey of generative AI in protein design, organized around neural representations, generative architectures, and task settings, with emphasis on evaluation standards and responsible development.
- **Visible evidence base** Complete manuscript text including all sections, tables, and references
- **Missing materials affecting confidence** Figures and tables referenced in the text (e.g., Table I-VII, Fig. 2) were not provided; this limits verification of data presentation quality

## Reviewer
- **Overall assessment** This manuscript provides a broad and timely survey of generative modeling in protein design. The organization around representations, model architectures, and task settings is logical and comprehensive. The inclusion of evaluation standards and responsible development considerations is commendable and addresses a gap in existing literature. However, the survey would benefit from deeper critical analysis of method limitations, more concrete comparisons between approaches, and clearer articulation of open problems. The writing is generally clear but occasionally verbose, and some technical descriptions lack precision.
- **Who would be interested in the results, and why** Researchers and practitioners in computational biology, protein engineering, and machine learning would find this survey valuable as an entry point to the rapidly evolving field. The structured taxonomy and consolidated evaluation practices would help newcomers navigate the literature. The discussion of biosecurity and responsible development would also interest policymakers and ethicists working at the intersection of AI and biotechnology.
- **Major strengths** 1) Comprehensive coverage of generative model families including diffusion, flow matching, and language models. 2) Clear articulation of the generator-oracle boundary, which is conceptually useful. 3) Thoughtful consolidation of evaluation metrics and leakage-aware benchmarking practices. 4) Inclusion of responsible development considerations, which is increasingly important. 5) Good balance between breadth and depth across multiple task settings.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** The survey's claims about method performance and state-of-the-art status require more rigorous substantiation. Several statements about model capabilities lack specific quantitative comparisons or citations to benchmark results. The discussion of evaluation standards would benefit from concrete examples of how different metrics behave on real design tasks.
- **Assessment against Nature-style criteria** Originality: The survey offers a useful synthesis but does not present fundamentally new conceptual frameworks. Scientific importance: High, given the rapid growth of the field and need for consolidated guidance. Interdisciplinary readership: The manuscript bridges machine learning, structural biology, and protein engineering effectively. Technical soundness: Generally sound but with some imprecise technical descriptions. Readability for nonspecialists: Good overall, though some sections assume familiarity with advanced ML concepts.
- **Recommendation posture** Supportive if technical concerns are resolved

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that flow matching methods "often enabling substantially fewer sampling steps" compared to diffusion models, and that FrameFlow "significantly accelerates inference" while "maintaining generation quality."
- **Evidence pointer** Section III-B, location not provided
- **Concern** The claims about flow matching advantages over diffusion are presented without quantitative evidence or specific benchmark comparisons. The manuscript does not provide concrete numbers for sampling step reductions or quality metrics (e.g., scRMSD, designability) that would substantiate these comparative claims. Additionally, the statement that FrameFlow maintains generation quality is not supported by specific evaluation results.
- **Why it matters** These are empirical claims about method performance that require quantitative substantiation. Without specific numbers or benchmark comparisons, readers cannot assess the validity of the stated advantages, and the survey risks propagating unverified claims.
- **Resolution test** Provide specific quantitative comparisons from published benchmarks (e.g., sampling steps required, scRMSD distributions, designability scores) for the methods discussed. Alternatively, soften claims to reflect qualitative trends rather than definitive advantages.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The manuscript states that "evaluation cannot rely solely on AlphaFold2-based self-consistency checks" and that "comprehensive assessment requires diverse metrics (PoseBusters, PLINDER benchmarks) and ultimately experimental validation."
- **Evidence pointer** Section VIII, location not provided
- **Concern** While the claim about evaluation limitations is reasonable, the manuscript does not provide a critical analysis of when and why self-consistency checks fail. The discussion of evaluation standards is largely descriptive rather than analytical. The manuscript does not address known limitations of specific metrics (e.g., scRMSD thresholds, PoseBusters failure modes) or discuss how metric choice affects conclusions about method performance.
- **Why it matters** The stated goal of the survey is to synthesize evaluation best practices. A purely descriptive account does not help readers understand the trade-offs between different evaluation approaches or how to interpret conflicting results from different metrics.
- **Resolution test** Add a critical subsection analyzing specific failure modes of common evaluation metrics, with examples from the literature where self-consistency checks gave misleading results. Discuss how different metrics capture different aspects of design quality and when each is most appropriate.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interdisciplinary readership
- **Claim pointer** The manuscript claims to provide "a unified, task-spanning view of generative AI in protein research" and to be accessible to newcomers.
- **Evidence pointer** Sections II-III, location not provided
- **Concern** The technical depth varies considerably across sections. Some concepts (e.g., SE(3)-equivariance, flow matching on Riemannian manifolds) are introduced with minimal explanation, while others (e.g., masked language modeling) receive more detailed treatment. The notation table (Table I) is referenced but not provided, making it difficult to assess whether notation is consistently defined. The manuscript would benefit from more consistent pedagogical scaffolding.
- **Why it matters** The stated audience includes newcomers to the field. Inconsistent technical depth may leave some readers unable to follow key sections, undermining the survey's utility as an entry point.
- **Resolution test** Review each section for accessibility, adding brief intuitive explanations for advanced concepts. Ensure that all notation is defined at first use and that the notation table is included.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Section I-B, paragraph on paradigm shift
- **Evidence pointer** Section I-B, location not provided
- **Issue** The four "key developments" driving the paradigm shift are listed but not elaborated with specific examples or dates, making the historical narrative somewhat abstract.
- **Required correction** Add specific examples or citations for each development (e.g., AlphaFold2 for structure prediction, ESM-2 for protein language models) to ground the narrative.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section III-A, diffusion models
- **Evidence pointer** Section III-A, location not provided
- **Issue** The description of the DDPM forward process and training objective is incomplete. The equation for the training loss is referenced but not shown, and the distinction between predicting noise versus predicting the clean signal is not clearly explained.
- **Required correction** Include the training objective equation and briefly explain the noise prediction versus data prediction formulation.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Section V-C, motif scaffolding
- **Evidence pointer** Section V-C, location not provided
- **Issue** The discussion of RFdiffusion's motif scaffolding capability would benefit from more detail on how conditioning is implemented and what specific challenges remain in this task.
- **Required correction** Add a brief description of the conditioning mechanism and mention specific open challenges in motif scaffolding.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Section VII, protein-ligand interactions
- **Evidence pointer** Section VII, location not provided
- **Issue** The distinction between "ligand" and "drug" is made, but the practical implications of this distinction for model design and evaluation are not discussed.
- **Required correction** Briefly explain why this distinction matters for modeling choices and evaluation metrics.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section IX-D, model limitations
- **Evidence pointer** Section IX-D, location not provided
- **Issue** The discussion of computational costs mentions energy consumption and carbon emissions but does not provide any quantitative estimates or comparisons across model types.
- **Required correction** Add approximate training costs or energy consumption figures for representative models to give readers a sense of scale.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Section X-A, open challenges
- **Evidence pointer** Section X-A, location not provided
- **Issue** The open challenges are listed but not prioritized or connected to specific research opportunities. The discussion of conformational dynamics and IDPs is brief given the importance of these topics.
- **Required correction** Expand the discussion of conformational dynamics and IDPs, and consider prioritizing challenges based on potential impact.

## Risk / unsupported claims
- Claims about flow matching advantages over diffusion (fewer sampling steps, maintained quality) lack quantitative support
- Statements about specific model performance (e.g., SurfCoat 68.4% success rate) are presented without verification against the cited source
- The claim that "self-distillation from AlphaFold predictions provides a scalable source of synthetic structural data" is presented as established fact without discussing known limitations or failure modes
- The assertion that "federated learning offers a promising solution" for aggregating sensitive protein data is speculative and not supported by concrete examples in the protein domain
- The statement that "knowledge distillation and quantization are adopted as a result" of computational challenges implies a causal relationship that is not established
- The claim that "LoRA-tuned models are highly competitive with full fine-tuning" is presented without specific benchmark comparisons
- The discussion of biosecurity risks references "researchers have already demonstrated" capabilities without providing specific examples or citations
- The manuscript's claim to provide "evaluation best practices" is weakened by the lack of critical analysis of metric limitations
- Several references to "recent benchmarks" and "state-of-the-art" results lack specific citations or quantitative details