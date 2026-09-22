## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, technical soundness, and presentation of the review article as provided
- **Shared manuscript claim summary** The manuscript is a review article that surveys recent advances in multiscale simulation of intrinsically disordered proteins (IDPs), with a focus on enhanced sampling techniques, force field developments, and coarse-grained approaches for studying IDP conformational ensembles and dynamic interactions.
- **Visible evidence base** Full text including abstract, introduction, sections on force fields, enhanced sampling methods, multiscale approaches, and concluding remarks; one figure referenced (Figure 1, Figure 2); one table referenced (Table 1); equations for REST scaling factors
- **Missing materials affecting confidence** Figures and tables referenced in the text were not provided; specific citation details for many referenced studies are incomplete; no supplementary information was available

## Reviewer
- **Overall assessment** This is a well-structured and informative review that covers an important and rapidly evolving area of computational biophysics. The authors demonstrate strong command of the subject matter and provide a useful synthesis of recent methodological developments. The organization is logical, progressing from force field accuracy to enhanced sampling techniques to multiscale approaches. The discussion of REST methods and their sensitivity to force field balance is particularly insightful. However, the review would benefit from more critical comparative analysis of method performance, clearer guidance for practitioners on method selection, and more explicit discussion of validation against experimental data. The absence of figures and tables in the provided material limits full evaluation of the illustrative content.
- **Who would be interested in the results, and why** Computational biophysicists and chemists working on protein simulations, particularly those studying IDPs and dynamic protein interactions. Method developers in enhanced sampling and coarse-graining will find the survey of recent techniques useful. Experimentalists studying IDPs who seek to understand what computational approaches can offer for interpreting their data would also benefit. The review is timely given the growing recognition of IDP importance in biology and disease.
- **Major strengths** 
  1. Comprehensive and current coverage of enhanced sampling methods relevant to IDP simulations, with appropriate categorization into CV-based and CV-free approaches.
  2. Insightful discussion of the interplay between force field accuracy and sampling efficiency, particularly the sensitivity of REST performance to the balance of protein-protein and protein-water interactions.
  3. Clear articulation of the multiscale strategy, connecting atomistic simulations with coarse-grained approaches for addressing larger systems.
  4. Balanced treatment of successes and remaining limitations of current methods.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness
  - **Claim pointer** The manuscript claims that "REST has proven to be one of the most reliable choices for enhanced sampling of protein folding and particularly disordered conformational ensembles" and that "REST are specifically appropriate in simulating IDRs as the disordered region can be targeted in REST without tempering the well-structured region."
  - **Evidence pointer** Section 4.2, location not provided
  - **Concern** While the authors cite several successful applications of REST, the claim of "most reliable" is presented without systematic comparative analysis against other enhanced sampling methods. The discussion of REST's advantages is largely qualitative, and the sensitivity of REST to force field balance (as noted in the p53-TAD example) raises questions about its general reliability. A more critical assessment of when REST is preferable to other methods, and when it may fail, would strengthen the review.
  - **Why it matters** Readers seeking to select an appropriate enhanced sampling method for their specific IDP system need clearer guidance on the relative merits and limitations of REST compared to alternatives such as metadynamics, accelerated MD, or other replica exchange variants. The current presentation may overstate the general reliability of REST.
  - **Resolution test** The authors should provide a more systematic comparison of REST performance across multiple benchmark systems, including cases where REST fails or underperforms relative to other methods, and discuss criteria for method selection based on system properties and research questions.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Claim pointer** The manuscript states that "together with dramatically improved protein force fields, these advanced simulation approaches have achieved substantial success and demonstrated significant promise towards the quantitative and predictive modeling of IDPs and their dynamic interactions."
  - **Evidence pointer** Abstract and Section 3, location not provided
  - **Concern** The claim of "quantitative and predictive modeling" is ambitious and not fully supported by the evidence presented. While the review documents improvements in force fields and sampling methods, it also acknowledges significant remaining limitations, including challenges with large systems, residual structure prediction, and the balance of interactions. The gap between current capabilities and the stated promise of quantitative prediction is not critically examined.
  - **Why it matters** The field of IDP simulation is still developing, and overstating current capabilities could mislead readers about the maturity of these methods. A more nuanced assessment of what constitutes "quantitative" agreement with experiment, and where current methods fall short, would provide a more accurate picture.
  - **Resolution test** The authors should provide specific examples where simulations have achieved quantitative agreement with experimental observables (e.g., chemical shifts, SAXS profiles, FRET efficiencies) and clearly delineate the remaining challenges that prevent routine quantitative prediction.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness
  - **Claim pointer** The manuscript discusses "on-the-fly discovery of optimal CV was also demonstrated using the artificial neural networks" and "machine learning algorithms and deep learning network have been recently proposed to analyze information from many candidate CVs and construct the free energy landscape using low-dimensional representations."
  - **Evidence pointer** Section 4.1, location not provided
  - **Concern** The discussion of machine learning approaches for enhanced sampling is brief and lacks critical evaluation. The authors mention several methods but do not provide sufficient detail on their underlying principles, demonstrated applications to IDPs specifically, or comparative performance against established methods. The claim that these are "exciting developments" is not backed by concrete examples of IDP applications.
  - **Why it matters** Machine learning approaches to enhanced sampling are proliferating rapidly, and readers need guidance on which methods are mature enough for IDP applications and which remain proof-of-concept. The current treatment is too superficial to be useful for practitioners.
  - **Resolution test** The authors should either expand this section with specific examples of ML-based enhanced sampling applied to IDPs, including performance benchmarks, or temper the claims about their current utility for IDP simulations.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Section 4.2, equation for REST scaling factors
  - **Evidence pointer** Section 4.2, location not provided
  - **Issue** The equation for REST scaling factors is presented without sufficient explanation of the physical meaning of the parameters and how different scaling schemes (REST1 vs REST2) affect the sampling behavior. Nonspecialist readers may struggle to understand the practical implications.
  - **Required correction** Provide a brief explanation of the physical interpretation of the scaling factors and a qualitative description of how REST1 and REST2 differ in their effects on conformational sampling.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Section 5.2, discussion of coarse-grained models
  - **Evidence pointer** Section 5.2, location not provided
  - **Issue** The discussion of coarse-grained models for IDPs is somewhat cursory. The authors mention several models (SOP-IDP, HyRes, AWSEM-IDP, MARTINI-IDP) but do not provide sufficient detail on their key differences, parameterization strategies, or relative performance on benchmark systems.
  - **Required correction** Consider adding a comparative table summarizing key features of each coarse-grained model (resolution, parameterization approach, demonstrated applications, limitations) to aid readers in model selection.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Section 1, Introduction
  - **Evidence pointer** Section 1, location not provided
  - **Issue** The introduction assumes familiarity with IDP terminology and concepts. A brief primer on what defines an IDP, why they are biologically important, and why their simulation is particularly challenging would make the review more accessible to a broader audience.
  - **Required correction** Add a short paragraph in the introduction providing basic context on IDP properties and the specific challenges they pose for molecular simulation.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Scientific importance
  - **Affected element** Section 6, Concluding Remarks
  - **Evidence pointer** Section 6, location not provided
  - **Issue** The concluding remarks are somewhat generic and do not provide a clear roadmap for future developments. The mention of machine learning as a "promising direction" is not developed into specific recommendations or predictions.
  - **Required correction** Expand the concluding section with more specific discussion of key open challenges and potential strategies to address them, including how ML methods might be integrated with existing approaches.
- **Technical failings that need to be addressed before the case is established** 
  - The manuscript claims that "REST has proven to be one of the most reliable choices" without providing systematic comparative evidence. This claim should be either substantiated with more comprehensive benchmarking or tempered.
  - The discussion of machine learning approaches for enhanced sampling is too brief to support the claim that these are "exciting developments that may greatly expand the applicability" of CV-based methods. More concrete examples or a more cautious framing is needed.
  - The statement that "quantitative and predictive modeling" has been achieved is not fully supported by the evidence presented, given the acknowledged limitations. This should be reframed to more accurately reflect current capabilities.
- **Assessment against Nature-style criteria** 
  - **Originality**: The review covers a rapidly evolving field and includes recent developments, but the overall structure and topics are similar to other recent reviews on IDP simulation. The specific focus on advanced sampling methods provides some differentiation, though the treatment is not sufficiently novel in its perspective or synthesis.
  - **Scientific importance**: The topic is of high importance given the growing recognition of IDP roles in biology and disease. The review addresses a genuine need for synthesis of recent methodological advances. However, the lack of critical comparative analysis limits its value as a definitive resource.
  - **Interdisciplinary readership**: The review is primarily targeted at computational biophysicists and chemists. While experimentalists studying IDPs may find it useful, the technical depth and lack of primer material limit broader accessibility.
  - **Technical soundness**: The technical content is generally accurate and well-informed, but the review would benefit from more critical evaluation of method performance and limitations. Some claims (e.g., REST reliability, ML utility) are not fully substantiated.
  - **Readability for nonspecialists**: The writing is clear and well-organized, but assumes significant background knowledge. The inclusion of equations and technical jargon without sufficient explanation may limit accessibility for readers outside the immediate field.
- **Recommendation posture** Supportive if technical concerns are resolved. The review addresses an important topic and provides a useful synthesis of recent developments. However, the claims regarding method reliability and predictive capability should be tempered or better substantiated, and the discussion of machine learning approaches should be either expanded or more cautiously framed. With these revisions, the review would be a valuable contribution to the literature.

## Risk / unsupported claims
- The claim that REST is "one of the most reliable choices" for enhanced sampling of IDPs is not supported by systematic comparative evidence in the manuscript.
- The statement that "quantitative and predictive modeling" of IDPs has been achieved is not fully supported given the acknowledged limitations discussed in the text.
- The assertion that machine learning approaches "may greatly expand the applicability" of CV-based methods is speculative and not backed by demonstrated IDP applications in the text.
- The claim that "many of these force fields are now well balanced for both folded and disordered proteins" is presented without quantitative evidence of balanced performance across diverse test cases.
- The statement that "REST are specifically appropriate in simulating IDRs as the disordered region can be targeted in REST without tempering the well-structured region" is presented as a general advantage without discussing potential limitations of this approach.