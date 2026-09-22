## Review setup
- **Input scope** Full manuscript text (abstract, introduction, related work, methodology, experiments, results, conclusion, references) as provided.
- **Assessment boundary** Scientific and technical soundness of the proposed method, validity of the experimental design and claims, and quality of presentation. No assessment of code availability, reproducibility scripts, or supplementary data beyond the provided text.
- **Shared manuscript claim summary** The authors propose D2MOE, a two-stage framework for protein intrinsic disorder prediction. Stage one extracts dual-view (evolutionary HMM profiles and ProtT5 semantic embeddings) multiscale features using CNNs and RNNs. Stage two uses a multi-objective evolutionary algorithm (NSGA-II) coupled with differential evolution to jointly select feature subsets and optimize continuous fusion weights. The authors claim consistent state-of-the-art performance across three benchmark datasets (CB513, TS115, CASP12) and demonstrate the superiority of each design component through ablations.
- **Visible evidence base** Figures 1-5, Tables I-V, Algorithm 1 and 2, and the associated text in Sections III-V. The manuscript text includes descriptions of results but the actual numerical values for many comparisons are only partially visible in the text (e.g., specific MCC/AUPR values for baselines are not all reported in the text body).
- **Missing materials affecting confidence** The full tables (Table II, III, IV, V) and figures (Fig. 2, 3, 4, 5) are referenced but their complete contents are not fully described in the provided text. Statistical significance testing is not reported. Details on the hyperparameter search space and the computational cost of the evolutionary search are not provided. The exact definition of the "best individual" selection criterion from the Pareto front is not fully specified.

## Reviewer

- **Overall assessment** The manuscript addresses a relevant problem in computational biology and proposes a technically elaborate solution that combines established components (HMM profiles, ProtT5 embeddings, CNNs, RNNs) with a sophisticated evolutionary optimization strategy for feature fusion. The motivation for adaptive fusion over manual rules is reasonable. However, the current evidence base is insufficient to fully support the central claims. The reported performance gains, while positive, appear modest in some cases and lack statistical validation. The manuscript would benefit from a clearer articulation of the novelty relative to existing multi-view/multiscale predictors and a more rigorous experimental analysis, including significance testing and a discussion of computational overhead. The writing is generally clear but some methodological details are underspecified.

- **Who would be interested in the results, and why** Researchers in the fields of protein bioinformatics, specifically those working on disorder prediction, protein function annotation, and the application of deep learning and evolutionary computation to biological sequence analysis. The work may also be of interest to method developers exploring automated neural architecture search or feature fusion strategies for other residue-level prediction tasks.

- **Major strengths**
    1.  The problem is well-motivated, and the limitations of existing single-view, fixed-fusion approaches are clearly articulated.
    2.  The proposed framework is technically sound and integrates several powerful, complementary ideas: dual-view representation, multiscale feature extraction, and multi-objective optimization for fusion.
    3.  The use of a multi-objective approach to balance accuracy and model compactness is a thoughtful design choice that addresses a practical concern in deploying such models.
    4.  The ablation study is well-structured, isolating the contributions of the dual-view design, multiscale features, and the MOEA components (including the DE-based weight optimization).
    5.  The paper is generally well-written and the methodology is described in sufficient detail to be reproducible, given the algorithms and architectural descriptions.

- **Major Concerns**

    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Experimental Rigor
    - **Claim pointer** "D2MOE consistently outperforms state-of-the-art methods" and "D2MOE consistently outperforms baselines across multiple evaluation metrics on three benchmark datasets."
    - **Evidence pointer** Section V-A, Figure 2, Section V-B, V-C, V-D, Tables II, III, IV
    - **Concern** The central claim of consistent superiority is not fully supported by the evidence presented. While the text states D2MOE ranks first in MCC and AUPR, the actual performance differences, particularly against strong baselines like NetSurfP-3.0, appear modest in some cases (e.g., on TS115, the text notes MCC and AUPR are 0.677 and 0.773, but the corresponding values for NetSurfP-3.0 are not provided in the text for direct comparison). More critically, no statistical significance testing (e.g., paired tests across dataset folds or multiple runs) is reported. Without this, it is impossible to determine if the observed improvements are meaningful or within the range of random variation.
    - **Why it matters** The primary contribution of the paper is a new method that claims to improve prediction performance. If the performance gains are not statistically robust, the core value proposition of the work is weakened. The lack of significance testing is a major omission for a methods paper in this field.
    - **Resolution test** The authors should provide a statistical analysis of their results. This could include running the experiments multiple times with different random seeds and reporting mean and standard deviation, or performing a paired statistical test (e.g., Wilcoxon signed-rank test) between D2MOE and the best-performing baseline for each metric and dataset. The paper should state whether the observed differences are statistically significant.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** No
    - **Axis** Methodological Novelty and Clarity
    - **Claim pointer** "a multi-objective evolutionary algorithm is designed to adaptively discover optimal fusion architectures" and "co-evolving discrete feature selection and continuous fusion weights".
    - **Evidence pointer** Section III-B, Algorithm 2
    - **Concern** The novelty of the evolutionary approach is not clearly differentiated from existing work. The authors state that evolutionary algorithms have been used for feature selection in other domains, but the specific challenges and adaptations for this protein sequence problem are not deeply analyzed. For instance, the search space of possible fusion architectures (defined by the sequence of operators and features) is not characterized. What is the size of this space? How does the NSGA-II algorithm's performance (e.g., convergence, diversity of solutions) compare to a simpler random search or a greedy approach? The paper does not provide a baseline for the search algorithm itself.
    - **Why it matters** The paper's contribution is framed as a novel fusion of deep learning and evolutionary algorithms. To establish this, it is necessary to show that the evolutionary search is not just an over-engineered solution that could be replaced by a simpler heuristic. A comparison against a random search or a simple greedy feature selection algorithm would help to demonstrate the value of the MOEA.
    - **Resolution test** The authors should add a baseline experiment where the fusion architecture is selected by a simpler method, such as a random search with the same computational budget, or a greedy forward selection of features. This would help to isolate the contribution of the MOEA's search strategy. Additionally, a brief analysis of the search space and the algorithm's convergence would strengthen the methodological contribution.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical Soundness and Reproducibility
    - **Claim pointer** "the algorithm adaptively explores optimal cross-feature architectures to enhance predictive accuracy while maintaining model compactness."
    - **Evidence pointer** Section III-B, Algorithm 2, Section IV-B
    - **Concern** The computational cost of the proposed method is not discussed. The evolutionary algorithm requires training and evaluating numerous candidate fusion models (each involving a fully connected layer on top of the extracted features) over many generations. The paper does not report the total training time, the number of generations required for convergence, or the computational resources used. This is a significant omission, as the practical utility of the method depends on its computational feasibility. Furthermore, the hyperparameters for the MOEA (population size, mutation rate, crossover rate, etc.) are not listed in Table I, which is stated to summarize key hyperparameters.
    - **Why it matters** A method that is computationally prohibitive is unlikely to be adopted by the community. The lack of information on computational cost and MOEA hyperparameters hinders reproducibility and makes it difficult for other researchers to apply the method to larger datasets or other problems.
    - **Resolution test** The authors should report the total training time (including the evolutionary search) and the inference time. They should also provide the full set of hyperparameters for the MOEA in Table I or in the text. A discussion of the computational trade-offs compared to simpler fusion methods would be valuable.

- **Minor Comments**

    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity and Presentation
    - **Affected element** Section V-A, Figure 2
    - **Evidence pointer** Figure 2 (a-c)
    - **Issue** The text describes results on three datasets but the figure panels are not explicitly referenced in the text (e.g., "Fig. 2a" is not used). The caption for Figure 2 is not provided in the text, making it difficult to interpret the panels.
    - **Required correction** Explicitly reference each panel in the text (e.g., "As shown in Fig. 2a, ..."). Provide a detailed caption for Figure 2 that explains what each panel shows and what the plotted values represent.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Section IV-C, Evaluation Metrics
    - **Evidence pointer** Section IV-C
    - **Issue** The definitions of MCC, F1, AUC, and AUPR are given in the text, but the formulas are not explicitly written out. While these are standard metrics, providing the exact formulas (especially for MCC) would improve precision and self-containedness.
    - **Required correction** Add the explicit formulas for MCC, F1, Precision, Recall, and the definitions of AUC and AUPR.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Clarity and Presentation
    - **Affected element** Section III-A, Algorithm 1
    - **Evidence pointer** Algorithm 1
    - **Issue** The algorithm pseudocode is presented as a numbered list, which is not a standard format for an algorithm. It is also not referenced in the text as "Algorithm 1".
    - **Required correction** Reformat the pseudocode into a standard algorithm environment. Reference it in the text (e.g., "as detailed in Algorithm 1").

    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Clarity and Presentation
    - **Affected element** Section V-D, Figure 5
    - **Evidence pointer** Figure 5
    - **Issue** The text states "The best-evolved fusion architecture in Fig. 5 helps explain why a compact solution remains competitive." However, the figure is not described in the text, and its contents are not explained. The reader is left to guess what the figure shows.
    - **Required correction** Add a description of Figure 5 in the text, explaining what the architecture is and how it demonstrates the point about compactness and complementary features.

    - **Concern ID** R1-m5
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Section IV-B, Table I
    - **Evidence pointer** Table I
    - **Issue** The text states "Table I summarizes the key hyperparameters used in this study." However, the table is not shown in the provided text, and the hyperparameters for the MOEA are not mentioned.
    - **Required correction** Ensure Table I includes all hyperparameters, including those for the MOEA (population size, generations, mutation/crossover probabilities, etc.). If the table is too large, consider splitting it.

- **Technical failings that need to be addressed before the case is established**
    - R1-M1: Lack of statistical significance testing for the main performance claims.
    - R1-M2: Lack of a baseline comparison for the evolutionary search strategy itself.
    - R1-M3: Omission of computational cost analysis and MOEA hyperparameters.

- **Assessment against Nature-style criteria**
    - **Originality** Moderate. The combination of dual-view features and a multi-objective evolutionary algorithm for fusion is a novel engineering contribution, but the individual components are well-established. The originality lies in the specific integration and application to disorder prediction, not in a fundamentally new concept.
    - **Scientific importance** Moderate. Improving disorder prediction is a valuable goal with implications for functional annotation and drug discovery. However, the reported improvements are incremental and their significance is not established. The work is unlikely to fundamentally change the field's understanding of protein disorder.
    - **Interdisciplinary readership** Limited. The work is highly specialized and will primarily appeal to bioinformaticians and computational biologists. The use of evolutionary algorithms may draw some interest from the broader machine learning community, but the application is very specific.
    - **Technical soundness** The proposed method is technically sound in its design, but the experimental validation is incomplete. The lack of statistical testing and computational cost analysis are significant weaknesses that undermine the robustness of the claims.
    - **Readability for nonspecialists** The abstract and introduction are accessible, but the methodology section is dense and assumes significant prior knowledge of both deep learning architectures and evolutionary computation. The paper is not written for a general scientific audience.

- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising and the method is well-engineered. However, the manuscript in its current form does not fully establish the superiority of the proposed method due to the lack of statistical rigor and missing experimental details. The authors should be encouraged to revise the manuscript to address these concerns.

## Risk / unsupported claims
- The claim of "consistent" outperformance is not supported without statistical significance testing.
- The claim that the MOEA "adaptively discovers optimal fusion architectures" is not fully supported without a comparison to simpler search or fusion strategies.
- The claim that the method provides a "robust computational tool" is an overstatement given the lack of analysis on computational cost and potential failure modes.
- The specific numerical results for all baselines and ablations are not fully visible in the provided text, making a full independent assessment of the performance claims impossible.