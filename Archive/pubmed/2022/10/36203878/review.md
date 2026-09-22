## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, claims, and evidence as presented in the manuscript
- **Shared manuscript claim summary** The manuscript reviews computational and theoretical studies on the interplay between receptor-ligand binding and lipid domain formation during cell adhesion, proposing that ligand mobility and distribution determine whether these processes positively or negatively correlate.
- **Visible evidence base** Abstract, Introduction, Cell-cell adhesion, Cell-extracellular matrix adhesion, Discussion and perspective sections; no figures or tables were provided
- **Missing materials affecting confidence** Figures and tables referenced in the text (e.g., Figure 1A, 1B, 2A-C) were not provided; primary simulation data and methodological details of the reviewed studies are not included

## Reviewer
- **Overall assessment** This is a well-structured review article that synthesizes recent computational work on the coupling between receptor-ligand binding and lipid raft dynamics in cell adhesion. The authors present a coherent framework distinguishing cell-cell adhesion (mobile ligands) from cell-extracellular matrix adhesion (immobile ligands), and they use this distinction to reconcile contradictory experimental observations. The manuscript is clearly written and accessible to a broad biophysics audience. However, the review relies heavily on the authors' own prior simulation studies, and the absence of figures and quantitative details limits the ability to fully evaluate the strength of the evidence presented. The conceptual framework is valuable, but the review would benefit from more critical engagement with alternative models and from explicit discussion of model limitations.

- **Who would be interested in the results, and why** Researchers in membrane biophysics, cell adhesion, and lipid raft biology would find this review useful. It provides a theoretical perspective on how membrane heterogeneity and receptor-ligand interactions are coupled, which is relevant to understanding immune synapse formation, cancer cell adhesion, and integrin-mediated signaling. Computational biologists and experimentalists studying membrane-protein interactions may also benefit from the synthesis of simulation approaches and the proposed framework for interpreting contradictory experimental data.

- **Major strengths** The manuscript offers a clear conceptual framework that distinguishes between mobile and immobile ligand systems, providing a plausible explanation for contradictory experimental findings. The review is well-organized, with logical progression from cell-cell to cell-extracellular matrix adhesion. The authors connect theoretical predictions to experimental observations, which enhances the practical relevance of the review. The discussion of future directions, particularly the role of the cytoskeleton, is thoughtful and forward-looking.

- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3  
  - R1-M4  

- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3  
  - R1-m4  
  - R1-m5  

- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3

- **Assessment against Nature-style criteria**  
  - Originality: The review presents a synthesis of recent computational work, but the core ideas largely derive from the authors' own prior publications. The framework distinguishing mobile and immobile ligand systems is useful but not entirely novel.  
  - Scientific importance: The topic is of significant interest to cell biology and biophysics, and the review addresses a real gap in understanding how membrane heterogeneity and adhesion are coupled.  
  - Interdisciplinary readership: The manuscript is accessible to researchers in biophysics, cell biology, and computational biology, though some sections assume familiarity with statistical mechanics.  
  - Technical soundness: The review is technically sound in its description of the models, but the lack of quantitative detail and figures prevents full verification of the claims.  
  - Readability for nonspecialists: The writing is clear and generally accessible, though the Introduction could be streamlined for a broader audience.

- **Recommendation posture** Supportive if technical concerns are resolved, particularly the inclusion of figures and more critical discussion of model limitations.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** The manuscript claims that receptor-ligand binding promotes coalescence of lipid clusters into mesoscale domains in cell-cell adhesion, and that this enhances binding affinity and cooperativity.  
- **Evidence pointer** Cell-cell adhesion section, location not provided  
- **Concern** The central claims are based on the authors' own Monte Carlo simulations and mean-field calculations, but the manuscript does not provide quantitative results, parameter values, or direct comparisons with experimental data. The referenced figures (Figure 1A, 1B) were not included in the provided material, making it impossible to assess the magnitude of the reported effects or the robustness of the conclusions.  
- **Why it matters** The review's primary contribution is the claim that computational models explain experimental observations. Without access to the underlying data or figures, the reader cannot evaluate whether the simulations are well-converged, whether the parameter ranges are physiologically relevant, or whether the predicted effects are large enough to be biologically meaningful.  
- **Resolution test** Provide the referenced figures and a summary of key quantitative results, including parameter values, error estimates, and comparisons with experimental measurements where available.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Claim support  
- **Claim pointer** The manuscript states that for cell-extracellular matrix adhesion with immobile ligands, the relationship between receptor-ligand binding and lipid cluster coalescence depends strongly on ligand distribution, with clustered ligands promoting cooperation and uniform or random ligands promoting antagonism.  
- **Evidence pointer** Cell-extracellular matrix adhesion section, location not provided  
- **Concern** The distinction between single and multiple ligand clusters is presented as a key finding, but the mechanistic explanation is brief and the supporting evidence is not shown. The claim that a single cluster promotes raft coalescence while multiple clusters inhibit it is counterintuitive and requires more detailed explanation of the underlying thermodynamics. The manuscript does not discuss how the size, density, or spatial arrangement of clusters affects the outcome.  
- **Why it matters** This is a central claim of the review and is used to reconcile contradictory experimental results. If the evidence is not clearly presented, the framework loses its explanatory power and the reader cannot assess whether the conclusions are robust.  
- **Resolution test** Include a detailed description of the simulation setup for different ligand distributions, present the phase diagrams or key observables, and provide a mechanistic explanation for the observed differences between single and multiple clusters.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Scope and generalizability  
- **Claim pointer** The manuscript claims that the reviewed results "deepen our understanding of correlations between cell adhesion and membrane heterogeneities" and can help clarify contradictory experimental observations.  
- **Evidence pointer** Abstract and Discussion, location not provided  
- **Concern** The review focuses almost exclusively on the authors' own computational models. It does not critically discuss alternative theoretical approaches, such as continuum membrane models, molecular dynamics simulations of specific receptor-ligand pairs, or experimental studies that may not support the proposed framework. The generalizability of the conclusions to real biological membranes, which contain a complex mixture of lipids, proteins, and cytoskeletal interactions, is not addressed.  
- **Why it matters** A review article should provide a balanced perspective on the field. If the review only presents one line of evidence, it risks overstating the certainty of the conclusions and may mislead readers about the current state of knowledge.  
- **Resolution test** Add a section discussing alternative models and experimental findings that may challenge or refine the proposed framework, and explicitly state the limitations of the reviewed computational approaches.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Reproducibility  
- **Claim pointer** The manuscript describes a mesoscopic model with specific parameters, including raft-raft contact energy, raft area fraction, and receptor-ligand binding energy, but does not provide sufficient detail for reproduction.  
- **Evidence pointer** Cell-cell adhesion and Cell-extracellular matrix adhesion sections, location not provided  
- **Concern** The model description is qualitative. Key details such as the lattice size, simulation length, equilibration protocol, and the range of parameter values explored are not given. The relationship between the model parameters and physical quantities (e.g., how the contact energy maps to real lipid-lipid interactions) is not explained.  
- **Why it matters** Without these details, the simulations cannot be reproduced or independently verified, which weakens the scientific basis of the review's claims.  
- **Resolution test** Provide a supplementary methods section or table summarizing the model parameters, simulation protocols, and the mapping between model parameters and physical quantities.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Introduction  
- **Evidence pointer** Introduction, location not provided  
- **Issue** The Introduction is dense and covers a wide range of topics, including experimental techniques, model systems, and biological context. Some sentences are long and could be simplified for readability.  
- **Required correction** Consider breaking up long sentences and using subheadings to guide the reader through the background material.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Terminology  
- **Affected element** Cell-cell adhesion section  
- **Evidence pointer** Cell-cell adhesion section, location not provided  
- **Issue** The term "cis-attraction" is used to describe the fluctuation-induced attraction between receptor-ligand complexes, but this term may be confusing to readers unfamiliar with the membrane biophysics literature.  
- **Required correction** Define "cis-attraction" explicitly when first used, or use a more descriptive term such as "lateral attraction within the same membrane."

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Discussion and perspective  
- **Evidence pointer** Discussion and perspective section, location not provided  
- **Issue** The discussion of future directions focuses on the cytoskeleton but does not mention other potentially important factors, such as membrane curvature, protein crowding, or active processes.  
- **Required correction** Briefly mention additional factors that could influence the interplay between receptor-ligand binding and lipid domain formation.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Consistency  
- **Affected element** Abstract and Discussion  
- **Evidence pointer** Abstract and Discussion, location not provided  
- **Issue** The abstract states that the review covers "recent computational studies," but the Discussion refers to "we adopt the mesoscale model," suggesting that the authors are presenting their own unpublished results. This inconsistency could confuse readers about the scope of the review.  
- **Required correction** Clarify in the abstract and throughout the text which results are from published studies and which are new or unpublished.

- **Concern ID** R1-m5  
- **Severity** Minor  
- **Axis** Referencing  
- **Affected element** Throughout  
- **Evidence pointer** Location not provided  
- **Issue** The manuscript cites several of the authors' own papers but does not always provide context for how these studies relate to other work in the field.  
- **Required correction** Add more citations to independent studies and discuss how the authors' findings compare with or extend other theoretical and experimental work.

## Risk / unsupported claims
- The claim that receptor-ligand binding affinity can serve as a general indicator of the phase transition in cell-cell adhesion is not fully supported by the evidence presented, as no quantitative data or error analysis is provided.
- The claim that the reviewed results can reconcile contradictory experimental observations is plausible but not rigorously demonstrated, as the manuscript does not systematically compare model predictions with specific experimental datasets.
- The statement that "the receptor-ligand binding and the lipid cluster coalescence can be correlated or anti-correlated, depending strongly on the ligand distribution" is presented as a general conclusion but is based on a limited set of simulation scenarios that may not capture the full complexity of biological systems.
- The discussion of the SARS-CoV-2 example, while interesting, is speculative and not directly supported by the reviewed computational studies.