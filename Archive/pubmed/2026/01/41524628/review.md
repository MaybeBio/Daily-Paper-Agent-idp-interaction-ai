## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, materials and methods, and figure legends as provided.
- **Assessment boundary** The scientific claims, experimental design, data interpretation, and technical soundness as presented in the provided manuscript text. No external data or unpublished materials were consulted.
- **Shared manuscript claim summary** The authors report that IBDV VP3 is necessary but not sufficient for the formation of cytoplasmic puncta, that VP3 and VP1 (with likely vRNA) constitute the minimal components for phase-separated condensates, and that the C-terminal 36 amino acids of VP3 form a predicted intrinsically disordered region (IDR) that promotes puncta formation and modulates their physical properties, including size, shape, and liquidity.
- **Visible evidence base** Results sections describing cell transfection, infection, imaging, FRAP, AlphaFold modeling, MD simulations, and statistical comparisons; figures referenced as Fig. 1 through Fig. 13 and Fig. S1 through S7; methods sections for AlphaFold, MD simulations, cell culture, and FRAP.
- **Missing materials affecting confidence** Figure panels and raw data for several key experiments (e.g., FRAP curves, colocalization images, puncta morphology distributions) are not fully described in the text; exact statistical values (e.g., effect sizes, confidence intervals) for several comparisons are not reported; details of the MD simulation convergence and force field validation are not provided; the nature of the "likely vRNA" requirement is not experimentally tested.

## Reviewer
- **Overall assessment** This manuscript addresses an important question in virology and phase separation biology: the molecular determinants of birnavirus replication compartment formation. The authors provide a clear and logical progression from identifying VP3 as a necessary component, to defining a minimal system, to characterizing a specific C-terminal IDR and its functional impact. The work is technically sound in its core imaging and modeling approaches, and the conclusions are largely supported by the data presented. However, several concerns regarding the quantitative rigor of the FRAP analysis, the lack of direct evidence for vRNA involvement, and the limited mechanistic depth of the IDR's role warrant attention. The manuscript is of interest to virologists and cell biologists studying LLPS, but the current evidence does not fully establish the mechanistic claims without additional experimental support.
- **Who would be interested in the results, and why** Virologists studying dsRNA virus replication, particularly birnaviruses and related pathogens, will find the identification of VP3 as a key scaffold and the minimal component requirements valuable. Researchers in the LLPS field will be interested in the demonstration that a specific IDR can modulate condensate physical properties, providing a viral model system for studying IDR function. The work may also appeal to those interested in viral replication compartment biology and the development of antiviral strategies targeting phase separation.
- **Major strengths** The study combines computational prediction, molecular biology, live-cell imaging, and biophysical assays to address a focused question. The identification of VP3 as necessary but not sufficient, and the minimal component definition, are clear and well-supported. The use of multiple tags to control for artifacts is a thoughtful approach. The FRAP and morphology analyses provide quantitative evidence for the IDR's role in modulating condensate properties. The work is well-contextualized within the broader LLPS literature.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (FRAP quantification), R1-M2 (vRNA requirement), R1-M3 (IDR mechanistic role), R1-M4 (statistical reporting).
- **Assessment against Nature-style criteria** **Originality:** The work is original in its focus on birnavirus VP3 and its IDR, providing a new viral model for LLPS. The finding that a specific IDR modulates condensate physical properties is a valuable contribution. **Scientific importance:** The study advances understanding of birnavirus replication and adds to the growing evidence that LLPS is a conserved mechanism in viral replication. The minimal component definition is a useful step forward. **Interdisciplinary readership:** The topic bridges virology, cell biology, and biophysics, and the findings are likely to appeal to researchers in all three areas. **Technical soundness:** The core imaging and modeling approaches are appropriate, but the FRAP quantification and lack of direct vRNA testing weaken the technical rigor. **Readability for nonspecialists:** The manuscript is generally well-written and accessible, with clear explanations of LLPS concepts. However, some methods details (e.g., MD simulation parameters) may be dense for non-specialists. Overall, the manuscript has strong potential but requires revisions to fully meet the standards of a high-impact journal.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly the FRAP quantification and the direct testing of vRNA involvement.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that FRAP analysis demonstrates that the VP3 C-terminal IDR affects the liquidity of puncta, with a significantly higher mobile fraction in wild-type (0.704) compared to ΔC (0.291) puncta.
- **Evidence pointer** Results section "The IBDV VP3 C-terminal IDR affects the physical properties of VFs"; Figure 11; Methods "Fluorescence recovery after photobleaching"
- **Concern** The FRAP methodology and analysis are not described in sufficient detail to assess the robustness of the mobile fraction and recovery half-time measurements. Key parameters such as the bleach depth, the normalization method (e.g., double vs. single normalization), the fitting model (e.g., single vs. double exponential), and the number of replicates are not reported. The authors state that the analysis was based on easyFRAP-web, but the specific settings and any modifications are not detailed. Furthermore, the authors note that the mNG fluorophore was fused to VP1, not VP3, and that unbound VP1-mNG may contribute to the recovery, which complicates the interpretation of the mobile fraction as a direct measure of VP3 dynamics.
- **Why it matters** The FRAP data are central to the claim that the IDR modulates the physical properties of the puncta. Without a clear and rigorous description of the FRAP methodology, the reliability of the mobile fraction and recovery half-time values cannot be evaluated. The potential contribution of unbound VP1-mNG to the recovery could confound the interpretation, and the authors' explanation, while plausible, is not experimentally tested.
- **Resolution test** Provide a detailed description of the FRAP protocol, including the bleach region size, bleach depth, imaging acquisition rate, and the normalization and fitting procedures. Report the number of puncta and cells analyzed per condition, and include representative FRAP curves with error bars. To address the potential confound of unbound VP1-mNG, perform a control experiment where the mobile fraction of VP1-mNG is measured in the absence of puncta, or use a photoactivatable or photoconvertible tag on VP3 to directly measure its dynamics.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The authors state that "the minimal components required for the formation of phase-separated biomolecular condensates were VP3, VP1, and likely vRNA."
- **Evidence pointer** Results section "VP3 and VP1, in the presence of a vRNA template, are the minimal components necessary for the formation of phase-separated biomolecular condensates"; Figure 3 and Figure 4
- **Concern** The claim that vRNA is a required component is based on the observation that co-expression of VP3 and VP1 alone (without vRNA) resulted in puncta with limited FRAP recovery, whereas co-expression of VP3 with the full SegB (which provides vRNA) resulted in more liquid-like puncta. However, the authors did not directly test the requirement for vRNA. The difference in FRAP recovery could be due to other factors, such as the presence of other viral proteins or the level of VP1 expression. The authors acknowledge this limitation in the discussion, but the claim as stated in the results is not fully supported by the data.
- **Why it matters** Defining the minimal components is a key claim of the manuscript. If vRNA is not directly tested, the claim remains speculative and could be misleading. The distinction between "likely" and "demonstrated" is important for the field, as it affects how the model is interpreted and used in future studies.
- **Resolution test** Perform a direct test of vRNA requirement by, for example, co-expressing VP3 and VP1 in the presence of a non-viral RNA or in the presence of an RNA-binding mutant of VP3 that cannot bind vRNA. Alternatively, use an in vitro reconstitution system with purified VP3, VP1, and defined RNA to demonstrate that RNA is required for phase separation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Mechanistic insight
- **Claim pointer** The authors propose that the C-terminal IDR of VP3 promotes puncta formation and modulates their physical properties, but the mechanistic basis for this is not explored.
- **Evidence pointer** Results sections "The C-terminal IDR is not required for the recruitment of IBDV VP3 into VFs" and "The IBDV VP3 C-terminal IDR promotes the formation of cytoplasmic puncta and influences their size and shape"; Figure 10 and Figure 11
- **Concern** The manuscript demonstrates a phenotypic effect of the IDR on puncta formation and properties, but does not provide a mechanistic explanation for how the IDR achieves this. For example, does the IDR mediate multivalent interactions with other proteins or RNA? Does it affect the diffusion of VP3 within the condensate? Does it alter the surface tension or viscosity of the condensate? The authors speculate that the IDR may interact with VP1 or other client molecules, but this is not tested.
- **Why it matters** Understanding the mechanism by which the IDR modulates condensate properties is crucial for a complete understanding of the system and for generalizing the findings to other IDR-containing proteins. Without mechanistic insight, the study remains largely descriptive.
- **Resolution test** Perform experiments to test the mechanism, such as: (i) mutagenesis of specific residues within the IDR to disrupt predicted interaction motifs; (ii) in vitro binding assays to test whether the IDR interacts with VP1 or RNA; (iii) measurement of condensate viscosity or surface tension using optical tweezers or fluorescence recovery after photobleaching with varying bleach sizes; (iv) FRAP analysis of a VP3 mutant with a disrupted IDR to assess the role of the IDR in VP3 dynamics.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Statistical rigor
- **Claim pointer** The authors report significant differences in puncta number, size, and morphology between wild-type and ΔC conditions, but the statistical details are not fully reported.
- **Evidence pointer** Results section "The IBDV VP3 C-terminal IDR promotes the formation of cytoplasmic puncta and influences their size and shape"; Figure 10
- **Concern** The authors state that "puncta were detected at a significantly reduced rate (P < 0.0001)" and that "the mean number of puncta per cell was significantly reduced in the ΔC system compared to wt (P < 0.0001)." However, the specific statistical test used (e.g., Mann-Whitney U test, as mentioned in the methods) is not consistently reported for all comparisons, and effect sizes or confidence intervals are not provided. Additionally, the number of independent experiments and the total number of cells analyzed are not clearly stated for each comparison.
- **Why it matters** Transparent and complete reporting of statistical methods and results is essential for the reproducibility and credibility of the findings. The lack of detail makes it difficult for readers to assess the robustness of the reported differences.
- **Resolution test** Provide a comprehensive statistical summary for all quantitative comparisons, including the test used, the sample size (number of cells, number of independent experiments), the test statistic, the degrees of freedom, and the effect size with confidence intervals. Consider using a figure with individual data points overlaid on box plots to show the distribution of the data.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 2
- **Evidence pointer** Results section "VP3 is necessary but not sufficient to drive the formation of cytoplasmic puncta"
- **Issue** The description of the tag comparison in Figure 2 is brief. It is unclear how many tags were tested and whether the images shown are representative of all experiments. The authors state that "the pattern of the TC::VP3 and mNG::VP3 fluorescence signals was also consistent with this observation," but it would be helpful to see a quantitative comparison of the distribution patterns (e.g., diffuse vs. punctate) across the different tags.
- **Required correction** Provide a more detailed description of the tag comparison, including the number of tags tested, the number of independent experiments, and a quantitative analysis of the distribution patterns (e.g., percentage of cells with puncta) for each tag.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Figure 4
- **Evidence pointer** Results section "VP3 and VP1, in the presence of a vRNA template, are the minimal components necessary for the formation of phase-separated biomolecular condensates"
- **Issue** The FRAP data in Figure 4 are described in the text, but the figure itself is not shown in the provided manuscript. It is unclear whether the figure includes representative recovery curves, the number of puncta analyzed, and the statistical comparison between conditions.
- **Required correction** Ensure that Figure 4 includes representative FRAP curves with error bars, the number of puncta and cells analyzed, and the statistical test used to compare the mobile fractions.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion section
- **Evidence pointer** Discussion, paragraph on the role of the C-terminal IDR
- **Issue** The authors suggest that the IDR may "interface with other client biomolecules" but do not elaborate on what these might be or how they would be identified. This is a speculative statement that could be strengthened by referencing specific candidate interactors or proposing experimental approaches to identify them.
- **Required correction** Expand the discussion to include specific hypotheses about the identity of potential client molecules and suggest experimental approaches (e.g., proximity labeling, cross-linking mass spectrometry) to identify them.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Methods section "MD simulations"
- **Evidence pointer** Methods "MD simulations"
- **Issue** The description of the MD simulations is brief. The authors state that simulations were 20 nanoseconds in duration and used the OPLS-AA/L force field, but they do not provide details on the system setup (e.g., solvation, ionic strength, temperature coupling), the number of replicates, or the convergence criteria. This makes it difficult to assess the reliability of the simulations.
- **Required correction** Provide a more detailed description of the MD simulation setup, including the system size, solvation model, equilibration protocol, and the number of independent simulations. Include an analysis of convergence (e.g., root-mean-square deviation of the protein backbone over time).

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure 10
- **Evidence pointer** Results section "The IBDV VP3 C-terminal IDR promotes the formation of cytoplasmic puncta and influences their size and shape"
- **Issue** The figure legend for Figure 10 is not provided in the manuscript text. It is unclear what exactly is plotted in panels A through F and how the data were normalized.
- **Required correction** Provide a complete figure legend for Figure 10, including a description of each panel, the units of measurement, and the normalization procedure.

## Risk / unsupported claims
- The claim that vRNA is a required component for phase separation is not directly tested and is therefore unsupported by the current data.
- The claim that the C-terminal IDR "modulates the physical properties" of puncta is supported by FRAP and morphology data, but the mechanistic basis for this modulation is not established.
- The claim that the C-terminal IDR is "highly dynamic" is based on MD simulations, but the simulations are not described in sufficient detail to assess their reliability, and the experimental validation of this prediction is lacking.
- The statement that "the minimal components required for the formation of phase-separated biomolecular condensates were VP3, VP1, and likely vRNA" is presented as a conclusion, but the "likely" qualifier indicates uncertainty that is not fully resolved by the data.