## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) from bioRxiv preprint
- **Assessment boundary** Scientific content, technical soundness, and claim support based solely on the provided text; no external validation or supplementary figure inspection possible
- **Shared manuscript claim summary** The authors report that the Hsp90 co-chaperones p23 and FKBP51 form a complex that inhibits tau aggregation in an Hsp90-independent manner. They propose a structural model of the p23-FKBP51 interaction, map the tau-binding site to the C-terminal disordered tail of p23, and suggest formation of a dynamic p23-FKBP51-tau trimeric complex that may counteract Hsp90-FKBP51-mediated toxicity.
- **Visible evidence base** In vitro ThT aggregation kinetics; NMR titration data (1H-15N TROSY HSQC, 1H-13C HMQC); SEC-SAXS envelopes; HADDOCK docking model; site-directed mutagenesis validation
- **Missing materials affecting confidence** Supplementary figures (Supplementary Fig. 1-4), Supplementary Tables 1-2, full NMR assignment details, SAXS fitting statistics, docking score distributions, raw ThT traces, negative controls, and statistical analyses are not provided in the supplied text

## Reviewer
- **Overall assessment** The manuscript addresses a timely and potentially important question in tau biology: whether Hsp90 co-chaperones can directly modulate tau aggregation independently of Hsp90. The combination of NMR, SAXS, docking, and mutagenesis is appropriate and potentially powerful. However, the evidence as presented is incomplete in several critical respects. The claim of cooperative inhibition of tau aggregation by p23 and FKBP51 rests on ThT data that are described qualitatively, with no statistical treatment or quantification of replicates. The structural model of the p23-FKBP51 complex is based on docking with limited experimental restraints, and the validation via mutagenesis is described only in supplementary material. The most significant gap is the absence of direct evidence for a stable trimeric p23-FKBP51-tau complex; the NMR data shown support binary interactions but not simultaneous ternary complex formation. The functional relevance of the proposed trimeric complex to cellular tau toxicity is speculative. The manuscript is well written and the conceptual framework is clear, but the current evidence base does not fully establish the central claims.
- **Who would be interested in the results, and why** Researchers studying tau aggregation mechanisms, molecular chaperone biology, Hsp90 co-chaperone functions, and the molecular basis of neurodegeneration. The work may also interest structural biologists using integrative approaches (NMR, SAXS, docking) to study protein-protein interactions involving intrinsically disordered proteins. The potential therapeutic angle regarding co-chaperone-specific targeting could attract drug discovery groups focused on tauopathies.
- **Major strengths** 1) The question is well motivated and clinically relevant. 2) The integrative structural biology approach is appropriate for studying dynamic, partially disordered complexes. 3) The finding that p23 and FKBP51 act cooperatively rather than additively is potentially novel and interesting. 4) The identification of the C-terminal tail of p23 as the tau-interacting region provides a clear mechanistic hypothesis. 5) The writing is clear and accessible.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative rigor of aggregation data), R1-M2 (evidence for trimeric complex), R1-M3 (structural model validation), R1-M4 (functional relevance claims)
- **Assessment against Nature-style criteria** Originality: The concept of Hsp90-independent chaperoning of tau by a co-chaperone complex is original and potentially significant. However, the novelty is partially tempered by prior work on p23 and FKBP51 individually. Scientific importance: High, given the prevalence of tauopathies and the need for specific therapeutic targets. Interdisciplinary readership: The work bridges structural biology, biophysics, and neurodegeneration, which could attract a broad audience. Technical soundness: The methods are appropriate but the presented evidence is incomplete in several areas (quantification, controls, validation details). Readability for nonspecialists: The manuscript is generally well written, but some sections assume familiarity with NMR and SAXS terminology. Overall, the manuscript has potential for a high-impact venue, but the current evidence does not yet meet the standard required for Nature.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising and the approach is sound, but the evidence as presented is insufficient to fully establish the claims of cooperative inhibition, trimeric complex formation, and functional relevance.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative rigor of aggregation data
- **Claim pointer** The authors claim that p23 and FKBP51 cooperatively inhibit tau aggregation, with the combination showing greater attenuation than either protein alone.
- **Evidence pointer** Results section "p23-FKBP51 cooperatively modulate tau aggregation"; Figure 1c,d; Supplementary Fig. 1
- **Concern** The ThT aggregation data are described qualitatively. No replicate numbers, error bars, statistical tests, or quantitative metrics (e.g., lag time, Tm, apparent rate constants) are provided. The claim of cooperativity requires demonstration that the effect of the combination is greater than the sum or expected additive effect of the individual components, which is not shown. Additionally, the observation that FKBP51 alone increases final ThT intensity while p23 alone does not is not mechanistically explained. The statement that "quantification of the supernatant suggested a lower amount of aggregated tau" at high ThT intensity is contradictory and requires reconciliation.
- **Why it matters** The central functional claim of the manuscript rests on these aggregation data. Without quantitative rigor, the conclusion that p23 and FKBP51 act cooperatively is not established.
- **Resolution test** Provide full ThT kinetic traces with at least three independent replicates, error bars, and appropriate statistical comparisons (e.g., one-way ANOVA with post-hoc tests). Quantify lag time, Tm, and final ThT intensity for each condition. Demonstrate that the combination effect is significantly greater than additive. Address the discrepancy between ThT intensity and sedimented tau quantification.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence for trimeric complex formation
- **Claim pointer** The authors state that p23-FKBP51 binds tau to form a dynamic p23-FKBP51-tau trimeric complex.
- **Evidence pointer** Results section "p23-FKBP51-tau trimeric complex formation"; Figure 6
- **Concern** The NMR data presented support binary interactions: p23 binds FKBP51 (Fig. 2), and p23 binds tau via its C-terminal tail (Fig. 6a-d). However, no experiment directly demonstrates simultaneous binding of p23 to both FKBP51 and tau in a ternary complex. The proposed trimeric complex is inferred from the binary interaction data. Techniques such as three-component NMR titrations, size-exclusion chromatography with ternary mixtures, or cross-linking mass spectrometry would be needed to substantiate the trimeric complex claim.
- **Why it matters** The trimeric complex is central to the proposed model of how p23-FKBP51 inhibits tau aggregation. Without direct evidence, the model remains speculative.
- **Resolution test** Perform a three-component NMR titration (p23 + FKBP51 + tau) and show that residues on p23 that bind FKBP51 and tau are simultaneously engaged. Alternatively, use SEC-MALS or AUC with a ternary mixture to demonstrate formation of a complex with the expected molecular weight. Provide binding affinities for each binary interaction and show that they are compatible with ternary complex formation at the concentrations used.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Structural model validation
- **Claim pointer** The authors present a HADDOCK-derived structural model of the p23-FKBP51 complex and validate it with site-directed mutagenesis of R88 and R93.
- **Evidence pointer** Results section "Structure of the p23-FKBP51 complex"; Figure 4; Supplementary Fig. 3
- **Concern** The docking model is based on ambiguous restraints derived from CSP data, and the validation is described only in supplementary material. The manuscript does not report docking scores, cluster statistics beyond RMSD, or a comparison with alternative models. The mutagenesis data (R88A/R93A) are stated to show reduced binding, but the extent of reduction and the specificity of the effect are not quantified. It is unclear whether the mutation disrupts the p23-FKBP51 interaction globally or only locally.
- **Why it matters** The structural model is a key deliverable of the manuscript. Without rigorous validation and transparent reporting of docking statistics, the model cannot be evaluated by the community.
- **Resolution test** Provide full docking statistics (HADDOCK scores, Z-scores, cluster populations, restraint satisfaction). Show the mutagenesis data quantitatively (e.g., binding affinities or NMR intensity ratios for mutant vs. wild-type). Include a control mutation in a region not predicted to be at the interface. Consider validating the model with an orthogonal technique such as cross-linking mass spectrometry or paramagnetic relaxation enhancement NMR.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Functional relevance claims
- **Claim pointer** The authors suggest that the p23-FKBP51 complex may counteract Hsp90-FKBP51 mediated toxicity and play a protective role.
- **Evidence pointer** Abstract; Discussion; Figure 7
- **Concern** The functional relevance of the proposed trimeric complex to cellular tau toxicity is entirely speculative. No cellular or in vivo experiments are presented. The relationship between the in vitro aggregation inhibition and the proposed protective role in cells is not established. The model shown in Figure 7 is a schematic without experimental support.
- **Why it matters** The broader significance of the work depends on the functional relevance of the proposed mechanism. Speculative claims without experimental support weaken the manuscript.
- **Resolution test** Provide cellular data, such as tau aggregation assays in cells with overexpression or knockdown of p23 and FKBP51, or demonstrate that the p23-FKBP51 complex affects tau toxicity in a relevant model system. Alternatively, temper the claims in the discussion to clearly distinguish speculation from established findings.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 1
- **Evidence pointer** Results section "p23-FKBP51 cooperatively modulate tau aggregation"
- **Issue** The ThT curves in Figure 1c are described but not shown in the provided text. The reader cannot assess the quality of the data or the magnitude of the effects.
- **Required correction** Ensure that representative ThT traces are shown with clear labeling of conditions and replicates. Consider showing normalized curves to facilitate comparison.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** NMR experiments
- **Evidence pointer** Methods section "NMR Spectroscopy"
- **Issue** The NMR experiments are described briefly. Key parameters such as temperature, NMR buffer composition, and data processing details are not provided. The assignment transfer for FKBP51 methyl groups is mentioned but not described.
- **Required correction** Provide complete NMR experimental parameters, including temperature, buffer, and referencing. Describe how assignments were transferred and the confidence in those assignments.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Throughout results
- **Evidence pointer** Results sections
- **Issue** No statistical analyses are reported for any of the quantitative claims, including CSP values, intensity ratios, or aggregation kinetics.
- **Required correction** Add appropriate statistical tests and report p-values or confidence intervals for all quantitative comparisons.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction and Discussion
- **Evidence pointer** Introduction; Discussion
- **Issue** The discussion of FKBP51's role in tau biology is brief. The authors mention prior work on FKBP51-tau interactions but do not fully contextualize their findings against the existing literature on FKBP51 as a tau aggregation enhancer.
- **Required correction** Expand the discussion to more thoroughly address how the proposed protective p23-FKBP51 complex relates to the known pro-toxic functions of FKBP51, and how the two activities might be reconciled.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity of model
- **Affected element** Figure 7
- **Evidence pointer** Discussion
- **Issue** The schematic model in Figure 7 is described only in the text. The relationship between the Hsp90-dependent and Hsp90-independent pathways is not clearly delineated.
- **Required correction** Provide a clear figure legend and ensure the schematic accurately represents the proposed model, distinguishing established findings from speculative elements.

## Risk / unsupported claims
- The claim that p23 and FKBP51 act cooperatively to inhibit tau aggregation is not quantitatively supported by the provided data.
- The existence of a stable p23-FKBP51-tau trimeric complex is inferred but not directly demonstrated.
- The structural model of the p23-FKBP51 complex is based on docking with limited experimental validation.
- The proposed protective role of the p23-FKBP51 complex in counteracting Hsp90-FKBP51 mediated toxicity is speculative and not supported by functional experiments.
- The statement that FKBP51 alone does not modulate tau aggregation kinetics is based on qualitative ThT data and is contradicted by the observed increase in final ThT intensity.
- The claim that the C-terminal tail of p23 interacts with the positively charged C-terminal half of tau is supported by NMR data, but the functional significance of this interaction for aggregation inhibition is not established.