## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, materials and methods summary, and supplementary figure legends as provided.
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims by presented evidence. Editorial or stylistic issues are noted only where they affect scientific clarity.
- **Shared manuscript claim summary** The authors propose that the viscoelasticity of biomolecular condensates is governed by sticker motif strength and chain length, but that the flow activation energy is determined solely by intermolecular interaction strength and is independent of chain length. They further claim that biomolecular diffusion in the dense phase is reaction-limited and correlates with flow activation energy rather than bulk viscosity.
- **Visible evidence base** Microrheology data (pMOT), temperature-controlled video particle tracking (VPT), FRAP measurements, all-atom molecular dynamics simulations with umbrella sampling, coarse-grained simulations with direct coexistence and Green-Kubo viscosity calculations, and Rouse mode analysis. Figures 1–6 and supplementary figures S1–S15 are referenced.
- **Missing materials affecting confidence** Full experimental protocols are deferred to Supplementary Materials, which were not provided. Detailed simulation parameters, force field details, and analysis procedures for the coarse-grained model are not fully described in the visible text. Raw data files and statistical analysis details are not available. Figure S15 is referenced but its content is not described in the visible text.

## Reviewer
- **Overall assessment** This manuscript addresses an important question in the condensate field: what molecular features control viscoelasticity versus flow activation energy, and how do these relate to transport? The combination of experimental rheology with all-atom and coarse-grained simulations is ambitious and potentially powerful. The central claim, that flow activation energy is independent of chain length but sensitive to interaction strength, is interesting and, if correct, would be a useful conceptual advance. However, the evidence as presented has several gaps. The experimental distinction between viscosity changes and activation energy invariance across chain lengths relies on fits whose quality is not fully shown. The connection between simulated dissociation free energies and measured activation energies is qualitative. The FRAP interpretation, which is central to the transport claim, depends on assumptions about bleaching and recovery that are not fully discussed. The manuscript is readable and the figures appear well organized, but several claims go beyond what the visible evidence supports.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, and intracellular organization would be the primary audience. The work is also relevant to the broader soft matter and polymer physics community interested in associative polymer networks, viscoelasticity, and reaction-diffusion transport. The methodological combination of microrheology with simulations may interest biophysicists developing tools to characterize material properties of biological fluids.
- **Major strengths** The study tackles a question of genuine importance: disentangling the roles of interaction strength and polymer length in condensate material properties. The use of a designed peptide-ssDNA system with systematic sequence and length variation is a sensible approach. The combination of multiple experimental techniques (pMOT, VPT, FRAP) with two levels of simulation (all-atom and coarse-grained) is comprehensive. The finding that flow activation energy is insensitive to chain length, if robust, would be a useful design principle. The observation that peptide diffusion does not track bulk viscosity is thought-provoking and could have implications for how transport is interpreted in condensate studies.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of activation energy determination
- **Claim pointer** The authors claim that flow activation energy is independent of chain length for both ssDNA length variation (dT20 to dT200) and peptide repeat number variation (n = 3, 5, 7).
- **Evidence pointer** Figures 3F–H, 4A–C, fig. S11, fig. S12, table S1
- **Concern** The activation energies are extracted from Arrhenius fits of viscosity versus temperature. The visible text reports values with uncertainties (e.g., 17 ± 1 RT for [RGRGG]5-dT40), but the quality of the linear fits is not shown for all conditions. For the chain length series, the claim of invariance rests on comparing slopes across conditions. If the temperature range is narrow or the viscosity range is limited, the fits may not have sufficient power to detect modest differences. The number of independent measurements, the temperature points used, and the reproducibility across condensate batches are not reported in the visible text. The uncertainty on the activation energy for the dT200 and n = 7 conditions is not stated, making it difficult to assess whether the invariance claim is statistically meaningful.
- **Why it matters** The chain-length independence of activation energy is a central conclusion of the paper. If the fits are underpowered or the uncertainties are large, the conclusion may not be robust. This claim also underpins the later interpretation that diffusion is reaction-limited rather than viscosity-dominated.
- **Resolution test** Provide Arrhenius plots with fit lines and residuals for all conditions. Report the number of independent replicates, the temperature range, and the number of temperature points. State the uncertainty on each activation energy and perform a statistical test for equality of slopes across chain lengths.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Support for mechanistic interpretation from simulations
- **Claim pointer** The authors claim that all-atom simulations reveal that flow activation energy is linked to the dissociation of sticker motifs from DNA chains, and that coarse-grained simulations corroborate this by showing higher dissociation barriers give rise to denser condensates with higher critical temperatures and viscosities.
- **Evidence pointer** Figures 2G–J, 5A–G, fig. S14
- **Concern** The connection between simulated dissociation free energies and measured activation energies is qualitative. The all-atom simulations use single peptide-DNA pairs, not condensates, and the free energy profiles show two-state dissociation with barriers that are not quantitatively compared to the measured activation energies. The coarse-grained simulations extract activation energies from Green-Kubo viscosity calculations, but the visible text does not report the actual values or their uncertainties. The claim that "higher dissociation barriers give rise to denser condensates featuring higher critical temperatures and viscosities" is presented as a correlation, but the statistical strength of this correlation is not given. The Rouse mode analysis in Figure 5G shows different relaxation timescales, but the connection to the measured activation energies is not made explicit.
- **Why it matters** The simulations are used to provide a microscopic mechanism for the experimental observations. If the link is only qualitative, the mechanistic claim is not established. The paper would be stronger if the simulated activation energies were quantitatively compared to the experimental values, or if the simulations made a prediction that was then tested experimentally.
- **Resolution test** Report the simulated activation energies with uncertainties and compare them directly to the experimental values. Provide a quantitative correlation between dissociation barriers and critical temperatures or viscosities, with appropriate statistics. Clarify how the Rouse mode analysis relates to the measured activation energies.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation of FRAP data and transport claim
- **Claim pointer** The authors claim that peptide diffusion in the dense phase is inversely correlated with flow activation energy and is not substantially altered by ssDNA length variation, even when bulk viscosity changes by an order of magnitude. They interpret this as evidence for a reaction-limited diffusion mechanism.
- **Evidence pointer** Figure 6A–D, fig. S15
- **Concern** The FRAP experiments measure diffusion of fluorescently labeled peptides. The visible text reports diffusion timescales (τD) but does not describe the FRAP model used to extract these values, the assumptions about bleaching profile, or the potential contribution of binding-unbinding kinetics to the recovery. The claim that diffusion is "not substantially altered" by ssDNA length is based on comparing τD values across conditions, but the uncertainties on these values are not reported for all conditions. The interpretation that the data support a reaction-limited mechanism requires ruling out other explanations, such as changes in mesh size or excluded volume effects that might coincidentally compensate for viscosity changes. The partial recovery observed for Cy5-dT40 in fig. S15 is mentioned but not quantified or discussed in the context of the transport model.
- **Why it matters** The transport claim is a major conclusion with implications for how FRAP data are interpreted in the condensate field. If the FRAP analysis is not rigorous or the alternative explanations are not excluded, the conclusion is not established.
- **Resolution test** Provide a detailed description of the FRAP model, including assumptions and validation. Report uncertainties on all τD values and perform statistical comparisons across conditions. Discuss and, if possible, rule out alternative explanations for the observed diffusion behavior.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of the findings
- **Claim pointer** The authors state in the Discussion that their findings "have implications on the way macromolecular diffusion within condensates is regulated" and suggest that their approach "will enable precise comparisons of biomolecular condensates that feature macromolecules with distinct sequences and sizes."
- **Evidence pointer** Discussion section
- **Concern** The study uses a single model system: RG-rich peptides with ssDNA. The authors do not test whether their conclusions hold for other types of condensates, such as those formed by proteins with different sticker chemistries, RNA instead of DNA, or systems with post-translational modifications. The claim that flow activation energy is a "unique reporter of the strength of multivalent intermolecular interactions" is presented as a general principle, but it is only demonstrated for one system.
- **Why it matters** The broader relevance of the findings depends on whether they generalize beyond the specific peptide-ssDNA system studied. Without testing additional systems, the generality of the claims is uncertain.
- **Resolution test** Either temper the generalizing language in the Discussion or add experiments or simulations with at least one additional condensate-forming system to test the generality of the conclusions.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Materials and Methods section
- **Evidence pointer** Materials and Methods, Supplementary Materials
- **Issue** The Materials and Methods section states that details are provided in the Supplementary Materials, but the supplementary file was not available for review. Key experimental details, such as the concentration of peptides and DNA, buffer conditions for each experiment, and the number of replicates, are not stated in the visible text.
- **Required correction** Provide the key experimental parameters in the main text or ensure the Supplementary Materials are available to reviewers.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figures 1–6
- **Evidence pointer** Figures 1–6, table S1
- **Issue** The number of independent measurements for each data point is not consistently reported. For example, the viscosity values in Figure 1D and the activation energies in Figure 2F are presented with error bars, but the number of replicates is not stated in the figure legends or the visible text.
- **Required correction** Add the number of independent replicates to all figure legends and table entries.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of Figure 5G
- **Affected element** Figure 5G
- **Evidence pointer** Figure 5G
- **Issue** The Rouse mode analysis shows relaxation timescales for ssDNA chains in the presence of three peptides, but the visible text does not explain how these timescales were computed or what the error bars represent. The connection to the measured activation energies is not made explicit.
- **Required correction** Expand the description of the Rouse mode analysis in the main text or figure legend, and clarify the relationship between the simulated relaxation timescales and the experimental activation energies.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The Discussion does not acknowledge potential limitations of the study, such as the use of a single model system, the assumptions in the FRAM analysis, or the qualitative nature of the simulation-experiment comparison.
- **Required correction** Add a paragraph acknowledging the limitations of the study and suggesting directions for future work.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract, Introduction
- **Issue** The term "flow activation energy" is used throughout, but it is not explicitly defined in the main text. The relationship between this quantity and the activation energy of viscous flow from the Arrhenius equation is implied but not stated.
- **Required correction** Define "flow activation energy" explicitly when it is first introduced, and clarify its relationship to the Arrhenius equation.

## Risk / unsupported claims
- The claim that flow activation energy is independent of chain length is not fully supported because the statistical power of the Arrhenius fits across chain lengths is not demonstrated.
- The claim that simulations provide a microscopic origin for the flow activation energy is qualitative and not quantitatively validated against experiments.
- The claim that peptide diffusion is reaction-limited rather than viscosity-dominated is not fully established because alternative explanations are not ruled out and the FRAP model is not described.
- The generalizing statements in the Discussion about the implications for other condensate systems are not supported by data from additional systems.
- The statement that "flow activation energy is a unique reporter of the strength of multivalent intermolecular interactions" is presented as a general principle but is only demonstrated for one model system.