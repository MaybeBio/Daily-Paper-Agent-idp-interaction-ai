## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) and figure references, but no actual figures or supplementary materials were provided.
- **Assessment boundary** Assessment is limited to the written text, methodological descriptions, and reported numerical results. Figures, tables, and supplementary materials referenced in the text were not available for direct inspection.
- **Shared manuscript claim summary** The authors use all-atom and coarse-grained molecular dynamics simulations to characterize the conformational ensemble of monomeric TDP-43, identify a network of transient interdomain interactions (involving NTD, RRM1/2, linkers L1/L2, and CTD), and argue that these interactions are predominantly electrostatic, salt-sensitive, and relevant to TDP-43 phase separation.
- **Visible evidence base** Text descriptions of simulation methods, force fields, system setups, and analysis protocols; reported Rg values, contact map descriptions, and qualitative comparisons to experimental data. No primary data files, figures, or supplementary information were accessible.
- **Missing materials affecting confidence** All figures (main and supplementary), simulation trajectory data, contact map plots, Rg distributions, density profiles, and validation plots (Figure S7, S8) were not available. This substantially limits the ability to verify quantitative claims and the quality of the simulation analyses.

## Reviewer
- **Overall assessment** The manuscript presents a plausible and potentially useful multiscale simulation study of TDP-43, addressing an important gap in understanding heterodomain interactions in this disease-relevant protein. The methodological approach is reasonable, and the qualitative conclusions are consistent with existing experimental literature. However, the absence of figures and supplementary data prevents a full evaluation of the quantitative claims, the robustness of the simulation analyses, and the strength of the validation. The central claim that heterodomain interactions modulate phase behavior is supported by the text but requires closer scrutiny of the contact analyses and the CG model validation.
- **Who would be interested in the results, and why** Researchers studying TDP-43 biology, phase separation of multidomain proteins, and computational modeling of protein conformational ensembles. The findings may also be of interest to those investigating ALS/FTD mechanisms, as the work provides a molecular-level framework for understanding how interdomain interactions and salt sensitivity could influence TDP-43 aggregation and condensation.
- **Major strengths** The study addresses a relevant and under-explored question about heterodomain interactions in TDP-43. The multiscale approach (all-atom plus coarse-grained) is appropriate and leverages complementary strengths. The authors are transparent about limitations of the CG model and attempt validation against both all-atom simulations and experimental data. The connection between dilute-phase conformational ensembles and condensed-phase interactions is conceptually important and well motivated.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (CG model validation), R1-M2 (quantitative support for electrostatic claim), R1-M3 (generalizability of monomeric simulations to condensed phase).
- **Assessment against Nature-style criteria**  
  - **Originality** Moderate. The concept of interdomain interactions modulating phase behavior is not entirely new, but the specific focus on TDP-43 heterodomain interactions and the multiscale approach provide some novelty.  
  - **Scientific importance** Moderate to high. TDP-43 is a key protein in neurodegeneration, and understanding its phase behavior is of broad interest. However, the study is largely computational and does not provide new experimental validation.  
  - **Interdisciplinary readership** Moderate. The work bridges computational biophysics and cell biology, but the technical nature may limit appeal to a broad audience.  
  - **Technical soundness** Not fully assessable without figures and supplementary data. The methods are generally sound, but the validation of the CG model and the contact analyses need closer inspection.  
  - **Readability for nonspecialists** Acceptable. The text is generally clear, but some sections (e.g., CG model parameterization) may be dense for non-experts.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising and the methodology is appropriate, but the current evidence base (as presented in text only) is insufficient to fully establish the claims. Access to figures and supplementary data is essential for a definitive assessment.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / Validation
- **Claim pointer** The authors claim that the CG model, after temperature adjustment, reproduces the all-atom conformational ensemble and is suitable for studying TDP-43 phase behavior.
- **Evidence pointer** Methods section "Validation of monomeric TDP-43 CG ensemble against all-atom simulations"; Figure S7a-c (not provided)
- **Concern** The validation of the CG model relies on comparing Rg distributions and contact maps between CG and all-atom simulations. However, the text states that the CG model at 300 K produces more compact conformations (Rg = 3.16 nm) than all-atom (Rg = 3.56 nm), and the authors compensate by increasing the simulation temperature to 320/330 K. This temperature adjustment is a pragmatic but potentially problematic approach, as it may alter the balance of interactions in ways not captured by Rg alone. The contact map comparison (Figure S7b,c) is described as showing "qualitative agreement," but the text also notes "sparser intra-CTD and NTD-CTD contacts in CG simulations." This discrepancy is concerning because these are precisely the interactions that the manuscript claims are important. Without seeing the actual contact maps and quantitative measures of agreement, it is difficult to assess whether the CG model faithfully captures the interdomain interaction network.
- **Why it matters** The CG model is the primary tool used to study the condensed phase. If the model does not accurately reproduce the key interactions identified in the all-atom simulations, the conclusions about heterodomain interactions in the condensed phase are not reliable.
- **Resolution test** Provide the actual Rg distributions and contact maps for both CG and all-atom simulations, along with quantitative metrics of agreement (e.g., Jensen-Shannon divergence for Rg, contact map correlation coefficients). Demonstrate that the temperature-adjusted CG model reproduces not only Rg but also the specific interdomain contacts (especially NTD-CTD and intra-CTD) observed in all-atom simulations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength / Quantitative support
- **Claim pointer** The authors claim that "heterodomain interactions are predominantly electrostatic in nature and sensitive to salt," based on contact analysis and high-salt simulations.
- **Evidence pointer** Results section "Heterodomain interactions are predominantly electrostatic in nature and sensitive to salt"; Figures 4a-d, S5a-d (not provided)
- **Concern** The claim that the interactions are "predominantly electrostatic" is supported by two lines of evidence: (1) enrichment of salt-bridge pairs in the all-atom contact analysis, and (2) loss of interactions at 300 mM NaCl. However, the text does not provide quantitative data, such as the fraction of contacts attributed to salt bridges versus other interaction types, or the magnitude of the change in contact frequencies at high salt. The statement that "the increase in salt concentration led to a clear shift in the Rg probability distribution" is qualitative. Without numerical values, it is not possible to assess the strength of the electrostatic contribution relative to other forces (e.g., hydrophobic, pi-pi). Furthermore, the CG model uses a Debye-Hückel potential with a fixed screening length, which is a simplified treatment of electrostatics; the authors should discuss whether this approximation could bias the conclusion.
- **Why it matters** The electrostatic nature of the interactions is a central claim of the paper and is used to connect the simulations to experimental observations of salt sensitivity. If the evidence is not quantitative, the claim remains suggestive rather than established.
- **Resolution test** Provide quantitative data: (a) the percentage of interdomain contacts that are salt bridges versus other types in the all-atom simulations; (b) the change in contact frequency for specific interdomain pairs (e.g., NTD-CTD, L1-RRM2) at 100 vs 300 mM NaCl, with error bars; (c) a comparison of the Rg distributions at both salt concentrations with statistical significance tests.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability / Interpretation
- **Claim pointer** The authors suggest that the interdomain interactions observed in the monomeric (dilute phase) simulations are "also prevalent in the condensed phase" and that they "modulate the phase behavior of TDP-43."
- **Evidence pointer** Results section "CG simulations of TDP-43 condensates reveal a complex network of homo- and heterodomain intermolecular interactions"; Figures 3a,b, S8a-d (not provided)
- **Concern** The connection between monomeric conformational ensembles and condensed-phase behavior is a key conceptual leap. The authors argue that intramolecular interactions in the dilute phase resemble intermolecular interactions in the condensed phase, citing prior work. However, the text does not provide a direct comparison of the interaction networks in the two phases. The CG condensed-phase simulations are performed with a monomeric model, and the authors justify this by showing that dimeric models (NTD-dimer, CR-dimer) produce similar contact maps. This is a reasonable approach, but the text does not quantify the similarity (e.g., correlation coefficients for contact maps). Moreover, the manuscript does not discuss whether the transient nature of the interactions in the dilute phase is preserved in the condensed phase, or whether the crowded environment could alter the interaction preferences.
- **Why it matters** The claim that the same interactions drive both conformational ensembles and phase separation is central to the paper's significance. If the evidence for this connection is weak, the impact of the study is diminished.
- **Resolution test** Provide a direct comparison of intra- and intermolecular contact maps (e.g., Figure 3a vs Figure 2c), with quantitative similarity metrics. Discuss whether the transient interactions observed in the monomer are stable enough to persist in the condensed phase, and whether the CG model captures this.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity / Reproducibility
- **Affected element** Methods section "All-atom MD simulations"
- **Evidence pointer** Methods section, "Simulation protocol"
- **Issue** The text states "5 μs production simulations were performed for 5 μs in the NVT ensemble" which is redundant. Also, the use of the Langevin Middle Integrator with a friction coefficient of 1 ps⁻¹ is mentioned, but the collision rate is not specified. For reproducibility, the exact simulation parameters should be listed.
- **Required correction** Reword the sentence to "5 μs production simulations were performed in the NVT ensemble." Specify the Langevin collision rate and any other relevant parameters (e.g., temperature coupling, pressure coupling details).

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Interpretation / Literature context
- **Affected element** Discussion section
- **Evidence pointer** Discussion, first paragraph
- **Issue** The authors mention that "recent successes in the purification of TDP-43 in vitro coupled with in vivo studies have provided rich insights" but do not cite specific studies. Given the importance of connecting simulations to experiments, a few key references would strengthen the discussion.
- **Required correction** Add citations to recent experimental studies on TDP-43 phase separation and purification, particularly those that report salt sensitivity or interdomain interactions.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical detail / Model limitations
- **Affected element** Methods section "Coarse-grained (CG) MD simulations"
- **Evidence pointer** Methods section, "System setup"
- **Issue** The CG model uses a Debye-Hückel potential with a screening length corresponding to ~100 mM salt. The authors should clarify whether the high-salt simulations (300 mM) were performed by adjusting the screening length, and whether this is the only salt-dependent parameter in the model.
- **Required correction** State explicitly how salt concentration is modeled in the CG simulations and whether other parameters (e.g., hydrophobic interactions) are salt-dependent.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation / Figure quality
- **Affected element** Figure 5 (referenced in Discussion)
- **Evidence pointer** Discussion, final paragraph
- **Issue** The text refers to "Figure 5" as a summary of the proposed interaction network, but the figure was not provided. The description in the text is brief and does not fully explain the schematic.
- **Required correction** Ensure Figure 5 is self-explanatory and include a detailed legend that describes the proposed model, including the specific interactions and their proposed roles in phase separation.

## Risk / unsupported claims
- The claim that heterodomain interactions are "predominantly electrostatic" is not quantitatively supported in the text; the evidence is qualitative and requires the actual contact analysis data.
- The claim that the CG model is validated against all-atom simulations is weakened by the acknowledged discrepancies in intra-CTD and NTD-CTD contacts; the text does not provide quantitative measures of agreement.
- The claim that the interdomain interactions observed in the monomeric state are "prevalent in the condensed phase" is based on a comparison that is not shown or quantified in the text.
- The statement that the CG model at 320/330 K "showed excellent agreement" with all-atom simulations at 300 K is not verifiable without the Rg distribution plots.
- The relevance of the simulations to disease-associated mutations (e.g., A90V in the NTD-RRM1 linker) is mentioned but not explored; this is a missed opportunity but not a claim that is unsupported.