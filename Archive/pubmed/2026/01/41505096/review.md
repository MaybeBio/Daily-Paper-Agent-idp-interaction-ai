## Review setup
- **Input scope** Full manuscript text including abstract, materials and methods, results, discussion, and supplementary figure references
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and consistency between evidence and conclusions as presented in the provided text
- **Shared manuscript claim summary** The authors propose that Lsr2, a nucleoid-associated protein in Mycobacterium tuberculosis, compacts DNA through sequence-dependent co-condensation with AT-rich regions, mediated by multivalent protein–protein and protein–DNA interactions, and that this mechanism underlies gene silencing and genome organization in vivo
- **Visible evidence base** Biochemical phase separation assays, EMSA, AFM, single-molecule TIRF microscopy with defined DNA constructs, FRAP, coarse-grained Brownian dynamics simulations, and confocal imaging of endogenously tagged Lsr2-eGFP in M. tuberculosis
- **Missing materials affecting confidence** Figures and supplementary figures are referenced but not provided; exact numerical data, statistical details, and control conditions for several experiments are not fully described; simulation parameters are only partially listed in supplementary tables that are not available for inspection

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question in bacterial chromosome biology: how a nucleoid-associated protein achieves genome-wide compaction and gene regulation. The combination of biochemical assays, single-molecule imaging, simulations, and in vivo validation is ambitious and potentially impactful. The central claim that Lsr2 undergoes sequence-dependent co-condensation with AT-rich DNA, rather than simple sequence-specific binding of individual proteins, is conceptually novel and would be of broad interest. However, the evidence as presented in the text has several gaps that prevent full evaluation. Key quantitative details, control experiments, and statistical analyses are not described in sufficient depth. The in vivo data, while suggestive, rely on a limited set of observations that do not yet establish the causal link between co-condensation and gene regulation. The simulation model is described only in outline, and its predictive power relative to the experimental observations cannot be fully assessed without the supplementary information. The manuscript is well written and logically organized, but the technical depth required to support the strong claims is not fully visible in the provided material.

- **Who would be interested in the results, and why** Researchers studying bacterial nucleoid organization, nucleoid-associated proteins, phase separation in biology, and mycobacterial pathogenesis would find these results of interest. The concept of sequence-dependent co-condensation as a mechanism for genome compaction and gene silencing could also attract attention from the broader chromatin and gene regulation community, as it offers a new paradigm for how proteins can collectively sense DNA sequence features over long genomic scales.

- **Major strengths**
  - The study combines multiple orthogonal approaches, including biochemistry, single-molecule imaging, simulations, and in vivo imaging, which strengthens the overall argument
  - The central concept of sequence-dependent co-condensation is novel and distinguishes this work from prior studies of NAP-mediated DNA compaction
  - The use of defined DNA constructs with controlled AT-content distributions is a thoughtful experimental design that directly tests the sequence-dependence hypothesis
  - The in vivo validation using endogenously tagged Lsr2 in M. tuberculosis adds physiological relevance
  - The authors connect their findings to a mechanistic model that can explain how a single protein regulates many genes simultaneously

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that Lsr2 forms co-condensates with DNA preferentially at AT-rich regions, with 86.4% of condensates forming at the AT-rich segment in the 21 kb construct
- **Evidence pointer** Results section, Figure 4g and 4h; location not provided
- **Concern** The quantitative claim of 86.4% is presented without statistical context. It is unclear how many molecules were analyzed, what the variability is across independent experiments, and whether this percentage is significantly different from what would be expected by chance given the fraction of the DNA that is AT-rich. The thresholding method for defining condensate regions is described, but the choice of threshold parameter x = 0.5 is not justified, and no sensitivity analysis is provided. Without these details, the strength of the sequence-dependence claim cannot be properly evaluated.
- **Why it matters** The central conclusion of the paper rests on the claim that co-condensation is sequence-dependent. If the 86.4% figure is not robustly supported by statistical analysis, the main conclusion is weakened.
- **Resolution test** Provide the number of molecules analyzed, the distribution of condensate positions across all molecules, a statistical comparison against a null model of random condensate positioning, and a sensitivity analysis for the threshold parameter.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that the addition of DNA lowers the concentration required for Lsr2 phase separation from approximately 5 µM to approximately 1 µM (and 500 nM in supplementary data)
- **Evidence pointer** Results section, Figure 1d and Supplementary Figure S1c; location not provided
- **Concern** The saturation concentrations are reported as approximate values, but the experimental method for determining these concentrations is not described in sufficient detail. It is unclear how phase separation was scored, whether the measurements were performed at equilibrium, and what the error bars represent. The discrepancy between 1 µM and 500 nM in the main text and supplementary figure is not explained. Additionally, the relationship between the in vitro saturation concentration and the estimated cellular concentration of Lsr2 (15 µM) is mentioned but not critically discussed.
- **Why it matters** The claim that DNA lowers the phase separation threshold is a key part of the mechanistic model. If the concentration measurements are not robust, the model's foundation is uncertain.
- **Resolution test** Provide a detailed description of the phase separation assay, including how the threshold for phase separation was defined, the number of replicates, and the statistical analysis. Clarify the discrepancy between the 1 µM and 500 nM values.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that their coarse-grained Brownian dynamics simulations reproduce the experimental observations of sequence-dependent co-condensation, with a Pearson correlation coefficient of approximately 0.75 between simulated and experimental condensate position probabilities
- **Evidence pointer** Results section, Figure 4j; location not provided
- **Concern** The simulation model is described only in outline. The interaction parameters, the mapping between simulation units and physical units, and the specific implementation of sequence-dependent binding affinities are not described in the main text. The Pearson correlation of 0.75 is reported without confidence intervals or a description of how many independent simulations were performed. It is also unclear whether the model was parameterized to match the experimental data or whether it makes independent predictions. Without this information, the claim that the simulations "confirm" the experimental findings cannot be evaluated.
- **Why it matters** The simulation is presented as a key validation of the proposed mechanism. If the model is not described in sufficient detail or is not shown to make robust predictions, the support it provides is limited.
- **Resolution test** Provide a full description of the simulation model, including all interaction parameters, the mapping to physical units, the number of independent simulations, and the statistical analysis of the correlation. Clarify whether the model was parameterized independently of the experimental results.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that in M. tuberculosis cells, Lsr2-eGFP forms puncta that co-localize with DAPI-stained DNA, and that this supports the co-condensation mechanism
- **Evidence pointer** Results section, Figure 5; location not provided
- **Concern** The in vivo imaging data are described qualitatively. No quantification is provided for the degree of co-localization between Lsr2-eGFP puncta and DAPI-stained DNA. It is unclear how many cells were analyzed, whether the co-localization is statistically significant, and whether the puncta represent phase-separated condensates or simply clusters of Lsr2 bound to DNA. The authors also state that the total integrated fluorescence intensity of Lsr2 remains constant regardless of puncta number, but no data or statistical analysis is shown to support this claim. The comparison between Lsr2 knockout and wild-type cells is mentioned but not described in detail.
- **Why it matters** The in vivo data are intended to bridge the in vitro and in silico findings to physiological relevance. Without quantitative analysis, the strength of this bridge is unclear.
- **Resolution test** Provide quantitative co-localization analysis, the number of cells analyzed, statistical comparisons, and a more detailed description of the knockout control experiments.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that their findings reveal a "novel mechanism for NAP-mediated genome organization in bacteria" and that this is "contrary to the classical view of sequence-dependent binding of individual protein molecules to DNA"
- **Evidence pointer** Abstract and Discussion; location not provided
- **Concern** The claim of novelty is strong, but the distinction between the proposed co-condensation mechanism and previously described models of NAP-mediated DNA bridging and phase separation is not fully articulated. The authors reference prior work on H-NS and Dps but do not clearly delineate what is conceptually new about their model beyond the sequence-dependence aspect. The statement that co-condensation "senses" the average binding energy landscape is intriguing but is not developed into a testable quantitative prediction that distinguishes it from alternative models.
- **Why it matters** The broader significance of the work depends on the novelty of the mechanism. If the distinction from prior models is not clearly established, the impact of the findings may be overstated.
- **Resolution test** Provide a more explicit comparison with existing models of NAP-mediated DNA compaction and phase separation, and articulate specific predictions that uniquely arise from the co-condensation model.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Abstract
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract uses the term "co-condensation" without defining it, which may be unfamiliar to readers outside the phase separation field. The phrase "senses the average binding energy landscape" is evocative but not immediately clear.
- **Required correction** Briefly define co-condensation in the abstract and rephrase the "senses" statement in more concrete terms.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, EMSA and AFM
- **Evidence pointer** Results section, Supplementary Figure S2; location not provided
- **Issue** The EMSA and AFM experiments are mentioned as supporting evidence for higher-order complex formation, but no details are provided about the experimental conditions, the concentrations used, or how the images were quantified.
- **Required correction** Provide a brief description of the EMSA and AFM conditions and how the results support the phase separation model.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, FRAP analysis
- **Evidence pointer** Results section, Figure 1g and 3g; location not provided
- **Issue** The FRAP recovery curves are described qualitatively. It is unclear what fraction of fluorescence was recovered and over what timescale, and whether the recovery was complete.
- **Required correction** Provide quantitative FRAP parameters, such as mobile fraction and half-time of recovery, for the conditions tested.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, mutant analysis
- **Evidence pointer** Results section, Figure 2c–e; location not provided
- **Issue** The mutant analysis is described in terms of "reduced ability" or "required higher concentration," but the magnitude of these effects is not quantified.
- **Required correction** Provide quantitative values for the phase separation thresholds or condensate areas for each mutant relative to wild type.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Interdisciplinary readership
- **Affected element** Discussion
- **Evidence pointer** Discussion; location not provided
- **Issue** The discussion of implications for pathogenicity is brief and speculative. The connection between co-condensation and virulence is not developed.
- **Required correction** Either expand the discussion of pathogenic implications with specific hypotheses or temper the speculation.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, simulation analysis
- **Evidence pointer** Methods, simulation section; location not provided
- **Issue** The description of the simulation analysis is brief. The method for identifying condensates in the simulations and mapping them to experimental positions is not described.
- **Required correction** Provide a more detailed description of the simulation analysis, including how condensates were identified and how the probability profiles were generated.

## Risk / unsupported claims
- The claim that Lsr2 co-condensation "senses" the average binding energy landscape is presented as a conclusion but is not directly tested as a distinct hypothesis
- The statement that the findings are "contrary to the classical view" of sequence-dependent binding is an interpretation that is not directly tested by the experiments
- The in vivo claim that Lsr2 is "causally" responsible for DNA compaction in M. tuberculosis is not fully supported by the described knockout experiments, which are mentioned only briefly
- The claim that the total amount of Lsr2 in condensates is conserved regardless of puncta number is stated without supporting quantitative data
- The physiological relevance of the in vitro phase separation concentrations to the intracellular environment is asserted but not critically examined