## Review setup
- **Input scope** Full manuscript text, including Significance statement, Results, Discussion, Conclusions, Methods, and Data Availability sections. Figures and supplementary materials referenced but not provided in full.
- **Assessment boundary** Assessment is limited to the claims and evidence as presented in the provided text. Figures, tables, and supplementary information are referenced but were not available for direct inspection. Statistical details, experimental protocols beyond brief summaries, and full datasets were not accessible.
- **Shared manuscript claim summary** The manuscript reports that the intrinsically disordered C-terminal domains (CTDs) of metabotropic glutamate receptors mGluR2 and mGluR3 interact with negatively charged lipid membranes via electrostatic interactions, that this interaction is mediated by N-terminal basic clusters and an aromatic residue (Y853) in the S/T-rich region, and that modulating CTD–membrane interactions alters receptor internalization in living cells. The authors propose that dynamic CTD–membrane interactions constitute a general mechanism for regulating GPCR function.
- **Visible evidence base** NMR spectroscopy (HSQC signal attenuation assays, backbone assignments, chemical shift-based secondary structure predictions), circular dichroism spectroscopy, all-atom molecular dynamics simulations (6 replicas, 1,370 ns each), site-directed mutagenesis, cell-based internalization assays (surface labeling, fluorescence microscopy), GIRK channel patch clamp recordings, and cancer-associated mutation analysis.
- **Missing materials affecting confidence** Figures 1–6 and all supplementary figures (S1–S10) were not provided. Full experimental protocols, statistical analysis details, raw data, and MD simulation parameters beyond brief descriptions were not accessible. The specific NMR intensity ratio values, CD spectra, and microscopy images could not be independently evaluated.

## Reviewer
- **Overall assessment** This manuscript presents a novel and potentially significant finding: that intrinsically disordered C-terminal domains of mGluR2 and mGluR3 interact with cellular membranes through electrostatic mechanisms, and that this interaction regulates receptor internalization. The combination of biophysical (NMR, CD), computational (MD), and cellular (internalization assays, electrophysiology) approaches is commendable and provides multiple lines of evidence. However, the absence of the actual figures and supplementary data prevents full verification of the quantitative claims. The causal link between membrane binding and functional outcomes, while plausible and supported by the mutagenesis data, would benefit from more direct mechanistic evidence. The generalizability claim, while appropriately framed as a proposal, extends beyond the direct evidence presented for two receptors.
- **Who would be interested in the results, and why** Researchers in GPCR biology, particularly those studying receptor signaling, desensitization, and internalization. The work is also relevant to the intrinsically disordered protein community, as it provides a concrete example of functional IDP–membrane interactions in a receptor context. Structural biologists studying GPCR architecture and membrane protein biophysicists investigating protein–lipid interactions would find the NMR and MD approaches of interest. Clinically oriented researchers may be drawn to the cancer-associated mutation analysis, which links fundamental biophysics to disease-relevant variants.
- **Major strengths** The study combines multiple orthogonal techniques to establish a biophysical phenomenon (CTD–membrane binding) and then connects it to cellular function. The NMR-based assay provides residue-level resolution of membrane interactions, which is a powerful approach. The inclusion of cancer-associated mutations adds translational relevance. The use of a CAAX box to artificially enhance membrane anchoring provides a clever gain-of-function manipulation. The authors are appropriately cautious in their interpretation and acknowledge limitations.
- **Major Concerns** The most significant concern is the indirect nature of the link between in vitro membrane binding measurements and the observed functional effects in cells. The authors propose that membrane binding sequesters the CTD and reduces accessibility to kinases and arrestins, but direct evidence for this mechanism in cells is lacking. Additionally, the quantitative relationship between the degree of membrane binding (as measured by NMR signal attenuation) and the magnitude of functional effects is not systematically explored. The MD simulations, while useful, are limited to a single construct and may not capture the full conformational landscape. The generalizability claim rests on only two receptors from one GPCR family.
- **Technical failings that need to be addressed before the case is established** The manuscript does not provide statistical details for the internalization assays (number of independent experiments, error bars, significance testing). The NMR intensity ratio data are described qualitatively; quantitative thresholds for "binding" versus "no binding" are not defined. The MD simulation analysis lacks convergence assessment and error estimation. The patch clamp data are mentioned but not shown or described in sufficient detail to evaluate the claim of "clear left-shift."
- **Assessment against Nature-style criteria**  
  *Originality*: High. The concept of GPCR CTD–membrane interactions as a regulatory mechanism is novel and not previously described for this receptor family.  
  *Scientific importance*: Potentially high. If the proposed mechanism is general, it could reshape understanding of GPCR desensitization and internalization. The cancer-associated mutation link adds translational significance.  
  *Interdisciplinary readership*: Moderate to high. The work bridges membrane biophysics, structural biology, and cell signaling, and should appeal to readers across these fields.  
  *Technical soundness*: Generally sound in approach, but the absence of full data presentation and statistical details limits verification. The NMR methodology is well-established, and the MD protocols follow standard practice.  
  *Readability for nonspecialists*: The manuscript is clearly written and the significance is well articulated. The Significance statement effectively frames the work for a broad audience. However, some sections assume familiarity with NMR and MD terminology.
- **Recommendation posture** Supportive if technical concerns are resolved. The core finding is novel and potentially important, but the manuscript requires additional data presentation, statistical rigor, and more direct mechanistic evidence to fully establish the proposed model.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The manuscript claims that CTD–membrane interactions regulate receptor internalization, with mutations that reduce membrane binding enhancing internalization and mutations that enhance membrane binding reducing it.
- **Evidence pointer** Results section "mGluR3 CTD Membrane Interactions Modulate Receptor Internalization in Living Cells"; Figure 6
- **Concern** The functional data linking membrane binding to internalization are presented without statistical details. The number of independent experiments, error bars, and significance testing are not described. The claim of a "consistent ~30% drop in fluorescence" for wild type requires quantitative support. The differences between mutants are described qualitatively ("greater degree," "drastically decreased") without numerical values or statistical comparison. The patch clamp data are mentioned but not shown, making the claim of a "clear left-shift" unverifiable.
- **Why it matters** The central thesis of the manuscript is that membrane binding modulates receptor function. Without rigorous quantitative analysis of the functional assays, the strength of this conclusion cannot be assessed. The reader cannot determine whether the observed differences are robust and reproducible or within experimental noise.
- **Resolution test** Provide full statistical analysis of internalization data, including number of replicates, mean values with error bars, and appropriate significance tests (e.g., ANOVA with post-hoc comparisons). Present the patch clamp data as a figure with dose-response curves and statistical comparison of EC50 values.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic evidence
- **Claim pointer** The manuscript proposes that membrane binding sequesters the CTD, reducing its accessibility to kinases (GRKs) and arrestins, thereby modulating internalization.
- **Evidence pointer** Discussion section; Figure 6G
- **Concern** The proposed mechanism is plausible but not directly tested. The authors do not provide evidence that membrane-bound CTDs are less accessible to GRKs or β-arrestins in cells. The correlation between membrane binding affinity and internalization is suggestive but does not establish causality. Alternative explanations, such as direct effects of the mutations on protein stability, folding, or interactions with other partners, are not excluded.
- **Why it matters** The manuscript claims a mechanistic understanding of how CTD–membrane interactions regulate receptor function. Without direct evidence for the proposed sequestration mechanism, the conclusion remains speculative. The field would benefit from a clear demonstration that membrane binding competes with effector binding.
- **Resolution test** Perform experiments that directly test the accessibility of the CTD to kinases or arrestins in the presence and absence of membrane binding. This could include in vitro kinase assays with membrane-bound versus free CTD, or cellular assays measuring GRK phosphorylation or β-arrestin recruitment in the presence of membrane-binding modulators.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** The authors propose that "dynamic CTD–membrane interaction constitutes a general mechanism for regulating GPCR function."
- **Evidence pointer** Significance statement; Discussion section
- **Concern** The evidence for this general mechanism is based on two receptors (mGluR2 and mGluR3) from the same family. While the authors acknowledge this is a proposal, the claim of generality is not supported by the data presented. The sequence features that drive membrane binding (basic clusters, aromatic residues) may not be conserved across all GPCRs, and the functional consequences may differ.
- **Why it matters** The significance of the work is substantially enhanced if the mechanism is general. Without evidence from additional GPCR families or a bioinformatic analysis showing conservation of the relevant sequence features, the generalizability claim remains speculative.
- **Resolution test** Provide a bioinformatic analysis of GPCR CTD sequences to identify how many receptors contain similar basic clusters and aromatic residues. Alternatively, test membrane binding and functional consequences for one or two additional GPCRs from different families.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative rigor
- **Claim pointer** The manuscript states that "the extent of attenuation for the anchored CTD is dramatically greater in the S/T-rich and C-terminal regions than that observed for the unanchored CTD using vesicles containing 50% negative charge content."
- **Evidence pointer** Results section "Aromatic and Distal Charged Residues Help Anchor the mGluR3 CTD S/T-Rich Region to the Membrane"; Figure 5; Supplementary Figure S6E
- **Concern** The comparison between anchored and unanchored CTD binding is made under different conditions (different lipid compositions, different vesicle preparations). The claim of "dramatically greater" attenuation is qualitative. Without quantitative comparison of binding affinities or a controlled experiment where only the anchoring is varied, the conclusion that anchoring enhances binding is not rigorously established.
- **Why it matters** The anchored CTD experiment is used to argue that the in vitro measurements are relevant to the intact receptor context. If this comparison is not quantitatively rigorous, the relevance of the in vitro data to the cellular context is weakened.
- **Resolution test** Perform a direct comparison of anchored versus unanchored CTD binding under identical lipid conditions, with quantitative analysis of binding affinities or dissociation constants.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section, MD simulation description
- **Evidence pointer** Methods section
- **Issue** The description of the MD simulation setup is brief. The force field parameters, water model, ion concentration, temperature coupling, and pressure coupling are not specified. The statement "equilibrated using the standard CHARMM-GUI-based protocol" is vague.
- **Required correction** Provide a more detailed description of the simulation parameters, including software version, force field, water model, salt concentration, and equilibration protocol. This is essential for reproducibility.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Results section, NMR intensity ratio data
- **Evidence pointer** Figure 2; Supplementary Figures S1, S4, S6, S9
- **Issue** The NMR intensity ratio data are presented as plots, but the numerical values and the criteria for defining "binding" versus "no binding" are not stated. The reader cannot determine the dynamic range of the assay or the significance of the observed attenuation.
- **Required correction** Define a quantitative threshold for binding (e.g., intensity ratio below a certain value) and provide the numerical values for key residues. Consider presenting the data as bar graphs with error bars for key positions.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Results section, cancer-associated mutations
- **Evidence pointer** Results section "CTD–Membrane Binding Is Modulated by Cancer-Associated Mutations"; Figure 5
- **Issue** The manuscript states that the cancer-associated mutations "could influence membrane interactions" and shows data for three mutations. However, the functional significance of these mutations in cancer is not discussed. The connection between altered membrane binding and cancer biology is not developed.
- **Required correction** Add a brief discussion of the potential relevance of altered CTD–membrane interactions to cancer biology, or explicitly state that the functional consequences for cancer are unknown and require further investigation.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results section, phosphorylation hypothesis
- **Evidence pointer** Results section "mGluR3 CTD Membrane Interactions Modulate Receptor Internalization in Living Cells"; Figure 6
- **Issue** The manuscript proposes that phosphorylation of Y853 could modulate membrane binding and internalization, but does not directly test this hypothesis. The Y853D phosphomimetic is used, but the actual phosphorylation state of Y853 in cells is not examined.
- **Required correction** Acknowledge more explicitly that the phosphorylation hypothesis is speculative and not directly tested. Alternatively, include experiments examining Y853 phosphorylation in response to EGF treatment.

## Risk / unsupported claims
- The claim that CTD–membrane interactions constitute a "general mechanism for regulating GPCR function" is not supported by the data, which only address two receptors from one family.
- The claim that membrane binding "regulates the accessibility of the CTD to GRKs and β-arrestins" is proposed but not directly tested.
- The claim that EGF-induced internalization is mediated by Y853 phosphorylation is not directly supported, as phosphorylation of Y853 was not measured.
- The quantitative relationship between membrane binding affinity (as measured by NMR) and the magnitude of functional effects (internalization) is not established.
- The relevance of the in vitro membrane binding measurements to the cellular context is inferred but not directly demonstrated, despite the anchored CTD experiments.