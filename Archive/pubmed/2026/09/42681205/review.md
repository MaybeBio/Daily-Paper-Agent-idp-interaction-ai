## Review setup
- **Input scope** Full manuscript (Methods in Molecular Biology chapter)
- **Assessment boundary** The manuscript describes the DisoRDPbind web server for predicting RNA-binding intrinsically disordered regions (IDRs), including its model, performance, usage instructions, and a case study on the HCV core protein.
- **Shared manuscript claim summary** The authors present DisoRDPbind as one of the first tools for predicting RNA-binding IDRs, highlighting its ease of use, small computational footprint suitable for proteome-scale predictions, and its utility in studying RNA chaperones, as demonstrated by a case study on the HCV core protein.
- **Visible evidence base** The manuscript text, including descriptions of the predictive model, performance metrics from the CAID experiment, web server interface instructions, and a case study example.
- **Missing materials affecting confidence** No supplementary data, code, or detailed performance tables/figures are provided. The manuscript is a methods chapter, not a primary research article, so the evidence base is limited to the authors' description and references to prior work.

## Reviewer
- **Overall assessment** This manuscript provides a practical guide to using the DisoRDPbind web server for predicting RNA-binding IDRs. The tool addresses a niche but important gap in the field, and the description of its use is clear. However, the manuscript lacks a critical evaluation of the tool's limitations, a comparison with other available methods, and a rigorous demonstration of its utility beyond the single case study. The claims about performance and utility are not fully substantiated within the manuscript itself, relying heavily on external references.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, RNA biology, and RNA chaperones would be interested. The tool provides a convenient way to generate hypotheses about RNA-binding IDRs, which is a relatively under-served area in computational biology. The chapter format makes it accessible to experimentalists who may not be familiar with bioinformatics tools.
- **Major strengths** The manuscript addresses a clear need for tools that predict RNA-binding IDRs, a function that is less commonly targeted than protein-binding IDRs. The web server is described as easy to use and computationally efficient, which are practical advantages. The case study on the HCV core protein provides a concrete example of the tool's potential application.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Evidence and Support
    - **Claim pointer** The authors claim that DisoRDPbind is "one of the first tools designed to predict RNA-binding IDRs" and that it has a "small computational footprint" allowing for "large/proteome-scale predictions."
    - **Evidence pointer** Section: "We focus on one of the first tools designed to predict RNA-binding IDRs: DisoRDPbind." and "We highlight the small computational footprint of DisoRDPbind, which allows for large/proteome-scale predictions."
    - **Concern** The manuscript does not provide any quantitative evidence to support these claims. No runtime benchmarks, no comparison of the number of sequences that can be processed, and no demonstration of a proteome-scale prediction are presented. The claim of being "one of the first" is not contextualized with a literature survey of other tools.
    - **Why it matters** These are central claims about the tool's novelty and utility. Without supporting data, the reader cannot assess whether DisoRDPbind is indeed a practical choice for large-scale studies or how it compares to other existing or emerging methods.
    - **Resolution test** Provide quantitative data: (1) a table or figure showing runtime vs. number of sequences, (2) a brief comparison with other available tools for RNA-binding IDR prediction (e.g., listing them and their features), and (3) a concrete example of a proteome-scale prediction (e.g., number of proteins processed, total runtime, output size).

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Evidence and Support
    - **Claim pointer** The authors state that the predictive performance was "recently measured in the second CAID experiment."
    - **Evidence pointer** Section: "We describe the predictive model employed by DisoRDPbind and discuss its predictive performance and runtime, which were recently measured in the second CAID (Critical Assessment of protein Intrinsic Disorder) experiment."
    - **Concern** The manuscript does not present the actual performance metrics (e.g., AUC, precision, recall, F1-score) from the CAID experiment. The reader is left to trust the authors' summary without seeing the data. Furthermore, the context of the CAID experiment (e.g., what other methods were compared, what datasets were used) is not provided.
    - **Why it matters** Performance is a critical aspect of any predictive tool. Without presenting the actual numbers, the reader cannot evaluate the reliability of DisoRDPbind's predictions. This is a fundamental omission for a methods chapter.
    - **Resolution test** Include a table or figure summarizing the key performance metrics from the CAID experiment (e.g., AUC, MCC, F1-score) for DisoRDPbind and, ideally, for a few other top-performing methods for context. Cite the CAID paper and briefly describe the benchmark dataset.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scope and Generalizability
    - **Claim pointer** The authors present a case study of an RNA chaperone, HCV core protein, to "illustrate the method's utility in studying RNA chaperones."
    - **Evidence pointer** Section: "While DisoRDPbind does not identify RNA chaperones directly, we present a case study of an RNA chaperone, HCV core protein, to illustrate the method's utility in studying RNA chaperones."
    - **Concern** The case study is presented as an illustration, but it is not clear how the prediction results from DisoRDPbind were validated or interpreted in the context of RNA chaperone function. The manuscript does not show whether the predicted RNA-binding IDRs correspond to known functional regions of the HCV core protein or whether the predictions led to any new biological insight.
    - **Why it matters** The case study is meant to demonstrate the tool's practical value. Without a clear link between the prediction and biological function, the example is merely a demonstration of the tool's output, not a validation of its utility for studying RNA chaperones.
    - **Resolution test** Strengthen the case study by: (1) showing the predicted RNA-binding IDRs on a sequence or structure of the HCV core protein, (2) comparing these predictions to known functional regions (e.g., from literature), and (3) discussing how these predictions could guide future experiments (e.g., mutagenesis, binding assays).

- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity and Presentation
    - **Affected element** Web server instructions
    - **Evidence pointer** Section: "We detail how to use the web server interface of DisoRDPbind and provide an example to illustrate how to read and interpret its prediction results."
    - **Issue** The instructions for using the web server are described in text, but no screenshots or figures of the interface are provided. This makes it harder for a reader to follow the steps.
    - **Required correction** Include at least one screenshot of the web server input page and one of the output page, with annotations to guide the reader.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Completeness
    - **Affected element** Model description
    - **Evidence pointer** Section: "We describe the predictive model employed by DisoRDPbind."
    - **Issue** The description of the predictive model is likely too brief for a methods chapter. The reader needs to understand the input features, the algorithm (e.g., is it a classifier? what type?), and how the model was trained.
    - **Required correction** Expand the model description to include: (1) the type of features used (e.g., sequence composition, predicted disorder, evolutionary information), (2) the machine learning algorithm (e.g., random forest, SVM), and (3) the training dataset (e.g., number of proteins, source).

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Reproducibility
    - **Affected element** Web server availability
    - **Evidence pointer** Section: "DisoRDPbind is available as an easy-to-use web server at http://biomine.cs.vcu.edu/servers/DisoRDPbind/."
    - **Issue** The URL should be verified to be active and functional. It is also good practice to mention if the server is expected to be maintained long-term and if the source code or a standalone version is available.
    - **Required correction** Confirm the URL is active. Add a statement about the expected maintenance period and whether a standalone version or source code is available for local use.

- **Technical failings that need to be addressed before the case is established** R1-M1 (lack of quantitative evidence for computational footprint and novelty), R1-M2 (lack of presented performance metrics from CAID).
- **Assessment against Nature-style criteria** 
    - **Originality:** Low. The tool itself is not new (it was previously published), and the manuscript is a methods chapter, not a primary research article. The originality lies in the practical guide format.
    - **Scientific importance:** Moderate. The topic of RNA-binding IDRs is important, but the manuscript does not provide new scientific insights. Its value is in making an existing tool more accessible.
    - **Interdisciplinary readership:** Low. The manuscript is targeted at a specialized audience of computational and molecular biologists working on IDPs and RNA biology.
    - **Technical soundness:** Not fully established. The claims about performance and computational efficiency are not supported by data within the manuscript.
    - **Readability for nonspecialists:** Good. The writing is clear and the instructions are easy to follow, though the model description could be more detailed.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript is a useful practical guide, but it fails to provide the necessary quantitative evidence to support its central claims about the tool's performance and utility. The authors should add performance data, runtime benchmarks, and a more rigorous case study to make the chapter self-contained and convincing.

## Risk / unsupported claims
- The claim that DisoRDPbind is "one of the first tools" for RNA-binding IDR prediction is unsupported without a literature survey.
- The claim of a "small computational footprint" allowing for "proteome-scale predictions" is unsupported without runtime benchmarks.
- The claim that the tool's performance was measured in the CAID experiment is unsupported without presenting the actual metrics.
- The claim that the case study illustrates the method's utility in studying RNA chaperones is unsupported without a clear link between predictions and biological function.