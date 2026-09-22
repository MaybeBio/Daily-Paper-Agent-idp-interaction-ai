## Review setup
- **Input scope** Full manuscript text (abstract, main text, figure captions referenced but not provided, supplementary material referenced but not provided)
- **Assessment boundary** Scientific content, methodological soundness, evidence quality, and claims as presented in the supplied text. Figures, tables, movies, and supplementary documents are referenced but were not available for inspection.
- **Shared manuscript claim summary** The authors present SimHS-AFMfit-MD, an integrative pipeline combining high-speed atomic force microscopy (HS-AFM), molecular dynamics (MD) simulations, and AFMfit-based structural fitting (with nonlinear normal mode analysis, NOLB) to infer atomic-resolution conformational dynamics of alpha-actinin. They report that AFMfit-MD (guided by MD trajectories) outperforms AFMfit-NMA, that the resulting conformational libraries align with unbiased all-atom MD simulations, and that Ca2+ binding slightly reduces flexibility in the CH1-CH2 and EF12-EF34 domains near the neck. PCA of the generated ensembles identifies bending (PC1, PC2) and twisting (PC3) modes.
- **Visible evidence base** Abstract, main text narrative, references to Figures 1-5 (captions not provided), Tables S1-S3, Movies S1-S6, and Supplementary Methods (none of these items were supplied for review)
- **Missing materials affecting confidence** All figures, tables, movies, and supplementary methods. Quantitative results (RMSF values, PCA projections, statistical tests, fitting accuracies) are described but cannot be verified. The manuscript text contains placeholder figure references (e.g., "Figure  ") that could not be resolved.

## Reviewer
- **Overall assessment** The manuscript addresses a timely and technically challenging problem: extracting atomic-resolution conformational dynamics from low-resolution HS-AFM images. The proposed integrative pipeline is conceptually appealing and builds on established tools (AFMfit, NOLB, MD). However, the provided text alone does not contain sufficient quantitative evidence to evaluate the central claims. Key results are described qualitatively, and all supporting data (figures, tables, movies, methods) are absent from the review package. The claim that AFMfit-MD outperforms AFMfit-NMA, the validation against independent MD simulations, and the biological conclusion regarding Ca2+ effects on alpha-actinin flexibility all require the missing evidence to be assessed. The manuscript also contains a substantial amount of background discussion on NMR and cryo-EM limitations that appears tangential to the core methodology.
- **Who would be interested in the results, and why** Researchers in biophysics, structural biology, and computational chemistry, particularly those working on integrative methods combining experimental imaging with simulation. The approach could interest groups studying flexible proteins, intrinsically disordered proteins, and large multidomain complexes that resist conventional structural characterization. Developers of AFM analysis tools and MD-based fitting methods would also find the methodological advances relevant.
- **Major strengths** The conceptual integration of HS-AFM with MD-guided fitting is a sensible and potentially powerful strategy. The use of nonlinear normal mode analysis (NOLB) for flexible fitting is appropriate. The choice of alpha-actinin as a model system is well justified given its size, flexibility, and biological importance. The authors explicitly address the challenge of weak surface adsorption and electrostatic screening, which is a critical practical consideration for HS-AFM of dynamic proteins. The PCA-based classification of conformational ensembles is a reasonable approach for comparing different methods.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (missing quantitative evidence for fitting performance), R1-M2 (validation logic requires independent data), R1-M3 (biological conclusion not supported by visible data), R1-M4 (statistical reporting incomplete)
- **Assessment against Nature-style criteria** Originality: The combination of HS-AFM, AFMfit, and MD in a single pipeline is novel, though each component is established. Scientific importance: Potentially high if the method is shown to reliably recover atomic dynamics from HS-AFM data, but this is not established from the provided text. Interdisciplinary readership: The topic bridges microscopy, simulation, and structural biology, which could attract broad interest. Technical soundness: Cannot be assessed without figures, tables, and methods. Readability for nonspecialists: The main text is generally clear, but the extensive background on NMR and cryo-EM limitations is distracting and not well integrated with the core narrative.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript may be supportable if the missing quantitative data are supplied and the concerns below are addressed.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that "guiding AFMfit with MD trajectories (AFMfit-MD) significantly improves fitting performance, aligning closely with unbiased all-atom MD simulations."
- **Evidence pointer** Main text section "Investigating Alpha-Actinin Dynamics at the Atomic Level via SimHS-AFMfit-MD"; Figures 2-3 (not provided); Table S2 (not provided)
- **Concern** The central methodological claim of the paper is that AFMfit-MD outperforms AFMfit-NMA. However, no quantitative metrics (e.g., RMSD to reference, correlation coefficients, fitting scores) are reported in the text. The comparison is described only qualitatively ("more closely aligned," "significantly improves"). Without numerical results or the corresponding figures, the performance advantage cannot be evaluated.
- **Why it matters** This is the core technical contribution of the manuscript. If the improvement is marginal or only present under specific conditions, the general utility of the method is weakened. The claim of "significant" improvement requires statistical support and clear reporting of effect sizes.
- **Resolution test** Provide quantitative fitting metrics (e.g., RMSD, TM-score, or similar) for AFMfit-NMA versus AFMfit-MD across the full dataset, with error bars and statistical tests. Show representative fits in figures with clear visual comparison.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation logic
- **Claim pointer** The authors state that "The resulting fluctuation profiles and dominant dynamic modes derived from the independent MD simulations are consistent with, yet statistically independent from, the conformational dynamics inferred from SimHS-AFMfit-MD. This agreement therefore provides an orthogonal validation of our approach."
- **Evidence pointer** Main text section "Classifying the Dynamic Atomic Conformations of Alpha-Actinin via PCA"; Figures 4-5 (not provided); Figure S5 (not provided)
- **Concern** The validation logic is circular if the MD simulations used for validation are the same as those used to guide AFMfit-MD. The text mentions "independent MD simulations" for validation, but it is unclear whether these are truly independent (different initial conditions, force fields, or run lengths) or simply a held-out portion of the same trajectories. The distinction is critical for the claim of orthogonal validation.
- **Why it matters** If the validation MD simulations are not genuinely independent, the agreement between AFMfit-MD and MD is expected by construction and provides no independent confirmation that the AFM-derived conformations are physically meaningful.
- **Resolution test** Clearly describe the relationship between the guiding MD trajectories and the validation MD simulations. If they are the same, remove the claim of orthogonal validation. If they are different, specify the differences (e.g., force field, initial structure, simulation length, random seed) and show that the validation results are robust across these variations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Biological claim support
- **Claim pointer** The authors conclude that "Ca2+ binding slightly reduced the motion of the CH1-CH2 and EF12-EF34 domains near the neck in muscle alpha-actinin."
- **Evidence pointer** Main text sections "Ca2+ Binding Affects Smooth Muscle Alpha-Actinin Flexibility" and "Classifying the Dynamic Atomic Conformations of Alpha-Actinin via PCA"; Figures 1, 4 (not provided); Table S1 (not provided)
- **Concern** The biological conclusion is based on comparisons between Ca2+-bound and Ca2+-unbound states using HS-AFM height measurements and the derived conformational ensembles. The text reports mean heights of 5.7 ± 0.9 nm (N = 3040) and 4.8 ± 0.7 nm (N = 6080) for bound and unbound states, respectively, with p < 0.05. However, the effect size is small relative to the standard deviations, and the text does not report the statistical test used, whether multiple comparisons were corrected, or whether the height difference is biologically meaningful. The connection between reduced height and reduced flexibility is not established.
- **Why it matters** The biological interpretation is a key selling point of the paper. If the Ca2+ effect is not robustly supported, the significance of the method for biological discovery is diminished.
- **Resolution test** Report the specific statistical test, effect size (e.g., Cohen's d), and confidence intervals for the height comparison. Provide independent evidence (e.g., from the conformational ensembles) that the reduced height corresponds to reduced flexibility. Discuss whether the observed difference is within the expected noise of HS-AFM measurements.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The manuscript describes a four-step pipeline (acquisition, AFM fitting, MD simulations, PCA) but the text contains placeholder figure references (e.g., "Figure  ") and refers to "SI Methods" for critical details.
- **Evidence pointer** Main text sections "Overview of the Methodology" and "Investigating Alpha-Actinin Dynamics at the Atomic Level"; Supplementary Methods (not provided)
- **Concern** The main text does not provide sufficient detail to reproduce the pipeline. Key parameters (e.g., AFM tip geometry, scan rate, force constants for NOLB, MD force field, water model, simulation temperature, pressure coupling, number of replicas) are not stated. The placeholder figure references suggest the manuscript is incomplete or the figures were not properly inserted.
- **Why it matters** Reproducibility is a fundamental requirement for methodological papers. Without detailed methods, other groups cannot apply or validate the approach.
- **Resolution test** Provide a complete Methods section (either in the main text or supplementary) with all parameters, software versions, and analysis scripts. Ensure all figure references are correctly inserted.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Background discussion on NMR and cryo-EM
- **Evidence pointer** Main text section "Classifying the Dynamic Atomic Conformations of Alpha-Actinin via PCA" (paragraphs on time-resolved cryo-EM and NMR)
- **Issue** The manuscript includes several paragraphs discussing the limitations of NMR and cryo-EM for studying protein dynamics. While relevant to the motivation, this material is lengthy and not directly connected to the results or the specific advantages of the proposed method.
- **Required correction** Condense this background to a few sentences that directly contrast the proposed approach with existing methods, and move the detailed discussion to the introduction or a supplementary note.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Height and length measurements
- **Evidence pointer** Main text section "Ca2+ Binding Affects Smooth Muscle Alpha-Actinin Flexibility"; Table S1 (not provided)
- **Issue** The text reports mean ± SD for heights and lengths but does not specify the number of molecules vs. number of frames, whether measurements are independent, or how the semiautomated tracking handles tracking errors or molecule drift.
- **Required correction** Clarify the unit of analysis (molecules, frames, or both), report the number of independent molecules, and describe quality control for tracking.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "Atomic resolution" and "atomic-scale"
- **Evidence pointer** Abstract and main text throughout
- **Issue** The manuscript uses "atomic resolution" and "atomic-scale" to describe the output of the pipeline. However, the input is HS-AFM data with nanometer-scale resolution, and the atomic detail comes from the MD simulations and fitting. This terminology could be misleading.
- **Required correction** Use more precise language, such as "atomistic detail inferred from integrative modeling" or "atomic-level conformational ensembles," and clarify that the resolution is derived from the simulation, not the imaging.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Figure references
- **Evidence pointer** Main text throughout
- **Issue** Multiple figure references appear as "Figure  " with no number or caption. This suggests the manuscript is incomplete or the figures were not properly formatted.
- **Required correction** Ensure all figure references are correctly numbered and that figure captions are included.

## Risk / unsupported claims
- The claim that AFMfit-MD "significantly improves" fitting performance over AFMfit-NMA is unsupported in the provided text, as no quantitative metrics are reported.
- The claim of "orthogonal validation" via independent MD simulations is unverifiable, as the relationship between guiding and validation simulations is not described.
- The biological conclusion that Ca2+ binding reduces flexibility in specific domains is based on small height differences with overlapping standard deviations and no reported effect size or robust statistical analysis.
- The statement that the method "converts thousands of 3D HS-AFM images into atomic-scale conformational ensembles" is not supported by any quantitative description of the ensemble generation or its accuracy.
- The discussion of potential applications (force field development, deep learning training data) is speculative and not supported by results in the provided text.