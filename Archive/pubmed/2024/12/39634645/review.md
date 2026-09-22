## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion) for the article "Amino Acid Residue-Specific Ramachandran Distributions Derived from a Simple Mean Field Potential" by Andrews, published in ACS Physical Chemistry Au (2024).
- **Assessment boundary** Scientific content, methodological soundness, validity of claims, and alignment with Nature-style criteria. Editorial or formatting issues are not assessed.
- **Shared manuscript claim summary** The author proposes that residue-specific Ramachandran distributions for alanine, valine, leucine, and isoleucine in the unfolded state can be derived from a simple mean field potential combining average intrapeptide Lennard-Jones interactions and an empirical peptide backbone–water term, without dihedral-specific energy terms. The work claims that unique conformational preferences arise from competition between backbone–water stabilization of pPII and repulsive side chain–backbone interactions.
- **Visible evidence base** Full text including methods, results (Figures 1–5 referenced), supplementary tables (S1–S5) and figures (S1–S5) mentioned but not provided, and comparison to experimental NMR coupling constants from prior work.
- **Missing materials affecting confidence** Supplementary figures and tables (S1–S5) are referenced but not included in the provided material. Raw data and scripts are stated to be on GitHub but not accessible in this review. Experimental data used for comparison (from refs 16, 19, 30) are not reproduced. This limits full verification of quantitative claims.

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting and computationally simple approach to understanding residue-specific conformational preferences in unfolded proteins. The idea of averaging over side chain torsions to create a mean field is novel and potentially valuable. However, the current evidence base is insufficient to fully establish the claims. The model's qualitative agreement with experiments is acknowledged by the author, but quantitative reproduction of NMR data is poor, and the hyperparameter λ is tuned without clear physical justification. The work is at an early stage and would benefit from additional validation and refinement before the case is fully established.
- **Who would be interested in the results, and why** Researchers in protein folding, intrinsically disordered proteins, and computational biophysics would find this work relevant. The simple mean field approach could offer a computationally efficient alternative to full MD simulations for exploring backbone conformational preferences. Those interested in force field development and the physical origins of Ramachandran distributions may also find the conceptual framework useful.
- **Major strengths** (1) The conceptual simplicity of the model is appealing, reducing complex interactions to a few key terms. (2) The systematic exploration of λ as a hyperparameter shows awareness of model sensitivity. (3) The comparison to multiple experimental and computational datasets (NMR, Gaussian model, CHARMM36m) is a strength, even if agreement is qualitative. (4) The work addresses an important gap in understanding the physical mechanisms behind residue-specific conformational preferences.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (λ sensitivity and arbitrariness), R1-M2 (quantitative agreement with experiments), R1-M3 (omission of electrostatics and vibrational degrees of freedom), R1-M4 (lack of validation against full MD or experimental ensembles).
- **Assessment against Nature-style criteria** Originality: The mean field approach is a novel contribution, though it builds on prior work by Zhou et al. and Schweitzer-Stenner. Scientific importance: The question of what drives residue-specific conformational preferences is important, but the current model's limited quantitative accuracy reduces its immediate impact. Interdisciplinary readership: The work is primarily of interest to computational biophysicists and protein chemists; broader appeal is limited by the technical nature and preliminary results. Technical soundness: The methodology is generally sound but has notable limitations, including the arbitrary λ selection and omission of key physical interactions. Readability for nonspecialists: The manuscript is clearly written and accessible, with good context provided in the introduction, though the methods section assumes familiarity with computational techniques.
- **Recommendation posture** Supportive if technical concerns are resolved. The conceptual framework is promising, but the current evidence does not fully establish the claims. Additional validation, better quantitative agreement, and clearer justification of model choices are needed.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that the mean field model produces residue-specific Ramachandran distributions qualitatively consistent with experimental predictions, with λ as a tunable hyperparameter.
- **Evidence pointer** Methods section "Generating the Mean Fields", Results section "Amino Acid Residue-Specific Ramachandran Distributions", Figure 3
- **Concern** The hyperparameter λ, which controls the cutoff for excluding high-energy structures, is varied across a wide range (0.70 to 1.00) with different optimal values for different residues (e.g., 0.90 for valine and leucine, 0.75 for isoleucine). The choice of λ appears arbitrary and is not justified by physical principles or independent data. This raises concerns about overfitting and the predictive power of the model. The author acknowledges this issue in the Discussion but does not provide a resolution strategy.
- **Why it matters** If the model's predictions depend critically on an arbitrarily chosen parameter, the conclusions about the physical origins of conformational preferences are weakened. A robust model should have parameters that are either physically motivated or consistently determined across residues.
- **Resolution test** The author should provide a physical justification for λ or demonstrate that the qualitative conclusions are robust across a wider range of λ values. Alternatively, λ could be determined by fitting to a training set of experimental data and then tested on held-out residues.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The manuscript claims that the derived Ramachandran distributions can be compared to experimental NMR coupling constants, implying quantitative utility.
- **Evidence pointer** Results section "Ramachandran Distributions Share Qualitative Properties", Figure 4, Tables S4 and S5
- **Concern** The calculated NMR coupling constants deviate significantly from experimental values for most residues and λ choices. For alanine, the deviation is acknowledged as significant. For valine, leucine, and isoleucine, the agreement is mixed and often poor. The author states that "additional model refinement will be done before comparing to additional experimental measures," which suggests the current model is not yet quantitatively reliable.
- **Why it matters** The scientific value of the model depends on its ability to reproduce or predict experimental observables. If quantitative agreement is poor, the model's utility as a predictive tool is limited, and the claims about understanding physical mechanisms are weakened.
- **Resolution test** The author should either improve the model to achieve better quantitative agreement with NMR data or clearly state the limitations and reframe the claims as purely qualitative. Additional experimental observables (e.g., J-coupling constants for other residues, or circular dichroism spectra) could be used for validation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that the mean field potential, consisting of only backbone–water and average intrapeptide Lennard-Jones contributions, is sufficient to explain residue-specific conformational preferences.
- **Evidence pointer** Methods section "Generating the Mean Fields", Discussion section
- **Concern** The model omits electrostatics, partial charges, and explicit vibrational degrees of freedom. While the author justifies these omissions for simplicity, the Discussion acknowledges that vibrational degrees of freedom "will likely substantially contribute to the conformational preferences." This undermines the claim that the simple model captures the essential physics. The omission of electrostatics is particularly concerning for residues with polar or charged side chains, though the chosen residues (A, V, L, I) are nonpolar.
- **Why it matters** If key physical interactions are omitted, the model's ability to explain the mechanisms driving conformational preferences is incomplete. The conclusions may not generalize to other residues or conditions.
- **Resolution test** The author should either include additional terms (e.g., electrostatics) in future iterations or clearly delineate the scope of the model's applicability. Sensitivity analyses showing the impact of omitted terms would strengthen the claims.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that the mean field approach can produce Ramachandran distributions comparable to those from MD simulations and experimental data.
- **Evidence pointer** Results section "Ramachandran Distributions Share Qualitative Properties", Figure 5
- **Concern** The comparison to MD-derived distributions (CHARMM36m) and the Gaussian model is qualitative, and the author notes that the mean field distributions are much narrower. This suggests the model does not capture the full conformational flexibility or dynamics of the system. The lack of dynamical information is a fundamental limitation, as the model only characterizes minima of the energy landscape.
- **Why it matters** Conformational preferences in unfolded proteins are influenced by entropic and dynamic effects, which the current model does not capture. The narrow distributions may lead to incorrect predictions of ensemble-averaged properties.
- **Resolution test** The author should compare the model's predictions to more comprehensive experimental data (e.g., ensemble FRET, SAXS) or MD simulations that capture dynamics. If the model is intended only for identifying energy minima, this should be clearly stated.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and reproducibility
- **Affected element** Methods section "Generating the Mean Fields"
- **Evidence pointer** Location not provided
- **Issue** The description of the normalization factor for the average number of atomic overlaps is incomplete. The formula is not fully specified, and the text says "normalized by a factor of where Nχ is the number of side chain torsional angles" but the actual expression is missing.
- **Required correction** Provide the complete formula for the normalization factor and clarify how the averaging is performed.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Interpretation of results
- **Affected element** Results section "Atomic Overlaps in Ramachandran Space Are Unique to Each Amino Acid Residue Mimetic"
- **Evidence pointer** Figure 2
- **Issue** The discussion of differences between residues (e.g., valine vs. isoleucine) is somewhat descriptive and could benefit from a more systematic analysis of which specific atomic interactions drive the observed differences.
- **Required correction** Consider adding a quantitative analysis of the contributions of specific atom pairs to the overlap distributions.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Comparison to literature
- **Affected element** Discussion section
- **Evidence pointer** Location not provided
- **Issue** The Discussion mentions that the model's results are "qualitatively consistent" with prior work, but the specific points of agreement and disagreement are not systematically enumerated.
- **Required correction** Provide a more detailed comparison table or list of qualitative features (e.g., pPII preference, β-region location) for each residue across methods.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Future directions
- **Affected element** Discussion section
- **Evidence pointer** Location not provided
- **Issue** The Discussion lists several limitations and future directions but does not prioritize them or provide a clear roadmap for how the model will be improved.
- **Required correction** Suggest a prioritized list of improvements (e.g., adding electrostatics, including vibrational averaging, testing on more residues) with expected impacts.

## Risk / unsupported claims
- The claim that the mean field model "provides evidence" for the direct attribution of conformational preferences to competition between backbone–water and side chain–backbone interactions is not fully supported, as the model omits several potentially important interactions and the quantitative agreement with experiments is poor.
- The claim that the model produces distributions "qualitatively consistent" with experimental predictions is supported only for certain features and residues; the degree of consistency varies and is not systematically quantified.
- The choice of λ values for each residue is not justified, and the sensitivity of conclusions to this choice is not fully explored.
- The comparison to MD simulations (CHARMM36m) is limited to a single force field, and the generalizability of the comparison is unclear.
- The manuscript states that "additional model refinement will be done before comparing to additional experimental measures," which implies the current results are preliminary and not yet fully validated.