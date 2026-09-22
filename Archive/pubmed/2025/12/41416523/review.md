## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion) without figures, tables, or supplementary materials
- **Assessment boundary** Scientific claims, experimental design, methodological rigor, and logical coherence as presented in the text; visual data (figures, gels, microscopy images) not assessable
- **Shared manuscript claim summary** The authors propose that MBD2 acts as a phase separation scaffold protein for pericentric heterochromatin, organizing heterochromatin compartmentalization and composition through liquid-liquid phase separation, and that this process modulates histone acetylation states by recruiting and excluding specific proteins
- **Visible evidence base** Text descriptions of quantitative spatial proteomics, in vitro phase separation assays, machine learning-based prediction tools, AlphaFold structure predictions, co-immunoprecipitation, fluorescence microscopy, and functional assays in C2D12 and ES cells
- **Missing materials affecting confidence** All figures, supplementary figures, supplementary tables, movies, raw mass spectrometry data, and statistical analysis details; exact numerical values for key experiments; gating strategies and controls for imaging experiments

## Reviewer
- **Overall assessment** This manuscript presents a systematic approach to identify phase separation scaffold proteins in heterochromatin, with a focus on MBD2. The integration of multiple methodologies is commendable, and the identification of MBD2 as a candidate scaffold is plausible. However, the manuscript has several significant weaknesses. The causal link between MBD2 phase separation and heterochromatin compartmentalization is not firmly established, as the data are largely correlative. The distinction between phase separation-mediated effects and direct protein-protein interactions is acknowledged but not resolved. The physiological relevance of the in vitro phase separation observations is unclear, particularly given the high protein concentrations typically required. The manuscript would benefit from clearer presentation of quantitative data and statistical rigor. The claim that MBD2 acts as a scaffold for heterochromatin compartmentalization is supported by the data, but the mechanistic details and functional consequences require further validation.

- **Who would be interested in the results, and why** Researchers studying chromatin organization, phase separation biology, epigenetic regulation, and heterochromatin structure would find this work relevant. The methodological framework combining spatial proteomics with phase separation prediction tools could be of interest to the broader chromatin biology community. The focus on MBD2 and its role in NuRD complex recruitment may interest those studying DNA methylation readout and transcriptional repression.

- **Major strengths** The study uses a multi-pronged approach combining experimental and computational methods. The in vitro reconstitution of heterochromatin condensates from native tissue is a notable technical achievement. The systematic screening strategy for phase separation scaffolds is well conceived. The isoform-specific analysis of MBD2 provides useful insights into functional diversification.

- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Causal inference
  - **Claim pointer** The authors claim that MBD2 phase separation modulates heterochromatin compartmentalization and composition, and that this results in functional consequences including reduced histone acetylation and transcriptional activity
  - **Evidence pointer** Results sections on MBD2 isoform effects, histone acetylation, and transcriptional activity; location not provided
  - **Concern** The causal relationship between MBD2 phase separation and the observed effects on heterochromatin is not established. The authors show correlations between MBD2 expression, condensate formation, and histone acetylation changes, but do not demonstrate that phase separation per se is required for these effects. The MBD2∆CC construct, which shows altered phase separation, also lacks regions that may mediate other protein-protein interactions. The authors acknowledge this limitation but do not provide experiments to distinguish phase separation-dependent from phase separation-independent effects.
  - **Why it matters** The central claim of the manuscript is that MBD2 acts as a phase separation scaffold. Without demonstrating that the phase separation property is causally required for the observed functional effects, the conclusion is not fully supported. Alternative explanations, such as direct protein-protein interactions or chromatin remodeling activities, remain viable.
  - **Resolution test** Rescue experiments with phase separation-deficient MBD2 mutants that retain protein interaction capabilities, or optogenetic/chemical dimerization systems to induce phase separation independently of other MBD2 functions, would help establish causality.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Quantitative rigor
  - **Claim pointer** The authors state that MBD2a and MBD2b reduce heterochromatin compartment size at lower concentrations but enlarge it at higher concentrations, and that these effects correlate with phase separation ability
  - **Evidence pointer** Results section on MBD2 isoform effects; location not provided
  - **Concern** The quantitative analysis of heterochromatin compartment size changes is not described in sufficient detail. The text mentions dose-dependent effects but does not provide the number of cells analyzed, the statistical methods used, or the effect sizes. The threshold concentrations for the biphasic response are not specified. Without this information, the robustness of the phenotype is unclear.
  - **Why it matters** The biphasic concentration-dependent effect is a key observation supporting the phase separation model. If this effect is not rigorously quantified and replicated, the interpretation may be overstated.
  - **Resolution test** Provide detailed statistical analysis including sample sizes, effect sizes, and confidence intervals for all imaging-based measurements. Specify the exact concentrations used and the criteria for categorizing low versus high expression.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Physiological relevance
  - **Claim pointer** The authors estimate endogenous MBD2 concentrations in tissues and use these to argue that phase separation occurs at physiologically relevant levels
  - **Evidence pointer** Results section on MBD2 abundance estimation; location not provided
  - **Concern** The estimation of endogenous MBD2 concentrations relies on the assumption that MBD2 levels in C2C12 cells are comparable to those in muscle tissue. This assumption is not validated. The range of concentrations across tissues is very broad (3 to 320 µM), and the relevance of the in vitro phase separation threshold to the nuclear environment is unclear. The nuclear environment contains many other molecules that may influence phase separation.
  - **Why it matters** The physiological relevance of the in vitro phase separation observations is central to the claim that MBD2 regulates heterochromatin in vivo. If the concentrations required for phase separation are not achieved in vivo, the model is not supported.
  - **Resolution test** Direct measurement of MBD2 concentration in the relevant cell types using quantitative fluorescence microscopy or other methods. Testing phase separation in the presence of nuclear extracts or other cellular components would also strengthen the relevance.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Specificity of interactions
  - **Claim pointer** The authors claim that MBD2 phase separation selectively recruits histone deacetylases and excludes histone acetyltransferases, thereby modulating heterochromatin acetylation
  - **Evidence pointer** Results sections on protein composition and histone acetylation; location not provided
  - **Concern** The specificity of the recruitment and exclusion effects is not fully demonstrated. The authors show that some proteins are enriched or depleted in condensates, but the mechanism of selectivity is unclear. The claim that CC domain-containing proteins are preferentially recruited is based on a limited analysis. The functional significance of the observed changes in protein composition is inferred but not directly tested.
  - **Why it matters** The model proposes that MBD2 phase separation specifically modulates heterochromatin composition. If the recruitment and exclusion are not selective, the functional consequences may be different from those proposed.
  - **Resolution test** Systematic analysis of protein composition changes with quantitative proteomics, and functional assays to test whether the observed changes in protein composition are required for the effects on histone acetylation.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Abstract
  - **Evidence pointer** Abstract, location not provided
  - **Issue** The abstract states that "MBD2a and MBD2b exclude histone acetyltransferases (e.g. Kat7) and recruit histone deacetylases (e.g. HDAC11, GATAD2b)" but the distinction between direct protein interactions and phase separation-mediated effects is not clear.
  - **Required correction** Clarify whether these interactions are direct or mediated by phase separation, or acknowledge the uncertainty.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Methodological detail
  - **Affected element** Methods section on protein purification
  - **Evidence pointer** Methods, protein purification section
  - **Issue** The methods describe purification of MBD2 truncations but do not specify how protein quality and folding were assessed before use in phase separation assays.
  - **Required correction** Add details on quality control measures such as circular dichroism, size exclusion chromatography, or activity assays.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Statistical reporting
  - **Affected element** Results section on imaging
  - **Evidence pointer** Results, location not provided
  - **Issue** The text mentions statistical significance but does not consistently report effect sizes or confidence intervals.
  - **Required correction** Include effect sizes and confidence intervals for all key comparisons.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** Discussion
  - **Evidence pointer** Discussion, location not provided
  - **Issue** The terms "liquid-liquid phase separation" and "polymer-polymer phase separation" are used, but the distinction between these processes in the context of the data is not clearly explained.
  - **Required correction** Define these terms and explain how the data distinguish between them.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Literature context
  - **Affected element** Introduction
  - **Evidence pointer** Introduction, location not provided
  - **Issue** The introduction mentions that MBD2 is a member of the NuRD complex but does not discuss the known functions of MBD2 in detail, which would help contextualize the findings.
  - **Required correction** Add a brief summary of MBD2's known functions and how the current study extends this knowledge.

- **Technical failings that need to be addressed before the case is established** The causal link between MBD2 phase separation and heterochromatin compartmentalization is not established. The quantitative rigor of imaging analyses needs improvement. The physiological relevance of in vitro phase separation concentrations requires validation. The specificity of protein recruitment and exclusion needs further characterization.

## Risk / unsupported claims
- The claim that MBD2 phase separation is required for heterochromatin compartmentalization is not supported by direct causal evidence
- The claim that MBD2 phase separation specifically modulates histone acetylation through recruitment and exclusion of specific enzymes is inferred but not directly tested
- The estimation of endogenous MBD2 concentrations and their relevance to phase separation thresholds is based on unvalidated assumptions
- The distinction between phase separation-mediated effects and direct protein-protein interactions is not resolved
- The functional consequences of MBD2 phase separation on transcriptional activity are stated but not directly measured

## Assessment against Nature-style criteria
- **Originality** The integration of spatial proteomics with phase separation prediction tools is a novel approach. The identification of MBD2 as a potential phase separation scaffold in heterochromatin adds to the growing list of chromatin-associated phase separation proteins. However, the concept of phase separation in heterochromatin organization is already established, and the novelty lies primarily in the specific protein and methodological approach.
- **Scientific importance** The work addresses a fundamental question about how heterochromatin compartments are organized. Understanding the role of MBD2 in this process could have implications for diseases associated with MBD2 dysfunction. However, the importance is somewhat limited by the lack of causal evidence and the focus on a single protein.
- **Interdisciplinary readership** The work bridges chromatin biology, biophysics, and computational biology. The methodological framework could be of interest to researchers in these fields. However, the specialized nature of the topic may limit broader appeal.
- **Technical soundness** The experimental design is generally sound, but there are concerns about quantitative rigor and the lack of causal experiments. The use of multiple prediction tools and experimental validation is commendable, but the manuscript would benefit from more detailed statistical reporting and additional controls.
- **Readability for nonspecialists** The manuscript is written in a technical style that assumes familiarity with phase separation and chromatin biology. The abstract is accessible, but the results and methods sections may be challenging for nonspecialists. The logical flow is generally clear, but some sections could be streamlined.

## Recommendation posture
**Supportive if technical concerns are resolved.** The manuscript presents a potentially important contribution to the field of heterochromatin organization and phase separation biology. The methodological approach is innovative, and the identification of MBD2 as a candidate scaffold is plausible. However, the causal link between MBD2 phase separation and heterochromatin compartmentalization needs to be strengthened, and the quantitative rigor of the imaging analyses needs improvement. If these concerns are addressed, the manuscript could make a valuable contribution to the field.