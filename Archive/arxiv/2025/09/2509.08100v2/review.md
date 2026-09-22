## Review setup
- **Input scope** Full manuscript text including main text, methods, and supplementary information
- **Assessment boundary** Scientific claims, methodology, theoretical framework, and evidence presented in the provided material
- **Shared manuscript claim summary** The authors propose that multicomponent surface condensates can be designed to perform classification tasks by recruiting distinct output molecules to surfaces with different input compositions. They demonstrate that hidden species expand the expressivity of these systems to encode nonlinear decision boundaries, and that trained parameters from mean-field models translate to 3D lattice simulations.
- **Visible evidence base** Main text figures (Figs. 1-7), supplementary figures (Figs. S1-S15), supplementary notes (Notes 1-7), and code availability statement
- **Missing materials affecting confidence** Experimental validation data, specific parameter values for trained models, detailed loss function hyperparameters, and quantitative comparison metrics with alternative approaches

## Reviewer
- **Overall assessment** This manuscript presents a theoretically grounded framework for understanding how multicomponent surface condensates can perform classification tasks, drawing an interesting analogy to machine learning architectures. The core idea that hidden species expand expressivity through encoding multiple phases is conceptually novel and potentially significant for understanding biological information processing. However, the manuscript would benefit from clearer presentation of the mathematical framework, more rigorous validation of the universal approximation claims, and explicit discussion of biological relevance and testable predictions.

- **Who would be interested in the results, and why** Researchers in biophysics, particularly those studying phase separation and condensate biology, would find this work relevant. The machine learning community interested in physical implementations of computation may also be interested. Additionally, synthetic biologists designing molecular circuits and systems biologists studying cellular decision-making would benefit from the conceptual framework presented.

- **Major strengths** The manuscript introduces a novel conceptual framework connecting phase separation physics to computational principles. The analytical treatment of decision boundaries in simple cases provides useful intuition. The demonstration that hidden species enable nonlinear classification is compelling and well-supported by simulations. The translation from mean-field to 3D lattice models strengthens the robustness of the findings.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that multicomponent surface condensates can perform classification tasks with high accuracy across various decision boundaries
- **Evidence pointer** Figures 2-3, 6-7; Supplementary Figures S1-S5, S13-S15
- **Concern** The manuscript lacks a systematic analysis of the robustness and stability of the trained solutions. The authors report success rates for classification tasks but do not provide error bars, confidence intervals, or analysis of variance across different random initializations. The training procedure appears to be deterministic in some cases, but the sensitivity of the results to hyperparameter choices and initial conditions is not thoroughly explored.
- **Why it matters** Without robustness analysis, it is difficult to assess whether the reported classification performance is a general property of the physical system or an artifact of specific training conditions. This is particularly important given the claim that these systems could function in biological contexts where parameters are subject to noise and variability.
- **Resolution test** The authors should provide multiple independent training runs with different random seeds, report mean and standard deviation of classification accuracy, and analyze how performance varies with key hyperparameters such as learning rate, batch size, and the number of training epochs.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The claim that hidden species expand expressivity by encoding multiple modular, encrypted phases
- **Evidence pointer** Figure 4; Supplementary Figures S8-S12
- **Concern** The biological relevance of the "encrypted phases" concept is not clearly established. While the authors draw analogies to coactivators and chromatin remodelers, the specific biological predictions or experimental tests that would validate this mechanism are not articulated. The manuscript would benefit from a more explicit discussion of how these findings could be tested experimentally and what biological systems might exhibit this behavior.
- **Why it matters** The significance of the work for biology depends on whether the proposed mechanism is experimentally accessible and biologically plausible. Without clear experimental predictions, the work remains primarily theoretical and its impact on the broader biological community may be limited.
- **Resolution test** The authors should provide specific, testable predictions for experimental systems, such as which molecular perturbations would alter classification behavior, what temporal dynamics would be expected, and how the predicted phase behavior could be observed experimentally.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The claim that the mean-field model provides a valid description of surface condensation dynamics
- **Evidence pointer** Equations 5-8; Supplementary Note 1
- **Concern** The derivation of the mean-field dynamics relies on several assumptions that are not fully justified. The treatment of the reservoir as infinite and well-mixed, the assumption of fast solvent dynamics, and the neglect of spatial correlations are all stated but not systematically validated. The authors do compare with 3D lattice simulations, but the parameter mapping between the two models is not described in sufficient detail to assess whether the comparison is meaningful.
- **Why it matters** The validity of the mean-field approximation is central to the theoretical framework. If the assumptions are not well-justified, the conclusions drawn from the mean-field analysis may not hold in more realistic settings.
- **Resolution test** The authors should provide a more detailed analysis of when the mean-field approximation breaks down, including systematic comparison with lattice simulations across a range of parameters, and discuss the biological conditions under which the assumptions are likely to hold.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Originality
- **Claim pointer** The claim that this framework provides a novel perspective on information processing in biological systems
- **Evidence pointer** Introduction; Discussion
- **Concern** While the specific application to surface condensates is novel, the general concept of physical systems performing computation through phase transitions has been explored in previous work, including the cited references on Hopfield networks and Boltzmann machines. The manuscript would benefit from a more explicit discussion of what is genuinely new about this framework compared to existing models of physical computation, and how it advances beyond the prior work cited.
- **Why it matters** The novelty of the contribution is a key criterion for publication in a high-impact journal. If the framework is largely a reapplication of existing ideas to a new physical system, the significance of the work may be more limited.
- **Resolution test** The authors should clearly articulate the specific new insights or capabilities that this framework provides beyond existing models, and discuss how these advances could lead to new understanding or applications.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Model formulation section
- **Evidence pointer** Equations 1-8
- **Issue** The mathematical notation is dense and some symbols are not clearly defined in the main text. The relationship between the free energy, chemical potential, and dynamics could be explained more intuitively.
- **Required correction** Provide a brief intuitive explanation of the key equations and define all symbols clearly. Consider adding a schematic figure illustrating the model setup.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Classification performance metrics
- **Evidence pointer** Figures 2-3, 6-7
- **Issue** The definition of classification success is binary (success/failure) and does not capture the degree of enrichment or the sharpness of the transition. A more quantitative metric would be informative.
- **Required correction** Report the actual concentration ratios of correct to incorrect output species, not just binary success, and consider reporting the sharpness of the transition.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion of biological implications
- **Evidence pointer** Discussion section
- **Issue** The biological implications are discussed at a general level, but specific examples of biological systems where this mechanism might operate are not provided.
- **Required correction** Provide concrete examples of biological systems where surface condensation-based classification could be relevant, and discuss how the predictions could be tested in those systems.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Lattice model validation
- **Evidence pointer** Figure 7; Supplementary Note 4
- **Issue** The comparison between mean-field and lattice models is presented for a limited set of conditions. The authors note that lattice models show more continuous variation near decision boundaries, but this is not quantified.
- **Required correction** Provide a quantitative comparison of mean-field and lattice model predictions across a range of conditions, including metrics for the sharpness of transitions and the degree of agreement.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Discussion of machine learning analogy
- **Evidence pointer** Introduction; Discussion
- **Issue** The analogy to machine learning is useful but could be developed further. The connection between hidden species and hidden nodes in neural networks is mentioned but not explored in depth.
- **Required correction** Expand the discussion of the machine learning analogy, including a more detailed comparison of the roles of different components and the implications for understanding both biological and artificial computation.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Training procedure
- **Evidence pointer** Methods; Supplementary Note 2
- **Issue** The training procedure is described, but the computational cost and scalability of the approach are not discussed. It is unclear how the method would scale to larger systems with more species.
- **Required correction** Provide information on computational requirements and discuss the scalability of the approach to larger systems.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Comparison with alternative approaches
- **Evidence pointer** Discussion
- **Issue** The manuscript does not compare the proposed framework with alternative models of biological information processing, such as gene regulatory networks or signaling cascades.
- **Required correction** Discuss how the proposed mechanism compares with and complements existing models of biological computation, and what unique capabilities it provides.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract is dense and may be difficult for nonspecialists to understand. The key findings and their significance could be stated more clearly.
- **Required correction** Revise the abstract to make the main findings and their implications more accessible to a broad audience.

## Risk / unsupported claims
- The claim that "the same molecular repertoire can be reprogrammed to solve new tasks" (Figure 5) is based on simulations with randomly generated interaction networks and may not generalize to biologically realistic parameter regimes.
- The universal approximation argument in Supplementary Note 3 relies on several assumptions that are acknowledged but not rigorously validated, including the existence of stable steady states and the absence of multiple local minima.
- The biological relevance of the "encrypted phases" concept is asserted but not supported by specific experimental evidence or detailed biological examples.
- The claim that the framework "suggests that the physical processes underlying biomolecular condensates can encode and drive adaptive information processing beyond compartmentalization" is a reasonable interpretation but goes beyond the direct evidence presented.
- The comparison with previous work on Hopfield networks and Boltzmann machines is qualitative and does not establish clear advantages or distinctions of the proposed framework.