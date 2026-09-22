## Review setup
- **Input scope** Full manuscript text (preprint, bioRxiv 2023.05.10, DOI 10.1101/2023.04.25.538329)
- **Assessment boundary** Scientific content, methodology, claims, and evidence as presented in the provided text. No external validation or replication was performed.
- **Shared manuscript claim summary** The authors present an atomistic computational approach combining FFT-based chemical potential calculations (FMAPμ) with Brownian dynamics simulations to compute liquid-liquid phase separation binodals for bovine γ-crystallins γB and γF. They report a higher critical temperature (Tc) for γF (~10 °C) than γB (~4 °C), and identify a single amino acid substitution, Ser130Trp, as the major contributor to this difference. The claim is supported by residue-level energy decomposition, mutagenesis simulations, and virial coefficient analysis across 16 γ-crystallin structures.
- **Visible evidence base** Figures 1–6 (described in text), Supplementary Figures S1–S8, Supplementary Movies S1–S2, computational methods section, and references to prior experimental data (Thomson et al., Bucciarelli et al.).
- **Missing materials affecting confidence** Actual figure images, numerical data tables, simulation trajectory details, convergence criteria, error bars on binodal points, and the full set of PDB identifiers for the 14 additional structures. The manuscript is a preprint and has not undergone peer review.

## Reviewer
- **Overall assessment** This manuscript presents a technically ambitious and potentially significant advance in atomistic modeling of liquid-liquid phase separation for globular proteins. The methodological combination of FMAPμ with Brownian dynamics is novel and addresses a known limitation of coarse-grained models. The identification of Ser130Trp as a key determinant of Tc differences is plausible and well-supported by multiple independent analyses. However, several technical concerns regarding the accuracy of the energy function, the treatment of protein flexibility, and the quantitative agreement with experimental Tc values need to be addressed before the central claims can be fully accepted.
- **Who would be interested in the results, and why** Researchers in the fields of protein phase separation, biophysics of eye lens proteins, computational chemistry, and protein engineering. The work provides a framework for linking amino acid sequence to phase behavior in structured proteins, which is relevant for understanding cataract formation and for designing proteins with tunable phase separation properties.
- **Major strengths** 1) The methodological advance of combining FMAPμ with BD simulations for atomistic binodal determination is significant and addresses a long-standing computational challenge. 2) The multi-pronged approach (binodals, virial coefficients, residue decomposition, mutagenesis, Grantham distance analysis) provides converging evidence for the Ser130Trp claim. 3) The validation against experimental binodal data for γB adds credibility. 4) The work addresses a question posed nearly 40 years ago, providing a satisfying resolution.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (energy function accuracy), R1-M2 (flexibility treatment), R1-M3 (quantitative Tc agreement), R1-M4 (statistical robustness of decomposition).
- **Assessment against Nature-style criteria** **Originality**: High. The combination of FMAPμ with BD for atomistic binodal determination is novel, and the identification of a single residue as the dominant determinant of Tc in a globular protein is a new finding. **Scientific importance**: High. The work addresses a fundamental question in protein phase separation and provides a computational tool with broad applicability. **Interdisciplinary readership**: Moderate to high. The topic bridges biophysics, computational chemistry, and cell biology, but the technical density may limit accessibility to a general audience. **Technical soundness**: Generally sound but with concerns as detailed below. The methodology is well-described and the authors have made efforts to validate against experimental data. **Readability for nonspecialists**: The abstract and introduction are accessible, but the methods and results sections are highly technical. The authors could improve accessibility with more intuitive explanations of key concepts.
- **Recommendation posture** Supportive if technical concerns are resolved. The central claim regarding Ser130Trp is well-supported by converging evidence, but the quantitative accuracy of the computed Tc values and the robustness of the energy decomposition need further validation.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that their atomistic model, using a specific energy function with scaling parameters s1=0.16 and s2=1.6, accurately captures inter-protein interactions in dense protein solutions.
- **Evidence pointer** Computational Methods, Eqs [4]–[7]; Results section "FFT-based method, FMAPμ, enables calculation of the chemical potentials of γ-crystallins"
- **Concern** The energy function relies on two empirical scaling parameters (s1 and s2) that were previously fitted. The sensitivity of the computed binodals and Tc values to these parameters is not systematically explored. If the results are highly sensitive to these parameters, the predictive power of the method is questionable.
- **Why it matters** The central quantitative claims (Tc values, energy decomposition) depend entirely on the accuracy of the interaction energy function. Without a sensitivity analysis, it is unclear whether the identified Ser130Trp effect is robust or an artifact of the specific parameter choice.
- **Resolution test** Provide a sensitivity analysis varying s1 and s2 over a reasonable range and show that the qualitative conclusions (γF > γB Tc, Ser130Trp dominance) are preserved. Alternatively, validate the energy function against additional experimental data (e.g., osmotic second virial coefficients for mutants).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors treat proteins as rigid bodies in their simulations, stating "If we treat each protein molecule as rigid" (Results, Eq [3] context).
- **Evidence pointer** Results section "FFT-based method, FMAPμ, enables calculation of the chemical potentials of γ-crystallins"; Computational Methods "Brownian dynamics (BD) simulations"
- **Concern** The rigid-body assumption ignores conformational flexibility, which is known to be important for protein-protein interactions, especially for surface residues. The authors acknowledge this limitation in the Discussion but do not assess its impact on their conclusions. The Ser130Trp substitution could potentially affect local flexibility, which would be missed in this treatment.
- **Why it matters** If conformational changes contribute significantly to the Tc difference, the identification of Ser130Trp as the "main cause" would be incomplete or potentially incorrect.
- **Resolution test** Perform additional simulations with limited flexibility (e.g., using an ensemble of conformers from molecular dynamics) for γB and γF to test whether the Tc difference and Ser130Trp dominance are maintained.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative accuracy
- **Claim pointer** The computed Tc for γF is ~10 °C, which "significantly underestimates the experimental value of ~39 °C" (Results, "Binodals determined from concentration dependence of chemical potential show higher Tc for γF than for γB").
- **Evidence pointer** Results section, Figure 3F
- **Concern** The computed Tc for γF is off by ~29 °C from experiment. While the authors acknowledge this, the magnitude of the discrepancy raises questions about the quantitative reliability of the method. The agreement for γB (~4 °C computed vs. experimental <10 °C) is better but still not precise. The claim that the method "explains" the dependence of Tc on sequence is weakened by this quantitative failure.
- **Why it matters** The title claims the modeling "explains" the dependence of Tc on sequence. If the absolute Tc values are inaccurate, the explanation is only qualitative. For a Nature-level claim, quantitative accuracy is expected.
- **Resolution test** Improve the energy function or simulation protocol to achieve closer agreement with experimental Tc values. Alternatively, provide a clear physical explanation for the systematic underestimation and demonstrate that the relative Tc differences are robust.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Statistical robustness
- **Claim pointer** The residue-specific decomposition of pair interaction energies identifies positions 128, 130, 84, 79, 127, and 21 as the greatest contributors to the Tc difference, with Ser130Trp being the only substitution among them.
- **Evidence pointer** Results section "Residue-specific decomposition of pair interaction energy reveals the S130W substitution as the main cause for Tc difference", Figure 5
- **Concern** The decomposition is based on the 1,000 lowest-energy configurations from FMAPB2 calculations. The statistical significance of the differences at each position is not assessed. It is unclear whether the ranking of contributions is stable across different numbers of configurations or different energy thresholds.
- **Why it matters** The central claim of the paper rests on this decomposition. If the ranking is not statistically robust, the identification of Ser130Trp as the "main cause" could be coincidental.
- **Resolution test** Provide error bars or confidence intervals for the residue-specific contributions, e.g., by bootstrapping over configurations or varying the number of configurations included.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 3C
- **Evidence pointer** Results section "Binodals determined from concentration dependence of chemical potential show higher Tc for γF than for γB"
- **Issue** The comparison between computed and experimental binodals for γB is described as "match well," but the experimental Tc is reported as <10 °C while the computed value is ~4 °C. The visual comparison in Figure 3C is not available to the reviewer.
- **Required correction** Provide a quantitative measure of agreement (e.g., root-mean-square deviation) between computed and experimental binodals, and clarify the experimental Tc value for γB.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion section
- **Evidence pointer** Discussion, paragraph on flexibility
- **Issue** The authors mention "using a precomputed library of protein structures in simulations" as a future direction but do not discuss the potential impact of flexibility on their current conclusions.
- **Required correction** Add a brief statement in the Discussion assessing the likely impact of flexibility on the Ser130Trp finding, even if qualitative.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Computational Methods, "FMAPB2 calculations and related analyses"
- **Evidence pointer** Computational Methods section
- **Issue** The clustering of low-energy configurations uses a ligand-RMSD cutoff of 10 Å, which is quite large. The sensitivity of the cluster analysis to this cutoff is not discussed.
- **Required correction** Justify the choice of 10 Å or show that the results are insensitive to reasonable variations in this parameter.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states the method "yielding the binodal and critic temperature Tc" but does not mention the quantitative discrepancy with experimental Tc for γF.
- **Required correction** Consider adding a caveat about the quantitative accuracy of Tc predictions in the abstract to avoid overstating the agreement.

## Risk / unsupported claims
- The claim that Ser130Trp is the "main cause" of the Tc difference is supported by the decomposition analysis, but the statistical robustness of this decomposition is not established (R1-M4).
- The quantitative Tc values, particularly for γF, are significantly underestimated compared to experiment, which limits the strength of the claim that the modeling "explains" the dependence of Tc on sequence (R1-M3).
- The rigid-body assumption is a known limitation that could affect the conclusions, but its impact is not assessed (R1-M2).
- The claim that the approach "opens the possibility for designing mutations to alter phase equilibrium" is plausible but not directly demonstrated; only two mutants were tested in silico.
- The statement that "the division of the bovine γ-crystallins into two groups on the basis of the tryptophan fluorescence coincides with the division into two groups on the basis of phase separation behaviour" is attributed to a prior work and is not independently verified here.