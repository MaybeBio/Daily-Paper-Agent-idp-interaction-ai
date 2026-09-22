## Review setup
- **Input scope** Full manuscript text (preprint v2, arXiv:2512.15930v2), including abstract, introduction, related work, architecture description, evaluation, scaling/performance sections, and references list. Figures and tables referenced but not provided.
- **Assessment boundary** Scientific and technical soundness of the claims as presented in the text; architectural design logic; evidence quality for the stated biological and computational results; alignment with stated venue scope (PASC '26). No assessment of code availability, reproducibility artifacts, or experimental validation beyond what is described.
- **Shared manuscript claim summary** The authors present StructBioReasoner, a multi-agent system for designing peptide/protein binders targeting intrinsically disordered proteins (IDPs). The system integrates retrieval-augmented generation, structure prediction, molecular dynamics, and free energy analysis within a tournament-based reasoning framework, orchestrated on HPC resources via the Academy middleware. Claims include: (1) over 50% of 787 validated Der f 21 binders outperform a literature reference binder in binding free energy; (2) identification of three binding modes for NMNAT-2 from 97,066 candidates, including the known NMNAT2:p53 interface; (3) scalable performance on the Aurora supercomputer with 80.4% parallel efficiency for MD at 256 nodes and 84.4% for binder design at 256 nodes.
- **Missing materials affecting confidence** Figures 1-5 are referenced but not included. No structural data, binding assay results, or experimental validation are provided. The NMNAT-2 "binding modes" are not defined or characterized. No comparison against non-agentic baselines or human expert workflows is quantified. No statistical analysis of the free energy distributions is presented. The relationship between MM-PBSA values and actual binding affinity is not calibrated or validated.

## Reviewer

- **Overall assessment** The manuscript describes an ambitious and timely integration of multi-agent AI reasoning with HPC-enabled structural biology workflows, targeting a genuinely important problem class (IDP biologics design). The architectural vision is coherent, and the use of a tournament-based framework for parallel hypothesis generation and evaluation is a reasonable design choice. However, the evidence presented is almost entirely computational and in silico, with no experimental validation, no clear definition of what constitutes a "binding mode," and no quantitative comparison against non-agentic baselines. The scaling results are presented for individual components rather than the integrated system, and the claimed biological outcomes rest on MM-PBSA approximations that are known to be unreliable for ranking binders. The manuscript is better positioned as a systems/architecture paper than a biological discovery paper, but even on those terms, the evaluation is incomplete. The core claims of biological utility are not established from the provided evidence.
- **Who would be interested in the results, and why** Researchers in computational biology, AI for science, and HPC systems who are interested in autonomous scientific workflows, multi-agent orchestration, and the application of LLM-driven reasoning to protein design. The paper may also interest structural biologists working on IDPs who are seeking computational tools to navigate conformational ensembles. The HPC community, particularly those involved in exascale software development, may find the Academy integration and scaling analysis relevant. However, the lack of experimental validation will limit interest from the drug discovery community.
- **Major strengths** (1) The problem is well-motivated and significant: IDPs are underexplored therapeutic targets, and the conformational complexity argument is compelling. (2) The system architecture is thoughtfully designed, with clear separation of concerns across agents and a sensible integration of literature retrieval, structure prediction, MD, and free energy analysis. (3) The use of a tournament framework for parallel hypothesis evaluation is a novel and appropriate mechanism for this problem class. (4) The scaling analysis, while limited, addresses a real gap in the literature on agentic systems for HPC. (5) The authors are transparent about the I/O bottlenecks and the need for future optimization.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality for biological claims
- **Claim pointer** "over 50% of 787 designed and validated candidates for Der f 21 outperformed the human-designed reference binders from literature, in terms of improved binding free energy"
- **Evidence pointer** Section 4.1, Figure 3 (not provided)
- **Concern** The central biological claim rests entirely on MM-PBSA free energy calculations. MM-PBSA is a well-known approximation with documented poor correlation with experimental binding affinities, particularly for ranking closely related binders. The manuscript provides no calibration of MM-PBSA values against experimental data for these specific systems, no error analysis beyond standard deviation, and no discussion of the known limitations of this method for IDP systems, where conformational entropy contributions are expected to be large and are poorly captured by MM-PBSA. The threshold for "more favorable" (1 standard deviation below -145.25 kcal/mol) is arbitrary and not justified. Without experimental validation (e.g., surface plasmon resonance, isothermal titration calorimetry) or at minimum a rigorous benchmarking against known binders with measured affinities, this claim is not supported.
- **Why it matters** The stated value proposition of the system is its ability to design better binders. If the primary metric for "better" is an unreliable computational proxy, the entire biological contribution is called into question. The reader cannot distinguish between genuine design improvement and artifacts of the scoring function.
- **Resolution test** Provide experimental binding affinity measurements for a representative subset of the designed binders (e.g., 10-20 candidates spanning the predicted range) and demonstrate correlation with MM-PBSA predictions. Alternatively, benchmark the MM-PBSA protocol against a set of known IDP-binder complexes with experimentally determined affinities and show that the method can rank them correctly.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Definition and characterization of results
- **Claim pointer** "we identified three binding modes from 97,066 binders, including the well-studied NMNAT2:p53 interface"
- **Evidence pointer** Section 4.2, Figure 4 (not provided)
- **Concern** The term "binding mode" is never defined. Does it refer to distinct structural conformations of the binder-NMNAT-2 complex? Different interaction interfaces? Different energetic signatures? The manuscript states that 97,066 binders passed quality control, but it is unclear how these were clustered into three modes, what criteria were used, and how the NMNAT2:p53 interface was recognized as one of them. The claim that the system "identified" this interface is also ambiguous: was this a de novo discovery, or was the p53 interaction already known from the literature retrieved by HiP-RAG? If the latter, the novelty of the identification is substantially reduced. The figure is not provided, so the reader cannot assess the structural basis of the claim.
- **Why it matters** The NMNAT-2 case study is presented as a demonstration of the system's ability to navigate a complex interactome and identify therapeutically relevant targets. Without a clear definition of binding modes and a transparent clustering methodology, the result is not interpretable or reproducible. The distinction between rediscovery of known interactions and novel prediction is critical for assessing the system's scientific value.
- **Resolution test** Define "binding mode" operationally. Provide the clustering algorithm, similarity metric, and thresholds used. Show the structural representatives of each mode. Clarify whether the p53 interaction was known a priori from the literature and whether the system's identification was independent of that knowledge.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Comparative evaluation against baselines
- **Claim pointer** "StructBioReasoner lays the groundwork for agentic reasoning systems for IDP therapeutic discovery" and the implicit claim that the agentic approach adds value over existing workflows
- **Evidence pointer** Sections 4.1, 4.2, 5
- **Concern** The manuscript provides no comparison against non-agentic baselines. For Der f 21, the reference is a single binder from prior work, but there is no comparison against, for example, running the same binder design tools (BindCraft, RFDiffusion) without the agentic reasoning layer, or against a simple grid search or random sampling strategy. For NMNAT-2, there is no baseline at all. The reader cannot determine whether the tournament-based reasoning framework actually improves design outcomes, or whether the same results could be achieved by brute-force sampling with the same underlying tools. The scaling analysis in Section 5 measures throughput of individual components but does not measure end-to-end time-to-solution for a design campaign, nor does it compare against a non-agentic orchestration of the same tools.
- **Why it matters** The core contribution is the agentic reasoning layer. Without a demonstration that this layer adds value over simpler approaches, the manuscript does not establish its central thesis. The computational overhead of the reasoning layer (LLM calls, state management, inter-agent communication) must be justified by improved outcomes or reduced human effort, neither of which is quantified.
- **Resolution test** Run the same design tasks with the agentic layer disabled (e.g., random or round-robin tool selection) and compare the distribution of resulting binding free energies, the number of candidates needed to achieve a given threshold, and the wall-clock time. Provide at least one such comparison for each benchmark system.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Statistical rigor of reported results
- **Claim pointer** "50.98% success rate" and "over 50% of 787 designed and validated candidates outperformed the reference"
- **Evidence pointer** Section 4.1, Figure 3 (not provided)
- **Concern** The success rate is reported as a single percentage with no confidence interval, no description of the underlying distribution, and no sensitivity analysis. The threshold for success is defined relative to a single reference binder's mean free energy minus one standard deviation, which is itself a noisy quantity. It is unclear how many independent design runs were performed, whether the 787 candidates are independent or correlated (e.g., derived from shared intermediates), and how sensitive the success rate is to the choice of threshold. The MM-PBSA values are reported as mean ± standard deviation, but the number of replicate simulations per candidate is not stated.
- **Why it matters** The reported success rate is a headline result. If it is not statistically robust, the conclusion that the system "outperforms" the reference is not reliable. The reader needs to know the uncertainty in the 50.98% figure to assess whether it is meaningfully different from, say, 40% or 60%.
- **Resolution test** Report the number of independent design runs, the distribution of free energy values across all candidates, and a bootstrap confidence interval for the success rate. Show how the success rate varies as a function of the threshold (e.g., 0.5, 1, 1.5, 2 standard deviations below the reference mean).

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability and scope of validation
- **Claim pointer** "StructBioReasoner lays the groundwork for agentic reasoning systems for IDP therapeutic discovery on Exascale platforms"
- **Evidence pointer** Sections 4, 5, 6
- **Concern** The system is validated on only two targets, both of which are relatively small proteins. Der f 21 is described as "compact" and NMNAT-2, while larger, is still a single-domain protein. The manuscript does not address how the system would perform on larger, multi-domain IDPs, on IDPs with multiple known interaction partners requiring selectivity, or on targets where the conformational ensemble is exceptionally broad. The scaling analysis is performed on individual components (MD, binder design) rather than on the full agentic loop, so the end-to-end scalability of the reasoning layer itself is not demonstrated. The claim about "Exascale platforms" is aspirational rather than demonstrated.
- **Why it matters** The stated goal is to enable IDP therapeutic discovery at scale. If the system only works on small, well-behaved targets, its practical utility is limited. The reader needs to understand the boundaries of the approach and where it is likely to fail.
- **Resolution test** Add at least one additional benchmark on a larger, more challenging IDP target with a well-characterized conformational ensemble. Provide a qualitative or quantitative analysis of the expected failure modes as target size and complexity increase.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** Section 3, "tournament-based reasoning framework"
- **Evidence pointer** Section 3, Figure 1 (not provided)
- **Issue** The term "tournament" is used to describe the reasoning framework, but the mechanics of the tournament are not described. How are agents paired or compared? What is the elimination or scoring criterion? Is it a single-elimination or round-robin structure? The reader is left to infer the meaning.
- **Required correction** Provide a formal description of the tournament structure, including how hypotheses are paired, scored, and advanced or eliminated across rounds.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility of the literature retrieval
- **Affected element** Section 3.2, HiP-RAG agent
- **Evidence pointer** Section 3.2, Figure 2 (not provided)
- **Issue** The corpus construction is described as using an "automated pipeline" integrating Europe PMC, OpenAlex, Crossref, and Unpaywall, with deduplication by DOI/PMCID. However, the specific query terms, date ranges, inclusion/exclusion criteria, and the final corpus composition (beyond counts of 1,520 and 38 papers) are not provided. The retrieval quality is not evaluated.
- **Required correction** Provide the full search strategy, including query strings and filters. Report the precision of the retrieval (e.g., fraction of retrieved papers that were relevant) and describe any manual curation steps.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical detail on MM-PBSA protocol
- **Affected element** Section 3.6, Free Energy Agent
- **Evidence pointer** Section 3.6
- **Issue** The MM-PBSA protocol is described only as "an in-house Python-based workflow." No details are given on the force field parameters, solvation model, dielectric constants, entropy contributions (if any), or the number of frames used for averaging. The choice of MM-PBSA over more rigorous methods (e.g., FEP, TI) is not justified.
- **Required correction** Provide a complete description of the MM-PBSA protocol, including all parameters and settings. Justify the choice of MM-PBSA for this application and discuss its known limitations in the context of IDP binding.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation of scaling results
- **Affected element** Section 5, Figures 5A-C (not provided)
- **Evidence pointer** Section 5
- **Issue** The scaling analysis reports efficiency relative to a 64-node baseline, which is unusual. The choice of 64 nodes as the baseline is justified by "stability and reproducibility," but the reader cannot assess the absolute performance without knowing the single-node throughput. The strong scaling behavior (fixed problem size, increasing nodes) is not reported, only weak scaling.
- **Required correction** Report single-node throughput for each agent. Add strong scaling results or explain why they are not applicable. Show the raw throughput values alongside the efficiency percentages.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Related work coverage
- **Affected element** Section 2
- **Evidence pointer** Section 2
- **Issue** The related work section is brief and does not engage deeply with recent advances in agentic scientific discovery (e.g., ChemCrow, Coscientist are mentioned but not critically compared) or with the growing literature on ML-based IDP binder design beyond the cited diffusion models. The discussion of HPC for biological AI focuses on throughput benchmarks but does not address challenges such as data movement, checkpointing, or fault tolerance in agentic workflows.
- **Required correction** Expand the related work to include a more critical comparison with existing agentic frameworks and a discussion of how StructBioReasoner differs. Add a paragraph on the specific HPC challenges posed by agentic (as opposed to single-workflow) execution.

- **Technical failings that need to be addressed before the case is established** (1) The absence of any experimental validation for the designed binders is the most significant gap. The manuscript claims "designing biologics" but provides no evidence that any designed molecule binds its target in vitro or in vivo. (2) The MM-PBSA-based success metric is not validated or calibrated. (3) No baseline comparison against non-agentic approaches is provided. (4) The NMNAT-2 "binding modes" are undefined and the clustering methodology is not described. (5) The scaling analysis does not cover the end-to-end agentic loop. (6) The relationship between the computational predictions and the biological relevance of the targets (e.g., the disease association of the specific NMNAT-2 interfaces) is asserted but not developed.
- **Assessment against Nature-style criteria** Originality: Moderate. The combination of multi-agent reasoning with HPC for IDP binder design is novel, but the individual components (RAG, diffusion-based design, MM-PBSA, tournament-based selection) are all established. The originality lies in the integration, not in any single methodological advance. Scientific importance: Potentially high, if the system can be shown to produce experimentally validated binders for challenging IDP targets. As presented, the importance is not demonstrated because the biological claims are unvalidated. Interdisciplinary readership: The topic sits at the intersection of AI, structural biology, and HPC, which is a broad and growing community. However, the manuscript assumes significant familiarity with all three fields, and the lack of experimental validation will limit its appeal to biologists. Technical soundness: The architecture is reasonable, but the evaluation is incomplete. The scaling analysis is component-level rather than system-level, and the biological evaluation relies on an unvalidated computational proxy. Readability for nonspecialists: The manuscript is clearly written but dense. The abstract and introduction are accessible, but the architecture and evaluation sections require specialist knowledge. The absence of figures in the provided material makes it difficult to assess the clarity of the presentation.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript presents a plausible and potentially valuable system architecture, but the central claims of biological utility and system-level scalability are not supported by the evidence provided. The authors should be encouraged to resubmit with experimental validation, baseline comparisons, and a more rigorous statistical treatment of their results. If the authors can provide even a small number of experimentally confirmed binders, or a compelling demonstration that the agentic layer outperforms non-agentic baselines on a meaningful metric, the case would be substantially strengthened.

## Risk / unsupported claims
- The claim that "over 50% of 787 designed and validated candidates outperformed the human-designed reference binder" is unsupported because the metric (MM-PBSA free energy) is not validated against experimental data and the statistical significance of the comparison is not established.
- The claim that "three binding modes" were identified for NMNAT-2 is unsupported because "binding mode" is not defined and the methodology for clustering 97,066 candidates into three modes is not described.
- The claim that the system "identified" the NMNAT2:p53 interface is ambiguous and potentially misleading if this interaction was already known from the literature retrieved by HiP-RAG.
- The claim that the framework "lays the groundwork for agentic reasoning systems for IDP therapeutic discovery on Exascale platforms" is aspirational and not supported by the scaling analysis, which covers individual components rather than the integrated system.
- The statement that "approximately 80% of cancer-related proteins contain long disordered regions" is cited but the citation is not verifiable from the provided material.
- The claim that the system "autonomously identified E7 as a key interaction residue" is not supported by a clear description of how this identification was made and distinguished from the literature knowledge already present in the system.
- The overall framing that the system can "design biologics" is not supported by any experimental evidence that the designed molecules are functional binders.