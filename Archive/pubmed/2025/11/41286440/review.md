## Review setup
- **Input scope** Full manuscript text including abstract, main text, results, discussion, methods, and figure legends
- **Assessment boundary** Scientific content, experimental design, data interpretation, modelling approach, and claims as presented in the provided manuscript
- **Shared manuscript claim summary** The authors propose that hierarchical interactions between nucleolar and pericentromeric heterochromatin condensates are mediated by a dual-affinity protein, Pitchoune (Pit), which binds both compartments. They support this with live imaging in Drosophila embryos, genetic removal of rDNA, and coarse-grained simulations based on wetting theory.
- **Visible evidence base** Main text figures 1-7, extended data figures 1-9, supplementary videos 1-9, methods section, and statistical source data references
- **Missing materials affecting confidence** Full figure panels and raw imaging data not visible; exact statistical values and error bar definitions partially provided; supplementary video content not viewable; extended data figures not fully described in text

## Reviewer

### Overall assessment
This manuscript addresses a fundamental question in nuclear biology: how two distinct biomolecular condensates, the nucleolus and pericentromeric heterochromatin, establish and maintain spatial associations. The authors combine high-resolution live imaging, genetic perturbations, and physical modelling to propose a mechanism involving a dual-affinity linker protein, Pit. The work is timely and conceptually interesting, with potential implications for understanding nuclear architecture and condensate biology. However, several technical and interpretive concerns need to be addressed before the conclusions are fully supported.

### Who would be interested in the results, and why
This work will appeal to researchers in nuclear organization, phase separation, heterochromatin biology, and nucleolar function. The concept of dual-affinity proteins as molecular linkers between distinct condensates is broadly relevant to the condensate field. Developmental biologists studying nuclear reorganization during embryogenesis will also find the dynamic imaging data valuable. The modelling framework may interest biophysicists working on multiphase condensate systems.

### Major Strengths
1. The use of high-resolution live imaging across multiple developmental stages provides a dynamic view of PCH-nucleolar associations that goes beyond static snapshots.
2. The combination of experimental genetics (rDNA removal) with physical modelling is a powerful approach that strengthens the mechanistic claims.
3. The identification and validation of Pit as a dual-affinity protein with distinct domains mediating nucleolar and heterochromatin interactions is a concrete, testable finding.
4. The study addresses a conserved and biologically important phenomenon, with potential relevance to senescence and disease.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental evidence for direct Pit-HP1a interaction
- **Claim pointer** The authors claim that Pit directly interacts with HP1a via a conserved PxVxL motif, and that this interaction is required for PCH-nucleolar associations.
- **Evidence pointer** Figure 5, Extended Data Figure 6, Methods section "Co-immunoprecipitation" and "His-tag pull-down binding assay"
- **Concern** The pull-down binding assay is described with limited quantitative detail. The authors state that HP1a is enriched in the elution fraction when PitWT and HP1aWT are incubated together, but the fold enrichment is only shown for two independent experiments. The specificity of the interaction is supported by loss of binding with PitPxExL and HP1aI191E, which is good, but the affinity (Kd) is not measured. The claim of "weak interaction" is inferred from modelling but not directly quantified experimentally. Additionally, the APEX2 proximity labelling shows proximity within 20 nm, which is suggestive but not definitive for direct interaction. The authors should provide more quantitative binding data (e.g., titration, affinity estimates) or acknowledge that the interaction strength is not directly measured.
- **Why it matters** The central claim of the paper is that Pit acts as a dual-affinity linker. The strength of this claim depends on demonstrating a direct, specific interaction with both nucleolar components and HP1a. Without quantitative binding data, the "weak interaction" assumption in the model remains speculative.
- **Resolution test** Provide quantitative binding assays (e.g., ITC, SPR, or fluorescence anisotropy) to measure the affinity of Pit for HP1a and nucleolar components. Alternatively, perform competition experiments or mutagenesis to map the binding interface more precisely.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Modelling parameter selection and uniqueness
- **Claim pointer** The authors claim that their coarse-grained model recapitulates the in vivo organization and that the interaction hierarchy is validated by the simulations.
- **Evidence pointer** Figure 3, Extended Data Figure 4, Methods section "Modelling"
- **Concern** The model has many free parameters (interaction strengths between four components, concentrations, confinement size). The authors state that the parameter choices are not unique and that any hierarchy satisfying certain inequalities reproduces the observed organization. This raises the question of whether the model is over-parameterized and whether the conclusions are robust. The sensitivity analysis in Extended Data Figure 4 is helpful but appears limited to a few perturbations. A more systematic exploration of parameter space (e.g., random sampling or bifurcation analysis) would strengthen the claim that the observed organization is a robust consequence of the proposed hierarchy rather than a fine-tuned result.
- **Why it matters** The modelling is used to make predictions about the mechanism (e.g., dual-affinity protein requirement). If the model is not robust to parameter variations, the predictions may not be reliable.
- **Resolution test** Perform a systematic parameter sweep or use Bayesian inference to map the region of parameter space that reproduces the observed phenotypes. Show that the qualitative conclusions (e.g., requirement for dual-affinity protein) hold across a wide range of parameters.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Quantification of imaging data and statistical rigour
- **Claim pointer** The authors claim that PCH transitions from extended to surrounded configuration during development and that Pit knockdown reduces PCH-nucleolar associations.
- **Evidence pointer** Figures 1, 2, 6, Extended Data Figures 1, 2, 7
- **Concern** The imaging data are presented as representative images with some quantification (e.g., HP1a occupancy, aspect ratio, circularity). However, the statistical details are incomplete. For example, in Figure 1c, the number of embryos and nuclei analysed is stated, but the statistical test used is not specified. In Figure 6c, the P values are given, but the effect size and confidence intervals are not reported. The authors state that data distribution was assumed normal but not tested, which is a concern for small sample sizes. Additionally, the classification of PCH organization into discrete categories (surrounded, extended, clustered, fragmented) may be subjective; inter-observer variability or automated classification should be considered.
- **Why it matters** The dynamic reorganization is a key finding, and the quantification needs to be rigorous to support the claims. Subjective classification could introduce bias.
- **Resolution test** Provide full statistical details (test used, effect sizes, confidence intervals) for all quantified data. Consider using automated or blinded classification for PCH organization phenotypes. Report the number of independent experiments and embryos for each quantification.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Specificity of Pit function
- **Claim pointer** The authors claim that Pit is specifically required for PCH-nucleolar associations, and that its dual-affinity is the mechanism.
- **Evidence pointer** Figures 4, 6, Extended Data Figure 7
- **Concern** The knockdown experiments show that Pit depletion reduces PCH-nucleolar associations, and rescue with PitWT restores it. However, the specificity of this effect is not fully established. The authors do not show that other nucleolar proteins (e.g., Fib, Mod) are unaffected in their localization or that the effect is not due to general nucleolar disruption. Additionally, the rescue with PitPxExL and PitDQVD is informative, but the authors do not show that these mutants are expressed at similar levels to PitWT. Differences in expression could confound the interpretation.
- **Why it matters** The claim that Pit is a specific linker requires excluding non-specific effects of knockdown and ensuring that the mutant phenotypes are due to loss of specific functions rather than altered protein levels.
- **Resolution test** Show that Pit knockdown does not affect the localization of other nucleolar proteins (e.g., Fib, Mod) or overall nucleolar integrity. Quantify expression levels of PitWT, PitPxExL, and PitDQVD in rescue experiments to ensure comparable expression.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of the model
- **Claim pointer** The authors propose a generalizable role for dual-affinity proteins in co-organizing immiscible condensates.
- **Evidence pointer** Discussion section
- **Concern** The study is performed exclusively in Drosophila. While the authors discuss potential conservation, no data are presented to support generalizability. The claim that this is a "generalizable role" is speculative. The authors should either provide evidence from other systems or temper the claim.
- **Why it matters** The broader significance of the work depends on whether the mechanism is conserved. Overstating generalizability could mislead readers.
- **Resolution test** Provide evidence of similar mechanisms in other organisms (e.g., mammalian cells) or clearly state that generalizability is a hypothesis requiring further testing.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure labels
- **Affected element** Figures 1, 2, 4, 6
- **Evidence pointer** Figure legends
- **Issue** Some figure panels are not clearly labelled (e.g., Figure 1b, time points are indicated but not all are labelled; Figure 4b, the schematic is not fully explained in the legend).
- **Required correction** Ensure all panels are clearly labelled and that the legends fully describe the content of each panel, including time points, genotypes, and conditions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figures 1c, 2c, 2e, 6c, 7d, 7e
- **Evidence pointer** Figure legends
- **Issue** The statistical tests used are not consistently reported. Some legends state "P value was calculated using an unpaired two-tailed Student's t-test" but others do not specify the test.
- **Required correction** Consistently report the statistical test used, the number of replicates, and the definition of error bars (s.d. vs s.e.m.) in all figure legends.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Methods detail for imaging
- **Affected element** Methods section "Microscopy"
- **Evidence pointer** Methods section
- **Issue** The imaging parameters (e.g., laser power, gain, z-step size, time interval) are described as "adjusted to minimize bleaching" but specific values are not provided. This limits reproducibility.
- **Required correction** Provide specific imaging parameters for each experiment, including laser power, gain, pixel size, z-step, and time intervals.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Discussion of alternative models
- **Affected element** Discussion section
- **Evidence pointer** Discussion
- **Issue** The authors do not discuss alternative mechanisms for PCH-nucleolar association, such as direct DNA-RNA interactions or other bridging proteins. This would strengthen the discussion.
- **Required correction** Add a brief discussion of alternative models and how the proposed mechanism could be distinguished experimentally.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Nomenclature
- **Affected element** Throughout
- **Evidence pointer** Main text
- **Issue** The term "neocondensates" is used but not formally defined. It may be confused with other uses of the term in the literature.
- **Required correction** Define "neocondensates" clearly at first use and consider using a more descriptive term.

### Technical failings that need to be addressed before the case is established
1. Quantitative binding data for Pit-HP1a interaction (R1-M1)
2. Robustness analysis of the coarse-grained model (R1-M2)
3. Complete statistical reporting for imaging data (R1-M3)
4. Control for non-specific effects of Pit knockdown (R1-M4)

### Assessment against Nature-style criteria
- **Originality**: High. The concept of a dual-affinity protein mediating interactions between two distinct condensates is novel and will be of broad interest.
- **Scientific importance**: High. Understanding how nuclear condensates organize is fundamental to cell biology, and this work provides a mechanistic framework.
- **Interdisciplinary readership**: Moderate to high. The combination of imaging, genetics, and modelling will appeal to cell biologists, biophysicists, and developmental biologists.
- **Technical soundness**: Moderate. The imaging and genetic experiments are well-designed, but the quantitative binding data and model robustness need strengthening.
- **Readability for nonspecialists**: Good. The manuscript is clearly written, with helpful schematics and summaries. The modelling section may be challenging for some readers but is adequately explained.

### Recommendation posture
Supportive if technical concerns are resolved. The core findings are interesting and potentially important, but the quantitative evidence for the dual-affinity mechanism and the robustness of the model need to be strengthened. The authors should also provide more complete statistical reporting and address the specificity of Pit function.

## Risk / unsupported claims
1. The claim that Pit directly interacts with HP1a via the PxVxL motif is supported by pull-down and proximity labelling, but the affinity is not quantified. The "weak interaction" assumption in the model is not directly measured.
2. The claim that the model "recapitulates" the in vivo organization is based on a limited set of parameter choices; the robustness of this conclusion is not fully established.
3. The claim that the mechanism is "generalizable" to other systems is speculative and not supported by data outside Drosophila.
4. The statement that PCH "prevents" nucleolar hypercompaction in the absence of rDNA is based on correlative observations; a direct causal link is not demonstrated.
5. The functional significance of the PCH-nucleolar association (e.g., for ribosome synthesis or heterochromatin function) is not directly tested, and the authors do not claim this, but the broader implications should be stated more cautiously.