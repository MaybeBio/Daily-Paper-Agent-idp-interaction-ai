## Review setup
- **Input scope** Full manuscript text including abstract, results, discussion, experimental procedures, and figure legends
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and technical soundness based solely on the provided manuscript text
- **Shared manuscript claim summary** The manuscript identifies two putative B56-docking motifs (BS1 and BS2) in the CREB kinase-inducible domain, proposes that BS2 mediates constitutive PP2A-B56 recruitment for dephosphorylation of S133 and the CK cassette, and that BS1 may act as a signal-dependent low-affinity site. The authors use in vitro binding, phosphatase kinetics, cell-based overexpression, and a CRISPR-engineered mouse model to support these claims.
- **Visible evidence base** Figures 1–8 and Supplemental Figures S1–S6 as described in the text; no raw data, uncropped blots, or statistical source data are provided
- **Missing materials affecting confidence** Raw immunoblot images, uncropped gels, statistical source data with exact p-values and effect sizes, details of CRISPR off-target validation, ChIP-qPCR primer validation data, and full enzyme kinetics replicates

## Reviewer
- **Overall assessment** The manuscript addresses an important question in CREB signaling, namely how PP2A-B56 holoenzymes attenuate CREB activity through docking motifs. The identification of BS2 as a functional B56-binding site with in vivo validation is a valuable contribution. However, several technical concerns, particularly regarding the specificity of the BS2 mutations, the quantitative interpretation of the enzyme kinetics, and the incomplete characterization of the mouse model, limit the strength of the conclusions as currently presented.
- **Who would be interested in the results, and why** Researchers studying CREB signaling, protein phosphatase targeting mechanisms, and transcriptional burst attenuation. The work also has relevance for those interested in kinase-phosphatase balance in neuronal plasticity, metabolism, and cell growth, given CREB's central role in these processes.
- **Major strengths** The study combines biochemical, cellular, and in vivo approaches to address a mechanistically important question. The identification of a specific B56-docking motif in CREB and its validation in a knock-in mouse model is a significant step forward. The inclusion of structural modeling to rationalize the functional differences between BS1 and BS2 adds mechanistic depth.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** Originality is moderate to high, as the concept of docking-mediated PP2A targeting to CREB is not entirely new but the specific identification and in vivo validation of BS2 is novel. Scientific importance is substantial for the CREB field and for phosphatase biology. Interdisciplinary readership is limited, as the work is primarily of interest to signal transduction and transcription researchers. Technical soundness is adequate but with notable gaps in quantitative rigor and mutation specificity controls. Readability for nonspecialists is acceptable, though the Results section is dense and would benefit from clearer framing of the key questions.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly the mutation specificity controls and the quantitative interpretation of the enzyme kinetics.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "BS2 mutations increased baseline and stimulus-induced phosphorylation of S133" and that this is due to disrupted PP2A-B56 binding.
- **Evidence pointer** Figure 3A–D, Figure 5A–C
- **Concern** The E153D/A mutations are assumed to specifically disrupt B56 binding without affecting other CREB functions. However, the manuscript does not provide evidence that these mutations do not alter CREB conformation, stability, or interactions with other proteins (e.g., CBP, TORCs, or kinases). The possibility that the increased pS133 levels are due to enhanced kinase accessibility or reduced CBP competition rather than reduced PP2A activity is not excluded.
- **Why it matters** The central conclusion that BS2 mediates PP2A-dependent dephosphorylation relies on the specificity of the E153 mutations. Without controls demonstrating that these mutations do not globally perturb CREB structure or function, the interpretation is not fully supported.
- **Resolution test** Provide evidence that E153D/A mutations do not affect CREB protein stability, nuclear localization, or interaction with known binding partners (e.g., CBP KIX domain in the absence of phosphorylation). Additionally, show that the increased pS133 is reversed by PP2A overexpression or that PP2A-B56 recruitment is directly impaired in cells (e.g., by co-immunoprecipitation).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "BS2 is the dominant B56-binding motif" based on pull-down assays and that BS1 is a "low-affinity binding enhanced by phosphorylation."
- **Evidence pointer** Figure 2B–E, Figure S2
- **Concern** The pull-down assays use GST-fusion proteins and purified B56γ1, but the quantitative comparison between BS1 and BS2 binding is not rigorously established. The titration pull-down assay (Figure S2D–E) estimates affinity between 7.5 and 15 μM, but this is a single experiment without error bars or replicates. Additionally, the phosphomimetic S108E effect on BS1 binding is shown only qualitatively, and the physiological relevance of this phospho-site is not established in cells.
- **Why it matters** The distinction between constitutive (BS2) and signal-dependent (BS1) binding is a key conceptual advance. If the affinity measurements are not robust, the claim that BS1 is a weaker, regulated site is not well supported.
- **Resolution test** Provide replicate titration experiments with standard errors, and test whether S108 phosphorylation occurs endogenously in response to cAMP or other stimuli. Additionally, perform competition assays to directly compare BS1 and BS2 affinities.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors conclude that "BS2 mutations potentiate CREB transcriptional activation" and that this is due to increased S133 phosphorylation.
- **Evidence pointer** Figure 5D–E, Figure 7A
- **Concern** The transcriptional assays use Gal4-CREB fusions lacking the bZip and CRTC-binding domains, which may not fully recapitulate endogenous CREB regulation. The in vivo gene expression data show modest effects (approximately 1.5- to 2-fold) with significant variability, and the ChIP data (Figure 7B) are presented without clear statistical comparisons across time points. The link between increased pS133 and transcriptional output is correlative, not causal.
- **Why it matters** The claim that BS2-mediated dephosphorylation attenuates CREB transcriptional bursts is a central conclusion. If the transcriptional assays are not physiologically representative or the statistical power is insufficient, the conclusion is weakened.
- **Resolution test** Use full-length CREB constructs in transcriptional assays, and include a phospho-null S133A control to demonstrate that the transcriptional effects of E153D are dependent on S133 phosphorylation. For the in vivo data, provide time-course analyses with appropriate multiple testing corrections and effect sizes.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "BS2 mediates dephosphorylation of the CK cassette" based on increased pS121 levels in E153D mutants.
- **Evidence pointer** Figure 4A–B
- **Concern** The CK cassette contains multiple phosphorylation sites (S108, S111, S114, S117, S121), and the manuscript only monitors pS121 as a proxy. It is unclear whether the increased pS121 reflects a general increase in CK cassette phosphorylation or a specific effect on S121. Additionally, the functional consequence of increased CK cassette phosphorylation is not directly assessed (e.g., DNA binding or transcriptional activity).
- **Why it matters** The CK cassette is known to inhibit CREB DNA binding when hyperphosphorylated. If BS2 regulates CK cassette dephosphorylation, this could be an important feedback mechanism. However, the current data are too limited to support a strong claim.
- **Resolution test** Monitor multiple CK cassette phospho-sites (e.g., using phospho-specific antibodies or mass spectrometry) and assess the functional impact of increased CK phosphorylation on CREB DNA binding or transcriptional activity in the E153D background.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, "Results" section
- **Issue** The abstract states that "BS2 mutations elevated both basal and stimulus-induced phosphorylation of S133" but does not mention the modest effect sizes or the redundancy with other phosphatases noted in the Discussion.
- **Required correction** Add a qualifier such as "moderately" or "in a manner consistent with partial redundancy" to avoid overstating the effect.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Experimental procedures, "GST-mediated pull-down assay"
- **Evidence pointer** Experimental procedures, "GST-mediated pull-down assay"
- **Issue** The pull-down assay description does not specify the buffer conditions, salt concentrations, or incubation times, which are critical for assessing binding affinity.
- **Required correction** Provide detailed buffer compositions and incubation conditions to enable replication.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Figure 7A
- **Evidence pointer** Figure 7A
- **Issue** The gene expression data are presented as bar graphs with error bars, but the number of biological replicates and the statistical test used are not stated in the figure legend.
- **Required correction** Specify the number of independent experiments and the statistical test used in the legend.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion
- **Evidence pointer** Discussion, paragraph 2
- **Issue** The Discussion mentions that "S156 phosphorylation influences PP2A-B56 recruitment" as a possibility, but this is not tested experimentally.
- **Required correction** Either provide preliminary data on S156 phosphorylation or clearly label this as a speculative hypothesis.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 2G
- **Evidence pointer** Figure 2G
- **Issue** The enzyme kinetics data show a single Michaelis-Menten curve, but the number of replicates and the error bars are not described.
- **Required correction** Provide the number of independent experiments and include error bars or confidence intervals.

## Risk / unsupported claims
- The claim that BS1 is a "signal-dependent" B56 recruitment motif is not supported by cellular data; only in vitro phosphomimetic effects are shown.
- The claim that "BS2 mutations potentiate CREB transcriptional activation" is based on Gal4-CREB fusions and may not reflect endogenous CREB function.
- The in vivo mouse data are described as "viable and fertile" but no functional phenotype is presented beyond phosphorylation and gene expression changes, limiting the physiological relevance.
- The statement that "BS2 mediates dephosphorylation of the CK cassette" is based on a single phospho-site (pS121) and lacks functional validation.
- The enzyme kinetics parameters (Kcat, Km) are presented without error estimates, making the quantitative comparison to other PP2A substrates unreliable.