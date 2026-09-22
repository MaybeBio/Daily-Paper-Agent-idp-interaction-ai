## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and figure legends (figures themselves not provided)
- **Assessment boundary** Scientific claims, methodology, data interpretation, and internal consistency based solely on the provided manuscript text
- **Shared manuscript claim summary** The authors use atomistic MD simulations to show that reversible association between two LAF-1 RGG domains is dominated by sustained interactions mediated by a C-terminal contact-prone region (residues 138–168), and that extended conformational states are necessary for such sustained associations. Experimental phase separation assays on deletion mutants support the functional importance of this region.
- **Visible evidence base** Simulation trajectories (17 independent, ~18 μs total), conformational analysis (Rg distributions, asphericity), contact analysis (residue propensities, contact matrices), interaction analysis (hydrogen bonds, salt bridges), and phase separation experiments on WT and deletion mutants
- **Missing materials affecting confidence** Figures and supplementary figures not provided; simulation force field parameters and validation details incomplete; no error analysis or statistical treatment of simulation data; experimental details for phase diagrams partially described; no raw data or trajectory analysis scripts

## Reviewer

- **Overall assessment** This manuscript addresses an important question in the IDP field: whether sequence-localized interaction hotspots exist in low-complexity IDPs and how conformational fluctuations contribute to their emergence. The combination of unbiased atomistic MD with experimental validation is commendable and appropriate for the question. The central claim that a C-terminal region (138–168) acts as a contact-prone hotspot for sustained interactions is interesting and potentially significant. However, several technical concerns regarding simulation sampling, statistical robustness, and the interpretation of the experimental validation need to be addressed before the case is fully established. The manuscript is clearly written and accessible to a broad readership.

- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation, intrinsically disordered proteins, and biomolecular condensates would be the primary audience. The work is also relevant to those interested in sequence determinants of IDP interactions and the role of conformational dynamics in protein-protein interactions. The identification of a finite contact-prone region in a low-complexity IDP challenges the view of uniformly nonspecific IDP interactions and may inform engineering of synthetic condensates.

- **Major Strengths**
  1. The use of unbiased all-atom MD simulations with a modern force field (a99SB-disp/TIP4P-DE) is appropriate for studying IDP interactions at atomic resolution.
  2. The identification of two distinct interaction modes (transient vs. sustained) with different sequence propensities is a novel and important observation.
  3. The connection between conformational state (extended vs. compact) and interaction stability provides a mechanistic framework.
  4. Experimental validation using deletion mutants and phase diagrams directly tests the simulation-derived prediction.
  5. The manuscript is well-structured and clearly written, with appropriate context provided in the introduction.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that sustained associations dominate IDP interaction, contributing 4736 ns out of 6020 ns of accumulated association duration.
- **Evidence pointer** Results section "Reversible Association between LAF-1 RGG Domains", Figure 2
- **Concern** The statistical robustness of the association analysis is questionable. Only 14 out of 57 association events are classified as sustained, and these come from an unspecified number of independent trajectories. The authors state that "sustained protein association events are observed in two independent simulations" (Methods), which suggests that the dominant contribution to total association time comes from only 2 out of 17 trajectories. This raises concerns about whether the observed dominance of sustained associations is a general property of the system or an artifact of specific initial conditions or rare events in a small number of trajectories.
- **Why it matters** The central claim that sustained associations dominate IDP interaction depends critically on the statistical representativeness of the sampled trajectories. If the result is driven by a small number of trajectories, the conclusion may not be generalizable.
- **Resolution test** Provide a per-trajectory breakdown of association durations and sustained event counts. Report the number of trajectories contributing sustained events and assess whether the dominance of sustained associations holds when excluding outlier trajectories. Consider additional independent simulations to improve statistical power.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the C-terminal region 138–168 serves as a contact-prone region with more than twice the interaction propensity of other regions in sustained associations.
- **Evidence pointer** Results section "Comparison of the IDP Interactions with Different Durations", Figure 3
- **Concern** The definition of "contact propensity" and the statistical significance of the observed enrichment are not fully described. The authors report residue-level contact fractions but do not provide error bars, confidence intervals, or statistical tests comparing the C-terminal region to other regions. Given that the analysis is based on a limited number of sustained events (14), the enrichment could be driven by a few specific contacts rather than a general property of the region.
- **Why it matters** The identification of a specific contact-prone region is a key finding with implications for understanding sequence determinants of IDP interactions. Without statistical validation, the claim that this region is uniquely important is not fully supported.
- **Resolution test** Provide statistical analysis of contact propensities, including bootstrapping or block averaging across trajectories. Report confidence intervals for the enrichment of the C-terminal region and perform a formal comparison against other regions. Show that the enrichment is robust across individual sustained events.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that stretched conformation is a necessary condition for sustained association, based on the observation that all sustained associations involve at least one IDP with Rg > 2.8 nm in the early stage.
- **Evidence pointer** Results section "Conformation of IDPs in the Associations with Different Durations", Figure 4, Figure S12
- **Concern** The correlation analysis between early-stage conformation and association duration is based on a dichotomous classification (stretched vs. compact) with a correlation coefficient of 0.31. The authors state that stretched conformation is necessary but not sufficient for sustained association, but the evidence for necessity relies on the absence of sustained events with both IDPs compact. Given the small number of sustained events (14), the probability of observing no compact-compact sustained events by chance should be assessed. Additionally, the choice of Rg threshold (2.8 nm) and the time window for "early stage" (2 ns before and after contact) need justification.
- **Why it matters** The claim that conformational state determines interaction stability is mechanistically important. If the necessity claim is not statistically robust, the mechanistic interpretation is weakened.
- **Resolution test** Perform a statistical test for the association between conformational state and sustained duration (e.g., Fisher's exact test). Provide sensitivity analysis for the Rg threshold and time window choices. Discuss the physical rationale for the chosen parameters.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that the contact-prone region is important for LLPS, validated by phase separation experiments showing that deletion of residues 138–168 weakens phase separation.
- **Evidence pointer** Results section "Experimental Verification", Figure 5
- **Concern** The experimental validation is limited to a single deletion mutant (Δ138–168) and one comparison mutant (Δ1–31). While the result is consistent with the simulation prediction, the interpretation is complicated by the fact that deleting 31 residues may alter overall protein properties (e.g., net charge, hydrophobicity, solubility) beyond simply removing the contact-prone region. The authors do not discuss potential confounding effects of the deletion on protein stability or expression levels.
- **Why it matters** The experimental validation is crucial for establishing biological relevance. If the deletion has nonspecific effects, the conclusion that the contact-prone region specifically drives LLPS is not fully supported.
- **Resolution test** Provide additional characterization of the deletion mutants (e.g., circular dichroism, size exclusion chromatography, expression yields). Consider point mutations within the 138–168 region rather than complete deletion. Discuss how the deletion might affect protein properties beyond removing the contact-prone region.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the a99SB-disp force field with TIP4P-DE water model is appropriate for studying IDP interactions.
- **Evidence pointer** Methods section "Computational Details"
- **Concern** While a99SB-disp is a modern force field optimized for disordered proteins, the authors do not provide validation of the force field for this specific system. No comparison with experimental data (e.g., radius of gyration from SAXS, chemical shifts from NMR) is provided to confirm that the simulated conformational ensemble matches the experimental one. The choice of simulation length (1000–1500 ns per trajectory) may be insufficient for converged sampling of IDP conformational ensembles.
- **Why it matters** The reliability of all simulation-derived conclusions depends on the accuracy of the force field and the convergence of sampling. Without validation, the quantitative claims about interaction durations and propensities may be force field-dependent.
- **Resolution test** Provide validation of the simulated conformational ensemble against available experimental data (e.g., SAXS, FRET, NMR chemical shifts). Show convergence of key observables (Rg distribution, contact maps) as a function of simulation time. Discuss the expected impact of force field choice on the conclusions.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states "the sustained associations essentially dominate the IDP interaction" without providing quantitative context. The reader cannot assess the magnitude of this dominance from the abstract alone.
- **Required correction** Include a quantitative statement in the abstract, e.g., "sustained associations (>100 ns) account for approximately 75% of total interaction time despite representing only 25% of association events."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, simulation setup
- **Evidence pointer** Methods section "Reversible Association between LAF-RGG Domains"
- **Issue** The initial distance between the two proteins is set to 6 nm (center of mass), but the rationale for this choice is not provided. The protein concentration in the simulation box (16.9 mg/mL) is stated to be on the same order as experimental conditions, but the relationship between box size, protein concentration, and the ability to observe association events is not discussed.
- **Required correction** Provide justification for the initial separation distance and discuss how the box size and protein concentration affect the frequency and nature of association events.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion of biological relevance
- **Evidence pointer** Conclusions section
- **Issue** The authors mention that the contact-prone region is rich in charged and polar residues and is overall neutral, but they do not discuss how this relates to known sequence features of other RGG domains or IDPs involved in LLPS. The broader implications for understanding LLPS mechanisms could be strengthened.
- **Required correction** Add a brief discussion comparing the identified contact-prone region with known interaction hotspots or stickers in other IDP systems, and discuss the generalizability of the findings.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Figure legends
- **Evidence pointer** Figures 2, 3, 4
- **Issue** The figure legends are not provided in the manuscript text, making it difficult to fully interpret the results described in the text.
- **Required correction** Ensure figure legends are complete and self-explanatory, including definitions of all abbreviations and statistical annotations.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, experimental section
- **Evidence pointer** Methods section "Protein Engineering, Expression, and Purification"
- **Issue** The methods mention a Δ70–100 mutant in the cloning list, but this mutant is not discussed in the results or conclusions. It is unclear whether this mutant was characterized and, if so, what the results were.
- **Required correction** Either present the results for the Δ70–100 mutant or remove it from the methods section to avoid confusion.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Readability
- **Affected element** Introduction
- **Evidence pointer** Introduction, paragraph 2
- **Issue** The introduction states that "the comprehensive descriptions about the reversible interaction of IDP as well as its relationship with the inherent conformational fluctuations and sequence features of IDP are still limited." This is somewhat vague and could be more specific about what is missing in the current literature.
- **Required correction** Specify the gaps in current knowledge more precisely, e.g., lack of atomistic resolution on IDP interaction dynamics, limited understanding of how conformational fluctuations create transient interaction hotspots, etc.

## Risk / unsupported claims
- The claim that sustained associations "essentially dominate" IDP interaction is based on a small number of events from a limited number of trajectories and requires statistical validation.
- The claim that the C-terminal region 138–168 is a "contact-prone region" with more than twice the propensity of other regions is not supported by statistical analysis.
- The claim that stretched conformation is a "necessary condition" for sustained association is based on a small sample and requires formal statistical testing.
- The experimental validation using deletion mutants does not fully exclude nonspecific effects of the deletion on protein properties.
- The force field accuracy and simulation convergence are not validated against experimental data, limiting confidence in quantitative conclusions.
- The biological relevance of the identified contact-prone region to LLPS in the full-length LAF-1 protein (with its folded domains) is acknowledged as a limitation but not addressed experimentally.