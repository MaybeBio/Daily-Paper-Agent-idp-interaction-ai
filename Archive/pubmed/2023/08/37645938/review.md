## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, conclusions, methods summary, data sharing plan) as provided
- **Assessment boundary** Scientific content, experimental logic, evidence consistency, and claims as presented in the supplied text; no external validation of data or methods beyond what is described
- **Shared manuscript claim summary** The authors propose that the intrinsically disordered C-terminal domains (CTDs) of mGluR2 and mGluR3 bind to lipid membranes in a composition-dependent manner, that this binding is mediated by electrostatic and aromatic interactions, and that modulation of this binding alters GPCR internalization and G protein signaling in living cells, suggesting a general regulatory mechanism for GPCR function
- **Visible evidence base** NMR spectroscopy (HSQC, triple resonance assignments, intensity ratios), circular dichroism, all-atom molecular dynamics simulations, site-directed mutagenesis, live cell internalization assays, GIRK channel electrophysiology, EGFR stimulation experiments
- **Missing materials affecting confidence** Full methods details, supplementary figures (S1–S10), movies (SM1–SM4), BMRB accession data, GitHub repository contents, exact statistical analyses and replicates, raw data for internalization and electrophysiology experiments

## Reviewer
- **Overall assessment** This manuscript presents a compelling and well-integrated study combining biophysical, computational, and cellular approaches to establish a novel regulatory mechanism for GPCR function via CTD-membrane interactions. The work is timely, addresses a genuine gap in the field, and the conclusions are largely supported by the evidence presented. However, several technical concerns regarding the quantitative interpretation of NMR data, the physiological relevance of the in vitro conditions, and the causal link between membrane binding and functional outcomes require clarification before the case is fully established.
- **Who would be interested in the results, and why** Researchers in GPCR biology, membrane protein biophysics, intrinsically disordered protein function, signal transduction, and drug discovery. The proposed mechanism of CTD-membrane interactions as a regulatory node for receptor internalization and G protein coupling has broad implications for understanding GPCR signaling diversity and could inform therapeutic strategies targeting receptor desensitization.
- **Major strengths** The study combines multiple orthogonal techniques to characterize CTD-membrane interactions at residue-level resolution. The identification of specific residues (basic cluster, Y853) and their differential roles in membrane binding and receptor function is elegant. The use of cancer-associated mutations to probe functional relevance adds translational significance. The live cell experiments directly link in vitro biophysical observations to receptor biology.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative NMR interpretation), R1-M2 (causal link between membrane binding and internalization), R1-M3 (physiological relevance of in vitro conditions)
- **Assessment against Nature-style criteria** Originality: High. The concept of GPCR CTDs as membrane-interacting regulatory elements is novel and extends beyond previous studies of isolated CTD disorder. Scientific importance: High. If the mechanism is generalizable, it could reshape understanding of GPCR regulation and desensitization. Interdisciplinary readership: Strong. The work bridges structural biology, biophysics, cell biology, and pharmacology. Technical soundness: Generally strong, but with specific concerns noted below that need resolution. Readability for nonspecialists: The abstract and introduction are accessible, but the results section assumes significant familiarity with NMR and MD methodologies; some streamlining would improve accessibility.
- **Recommendation posture** Supportive if technical concerns are resolved. The core findings are novel and potentially important, but the quantitative claims regarding membrane binding and the causal relationship to receptor function require additional evidence or more careful framing.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that NMR signal attenuation in the presence of vesicles reflects direct membrane binding of specific CTD residues, and that intensity ratios provide a quantitative measure of binding strength across mutants and lipid compositions.
- **Evidence pointer** Results section "Disordered mGluR CTDs bind negatively charged membranes in vitro"; Figures 2A–D, S1, S4, S6
- **Concern** The interpretation of NMR intensity ratios as a direct proxy for membrane binding assumes that signal attenuation is solely due to immobilization upon vesicle binding. However, other factors, including exchange broadening, aggregation, or non-specific interactions with vesicle surfaces, could contribute to signal loss. The authors do not report control experiments such as titration curves, dissociation constants, or competition assays to establish the specificity and affinity of the interaction. Additionally, the use of a single lipid concentration for most comparisons (except Figure S6) limits the ability to distinguish changes in binding affinity from changes in binding stoichiometry or mode.
- **Why it matters** The central claim of the paper, that CTD-membrane interactions are functionally relevant and modulated by specific residues and mutations, rests on the quantitative interpretation of these NMR data. Without a more rigorous biophysical characterization, the conclusions regarding differential binding of mutants and lipid compositions are not fully supported.
- **Resolution test** Provide titration data with increasing vesicle concentrations to derive binding isotherms and, where possible, apparent affinities. Include control experiments with neutral vesicles or vesicles of different compositions to demonstrate specificity. For key mutants, show that observed differences in intensity ratios are not due to changes in protein stability or aggregation (e.g., via SEC or analytical ultracentrifugation).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Causal link
- **Claim pointer** The authors state that mutations that reduce membrane binding (R843A, G848E, Y853A, Y853D, R869Q) enhance internalization, while those that enhance binding (Y853F, E870K, CAAX) reduce internalization, and interpret this as evidence that CTD-membrane interactions regulate receptor function.
- **Evidence pointer** Results section "mGluR3 CTD membrane interactions modulate receptor internalization in living cells"; Figures 6B–F, S10
- **Concern** The correlation between in vitro membrane binding and cellular internalization is suggestive but does not establish causality. The mutations could affect internalization through other mechanisms, such as altering CTD conformation, disrupting interactions with arrestins or GRKs directly, or affecting receptor trafficking independent of membrane binding. The CAAX experiment is a useful control, but the authors do not demonstrate that the CAAX motif specifically increases membrane binding of the CTD in the cellular context. Additionally, the Y853F mutation, which enhances membrane binding, could also affect phosphorylation-dependent interactions with arrestins, confounding the interpretation.
- **Why it matters** The paper proposes a mechanistic model where membrane binding sequesters the CTD and modulates accessibility to downstream effectors. To establish this model, it is necessary to exclude alternative explanations and demonstrate that the functional effects are specifically due to altered membrane interactions.
- **Resolution test** Perform experiments that directly manipulate membrane binding in cells without altering the CTD sequence, e.g., using inducible membrane recruitment systems or altering membrane lipid composition pharmacologically. Alternatively, show that mutations that enhance or reduce membrane binding have corresponding effects on CTD phosphorylation or arrestin recruitment in a manner consistent with the model.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Physiological relevance
- **Claim pointer** The authors suggest that CTD-membrane interactions may be a general regulatory mechanism throughout the GPCR superfamily and that changes in membrane composition could modulate receptor function.
- **Evidence pointer** Discussion section; Results section "CTD-membrane binding is modulated by cancer-associated mutations"
- **Concern** The in vitro experiments use model membranes (DOPS, DOPC, DOPE) that do not recapitulate the complex lipid composition of the plasma membrane inner leaflet, including phosphoinositides, cholesterol, and other anionic lipids. While the authors test a more complex mixture in Figure S6, the physiological relevance of the observed binding preferences is not established. The claim of generality across the GPCR superfamily is speculative, as only two closely related receptors are examined.
- **Why it matters** The broader significance of the work depends on the generality of the mechanism and its relevance to native membranes. Overinterpretation could mislead the field.
- **Resolution test** Test CTD-membrane interactions using native membrane preparations or giant plasma membrane vesicles. Examine additional GPCRs with diverse CTD sequences to assess generality. Acknowledge the limitations of model membranes more explicitly in the discussion.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, last sentence
- **Issue** The phrase "suggesting that CTD-membrane binding may be a general regulatory mode throughout the broad GPCR superfamily" is a strong claim given the limited evidence presented.
- **Required correction** Soften to "raising the possibility that CTD-membrane interactions could represent a general regulatory mechanism, warranting further investigation across the GPCR superfamily."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Methods summary
- **Evidence pointer** Methods section
- **Issue** The methods summary is extremely brief and refers to the SI for details. For a preprint, this is acceptable, but key parameters (e.g., NMR acquisition temperatures, vesicle sizes, protein concentrations, MD force field details) should be stated in the main text or the SI should be made available for review.
- **Required correction** Provide a more detailed methods summary in the main text or ensure the SI is accessible and complete.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figures 5 and 6
- **Evidence pointer** Results sections on cancer mutations and internalization
- **Issue** The figures are referenced but not shown in the provided text. It is difficult to assess the quality of the data and the magnitude of the reported effects.
- **Required correction** Ensure figures are included in the manuscript or provide representative data in the text.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Internalization and electrophysiology data
- **Evidence pointer** Results section "mGluR3 CTD membrane interactions modulate receptor internalization in living cells"
- **Issue** The text reports "consistent ~30% drop" and "clear left-shift" without providing statistical details (n, error bars, significance tests).
- **Required correction** Include statistical analyses and effect sizes for all quantitative comparisons.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion of Y853 phosphorylation
- **Evidence pointer** Discussion section
- **Issue** The authors speculate that Y853 phosphorylation could regulate membrane binding, but the Y853D phosphomimetic is a crude approximation of phosphorylation. The claim would be strengthened by direct evidence of Y853 phosphorylation in cells.
- **Required correction** Acknowledge the limitations of phosphomimetics and consider mass spectrometry-based phosphoproteomics to detect endogenous Y853 phosphorylation.

## Risk / unsupported claims
- The claim that CTD-membrane interactions are a "general regulatory mode throughout the broad GPCR superfamily" is not supported by the data, which only examine two closely related receptors.
- The claim that Y853 phosphorylation drives internalization by reducing membrane binding is speculative; the Y853D phosphomimetic data are suggestive but not conclusive.
- The statement that "changes in membrane composition" could regulate receptor function is plausible but not directly tested in this study.
- The assertion that the in vitro NMR and MD results quantitatively reflect the behavior of the CTD in the context of the full-length membrane-embedded receptor is not fully established, although the anchored CTD experiment (Figure S6E) partially addresses this.
- The functional significance of the cancer-associated mutations (G848E, R869Q, E870K) in terms of tumor biology is not explored beyond the observation that they alter membrane binding and internalization.