## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract, with no access to methods, figures, tables, or supplemental information
- **Shared manuscript claim summary** The authors present Disobind, a sequence-based deep-learning method that predicts inter-protein contact maps and interface residues for intrinsically disordered regions (IDRs) and their binding partners. The method uses ProtT5 protein language model embeddings, does not require structures or multiple sequence alignments, and is claimed to outperform state-of-the-art interface predictors for IDRs, as well as AlphaFold-multimer and AlphaFold3 at multiple confidence cutoffs. Combining Disobind with AlphaFold-multimer is reported to further improve performance.
- **Visible evidence base** Abstract text only. No quantitative results, benchmark datasets, evaluation metrics, or methodological details are provided in the supplied material.
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, benchmark definitions, statistical analyses, and supplemental information. The absence of these materials severely limits the ability to evaluate the validity of the performance claims.

## Reviewer
- **Overall assessment** The abstract describes a potentially useful tool for predicting IDR-mediated interactions, a topic of growing importance in structural biology. The conceptual advance of being partner-dependent and sequence-only is appealing. However, the abstract alone provides no quantitative evidence, no benchmark details, and no methodological specifics. The central performance claims, particularly the comparison with AlphaFold-multimer and AlphaFold3, cannot be assessed from the supplied material. The manuscript may have merit, but the case is not established from the abstract alone.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins and their interaction networks, computational biologists developing or using interface prediction tools, and experimentalists seeking to prioritize IDR binding sites for mutagenesis or structural characterization. The method's potential to localize IDRs in large assemblies could also interest those working on biomolecular condensates and signaling complexes.
- **Major strengths** The problem addressed is relevant and technically challenging. The proposed approach, using partner context and sequence embeddings without requiring structures or MSAs, is a sensible design choice that could offer practical advantages over structure-dependent methods. The claim of complementary performance with AlphaFold-multimer is interesting and, if substantiated, could provide a useful combined workflow.
- **Major Concerns**  
  - **Concern ID** R1-M1  
  - **Severity** Major  
  - **Blocking** Yes  
  - **Axis** Evidence sufficiency  
  - **Claim pointer** "Disobind outperforms state-of-the-art interface predictors for IDRs. It also outperforms AlphaFold-multimer and AlphaFold3 at multiple confidence cutoffs."  
  - **Evidence pointer** Abstract only, location not provided  
  - **Concern** The abstract makes strong comparative performance claims but provides no numerical results, no benchmark datasets, no evaluation metrics, and no statistical significance testing. Without these, the claims are unverifiable.  
  - **Why it matters** Comparative claims against established methods such as AlphaFold-multimer and AlphaFold3 require rigorous benchmarking on standardized datasets with appropriate metrics and error bars. The absence of any quantitative support means the central contribution of the paper cannot be evaluated.  
  - **Resolution test** Provide benchmark results with clear metrics (e.g., precision, recall, AUC, F1) on defined test sets, including comparisons with baseline methods and statistical significance tests.  
  - **Concern ID** R1-M2  
  - **Severity** Major  
  - **Blocking** Yes  
  - **Axis** Methodological transparency  
  - **Claim pointer** "It uses sequence embeddings from the ProtT5 protein language model."  
  - **Evidence pointer** Abstract only, location not provided  
  - **Concern** The abstract does not describe the network architecture, training data, loss functions, or how partner context is incorporated. Without this information, the method cannot be reproduced or assessed for potential biases or limitations.  
  - **Why it matters** Reproducibility is a core requirement for computational methods. The lack of methodological detail prevents readers from understanding what the method actually does and whether the design is sound.  
  - **Resolution test** Provide a full methods section with architecture details, training and validation data descriptions, hyperparameters, and code availability.  
  - **Concern ID** R1-M3  
  - **Severity** Major  
  - **Blocking** Yes  
  - **Axis** Generalizability and scope  
  - **Claim pointer** "Its predictions can be used to localize IDRs in large assemblies and characterize IDR-mediated interactions."  
  - **Evidence pointer** Abstract only, location not provided  
  - **Concern** The abstract claims broad applicability to large assemblies, but no evidence is presented that the method scales to such systems or that its accuracy holds in that context.  
  - **Why it matters** The utility claim extends beyond the core prediction task. If the method fails on larger or more complex systems, the stated applications would be misleading.  
  - **Resolution test** Provide case studies or benchmarks on large assemblies, with clear definitions of what constitutes a large assembly and quantitative assessment of performance in those settings.

- **Minor Comments**  
  - **Concern ID** R1-m1  
  - **Severity** Minor  
  - **Axis** Clarity  
  - **Affected element** Definition of "partner-dependent"  
  - **Evidence pointer** Abstract, location not provided  
  - **Issue** The abstract states the method is partner-dependent but does not clarify how this differs from standard pairwise interaction predictors or what specific advantage this provides.  
  - **Required correction** Define partner-dependence explicitly and explain how it improves over independent per-protein predictions.  
  - **Concern ID** R1-m2  
  - **Severity** Minor  
  - **Axis** Completeness  
  - **Affected element** Benchmark description  
  - **Evidence pointer** Abstract, location not provided  
  - **Issue** The abstract mentions "multiple confidence cutoffs" but does not specify which cutoffs were used or how they were chosen.  
  - **Required correction** Specify the confidence cutoffs and justify their selection in the methods or results.  
  - **Concern ID** R1-m3  
  - **Severity** Minor  
  - **Axis** Terminology  
  - **Affected element** "Fully-disordered binding"  
  - **Evidence pointer** Abstract, location not provided  
  - **Issue** This term is used without definition, and it is unclear whether it refers to a specific binding mode or a general category.  
  - **Required correction** Define the term or use more standard terminology from the IDP literature.

- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3. The absence of quantitative benchmarking, methodological detail, and evidence for the stated applications means the core claims are currently unsupported.

- **Assessment against Nature-style criteria**  
  - **Originality** The idea of a partner-dependent, sequence-only predictor for IDR interfaces is a reasonable incremental advance over existing methods, but the abstract does not demonstrate conceptual novelty beyond combining known components (ProtT5 embeddings, deep learning, pairwise prediction).  
  - **Scientific importance** The problem is important, and a reliable IDR interface predictor would be valuable. However, the abstract does not show that the method addresses a limitation that cannot be handled by existing tools.  
  - **Interdisciplinary readership** The topic is relevant to structural biology, computational biology, and biochemistry. The abstract is written in accessible language, but the lack of quantitative results limits its appeal to a broad audience.  
  - **Technical soundness** Cannot be assessed from the abstract. The design choices are plausible, but no evidence is provided to support their validity.  
  - **Readability for nonspecialists** The abstract is clear and well-structured, but the absence of results makes it difficult for nonspecialists to gauge the significance of the work.

- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a plausible approach and interesting claims, but without the full manuscript, methods, and benchmark results, the case for the method's utility and superiority is not made. A supportive assessment would require access to the complete manuscript and verification of the performance claims.

## Risk / unsupported claims
- The claim that Disobind outperforms state-of-the-art interface predictors for IDRs is unsupported by any quantitative data in the supplied material.
- The claim that Disobind outperforms AlphaFold-multimer and AlphaFold3 at multiple confidence cutoffs is unsupported and cannot be evaluated without benchmark details.
- The claim that combining Disobind and AlphaFold-multimer improves performance is unsupported.
- The claim that predictions can be used to localize IDRs in large assemblies is unsupported by any demonstration or case study.
- The generalizability of the method to diverse IDR binding modes, as implied by the introduction, is not evidenced in the abstract.