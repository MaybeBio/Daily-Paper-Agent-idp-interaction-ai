## Review setup
- **Input scope** Full manuscript text (main text, equations, and references) as provided.
- **Assessment boundary** The review assesses the manuscript's scientific content, technical soundness, and clarity as a review article. It does not assess the accuracy of the references cited, as they are not provided in full.
- **Shared manuscript claim summary** The manuscript is a review article that summarizes recent theoretical and computational advances in predicting and designing multiphase coexistence in biomolecular mixtures. It covers mean-field models, sequence-dependent theories, coarse-grained simulations, and inverse design approaches, and outlines future challenges.
- **Visible evidence base** The manuscript's claims are supported by descriptions of published work, including specific model types, theoretical predictions, and simulation results. The text includes equations for free-energy models and describes qualitative and quantitative findings from cited studies.
- **Missing materials affecting confidence** The full text of all cited references is not provided, preventing independent verification of the accuracy of the summarized results. Additionally, the manuscript lacks a dedicated methods section, which is typical for a review but limits the ability to assess the reproducibility of any specific calculations described.

## Reviewer
- **Overall assessment** This is a well-written and timely review that addresses an important and rapidly evolving area of biophysical chemistry. The author provides a clear conceptual framework for understanding multiphase coexistence, effectively bridging statistical mechanical theories with coarse-grained simulation approaches. The organization is logical, progressing from fundamental thermodynamic principles to specific model classes and ending with a forward-looking perspective. The review is likely to be a valuable resource for researchers entering the field and for experimentalists seeking a theoretical grounding. However, the review's scope is somewhat narrow, focusing heavily on the author's own contributions and closely related work, which may limit its comprehensiveness as a general overview. The discussion of future challenges, while relevant, is relatively brief and could be more deeply developed.
- **Who would be interested in the results, and why** Researchers in biophysics, physical chemistry, and computational biology studying biomolecular condensates, phase separation, and intracellular organization. The review is also relevant for experimentalists in cell biology and biochemistry who seek a theoretical framework for interpreting their observations of multiphase condensates. The clear explanations of complex concepts make it accessible to graduate students and postdocs entering the field.
- **Major strengths**
    1.  The review provides a clear and logical conceptual framework, starting from fundamental thermodynamic principles and building towards complex, multicomponent systems.
    2.  It effectively bridges different theoretical approaches, including mean-field models, field-theoretic methods, and coarse-grained simulations, highlighting their complementary strengths and limitations.
    3.  The discussion of inverse design as a strategy for engineering phase behavior is a forward-looking and valuable contribution.
    4.  The writing is clear and accessible, making complex topics understandable for a broad audience.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scope and comprehensiveness
    - **Claim pointer** The review claims to cover "recent advances in the prediction and computational design of biomolecular mixtures that phase-separate into many coexisting phases."
    - **Evidence pointer** Sections III and IV, and the reference list.
    - **Concern** The review's scope is heavily weighted towards the author's own research program and closely related work, particularly in the areas of random interaction matrices and inverse design. While this work is significant, a more comprehensive review would benefit from a broader survey of the field, including a more detailed discussion of other prominent approaches, such as stickers-and-spacers models applied to specific biological systems, and a more balanced representation of the literature. The current focus may give a reader new to the field a somewhat skewed perspective on the landscape of available methods.
    - **Why it matters** A review article should provide a balanced and comprehensive overview of a field. An over-reliance on a single research group's contributions can limit the review's utility as an unbiased introduction and reference for the community.
    - **Resolution test** The author should expand the scope to include a more diverse range of theoretical and simulation approaches, and ensure that the discussion of each approach is proportionate to its impact and usage in the field. This could involve adding sections or subsections on other model families and citing a broader range of primary literature.
    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** No
    - **Axis** Depth of critical analysis
    - **Claim pointer** The review describes various methods and their predictions but often does not critically compare their relative accuracy, computational cost, or applicability to different biological questions.
    - **Evidence pointer** Sections III and IV.
    - **Concern** The review is largely descriptive, summarizing the results of various studies without a deep critical analysis of their strengths and weaknesses. For example, the discussion of RPA and its limitations is brief, and the comparison between different coarse-grained models is not systematic. A more critical perspective, explicitly stating which methods are best suited for which problems and why, would significantly enhance the review's value.
    - **Why it matters** A key role of a review is to help readers navigate the complex landscape of available methods. A purely descriptive summary does not provide sufficient guidance for researchers to choose the most appropriate approach for their specific problem.
    - **Resolution test** The author should add a more explicit comparative analysis of the discussed methods, including a discussion of their respective assumptions, limitations, and domains of applicability. A summary table comparing key features of different models would be a useful addition.
    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Depth of future outlook
    - **Claim pointer** The final section, "Outlook and challenges," lists several future directions.
    - **Evidence pointer** Section V.
    - **Concern** The "Outlook and challenges" section, while identifying important areas, is relatively brief and does not delve into the specific technical hurdles or potential strategies for overcoming them. For instance, the challenge of accounting for nonequilibrium effects is mentioned, but the specific theoretical or computational frameworks that might be extended to address this are not discussed in detail.
    - **Why it matters** A forward-looking perspective is a key component of a high-impact review. A more detailed and speculative discussion of future directions would be more stimulating and useful for the community.
    - **Resolution test** The author should expand the final section to provide a more detailed and critical discussion of each challenge, including potential avenues for future research and the specific obstacles that need to be overcome.
- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity and accessibility
    - **Affected element** Section II, Figure 3
    - **Evidence pointer** Section II, Figure 3
    - **Issue** The description of the common tangent plane construction and the associated figure could be clearer for a non-specialist reader. The concept of a high-dimensional convex hull is abstract, and a more intuitive explanation or a schematic in the figure would be helpful.
    - **Required correction** Consider adding a more intuitive explanation of the common tangent plane construction, perhaps with a simple 2D or 3D schematic in Figure 3, to aid readers unfamiliar with convex geometry.
    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical accuracy
    - **Affected element** Section III.1, Equation (3)
    - **Evidence pointer** Section III.1, Equation (3)
    - **Issue** The text states that the model is consistent with Equation (3) with μ_v = 0, but the physical meaning of this choice (i.e., neglecting excluded volume) could be stated more explicitly for clarity.
    - **Required correction** Briefly state that setting μ_v = 0 corresponds to an athermal or ideal entropy of mixing, which is a simplifying assumption.
    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Completeness
    - **Affected element** Section IV.2
    - **Evidence pointer** Section IV.2
    - **Issue** The discussion of associating fluid theory is focused on its application to specific biological systems. A brief mention of the theory's broader historical development and its roots in chemical engineering would provide useful context.
    - **Required correction** Add a sentence or two providing historical context for associating fluid theory, citing its origins in the study of associating fluids in chemical engineering.
    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Clarity
    - **Affected element** Section V
    - **Evidence pointer** Section V
    - **Issue** The list of future challenges is presented as a bulleted list, which is clear but somewhat disjointed. A more integrated narrative connecting these challenges would improve readability.
    - **Required correction** Consider rewriting the final section as a more connected prose discussion, rather than a list, to better highlight the interconnections between the challenges.

## Risk / unsupported claims
- The claim that "agreement between theory and experiment... provided strong evidence that the phase behavior of these condensates is indeed governed by specific PPIs and interactions between RBDs and mRNA" (Section IV.2) is presented as a summary of a cited work. The strength of this evidence cannot be independently assessed without access to the cited reference.
- The statement in Section III.1 that "simulation results indicated that the extreme values of the interaction matrix are more predictive of the simulated coexistence concentrations than the eigenspectrum of the mean-field Hessian matrix" is a specific finding from a cited study. Its validity is not verifiable from the provided text alone.
- The general claim in the abstract that the review covers "recent advances" is supported by the text, but the completeness of the coverage is not verifiable without a full literature search.