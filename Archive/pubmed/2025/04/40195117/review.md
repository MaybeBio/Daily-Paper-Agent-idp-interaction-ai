## Review setup
- **Input scope** Full manuscript text (review article, no figures or tables included in the provided material)
- **Assessment boundary** Scientific content, structure, and claims as presented in the text; figures and tables referenced but not directly assessable
- **Shared manuscript claim summary** The authors present a narrative review of recent progress in structure-based protein-protein interaction (PPI) prediction, emphasizing the transformative role of AI-based methods, and discuss biomedical applications and remaining challenges including IDR-mediated interactions, host-pathogen PPIs, immune-related interactions, and quality assessment of predicted structures.
- **Visible evidence base** Text only; figures (Figures 1-4) and Table 1 are referenced but not provided; literature citations are present but not individually verifiable from the supplied material
- **Missing materials affecting confidence** Figures 1-4, Table 1, full reference list, and any supplementary material; these are essential for evaluating the accuracy of the historical timeline, methodological comparisons, and resource descriptions

## Reviewer

- **Overall assessment** This is a well-organized and clearly written review that covers a timely and important topic. The authors successfully trace the evolution of structure-based PPI prediction from coevolution-based and docking methods to modern deep learning approaches, and they provide a useful overview of biomedical applications. The discussion of challenges, particularly IDR-mediated interactions and immune-related PPIs, is thoughtful and identifies genuine gaps in the field. However, the review is largely descriptive rather than critical, and several claims about method performance and limitations would benefit from more quantitative support or direct comparison. The manuscript would be strengthened by a more explicit framework for evaluating different methods and by deeper engagement with the limitations of current AI-based approaches beyond what is presented.

- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein structure prediction, PPI prediction, and protein design would find this review useful as an entry point to the field. Structural biologists using cryo-EM or X-ray crystallography who are interested in integrating computational predictions into their workflows would also benefit. Additionally, researchers in drug discovery and therapeutic design, particularly those interested in targeting PPIs or designing protein binders, would find the applications section relevant. The challenges section on IDRs and immune interactions may attract immunologists and cell biologists seeking computational tools for their systems of interest.

- **Major strengths**
  1. The review provides a coherent historical narrative that connects early coevolution-based methods to modern deep learning approaches, which helps readers understand how the field arrived at its current state.
  2. The organization is logical, moving from methods to applications to challenges, and the figures (as described) appear well designed to support this structure.
  3. The discussion of biomedical applications is concrete and includes specific examples with experimental validation, which grounds the review in real biological impact.
  4. The challenges section identifies important and underappreciated problems, particularly the difficulty of predicting IDR-mediated interactions and the unique features of immune-related PPIs.
  5. The inclusion of a resources table (Table 1) is practical and will be useful for readers entering the field.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness / critical evaluation
- **Claim pointer** The review states that modern deep learning methods have achieved accuracy "comparable with experimental approaches" for PPI prediction, and that AF2-based methods "remain the best based on results from CASP15."
- **Evidence pointer** Introduction section; "Key developments in computational methods for PPI modeling" section; location not provided for specific CASP15 results
- **Concern** The claim that AI-based PPI prediction accuracy is comparable to experimental approaches is strong and potentially misleading. While AF2 and related methods have achieved remarkable accuracy for monomer structure prediction, the accuracy for complex prediction, particularly for antibody-antigen and other challenging targets, is substantially lower. The CASP15 results cited do show AF2-based methods performing well, but the review does not discuss the significant variability in accuracy across different types of complexes or the fact that many predicted interfaces may not be biologically relevant. The statement about comparability with experimental approaches needs qualification, as experimental methods can validate interactions under physiological conditions, whereas computational predictions often cannot distinguish between biologically relevant and non-specific interactions.
- **Why it matters** This claim could mislead readers, particularly experimental biologists, into over-trusting computational predictions without appropriate validation. The review itself later acknowledges that AI models can predict plausible structures for non-interacting pairs, which somewhat contradicts the earlier strong claim. A more nuanced statement would better serve the readership.
- **Resolution test** Revise the claim to specify which types of complexes achieve accuracy comparable to experimental methods, and add a discussion of the limitations of computational predictions in distinguishing true from false interactions. Provide specific quantitative metrics (e.g., DockQ scores, CAPRI ratings) for different complex types.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance / completeness
- **Claim pointer** The review states that "the challenge lies in selecting the correct ones" from multiple predicted structures, and that "physics-based methods are promising in ranking predictions and selecting the best models for challenging targets."
- **Evidence pointer** "Quality evaluation of predicted structures" section; location not provided
- **Concern** The discussion of model selection and quality assessment is underdeveloped. The authors mention their experience with CASP16 and suggest that physics-based methods are promising for ranking predictions, but they do not provide specific data or comparisons. The field has developed several metrics (e.g., pLDDT, PAE, ipTM) and methods for model selection, and the review would benefit from a more systematic discussion of these tools. Additionally, the claim that physics-based methods are promising is based on the authors' own analysis of CASP16 results, but no details are provided, making this difficult to evaluate.
- **Why it matters** Model selection is a critical practical issue for users of these prediction tools. A review that identifies this as a key challenge but does not provide concrete guidance or comparative data is less useful to the community than it could be.
- **Resolution test** Expand this section to include a systematic comparison of available quality assessment metrics and methods, with specific examples of their performance on different types of complexes. Provide quantitative data from the authors' CASP16 analysis to support the claim about physics-based methods.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness / completeness
- **Claim pointer** The review discusses methods for predicting IDR-mediated interactions and states that AFM "struggles to capture the dynamic and fuzzy interactions between IDRs."
- **Evidence pointer** "Interactions mediated by intrinsically disordered regions" section; location not provided
- **Concern** The discussion of IDR-mediated interactions is brief and does not adequately cover the range of computational approaches being developed for this problem. The review mentions DeePhase, machine learning models for LLPS prediction, and molecular simulation, but does not discuss recent developments in using AF2/AFM for IDR-containing complexes in more detail, nor does it address the growing literature on conformational ensembles and their prediction. The statement about AFM struggling with fuzzy interactions is supported by one reference, but the broader landscape of methods and their relative strengths and weaknesses is not presented.
- **Why it matters** IDR-mediated interactions are highlighted as a key future challenge, yet the review provides limited depth on this topic. Given the increasing importance of phase separation and IDRs in biology, a more comprehensive treatment would significantly increase the value of this review.
- **Resolution test** Expand this section to include a more detailed discussion of computational approaches for IDR-mediated interactions, including recent methods that combine AF2/AFM with molecular dynamics or ensemble-based approaches. Provide a comparative assessment of current capabilities and limitations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance / originality
- **Claim pointer** The review states that "predicting the impact of mutations on PPIs remains a challenging problem" and discusses the limitations of AF2 in this regard.
- **Evidence pointer** "Predicting the effect of mutations at PPI interfaces" section; location not provided
- **Concern** The discussion of mutation effect prediction is relatively brief and does not adequately cover the range of methods available, including sequence-based approaches (e.g., deep mutational scanning coupled with machine learning), structure-based approaches beyond AF2, and hybrid methods. The review mentions AF2's insensitivity to mutations and the AF_unmasked pipeline, but does not discuss other recent developments such as ESM-based variant effect predictors or methods specifically designed for interface mutations. The statement about the lack of large, high-quality experimental datasets is valid, but the review does not discuss emerging high-throughput approaches in sufficient detail.
- **Why it matters** Predicting the effects of mutations at PPI interfaces is directly relevant to interpreting genetic variants and designing experiments. A more comprehensive discussion of available methods and their limitations would be valuable for the readership.
- **Resolution test** Expand this section to include a broader survey of mutation effect prediction methods, including sequence-based and hybrid approaches, and discuss recent advances in high-throughput experimental measurement of mutational effects on binding.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction section
- **Evidence pointer** Introduction; location not provided
- **Issue** The introduction assumes familiarity with terms such as "coevolutionary signals," "liquid-liquid phase separation," and "intrinsically disordered regions" without defining them. While the target audience likely includes computational biologists, the review claims to address a broader readership including experimental biologists.
- **Required correction** Add brief definitions or explanations for key terms when first introduced, or provide a glossary box.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** "Key developments in computational methods for PPI modeling" section
- **Evidence pointer** Section text; location not provided
- **Issue** The description of the transition from AF2 to AF3 is brief and does not clearly explain the architectural differences beyond the replacement of the structure module with a diffusion-based model. The claim that AF3 "only processes MSA representations in the first few blocks" is stated without explaining the implications for accuracy or speed.
- **Required correction** Provide a more detailed comparison of AF2 and AF3 architectures and their respective strengths and limitations, particularly for complex prediction.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** "Useful resources" section (Table 1)
- **Evidence pointer** Table 1; location not provided
- **Issue** The table lists tools and databases but does not include some widely used resources for PPI prediction, such as InterProSurf, PPIpred, or DeepPPI. Additionally, the table does not indicate which tools are actively maintained or provide any guidance on tool selection.
- **Required correction** Consider expanding the table to include additional widely used resources, and add a brief note on tool selection criteria or limitations.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** "Biomedical applications of PPI prediction" section
- **Evidence pointer** Section text; location not provided
- **Issue** The examples of biomedical applications are presented as a list of success stories without critical discussion of the limitations or failure cases. For instance, the section on drug discovery mentions PPI modulators but does not discuss the challenges of targeting PPI interfaces with small molecules.
- **Required correction** Add a brief discussion of the limitations and challenges in translating PPI predictions to therapeutic applications.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** "Interactions between host and pathogen proteins" section
- **Evidence pointer** Section text; location not provided
- **Issue** The discussion of host-pathogen PPI prediction mentions P-HIPSTer but does not discuss other approaches, such as interolog-based methods or machine learning approaches trained on host-pathogen interaction data. The claim that "protein language models that do not explicitly utilize evolutionary information from MSAs also show promise" is not supported by specific examples.
- **Required correction** Provide specific examples of protein language model applications to host-pathogen PPI prediction and discuss their performance relative to other methods.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Completeness
- **Affected element** "Interactions related to human immune responses" section
- **Evidence pointer** Section text; location not provided
- **Issue** The discussion of TCR-pMHC interactions focuses on sequence-based methods but does not mention recent structure-based approaches that incorporate AF2/AFM for TCR-pMHC modeling, such as TCRmodel2 and tFold-TCR, which are mentioned later in the same section. The organization could be improved to avoid this redundancy.
- **Required correction** Reorganize the section to present sequence-based and structure-based methods together, with a clearer comparison of their respective strengths and limitations.

## Risk / unsupported claims
- The claim that AI-based PPI prediction accuracy is "comparable with experimental approaches" is not supported by specific quantitative comparisons and may overstate current capabilities.
- The statement that "CluPro consistently outperforms AF3" on antibody-antigen targets from CASP16 is based on the authors' own analysis, but no data are provided to support this claim.
- The claim that "higher-confidence predictions are enriched within those supported by multiple experimental methods" (referring to Burke et al.) is presented without specific metrics or effect sizes.
- The statement that AF2 "is not sensitive to mutations in query sequences" is presented as a general limitation, but the extent of this insensitivity and its variability across different protein types is not quantified.
- The assertion that "the field remains in its early stages" for IDR-mediated interaction prediction is reasonable but not supported by a systematic survey of current methods and their capabilities.
- The claim that "incorporating more physics-based ideas in AI models can be a promising future direction" is presented as a conclusion from the authors' CASP16 analysis, but the evidence for this is not presented in the text.

## Assessment against Nature-style criteria
- **Originality**: The review does not present new methods or data, but it offers a synthesis of recent developments that is reasonably current. The framing around challenges, particularly IDR-mediated interactions and immune-related PPIs, is somewhat distinctive, though similar reviews exist in the literature. The originality is moderate for a review article.
- **Scientific importance**: The topic is of high importance given the rapid adoption of AI-based methods in structural biology and the central role of PPIs in biology and medicine. The review addresses questions that are relevant to a broad community, including computational and experimental researchers.
- **Interdisciplinary readership**: The review has the potential to appeal to researchers in structural biology, bioinformatics, cell biology, immunology, and drug discovery. However, the level of technical detail in some sections may be challenging for nonspecialists, and the lack of definitions for key terms may limit accessibility.
- **Technical soundness**: The review is generally accurate in its descriptions of methods and their capabilities, but several claims are made without sufficient supporting evidence or qualification. The discussion of limitations is present but could be more critical and quantitative.
- **Readability for nonspecialists**: The writing is clear and well organized, but the review assumes familiarity with computational methods and structural biology concepts. The inclusion of a resources table is helpful, but the text would benefit from more explicit explanations of technical terms and methods.

## Recommendation posture
**Supportive if technical concerns are resolved.** The review covers a timely and important topic, is well organized, and provides a useful overview of the field. However, several claims need to be qualified or supported with specific data, and the discussion of certain challenges (particularly IDR-mediated interactions and mutation effect prediction) would benefit from greater depth. The manuscript is suitable for publication in a journal like Molecular Therapy after revisions that address the major concerns, particularly the overstatement of AI method accuracy and the lack of quantitative support for several key claims.