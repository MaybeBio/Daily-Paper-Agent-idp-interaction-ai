## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, discussion, conclusion, and data availability statement. Figures are referenced but not directly viewable; figure content is inferred from captions and text.
- **Assessment boundary** Scientific soundness, methodological rigor, internal consistency, and support of claims by presented evidence. No assessment of formatting, grammar, or journal fit beyond Nature-style criteria.
- **Shared manuscript claim summary** The authors characterize the conformational ensemble of a 35-residue AICD fragment containing the YENPTY motif using all-atom MD simulations (AMBER99SB-ILDN, TIP4P-D, 5 × 1 μs), and compare against experimental SAXS, CD, and NMR data. They report a dynamic equilibrium between compact and extended states, transient secondary structure, motif-specific hydrogen bonding, and metastable conformational states identified via tICA and clustering.
- **Visible evidence base** Abstract, introduction, methods, results, discussion, conclusion, data availability, acknowledgments, author contributions, declaration of interests. Figures 1–12 are described in text and captions. Supplementary figures S1–S9 are mentioned but not provided.
- **Missing materials affecting confidence** Actual figure images, supplementary figures S1–S9, experimental SAXS data files, CD spectra raw data, NMR data details, simulation input files, and the Zenodo repository contents were not accessible. This limits verification of fit quality, spectral comparisons, and clustering results.

## Reviewer
- **Overall assessment** This manuscript presents a technically competent and potentially useful characterization of the conformational landscape of an AICD fragment. The combination of long all-atom MD simulations with experimental validation via SAXS and CD is appropriate and timely. However, several concerns reduce confidence in the strength of the conclusions. The claim of being the "first application of all-atom MD simulations to a biologically active AICD fragment" is difficult to verify and may be overstated. The comparison between simulated and experimental SAXS data, while showing a reasonable χ² value, lacks discussion of systematic deviations visible in the Kratky plot. The CD spectral comparison shows notable discrepancies that are acknowledged but not fully explained. The tICA analysis is presented without convergence assessment or validation of the chosen lag time. The clustering analysis in Figure 12 appears to describe interactions with a "protein partner" that is not defined in the methods, creating confusion about what was actually simulated. The functional implications discussed are speculative and not directly supported by the data presented. Overall, the work is a solid biophysical characterization but the interpretive claims extend beyond the evidence base.

- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, particularly those involved in neurodegeneration, would find this work relevant. The methodological approach combining MD with SAXS and CD validation is of interest to computational biophysicists. Those studying APP processing and AICD signaling may use these conformational insights to inform hypotheses about binding mechanisms. The study may also interest developers of force fields for disordered proteins, given the use of AMBER99SB-ILDN with TIP4P-D.

- **Major strengths**
  1. The study addresses a biologically important and structurally undercharacterized system.
  2. The use of multiple independent 1 μs simulations provides substantial sampling.
  3. Integration of experimental SAXS and CD data with simulations strengthens the validation approach.
  4. The residue-level analysis of SASA, secondary structure propensity, and hydrogen bonding provides useful detail.
  5. The data and code availability statement is commendable.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "to our knowledge, this study represents the first application of all-atom molecular dynamics (MD) simulations to a biologically active AICD fragment encompassing the conserved YENPTY motif."
- **Evidence pointer** Introduction, location not provided
- **Concern** This novelty claim is difficult to verify and may be inaccurate. Prior computational studies on AICD or APP intracellular domains may exist that are not cited. The claim is presented without a comprehensive literature search or a clear definition of what constitutes a "biologically active fragment." If this claim is incorrect, it undermines the perceived novelty of the work.
- **Why it matters** The primary contribution of this study is framed around being the first all-atom MD study of this system. If this is not accurate, the scientific contribution shifts from novelty to incremental characterization, which changes the assessment of the work's significance.
- **Resolution test** The authors should either provide a thorough literature search demonstrating no prior all-atom MD studies of AICD, or soften the claim to accurately reflect the state of the field.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the agreement in secondary structure composition suggests that the simulation provides a reasonable representation of the protein's structural ensemble" based on the CD comparison in Figure 8.
- **Evidence pointer** Results, Figure 8, location not provided
- **Concern** The experimental CD spectrum shows two negative bands near 208 nm and 222 nm, characteristic of α-helical structure, with the table indicating 60% helical content. The simulated spectrum is described as capturing "several general features" but with "differences in intensity and spectral shape." The nature and magnitude of these differences are not quantified. A 60% helical content for a predominantly disordered protein is surprisingly high and may indicate that the peptide has significant secondary structure propensity that is not fully captured by the simulation. The authors do not provide a quantitative comparison of secondary structure fractions between experiment and simulation.
- **Why it matters** The CD comparison is one of the key experimental validations of the simulation. If the agreement is only qualitative and the helical content is substantially different, the claim that the simulation represents the experimental ensemble is weakened.
- **Resolution test** Provide a quantitative comparison of secondary structure fractions (e.g., helix, sheet, coil) from CD analysis versus simulation, with error estimates. Discuss the implications of any discrepancies for the interpretation of the conformational ensemble.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "tICA identifies the slowest dynamic processes, which could be linked to biologically significant transitions" and that "the gradual change across tICA space suggests that the expansion and compaction of AICD are slow processes governed by its underlying energy landscape."
- **Evidence pointer** Results, Figure 10, location not provided
- **Concern** The tICA analysis is presented without essential methodological details. The lag time used for the tICA calculation is not stated. No convergence assessment is provided to demonstrate that the identified metastable states are robust. The choice of features used as input for tICA is not described. Without these details, the reliability of the tICA results cannot be evaluated.
- **Why it matters** tICA results are highly sensitive to the choice of lag time and input features. If the analysis is not converged or the parameters are not justified, the identified metastable states may be artifacts of the analysis rather than genuine features of the conformational landscape.
- **Resolution test** Provide the tICA lag time, the features used, and a convergence analysis (e.g., implied timescales vs. lag time). Demonstrate that the metastable states are robust to parameter choices.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "Fig. 12 illustrates four representative structural clusters (a–d) obtained from the conformational analysis of a protein containing the YENPTY motif" and describe "van der Waals interactions" and "π-interactions" that "may contribute to stabilizing the peptide within different binding pockets of the protein."
- **Evidence pointer** Results, Figure 12, location not provided
- **Concern** The methods section does not describe any simulation of AICD bound to a protein partner. The clustering analysis appears to be performed on the free AICD simulations, yet Figure 12 is described in terms of "binding pockets," "binding state," and "docking pose." This is confusing and suggests either a missing methods description or an overinterpretation of the free-state simulations. If the clusters are from free AICD simulations, the description of "binding" is inappropriate.
- **Why it matters** The interpretation of the clusters as binding-competent states is a key part of the functional implications discussed. If this interpretation is not supported by the actual simulations performed, the conclusions about AICD's interaction potential are not justified.
- **Resolution test** Clarify what system was used for the clustering analysis. If the clusters are from free AICD simulations, revise the interpretation to avoid implying binding interactions. If a bound simulation was performed, provide the full methods details.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors state that "These findings highlight the structural plasticity of AICD and offer insights into its potential for interaction and regulatory roles in nuclear signaling and neurodegeneration."
- **Evidence pointer** Abstract, Discussion, location not provided
- **Concern** The functional implications are largely speculative. The study characterizes the conformational ensemble of a free 35-residue fragment, but does not directly measure or simulate interactions with binding partners, posttranslational modifications, or nuclear transport. The link between the observed conformational heterogeneity and specific biological functions is not established.
- **Why it matters** The significance of the work depends on the relevance of the characterized conformational landscape to AICD function. Without direct evidence connecting the observed states to functional outcomes, the significance remains inferred rather than demonstrated.
- **Resolution test** Either temper the functional claims to match the evidence, or add experiments or simulations that directly test the functional relevance of the identified conformational states.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, Molecular dynamics simulations
- **Evidence pointer** Methods, location not provided
- **Issue** The manuscript states that five independent simulations were performed, each with a production run of 1 μs, totaling 5 μs. However, the first 300 ns of each simulation were discarded, leaving 700 ns per simulation and 3.5 μs of total analyzed simulation time. The text does not clearly state the total analyzed time.
- **Required correction** Clarify the total analyzed simulation time after discarding the equilibration period.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, Small-angle X-ray scattering measurements
- **Evidence pointer** Methods, location not provided
- **Issue** The peptide concentration for SAXS was 0.5 mg/mL, but the molecular weight of the peptide is not stated, so the molar concentration cannot be determined. This limits assessment of whether the concentration is appropriate for SAXS measurements of a small peptide.
- **Required correction** Provide the molecular weight of the peptide and the molar concentration used for SAXS measurements.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, Figure 3
- **Evidence pointer** Results, Figure 3, location not provided
- **Issue** The text states that simulations yielded average Rg values of 16.10 Å and 15.10 Å, but only one force field (AMBER99SB-ILDN) is described in the methods. The source of the second Rg value is unclear.
- **Required correction** Clarify whether two force fields were used or if the two values correspond to different analysis conditions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Discussion
- **Evidence pointer** Discussion, location not provided
- **Issue** The discussion of "conformational selection or induced fit mechanisms" is brief and does not explain how the observed data specifically support one mechanism over the other.
- **Required correction** Expand the discussion to explain how the data inform these mechanisms, or temper the claim if the data are not discriminating.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, Figure 12
- **Evidence pointer** Results, Figure 12, location not provided
- **Issue** The figure caption mentions "dihedral angle distance" for the pink dashed lines, but the text describes these as "π-interactions." These are different concepts and the inconsistency is confusing.
- **Required correction** Reconcile the figure caption and text description of the pink dashed lines.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, Circular dichroism
- **Evidence pointer** Methods, location not provided
- **Issue** The CD measurements were performed at pH 7.0 in a phosphate buffer, while the SAXS measurements were at pH 7.5 in Tris buffer. The simulations were at neutral pH. The potential effect of these buffer differences on the conformational ensemble is not discussed.
- **Required correction** Acknowledge the buffer differences and discuss whether they could affect the comparison between experimental and simulated data.

## Risk / unsupported claims
- The claim of being the "first application of all-atom MD simulations to a biologically active AICD fragment" is unverifiable from the provided text and may be inaccurate.
- The functional implications regarding "nuclear signaling and neurodegeneration" are speculative and not directly supported by the data.
- The interpretation of clusters in Figure 12 as "binding states" or "docking poses" is unsupported because no bound-state simulations are described in the methods.
- The statement that "the agreement in secondary structure composition suggests that the simulation provides a reasonable representation of the protein's structural ensemble" is weakened by acknowledged discrepancies in the CD comparison that are not quantified.
- The tICA results are presented without convergence assessment, making the identified metastable states unverifiable.
- The claim that "AICD fluctuates between compact and extended states" is supported by the SAXS and simulation data, but the biological relevance of this fluctuation is not established.
- The statement that "these findings provide a framework for therapeutic strategies targeting disordered protein regions" is an overreach given the basic biophysical nature of the study.