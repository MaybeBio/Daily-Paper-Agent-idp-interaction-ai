## Review setup
- **Input scope** Full manuscript text including abstract, introduction, materials and methods, results, and discussion. No supplementary figures or tables were provided.
- **Assessment boundary** Scientific claims, methodological soundness, and interpretation of results as presented in the main text. Supplementary materials referenced but not available for review.
- **Shared manuscript claim summary** The authors report that a thirteen-residue peptide corresponding to the linker region of the protein disulphide isomerase PmScsC is intrinsically disordered in aqueous solution, adopts partial helical structure in 50% TFE, and that the different conformations observed in crystal structures are stabilized by intermolecular contacts. They propose functional relevance for substrate binding and implications for understanding protein aggregation.
- **Visible evidence base** NMR chemical shift data (secondary shifts, SSP scores, 3JHNHα coupling constants), NOE observations, CD titration data (referenced as Figure S3), MD simulation trajectories (four 100 ns peptide simulations, one 20 ns trimer simulation), and analysis of crystal contacts using PISA and EPPIC.
- **Missing materials affecting confidence** Supplementary figures (S1–S4) and Table S1 are referenced but not provided. Raw NMR spectra, MD trajectory details, force field validation, and convergence assessments are not available. The CD titration data are only mentioned in passing with no quantitative results shown in the main text.

## Reviewer
- **Overall assessment** This manuscript presents a straightforward biophysical characterisation of a short peptide derived from a protein linker region. The NMR experiments are competently described and the conclusion that the peptide is largely disordered in aqueous solution is well supported by the data shown. The MD simulations provide complementary information, though the analysis is somewhat limited. The discussion connecting the findings to MoRF behaviour and protein aggregation is speculative but reasonable. The main weakness is the limited novelty: the observation that a short peptide is disordered in isolation is not surprising, and the functional implications are not tested experimentally. The manuscript would be of interest to a specialised audience in protein biophysics and folding, but the broader significance is modest.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, chameleon sequences, and conformational plasticity in proteins. The work may also interest those investigating protein disulphide isomerases and the role of flexible linkers in multidomain proteins. The connection to amyloid formation could attract researchers in protein misfolding diseases, though the relevance is indirect.
- **Major strengths** The NMR characterisation is thorough and the use of multiple complementary techniques (chemical shifts, NOEs, coupling constants, SSP analysis) provides a consistent picture of disorder in aqueous solution. The comparison between solution behaviour and crystal conformations is clearly presented. The MD simulations starting from different crystal conformations provide useful insight into the conformational landscape of the peptide.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** No
  - **Axis** Evidence sufficiency
  - **Claim pointer** The authors state that the peptide is "essentially disordered in aqueous solution" based on NMR data.
  - **Evidence pointer** Figure 2, Section 3
  - **Concern** The SSP scores without averaging show small preferences for extended structure at the termini and helix in the central region. While the overall conclusion of disorder is reasonable, the manuscript does not provide a quantitative assessment of the ensemble, such as a comparison with random coil predictions for the specific sequence or an analysis of the distribution of conformations. The 3JHNα coupling constants are reported as a range, but individual values per residue are not shown, which would strengthen the analysis.
  - **Why it matters** The central claim of the paper is that the peptide is disordered. While the data are consistent with this, a more detailed residue-by-residue analysis would make the case more robust and allow readers to assess the extent of residual structure.
  - **Resolution test** Provide per-residue 3JHNα values and a more detailed comparison of observed chemical shifts with sequence-specific random coil values. Consider reporting the fraction of the ensemble in helical conformations from a more rigorous analysis.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness
  - **Claim pointer** The MD simulations are used to support the conclusion that the peptide samples a wide range of conformations and that the helical population is approximately 10-20%.
  - **Evidence pointer** Section 2.3, Figure 3, Table S1
  - **Concern** The manuscript reports four 100 ns simulations, which is a limited sampling time for a disordered peptide. No convergence analysis is presented, and the clustering results are based on a single clustering algorithm with a specific RMSD cutoff. The choice of the GROMOS 54A7 force field is appropriate, but the authors do not discuss potential force field biases for disordered peptides. The claim that cluster 4 represents helical conformations at a level "similar to the level of helicity suggested by the SSP score" is based on a single cluster population and may be coincidental.
  - **Why it matters** MD simulations of disordered peptides are known to be sensitive to force field choice and sampling time. Without convergence assessment or comparison with experimental data beyond a qualitative level, the simulation results provide only weak support for the conclusions.
  - **Resolution test** Extend simulation time, perform replicate simulations, and assess convergence of structural properties. Compare simulated chemical shifts or J-couplings with experimental values to validate the force field and sampling.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Interpretation
  - **Claim pointer** The authors state that "the quaternary structure of the trimer is likely to be an ensemble of conformers, rather than any one of the different structures seen in crystals predominating in solution" based on a 20 ns simulation.
  - **Evidence pointer** Section 3, Figure 4
  - **Concern** A single 20 ns simulation of a trimeric protein is very short and unlikely to provide meaningful sampling of the conformational space. The observation that the N-terminal region of one linker peptide starts to unfold is anecdotal and not statistically supported. The conclusion about the ensemble nature of the trimer in solution is speculative and goes beyond what can be concluded from this limited simulation.
  - **Why it matters** The functional implications discussed later depend on the flexibility of the linker in the context of the full trimer. If the evidence for this flexibility is weak, the functional claims are correspondingly weakened.
  - **Resolution test** Perform longer simulations with replicates, or use enhanced sampling methods. Alternatively, temper the claims about the trimer dynamics and focus on what can be concluded from the peptide simulations and crystal structure analysis.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Abstract
  - **Evidence pointer** Abstract
  - **Issue** The abstract states that the peptide "can adopt helical, β-strand and loop conformations" in crystal structures, but the term "loop" is vague. It would be clearer to specify that this refers to a non-regular extended conformation.
  - **Required correction** Replace "loop" with "irregular" or "non-regular" conformation, or define what is meant by loop in this context.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Methods
  - **Evidence pointer** Section 2.2
  - **Issue** The NMR experiments are described, but no details are given for the CD spectroscopy experiments referenced in the results and Figure S3. The titration conditions, instrument, and analysis method should be described.
  - **Required correction** Add a subsection describing the CD experiments, including sample preparation, instrument parameters, and data analysis.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Interpretation
  - **Affected element** Discussion
  - **Evidence pointer** Section 4
  - **Issue** The comparison to p53 and MoRFs is interesting but the authors do not discuss the length difference: the PmScsC linker is only 11 residues, whereas MoRF regions are typically longer. This may affect the generalisability of the comparison.
  - **Required correction** Acknowledge the length difference and discuss whether the behaviour of such a short peptide can be meaningfully compared to longer MoRF regions.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Presentation
  - **Affected element** Figure 2
  - **Evidence pointer** Figure 2
  - **Issue** The figure shows secondary shifts and SSP scores, but the residue numbering is not clearly defined in the figure legend. It would help to state which residue numbers correspond to the peptide sequence.
  - **Required correction** Add residue numbering to the figure or clarify in the legend.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Technical detail
  - **Affected element** Methods
  - **Evidence pointer** Section 2.3
  - **Issue** The clustering analysis uses a 0.15 nm RMSD cutoff, but the rationale for this choice is not given. A brief justification or reference would be helpful.
  - **Required correction** Provide a brief justification for the clustering parameters or cite a reference for the choice.

## Technical failings that need to be addressed before the case is established
- The MD simulation sampling is limited (4 x 100 ns for the peptide, 1 x 20 ns for the trimer) without convergence analysis. This weakens the quantitative claims about conformational populations.
- The CD titration data are referenced but not described in the methods or shown in the main text, making the claim about "no cooperative transition" unverifiable from the provided material.
- The per-residue analysis of NMR parameters (coupling constants, NOE patterns) is not shown in sufficient detail to fully assess the disorder claim.

## Risk / unsupported claims
- The claim that the trimer exists as an ensemble of conformers in solution is not supported by the limited 20 ns simulation and is speculative.
- The functional relevance of linker flexibility for substrate binding and disulphide shuffling is plausible but not tested experimentally; this is presented as speculation in the discussion, which is acceptable, but should be clearly framed as such.
- The relevance to protein aggregation and amyloid formation is inferred from a single β-strand conformation in one crystal structure and is not directly demonstrated.
- The comparison to MoRFs in IDPs is qualitative and the short length of the peptide may limit the validity of this comparison.

## Assessment against Nature-style criteria
- **Originality** Moderate. The concept of chameleon sequences is established, and the specific system has been previously described. The new contribution is the solution characterisation of the isolated peptide, which is a logical but not highly original extension.
- **Scientific importance** Limited. The findings are of interest to specialists in protein biophysics but do not fundamentally change our understanding of protein folding, disorder, or function. The functional implications are speculative and not tested.
- **Interdisciplinary readership** Narrow. The work is primarily relevant to structural biology and biophysics. The connections to protein misfolding diseases and IDPs may attract some broader interest, but the technical nature of the study limits its appeal.
- **Technical soundness** The NMR methodology is sound, but the MD simulations are under-sampled and the CD data are not fully described. The crystal contact analysis is appropriate but descriptive.
- **Readability for nonspecialists** The manuscript is clearly written and the concepts are explained adequately. However, the significance of the findings for a general scientific audience is not compellingly articulated.

## Recommendation posture
Supportive if technical concerns are resolved. The core observation that the peptide is disordered in solution is well supported by the NMR data, and the manuscript is a reasonable contribution to the specialised literature. However, the MD simulation analysis needs strengthening, the CD data need to be properly described, and the speculative claims about function and aggregation should be tempered or clearly labelled as hypotheses. The novelty is modest, and the broader significance is not fully established.