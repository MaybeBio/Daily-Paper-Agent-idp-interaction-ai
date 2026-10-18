## Review setup
- **Input scope** Full manuscript text (abstract, main text, methods) as provided
- **Assessment boundary** Scientific claims, methodological soundness, validation rigor, and presentation quality based solely on the supplied material
- **Shared manuscript claim summary** The authors present CHORUS, a sequence-only deep learning framework that predicts residue-level protein-protein interaction (PPI) interfaces in α-helical transmembrane proteins. The method uses an ensemble of six predictors combining three protein language models (ESM-2, ESM-C, ProtT5) at selected layers with three neural network backbones. The authors report state-of-the-art performance against 18 established methods on a large independent test set, demonstrate accurate interface prediction on respiratory supercomplexes, and release a proteome-scale atlas covering 80,619 reviewed transmembrane proteins.
- **Visible evidence base** Abstract, Results sections (Overview, Orchestrating cross-pLM representation diversity, Performance evaluation, External datasets, Representation analyses, Membrane regions, Biological contexts, Supercomplex validation, Atlas description), Methods sections (dataset construction, model architectures, training, evaluation, statistical analysis)
- **Missing materials affecting confidence** Figures and tables referenced throughout (Figs 1-7, Supplementary Figs 1-2, Supplementary Tables 1-21) are not provided. Detailed hyperparameter values, exact model configurations, and full benchmark results per method are referenced but not visible. The web atlas and code repository URLs are stated but not accessible for verification.

## Reviewer
- **Overall assessment** This manuscript presents a potentially valuable contribution to the field of membrane protein interaction prediction. The core idea of combining multiple pLM families and layers in an ensemble for sequence-only PPI interface prediction is sensible and the reported performance gains are notable. The scale of the atlas resource is impressive. However, the manuscript as provided has several significant gaps that prevent full evaluation. The absence of all figures and tables makes it impossible to assess the quality of the visualizations, the detailed benchmark comparisons, and the biological case studies. The methodological description, while detailed in parts, lacks specific hyperparameter values and some implementation details that would be necessary for reproduction. The statistical analysis section is thorough in describing resampling procedures, but the actual results of these analyses are not visible. The claims of superiority over 18 methods rest entirely on numbers that are not shown. The biological validation on the respiratory supercomplex is described qualitatively but the quantitative results are not presented. The discussion of limitations is honest and appropriate. Overall, the work appears promising but the current form does not allow a definitive assessment of its claims.
- **Who would be interested in the results, and why** Computational biologists working on protein-protein interaction prediction, particularly those focused on membrane proteins, would be the primary audience. Researchers studying membrane protein structure and function, especially those interested in respiratory complexes, signaling receptors, and transporters, would find the atlas resource valuable. The demonstration that pLM embeddings can capture membrane-specific interaction features without structural input is of general interest to the deep learning for protein science community. The atlas could serve as a resource for experimental biologists seeking to prioritize residues for mutagenesis or epitope mapping in membrane proteins. The analysis of conservation patterns across membrane regions provides insights relevant to evolutionary biologists studying membrane protein evolution.
- **Major strengths** The manuscript addresses a clear and important gap: sequence-only prediction of PPI interfaces in membrane proteins, which are underrepresented in most interaction prediction tools. The ensemble approach across pLM families and layers is well-motivated and the ablation studies described suggest that cross-family diversity provides genuine value beyond simple scaling. The scale of the atlas (80,619 proteins, 33.7 million residues) is a significant resource contribution. The validation on respiratory supercomplexes is a strong test case given their size and complexity. The statistical framework using cluster-level resampling is appropriate for the hierarchical data structure. The authors are transparent about limitations, particularly regarding polytopic proteins and transient soluble interactions.
- **Major Concerns**
- **Minor Comments**
- **Technical failings that need to be addressed before the case is established** The absence of all figures and tables is the most critical failing. Without these, the core performance claims cannot be verified. The benchmark methodology, while described, cannot be assessed for fairness without seeing the per-method results. The biological case studies are described but not shown. The atlas interface and its utility cannot be evaluated.
- **Assessment against Nature-style criteria** Originality: The ensemble approach across pLM families for membrane-specific PPI prediction is a novel combination, though each component is established. Scientific importance: The atlas resource and the demonstrated performance gains have the potential to be impactful for the membrane protein community. Interdisciplinary readership: The work bridges deep learning, structural biology, and membrane biochemistry, which could attract a broad audience. Technical soundness: The methodology appears sound in principle, but the missing figures and tables prevent full verification. Readability for nonspecialists: The main text is generally clear, though some sections assume familiarity with pLM architectures and PPI prediction benchmarks.
- **Recommendation posture** Supportive if technical concerns are resolved. The core approach is promising and the resource is potentially valuable, but the manuscript in its current form does not provide sufficient visible evidence to establish the claims. The authors should be encouraged to resubmit with all figures and tables included, and with additional details on benchmark methodology and hyperparameters.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The manuscript claims CHORUS outperforms 18 established methods across 4,655 test contexts with an average precision of 0.643.
- **Evidence pointer** Results section "Performance evaluation on the independent test set", Figure 3, Supplementary Tables 10-11
- **Concern** The central performance claim of the manuscript cannot be evaluated because Figure 3 and all supplementary tables are not provided. The reader cannot see the per-method comparison, the magnitude of improvements, or the variability across methods. The claim of superiority over 18 methods is the foundation of the paper's significance, and without the actual benchmark results, this claim is unverifiable.
- **Why it matters** The primary contribution of the work is the demonstrated performance advantage. Without the visible benchmark data, the reader cannot assess whether the improvement is meaningful, whether it is consistent across method types, or whether the comparison was conducted fairly. This is the core evidence needed to establish the case.
- **Resolution test** Provide Figure 3 and Supplementary Tables 10-11 in full. Include per-method AP values, confidence intervals, and details on input requirements and configurations for each of the 18 methods. The comparison should be transparent about any method-specific tuning or adaptation.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological reproducibility
- **Concern** The Methods section describes the model architectures and training procedures but omits critical hyperparameters. The learning rate, batch size, number of epochs, optimizer settings, and specific layer dimensions are not stated. The description of the sliding window approach for long sequences lacks the exact window size and overlap values used during inference. The threshold selection procedure is described but the actual value (0.554) is only mentioned in the Results. Without these details, the work cannot be reproduced.
- **Why it matters** Reproducibility is a fundamental requirement for computational biology papers. The authors state that a repository with full configuration details will be released upon publication, but this is not sufficient for review. The reviewers and readers need to be able to assess the methodological choices and potentially reproduce the results.
- **Resolution test** Include a complete hyperparameter table in the main text or supplementary materials. Specify all optimizer settings, learning rates, batch sizes, architectural dimensions, and any regularization or early stopping criteria. Provide the exact sliding window parameters used for inference on long sequences.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation rigor
- **Concern** The external validation on respiratory supercomplexes is described qualitatively but no quantitative results are presented. The claim that CHORUS achieves an entity-macro AP of 0.984 on the porcine respirasome is stated in the Results but the supporting data, such as per-subunit performance, comparison to other methods on this specific test case, and visualizations of predicted versus actual interfaces, are not shown. The generalization to soluble proteins is also described but the quantitative results are not visible.
- **Why it matters** The respiratory supercomplex validation is a key demonstration of the method's practical utility on large, biologically important assemblies. Without the quantitative results and visualizations, the reader cannot assess the quality of the predictions or compare them to what structural knowledge would suggest. The soluble protein generalization results are important for understanding the method's broader applicability.
- **Resolution test** Provide the full results for the respiratory supercomplex analysis, including per-subunit AP values, visualizations of predicted interfaces mapped onto the cryo-EM structures, and a comparison to other methods on this test case. For the soluble protein analysis, provide the quantitative results for each of the 19 assemblies tested.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Biological interpretation
- **Concern** The analysis of biological context (Figure 5) is described in the text but the figure is not provided. The claims about performance differences across membrane regions, interaction partner types, and taxonomic groups cannot be evaluated. The finding that performance degrades for polytopic proteins with 7 or more transmembrane segments is important for understanding the method's limitations, but the data supporting this claim is not visible.
- **Why it matters** Understanding where the method works well and where it fails is crucial for users of the atlas and for future method development. The biological context analysis provides this information, but without the figure, the claims are unverifiable.
- **Resolution test** Provide Figure 5 in full, including all panels showing performance across membrane regions, partner types, topological complexity, and taxonomic groups. Include the underlying data in supplementary tables.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Comparison fairness
- **Concern** The comparison with 18 established methods is described but the details of how each method was configured and run are not visible. The authors state that structure-based methods used predicted structures from ESMFold or ColabFold, but the specific versions, parameters, and any method-specific preprocessing are not described. The potential for unfair comparison due to differences in training data, thresholds, or evaluation protocols cannot be assessed.
- **Why it matters** Benchmarking studies are only as credible as the fairness of the comparisons. Without seeing the detailed configuration of each baseline method, the reader cannot determine whether the comparison was conducted in a way that gives CHORUS an unfair advantage or disadvantages the baselines.
- **Resolution test** Provide a detailed table describing the exact configuration, input requirements, and any adaptations made for each of the 18 baseline methods. Include information on how thresholds were set for each method and whether any method-specific tuning was performed.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states the atlas covers "80,619 reviewed transmembrane proteins" but does not clarify whether this includes both α-helical and β-barrel proteins. The Methods section indicates the focus is on α-helical proteins, and the Results mention 27 β-strand chains in the training data. This discrepancy should be clarified.
- **Required correction** Specify in the abstract that the atlas covers α-helical transmembrane proteins, or clarify the inclusion criteria for β-barrel proteins.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Results section "Overview of the CHORUS framework"
- **Evidence pointer** Results section, Figure 1
- **Issue** The term "partner-agnostic" is used to describe the prediction task. This is appropriate but could be confused with "partner-specific" prediction methods. A brief clarification of what "partner-agnostic" means in this context (i.e., predicting interface residues without knowing the identity of the binding partner) would be helpful for readers unfamiliar with the PPI prediction literature.
- **Required correction** Add a brief parenthetical clarification when the term is first used.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results section "Performance evaluation on the independent test set"
- **Evidence pointer** Results section, Figure 3
- **Issue** The text reports average precision values but does not report confidence intervals for the main comparison. The authors describe bootstrap procedures in the Methods but do not present the resulting intervals in the Results.
- **Required correction** Include confidence intervals for the main performance metrics in the text or in Figure 3.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Resource description
- **Affected element** Atlas description
- **Evidence pointer** Results section "Pan-proteomic landscape", Data availability
- **Issue** The atlas is described as a "searchable" resource with "automatic topological alignment onto experimental structures or homology models," but the specific query capabilities, download options, and API access are not described. The URL provided in the Data availability section differs from the one in the Abstract.
- **Required correction** Provide a more detailed description of the atlas interface, including query types, download formats, and any API endpoints. Ensure the URL is consistent between the Abstract and Data availability sections.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Related work
- **Affected element** Introduction
- **Evidence pointer** Introduction
- **Issue** The introduction provides a good overview of the field but does not explicitly discuss recent deep learning methods for PPI interface prediction that also use pLM embeddings, such as those based on ESM-2 or ProtTrans. A brief discussion of how CHORUS differs from these recent approaches would strengthen the motivation.
- **Required correction** Add a paragraph in the Introduction discussing recent pLM-based PPI prediction methods and explicitly stating the novelty of CHORUS relative to these approaches.

## Risk / unsupported claims
- The claim that CHORUS "outperforms 18 established sequence- and structure-based methods" is unsupported in the provided material because the benchmark results (Figure 3, Supplementary Tables 10-11) are not visible.
- The claim of "amplified predictive capacity within the lipid-embedded core (0.746)" is unsupported without the underlying data and figure.
- The claim that CHORUS "delineates quaternary contact boundaries across megadalton respiratory supercomplexes directly from sequences alone (0.984)" is unsupported without the quantitative results and visualizations.
- The claim that CHORUS "decodes bona fide quaternary contact physics rather than generic pocket concavity" based on the BioLiP analysis is not fully supported because the analysis details and results are not visible.
- The claim that "intramembrane interfaces exhibit pronounced sequence plasticity" based on the FunFam analysis is not fully supported without the underlying data.
- The atlas coverage of "80,619 reviewed transmembrane proteins spanning 4,918 species" is stated but the completeness of this coverage relative to the total number of known transmembrane proteins is not discussed.
- The performance on soluble protein complexes is described but the quantitative results are not provided, making the claim of generalization difficult to assess.