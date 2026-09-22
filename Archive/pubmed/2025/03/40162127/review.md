## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary figure references
- **Assessment boundary** Scientific claims, experimental and simulation methodology, data interpretation, and consistency between evidence and conclusions as presented in the provided text
- **Shared manuscript claim summary** The authors present synDrops, a synthetic inducible phase-separation system, to study how the crowded, active cytoplasm affects mesoscale biomolecular condensate formation. They claim that macromolecular crowding promotes nucleation but inhibits growth, and that ATP-dependent actomyosin dynamics promotes growth by reducing confinement and elasticity.
- **Visible evidence base** Results sections with figures referenced (Figs. 1-7), appendices A-E, supplementary methods, and simulation descriptions
- **Missing materials affecting confidence** Actual figure images, numerical data values, statistical test details, simulation parameter tables, and supplementary movies were not provided in the text

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question in the condensate field: how the complex intracellular environment, rather than simple buffer conditions, affects phase separation. The synDrops system is thoughtfully designed with clear advantages over endogenous condensate studies. The combination of in vivo experiments with two independent simulation platforms is a strength. However, the manuscript has several technical concerns that need to be addressed, particularly regarding the interpretation of the osmotic compression experiments, the quantitative link between simulations and experiments, and the mechanistic claims about actomyosin dynamics. The core conclusions are plausible but not fully established from the evidence presented.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, intracellular biophysics, and cytoskeletal dynamics would be interested. The work bridges soft matter physics and cell biology, and the synDrops system could become a useful tool for the community. The findings on crowding and active matter effects on condensate assembly have implications for understanding endogenous condensate regulation in health and disease.

- **Major strengths** The synDrops system is a well-designed synthetic tool with defined geometry and inducibility, enabling controlled kinetic analysis. The combination of two independent simulation platforms (HOOMD-blue and custom Java) with experimental validation is rigorous. The study addresses a gap in the field by examining physical, rather than purely biochemical, determinants of condensate formation. The use of multiple orthogonal perturbations (osmotic compression, rapamycin, ATP depletion, actomyosin inhibition) strengthens the conclusions.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental design and interpretation
- **Claim pointer** The authors claim that osmotic compression increases macromolecular crowding and that this promotes nucleation but inhibits growth.
- **Evidence pointer** Results section, Fig. 2a-b, Fig. 12a-c in Appendix C
- **Concern** Osmotic compression is a pleiotropic perturbation. It increases macromolecular crowding but also changes cell volume, ionic strength, membrane tension, and potentially signaling pathways. The authors attempt to control for protein concentration changes by grouping cells into quantiles based on fluorescence intensity, but this does not fully account for other osmotic effects. The claim that the observed effects are specifically due to crowding requires more direct evidence.
- **Why it matters** The central conclusion that crowding promotes nucleation but inhibits growth depends on this interpretation. If other osmotic effects contribute, the mechanistic model is incomplete.
- **Resolution test** Provide additional controls such as genetic or pharmacological perturbations that alter crowding without changing osmolarity, or use inert crowder molecules in a cell-free system to recapitulate the observed effects.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative rigor and simulation-experiment link
- **Claim pointer** The authors claim that simulations and experiments are consistent in showing that crowding promotes nucleation but inhibits growth.
- **Evidence pointer** Results section, Figs. 3-5, Appendix A
- **Concern** The quantitative link between simulations and experiments is not clearly established. The authors note a discrepancy in time scales and droplet sizes between simulations and experiments but do not explain how this affects the comparison. The simulation parameters (binding affinity of 10.8 kBT, volume fractions of 30-50%) are not clearly justified against experimental conditions. The claim of consistency between simulations and experiments appears qualitative rather than quantitative.
- **Why it matters** The manuscript's strength is the combination of experiments and simulations. If the quantitative correspondence is not established, the simulations serve more as illustrative models than as validating evidence.
- **Resolution test** Provide quantitative metrics comparing simulation and experimental results, such as scaling relationships for nucleation rate and growth rate as functions of crowding, and demonstrate that these match within a defined tolerance.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic claim about actomyosin
- **Claim pointer** The authors claim that actomyosin dynamics is the dominant mechanism that increases mesoscale diffusivity and promotes droplet growth in mammalian cells.
- **Evidence pointer** Results section, Fig. 4c, Fig. 7a-b
- **Concern** The JLY cocktail inhibits actin polymerization, depolymerization, and myosin II activity simultaneously. This makes it difficult to attribute the observed effects specifically to actomyosin contractility versus other actin-dependent processes. Additionally, the claim that actomyosin dynamics is "dominant" is based on a comparison with total ATP depletion, but the JLY treatment may not fully inhibit all actomyosin-dependent processes. The authors also note that increasing diffusivity alone is insufficient to rescue growth, which complicates the mechanistic model.
- **Why it matters** The conclusion that actomyosin dynamics is the dominant ATP-dependent mechanism for promoting condensate growth is a key finding. If the perturbation is not specific, the conclusion is overstated.
- **Resolution test** Use more specific inhibitors (e.g., blebbistatin alone for myosin II, or latrunculin alone for actin polymerization) and compare their effects individually and in combination. Also, measure actomyosin contractility directly (e.g., via traction force microscopy or FRET-based tension sensors) to confirm the level of inhibition.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Statistical rigor
- **Claim pointer** The authors make quantitative claims about differences in droplet number, size, and diffusivity across conditions.
- **Evidence pointer** Results section, Figs. 2, 4, 7
- **Concern** The manuscript does not report statistical details such as the number of biological replicates, number of cells analyzed, or statistical tests used. Error bars are shown in figures but the meaning (SD, SEM, CI) is not stated. This makes it difficult to assess the robustness of the reported differences.
- **Why it matters** Quantitative claims require appropriate statistical support. Without this information, the reliability of the conclusions cannot be evaluated.
- **Resolution test** Add a statistics section detailing the number of replicates, cells analyzed, statistical tests used, and the definition of error bars for each figure.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Introduction, first paragraph
- **Evidence pointer** Introduction, paragraph 1
- **Issue** The statement that mesoscale particles are more affected by crowding than nanoscale particles is presented as a general principle, but the reasoning is somewhat compressed.
- **Required correction** Expand the explanation of why mesoscale particles are more affected by crowding, perhaps with a brief discussion of the relative sizes of particles and crowders.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodology
- **Affected element** Methods, drug treatment section
- **Evidence pointer** Methods, drug treatment
- **Issue** The concentration of DMSO used as solvent control is not stated.
- **Required correction** State the DMSO concentration used in control experiments to ensure it does not have independent effects.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion, paragraph on heterogeneity
- **Evidence pointer** Discussion, final paragraph
- **Issue** The speculation about local heterogeneity in crowding and activity is interesting but not directly supported by data presented.
- **Required correction** Clearly label this as speculation and consider whether any data in the manuscript could be re-analyzed to provide preliminary support.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure 3a
- **Evidence pointer** Results, Fig. 3a
- **Issue** The clustergram and its interpretation are described in the text but the figure itself is not shown in the provided material.
- **Required correction** Ensure the figure is clear and self-explanatory, with a legend that explains the color scale and the meaning of the clusters.

- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3. The pleiotropic effects of osmotic compression, the lack of quantitative simulation-experiment correspondence, and the non-specific actomyosin inhibition are the key technical issues that prevent the core conclusions from being fully established.

- **Assessment against Nature-style criteria** 
  - Originality: High. The synDrops system is a novel tool, and the focus on physical determinants of condensate formation in living cells is relatively underexplored.
  - Scientific importance: High. Understanding how the intracellular environment affects condensate formation is fundamental to cell biology and has implications for disease mechanisms.
  - Interdisciplinary readership: Good. The work bridges cell biology, biophysics, and soft matter physics, and should appeal to readers across these fields.
  - Technical soundness: Moderate. The experimental and simulation approaches are generally sound, but the concerns above about perturbation specificity and quantitative rigor need to be addressed.
  - Readability for nonspecialists: Good. The manuscript is generally well-written and the concepts are explained clearly, though some simulation details may be challenging for non-experts.

- **Recommendation posture** Supportive if technical concerns are resolved. The synDrops system is a valuable contribution, and the overall conclusions are plausible. However, the concerns about perturbation specificity and quantitative rigor must be addressed before the case is fully established.

## Risk / unsupported claims
- The claim that actomyosin dynamics is the "dominant" mechanism for promoting condensate growth in mammalian cells is not fully supported given the non-specific JLY inhibition.
- The claim that the effects of osmotic compression are specifically due to crowding is not fully established given the pleiotropic nature of the perturbation.
- The quantitative correspondence between simulations and experiments is asserted but not demonstrated with specific metrics.
- The statement that physiological crowding (~30-35%) is "optimal" for large condensate formation is based on a limited set of conditions and may be an overgeneralization.
- The speculation about local heterogeneity in crowding and activity as a regulatory mechanism is not directly supported by data.