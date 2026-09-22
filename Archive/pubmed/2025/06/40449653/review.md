## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results and discussion, conclusion, and materials and methods. Figures and tables are referenced but not directly provided; supplementary material is mentioned but not accessible.
- **Assessment boundary** Scientific content, methodological rigor, internal consistency, and support of claims by presented evidence. No assessment of formatting, language style, or journal fit beyond Nature-style criteria.
- **Shared manuscript claim summary** The K141E mutation in HSPB8 increases conformational flexibility and population of extended states, particularly at physiological ionic strength, as shown by smFRET and MD simulations, potentially explaining its reduced chaperone activity and pathogenicity.
- **Visible evidence base** Text descriptions of EncoderMap 2D KDE plots (Figure 2), representative structures (Figure 3), smFRET histograms and lifetime data (Figures 4, 8, 9), denaturation curves (Figures 5-7), salt bridge analysis (Figure S11), and BME reweighting results (Figure 9). Methods sections for smFRET, MD simulations, FRETpredict, and BME reweighting.
- **Missing materials affecting confidence** Actual figure images, numerical values for FRET efficiencies and uncertainties, supplementary figures and tables (S1-S13), simulation convergence metrics beyond autocorrelation times, and raw data. These limit quantitative verification of claims.

## Reviewer
- **Overall assessment** The manuscript presents a plausible and potentially valuable integration of smFRET experiments and all-atom MD simulations to characterize conformational changes induced by the K141E mutation in HSPB8. The combination of experimental and computational approaches is appropriate for studying an intrinsically disordered protein. However, the evidence as presented is largely qualitative, with key quantitative details and figure data not fully accessible in the text. The central claim that increased conformational flexibility underlies pathogenicity is reasonable but not definitively established, as the link to functional outcomes remains correlative. The work is technically sound in design but requires stronger quantitative support and clearer presentation of results to fully substantiate the conclusions.

- **Who would be interested in the results, and why** Researchers studying small heat shock proteins, molecular chaperones, intrinsically disordered proteins, and the molecular basis of neurodegenerative and neuromuscular diseases. The methodological integration of smFRET with MD simulations and BME reweighting will also interest biophysicists and computational biologists working on conformational ensembles of IDPs. The findings on ionic strength effects may inform studies on cellular stress responses and protein homeostasis.

- **Major Strengths**
  1. The combination of smFRET and all-atom MD simulations with BME reweighting is a powerful and appropriate approach for studying IDP conformational dynamics.
  2. The study addresses a clinically relevant mutation (K141E) linked to multiple neuropathies, providing potential mechanistic insight.
  3. The systematic variation of ionic strength is a thoughtful experimental design that reveals environment-dependent effects.
  4. The use of FRETpredict with rotamer libraries is a modern and rigorous method for computing FRET efficiencies from simulations.
  5. The authors acknowledge limitations and provide detailed methods for reproducibility.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** "The K141E mutant exhibits increased conformational flexibility compared to the wild-type protein, particularly at high physiological ionic strengths, leading to a more extended conformational ensemble."
- **Evidence pointer** Figure 2, Figure 3, Figure 4, Figure 8, Table S1
- **Concern** The central claim of increased conformational flexibility is supported primarily by qualitative descriptions of EncoderMap plots and visual inspection of smFRET histograms. No quantitative metrics (e.g., differences in covered area density, statistical tests, confidence intervals) are provided in the text. The reported differences in covered area density (e.g., 10% smaller rectangle at 0 mM, 24% larger at 165 mM) lack error estimates or significance testing. Without quantitative support, the claim remains descriptive rather than demonstrated.
- **Why it matters** The conclusion that the mutation increases conformational flexibility is the cornerstone of the paper. If this is not rigorously quantified, the mechanistic interpretation and link to pathogenicity are weakened.
- **Resolution test** Provide numerical values with uncertainties for covered area, covered area density, and FRET efficiency peak positions and widths for all conditions. Include statistical tests (e.g., bootstrap or Bayesian credible intervals) comparing WT and K141E at each ionic strength.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "Bayesian maximum entropy reweighting was applied to improve agreement between simulated and experimental smFRET data."
- **Evidence pointer** Figure 9, Figure S13, Methods section "Reweighting calculations with Bayesian/MaxEnt approach (BME)"
- **Concern** The BME reweighting procedure is described, but the results are only stated as "improved agreement" without showing quantitative before-and-after comparisons. The choice of uncertainty (δϵ²k = 0.02) is not justified, and the sensitivity of results to this parameter is not explored. Additionally, the text states that FRETpredict reweighting (based on dye-protein interactions) was not applied because it had negligible effect, but the rationale for this conclusion is not quantified.
- **Why it matters** BME reweighting is a key methodological step that claims to refine the ensemble. Without demonstrating its effect quantitatively and justifying parameter choices, the validity of the reweighted ensembles and subsequent analyses (salt bridges, EncoderMap) is uncertain.
- **Resolution test** Show quantitative comparison of FRET efficiency distributions (e.g., mean, width, overlap) before and after BME reweighting for all labeling positions and conditions. Provide a sensitivity analysis for the uncertainty parameter and justify the chosen value.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretive validity
- **Claim pointer** "The elevated secondary peak frequency in the K141E variant at physiological ionic strength suggests a destabilization of the folded state, which may be linked to its propensity to populate extended conformations."
- **Evidence pointer** Figure 4, Figure 8, Figure 9
- **Concern** The interpretation that the secondary peak represents an unfolded state and that its increased frequency in K141E indicates destabilization is plausible but not directly tested. The manuscript does not establish that the secondary peak corresponds to a specific conformational state (e.g., via comparison with denatured samples or independent structural probes). The connection between the secondary peak and functional impairment is speculative.
- **Why it matters** The mechanistic link between conformational dynamics and pathogenicity is a major conclusion. If the secondary peak assignment is not validated, the interpretation may be overreaching.
- **Resolution test** Provide evidence that the secondary peak corresponds to an unfolded or extended state (e.g., by comparing with chemically denatured samples or using complementary techniques such as fluorescence correlation spectroscopy). Discuss alternative interpretations and how the data distinguish them.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** "Five replicas of 1 μs all-atom MD simulations were performed for both the WT and the K141E mutant protein at 0 mM and 165 mM ionic strength."
- **Evidence pointer** Table 1, Methods section "MD simulations"
- **Concern** The simulation setup is described, but key details for reproducibility are missing. The starting structures are stated to be I-TASSER homology models, but the specific template, sequence coverage, and model quality are not provided. The choice of force field (Amber99sb-disp) and water model (TIP4PD) is stated, but no validation of the force field for this system is given. The equilibration protocol is brief, and the criteria for considering simulations converged are not fully described beyond autocorrelation times.
- **Why it matters** Reproducibility is essential for computational studies. Without complete details, other groups cannot replicate or build upon these simulations.
- **Resolution test** Provide full details of model construction, including template PDB IDs, alignment information, and model quality scores. Describe the full equilibration protocol and convergence criteria in detail. Consider depositing starting structures and trajectories in a public repository.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 2 description
- **Evidence pointer** Figure 2, text in "K141E pathogenic mutation increases conformational sensitivity to ionic strength"
- **Issue** The description of EncoderMap plots is vague. The text states "thicker contours correspond to the conformations most frequently sampled" and describes "conformational islands" but does not explain what the axes represent or how to interpret the differences quantitatively.
- **Required correction** Clarify the meaning of the EncoderMap coordinates and provide a more detailed interpretation of the plots, including what specific structural features distinguish the conformational states.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Salt bridge analysis
- **Evidence pointer** Figure S11, Methods section "Salt bridges"
- **Issue** The salt bridge analysis is mentioned as supporting the mechanistic interpretation, but the results are only described qualitatively in the text. The specific salt bridges that differ between WT and K141E are not named or quantified.
- **Required correction** Provide a table or list of the key salt bridges that differ between variants, with their frequencies and statistical significance.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Force field justification
- **Evidence pointer** Methods section "MD simulations"
- **Issue** The choice of Amber99sb-disp force field is stated but not justified. Given that this force field was developed for disordered proteins, a brief justification or citation would strengthen the methods.
- **Required correction** Add a sentence explaining why this force field is appropriate for HSPB8 and cite relevant validation studies.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Denaturation experiments
- **Evidence pointer** Figures 5-7, Methods section "Analysis of smFRET denaturation experiments"
- **Issue** The denaturation experiments are described, but the choice of denaturants (urea and GdmCl) and the interpretation of differences between them are not discussed. The text notes a "more pronounced difference in the unfolding response" for urea but does not explain why.
- **Required correction** Add a brief discussion of why urea and GdmCl may produce different responses and what this implies for the conformational properties of HSPB8.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Data availability
- **Evidence pointer** Data availability statement
- **Issue** The data availability statement only mentions sharing code, not the simulation trajectories or experimental data. Given the emphasis on reproducibility, this is insufficient.
- **Required correction** Specify where simulation input files, trajectories, and raw smFRET data can be accessed, or state clearly if they are available upon request.

## Risk / unsupported claims
- The claim that increased conformational flexibility "negatively influences the protein function" is not directly tested in this study; functional assays are referenced from prior work but not performed here.
- The statement that "the pathogenicity of the K141E mutation may be, at least in part, due to the enhanced conformational variability" is presented as a conclusion but remains a hypothesis without direct functional correlation.
- The assertion that "the study underscores the significance of ionic strength in the structural dynamics of intrinsically disordered proteins like HSPB8" is supported by the data but is a general statement that extends beyond the specific system studied.
- The claim that "the insights gained here can readily extend to other IDPs" is speculative and not supported by comparative analysis with other systems.
- The interpretation of the secondary peak in smFRET as an unfolded state is not validated with independent measurements.
- The statement that "the simulations have likely achieved convergence" based solely on autocorrelation times is weak; more robust convergence metrics (e.g., block averaging, multiple independent runs) are needed.
- The use of NaCl in simulations versus KCl in experiments is acknowledged but the potential impact on results is not discussed.