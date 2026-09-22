## Review setup
- **Input scope** Full manuscript text (Abstract, Introduction, Results, Conclusions, Materials and Methods) without figures, tables, or supplementary material
- **Assessment boundary** Scientific claims, methodological soundness, and internal consistency based solely on the provided text; figures, tables, and supplementary data referenced but not available for verification
- **Shared manuscript claim summary** The authors propose that site-specific methionine oxidation differentially affects the structure and phase separation of the TDP-43 C-terminal domain, with oxidation of conserved region methionines disrupting helical structure and helix-helix interactions, while oxidation of IDR methionines disrupts long-range contacts, both contributing to impaired phase separation through distinct mechanisms
- **Visible evidence base** NMR spectroscopy (chemical shift perturbations, secondary chemical shifts, 15N relaxation), DIC microscopy, mass spectrometry, and all-atom MD simulations of monomeric CTD variants and CR dimers
- **Missing materials affecting confidence** All figures, tables, and supplementary figures; experimental replicates and statistical details; raw NMR assignments and spectra; simulation convergence metrics beyond Rg autocorrelation; force field validation details; AlphaFold model confidence scores

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question regarding the molecular mechanisms by which methionine oxidation impairs TDP-43 phase separation, a process relevant to ALS and other neurodegenerative diseases. The combination of NMR spectroscopy and all-atom MD simulations is appropriate and potentially powerful. However, the current text presents several concerns that must be addressed before the conclusions can be considered fully established. The claim that oxidation of CR methionines disrupts helical structure is supported by secondary chemical shift analysis, but the quantitative extent of helicity loss and its direct causal link to impaired phase separation require stronger evidence. The simulation results are suggestive but limited by force field accuracy for disordered proteins and the absence of direct validation against experimental observables beyond qualitative trends. The distinction between CR and IDR methionine oxidation mechanisms is conceptually appealing but rests on indirect comparisons across different variants and simulation conditions. The manuscript would benefit from clearer presentation of quantitative data, explicit statistical treatment, and a more cautious interpretation of simulation-derived mechanistic insights.

- **Who would be interested in the results, and why** Researchers studying TDP-43 biology, liquid-liquid phase separation, protein oxidation and redox regulation, and the molecular basis of ALS and frontotemporal dementia. The work may also interest computational biophysicists developing and applying MD simulations to disordered proteins and those studying post-translational modification effects on protein conformation and interactions.

- **Major strengths** The study addresses a clinically relevant question with a combination of experimental and computational approaches. The use of NMR to demonstrate complete oxidation of all methionines and to map residue-specific structural changes is rigorous. The design of variants to separate CR versus IDR methionine contributions is thoughtful. The simulation work extends beyond simple observation to propose mechanistic explanations for the experimental findings.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency for causal mechanism
- **Claim pointer** The authors claim that oxidation of CR methionines disrupts helical structure and directly impairs intermolecular helical association, while oxidation of IDR methionines disrupts long-range contacts, and that both contribute to impaired phase separation through different mechanisms
- **Evidence pointer** Results sections "Methionine oxidation of CTD disrupts phase separation and reduces CR helicity" and "Oxidation of methionine impairs phase separation regardless of position but disrupts CR helicity only upon CR oxidation"; Figures 2, 4, 5 (not visible)
- **Concern** The central mechanistic claim relies on comparing the behavior of sequence variants (5M→AIDR and 5M→ACR+5M→AIDR) with the fully oxidized wild-type. However, the text does not provide quantitative data on the extent of helicity loss in the CR for each variant, nor does it demonstrate that the observed differences in phase separation behavior are specifically due to the location of oxidized methionines rather than to other sequence changes. The statement that "oxidation disrupts Met interactions not only in the structured CR but also in the unstructured CR-flanking regions" is presented as a conclusion, but the supporting data are not shown in the text. The causal link between helicity loss and impaired phase separation is asserted but not quantitatively established; for example, the authors do not show a correlation between residual helicity and saturation concentration across variants.
- **Why it matters** The central claim of the paper is that methionine oxidation impairs phase separation through two distinct, region-specific mechanisms. If the quantitative relationship between helicity loss, interaction disruption, and phase separation is not established, the mechanistic distinction between CR and IDR oxidation becomes speculative. This distinction is the primary novel contribution of the work.
- **Resolution test** Provide quantitative helicity values (e.g., fraction helical from secondary chemical shifts) for WT, CTDox, and each variant before and after oxidation. Show that the extent of helicity loss correlates with the degree of phase separation impairment across variants. Demonstrate that IDR oxidation alone (in the 5M→ACR+5M→AIDR variant) does not affect CR helicity but still impairs phase separation, with quantitative comparison to the CR-oxidized variant.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Simulation validity and interpretability
- **Claim pointer** The authors use all-atom MD simulations to conclude that oxidation causes conformational expansion of the CTD monomer and disrupts interactions involving polar, aliphatic, and aromatic residues, and that CR oxidation causes rapid dimer dissociation
- **Evidence pointer** Results sections "Methionine oxidation promotes expansion of the CTD monomer and disrupts interactions involving polar, aliphatic, and aromatic residues" and "Effect of position-specific oxidation on secondary structure, conformations, and CTD self-association"; Figures 3, 5, S2-S18 (not visible)
- **Concern** The simulation methodology raises several concerns. First, the Amber99sb-stq force field and TIP4P/2005s water model are not widely validated for disordered proteins, and the authors do not compare their simulation results to experimental observables (e.g., chemical shifts, SAXS profiles) to establish force field accuracy. Second, the use of only three replicas of 5 microseconds each for a 148-residue disordered protein may be insufficient for converged sampling of the conformational ensemble, despite the reported Rg autocorrelation times. Third, the dimer simulations are only 250 ns, which is short for assessing dimer stability, and the claim of "rapid dissociation" is based on qualitative observation rather than quantitative metrics. Fourth, the choice to exclude M414 from oxidation in simulations due to parameter availability introduces an inconsistency with the experimental system where all methionines are oxidized. Finally, the authors state that "disruption of long-range interactions in repetitive IDRs like those in TDP-43 CTD also correlates with disruption of homotypic phase separation," but this correlation is cited from prior work and not directly validated here.
- **Why it matters** The simulation results are used to provide mechanistic explanations for the experimental observations. If the simulations are not demonstrably accurate or converged, the proposed mechanisms remain speculative. The inconsistency in oxidation state between simulations and experiments could affect the conclusions, particularly if M414 plays a role in interactions.
- **Resolution test** Validate the force field by comparing simulated ensembles to experimental data (e.g., predicted chemical shifts from simulations versus measured values, or SAXS profiles). Provide convergence metrics beyond Rg autocorrelation, such as block error analysis or comparison of independent replicas. Extend dimer simulations or provide quantitative dissociation metrics. Address the M414 issue by either obtaining parameters or justifying its exclusion. If possible, simulate the exact experimental oxidation state.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative rigor and statistical treatment
- **Claim pointer** The authors state that oxidation "significantly disrupts helical structure and impairs phase separation" and that "both variants displayed a complete loss of phase separation" upon oxidation
- **Evidence pointer** Results sections "Methionine oxidation of CTD disrupts phase separation and reduces CR helicity" and "Oxidation of methionine impairs phase separation regardless of position but disrupts CR helicity only upon CR oxidation"; Figures 1, 2, 4 (not visible)
- **Concern** The text lacks quantitative details and statistical analysis. For example, the extent of chemical shift perturbations is described qualitatively ("large CSPs", "much weaker CSPs") without numerical thresholds or significance testing. The claim of "complete loss of phase separation" is not accompanied by quantitative measurements (e.g., turbidity, droplet counts, saturation concentrations) or statistical comparison to the unoxidized control. The secondary chemical shift analysis (Figure 2C-D) is described qualitatively ("strong positive value", "shift in position closer to those of a random coil") without reporting the actual values or the number of residues analyzed. The R2 relaxation data (Figure S8C) are described as showing "a difference" without statistical testing.
- **Why it matters** The conclusions depend on the magnitude and significance of the observed effects. Without quantitative data and statistical analysis, it is not possible to assess the robustness of the findings or compare them to previous studies. This is particularly important given the conflicting results in the literature cited by the authors.
- **Resolution test** Report numerical values for CSPs with defined significance thresholds. Provide quantitative phase separation measurements (e.g., saturation concentrations, droplet size distributions) with replicates and statistical tests. Report secondary chemical shift values with uncertainties. Perform statistical comparison of R2 values between conditions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of variant-based conclusions
- **Claim pointer** The authors conclude that "oxidation of methionines in both regions contributes to impaired phase separation, albeit through different mechanisms" based on experiments with variants where methionines are replaced with alanines
- **Evidence pointer** Results section "Oxidation of methionine impairs phase separation regardless of position but disrupts CR helicity only upon CR oxidation"; Figures 4, S8 (not visible)
- **Concern** The variants 5M→AIDR and 5M→ACR+5M→AIDR replace methionines with alanines, which is not equivalent to oxidation. Alanine substitution removes the sulfur atom entirely and changes the side chain size and hydrophobicity differently than oxidation to sulfoxide. The authors previously showed that alanine substitution itself impairs phase separation (reference 54), so the interpretation that the observed effects in the oxidized variants are due to oxidation of the remaining methionines is confounded by the alanine substitutions. The authors acknowledge this design limitation but do not fully address how the alanine substitutions might interact with the oxidation effects.
- **Why it matters** The conclusion that oxidation of IDR methionines alone impairs phase separation is based on the 5M→ACR+5M→AIDR variant, which has alanines in the CR. If the alanine substitutions in the CR already impair phase separation, the additional effect of IDR oxidation may be difficult to isolate. The mechanistic distinction between CR and IDR oxidation may be an artifact of the variant design.
- **Resolution test** Discuss explicitly how the alanine substitutions might affect the interpretation. If possible, use alternative approaches such as selective oxidation of specific methionines (e.g., using methionine analogs or enzymatic oxidation) or compare the oxidized variants to their unoxidized counterparts to isolate the oxidation effect. Alternatively, use computational models to predict the effect of oxidation versus alanine substitution on the same positions.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of writing
- **Affected element** Results section "Methionine oxidation of CTD disrupts phase separation and reduces CR helicity"
- **Evidence pointer** "DIC microscopy revealed that the while the unmodified CTD readily undergoes phase separation in the presence of NaCl, oxidation of Met residues results in the CTD losing the ability to undergo phase separation under the same conditions"
- **Issue** The phrase "the while" appears to be a typographical error and should read "while".
- **Required correction** Correct the typographical error.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Materials and Methods, NMR sample preparation
- **Evidence pointer** "NMR samples, were prepared by dilution of 2 mM protein stocks to the desired concentration with 20 mM MES pH 6.1 with 5.23% added 2H2O with 5% 2H2O (for NMR locking) sample buffer"
- **Issue** The sentence contains redundant and confusing information about 2H2O concentration. It states "5.23% added 2H2O" and then "with 5% 2H2O (for NMR locking)" which is unclear. The final concentration is stated as 5% 2H2O, but the initial 5.23% is not explained.
- **Required correction** Clarify the 2H2O concentration and the preparation procedure. Remove redundant or contradictory information.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Materials and Methods, MD simulations
- **Evidence pointer** "The structures were prepared for simulations in GROMACS 2021 using the Amber99sb-stq force field and the TIP4P/2005s water model"
- **Issue** The choice of force field and water model is unusual for disordered proteins, and no justification is provided. Additionally, the authors do not state the temperature and pressure coupling details, the equilibration protocol for the dimer simulations, or the criteria for determining simulation convergence.
- **Required correction** Provide justification for the force field and water model choice. Include details on temperature and pressure coupling, equilibration, and convergence criteria.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Referencing
- **Affected element** Introduction
- **Evidence pointer** "These biomolecular condensates form via phase separation, where proteins, nucleic acids, and other molecules spontaneously de-mix into concentrated liquid droplets through weak, multivalent interactions2–5."
- **Issue** The reference list is not provided in the manuscript text, so it is not possible to verify the appropriateness of the citations. This is a general issue for all citations.
- **Required correction** Ensure all references are complete and appropriate. This is a formatting issue that will be resolved in the final version.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Figure accessibility
- **Affected element** All figures
- **Evidence pointer** Figures 1-6, S1-S18 (not visible)
- **Issue** The figures are not available for review. Given the central role of figures in supporting the claims, the inability to assess them limits the evaluation.
- **Required correction** Provide figures and supplementary material for review.

## Risk / unsupported claims
- The claim that "oxidation of methionines in both regions contributes to impaired phase separation, albeit through different mechanisms" is not fully supported by the provided text, as the quantitative data and statistical analysis are not presented.
- The claim that "oxidation of CR methionines disrupts helical structure and directly impairs intermolecular helical association" is supported by secondary chemical shift data but the quantitative extent and causal link to phase separation are not established.
- The claim that "oxidation of IDR methionines disrupts long-range contacts" is based on simulation data that are not validated against experimental observables.
- The claim that "all methionine residues are vulnerable to oxidation" is supported by mass spectrometry data, but the text does not provide the mass spectrometry results or the extent of oxidation at each site.
- The simulation-based conclusion that "oxidation of Met residues, whether in CR or IDR, significantly disrupted long-range interactions between N- and C-terminal domains" is not directly validated by experimental data.
- The statement that "these findings establish methionines as critical redox-sensitive modulators of TDP-43 phase behavior" is an overstatement given the limitations described above; the findings suggest a role but do not establish criticality without further evidence.