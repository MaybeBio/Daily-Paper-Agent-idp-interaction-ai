## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) without supplementary figures, tables, or movies.
- **Assessment boundary** Scientific claims, methodological soundness, and presentation quality based solely on the provided text. Supplementary materials referenced but not provided are noted as such.
- **Shared manuscript claim summary** The authors present an atomistic computational approach, combining FMAP-derived chemical potentials with Brownian dynamics simulations, to compute liquid-liquid phase separation binodals for two bovine γ-crystallins, γB and γF. They report a higher critical temperature for γF than γB, and identify a single amino acid substitution, S130W, as the dominant contributor to this difference, supported by residue-level energy decomposition, mutagenesis calculations, and structural analysis.
- **Visible evidence base** Main text figures (Figs. 1–7) are referenced but not provided. Methods section is complete. No supplementary data, tables, or movies were available for review.
- **Missing materials affecting confidence** All figures, supplementary figures, supplementary tables, and supplementary movies. These are essential for evaluating the quantitative accuracy of the binodals, the statistical significance of the energy decomposition, and the structural claims.

## Reviewer
- **Overall assessment** This manuscript presents a technically ambitious and potentially important advance in the atomistic modeling of protein liquid-liquid phase separation. The central claim, that a single S130W substitution explains the critical temperature difference between γB and γF, is well-motivated and supported by a multi-pronged computational analysis. However, the absence of all figures and supplementary materials prevents a full evaluation of the quantitative results, the robustness of the methodology, and the strength of the structural evidence. The underestimation of the absolute critical temperature for γF, acknowledged by the authors, is a significant concern that warrants further discussion and analysis.
- **Who would be interested in the results, and why** Researchers in the fields of protein phase separation, biophysics of eye lens proteins, and computational biophysics. The methodological advance (FMAPμ for chemical potentials in dense protein solutions) will be of interest to the computational biophysics community. The specific finding regarding S130W will interest those studying cataract formation and sequence determinants of phase behavior in structured proteins.
- **Major strengths**
    1.  The methodological combination of FMAPμ and Brownian dynamics is novel and addresses a critical gap in atomistic simulations of phase separation.
    2.  The study directly tackles a long-standing question about sequence determinants of critical temperature in γ-crystallins.
    3.  The multi-faceted approach, including energy decomposition, mutagenesis calculations, and structural analysis, provides converging evidence for the role of S130W.
    4.  The authors are transparent about the limitations of their model, particularly the underestimation of the absolute critical temperature.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness
    - **Claim pointer** The manuscript claims that the computed binodals and critical temperatures, particularly the difference between γB and γF, are quantitatively reliable and capture the experimentally observed behavior.
    - **Evidence pointer** Fig. 3c, 3f; Results section "Binodals determined from concentration dependence of chemical potential show higher Tc for γF than for γB"
    - **Concern** The computed critical temperature for γF is approximately 10 °C, while the experimental value is approximately 39 °C. The authors acknowledge this underestimation but do not provide a thorough analysis of its origin or its implications for the validity of the predicted binodals. A significant quantitative discrepancy of this magnitude suggests that the energy function or the simulation protocol may not be sufficiently accurate to make reliable quantitative predictions, even if the qualitative trend (γF > γB) is captured. The manuscript would be strengthened by a detailed discussion of the potential sources of this error (e.g., force field inaccuracies, neglect of protein flexibility, finite-size effects) and a sensitivity analysis showing how the binodals and Tc depend on the scaling parameters s1 and s2.
    - **Why it matters** The central claim of the paper is that atomistic modeling can explain the dependence of critical temperature on sequence. If the model cannot quantitatively reproduce the absolute critical temperature, its ability to quantitatively attribute the difference to a specific residue is weakened. The reader needs to understand the magnitude and source of this error to assess the reliability of the mechanistic conclusion.
    - **Resolution test** The authors should provide a detailed error analysis, including a discussion of the sensitivity of the computed Tc to the energy function parameters and simulation length. They should also compare their computed binodals more directly with experimental data, perhaps by scaling or normalizing the temperature axis, to demonstrate that the shape of the binodal is correctly predicted even if the absolute scale is off.
    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness
    - **Claim pointer** The manuscript claims that the residue-level decomposition of interaction energies identifies S130W as the "major contributor" to the difference in Tc between γB and γF.
    - **Evidence pointer** Fig. 5; Results section "Residue-level decomposition of pair interaction energy reveals the S130W substitution as the main cause for Tc difference"
    - **Concern** The analysis identifies six positions (128, 130, 84, 79, 127, 21) that contribute most to the lower interaction energy of γF. Five of these positions are identical between γB and γF, meaning their differential contribution must arise from changes in their interaction partners or the overall protein context. The manuscript attributes the difference to S130W, but it is not clear how the contributions of the other five positions are modulated by the S130W substitution. A more rigorous analysis would involve calculating the interaction energy of the S130W mutant in the γB background and the W130S mutant in the γF background, and then decomposing the energy difference to confirm that the effect is localized to position 130 and not a global change in interaction patterns.
    - **Why it matters** The claim that a single substitution is the "main cause" is a strong causal statement. The current analysis is largely correlative. Without a direct test of causality, such as the mutant binodals shown in Fig. 4b, the role of the other five positions remains ambiguous. The manuscript would be more convincing if it could show that the energy decomposition of the mutant binodals specifically isolates the change at position 130.
    - **Resolution test** The authors should perform a differential decomposition analysis, comparing the residue-resolved interaction energies of the γB S130W mutant to γB, and γF W130S to γF. This would directly show which residues' contributions change upon mutation and whether the change is localized to position 130.
    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical soundness
    - **Claim pointer** The manuscript claims that the structural analysis of low-energy pairs reveals that γF interactions "more preferentially involve Trp130" and that this is due to the bulky aromatic sidechain of tryptophan.
    - **Evidence pointer** Fig. 6; Results section "γB interactions are more isotropic whereas γF interactions more preferentially involve Trp130"
    - **Concern** The structural analysis is based on the lowest-energy configurations from the FMAPB2 calculations. The authors show that γF has a stronger tendency to form interfaces that bury Trp130. However, the manuscript does not provide a quantitative measure of the "preference" or a statistical test to show that the difference between γB and γF is significant. Furthermore, the claim that tryptophan's specific chemical properties (cation-π, etc.) are responsible is speculative, as the energy decomposition in Fig. 5 does not break down the contributions by interaction type.
    - **Why it matters** The structural analysis is used to provide a mechanistic explanation for the energetic findings. If the structural preference is not robustly quantified, the mechanistic explanation is weakened. The reader needs to know how many of the 1000 lowest-energy configurations show the Trp130-Trp130 interface, and whether this is a dominant or minor population.
    - **Resolution test** The authors should provide quantitative statistics on the frequency of Trp130-Trp130 interfaces in the low-energy ensembles for γF and γB, and compare these to the frequency of other types of interfaces. They should also perform a control analysis, such as mutating Trp130 to a different aromatic residue (e.g., Phe or Tyr) to see if the structural preference is specific to tryptophan.
- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity
    - **Affected element** Abstract
    - **Evidence pointer** Abstract
    - **Issue** The abstract states that the method "yielding the binodal and critic temperature (Tc)" but does not mention the significant underestimation of Tc for γF compared to experiment.
    - **Required correction** The abstract should be more balanced and mention the quantitative limitation of the model, e.g., "yielding binodals and critical temperatures that capture the correct trend but underestimate the absolute scale."
    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Reproducibility
    - **Affected element** Methods
    - **Evidence pointer** Methods section "Protein structure preparation"
    - **Issue** The manuscript states that the S130W mutation was modeled by "grafting the sidechain of Trp130 in γF after structure alignment using all backbone atoms." It is not clear if any additional optimization of the grafted sidechain was performed beyond a simple energy minimization of the two sidechains that clashed.
    - **Required Correction** Please provide more details on the mutation protocol, including whether the rest of the protein was allowed to relax, and if so, for how many steps.
    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Statistical analysis
    - **Affected element** Results, Fig. 7
    - **Evidence pointer** Results section "High-Tc γ-crystallins collectively have more negative virial coefficients than low-Tc γ-crystallins"
    - **Issue** The comparison of B2 values between the low-Tc and high-Tc groups is based on a small number of structures (10 vs 5). The p-value from the unpaired t-test is reported, but it is not clear if the data meet the assumptions of the test (e.g., normality).
    - **Required Correction** Please consider using a non-parametric test (e.g., Mann-Whitney U test) or clearly state that the data are normally distributed.
- **Technical failings that need to be addressed before the case is established**
    - R1-M1: The significant underestimation of the absolute critical temperature for γF needs a thorough analysis and discussion.
    - R1-M2: The causal role of S130W needs to be more directly demonstrated through differential decomposition analysis of the mutant proteins.
- **Assessment against Nature-style criteria**
    - **Originality** High. The application of FMAPμ to compute chemical potentials in dense protein solutions for phase equilibrium is a novel methodological contribution.
    - **Scientific importance** High. The work addresses a fundamental question in the field of protein phase separation and provides a potential pathway for predicting the effects of mutations on phase behavior.
    - **Interdisciplinary readership** Moderate. The work will be of primary interest to biophysicists and computational biologists. The specific biological context (cataract) may broaden its appeal.
    - **Technical soundness** Moderate. The methodology is sophisticated, but the quantitative accuracy is a concern, and the causal analysis needs strengthening.
    - **Readability for nonspecialists** Good. The manuscript is generally well-written and the logic is clear, although the methods section is dense.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising and the qualitative findings are likely correct, but the quantitative limitations and the need for a more direct causal analysis must be addressed before the claims are fully established.

## Risk / unsupported claims
- The claim that the S130W substitution is the "main cause" for the Tc difference is not fully supported by the provided evidence, as the analysis is correlative and does not rule out contributions from other positions.
- The claim that the structural analysis reveals a "much stronger preference" for Trp130 to be an interaction site is not quantitatively supported.
- The generalizability of the findings to other γ-crystallins, while suggested by the B2 analysis, is not fully established without a more detailed sequence-structure-energy analysis.
- The accuracy of the computed binodals and Tc values cannot be fully assessed without the figures.