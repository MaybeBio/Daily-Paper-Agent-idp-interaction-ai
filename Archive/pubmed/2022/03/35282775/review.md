## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, technical soundness, and completeness of the review article as provided; no assessment of editorial fit or production quality
- **Shared manuscript claim summary** The manuscript is a review article surveying computational modeling approaches for studying physical instabilities in high-concentration biotherapeutic formulations, covering atomistic, coarse-grained, and continuum models, and their application to protein aggregation, liquid-liquid phase separation, and elevated solution viscosity. The author argues that computational models are valuable complementary tools for formulation development, particularly in early-stage drug development when material is limited, and identifies current limitations and future directions for the field.
- **Visible evidence base** Full text including abstract, introduction, four main sections (Types of protein models; Protein self-association and aggregation; Liquid-liquid phase equilibrium; Transport properties of high-concentration solution), a section on protein-protein and protein-excipient interactions, future directions, four tables, four figures, and a reference list
- **Missing materials affecting confidence** No supplementary information, no figure files (only captions and descriptions), no table data files, no author response or revision history; reference list is present but individual references were not verified for accuracy

## Reviewer
- **Overall assessment** This is a well-structured and informative review that provides a useful survey of computational approaches applied to physical instability problems in concentrated protein formulations. The author demonstrates broad knowledge of the field and organizes the material in a logical manner, progressing from model resolution levels to specific instability phenomena and then to interaction parameters. The review is particularly strong in its coverage of coarse-grained models for monoclonal antibodies and in its critical assessment of model limitations. However, the manuscript has several weaknesses that should be addressed. The treatment of some topics is uneven, with certain areas receiving substantial depth while others are only briefly mentioned. The review would benefit from a more explicit comparative framework that helps readers understand when to choose one modeling approach over another. The discussion of validation and benchmarking is somewhat repetitive across sections and could be consolidated. The future directions section is relatively brief given the breadth of challenges identified throughout the text. The figures are described but their quality and informativeness cannot be assessed from the text alone. Overall, this is a competent review that will be useful to practitioners in the field, but it does not yet fully realize its potential as a definitive guide to computational modeling for high-concentration biotherapeutic formulations.

- **Who would be interested in the results, and why** Researchers and practitioners in biopharmaceutical formulation development, particularly those working on monoclonal antibodies and other high-concentration protein therapeutics, would find this review valuable. This includes academic researchers studying protein-protein interactions, phase behavior, and rheology of concentrated protein solutions, as well as industrial scientists in pharmaceutical companies involved in formulation screening and developability assessment. Computational biophysicists interested in multiscale modeling approaches would also benefit from the survey of different model resolutions. The review is written at a level accessible to graduate students and researchers entering the field, providing a useful entry point to the literature.

- **Major strengths** 
  1. Comprehensive coverage of modeling approaches across resolution scales, from atomistic to continuum, with clear explanations of the underlying assumptions and limitations of each class of models.
  2. The organization around physical instability phenomena (aggregation, phase separation, viscosity) is effective and helps readers connect modeling approaches to specific problems.
  3. The discussion of protein-protein and protein-excipient interactions provides a useful framework for understanding how different modeling approaches relate to experimentally measurable parameters.
  4. The author provides balanced critical assessment of model limitations, avoiding overstating the predictive power of current approaches.
  5. The tables summarizing model applications and characteristics are useful reference tools.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** No
- **Axis** Comparative framework
- **Claim pointer** The review claims to provide "an overview of the different computational paradigms that have been successfully used in modeling undesirable physical behaviors of protein solutions" and to compare "these models... in the context of the physical processes and their underlying assumptions and limitations."
- **Evidence pointer** Section "Types of protein models"; Table 1; Table 2
- **Concern** While the review describes each class of models in detail, it does not provide a sufficiently explicit comparative framework to help readers understand when to choose one modeling approach over another for a given problem. The discussion of model strengths and limitations is distributed throughout the text, but there is no consolidated comparison that addresses questions such as: For a given protein size and instability phenomenon, what is the most appropriate model resolution? How do the computational costs compare quantitatively? What is the trade-off between accuracy and speed for different approaches? The tables provide some comparative information, but they are primarily descriptive rather than prescriptive.
- **Why it matters** A key value of a review article is to help readers navigate the landscape of available methods and make informed choices. Without an explicit comparative framework, readers may struggle to determine which modeling approach is most suitable for their specific problem, particularly those new to the field.
- **Resolution test** Add a dedicated section or subsection that provides a decision framework or flowchart for selecting modeling approaches based on the research question, protein system, and available computational resources. Include quantitative comparisons of computational cost where possible, and provide explicit guidance on when each class of model is most appropriate.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Validation and benchmarking
- **Claim pointer** The review states that "many of the shortcomings of existing computational models are discussed, providing perspectives and possible directions toward an efficient computational framework for designing effective protein formulations." The future directions section identifies "the lack of benchmarking of existing computational models against diverse experimental data sets" as "the most pressing limitation."
- **Evidence pointer** Section "Future directions"; Table 4
- **Concern** The review identifies the lack of benchmarking as the most pressing limitation but does not provide a systematic analysis of the existing benchmarking efforts or lack thereof. While individual model descriptions mention validation against experimental data, there is no consolidated discussion of what benchmarking has been done, what data sets are available, what gaps exist, and what a comprehensive benchmarking effort would look like. The author mentions that models are "borrowed or adapted from other fields" and that "such models and their corresponding force fields are unable to accurately capture the behavior of proteins in pharmaceutically relevant conditions," but this important point is not developed in sufficient detail.
- **Why it matters** The credibility of computational models for formulation development depends on their validation against experimental data. A review that identifies benchmarking as the most pressing limitation should provide a more detailed analysis of the current state of validation, including specific examples of successful and unsuccessful model predictions, and a roadmap for addressing the benchmarking gap.
- **Resolution test** Add a subsection that systematically reviews the benchmarking status of each class of model, including specific examples of model predictions compared to experimental data, identification of data gaps, and a proposed framework for community-wide benchmarking efforts.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Depth and currency of coverage
- **Claim pointer** The review claims to provide "a survey of the state-of-art of the in-silico application of a wide-range of computational models for effectively studying physical instabilities in protein solutions within the context of concentrated conditions."
- **Evidence pointer** Section "Types of protein models"; Section "Protein self-association and aggregation"; Section "Liquid-liquid phase equilibrium"; Section "Transport properties of high-concentration solution"
- **Concern** The coverage of some topics is uneven. The sections on coarse-grained models and their application to monoclonal antibodies are well developed, reflecting the author's expertise. However, the treatment of atomistic simulations is relatively brief given their importance in providing molecular-level detail, and the discussion of machine learning approaches is limited to brief mentions in the context of specific studies. Given the rapid growth of machine learning applications in protein science, a more substantial discussion of these emerging approaches would strengthen the review. Additionally, the review does not discuss recent advances in enhanced sampling techniques in sufficient depth, despite their importance for studying protein-protein interactions.
- **Why it matters** A review claiming to survey the state of the art should provide balanced coverage of all major approaches. The uneven treatment may lead readers to underestimate the potential of approaches that are not discussed in depth, and may not fully capture the current landscape of computational methods in this field.
- **Resolution test** Expand the discussion of atomistic simulation approaches, particularly recent advances in enhanced sampling and their application to concentrated protein systems. Add a more substantial discussion of machine learning and artificial intelligence approaches, including their current applications and potential future contributions to the field.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Practical guidance
- **Claim pointer** The review states that computational models "can help design biologic drug formulations by: (1) constraining the formulation space to be experimentally investigated; (2) providing understanding of the underlying mechanisms for the different instability processes; and/or (3) identifying the mechanisms by which different solution components (or excipients) modulate protein behavior in the formulation."
- **Evidence pointer** Section "Introduction"; Section "Future directions"
- **Concern** While the review describes what computational models can do, it provides limited practical guidance on how to implement these models in a formulation development workflow. The author does not discuss practical considerations such as software availability, input data requirements, expertise needed, or typical timelines for different types of simulations. The review would benefit from a more explicit discussion of how computational modeling integrates with experimental formulation development, including case studies or examples of successful implementation.
- **Why it matters** For the review to have impact beyond the computational modeling community, it needs to provide practical guidance for formulation scientists who may be considering using these tools. Without such guidance, the review may be seen as primarily descriptive rather than actionable.
- **Resolution test** Add a section or subsection that provides practical guidance for implementing computational modeling in formulation development, including discussion of software tools, data requirements, integration with experimental workflows, and case studies of successful applications.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 1
- **Evidence pointer** Figure 1 caption
- **Issue** The figure caption describes a representation of computational protein models at different resolution levels using an IgG2 mAb as an example. However, the figure itself is not visible in the provided text, and the caption alone does not convey sufficient information about the visual content. The description of the arrow indicating the direction of increasing resolution is helpful, but it is unclear what specific features of each model representation are being illustrated.
- **Required correction** Ensure that the figure clearly illustrates the key features of each model resolution level, such as the number of beads, the level of structural detail, and the representation of solvent. Consider adding labels or annotations to highlight the key differences between model types.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 2
- **Evidence pointer** Figure 2 caption
- **Issue** The figure caption describes a schematic representation of the generalized protein aggregation mechanism. The caption mentions reversible and irreversible steps, but it is not clear from the caption alone how these are visually distinguished in the figure. The description of the pathway is clear, but the visual representation cannot be assessed.
- **Required correction** Ensure that the figure clearly distinguishes between reversible and irreversible steps, for example through the use of different arrow types or colors. Consider adding a legend to explain the visual conventions used.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 3
- **Evidence pointer** Figure 3 caption
- **Issue** The figure caption describes a generic phase diagram for globular proteins. The caption mentions the solubility, binodal, and gelation curves, but it is not clear how these are visually distinguished in the figure. The redrawing from reference 166 is noted, but the specific features of the diagram cannot be assessed from the caption alone.
- **Required correction** Ensure that the figure clearly labels the solubility, binodal, and gelation curves, and that the regions corresponding to different phases are clearly identified. Consider adding a legend or annotations to explain the key features.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 4
- **Evidence pointer** Figure 4 caption
- **Issue** The figure caption describes an illustrative example of protein-excipient interactions calculated by the preferential interaction parameter. The caption mentions three panels showing interactions with different excipients, but the color coding and the specific features being illustrated cannot be assessed from the caption alone.
- **Required correction** Ensure that the figure clearly shows the protein structure and the distribution of preferential interaction parameter values on the protein surface. Consider adding a color scale or legend to explain the color coding.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Section "Protein self-association and aggregation"; Section "Liquid-liquid phase equilibrium"
- **Evidence pointer** Section headings and text
- **Issue** The review uses the term "liquid-liquid phase equilibrium" in the section heading but uses "liquid-liquid phase separation" (LLPS) throughout the text. While these terms are related, they are not identical, and the inconsistency may cause confusion.
- **Required correction** Use consistent terminology throughout the manuscript. Either use "liquid-liquid phase separation" in the section heading or define the relationship between the two terms early in the section.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Reference currency
- **Affected element** Reference list
- **Evidence pointer** Reference list
- **Issue** The review was published in 2022, and the most recent references appear to be from around 2021. Given the rapid pace of development in computational methods, particularly in machine learning applications, the review may miss some very recent advances.
- **Required correction** Consider adding references from 2021 and 2022 where relevant, particularly in the discussion of machine learning approaches and emerging multiscale modeling methods.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Clarity of scope
- **Affected element** Section "Types of protein models"
- **Evidence pointer** Section text
- **Issue** The review focuses on classical modeling studies and explicitly excludes quantum mechanical representations and statistical approaches. However, the rationale for these exclusions is not fully explained, and some readers may wonder whether these approaches have any relevance to the problems discussed.
- **Required correction** Briefly explain why quantum mechanical and statistical approaches are excluded from the review, and note whether they have any potential applications to the physical instability problems discussed.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Discussion of experimental validation
- **Affected element** Section "Protein self-association and aggregation"; Section "Liquid-liquid phase equilibrium"; Section "Transport properties of high-concentration solution"
- **Evidence pointer** Section text
- **Issue** While the review discusses the ability of models to predict experimental outcomes, it does not consistently discuss the quality of agreement between model predictions and experimental data. For some models, the text mentions that they "fit" or "reproduce" experimental data, but the degree of agreement is not always quantified or critically assessed.
- **Required correction** Where possible, provide quantitative information about the agreement between model predictions and experimental data, and critically assess the strengths and limitations of each model in terms of predictive accuracy.

## Risk / unsupported claims
- The claim that "computational models can help design biologic drug formulations" is presented as a general statement but is not supported by specific case studies or quantitative evidence of successful implementation in formulation development workflows.
- The statement that "even for proteins sharing a high level of homology between each other (e.g., mAbs of the same isotype), the effects of an excipient, for instance, might drastically vary from one protein to another" is presented as a conclusion but is not supported by specific examples or references in the text.
- The claim that "the lack of benchmarking of existing computational models against diverse experimental data sets" is "the most pressing limitation" is asserted but not systematically demonstrated through a review of existing benchmarking efforts.
- The statement that "novel and clever approaches need to be developed or adapted to reduce the computational burden for assessing LLPS" is speculative and not supported by a detailed analysis of the computational bottlenecks.
- The claim that machine learning approaches combined with computational models can address the limitations of current approaches is mentioned but not developed with specific examples or evidence of success.