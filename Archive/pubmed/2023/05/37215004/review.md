## Review setup
- **Input scope** Full manuscript text (abstract, results, discussion, methods) from bioRxiv preprint
- **Assessment boundary** Scientific content, methodology, claims, and evidence as presented in the provided text
- **Shared manuscript claim summary** The authors use coarse-grained molecular dynamics simulations (HPS and Martini models) to show that charge segregation in disordered proteins (model E-K sequences, LAF1 RGG, DDX4 N-terminal) monotonically alters condensate material properties (diffusion, viscosity, surface tension), that these changes correlate with contact dynamics between oppositely charged residues, and that single-chain conformations (radius of gyration) can predict condensate material properties.
- **Visible evidence base** Main text figures referenced (Figs. 1-5), supplementary figures (S1-S25), tables (S1-S5), methods section
- **Missing materials affecting confidence** Supplementary figures and tables not provided in the input; specific numerical values for material properties not fully detailed in main text; experimental comparison data only partially described

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question in the field of biomolecular condensates: how sequence features, specifically charge patterning, dictate material properties. The authors employ a combination of equilibrium and non-equilibrium simulations with two coarse-grained models to establish correlations between charge segregation, contact dynamics, and material properties. The finding that single-chain properties correlate strongly with condensate material properties is potentially significant and practically useful. However, the manuscript's central claims rest on correlations rather than mechanistic causation, and the quantitative comparison with experiments relies on a timescale mapping that requires careful scrutiny. The evidence presented is generally consistent with the claims, but several technical aspects need clarification to fully establish the case.
- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, intrinsically disordered proteins, and soft matter physics. The work provides computational predictions that could guide experimental design and engineering of condensates with tunable properties. The correlation between single-chain and condensed-phase properties is of broad interest to those studying sequence-to-function relationships in phase-separating systems.
- **Major strengths** 1) Systematic investigation of charge patterning effects across model and natural sequences. 2) Use of two independent coarse-grained models (HPS and Martini) to demonstrate robustness. 3) Quantitative comparison with experimental data for validation. 4) Identification of a practical predictor (single-chain Rg) for condensate material properties. 5) Clear presentation of results with logical progression from material properties to molecular mechanisms.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** 
- **Recommendation posture** Supportive if technical concerns are resolved

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "Our computations yield material properties that are quantitatively comparable with experimentally characterized condensate systems."
- **Evidence pointer** Figure 3b, Table S2, Table S4, Methods section "Connecting simulation and experimental timescales"
- **Concern** The timescale mapping strategy is central to the quantitative comparison with experiments, but the description in the Methods is insufficient to assess its validity. The authors derive timescales by matching single-chain diffusion coefficients to Stokes-Einstein predictions, then apply these timescales to interpret dense-phase dynamics. This assumes that the friction coefficient calibrated in dilute solution remains valid in the condensed phase, where crowding and intermolecular interactions could alter effective friction. The manuscript does not discuss potential limitations of this assumption or provide sensitivity analysis.
- **Why it matters** The quantitative agreement with experiments (e.g., viscosity values) is a key selling point of the manuscript. If the timescale mapping is flawed or model-dependent, the quantitative claims would be undermined, and the comparison with experiments would become qualitative at best.
- **Resolution test** Provide a detailed derivation of the timescale mapping, including error propagation. Show that the mapping is robust to reasonable variations in input parameters (e.g., hydrodynamic radius estimates, solvent viscosity). Compare dense-phase dynamics using timescales derived from alternative approaches (e.g., mapping based on experimental diffusion coefficients in dense phases, if available).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "We found a strong universal correlation between the lifetime of noncovalent bonds formed by the oppositely charged residues and the different material properties of all investigated sequences."
- **Evidence pointer** Figure 4c-e, Figure 5c-e, Methods section "Regarding the analysis of contact formation"
- **Concern** The manuscript reports power-law correlations between contact lifetimes and material properties (R² = 0.83-0.93) and between single-chain Rg and material properties (R² ≈ 0.96). However, the number of data points used to establish these correlations is not clearly stated. With only a limited number of sequences (approximately 5-7 per sequence family), high R² values can be achieved by chance, especially if the data span a wide range. The authors should report the number of data points, confidence intervals for the power-law exponents, and ideally perform a leave-one-out cross-validation to demonstrate predictive power.
- **Why it matters** The claim of "universal correlation" is strong and implies predictive utility. If the correlation is driven by a few outliers or is not robust to the inclusion of additional sequences, the practical value of the finding is diminished.
- **Resolution test** Report the number of sequences used in each correlation, provide confidence intervals for the fitted exponents, and perform cross-validation or bootstrap analysis to demonstrate that the correlations are statistically robust and predictive.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** "Condensed phase material properties and single-chain structural properties of charged disordered proteins are strongly correlated."
- **Evidence pointer** Figure 5, Figures S9-S11
- **Concern** The manuscript demonstrates a correlation between single-chain Rg and condensed-phase material properties, but the mechanistic basis for this correlation is not fully explored. The authors state that "molecular interactions within the condensate are highly similar to those within a single-chain," but this is based on comparing contact probabilities, which is a static measure. The dynamic nature of these contacts (e.g., lifetimes, rearrangement rates) in single chains versus dense phases is not compared. Without a mechanistic understanding, the correlation may be specific to the sequences studied and may not generalize to other sequence features (e.g., hydrophobic patterning, aromatic content).
- **Why it matters** The claim that single-chain properties can predict condensate material properties is potentially transformative for the field, as it would enable rapid screening of sequences. However, if the correlation is not mechanistically grounded, it may fail for sequences outside the training set, limiting its utility.
- **Resolution test** Provide additional analysis comparing the dynamics of contact formation/breakdown in single chains versus dense phases. Test the predictive power of the correlation on a held-out set of sequences with different compositions (e.g., sequences with hydrophobic residues, different chain lengths). Discuss the mechanistic basis for why single-chain conformations should reflect dense-phase dynamics.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction, Results section "Interfacial and dense phase properties"
- **Evidence pointer** Figure 3b
- **Issue** The comparison with experimental data in Figure 3b is presented as a scatter plot, but the experimental methods used for different data points are not clearly distinguished in the main text. The reader is referred to Table S4 for details, which is not provided in the input.
- **Required correction** Add a brief description in the main text of the experimental methods used for the comparison points (e.g., micropipette aspiration, viscocapillary model) and clearly indicate which points are direct measurements versus estimates.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, "Martini model and simulation details"
- **Evidence pointer** Methods section
- **Issue** The Martini simulations are described as using a slab geometry for equilibration, followed by cutting out the dense phase for production runs. The criteria for determining when the dense phase has reached equilibrium concentration are not stated.
- **Required correction** Specify the convergence criteria used to determine equilibrium dense-phase concentration and the method for identifying the dense-phase region for extraction.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, "Charge segregation in IDP sequences leads to monotonic changes"
- **Evidence pointer** Figure 2, Methods section
- **Issue** The normalization of D and η0 by reference sequences (E-K with nCD=0.017, WT for LAF1 and DDX4) is reasonable, but the choice of reference sequences is not justified. For LAF1 and DDX4, the WT sequences have different nCD values (0.010 and 0.021, respectively), which may complicate direct comparison of normalized values across sequence families.
- **Required correction** Provide a brief justification for the choice of reference sequences and discuss whether the normalization affects the interpretation of the master curve collapse.

## Risk / unsupported claims
- The claim of "quantitative comparability" with experiments (abstract, Results) is not fully supported without detailed error analysis of the timescale mapping.
- The "universal correlation" between contact dynamics and material properties is based on a limited number of sequences; the statistical robustness is not demonstrated.
- The predictive power of single-chain Rg for condensate material properties is claimed but not tested on independent sequences.
- The statement that "molecular interactions within the condensate are highly similar to those within a single-chain" is based on static contact probabilities; dynamic comparisons are not provided.
- The assumption that the viscocapillary model provides reasonable surface tension estimates for disordered protein condensates is discussed but not rigorously validated for all comparison points.