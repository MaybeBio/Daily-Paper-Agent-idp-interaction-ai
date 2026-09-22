## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, conclusions, acknowledgments) as provided; figures and supplementary materials referenced but not included.
- **Assessment boundary** Evaluation of the scientific claims, methodological soundness, and presentation quality based solely on the supplied text. No external verification of data, code, or database entries was performed.
- **Shared manuscript claim summary** The authors propose that the Energy Landscape Visualization Method (ELViM), a multidimensional projection tool based on internal coordinates, can be applied to ensembles of intrinsically disordered proteins (IDPs) obtained from the Protein Ensemble Database (PED). They claim that ELViM enables validation of ensembles, detection of sampling inconsistencies, identification of prevalent conformations (via Local Conformational Signatures, LCSs), and comparative analysis of ensembles generated under different conditions, even when average experimental observables such as radius of gyration are similar.
- **Visible evidence base** Text descriptions of results for four IDP systems (NUS, NUL, Sic1, SH3 domain of Drk), including qualitative statements about density distributions, LCSs, and reproducibility analyses. References to Figures 1–4 and Supplementary Figures S1–S7, none of which were provided.
- **Missing materials affecting confidence** All figures and supplementary materials; detailed methods for ensemble generation (referenced to prior work); quantitative metrics for density estimation, LCS selection, and reproducibility; code version and parameters used for ELViM projections; raw data or statistical analyses supporting qualitative claims.

## Reviewer
- **Overall assessment** This manuscript presents a proof-of-concept application of an existing visualization method (ELViM) to IDP ensembles from a public database. The core idea is potentially useful for the IDP community, as it addresses a real need for tools that can compare heterogeneous conformational ensembles without predefined reaction coordinates. However, the current manuscript is largely descriptive and lacks quantitative validation. The central claims, such as the ability to detect sampling inconsistencies or distinguish ensembles with similar average properties, are supported only by qualitative visual inspection of figures that were not available for review. The methodological novelty is limited, as ELViM has been previously published and applied to other biomolecular systems. The manuscript would benefit from a more rigorous, quantitative demonstration of what ELViM adds beyond existing tools, and from clearer articulation of the biological or biophysical insights gained.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins and regions, particularly those working on conformational ensembles, integrative structural biology, and energy landscape theory. The work may also interest method developers in computational biophysics who seek tools for visualizing and comparing high-dimensional conformational data. The potential to integrate ELViM with other approaches, such as AlphaFold, could attract a broader computational biology audience.
- **Major strengths** The manuscript addresses a relevant and timely problem: the lack of general frameworks for comparing IDP ensembles. The use of ELViM, which relies on internal coordinates and avoids the need for reference structures, is conceptually appealing. The selection of four diverse IDP systems from PED provides a reasonable test set. The authors also include reproducibility analyses, which is commendable. The writing is generally clear and accessible.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The authors claim that ELViM "enables comprehensive validation of ensembles, facilitating the detection of potential inconsistencies in the sampling process" and that it "can distinguish different ensembles even if the ensembles fit the same averaged experimental data, such as the radius of gyration."
  - **Evidence pointer** Results section, Figures 1–4; location not provided for specific figure panels.
  - **Concern** The central claims are based entirely on visual inspection of density plots and LCSs in figures that were not provided. No quantitative metrics are presented to support the assertion that ELViM detects sampling inconsistencies or distinguishes ensembles with similar Rg values. For example, the authors note that NUS ensembles have similar average Rg values, but no statistical comparison of the density distributions or conformational populations is given. Without quantitative evidence, the claims remain anecdotal.
  - **Why it matters** The stated advantage of ELViM over existing methods hinges on its ability to reveal differences that average observables miss. If this cannot be demonstrated rigorously, the manuscript does not establish a clear advance over current practice.
  - **Resolution test** Provide quantitative analyses, such as overlap metrics between ensemble density distributions, statistical tests comparing conformational populations in different regions of the ELViM projection, or comparison of ELViM results with those from established dimensionality reduction or clustering methods. Figures must be made available for review.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Methodological transparency
  - **Claim pointer** The authors state that "ELViM, a methodology that circumvents the need for a priori reaction coordinates, aids in analyzing the ensembles" and that LCSs are identified by "manually selecting all conformations within a high-density region and finding the centroid conformation."
  - **Evidence pointer** Methods section, ELViM subsection; location not provided.
  - **Concern** The LCS identification procedure is described as "manual," which introduces subjectivity and limits reproducibility. The criteria for selecting high-density regions, the bandwidth selection for the Gaussian KDE, and the threshold for defining a "dense region" are not specified. Additionally, the ELViM projection is stochastic, and while reproducibility is mentioned, no quantitative measure of projection stability is provided.
  - **Why it matters** For a method to be adopted by the community, it must be reproducible and objective. Manual selection undermines the claim that ELViM provides a systematic procedure. The lack of detail on parameters and stability prevents others from applying the method reliably.
  - **Resolution test** Describe an automated or semi-automated procedure for LCS identification, provide the KDE bandwidth values used for each system, and quantify projection reproducibility (e.g., via Procrustes analysis or similar) across multiple runs.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Comparative benchmarking
  - **Claim pointer** The authors state that "It is difficult to compare ELViM with other analogous approaches" and that "traditional quality metrics primarily gauge the optimization procedure's efficiency, falling short in quantifying how effectively the protein conformational space is depicted."
  - **Evidence pointer** Conclusions section; location not provided.
  - **Concern** The manuscript does not include any comparison of ELViM with existing dimensionality reduction or ensemble comparison methods, such as principal component analysis, t-SNE, UMAP, or the approaches cited in references 29–35. The authors acknowledge this difficulty but do not attempt to address it. Without a benchmark, it is unclear whether ELViM offers advantages over existing tools.
  - **Why it matters** The claim that ELViM is a "powerful tool" for IDP ensemble analysis requires evidence that it performs at least as well as, or better than, existing methods. The absence of any comparative analysis weakens the case for its adoption.
  - **Resolution test** Include a comparison of ELViM with at least one or two established methods on the same datasets, using quantitative metrics such as preservation of pairwise distances, clustering accuracy, or ability to recover known conformational states.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity of presentation
  - **Affected element** Abstract and Introduction
  - **Evidence pointer** Abstract, first sentence; Introduction, first paragraph.
  - **Issue** The phrase "a substantial portion of various organisms' proteomes" is vague. A specific range or citation would strengthen the opening.
  - **Required correction** Provide a quantitative statement (e.g., "30–50% of eukaryotic proteomes") with appropriate references.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility of methods
  - **Affected element** Methods, ELViM subsection
  - **Evidence pointer** Methods section, ELViM subsection; location not provided.
  - **Issue** The equation for dissimilarity is mentioned but not shown in the provided text. The parameters σ₀ and ε are given, but the normalization constant Np is not defined.
  - **Required correction** Include the full equation and define all variables, including Np.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Statistical rigor
  - **Affected element** Results, NUS and NUL sections
  - **Evidence pointer** Results section, NUS and NUL subsections; location not provided.
  - **Issue** The authors state that "each ensemble exhibits a unique distribution" and that "the densest regions vary among the different ensembles," but no statistical tests are reported to support these statements.
  - **Required correction** Add quantitative measures of distribution similarity or difference, such as Jensen-Shannon divergence or a permutation test, to support the qualitative descriptions.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Completeness of figure descriptions
  - **Affected element** Results, all subsections
  - **Evidence pointer** Figures 1–4; location not provided.
  - **Issue** The text refers to LCSs with labels (e.g., i, ii, vii) and describes their properties, but without the figures, it is impossible to assess whether the descriptions match the visual data.
  - **Required correction** Ensure that figure captions are self-explanatory and that all LCS labels are clearly marked in the figures. Consider adding a supplementary table summarizing the properties of each LCS.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Future directions
  - **Affected element** Conclusions
  - **Evidence pointer** Conclusions, final paragraph.
  - **Issue** The suggestion to integrate ELViM with AlphaFold is intriguing but speculative. No details are given on how this integration would work.
  - **Required correction** Either expand on this idea with a concrete proposal or remove it to avoid overreach.

## Technical failings that need to be addressed before the case is established
- R1-M1: Lack of quantitative evidence for the central claims of ensemble distinction and sampling inconsistency detection.
- R1-M2: Subjective and under-specified LCS identification procedure, with no quantitative reproducibility metrics.
- R1-M3: No comparative benchmarking against existing methods.

## Risk / unsupported claims
- The claim that ELViM "enables comprehensive validation of ensembles" is unsupported without quantitative validation metrics.
- The claim that ELViM "can distinguish different ensembles even if the ensembles fit the same averaged experimental data" is not substantiated by the provided evidence.
- The assertion that "high-density regions typically correspond to minima in the free energy landscape" is presented as a general statement but is not justified for the specific ensembles analyzed, especially given that the ensembles were generated with biases from experimental restraints.
- The statement that "ELViM proves to be a valuable tool in the study of intrinsically disordered proteins" is a conclusion that requires stronger evidence than the descriptive results presented.

## Assessment against Nature-style criteria
- **Originality** Moderate. The application of ELViM to IDP ensembles from PED is a new use case, but the method itself is previously published. The conceptual advance is incremental rather than transformative.
- **Scientific importance** Moderate. The problem of comparing IDP ensembles is important, but the manuscript does not yet demonstrate that ELViM provides a significant advantage over existing approaches. The potential for broad impact exists but is not realized in the current form.
- **Interdisciplinary readership** Limited. The work is primarily of interest to computational biophysicists and IDP researchers. The presentation assumes familiarity with energy landscape theory and multidimensional projection methods, which may limit accessibility to a broader readership.
- **Technical soundness** Weak. The lack of quantitative analysis, subjective LCS selection, and absence of benchmarking undermine the technical rigor. The stochastic nature of the projection is acknowledged but not adequately characterized.
- **Readability for nonspecialists** Acceptable. The writing is clear, but the abstract and introduction could be more accessible with additional context on why IDP ensembles are challenging to study. The methods section is too brief for reproducibility.

## Recommendation posture
Currently not established from the provided evidence. The manuscript presents a promising idea but lacks the quantitative rigor and comparative analysis needed to support its claims. I would be supportive if the authors address the major concerns, particularly by providing quantitative validation, automating the LCS identification, and benchmarking against existing methods.