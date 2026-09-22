## Review setup
- **Input scope** Full manuscript text including abstract, introduction, model description, results, discussion, and references cited within the text.
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims by the presented evidence. Editorial and stylistic issues are noted only where they affect scientific clarity.
- **Shared manuscript claim summary** The manuscript claims that coarse-grained Brownian dynamics simulations show that DNA-bridging proteins and globular crowders cooperate additively in compacting a model bacterial nucleoid, that the number of DNA bridges formed by nucleoid proteins depends critically on their ability to self-associate, and that non-associating proteins produce a liquid-like DNA/protein complex while self-associating proteins produce a gel-like network.
- **Visible evidence base** Simulation results presented in Figures 1, 3, 4, 6, 7, 8, 9, 10, and 11, with associated text in the Results and Discussion sections. Model parameters and simulation protocols described in the Model and simulations section. No experimental data are presented.
- **Missing materials affecting confidence** Supplementary material referenced (Eqs. S1–S22, Figure S8 of Joyeux 2021) is not provided. The manuscript states that the model is described in detail in the Supporting Material of a prior publication, but that material is not included here. This limits full verification of the model implementation and parameter choices. Additionally, no raw simulation trajectories or convergence analyses are provided.

## Reviewer

### Overall assessment
This manuscript presents a computational study of the combined effects of DNA-bridging proteins and globular crowders on the compaction of a model bacterial nucleoid. The work extends the author's prior simulation studies by systematically varying both protein number and crowder volume fraction, and by comparing non-associating versus self-associating protein models. The central finding, that the radius of gyration decreases linearly with both crowder volume fraction and number of DNA bridges, is clearly presented and supported by the simulation data shown. The distinction between liquid-like and gel-like DNA/protein complexes based on protein self-association is a useful conceptual contribution. However, the manuscript has several weaknesses that need to be addressed. The claim of "cooperation" between crowders and bridging proteins is essentially a statement of additivity, which is not deeply analyzed mechanistically. The comparison to experimental systems, while reasonable, is largely qualitative. The manuscript would benefit from a more critical discussion of the limitations of the coarse-grained model, particularly regarding the timescales accessible to simulation and the potential artifacts of the confinement scheme. The writing is generally clear, but some sections are dense and would benefit from more explicit signposting of the logical flow.

### Who would be interested in the results, and why
Researchers in bacterial cell biology, biophysics of chromatin organization, and computational biophysics would find this work relevant. The question of how DNA-bridging proteins and macromolecular crowding jointly organize the nucleoid is of active interest, and the simulation results provide testable predictions about the relative contributions of these two mechanisms. The distinction between liquid-like and gel-like behavior depending on protein self-association could inform interpretations of in vivo imaging experiments. The work may also be of interest to the broader community studying phase separation in biological systems, as it addresses the interplay between associative and segregative phase separation mechanisms.

### Major strengths
1. The systematic parameter sweep across crowder volume fractions and protein numbers is a strength. The data in Figures 4 and 6 cover a wide range of conditions, and the collapse onto a linear relationship in Figure 7 is compelling.
2. The comparison between non-associating and self-associating protein models is well motivated and clearly presented. The different compaction behaviors are rationalized through measurable quantities (number of bridges, mobility, asphericity).
3. The discussion of the biological relevance, including the comparison of model parameters to known properties of H-NS and E. coli, is thoughtful and appropriately cautious.
4. The manuscript is honest about its limitations, particularly regarding the neglect of supercoiling and the potential size-scaling issues.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that the coarse-grained model "reproduces satisfactorily the corresponding relevant features of bacterial cells," specifically citing DNA concentration, protein binding energy, and protein numbers.
- **Evidence pointer** Discussion section, first paragraph; Model and simulations section.
- **Concern** The validation of the model against experimental parameters is incomplete and partly inconsistent. The manuscript states that the DNA concentration in the model is approximately 5 mM versus approximately 6 mM in E. coli, which is reasonable. However, the protein binding energy of 7.8 kBT per binding site is compared to an experimental value of 10.0 kBT for H-NS, but the manuscript does not discuss whether this difference is significant for the conclusions. More critically, the manuscript states that P=50 protein chains in the model correspond to the approximately 8000 H-NS and 10000 StpA monomers in E. coli, based on a "approximately 200 reduction factor." This scaling argument is not developed. The model uses a DNA chain of 2880 beads representing 21600 bp, whereas E. coli has approximately 4.6 Mbp. The reduction factor is therefore approximately 213, which is consistent, but the manuscript does not explain how the protein number scales with this factor, nor whether the crowder concentrations are scaled consistently. Without a clear statement of the scaling rules for all components, the claim that the model reproduces in vivo conditions is not fully supported.
- **Why it matters** The biological relevance of the simulation results depends on the model being in a realistic parameter regime. If the scaling is not consistent across all components, the observed additivity of crowder and protein effects could be an artifact of the specific parameter choices rather than a general property of the system.
- **Resolution test** The author should provide a clear table or paragraph stating the scaling rules used to map model parameters to E. coli values, including DNA length, protein number, crowder concentration, and confinement volume. The sensitivity of the main conclusions to these scaling choices should be discussed, and ideally tested with at least one alternative parameter set.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The manuscript claims that "DNA-bridging proteins and globular crowders cooperate in compacting the DNA coil in the whole range of biologically relevant concentrations," and that this cooperation is reflected in a linear decrease of Rg with both rho and NB.
- **Evidence pointer** Results section, "DNA compaction laws look different" and "〈Rg〉 decreases linearly" subsections; Figures 4, 6, 7.
- **Concern** The central claim of "cooperation" is essentially a statement of additivity: the effects of crowders and proteins on Rg are independent and sum linearly. This is a useful empirical finding, but the manuscript does not provide a mechanistic explanation for why this additivity holds. The author notes that the two mechanisms are associative and segregative phase separation, respectively, but does not explain why these two mechanisms should combine linearly rather than synergistically or antagonistically. The discussion of the liquid-like versus gel-like behavior is suggestive but does not directly address the additivity question. The manuscript would be substantially strengthened by a mechanistic model or at least a dimensional analysis that explains the observed linearity.
- **Why it matters** The claim of cooperation is the main conceptual contribution of the paper. Without a mechanistic explanation, the finding remains at the level of a simulation observation. The broader significance for understanding nucleoid organization in vivo depends on whether the additivity is a general principle or a consequence of the specific model.
- **Resolution test** The author should provide a mechanistic argument, or at least a scaling analysis, that explains why Rg decreases linearly with both rho and NB. This could be in the form of a simple analytical model or a discussion of the relevant length scales and energies. Alternatively, the author could perform additional simulations with modified interaction potentials to test whether the additivity is robust.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The manuscript states that "simulations indicate that non-associating proteins preserve a high mobility inside the nucleoid while contributing to its compaction, leading to a DNA/protein complex which looks like a liquid droplet. In contrast, self-associating proteins form a little deformable network which cross-links the DNA chain, with the consequence that the DNA/protein complex looks more like a gel."
- **Evidence pointer** Results section, "Ability of DNA bridges to compact the DNA coil" subsection; Figures 3 and 11.
- **Concern** The characterization of the DNA/protein complex as "liquid-like" or "gel-like" is based on qualitative observations of mobility and shape. The manuscript reports the mean squared displacement of protein beads and the asphericity coefficient, but does not provide a quantitative criterion for distinguishing liquid-like from gel-like behavior. For example, the manuscript does not report whether the protein clusters in the self-associating case exhibit solid-like behavior (e.g., caged dynamics, non-Gaussian displacement distributions) or whether the non-associating case exhibits diffusive behavior on all accessible timescales. The distinction between liquid and gel is potentially important for the biological interpretation, and the current evidence is suggestive but not conclusive.
- **Why it matters** The liquid/gel distinction is used to explain the different compaction efficiencies of the two protein models. If the distinction is not robust, the explanation is weakened. Moreover, the biological implications of a liquid-like versus gel-like nucleoid are different, and the manuscript should be careful not to overstate the evidence.
- **Resolution test** The author should provide additional quantitative characterization of the dynamics, such as the van Hove correlation function, the non-Gaussian parameter, or the mean squared displacement at different time scales, to support the liquid/gel classification. Alternatively, the author could use a more direct measure of mechanical response, such as the shear modulus, if accessible from the simulations.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction, first paragraph
- **Evidence pointer** Introduction, paragraph 1
- **Issue** The introduction states that the nucleoid "would occupy a volume hundreds of times larger than the cell in the absence of constraints." This is a striking claim, but the calculation is not shown. A reader unfamiliar with polymer physics may not appreciate how this estimate is obtained.
- **Required correction** Provide a brief explanation of the estimate, e.g., the formula for the radius of gyration of a random coil and the relevant values of contour length and persistence length.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Model and simulations, Eq. 7
- **Evidence pointer** Model and simulations section, Eq. 7
- **Issue** The definition of the effective volume fraction rho is given in Eq. 7, but the text does not explicitly state the physical meaning of the parameter Delta b. It is mentioned that Delta b = 0.865 nm for the repulsive potential, but the reader is left to infer that this is a correction to the hard-core radius.
- **Required Correction** Add a sentence explaining that Delta b accounts for the soft repulsive tail of the interaction potential, effectively increasing the excluded volume of the crowders.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results section, "Evolution of 〈NB〉 with ρ and P" subsection
- **Evidence pointer** Results section, paragraph on "Evolution of 〈NB〉 with ρ and P"
- **Issue** The threshold for defining a "bridge" (|k-K|>10) is stated to be arbitrary, and the author notes that the results do not depend sensitively on it. However, no sensitivity analysis is shown. A reader may wonder how the results would change with a different threshold.
- **Required Correction** Either provide a brief sensitivity analysis in the text or supplementary material, or state more explicitly that the threshold was varied and the results were unchanged, with a representative example.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Discussion, final paragraph
- **Evidence pointer** Discussion, final paragraph
- **Issue** The discussion of Liquid-Liquid Phase Separation (LLPS) is brief and somewhat tangential. The connection between the simulation results and LLPS is not made explicit. The paragraph reads as an afterthought.
- **Required Correction** Either expand the discussion to make a clear connection between the simulation findings and the LLPS literature, or remove the paragraph to keep the discussion focused.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Model and simulations, simulation protocol
- **Evidence pointer** Model and simulations section, "Simulations" paragraph
- **Issue** The manuscript states that "four simulations with different initial conditions and different sets of random numbers were run for each pair of values." This is a small number of replicates, and the manuscript does not report the statistical uncertainty of the reported quantities (e.g., Rg, NB). The error bars in the figures are not described.
- **Required Correction** Report the standard error or standard deviation of the measured quantities, and state whether the reported trends are statistically significant given the number of replicates.

### Technical failings that need to be addressed before the case is established
1. The scaling rules for mapping model parameters to E. coli values are not fully specified (R1-M1). This is a blocking issue because the biological relevance of the conclusions depends on the model being in a realistic parameter regime.
2. The statistical uncertainty of the simulation results is not reported (R1-m5). This is a technical failing that affects the reliability of the reported trends.

### Assessment against Nature-style criteria
- **Originality** The work is a systematic extension of the author's prior simulation studies. The specific finding of additivity between crowder and bridging protein effects is new, but the conceptual framework is not radically novel. The liquid/gel distinction is a useful framing. Overall, the originality is moderate.
- **Scientific importance** The question of how the bacterial nucleoid is organized is of broad interest. The simulation results provide a clear and testable prediction about the additivity of two major compaction mechanisms. However, the lack of a mechanistic explanation for the additivity limits the depth of the contribution. The importance is moderate to high.
- **Interdisciplinary readership** The work sits at the interface of biophysics, computational biology, and bacterial cell biology. The methods are standard in the simulation community, and the results are presented in a way that should be accessible to experimentalists. The interdisciplinary appeal is moderate.
- **Technical soundness** The model is well described and the simulation protocol is standard. However, the incomplete specification of the scaling rules and the lack of statistical reporting are weaknesses. The technical soundness is adequate but not exemplary.
- **Readability for nonspecialists** The manuscript is generally well written, but some sections are dense. The introduction and discussion are accessible, but the results section assumes familiarity with polymer physics concepts. The readability is adequate.

### Recommendation posture
Supportive if technical concerns are resolved. The central finding is clearly presented and likely to be of interest to the community. However, the blocking concern regarding the scaling rules (R1-M1) must be addressed before the biological relevance of the conclusions can be fully assessed. The statistical reporting should also be improved. If these issues are resolved, the manuscript would be a solid contribution to the field.

## Risk / unsupported claims
- The claim that the model "reproduces satisfactorily the corresponding relevant features of bacterial cells" is not fully supported because the scaling rules are not completely specified (R1-M1).
- The claim that non-associating proteins form a "liquid droplet" and self-associating proteins form a "gel" is supported by qualitative evidence but lacks quantitative criteria for the classification.
- The claim that the results "transpose probably safely to real life" is an extrapolation that is not directly testable from the simulation data alone. The author does acknowledge limitations, but the statement is still stronger than the evidence warrants.
- The empirical fitting functions in Eqs. 10 and 12 are presented without a discussion of their physical basis. The fits are described as "good quality," but no goodness-of-fit statistics are provided.