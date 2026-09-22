## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and figure legends
- **Assessment boundary** Scientific validity, technical soundness, conceptual novelty, and clarity of claims as presented in the provided manuscript
- **Shared manuscript claim summary** The authors report the construction of liquid-liquid phase separated (LLPS) condensates in mammalian cells using de novo designed coiled-coil (CC) dimer-forming modules. They demonstrate that CC pair stability, number, linkers, and sequential arrangement govern the transition between diffuse, liquid, and immobile condensates, corroborated by coarse-grained molecular simulations. They further show modular control including multiple coexisting condensates, chemical regulation of LLPS, and regulation by a third polypeptide chain.
- **Visible evidence base** Full text of manuscript including all main figures (Figures 1–7), supplementary figure references, methods section, and figure legends
- **Missing materials affecting confidence** Supplementary figures, tables, movies, and data files referenced but not provided; detailed simulation parameters in Supplemental Methods not available for full assessment

## Reviewer
- **Overall assessment** This manuscript presents a systematic and well-executed study on the design of LLPS condensates using de novo coiled-coil modules. The work is conceptually interesting and technically sound in its experimental approach, with a strong combination of cellular imaging, biophysical characterization, and coarse-grained simulation. The modular design strategy and the demonstration of programmable features (chemical regulation, multi-condensate coexistence, single-chain systems) represent a meaningful advance in synthetic biology. However, several concerns regarding the quantitative rigor of the biophysical characterization, the direct comparability of simulation and experiment, and the generalizability of the design rules warrant attention. The manuscript is likely to be of interest to the synthetic biology and phase separation communities, but the strength of some claims exceeds what the presented evidence can support.
- **Who would be interested in the results, and why** Researchers in synthetic biology, protein design, and biomolecular condensate biology would find this work of interest. The demonstration of de novo designed CC-based LLPS provides a new toolkit for engineering cellular compartments, and the systematic parameter exploration (valency, linker, affinity) offers design rules that could be applied to other systems. The coarse-grained simulation framework may also be of interest to computational biologists working on phase separation prediction.
- **Major strengths** 
  1. The design strategy is conceptually clear and builds on well-understood CC interaction rules, providing a rational approach to LLPS engineering.
  2. The systematic exploration of parameters (valency, linker type, CC stability, arrangement) is thorough and provides useful design guidelines.
  3. The combination of experimental validation with coarse-grained simulations, including blind predictions, strengthens the conceptual framework.
  4. The demonstration of functional features (chemical regulation, multi-condensate coexistence, single-chain systems) extends the utility of the platform.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that "the stability of CC pairs, their number, linkers, and sequential arrangement govern the transition between diffuse, liquid and immobile condensates" and that this is "corroborated by coarse-grained molecular simulations."
  - **Evidence pointer** Results sections "Design of a two-chain LLPS condensate based on CC-dimer interactions", "Liquid properties of CC-LLPS condensates in mammalian cells", "The role of mismatch and CC stability on the condensate type formation", "Simulations of coiled-coil proteins recapitulate CC-LLPS"; Figures 2, 3
  - **Concern** The quantitative relationship between CC binding affinity and condensate properties is not rigorously established. The authors report Kd values for the P-set (low micromolar) and note the S-set is "too weak to be measured," but the S-set still forms condensates in cells. This raises the question of what affinity range is actually required for LLPS. Furthermore, the FRAP data are presented as mean ± SD with n values, but no statistical comparison between conditions is provided. The claim that 3-heptad CCs produce "liquid" condensates while 4-heptad CCs produce "immobile" condensates is based on qualitative FRAP recovery differences, but the quantitative threshold distinguishing these states is not defined. The simulation results are described as "consistent" with experiments, but the comparison appears qualitative; no quantitative metric (e.g., predicted vs. observed phase boundaries) is provided.
  - **Why it matters** The central claim of the paper is that CC stability governs the liquid-to-solid transition of condensates. Without quantitative correlation between measured affinities, FRAP recovery rates, and simulation predictions, this claim remains largely qualitative. The lack of statistical comparisons in FRAP data weakens the distinction between "liquid" and "immobile" states.
  - **Resolution test** Provide quantitative FRAP recovery curves with statistical comparisons (e.g., half-time of recovery, mobile fraction) across conditions. Establish a quantitative relationship between measured Kd values and condensate fluidity. Provide a quantitative comparison metric between simulation and experiment (e.g., predicted phase boundaries vs. observed condensation).
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that "through modular design, we achieve multiple coexisting condensates, chemical regulation of LLPS, condensate fusion, formation from either one or two polypeptide components or LLPS regulation by a third polypeptide chain."
  - **Evidence pointer** Results sections "CC-LLPS condensates composed of a single polypeptide chain", "Engineering programmable assembly and disassembly of LLPS condensates"; Figures 4, 5, 6
  - **Concern** The demonstration of multiple coexisting condensates (Figure 5) relies on the use of three different CC systems with orthogonal specificity. However, the evidence for orthogonality is not fully presented. The authors reference Supplementary Figure 13 for the design of these systems, but the specificity of each CC pair in the cellular context is not systematically demonstrated. For example, it is not shown that each condensate type contains only its intended components without cross-contamination. Additionally, the chemical regulation experiments (Figure 6) demonstrate rapamycin-induced assembly and disassembly, but the kinetics and reversibility of these processes are not quantified. The claim of "regulation by a third polypeptide chain" is supported by the data in Supplementary Figure 15, but the mechanism (competitive binding vs. sequestration) is not fully resolved.
  - **Why it matters** The modularity and programmability of the system are key selling points of the paper. If the orthogonality of the CC pairs is not rigorously demonstrated, the claim of multiple coexisting condensates is weakened. Similarly, the utility of the chemical regulation depends on its kinetics and reversibility, which are not characterized.
  - **Resolution test** Provide systematic evidence of CC pair orthogonality in cells (e.g., co-immunoprecipitation or FRET-based interaction assays). Quantify the kinetics of rapamycin-induced assembly and disassembly, and demonstrate reversibility over multiple cycles. Clarify the mechanism of third-polypeptide regulation with additional experiments (e.g., titration of the third polypeptide and measurement of condensate properties).
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Claim pointer** The authors state that "the design of liquid-liquid phase separated (LLPS) condensates based on de novo designed tunable modules that interact in a well-understood, controllable manner could improve our understanding of this phenomenon and enable the introduction of new features."
  - **Evidence pointer** Introduction, Discussion
  - **Concern** The novelty of the work relative to existing literature is not fully contextualized. The authors mention that CCs have been implicated in natural LLPS systems, but they do not discuss prior attempts to engineer CC-based LLPS in detail. The recent work on designed LLPS using other interaction motifs (e.g., repeat proteins, engineered IDRs) is not cited or compared. The claim that this is the first demonstration of de novo CC-based LLPS in mammalian cells may be true, but the authors do not explicitly state this or position their work against prior art.
  - **Why it matters** The scientific importance of the work depends on its novelty relative to existing approaches. Without a clear statement of what is new and how it advances beyond prior work, the significance of the contribution is difficult to assess.
  - **Resolution test** Add a paragraph in the Discussion that explicitly compares the CC-based approach to other engineered LLPS systems, highlighting what is uniquely enabled by the CC platform.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that "the simulations robustly predict the formation of condensates driven by CC interactions and are consistent with the experimentally established design principles."
  - **Evidence pointer** Results section "Simulations of coiled-coil proteins recapitulate CC-LLPS"; Figures 3, 4; Supplementary Figures 7, 9, 12, 15
  - **Concern** The coarse-grained simulation framework is described as having "a minimal set of tunable parameters," but the parameterization and validation of the model are not fully described in the main text. The authors state that parameters were "changed so that the shorter CCs in this study could form dimers with similar strength as the CCs used in the original CC LLPS framework," but the rationale for this change and its implications for the generality of the model are not discussed. The blind predictions (Supplementary Figure 15) are impressive, but the success rate and the criteria for "prediction" are not clearly defined. The simulation results are presented as snapshots and density profiles, but the quantitative agreement with experimental phase behavior is not systematically assessed.
  - **Why it matters** The simulation framework is presented as a predictive tool, but its reliability and limitations are not fully characterized. If the model is to be used for future design efforts, its predictive accuracy needs to be more rigorously established.
  - **Resolution test** Provide a more detailed description of the model parameterization and validation. Quantify the agreement between simulation and experiment (e.g., predicted vs. observed condensation propensity for a test set of designs). Discuss the limitations of the model and the conditions under which it is expected to be predictive.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Figure 1
  - **Evidence pointer** Figure 1b, c
  - **Issue** The figure legend states that cells were "transfected with 100 ng of a single plasmid" for Figure 1b, but the text in the Results section says "HEK293 cells transfected with plasmids for different constructs showed diffuse fluorescence in the cytoplasm." The cell type is inconsistent between the figure legend (NIH-3T3) and the text (HEK293). Clarify which cell type is shown in Figure 1b, c.
  - **Required correction** Ensure consistency between figure legends and text regarding cell types used in each experiment.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Results section "Liquid properties of CC-LLPS condensates in mammalian cells"
  - **Evidence pointer** Figure 2f
  - **Issue** The FRAP data are presented as "mean ± SD (n = 12 for mCit and n = 8 for BFP)" but the number of independent experiments is not stated. Clarify whether the n values represent individual condensates, cells, or independent transfections.
  - **Required correction** Specify the number of independent experiments and the unit of analysis for all quantitative measurements.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Methods section "Isothermal titration calorimetry"
  - **Evidence pointer** Methods, Supplementary Figure 2
  - **Issue** The ITC measurements were performed with peptide concentrations of 1 mM (P5f, P13f) and 100 µM (P6f, P14f) for the P-set, and 5.6 mM/560 µM for the S-set. The authors note that the S-set affinity was "too weak to be measured experimentally by ITC." However, the S-set still forms condensates in cells. This suggests that the effective local concentration of CC modules in the cellular context is much higher than the solution concentrations used in ITC. This point should be discussed.
  - **Required correction** Add a discussion of how solution-phase Kd values relate to cellular condensation behavior, considering local concentration effects.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Results section "Coarse-grained simulations of CC-LLPS"
  - **Evidence pointer** Figure 3k
  - **Issue** The MSD analysis is presented for 3- and 4-heptad proteins, but the units and the time range of the analysis are not specified in the figure legend. Clarify the simulation time scale and the units of the MSD values.
  - **Required correction** Provide units and time scales for all simulation-derived quantitative data.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Discussion
  - **Evidence pointer** Discussion, paragraph 2
  - **Issue** The statement that "designed CCs did not affect natural processes in mammalian cells" is made without citation or supporting data. If this is based on the authors' own observations, it should be stated as such and supported with data or a reference.
  - **Required correction** Provide a citation or qualify the statement as an observation from this study.
- **Technical failings that need to be addressed before the case is established** 
  1. Quantitative relationship between CC affinity and condensate properties (R1-M1)
  2. Rigorous demonstration of CC orthogonality in the multi-condensate system (R1-M2)
  3. Quantitative validation of the simulation framework against experimental data (R1-M4)
- **Assessment against Nature-style criteria** 
  - **Originality** The work is original in its use of de novo designed CC dimers as the sole interaction motif for LLPS in mammalian cells. While CCs have been implicated in natural condensates, the systematic engineering approach presented here is novel. The demonstration of single-chain LLPS and multi-condensate coexistence adds to the originality.
  - **Scientific importance** The work addresses a fundamental question in LLPS biology: what minimal design rules are required to drive phase separation? The identification of CC stability, valency, and arrangement as key parameters provides a framework for understanding natural systems and for engineering new ones. The potential applications in synthetic biology are significant.
  - **Interdisciplinary readership** The work bridges protein design, cell biology, and computational modeling, and would appeal to researchers in all three fields. The clear writing and well-organized figures make it accessible to a broad audience.
  - **Technical soundness** The experimental methods are generally sound, but the quantitative rigor of the biophysical characterization and the validation of the simulation framework need strengthening. The lack of statistical comparisons in FRAP data and the qualitative nature of the simulation-experiment comparison are notable weaknesses.
  - **Readability for nonspecialists** The manuscript is well-written and the concepts are explained clearly. The use of schematics (Figure 1a, Figure 7) helps convey the design strategy. However, some sections (e.g., simulation methods) may be challenging for nonspecialists.
- **Recommendation posture** Supportive if technical concerns are resolved. The core concept is interesting and the experimental work is largely well-executed, but the quantitative rigor of the biophysical characterization and the validation of the simulation framework need to be strengthened to fully support the claims made.

## Risk / unsupported claims
- The claim that CC stability "governs" the transition between liquid and immobile condensates is not quantitatively supported; the relationship between Kd and condensate fluidity is inferred but not directly demonstrated.
- The claim of "multiple coexisting condensates" relies on the orthogonality of the CC pairs, which is not systematically demonstrated in the provided material.
- The claim that the simulation framework "robustly predicts" LLPS behavior is based on qualitative comparisons; the predictive accuracy is not quantified.
- The statement that "designed CCs did not seem to have strong adverse effects on mammalian cells" is made without supporting data or citation.
- The claim that the S-set CCs have "too weak" affinity to be measured by ITC, yet still form condensates in cells, is not fully explained; the relationship between solution-phase affinity and cellular condensation is not addressed.