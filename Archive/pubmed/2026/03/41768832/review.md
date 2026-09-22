## Review setup
- **Input scope** Full manuscript text (abstract, introduction, theory, simulation results, discussion, conclusions) as provided by the user. No figures, tables, or supplementary information were included in the supplied material.
- **Assessment boundary** The review is limited to the scientific content, logical consistency, and evidentiary support of the claims as presented in the text. No assessment of formatting, citation accuracy, or literature completeness beyond what is visible in the text is attempted.
- **Shared manuscript claim summary** The authors present a scaling theory for single-chain conformations of charge-imbalanced polyampholytes with Markov charge statistics in solvents of arbitrary quality. They identify ten necklace regimes, classify them into three types (charge-in-beads, charge-in-strings, and hierarchical necklace-in-necklace), and report quantitative confirmation of key predictions via coarse-grained molecular dynamics simulations. The work is framed as relevant to intrinsically disordered proteins/regions.
- **Visible evidence base** The theoretical derivations are presented in the text with equations and scaling arguments. Simulation results are described qualitatively and with reference to figures (e.g., Figure 3c,d) that were not provided. No numerical data, error bars, or statistical analyses are available in the supplied material.
- **Missing materials affecting confidence** All figures, tables, and the supplementary information are absent. This includes the scaling diagram (Figure 1), simulation data plots (Figure 3), and the detailed free-energy derivations referenced as being in the SI. Without these, quantitative claims cannot be independently verified.

## Reviewer
- **Overall assessment** This manuscript addresses a significant and timely problem in polyampholyte physics, with clear relevance to the IDP community. The theoretical framework is ambitious and appears internally consistent, and the identification of hierarchical necklace-in-necklace conformations is conceptually novel. However, the evidentiary basis for the central quantitative claims is incomplete in the supplied material. The simulation section describes results but does not provide the data needed to assess the claimed quantitative agreement. The relevance to IDPs is discussed qualitatively but lacks a concrete demonstration of predictive utility. The work is potentially important, but the case is not fully established from the provided evidence.
- **Who would be interested in the results, and why** Polymer physicists studying charged polymers and conformational transitions would find the scaling diagram and the charge-migration mechanism of direct interest. The IDP community, particularly those working on sequence-conformation relationships, would be interested in the extension to Markov charge statistics and the potential for improved structure prediction. Experimentalists using scattering methods to probe IDP conformations may also find the predicted regimes useful for interpreting data.
- **Major strengths** The theoretical framework is systematic and general, unifying previous results for random polyampholytes and polyelectrolytes within a single scaling diagram. The concept of charge migration from beads to strings, and the resulting hierarchical necklaces, is a genuinely new contribution. The use of Markov statistics to interpolate between alternating and blocky sequences is a practical and powerful approach. The authors are careful to distinguish between mean-field regimes and those where charge migration matters.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (simulation data not provided), R1-M2 (quantitative agreement not assessable), R1-M3 (IDP relevance not demonstrated), R1-M4 (crossover derivations not shown).
- **Assessment against Nature-style criteria** Originality: High. The hierarchical necklace concept and the charge-migration mechanism are novel. Scientific importance: High for the polymer physics and IDP communities, provided the predictions hold. Interdisciplinary readership: Moderate. The work bridges polymer theory and biology, but the presentation is heavily theoretical and may be challenging for nonspecialists. Technical soundness: The scaling arguments appear plausible, but the lack of simulation data and SI derivations prevents full verification. Readability for nonspecialists: The introduction and conclusions are accessible, but the core theory sections are dense and assume significant prior knowledge. Overall, the work has the potential to meet Nature-level standards, but the current evidence is insufficient.
- **Recommendation posture** Supportive if technical concerns are resolved. The theoretical contribution is promising, but the manuscript cannot be accepted without the simulation data and SI derivations being made available for verification.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that "scaling predictions are quantitatively confirmed by molecular dynamics simulations" (abstract) and that "the detected scaling slopes for L_neck and N_bead are consistent with the scaling laws for the respective regimes" (Conclusions).
- **Evidence pointer** Section 8 (Molecular Dynamics Simulations), Figure 3 (not provided)
- **Concern** The simulation section describes results but the actual data are not available in the supplied material. No figures, numerical values, or statistical measures are provided. The claim of quantitative confirmation cannot be assessed without seeing the data, the fitting procedure, or the error analysis.
- **Why it matters** The quantitative confirmation is a central pillar of the paper's claim to provide a complete and validated theory. Without the data, the reader cannot distinguish between a robust confirmation and a loose qualitative agreement.
- **Resolution test** Provide the simulation data in a form that allows independent verification, including the fitted slopes, the range of parameters, and the statistical uncertainties. The data should be presented in a way that directly compares to the predicted scaling laws.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the detected scaling slopes for L_neck and N_bead are consistent with the scaling laws for the respective regimes" (Conclusions).
- **Evidence pointer** Section 8, Figure 3c,d (not provided)
- **Concern** The text mentions that the simulation data collapse onto a universal master curve when normalized by the crossover values, but the quality of this collapse is not described. The agreement between the predicted and measured slopes is stated but not quantified. The text also notes that data at high blockiness are excluded due to kinetic trapping, but the criteria for this exclusion are not given.
- **Why it matters** The scaling exponents are the quantitative predictions of the theory. If the agreement is only approximate or holds over a narrow range, the claim of quantitative confirmation is weakened.
- **Resolution test** Provide the actual scaling exponents extracted from the simulations, with uncertainties, and compare them to the predicted values. Describe the criteria for excluding kinetically trapped data and show that the results are robust to reasonable variations in these criteria.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors state that "Our findings on the conformational statistics of charge-imbalanced polyampholytes may contribute to improved prediction and classification of the structure of intrinsically disordered proteins/regions (IDPs/IDRs)" (abstract) and discuss this in Section 9.
- **Evidence pointer** Section 9 (Relevance to Intrinsically Disordered Proteins)
- **Concern** The relevance to IDPs is discussed in general terms, but no specific example is given. The authors mention that the average block length in IDPs is approximately 1.27, but they do not show how this value maps onto the scaling diagram or what conformational predictions follow for a specific IDP. The connection to experimental data is also not made.
- **Why it matters** The IDP relevance is a key motivation for the work and a potential source of broad impact. Without a concrete demonstration, the claim remains speculative.
- **Resolution test** Provide a specific example of an IDP or a set of IDPs, compute their effective blockiness and solvent quality parameters, and show where they fall on the scaling diagram. If possible, compare the predicted conformations to available experimental data.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the latter is rigorously derived in the SI by means of the free-energy minimization" (Section 7.3) and refer to the SI for several derivations.
- **Evidence pointer** Section 7.3, Supporting Information (not provided)
- **Concern** Several key results, including the equality of electrostatic potentials in good solvent and the free-energy minimization for the hierarchical necklace, are stated to be derived in the SI. These derivations are not available in the supplied material, so their correctness cannot be assessed.
- **Why it matters** These derivations underpin the quantitative predictions for the hierarchical necklace regime, which is a central novel contribution.
- **Resolution test** Make the SI available for review. The derivations should be complete, self-contained, and lead to the stated results.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2 (Theoretical Model)
- **Evidence pointer** Equation 3
- **Issue** The definition of the average block charge as 1 + Λ is stated, but the relationship between Λ and the physical block length is not immediately intuitive. A brief explanation of why this is the natural measure of blockiness would help the reader.
- **Required correction** Add a sentence explaining the physical interpretation of Λ and why it is the appropriate parameter for the scaling diagram.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section 4 (Polyampholyte Necklaces with Homogeneous Charge Distribution: General Analysis)
- **Evidence pointer** Equations 14-27
- **Issue** The general analysis is presented in a compact form with many variables defined in the text. The reader must track multiple parameters (φ_att, ξ_att, δf, etc.) without a summary table or a schematic figure.
- **Required correction** Consider adding a table summarizing the key parameters and their physical meanings, or a schematic figure illustrating the necklace structure and the relevant length scales.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 8 (Molecular Dynamics Simulations)
- **Evidence pointer** Section 8, first paragraph
- **Issue** The simulation model is described as "coarse-grained" but the specific interaction potentials, the choice of parameters, and the system size are not described in the text. The reader is referred to the SI for details.
- **Required correction** Provide a brief summary of the simulation model in the main text, including the key interaction parameters and the range of system sizes studied.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 9 (Relevance to Intrinsically Disordered Proteins)
- **Evidence pointer** Section 9, paragraph 2
- **Issue** The statement that "the average sequence of ionic monomers in IDPs only weakly deviates from an ideally random one" is based on a mean value of Λ ≈ 1.27, but the distribution of Λ values across IDPs is not discussed. It is possible that a significant fraction of IDPs have much higher blockiness.
- **Required correction** Provide information on the distribution of Λ values, not just the mean, to support the claim that most IDPs fall in the low-blockiness regimes.

## Risk / unsupported claims
- The claim of "quantitative confirmation" of scaling predictions by simulations is unsupported in the supplied material, as the simulation data are not provided.
- The claim that the equality of electrostatic potentials in good solvent is "rigorously derived" is unverifiable without the SI.
- The claim that the hierarchical necklace is a "novel" conformation is plausible but cannot be fully assessed without the figures showing the simulation snapshots.
- The relevance to IDPs is stated as a potential contribution but is not demonstrated with a specific example.
- The scaling diagram in Figure 1 is described but not shown, so the boundaries between regimes and the crossover lines cannot be checked.