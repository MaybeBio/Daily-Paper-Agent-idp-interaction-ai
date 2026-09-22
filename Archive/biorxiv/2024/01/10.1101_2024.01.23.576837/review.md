## Review setup

- **Input scope** Full manuscript text, including summary, introduction, results, discussion, figure legends, and supplemental video legends. Figures and supplemental figures referenced but not provided.
- **Assessment boundary** Scientific claims, experimental design, logical coherence, and alignment with stated conclusions. No assessment of formatting, grammar, or editorial style.
- **Shared manuscript claim summary** The authors propose that TDP-43 aggregation in stress granules requires a double event: up-concentration of TDP-43 above a threshold within stress granules and oxidative stress. These two events induce intra-condensate demixing, producing a TDP-43-enriched phase that undergoes a liquid-to-solid transition into pathological aggregates. Mechanistically, demixing is driven by local RRM1 unfolding enabling intermolecular disulfide bonds and by hydrophobic patch interactions in the C-terminal domain. Engineering TDP-43 variants resistant to demixing eliminates pathological aggregates in cells.
- **Visible evidence base** Text descriptions of results from HeLa cell experiments, iPSC-derived motor neuron experiments, in vitro reconstitution assays, FRAP analysis, STED microscopy, MD simulations, SDD-AGE, and DLS. Figure references are cited but figures themselves are not available for inspection.
- **Missing materials affecting confidence** All figures, supplemental figures, and supplemental tables are absent. Quantitative data, statistical analyses, and experimental protocols are not fully described. This substantially limits verification of the claims.

## Reviewer

- **Overall assessment** This manuscript addresses a significant and timely question in neurodegeneration research, namely the mechanistic triggers for TDP-43 aggregation. The proposed double-event model, combining concentration threshold and oxidative stress, is conceptually appealing and could have broad implications. The combination of cell biology, in vitro reconstitution, and computational approaches is ambitious and appropriate. However, the absence of figures and detailed quantitative data prevents full evaluation of the evidence. Several claims, particularly regarding the generality of the proposed mechanism and the therapeutic implications, extend beyond what the described experiments can support. The manuscript would benefit from clearer presentation of quantitative results and more cautious interpretation of the in silico predictions.
- **Who would be interested in the results, and why** Researchers in the fields of neurodegeneration, particularly ALS and FTD, will find the proposed mechanism of TDP-43 aggregation relevant. The work also speaks to the broader community studying biomolecular condensates and phase separation, as it proposes a general pathway for protein aggregation within condensates. Those interested in protein misfolding, oxidative stress biology, and RNA-binding protein pathology would also find value. The potential therapeutic angle, targeting intra-condensate demixing, may interest drug discovery groups focused on neurodegenerative diseases.
- **Major strengths** The study combines multiple complementary approaches, including cell-based assays, in vitro reconstitution, and molecular dynamics simulations, to build a mechanistic model. The double-event requirement, involving both concentration and oxidative stress, provides a plausible resolution to the ongoing debate about whether stress granules promote or protect against TDP-43 aggregation. The identification of specific molecular determinants, namely RRM1 cysteine exposure and hydrophobic patch interactions, offers testable hypotheses. The demonstration that engineered variants can abrogate pathological aggregation in cells is a notable step toward potential therapeutic strategies.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that intra-condensate demixing of TDP-43 inside stress granules generates pathological aggregates, and that this process requires both up-concentration beyond a threshold and oxidative stress.
- **Evidence pointer** Figures 1, 2, 3, 6; location not provided
- **Concern** The central claim rests on the observation of TDP-43 puncta formation inside stress granules and their subsequent conversion to aggregates. However, the figures that would document this process are not available for review. The text describes phenotypes at different expression levels, but without the actual images, quantification, and statistical analysis, it is not possible to verify the threshold concentrations, the time course of demixing, or the distinction between demixing and simple aggregation. The FRAP data are described qualitatively, and the extent of mobility reduction over time is not quantified.
- **Why it matters** The entire model depends on the demonstration that demixing is a distinct, observable intermediate step that precedes aggregation. If the evidence for demixing is not robust, the proposed mechanism collapses into a simpler concentration-dependent aggregation model. The threshold concentration values are critical for the model, and their determination from the data must be transparent.
- **Resolution test** Provide the figures with clear visualization of the demixing process, including time-lapse images, quantification of puncta formation, and statistical comparison across conditions. Include FRAP recovery curves with quantitative parameters and statistical tests. Show the concentration dependence with a clear threshold determination method.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Causal evidence
- **Claim pointer** The authors claim that oxidative stress is a prerequisite for intra-condensate demixing, based on experiments with arsenite and paraquat versus puromycin.
- **Evidence pointer** Figure 3A, 3B, S3A, S3B; location not provided
- **Concern** The conclusion that oxidative stress is specifically required, rather than any stress that induces stress granules, depends on the comparison between arsenite and paraquat (oxidative stressors) and puromycin (a non-oxidative stressor). However, the text does not provide quantitative data on the extent of stress granule formation, the levels of reactive oxygen species generated by each treatment, or the TDP-43 concentrations in each condition. It is possible that puromycin-induced stress granules have different biophysical properties or lower TDP-43 partitioning, which would confound the interpretation. The claim that oxidative stress is specifically required, rather than merely sufficient, is not established.
- **Why it matters** The double-event model requires that oxidative stress is a necessary component. If other stressors that do not generate reactive oxygen species can also induce demixing under appropriate conditions, the model would need revision. The distinction between oxidative and non-oxidative stress is central to the proposed mechanism.
- **Resolution test** Quantify stress granule formation, TDP-43 concentration within granules, and reactive oxygen species levels for each stressor. Include a non-oxidative stressor that produces comparable stress granule properties to arsenite. Show that oxidative stress specifically, and not general stress responses, drives demixing.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic support
- **Claim pointer** The authors claim that local unfolding of RRM1 for intermolecular disulfide bond formation and increased hydrophobic patch interactions in the C-terminal domain drive intra-condensate demixing.
- **Evidence pointer** Figures 4B, 4C, 4D, 4E, 4F, S4A, S4C, S4D; location not provided
- **Concern** The molecular mechanism is derived primarily from molecular dynamics simulations, with supporting experiments using mutant proteins. The all-atom MD simulations are described as showing RRM1 unfolding and exposure of cysteines, but the simulation conditions, timescales, and validation against experimental data are not described in sufficient detail. The coarse-grained simulations correlating interaction strength with demixing are presented without quantitative comparison to experimental results. The mutant experiments are described qualitatively, and the extent to which the mutations affect protein folding, stability, or RNA binding is not fully addressed beyond statements of preserved function.
- **Why it matters** The proposed mechanism makes specific molecular predictions that could guide therapeutic development. If the simulations are not robust or the mutant phenotypes are not clearly linked to the proposed molecular events, the mechanistic model is speculative. The distinction between disulfide bond formation and hydrophobic interactions as separate contributors is not clearly resolved.
- **Resolution test** Provide detailed simulation parameters, convergence criteria, and validation against experimental data. Show quantitative data on mutant protein stability, folding, and RNA binding. Demonstrate that the observed effects on demixing are specifically due to the proposed molecular changes and not to general protein destabilization.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** The authors conclude that up-concentration inside condensates and simultaneous exposure to environmental stress could be a general pathway for protein aggregation, with intra-condensate demixing as a key intermediate step.
- **Evidence pointer** Discussion; location not provided
- **Concern** The claim of generality is based on a single protein, TDP-43, studied in a limited set of experimental systems. While the authors cite previous work on other proteins, no new data are presented to support the extension of this model beyond TDP-43. The specific molecular features, such as the RRM1 cysteines and the hydrophobic patch, may be unique to TDP-43. The proposal that this is a general pathway is speculative and not directly tested.
- **Why it matters** The broader significance of the work depends on whether the mechanism applies to other disease-associated proteins. If the model is TDP-43-specific, the impact is more limited. The claim of generality should be framed as a hypothesis rather than a conclusion.
- **Resolution test** Either provide data on other proteins that aggregate in stress granules, or revise the claim to clearly state that this is a hypothesis requiring further testing.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Therapeutic relevance
- **Claim pointer** The authors suggest that targeting intra-condensate demixing could be a potential avenue for therapeutic intervention.
- **Evidence pointer** Discussion; location not provided
- **Concern** The therapeutic claim is based on the demonstration that engineered TDP-43 variants resistant to demixing do not form aggregates in cells. However, these variants are not representative of the wild-type protein in patients, and the approach of mutating the protein is not directly translatable to a therapeutic strategy. The authors do not demonstrate that any pharmacological intervention can prevent demixing or aggregation. The link between the experimental findings and therapeutic potential is not established.
- **Why it matters** Therapeutic claims should be supported by evidence that the identified process can be modulated by external factors. Without such evidence, the statement is premature and could be misleading.
- **Resolution test** Either provide proof-of-concept data showing that a small molecule or other intervention can inhibit demixing, or temper the therapeutic claim to reflect the speculative nature of this suggestion.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Definition of threshold concentration
- **Evidence pointer** Figure 1A, 2C; location not provided
- **Issue** The threshold concentration for demixing is mentioned repeatedly but never explicitly defined or quantified. The relationship between bulk cytoplasmic concentration and concentration within stress granules is not clearly explained.
- **Required correction** Provide a clear definition of the threshold concentration, how it was determined, and its numerical value if available. Clarify how concentrations within stress granules were measured or estimated.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Experimental detail
- **Affected element** Mutant characterization
- **Evidence pointer** Figures 4F, 5A, S4E, S4F, S4G, S4H; location not provided
- **Issue** The cysteine mutants and the HP deletion mutant are described as having preserved RNA binding and function, but the assays used are not described in detail. The text states that stability was comparable to wild-type, but the methods for assessing stability are not given.
- **Required correction** Briefly describe the assays used to assess protein stability, RNA binding, and function. Provide quantitative data or reference to supplemental methods.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Role of RNA in demixing
- **Evidence pointer** Figure 2A, S2A; location not provided
- **Concern** The authors show that RNA binding is important for TDP-43 partitioning into stress granules, but the demixed phase contains less RNA. The relationship between RNA loss and demixing is not fully explored. It is unclear whether RNA loss is a cause or consequence of demixing.
- **Required correction** Discuss the potential role of RNA in the demixing process and whether RNA displacement is a driving force or a downstream event.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Terminology
- **Evidence pointer** Throughout; location not provided
- **Issue** The terms "demixing," "phase separation," and "aggregation" are sometimes used interchangeably, which could confuse readers. The distinction between these processes is important for the model.
- **Required correction** Define each term clearly and use them consistently throughout the manuscript.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion of opposing views
- **Evidence pointer** Introduction, Discussion; location not provided
- **Issue** The manuscript mentions that the role of stress granules in TDP-43 aggregation is controversial, but the discussion of opposing evidence is brief. A more thorough treatment of studies that did not find a link between stress granules and TDP-43 aggregation would strengthen the argument.
- **Required correction** Expand the discussion of conflicting findings and explain how the proposed model reconciles these discrepancies.

- **Technical failings that need to be addressed before the case is established** The absence of all figures and quantitative data is a critical failing that prevents verification of the central claims. The threshold concentration values, the time course of demixing, the FRAP recovery parameters, and the statistical comparisons are not available. The molecular dynamics simulations are described without sufficient methodological detail to assess their validity. The mutant experiments lack quantitative characterization of protein stability and function. These issues must be resolved before the case for the proposed mechanism can be considered established.
- **Assessment against Nature-style criteria** Originality: The double-event model combining concentration threshold and oxidative stress is a novel contribution that could shift thinking in the field. Scientific importance: The work addresses a fundamental question in neurodegeneration with potential therapeutic implications, making it of high importance. Interdisciplinary readership: The topic bridges cell biology, biophysics, and computational biology, and would appeal to a broad readership. Technical soundness: The multi-method approach is appropriate, but the lack of accessible quantitative data and methodological detail currently undermines confidence in the technical execution. Readability for nonspecialists: The manuscript is generally well-written and the conceptual model is clearly articulated, though some sections assume familiarity with phase separation concepts.
- **Recommendation posture** Supportive if technical concerns are resolved. The conceptual model is compelling and the multi-method approach is appropriate, but the evidence base as presented is insufficient to fully establish the claims. Provision of the missing figures, quantitative data, and methodological details is essential.

## Risk / unsupported claims

- The claim that intra-condensate demixing is a general pathway for protein aggregation in cells is not supported by the data presented, which focus exclusively on TDP-43.
- The claim that targeting intra-condensate demixing is a viable therapeutic avenue is speculative and not supported by any pharmacological intervention data.
- The claim that oxidative stress is a prerequisite, rather than one of several possible triggers, is not fully established due to the limited comparison of stressors.
- The molecular mechanism involving RRM1 unfolding and hydrophobic patch interactions is based primarily on simulations that are not described in sufficient detail to assess their robustness.
- The threshold concentration for demixing is mentioned but not defined or quantified, making the claim difficult to evaluate.