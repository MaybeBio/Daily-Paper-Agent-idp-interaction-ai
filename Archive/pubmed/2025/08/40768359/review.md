## Review setup
- **Input scope** Full manuscript text (main text, methods, and references to supplementary materials)
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided manuscript text. Supplementary figures and tables were not directly provided and are assessed only through the authors' descriptions.
- **Shared manuscript claim summary** The authors propose that paraspeckle assembly is driven by competitive RNA binding between immiscible core and shell proteins. They report that core proteins FUS and NONO bind preferentially to NEAT1 ends rather than the middle assembly domain, that NONO and FUS synergistically condense with all NEAT1 regions at physiological stoichiometry, and that the shell protein TDP-43 competes for NEAT1 end binding and forms surfactant-like layers that exclude core proteins. A revised coarse-grained simulation incorporating these interactions produces layered condensates resembling paraspeckles.
- **Visible evidence base** Main text figures 1-5 (described), supplementary figures S1-S11 (described), supplementary table S1 (described), methods section, and data availability statements
- **Missing materials affecting confidence** Actual figure images, supplementary figures, supplementary table S1, full simulation parameter values, raw data, and analysis code were not provided for direct inspection. The manuscript text describes results but the underlying data cannot be independently verified from the supplied material.

## Reviewer
- **Overall assessment** This manuscript presents a compelling and well-structured investigation into the molecular mechanisms underlying paraspeckle layering. The combination of in vitro biochemistry, biophysical characterization, and coarse-grained simulation is appropriate and powerful. The central finding that core proteins bind preferentially to shell-localized NEAT1 regions contradicts the prevailing assembly model and is potentially significant. However, several technical concerns regarding data presentation, statistical rigor, and the interpretation of simulation results must be addressed before the conclusions are fully established.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, RNA-binding proteins, nuclear organization, and RNA biology. The work is also relevant to those interested in the mechanisms of layered or multi-domain condensate assembly, a topic of broad current interest. The findings on TDP-43 competition may be of interest to the neurodegeneration community given TDP-43's role in ALS/FTD.
- **Major strengths** 1) The study directly tests a prevailing model and provides surprising counter-evidence. 2) The combination of experiments and simulation is synergistic. 3) The use of multiple complementary assays (EMSA, FRAP, imaging) strengthens the conclusions. 4) The revised simulation model is grounded in experimental measurements. 5) The writing is clear and accessible.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (statistical rigor of Kd comparisons), R1-M2 (simulation parameter justification), R1-M3 (TDP-43 competition mechanism)
- **Assessment against Nature-style criteria** **Originality:** High. The finding that core proteins prefer shell-localized RNA regions is unexpected and challenges the current model. The concept of competitive RNA binding between immiscible proteins as a layering mechanism is novel. **Scientific importance:** High. Paraspeckles are a model system for understanding layered condensates, and the proposed mechanism may generalize to other multi-domain condensates. **Interdisciplinary readership:** Moderate to high. The work bridges RNA biology, biophysics, and computational modeling, and should appeal to a broad readership. **Technical soundness:** Moderate. The experimental approaches are appropriate, but several technical concerns (statistics, simulation justification, competition mechanism) need resolution. **Readability for nonspecialists:** Good. The manuscript is clearly written and the concepts are explained well, though some familiarity with condensate biology is assumed.
- **Recommendation posture** Supportive if technical concerns are resolved. The core findings are potentially important, but the statistical rigor of binding comparisons, the justification of simulation parameters, and the mechanistic evidence for TDP-43 competition need strengthening.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The authors claim that FUS binds with greater affinity to NEAT1 ends compared to the middle region, and that apparent Kd values correlate with motif abundance (Fig. 2B, 2C).
- **Evidence pointer** Figure 2B, 2C; SI Appendix Fig. S2B-G
- **Concern** The apparent Kd values are reported as mean ± sd, but the number of replicates, the statistical test used for comparisons, and the degrees of freedom are not stated in the main text. The claim of "order of magnitude" difference between E1 and C2 binding (65 vs 771 nM) needs a formal statistical comparison. Additionally, the correlation between motif abundance and binding affinity (Fig. 2C) is presented without a correlation coefficient or p-value. The authors state that "apparent Kd estimates for all proteins fell roughly along a common trend" but this is not quantified.
- **Why it matters** The central claim that core proteins prefer ends over middle is based on these Kd comparisons. Without proper statistics, the reader cannot assess whether the observed differences are robust or within experimental noise. The claim of a universal relationship between motif count and binding energy is a strong statement that requires quantitative support.
- **Resolution test** Provide the number of independent replicates for each Kd measurement, the statistical test used (e.g., t-test with multiple comparison correction or ANOVA), and the resulting p-values for all pairwise comparisons. Report the correlation coefficient and p-value for the ∆∆G versus motif abundance relationship. If the data are pooled from multiple experiments, show the distribution of individual measurements.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Simulation parameter justification
- **Claim pointer** The authors claim that their revised coarse-grained simulation, with parameters informed by experimental observations, produces layered condensates resembling paraspeckles (Fig. 5A, 5B).
- **Evidence pointer** Figure 5A, 5B; SI Appendix Fig. S9, Table S1
- **Concern** The simulation parameters are described as "based on experimental observations" but the specific mapping from experimental measurements to interaction strengths (ϵ values) is not provided in the main text. The authors state that "weak protein-protein interactions between FUS/NONO and TDP43" and "stronger RNA-RNA interactions between NEAT1 middle regions" were used, but the numerical values and the rationale for their selection are not given. Without this information, the reader cannot assess whether the simulation results are robust to parameter choices or whether they were tuned to produce the desired outcome.
- **Why it matters** The simulation is used to support the proposed mechanism. If the parameters are not justified or if the results are highly sensitive to parameter choices, the simulation provides weak evidence. The claim that the simulation "can give rise to paraspeckle-like, layered assemblies" needs to be supported by a demonstration that the result is not a trivial consequence of the chosen parameters.
- **Resolution test** Provide the full interaction matrix (ϵ values) in the main text or a clearly referenced table. Justify each parameter choice with reference to specific experimental measurements. Perform and report a sensitivity analysis showing how the layered structure depends on key parameters (e.g., TDP-43 interaction strengths, RNA-RNA interaction strength). If possible, show that the layered structure emerges for a range of reasonable parameters, not just a single finely-tuned set.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic evidence for TDP-43 competition
- **Claim pointer** The authors claim that TDP-43 competes with FUS and NONO for RNA binding, thereby excluding core proteins from the shell (Fig. 4, 5C).
- **Evidence pointer** Figure 4A-D; SI Appendix Fig. S6, S7
- **Concern** The evidence for competition is indirect. The authors show that TDP-43 binds E3 and that adding TDP-43 to FUS or NONO condensates reduces their size and protein levels. However, they do not directly demonstrate that TDP-43 displaces FUS or NONO from RNA. The claim of competition would be strengthened by a direct binding competition assay (e.g., TDP-43 titrated into FUS-RNA binding reactions) or by showing that TDP-43 and FUS/NONO cannot simultaneously bind the same RNA molecule. The authors also do not address whether the observed effects could be due to TDP-43 sequestering RNA through its strong self-interactions rather than direct competition.
- **Why it matters** The proposed mechanism relies on competitive RNA binding as the key determinant of layering. If the competition is not direct, the mechanism may be different (e.g., TDP-43 self-association creating a physical barrier). The distinction matters for understanding how the system is regulated and for predicting the effects of mutations or perturbations.
- **Resolution test** Perform direct competition experiments, such as EMSAs with both TDP-43 and FUS or NONO present, showing that TDP-43 reduces FUS/NONO binding to E3. Alternatively, use a biochemical approach (e.g., pull-down or crosslinking) to show that TDP-43 and FUS/NONO cannot form a ternary complex on the same RNA. Address whether TDP-43's self-interactions contribute to the observed exclusion independently of RNA binding competition.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 2D-F
- **Evidence pointer** Figure 2D-F; SI Appendix Fig. S3
- **Issue** The authors state that condensates assembled with middle region RNAs were "consistently smaller" compared to end RNAs, but the quantitative data (sizes, distributions, statistical comparisons) are not shown in the main text. The relationship between condensate area and FUS/RNA ratio (Fig. 2F) is presented as a correlation but the correlation coefficient and p-value are not reported.
- **Required correction** Report the quantitative data for condensate sizes (mean, SD, n) and the statistical test used. Provide the correlation coefficient and p-value for the area versus FUS/RNA ratio relationship.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion of TDP-43 patchiness
- **Evidence pointer** Figure 5A, 5B; SI Appendix Fig. S9B
- **Issue** The authors note that TDP-43 forms "discrete, patch-like clusters" in their simulations and state that this resembles previous imaging studies. However, the comparison to the imaging data is qualitative and the authors do not provide a quantitative comparison (e.g., patch size, density, or distribution).
- **Required correction** Either provide a quantitative comparison between simulated and experimental TDP-43 patch properties, or temper the claim to note that the patchiness is qualitatively consistent but not quantitatively validated.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section on EMSA analysis
- **Evidence pointer** Methods, "Gel EMSAs"
- **Issue** The description of how Kd values were extracted from EMSA data is brief. The authors state that data were fit to the Hill equation but do not specify how the fraction bound was calculated for each replicate, how many replicates were performed, or how outliers were handled. The filtering of I(C) values less than 0 is mentioned but the frequency of such occurrences is not reported.
- **Required correction** Provide more detail on the fitting procedure, including the number of replicates, the treatment of individual versus pooled data, and the criteria for accepting fits.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion of alternative models
- **Evidence pointer** Discussion section
- **Issue** The authors propose their mechanism as an alternative to the current model but do not discuss in detail how their findings might be reconciled with previous observations that supported the old model. For example, the previous model was based on specific NEAT1 deletion experiments; the authors do not explain why those experiments might have been misleading.
- **Required correction** Add a brief discussion of how the previous experimental evidence for the old model might be reinterpreted in light of the new findings.

## Risk / unsupported claims
- The claim that "all proteins prefer to bind portions of the RNA that localize to the same shell layer" is based on in vitro binding to 1 kb fragments and may not fully recapitulate the context of the full-length NEAT1 RNA with its complex secondary structure. The authors acknowledge this limitation but the claim as stated is strong.
- The claim that TDP-43 "competes" with FUS and NONO for RNA binding is not directly demonstrated (see R1-M3).
- The claim that the revised simulation "can give rise to paraspeckle-like, layered assemblies" is supported but the parameter sensitivity is not established (see R1-M2).
- The extrapolation from in vitro condensate behavior to the cellular context of paraspeckles is reasonable but speculative, particularly regarding the role of transcriptional bursts. The authors appropriately frame this as a proposal but the claim that "transcriptional bursts are required to form paraspeckle-like clusters" is not directly tested experimentally.
- The statement that "the middle region is more single-stranded and therefore more capable of engaging in RNA-RNA interactions" is based on secondary structure prediction and is not experimentally validated.