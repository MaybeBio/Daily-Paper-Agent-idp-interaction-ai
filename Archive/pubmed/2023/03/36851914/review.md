## Review setup
- **Input scope** Full manuscript text including abstract, introduction, historical overview, predictor descriptions, summary, funding, and authorship statements.
- **Assessment boundary** Assessment is limited to the content provided in the manuscript. No external data, code, or supplementary materials were available for verification.
- **Shared manuscript claim summary** The manuscript presents a systematic survey of 38 computational predictors of intrinsically disordered binding regions, covering MoRFs, SLiMs, protein-, nucleic acid-, and lipid-binding IDRs. It provides a historical perspective, categorizes predictors by architecture and target, analyzes availability and citation impact, and offers recommendations for future development.
- **Visible evidence base** Table 1 (predictor list with architecture, availability, URLs, citations), Figure 1 (timeline), and narrative descriptions of predictor architectures and historical events.
- **Missing materials affecting confidence** No supplementary data files, no detailed methodology for the literature search and citation analysis, no raw citation data, no validation of the availability checks beyond the authors' statement, and no access to the referenced predictors or their documentation.

## Reviewer
- **Overall assessment** This is a well-organized and informative survey of computational predictors for disordered binding regions. The authors have compiled a comprehensive list of 38 methods, categorized them logically, and provided useful historical context. The analysis of availability and citation impact is a valuable contribution. However, the manuscript lacks methodological detail regarding the literature search and citation analysis, and some claims about predictor performance and future directions are made without direct evidence. The survey is timely and will be of interest to researchers in the intrinsically disordered protein field.
- **Who would be interested in the results, and why** Researchers developing or using computational tools for predicting intrinsically disordered regions and their binding functions. This includes computational biologists, bioinformaticians, and experimentalists studying IDPs/IDRs in the context of protein-protein interactions, signaling, and disease. The availability and impact analysis is also relevant to tool developers and funding agencies interested in the sustainability of bioinformatics resources.
- **Major strengths** 1. Comprehensive coverage of 38 predictors, including recent deep learning-based methods. 2. Clear categorization by target type and predictive architecture. 3. Historical timeline (Figure 1) provides useful context for the field's evolution. 4. Analysis of tool availability and its correlation with citation impact is a practical and under-discussed topic. 5. Recommendations for future development are sensible and grounded in the observed trends.
- **Major Concerns** 1. The methodology for the literature search and predictor identification is not described in sufficient detail, limiting reproducibility. 2. The claim that deep learning models will likely improve predictive performance is speculative and not directly supported by evidence presented in this manuscript. 3. The analysis of citation impact, while interesting, is based on a single time point and does not account for potential confounding factors beyond availability. 4. The manuscript does not provide a critical comparison of predictor accuracy beyond referencing the CAID experiment, which limits its value for users choosing among tools.
- **Minor Comments** 1. The abstract could more clearly state the number of predictors surveyed and the key findings regarding availability. 2. Some predictor descriptions are brief; additional detail on input features and training data for the most popular tools would be helpful. 3. The discussion of CAID results could be expanded to give readers a better sense of the state of the art in terms of accuracy. 4. The figure caption for Figure 1 could be more descriptive. 5. The manuscript would benefit from a table summarizing the key recommendations.
- **Technical failings that need to be addressed before the case is established** 1. The literature search methodology is not described (databases, search terms, inclusion/exclusion criteria, date of search). 2. The citation analysis methodology is not described (exact date of data collection, handling of self-citations, statistical tests used). 3. The claim about the relationship between availability and citations is based on descriptive statistics only; no statistical analysis is presented.
- **Assessment against Nature-style criteria**  
  *Originality*: Moderate. The survey is not the first on this topic, but it is more comprehensive and up-to-date than previous reviews, and the focus on availability and impact is a novel angle.  
  *Scientific importance*: Moderate to high. The topic is relevant to a growing community of researchers studying IDPs, and the survey provides a useful resource. However, the manuscript does not present new experimental or computational results that would fundamentally advance the field.  
  *Interdisciplinary readership*: Moderate. The topic is of interest to computational biologists, bioinformaticians, and structural biologists, but the manuscript is unlikely to attract readers from outside these fields.  
  *Technical soundness*: The survey appears to be accurate based on the information provided, but the lack of methodological detail for the literature search and citation analysis prevents full verification.  
  *Readability for nonspecialists*: The manuscript is generally well-written and accessible, but some sections assume familiarity with the IDP field and machine learning terminology.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript provides a valuable and timely survey, but the methodology for the literature search and citation analysis must be described in detail to allow reproducibility and verification. The speculative claim about deep learning should be tempered or supported with evidence.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodology transparency
- **Claim pointer** The authors claim to have performed an "exhaustive literature search" to identify 38 predictors of binding IDRs.
- **Evidence pointer** Section "Historical overview", location not provided
- **Concern** The methodology for the literature search is not described. The authors do not specify which databases were searched, what search terms were used, what inclusion and exclusion criteria were applied, or how the search was validated for completeness.
- **Why it matters** Without a clear methodology, the claim of an "exhaustive" search cannot be verified, and the completeness of the predictor list is uncertain. This is a fundamental issue for a survey paper, as the value of the manuscript depends on the comprehensiveness and reproducibility of the search.
- **Resolution test** The authors should add a subsection describing the literature search methodology in detail, including databases, search terms, time period, and inclusion/exclusion criteria. They should also describe how they validated the completeness of their search (e.g., by cross-referencing with other reviews or databases).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence support for claims
- **Claim pointer** The authors state that "the recent influx of the deep learning-based predictors of binding IDRs will likely result in improved predictive quality" and that "deep learning models in general produce more accurate disorder predictions when compared to the shallow ML models."
- **Evidence pointer** Section "Predictive architectures", location not provided
- **Concern** The claim that deep learning will improve predictive quality is presented as a likely outcome, but no direct evidence is provided within this manuscript to support this for binding IDR prediction specifically. The authors cite a recent study on disorder prediction, but this is a related, not identical, task. The CAID results discussed earlier in the manuscript do not include deep learning-based methods for binding IDR prediction, so the claim is speculative.
- **Why it matters** This claim is used to justify a key recommendation for future development. If it is not well-supported, the recommendation is weakened. Readers may also be misled into expecting that deep learning methods will automatically outperform existing tools.
- **Resolution test** The authors should either provide direct evidence (e.g., from the CAID2 results or a comparative benchmark) that deep learning methods improve binding IDR prediction, or temper the claim to reflect that this is a hypothesis based on trends in related areas.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Analysis rigor
- **Claim pointer** The authors claim that "providing implementations and webservers results in much higher rates of citations/use" and that "methods which are more broadly available, as both webserver and source code, are substantially more cited/used."
- **Evidence pointer** Section "Availability and impact", Table 1
- **Concern** The citation analysis is based on descriptive statistics (medians) without any statistical testing. The authors do not control for potential confounding factors such as the age of the method, the popularity of the authors, or the venue of publication. The analysis is also based on a single time point (July 2022), which may not be representative.
- **Why it matters** The claim about availability and impact is a key finding of the manuscript and is used to support recommendations. Without statistical rigor, the claim is not fully substantiated and could be misleading.
- **Resolution test** The authors should perform a statistical analysis (e.g., a Mann-Whitney U test or a regression model) to test the significance of the difference in citations between available and unavailable methods, and ideally control for confounding factors such as publication year and venue.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract does not explicitly state the number of predictors surveyed (38) or the key finding regarding availability and citations.
- **Required correction** Add a sentence to the abstract stating the number of predictors surveyed and the main finding regarding availability and impact.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Figure 1
- **Evidence pointer** Figure 1
- **Issue** The figure caption is brief and does not fully explain the color coding and the significance of the "major events" callouts.
- **Required correction** Expand the figure caption to explain the color coding and the significance of the events highlighted.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Balance
- **Affected element** Section "Predictors of protein, RNA, DNA and lipid-binding regions"
- **Evidence pointer** Section "Predictors of protein, RNA, DNA and lipid-binding regions"
- **Issue** The descriptions of the predictors in this section are uneven, with some tools (e.g., ANCHOR2) receiving more detail than others. This may reflect the authors' familiarity but could be seen as biased.
- **Required correction** Provide more balanced descriptions of the predictors, or explicitly state that the level of detail reflects the availability of information in the original publications.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section "Predictive architectures"
- **Evidence pointer** Section "Predictive architectures"
- **Issue** The section on predictive architectures is dense and may be difficult for nonspecialists to follow, particularly the descriptions of deep learning architectures.
- **Required correction** Consider adding a brief explanation of key deep learning concepts (e.g., convolutional and recurrent networks) for nonspecialist readers.

## Risk / unsupported claims
- The claim that deep learning models will likely improve predictive quality of binding IDR predictors is speculative and not directly supported by evidence in this manuscript.
- The claim that availability of implementations and webservers results in higher citation rates is based on descriptive statistics without statistical testing or control for confounding factors.
- The statement that "the CAID experiment evaluated 11 predictors of disordered binding regions" is presented as fact, but the details of this evaluation are not provided, and the authors do not discuss the accuracy of these predictors in detail.
- The claim that "there are no predictors for the protean regions" is a negative claim that is difficult to verify and may become outdated quickly.
- The authors' statement that "the recent influx of the deep learning-based predictors of binding IDRs will likely result in improved predictive quality" is presented as a likely outcome, but no direct evidence is provided within this manuscript to support this for binding IDR prediction specifically.