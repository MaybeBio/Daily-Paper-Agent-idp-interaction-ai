## Review setup
- **Input scope** Full manuscript text (preprint, arXiv:2603.14806v1)
- **Assessment boundary** Technical soundness, scientific claims, and reproducibility of the proposed framework as described in the provided text; no code execution or benchmark replication performed
- **Shared manuscript claim summary** The authors present Fold-CP, a context parallelism framework for biomolecular structure prediction models (using Boltz as reference architecture), claiming: (1) memory scaling of O(N²/P) per device for N-token inputs across P GPUs; (2) exact numerical equivalence to serial implementations for all distributed operations; (3) ability to predict structures exceeding 30,000 residues on 64 NVIDIA B300 GPUs; (4) scientific utility demonstrated via case studies including PI4KA complex folding, COR database coverage, and partner deployments.
- **Visible evidence base** Full text including architecture description (Sections 2–3), scaling benchmarks (Section 4.1), accuracy benchmarks (Section 4.2), and case studies (Section 5); figures referenced but not viewable; tables referenced but not viewable
- **Missing materials affecting confidence** Figures 1–10, Table 1–2, code repository contents, benchmark datasets, hyperparameters, hardware configuration details, baseline comparison data, statistical significance measures, and the actual Boltz-1/Boltz-2 model weights or configurations

## Reviewer

- **Overall assessment** The manuscript presents a substantial systems engineering contribution addressing a real bottleneck in biomolecular structure prediction. The core idea of multi-dimensional sharding across a square GPU grid, combined with custom autograd primitives to avoid materializing global tensors, is technically sound and well-motivated. However, the manuscript currently reads more like a technical report or white paper than a Nature-caliber research article. The evidence base is largely qualitative or presented through partner testimonials rather than rigorous, reproducible benchmarks. The central claims of numerical equivalence and scaling efficiency require substantially more rigorous validation, including comparison against strong baselines, ablation studies, and independent replication. The scientific novelty is incremental (adapting known parallelism techniques to a specific domain) rather than transformative. The manuscript would be more suitable for a systems or machine learning venue, or as a shorter technical contribution, unless the authors substantially strengthen the evidence and reframe the scientific contribution.

- **Who would be interested in the results, and why** Computational structural biologists and machine learning practitioners working on protein structure prediction would find this work relevant, as it directly addresses the memory bottleneck that limits the application of AlphaFold-style models to large assemblies. Systems researchers interested in distributed training and inference of large models may also find the 2D sharding and custom autograd techniques of interest. However, the audience within the Nature readership is likely narrow, and the work would be of greater interest to the specialized communities at venues like ICML, NeurIPS, or SC.

- **Major strengths**
  1. The problem is well-defined and practically important: the memory ceiling of AlphaFold-style models is a genuine limitation for studying large biomolecular assemblies.
  2. The technical approach is coherent and well-architected: the 2D grid sharding, the custom autograd imperative, and the ring-based algorithms are described with sufficient detail to be understood and potentially reproduced.
  3. The inclusion of multiple case studies with external partners (Rezo, Proxima, Earendil) demonstrates real-world applicability and provides some evidence of utility beyond synthetic benchmarks.
  4. The authors are transparent about limitations (square topology constraint, current lack of generic grid support, data scarcity for large complexes), which is commendable.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "Our approach achieves efficient memory scaling; for an N-token input distributed across P GPUs, per-device memory scales as O(N²/P), enabling the structure prediction of assemblies exceeding 30,000 residues on 64 NVIDIA B300 GPUs."
- **Evidence pointer** Section 4.1, Figure 3, Table 2
- **Concern** The central scaling claim is presented with minimal quantitative detail. The text states that "maximum context length scales with the square root of the number of GPUs" and provides approximate token counts per GPU count, but no raw data points, no error bars, no comparison to theoretical limits, and no discussion of variance across runs are provided. The referenced Figure 3 and Table 2 are not viewable in the provided material, making it impossible to assess the quality of the evidence. Furthermore, the claim of "linear scaling with the square root of the number of GPUs" is presented as a success, but this is a sublinear scaling that should be contextualized against what is theoretically achievable and what competing methods achieve.
- **Why it matters** The scaling claim is the central technical contribution of the paper. Without rigorous, reproducible benchmark data, the claim cannot be verified, and the reader cannot assess whether the observed scaling is a genuine property of the method or an artifact of specific hardware, model configuration, or measurement methodology.
- **Resolution test** Provide raw data points for memory usage and maximum context length at each GPU count, including multiple runs with variance measures. Include a comparison against at least one strong baseline (e.g., ZeRO-style offloading, sequence sharding, or the best available alternative). Show that the scaling holds across different model sizes and sequence compositions (e.g., protein-only vs. protein-nucleic acid complexes).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Numerical equivalence claim
- **Claim pointer** "This preserves exact equivalence to serial softmax without materializing the full N×N attention matrix on any rank." (Section 3.2); "ensuring numerical equivalence to the global softmax without ever materializing the full N×N weight matrix on any rank" (Section 3.4)
- **Evidence pointer** Section 3.2, Section 3.4, Section 4.2, Figure 4
- **Concern** The claim of "exact equivalence" to serial implementations is made repeatedly, but the evidence provided in Section 4.2 shows a Pearson correlation of R = 0.97 and a median lDDT difference of 0.0007 between DP and Fold-CP predictions. A correlation of 0.97 is not "exact equivalence"; it indicates small but measurable differences. The authors do not explain the source of these differences (e.g., floating-point non-associativity, different summation orders, or actual algorithmic differences). Moreover, the accuracy benchmark is only performed on the Boltz-1 test set, which may not include the large complexes that Fold-CP is designed for.
- **Why it matters** The claim of exact numerical equivalence is a strong statement that, if true, would be a significant advantage of the method. If the equivalence is only approximate, the authors must characterize the nature and magnitude of the deviations, particularly for very large complexes where accumulated numerical differences could become significant. The current evidence is insufficient to support the strong claim.
- **Resolution test** Provide a direct numerical comparison of intermediate tensors (e.g., attention weights, pair representations) between DP and Fold-CP implementations on identical inputs, reporting maximum and mean absolute differences. If exact equivalence is claimed, demonstrate bitwise equality or provide a rigorous error bound. If only approximate equivalence is achieved, characterize the error growth as a function of sequence length and GPU count.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific contribution and novelty
- **Claim pointer** "Fold-CP represents a significant step toward the realization of a virtual cell" (Abstract); "Fold-CP provides the computational engine to process extreme scales" (Section 6)
- **Evidence pointer** Abstract, Section 6
- **Concern** The manuscript frames the contribution as a significant step toward a "virtual cell," but the actual scientific advances demonstrated are: (1) a systems engineering solution for distributing existing models, and (2) case studies showing that existing models can be applied to larger complexes when memory constraints are removed. The case studies, while interesting, do not demonstrate new biological insights that could not, in principle, be obtained by other means (e.g., model distillation, coarse-graining, or incremental hardware improvements). The claim that Fold-CP "represents a significant step toward the realization of a virtual cell" is an overreach given the evidence presented.
- **Why it matters** For a Nature-caliber publication, the scientific contribution must go beyond incremental engineering. The authors need to articulate what fundamentally new biological or scientific questions can now be addressed with Fold-CP that were previously intractable, and ideally demonstrate at least one such application with a concrete finding.
- **Resolution test** Either (a) temper the claims to match the evidence, or (b) include a case study that demonstrates a genuinely new biological insight enabled by Fold-CP, with appropriate validation (e.g., experimental corroboration, comparison to known structures, or a testable prediction).

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility and completeness
- **Claim pointer** "A proof-of-concept implementation of Fold-CP on Boltz models is available at https://github.com/NVIDIA-Digital-Bio/boltz-cp"
- **Evidence pointer** Code Availability section
- **Concern** The manuscript references a code repository but provides no details on its contents, license, dependencies, or documentation. The benchmarks described in Section 4 are not accompanied by configuration files, model checkpoints, or evaluation scripts. The case studies in Section 5 reference partner-specific integrations that are not described in sufficient detail to be reproduced or even fully understood.
- **Why it matters** Reproducibility is a core requirement for scientific publication. Without access to the code, data, and configuration details, independent verification of the claims is impossible. The current level of detail is insufficient for a rigorous review.
- **Resolution test** Provide a detailed description of the repository contents, including version numbers, dependencies, and a clear guide for reproducing the main scaling and accuracy benchmarks. Include configuration files and, where possible, the exact commands used to generate the reported results.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Benchmark rigor and baselines
- **Claim pointer** "Fold-CP enables the scoring of over 90% of Comprehensive Resource of Mammalian protein complexes (CORUM) database" (Abstract); "reduced the inference walltime of large complexes by up to two orders of magnitude" (Section 5.3)
- **Evidence pointer** Section 5.2, Section 5.3
- **Concern** The case studies report impressive-sounding numbers (90% CORUM coverage, two orders of magnitude speedup) but provide no methodological detail on how these numbers were computed. What is the baseline for the speedup comparison? What constitutes "scoring" a complex? What is the accuracy of the predictions on these large complexes? The CORUM claim is particularly problematic: the abstract states "over 90% of CORUM" while Section 5.2 states "encompassing 93% of CORUM" — these are different numbers, and neither is accompanied by a clear definition of what "scoring" or "encompassing" means.
- **Why it matters** Quantitative claims without methodological context are not verifiable and can be misleading. The reader cannot assess whether these numbers represent genuine advances or are the result of favorable but arbitrary choices in evaluation methodology.
- **Resolution test** Provide precise definitions of all metrics used, describe the evaluation protocol in detail, and include a comparison against at least one alternative approach (e.g., chunked inference, model distillation, or a different parallelism strategy). For the CORUM claim, specify the exact number of complexes, the criteria for "scoring," and the distribution of complex sizes.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of contribution
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract, Section 1
- **Issue** The abstract and introduction do not clearly distinguish between the framework's contributions to (a) systems engineering, (b) algorithmic innovation, and (c) scientific application. The reader is left uncertain whether the primary contribution is the parallelism framework itself, the specific algorithms for triangular operations, or the demonstration of large-scale folding.
- **Required correction** Restructure the abstract and introduction to explicitly state the three levels of contribution and which aspects are novel versus adapted from prior work.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Section 3.7
- **Evidence pointer** Section 3.7, "Window Batching and Distributed Gather"
- **Issue** The description of the Toeplitz structure exploitation is too brief. The claim that the window batching indexing matrix has a "block-Toeplitz structure" is stated without proof or detailed explanation. The halo exchange size of "~48 atoms" is mentioned without justification.
- **Required correction** Provide a formal derivation of the Toeplitz structure, explain why the halo size is 48 atoms, and include a diagram or pseudocode to clarify the algorithm.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Hardware and performance context
- **Affected element** Section 4.1
- **Evidence pointer** Section 4.1, Figure 3
- **Issue** The scaling benchmarks are reported on NVIDIA B300 and H100 GPUs, but no details are provided on interconnect topology (e.g., NVLink domains, InfiniBand), GPU memory configuration, or power constraints. These factors significantly affect the observed scaling.
- **Required correction** Include a detailed description of the hardware environment, including interconnect topology, and discuss how the results might generalize to other hardware configurations.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Comparison with prior work
- **Affected element** Section 1.1
- **Evidence pointer** Section 1.1, "Related Work"
- **Issue** The related work section mentions FastFold, ScaleFold, and MegaFold but does not provide a quantitative comparison of Fold-CP against these methods. The claim that Fold-CP achieves O(N²/P) memory scaling "rather than O(N²/√P)" is presented as an advantage, but no empirical comparison is shown.
- **Required correction** Include a table comparing memory usage, throughput, and maximum context length of Fold-CP against at least one of the cited prior methods on the same hardware and model.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Section 4.2
- **Evidence pointer** Section 4.2, Figure 5
- **Issue** The training comparison between DP and Fold-CP is described as "closely mirrors" with no quantitative measure of similarity. The number of training steps (5.5k) is very small for a structure prediction model, and no convergence criteria are reported.
- **Required correction** Report quantitative metrics (e.g., final loss values, validation lDDT with confidence intervals) and extend the training comparison to a more meaningful number of steps.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology precision
- **Affected element** Section 2.2
- **Evidence pointer** Section 2.2, "The Square Topology Constraint"
- **Issue** The term "square topology" is used to describe the requirement that the number of GPUs be a perfect square. This is a reasonable term, but the authors do not discuss the practical implications of this constraint, such as how users with non-square GPU counts would be affected.
- **Required correction** Add a brief discussion of the practical implications of the square topology constraint and whether it can be relaxed in future work.

## Risk / unsupported claims
- The claim of "exact equivalence" to serial implementations is not supported by the evidence (Pearson R = 0.97 indicates measurable differences).
- The claim of "over 90% of CORUM" in the abstract versus "93% of CORUM" in Section 5.2 is inconsistent and lacks methodological definition.
- The claim of "two orders of magnitude" inference speedup in Section 5.3 lacks a defined baseline and experimental protocol.
- The claim that Fold-CP "represents a significant step toward the realization of a virtual cell" is an overreach not supported by the evidence presented.
- The scaling results in Section 4.1 are presented without raw data, error bars, or comparison to theoretical limits, making them unverifiable from the provided material.
- The accuracy benchmarks in Section 4.2 are limited to a truncated model and a short training duration, which may not be representative of full-scale performance.
- The case studies in Section 5 are described qualitatively and lack the methodological detail required for independent assessment.
- The claim that the window batching matrix has a "block-Toeplitz structure" is stated without formal proof or detailed explanation.