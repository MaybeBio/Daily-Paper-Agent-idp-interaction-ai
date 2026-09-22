## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary figure legends.
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and consistency between results and conclusions. Not assessed: grammar, formatting, or editorial style.
- **Shared manuscript claim summary** The authors propose that acute stresses trigger polysome collapse and RNA condensation into ribonucleoprotein (RNP) granules, which transiently fluidize the cytoplasm. They argue this fluidization is required for efficient formation of quality control bodies (Q-bodies) during stress, and that this mechanism is conserved across yeast and mammalian cells.
- **Visible evidence base** Microrheology measurements using μNS particles and GEMs in yeast and mammalian cells; polysome profiling; cryo-electron tomography; coarse-grained molecular dynamics simulations; fluorescence imaging of P-bodies, stress granules, and Q-bodies; ATP and pH sensors; optogenetic RNA condensation experiments.
- **Missing materials affecting confidence** Figure panels referenced but not fully described in text (e.g., exact statistical tests and n numbers for several comparisons); supplementary videos not viewable; some methodological details for cryo-ET analysis are abbreviated; no raw trajectory data or code availability link verified.

## Reviewer
- **Overall assessment** This manuscript presents a compelling and novel hypothesis: that stress-induced polysome collapse and RNA condensation into RNP granules fluidize the cytoplasm, rather than simply causing passive crowding changes. The combination of experimental microrheology, genetic perturbations, and coarse-grained simulations provides a multi-pronged approach that strengthens the central claim. The data are largely consistent with the model, and the use of orthogonal methods (e.g., cycloheximide, edc3Δ, pab1ΔP, optogenetics) to test causality is commendable. However, several concerns remain regarding the quantitative rigor of the microrheology analysis, the interpretation of the simulation results, and the generalizability of the Q-body findings. These issues, while not fatal, need to be addressed to fully establish the case.
- **Who would be interested in the results, and why** Cell biologists studying stress responses, phase separation, and cytoplasmic organization; biophysicists interested in intracellular transport and crowding; researchers working on RNA metabolism and RNP granules. The findings have broad implications for understanding how cells coordinate biochemical reactions in space and time during stress.
- **Major strengths** 1) The study addresses a fundamental question about how cells modulate their physical properties in response to stress, moving beyond simple descriptions of crowding. 2) The use of multiple experimental systems (yeast, mammalian cells) and techniques (microrheology, cryo-ET, simulations) provides strong cross-validation. 3) The genetic and pharmacological perturbations (cycloheximide, edc3Δ, pab1ΔP) effectively dissect the causal requirements for polysome collapse and RNA condensation. 4) The optogenetic approach elegantly demonstrates that RNA condensation alone is sufficient to fluidize the cytoplasm, independent of stress signaling. 5) The simulations provide a mechanistic framework that connects molecular-level changes to mesoscale rheology.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Quantitative rigor of microrheology
  - **Claim pointer** The authors claim a "transient increase in mesoscale cytoplasmic diffusivity" upon stress, quantified as Deff at specific timescales.
  - **Evidence pointer** Figures 1B–D, 1H–J; Methods section "Passive rheological probes imaging and single particle tracking"
  - **Concern** The manuscript reports Deff values but does not provide sufficient detail on the statistical distribution of particle displacements, the number of cells/particles analyzed per condition, or the criteria for excluding trajectories. The choice of timescale (100 ms for GEMs, 1 s for μNS) is justified by similarity of step-size distributions, but the sensitivity of the conclusions to this choice is not explored. Furthermore, the authors note that μNS particles interact with P-bodies, which could bias their motion; while they argue against sequestration, a quantitative assessment of the fraction of particles near or within P-bodies is missing.
  - **Why it matters** The central claim of the paper rests on the reliability of the microrheology measurements. If the observed changes in Deff are influenced by particle-P-body interactions or by a small subset of trajectories, the interpretation of "cytoplasmic fluidization" could be compromised.
  - **Resolution test** Provide a detailed breakdown of the number of cells, particles, and trajectories per condition; show the full distribution of step sizes or MSD curves, not just Deff; perform a sensitivity analysis using different timescales; quantify the spatial correlation between particle positions and P-bodies/SGs to rule out sequestration artifacts.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** No
  - **Axis** Interpretation of simulation results
  - **Claim pointer** The authors state that "coarse-grained molecular dynamic simulations support this as a minimal mechanism for the observed biophysical changes."
  - **Evidence pointer** Figure 2I–J; Methods section "Coarse-grained molecular dynamic (MD) simulation"
  - **Concern** The simulations model polysomes as chains of six connected rigid spheres and RNA as spherical particles with attractive interactions. While this captures the essential physics, the parameters (e.g., spring constants, interaction strengths) are not systematically varied to test the robustness of the conclusions. The authors report that increasing polysome fraction reduces diffusivity, but it is unclear whether this effect is specific to the chain-like geometry or could be reproduced by simply increasing the total volume fraction of obstacles. A control simulation with an equivalent volume fraction of unconnected spheres would strengthen the claim that polysome architecture matters.
  - **Why it matters** The simulation is used to support the mechanistic interpretation. If the observed effects are merely due to increased crowding, the specific role of polysome collapse and RNA condensation would be less clear.
  - **Resolution test** Perform control simulations with (a) unconnected spheres at the same volume fraction, (b) varying chain lengths, and (c) different interaction strengths. Show that the reduction in diffusivity is specifically dependent on the presence of connected polysomes and condensing RNA.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Generalizability of Q-body findings
  - **Claim pointer** The authors conclude that "increased mesoscale diffusivity correlates with the efficient formation of quality control bodies (Q-bodies)" and that fluidization is required for Q-body assembly.
  - **Evidence pointer** Figures 4A–D; Results section "Increased mesoscale diffusivity facilitates Q-body formation upon acute glucose starvation"
  - **Concern** The correlation between early fluidization and later Q-body formation is based on a relatively small number of cells (n not specified in text). The rescue experiment with hypotonic shock is elegant, but it is unclear whether the effect is specific to Q-bodies or would also apply to other stress-induced assemblies. The authors do not test whether fluidization is required for the initial nucleation of Q-bodies or only for their growth/coalescence. Additionally, the physiological relevance of Q-bodies in this context is not fully established.
  - **Why it matters** The claim that fluidization enables Q-body formation is a key functional consequence of the proposed mechanism. If the effect is not specific or if the assay does not distinguish between nucleation and growth, the conclusion may be overstated.
  - **Resolution test** Quantify the number of cells analyzed and provide statistical power calculations. Test whether fluidization affects the nucleation rate (e.g., by measuring the appearance of small foci) versus growth (e.g., by measuring fusion events). Examine whether other stress-induced assemblies (e.g., P-bodies themselves) are similarly affected.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity of figure presentation
  - **Affected element** Figures 1B–D
  - **Evidence pointer** Figure 1
  - **Issue** The time courses of Deff are shown as line graphs, but the individual data points and error bars are not clearly visible. It is difficult to assess the variability between cells.
  - **Required correction** Provide box plots or scatter plots with individual cell values overlaid, and clearly indicate the number of cells per time point.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Methodological detail
  - **Affected element** Cryo-ET analysis
  - **Evidence pointer** Methods section "Cryo-electron tomography"
  - **Issue** The description of how polysomes were identified and assigned in the cryo-ET data is brief. The criteria for defining a polysome (distance cutoff of 8 nm) are stated, but the sensitivity of the results to this cutoff is not shown.
  - **Required correction** Show the distribution of exit-to-entry distances and demonstrate that the conclusions are robust to the choice of cutoff (e.g., 6–10 nm).
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Statistical reporting
  - **Affected element** Multiple figures
  - **Evidence pointer** Figures 3C–G, 4D
  - **Issue** The statistical tests used for comparisons (e.g., between wild-type and mutant cells) are not consistently reported in the figure legends or text.
  - **Required correction** Specify the statistical test used for each comparison, the n number, and the p-value or confidence interval.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** Abstract and Discussion
  - **Evidence pointer** Abstract, Discussion
  - **Issue** The term "fluidize" is used to describe the increase in diffusivity, but it is not defined quantitatively. It may be confused with a phase transition.
  - **Required correction** Define "fluidize" operationally (e.g., as an increase in Deff by X-fold) and clarify that this does not imply a liquid-solid phase transition.
- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative rigor of microrheology) is the most critical. Without a clear demonstration that the observed changes in Deff are robust and not artifacts of particle-P-body interactions, the central claim is not fully supported. R1-M2 (simulation controls) is also important to establish the specificity of the mechanism.
- **Assessment against Nature-style criteria**  
  *Originality*: High. The idea that polysome collapse and RNA condensation actively fluidize the cytoplasm is novel and counterintuitive, as most studies focus on crowding-induced slowing.  
  *Scientific importance*: High. The findings have broad implications for understanding stress responses, phase separation, and intracellular transport. The proposed mechanism could be relevant to many cellular processes.  
  *Interdisciplinary readership*: Moderate to high. The topic bridges cell biology, biophysics, and RNA biology. The use of simulations and microrheology may appeal to physical scientists, but the presentation is accessible.  
  *Technical soundness*: Moderate. The experimental design is generally sound, but the quantitative analysis of microrheology needs more rigor. The simulations are a useful complement but require additional controls.  
  *Readability for nonspecialists*: Good. The manuscript is well-written and the logic is clear. The use of figures and supplementary materials helps convey complex concepts.
- **Recommendation posture** Supportive if technical concerns are resolved. The core hypothesis is interesting and the data are largely consistent, but the quantitative rigor of the microrheology analysis and the specificity of the simulation results need to be strengthened. If these issues are addressed, the paper would be a strong contribution.

## Risk / unsupported claims
- The claim that "condensation of RNA into SGs or P-bodies is required for cytoplasmic fluidization" is supported by the edc3Δ and pab1ΔP experiments, but the authors do not rule out the possibility that other factors (e.g., changes in ATP or pH) contribute independently. The statement that these condensates are "required" may be too strong.
- The claim that "increased mesoscale diffusivity correlates with the efficient formation of quality control bodies" is based on a correlation and a rescue experiment, but the causal link is not fully established. The authors do not show that fluidization is sufficient for Q-body formation in the absence of stress.
- The statement that "the phenomenon of mesoscale cytoplasmic fluidization driven by polysome collapse and RNA condensation into RNP granules is conserved over more than a billion years of eukaryotic evolution" is an extrapolation from yeast and one mammalian cell line. This claim is not directly tested and should be softened.
- The simulation results are described as supporting a "minimal mechanism," but the authors do not rule out alternative mechanisms (e.g., changes in cytoskeletal organization or ATP-dependent processes). The claim that the simulations "support" the model is appropriate, but the word "minimal" may be misleading without more extensive parameter exploration.