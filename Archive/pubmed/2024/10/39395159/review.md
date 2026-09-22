## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions) and metadata (title, authors, journal, DOI, URL)
- **Assessment boundary** Scientific content, methodological soundness, evidence quality, and alignment with stated claims. No assessment of formatting, grammar, or editorial fit beyond Nature-style criteria.
- **Shared manuscript claim summary** The authors use all-atom molecular dynamics simulations of two-heptad CTD models to show that phosphorylation patterns and salt concentration modulate clustering via a balance of interpeptide H-bonds, intrapeptide interactions, and Na+ ion bridging between phosphate groups.
- **Visible evidence base** Main text figures (Figures 1–8), tables (Table 1, Table 2), and references to supplementary figures (Figures S1–S16, Tables S1–S3). Supplementary material itself was not provided.
- **Missing materials affecting confidence** Supplementary figures and tables (S1–S16, S1–S3) are referenced but not available. Simulation input files, force field parameter details, and raw trajectory data are not provided. Mutation simulation details (system setup, length, analysis) are only partially described.

## Reviewer
- **Overall assessment** The manuscript addresses a relevant question in the field of Pol II CTD phase separation, using a tractable model system and extensive all-atom simulations. The work is technically sound in its core simulation methodology, and the analysis of clustering, H-bonding, and ion bridging is generally careful. However, the study's scope is limited to a two-repeat model, and the authors themselves acknowledge that this is far shorter than physiologically relevant CTDs. The central claims about phosphorylation-dependent clustering are supported by the data shown, but the generalizability to full-length CTD and the link to phase separation remain speculative. The manuscript would benefit from clearer quantitative comparisons across conditions and a more direct discussion of limitations.
- **Who would be interested in the results, and why** Researchers studying Pol II CTD function, intrinsically disordered proteins, phase separation, and the role of post-translational modifications in transcription regulation. The methodological approach (all-atom MD of short CTD models) may also interest computational biophysicists working on IDP clustering and ion-mediated interactions.
- **Major strengths** (1) Systematic exploration of multiple phosphorylation patterns, salt concentrations, and protein concentrations. (2) Use of multiple complementary analyses (cluster size distributions, diffusion coefficients, Rg, H-bond counts, contact maps, ion bridging). (3) Clear presentation of complex data in figures. (4) Honest discussion of limitations and future directions.
- **Major Concerns** See items below.
- **Minor Comments** See items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (generalizability), R1-M2 (quantitative rigor), R1-M3 (mutation simulation analysis).
- **Assessment against Nature-style criteria** Originality: moderate. The work applies known methods to a specific system, and the finding of ion-mediated clustering is not entirely novel but adds to a growing body of work. Scientific importance: moderate. The study provides molecular-level insight into CTD clustering, but the model's short length limits direct relevance to full-length CTD phase separation. Interdisciplinary readership: limited. The work is primarily of interest to biophysicists and computational chemists; the link to transcription regulation is not developed enough to attract a broad biological audience. Technical soundness: generally good, with caveats noted in Major Concerns. Readability for nonspecialists: the manuscript is written in a clear style, but the methods and results assume familiarity with MD simulations and IDP concepts.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding the quantitative analysis and the interpretation of the two-repeat model's relevance.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability / claim scope
- **Claim pointer** The authors state that their results provide "insights into the clustering behavior and molecular interactions driving the cluster formation" and suggest implications for "the LLPS occurring in full human CTD" (Introduction, Results).
- **Evidence pointer** Results section, Discussion section
- **Concern** The study uses a two-heptad model (2CTD), which is far shorter than the 26 or 52 repeats in yeast and human CTD. The authors acknowledge this limitation but still frame their findings as relevant to full-length CTD phase separation. The clustering behavior of a two-repeat peptide may not capture the cooperative effects, multivalency, and network formation that occur in longer CTDs. The claim that "phase separation may occur for the 2CTD-non-phos system with a 25 mM protein concentration" (Results) is based on a single concentration and a short peptide, and the authors themselves note this requires validation. The central claim that phosphorylation modulates clustering in a way that is relevant to CTD phase separation is not established from the two-repeat model alone.
- **Why it matters** The manuscript's stated goal is to understand CTD clustering in the context of phase separation. If the model system is too short to capture the relevant physics, the conclusions may not transfer to the biological system of interest. The authors need to either provide evidence that two repeats capture the essential features of longer CTDs or temper their claims about relevance to full-length CTD.
- **Resolution test** The authors should either (a) perform simulations with longer CTD models (e.g., 4-8 repeats) to test whether the observed trends hold, or (b) explicitly reframe the conclusions to state that the findings apply to short CTD models and that extrapolation to full-length CTD requires further study. The Discussion should more clearly separate what is demonstrated (clustering of 2CTD models) from what is speculative (implications for full-length CTD phase separation).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative rigor / statistical support
- **Claim pointer** The authors report differences in clustering, H-bond counts, and diffusion coefficients across conditions (e.g., "phosphorylated systems display higher cluster sizes compared to the nonphosphorylated state except for the case of 2CTD-2P–5P at 0 mM NaCl").
- **Evidence pointer** Results section, Figures 1, 4, 5, Table 2
- **Concern** The manuscript does not report error bars, standard deviations, or statistical significance tests for the reported quantities. For example, Figure 1 shows distributions of largest cluster sizes, but it is unclear how many independent simulations or replicate runs were performed. The diffusion coefficients in Table 2 are presented without uncertainties. Without error estimates, it is difficult to assess whether the observed differences between conditions are meaningful or within statistical noise.
- **Why it matters** The conclusions rely on comparisons between different phosphorylation states and salt concentrations. If the differences are not statistically robust, the central claims about phosphorylation-dependent clustering are weakened. The authors should provide error estimates or at least state the number of independent simulations and the variability observed.
- **Resolution test** The authors should add error bars or confidence intervals to the reported quantities, or state the number of replicate simulations and the standard deviation across replicates. If replicates were not performed, this should be acknowledged and the results treated as preliminary.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Completeness of analysis / control experiments
- **Claim pointer** The authors state that mutation simulations (Y-to-A, T-to-A, P-to-A) were performed as controls, and that "We observed a decreased number of clustering when Y or P were mutated" and "an increase in clustering for the T-A mutations."
- **Evidence pointer** Results section, Figures S15, S16
- **Concern** The mutation simulations are described only briefly, and the results are only shown in the supplementary material. The manuscript does not provide details on how the mutations were introduced, whether the simulations were run for the same length and with the same protocol as the wild-type, or how the clustering was quantified for these controls. The claim that T-to-A mutations increase clustering is interesting but is not explained mechanistically. The contact map analysis for the T-A mutant is mentioned but not shown in the main text.
- **Why it matters** The mutation simulations are used to support the role of specific residues in clustering. If these controls are not rigorously described and analyzed, the conclusions about the importance of Y, P, and T residues are not fully supported.
- **Resolution test** The authors should provide a more detailed description of the mutation simulations in the Methods, including system setup, simulation length, and analysis. The results should be presented in the main text or at least summarized with quantitative comparisons to the wild-type. The mechanistic explanation for the T-A effect should be elaborated.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Simulation protocol
- **Evidence pointer** Computational Methods section
- **Issue** The description of the equilibration protocol is somewhat unclear. The text states that restraints were "turned on for the initial 625 ps of equilibration and turned off for the last 375 ps," but it is not specified which atoms were restrained and with what force constants during the last 375 ps. Additionally, the temperature coupling scheme and pressure control (if any) are not described.
- **Required correction** Clarify the restraint protocol and specify the thermostat and barostat settings used during equilibration and production runs.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Interpretation of results
- **Affected element** Discussion of phase separation
- **Evidence pointer** Results section, Discussion section
- **Issue** The authors suggest that the 25 mM 2CTD-non-phos system may show phase separation based on the coexistence of small and large clusters. However, this interpretation is speculative, as the authors do not provide any quantitative measure of phase separation (e.g., density profiles, order parameters, or comparison to known phase boundaries). The statement is also based on a single concentration.
- **Required correction** Either provide additional analysis to support the claim of phase separation or soften the language to indicate that the observation is suggestive but not conclusive.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion of ion-mediated interactions
- **Evidence pointer** Discussion section
- **Issue** The authors mention that ion-mediated condensation has been observed for nucleic acids, but they do not discuss the broader literature on ion-mediated interactions in IDPs or protein-RNA systems. A brief discussion of how their findings fit into this context would strengthen the manuscript.
- **Required correction** Add a few sentences in the Discussion to place the ion-bridging observation in the context of other studies on ion-mediated interactions in biomolecular condensates.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Figure presentation
- **Affected element** Figure 1
- **Evidence pointer** Results section, Figure 1
- **Issue** The cluster size distributions in Figure 1 are presented as histograms, but the y-axis label is not specified. It is unclear whether the y-axis represents probability, frequency, or percentage. This makes it difficult to interpret the distributions quantitatively.
- **Required correction** Add a clear y-axis label to Figure 1 and specify the units or normalization used.

## Risk / unsupported claims
- The claim that "phase separation may take place" for the 25 mM 2CTD-non-phos system is not supported by quantitative analysis and is based on a single concentration. This is speculative and should be labeled as such.
- The statement that "the role of counterion interactions in clustering and condensate formation by phosphorylated CTDs might be underestimated" is presented as a suggestion, but the authors do not provide direct evidence that this applies to full-length CTD. This is an extrapolation from the 2-repeat model.
- The claim that "the systems are in the liquid character" based on the magnitude of diffusion coefficient reduction is not well supported, as the authors do not provide a clear threshold or comparison to known liquid-like systems.
- The mutation simulation results are only shown in the supplementary material and are not described in sufficient detail to fully evaluate the claims about the role of Y, P, and T residues.