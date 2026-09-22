## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodology, data interpretation, and claims as presented in the provided manuscript
- **Shared manuscript claim summary** The authors use all-atom molecular dynamics simulations of 21-residue peptide segments from the androgen receptor N-terminal domain (AR-NTD) to investigate how covalent ligands (SARICAs) alter local conformational preferences. They report that effective condensate-neutralizing ligands containing a cyanopyrazole B-ring reduce helical propensity in the C406-centered peptide, with key contacts involving W399, whereas ineffective ligands with a cyanophenyl ring do not. They propose that disruption of transient helical structures may underlie LLPS neutralization.
- **Visible evidence base** Main text, Figures 1–4, Table 1, Supplementary Figures S1–S4 (referenced but not provided in full)
- **Missing materials affecting confidence** Supplementary figures and tables (S1–S4), force field parameter files, simulation input files, raw trajectory data, convergence metrics, and experimental details from the cited prior work (Thiyagarajan et al.) are not available for verification.

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question: whether small-molecule covalent ligands can specifically modulate the conformational ensemble of an intrinsically disordered region, and whether such modulation correlates with functional outcomes (LLPS neutralization). The computational approach is reasonable for the stated scope, and the comparison between effective and ineffective ligands is a useful design. However, the evidence presented is largely qualitative, based on short (50–100 ns) simulations of short peptides, and the link between local helical destabilization and LLPS neutralization remains speculative. Several technical aspects require clarification or additional analysis before the central claims can be considered established.
- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins, phase separation, nuclear receptor biology, and drug discovery targeting IDRs. The work provides a concrete example of ligand-induced conformational changes in an IDR and may inform future design of covalent modifiers targeting AR-NTD, which is relevant for castration-resistant prostate cancer.
- **Major strengths** 1) The study addresses a challenging and under-explored problem: drugging IDRs. 2) The use of covalent ligands with known functional differences (effective vs. ineffective LLPS neutralizers) provides a clear comparative framework. 3) The analysis combines secondary structure, contact maps, and dimensionality reduction, offering multiple perspectives on conformational changes. 4) The authors are appropriately cautious about the limitations of short simulations and peptide-level models.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** "We find that effective neutralizers make specific interactions (such as those between cyanopyrazole and tryptophan) that alter the helical propensity of the peptide segments."
  - **Evidence pointer** Figure 2, Figure 4, Section 3
  - **Concern** The claim that cyanopyrazole specifically reduces helical propensity is based on visual inspection of stacked bar graphs and contact maps from single 50 ns simulations per condition. No quantitative metrics (e.g., average helicity per residue with error bars, statistical significance testing, or replicate simulations) are provided. The difference between XNN/XN0 and XNB/XEN could arise from sampling variability rather than genuine ligand-specific effects.
  - **Why it matters** The central conclusion of the paper rests on this comparison. Without quantitative support and replicate sampling, the claim is not robustly established.
  - **Resolution test** Provide replicate simulations (at least 3 independent runs per condition) and report mean helicity with standard errors, along with a statistical test (e.g., bootstrap or t-test) comparing effective vs. ineffective ligands. Alternatively, show that the observed differences are reproducible across different starting conformations and force fields.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Scientific importance / claim support
  - **Claim pointer** "These findings on the mechanism of action can be useful for designing molecules that influence IDR structure and condensate of the AR in the future." and "SARICAs might disrupt helical structures, which could potentially interrupt the driver of the condensate."
  - **Evidence pointer** Section 3, Section 4
  - **Concern** The manuscript proposes a mechanistic link between local helical destabilization in a 21-residue peptide and the neutralization of LLPS in the full-length AR-NTD. However, no simulations or experiments directly test this link. The peptide model excludes long-range interactions, multivalency, and the full sequence context that are known to be critical for phase separation. The connection is presented as plausible but is not supported by direct evidence.
  - **Why it matters** The broader significance of the work depends on this mechanistic hypothesis. Without testing it, the study remains a descriptive analysis of peptide-level conformational changes, and the relevance to LLPS neutralization is unsubstantiated.
  - **Resolution test** Either (a) perform simulations of larger AR-NTD constructs or multi-chain systems to test whether ligand binding alters phase separation propensity, or (b) clearly reframe the claims as a hypothesis-generating observation and remove or soften the mechanistic statements in the abstract and conclusions.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness
  - **Claim pointer** "We initially performed 55 ns MD simulations for each peptide system... We performed simulations for an additional 50 ns for some of the systems to check the convergence."
  - **Evidence pointer** Section 2.2, Table 1, Figure 2h,i
  - **Concern** The convergence assessment is limited to a visual comparison of first vs. second 50 ns blocks for two systems (native and XNN on 406C). No quantitative convergence metrics (e.g., RMSD of contact maps, block averaging, or autocorrelation times) are provided. For other systems, only 50 ns of data are used, which may be insufficient for IDR conformational sampling.
  - **Why it matters** IDRs are known to sample diverse conformations slowly. Without demonstrated convergence, the reported conformational preferences may be artifacts of insufficient sampling.
  - **Resolution test** Provide quantitative convergence analysis (e.g., time-dependent helicity, contact map overlap between blocks) for all systems. If convergence is not achieved, acknowledge this limitation explicitly and temper the conclusions accordingly.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methods, force field parameterization
  - **Evidence pointer** Section 2.2
  - **Issue** The procedure for generating force field parameters for the covalent ligands is described, but no validation is shown (e.g., comparison to quantum mechanical reference data, or tests of parameter stability). The chiral center assumption is stated but not justified.
  - **Required correction** Provide validation data for the ligand parameters, or at minimum cite established protocols and note any limitations. Justify the chirality choice with a brief rationale.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Figure 2
  - **Evidence pointer** Figure 2
  - **Issue** The stacked bar graphs in Figure 2 are described in the text but the figure itself is not shown in the provided material. The description of "panels (a–k)" is difficult to follow without the figure.
  - **Required correction** Ensure the figure is included in the final submission and that the caption clearly labels each panel and the corresponding system and starting conformation.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Interpretation
  - **Affected element** Section 3, Figure 4
  - **Evidence pointer** Figure 4
  - **Issue** The claim that W399 initiates the contact with the cyanopyrazole ring is based on contact frequency, but no energetic or structural analysis (e.g., hydrogen bonding, pi-stacking) is provided to support a specific interaction mechanism.
  - **Required correction** Add a brief analysis of the nature of the W399-cyanopyrazole interaction (e.g., distance, geometry, interaction energy) or soften the claim to "frequent contacts" rather than "initiation."
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Table 1
  - **Evidence pointer** Table 1
  - **Issue** The table lists 14 systems, but the text only describes a subset in detail. It is unclear which systems were used for which analyses and whether all were analyzed for all properties.
  - **Required correction** Clarify in the text which systems were used for each analysis, and ensure Table 1 includes all relevant metadata (e.g., simulation length, starting conformation, ligand type).

## Risk / unsupported claims
- The claim that cyanopyrazole-containing ligands specifically reduce helical propensity is not quantitatively supported (no statistics, no replicates).
- The proposed mechanism linking local helical destabilization to LLPS neutralization is speculative and not directly tested.
- The statement that "effective drugs dissolve the condensate" is based on prior experimental work, not on data presented here; the connection to the current simulations is inferential.
- The convergence of simulations is not rigorously demonstrated for most systems.
- The force field parameters for covalent ligands are not validated.
- The relevance of the 21-residue peptide model to the full-length AR-NTD is not established.

## Assessment against Nature-style criteria
- **Originality** Moderate. The application of covalent ligands to modulate IDR conformation is not entirely new, but the specific focus on AR-NTD and the comparison of effective vs. ineffective LLPS neutralizers provides a useful angle. The work does not introduce novel methods or concepts.
- **Scientific importance** Moderate. The question of drugging IDRs is important, and AR is a clinically relevant target. However, the study is limited to short peptides and short simulations, and the functional relevance is not directly demonstrated. The impact is therefore incremental rather than transformative.
- **Interdisciplinary readership** Limited. The work will primarily appeal to computational biophysicists and researchers in nuclear receptor biology. The connection to drug discovery is present but not developed enough to attract a broad medicinal chemistry audience.
- **Technical soundness** The methods are standard and generally appropriate, but the lack of quantitative analysis, replicate simulations, and convergence assessment weakens the technical foundation. The force field parameterization for ligands requires validation.
- **Readability for nonspecialists** The manuscript is reasonably well-written and the "Simple Summary" helps accessibility. However, the results section relies heavily on figure descriptions without the figures being fully visible in the provided material, which hampers evaluation. Technical jargon is used but generally explained.

## Recommendation posture
Currently not established from the provided evidence. The manuscript presents an interesting hypothesis and a reasonable computational approach, but the central claims are not quantitatively supported, and the link to LLPS neutralization is speculative. The authors should be encouraged to revise with additional analyses (replicates, statistics, convergence metrics) and to temper the mechanistic claims. If these concerns are addressed, the work could be suitable for publication in a specialized journal, though it is unlikely to meet the broad-impact bar of Nature.