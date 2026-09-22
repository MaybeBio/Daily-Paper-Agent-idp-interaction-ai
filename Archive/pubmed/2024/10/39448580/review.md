## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) with figure legends, but no actual figure images or supplementary files.
- **Assessment boundary** Scientific content, experimental design, data interpretation, and internal consistency of the provided text. No assessment of figure quality or supplementary data.
- **Shared manuscript claim summary** The authors investigate sequence and structural determinants of RNAPII CTD phase-separation and phosphorylation by CDK7. They report that tyrosine aromaticity and proline cis-trans isomerization govern CTD phase-separation, that CDK7 associates with the surface of CTD droplets and accelerates phosphorylation under phase-separation conditions, and that phosphorylation reverses phase-separation.
- **Visible evidence base** In vitro LLPS assays with fluorescent microscopy and turbidity measurements; kinase assays with γ-[32P]-ATP; sedimentation assays; coarse-grained and all-atom MD simulations; AlphaFold2 predictions.
- **Missing materials affecting confidence** Actual figure images, supplementary figures and tables, source data files, and the reporting summary were not provided. Statistical details for several experiments are incomplete in the text.

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question in the field of transcription regulation: the molecular grammar underlying RNAPII CTD phase-separation and its modulation by CDK7 phosphorylation. The combination of systematic mutagenesis, in vitro phase-separation assays, kinase assays, and multi-scale MD simulations is ambitious and potentially valuable. The central claims regarding the roles of tyrosine aromaticity and proline cis-trans isomerization in CTD phase-separation are partially supported by the presented evidence, though several concerns about experimental rigor and interpretation need to be addressed. The finding that CDK7 associates with the droplet surface and accelerates phosphorylation under phase-separation conditions is interesting, but the mechanistic model requires further validation. The manuscript is generally well-written and accessible, though some methodological details are insufficient for full reproducibility.

- **Who would be interested in the results, and why** Researchers studying transcription regulation, RNA polymerase II biology, liquid-liquid phase-separation, intrinsically disordered proteins, and kinase-substrate interactions. The work also has relevance for understanding the "CTD code" and how post-translational modifications are regulated in the context of transcriptional condensates. The methodological framework combining experimental and computational approaches may interest biophysicists studying phase-separation.

- **Major strengths**
  1. Systematic generation of CTD variants covering all conserved residues provides a comprehensive mutagenesis approach.
  2. Integration of multiple experimental techniques (LLPS assays, kinase assays, sedimentation) with computational approaches (CG and atomistic MD simulations).
  3. The finding that CDK7 localizes to the droplet surface and accelerates phosphorylation under phase-separation conditions is novel and mechanistically interesting.
  4. The use of hydroxyproline as a tool to modulate proline isomerization is creative and informative.
  5. The manuscript addresses an important gap in understanding the biochemical determinants of CTD phase-separation.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental rigor / data interpretation
- **Claim pointer** "The aromaticity of tyrosine and cis-trans isomerization of prolines govern CTD phase-separation."
- **Evidence pointer** Figure 1d, e; Supplementary Figure 2a-d; Results section "Tyrosine and proline residues drive CTD phase-separation"
- **Concern** The claim that tyrosine aromaticity governs phase-separation is based on comparing Y1F and Y1A variants. While Y1A abolishes phase-separation and Y1F shows reduced phase-separation, the authors do not adequately address whether this is specifically due to aromaticity or simply to the loss of a hydrogen-bonding/steric contribution from the tyrosine hydroxyl group. The Y1F variant retains the aromatic ring but loses the hydroxyl group, yet shows reduced phase-separation. This suggests that the hydroxyl group may be important, not just aromaticity. The authors should include additional controls, such as a Y1W variant (tryptophan with different aromatic properties) or a Y1H variant, to more definitively establish the role of aromaticity. Furthermore, the claim that proline cis-trans isomerization governs phase-separation is primarily based on the hydroxyproline variant, which is a bulk substitution that may have pleiotropic effects beyond altering isomerization equilibrium. The authors should provide more direct evidence linking cis versus trans isomer populations to phase-separation propensity.
- **Why it matters** The central mechanistic claim of the paper rests on distinguishing the specific contributions of aromaticity and proline isomerization. Without appropriate controls, the conclusions are not uniquely determined by the data.
- **Resolution test** Additional variants (e.g., Y1W, Y1H, Y1F with hydroxyl-mimicking substitutions) should be tested in LLPS assays. For proline isomerization, the authors could use proline analogs with locked cis or trans conformations, or perform NMR-based population analysis to directly correlate isomer populations with phase-separation behavior.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative analysis / statistical rigor
- **Claim pointer** "Under phase-separation conditions, CDK7 associates with the surface of the CTD droplets, drastically accelerating phosphorylation and promoting the release of hyperphosphorylated CTD from the droplets."
- **Evidence pointer** Figure 3b, c, e, h, i; Results section "The CDK7 complex associates with the surface of CTD droplets and reverses phase-separation by CTD phosphorylation"
- **Concern** The claim of "drastic acceleration" of phosphorylation under phase-separation conditions is based on comparisons that are not fully described. The kinase assay data in Figure 3h show increased phosphorylation in the presence of dextran, but the authors do not provide a quantitative measure of the acceleration (e.g., fold-change in initial rates, time-to-completion). Furthermore, the sedimentation kinase assay (Figure 3i) reports a 21-fold increase in total reaction phosphorylation, but the statistical analysis and the number of replicates are not clearly stated. The authors should provide a more rigorous kinetic analysis, including time courses at multiple substrate and enzyme concentrations, to support the claim of acceleration. Additionally, the claim that CDK7 "associates with the surface" is based on colocalization microscopy, which shows surface localization but does not demonstrate a specific or functional association. The authors should provide quantitative colocalization analysis and ideally a binding assay to support this claim.
- **Why it matters** The kinetic acceleration and surface association are key novel findings that distinguish this work from previous studies. Without rigorous quantitative support, these claims are not fully established.
- **Resolution test** Provide full kinetic time courses with calculated initial rates and statistical comparisons. Include quantitative colocalization analysis (e.g., Pearson's coefficient) and a binding assay (e.g., pull-down or surface plasmon resonance) to demonstrate specific CDK7-CTD droplet interaction.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Computational methodology / model validation
- **Claim pointer** "The cis conformation of prolines and β-turns in the SPXX motif contribute to a more compact CTD ensemble, enhancing interactions among CTD residues."
- **Evidence pointer** Figure 2c-g; Supplementary Figures 5-9; Results section "Impact of CTD heptad residues on LLPS: insights from MD simulations"
- **Concern** The MD simulations are used to support mechanistic conclusions about the role of proline cis-trans isomerization and β-turn structure in phase-separation. However, the authors do not provide sufficient validation of their computational models. Specifically: (1) The CG model uses a modified interaction parameter (ε scaled by 1.1) that is not standard in Martini3; the authors should justify this choice and show that results are robust to this parameter. (2) The atomistic simulations are limited to di-heptad constructs, which may not capture the behavior of the full 52-repeat CTD. (3) The authors do not compare their simulation results to experimental data (e.g., radius of gyration from SAXS, or FRET measurements) to validate the models. (4) The claim that β-turns "enhance interactions among CTD residues" is inferred from distance distributions, but the authors do not directly demonstrate that β-turn formation promotes inter-molecular interactions relevant for phase-separation.
- **Why it matters** The computational results are used to provide mechanistic explanations for experimental observations. If the models are not validated, the mechanistic conclusions are speculative.
- **Resolution test** Provide additional validation of the CG model (e.g., comparison to experimental single-molecule FRET or SAXS data). Extend atomistic simulations to longer constructs or use enhanced sampling to capture larger conformational ensembles. Directly test the role of β-turns by comparing variants with disrupted versus stabilized β-turn propensity in both simulations and experiments.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Biological relevance / physiological context
- **Claim pointer** "Our results highlight the importance of conformationally restricted local structures within spacer regions, separating uniformly spaced tyrosine stickers of the CTD heptads, which are required for CTD phase-separation."
- **Evidence pointer** Discussion section; Figure 4
- **Concern** The study uses recombinant CTD constructs with GFP tags and in vitro conditions (dextran as crowding agent) that may not fully recapitulate the physiological environment. The authors do not address whether the phase-separation behavior observed in vitro occurs at physiologically relevant concentrations and conditions in cells. The claim that the identified determinants are "required for CTD phase-separation" in vivo is not directly tested. The authors should either temper their conclusions to the in vitro system or provide additional evidence (e.g., cellular experiments with CTD variants) to support the physiological relevance of their findings.
- **Why it matters** The broader significance of the work depends on whether the identified molecular determinants are relevant in the cellular context. Overinterpretation of in vitro results could mislead the field.
- **Resolution test** Perform cellular experiments (e.g., expression of CTD variants in cells, assessment of condensate formation) or at minimum clearly state the limitations of the in vitro system and avoid overgeneralization.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity / reproducibility
- **Affected element** Methods section, "FM—image analysis"
- **Evidence pointer** Methods section
- **Issue** The image analysis pipeline is described but lacks specific parameters (e.g., threshold values, minimum object size, background subtraction method). The statement "Otsu's method was used for image thresholding" is insufficient for reproducibility.
- **Required correction** Provide detailed parameters for image analysis, including specific threshold values, object size filters, and any preprocessing steps. Consider depositing the analysis pipeline as a code repository.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 1d, e, h, i
- **Evidence pointer** Figure legends
- **Issue** The quantification of droplet size and number is presented as box plots or scatter plots, but the number of independent experiments and the total number of droplets analyzed per condition are not clearly stated in the figure legends.
- **Required correction** Add the number of independent experiments (n) and the total number of droplets analyzed to each figure legend. Also specify whether the data points represent individual droplets or per-experiment means.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation / overstatement
- **Affected element** Discussion section
- **Evidence pointer** Discussion
- **Issue** The statement "This mechanism could also serve to exclude the already phosphorylated CTD stretches from the interface" is speculative and not directly supported by the data presented.
- **Required correction** Either provide additional experimental evidence to support this claim or rephrase it as a hypothesis for future investigation.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Methods section, "In vitro kinase assays"
- **Evidence pointer** Methods section
- **Issue** The kinase assay conditions are described, but the specific activity of the CDK7 complex is not reported, and the stoichiometry of the complex (CDK7/MAT1/Cyclin H) is not confirmed.
- **Required correction** Report the specific activity of the CDK7 complex and confirm the stoichiometry of the purified complex (e.g., by SDS-PAGE or mass spectrometry).

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction and Discussion
- **Evidence pointer** Introduction, Discussion
- **Issue** The authors do not discuss recent work on CTD phase-separation in the context of other RNAPII modifications (e.g., O-GlcNAcylation, arginine methylation) that may also influence phase behavior. This limits the contextualization of the findings.
- **Required correction** Add a brief discussion of how the identified determinants may interact with other known CTD modifications in regulating phase-separation.

## Risk / unsupported claims
1. The claim that "aromaticity of tyrosine" specifically governs phase-separation is not uniquely supported, as the Y1F variant (which retains aromaticity but loses the hydroxyl group) shows reduced phase-separation. The role of the hydroxyl group is not adequately addressed.
2. The claim that proline cis-trans isomerization "governs" phase-separation is inferred from the hydroxyproline variant, which may have effects beyond altering isomerization equilibrium. Direct evidence linking cis/trans populations to phase-separation is lacking.
3. The claim of "drastic acceleration" of phosphorylation under phase-separation conditions is not quantitatively supported with full kinetic analysis.
4. The claim that CDK7 "associates with the surface" of droplets is based on microscopy colocalization without quantitative analysis or binding assays.
5. The physiological relevance of the in vitro phase-separation findings is not established; the authors do not demonstrate that the identified determinants are required for CTD phase-separation in cells.
6. The MD simulation results are used to support mechanistic conclusions without adequate model validation against experimental data.
7. The statement that "conformationally restricted local structures within spacer regions... are required for CTD phase-separation" is an overgeneralization from the in vitro and in silico data presented.