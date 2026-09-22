## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, supplementary figure/table references)
- **Assessment boundary** Scientific claims, methodological rigor, and interpretive validity as presented in the manuscript; no assessment of editorial fit or publication policy
- **Shared manuscript claim summary** The authors characterize the transient homo-dimerization of the second bromodomain of BRD4 (BRD4BD2) using NMR spectroscopy, SAXS, and integrative modeling, and extend their analysis to predict dimerization propensity across the human bromodomain family using AlphaFold-Multimer and AlphaFold3.
- **Visible evidence base** NMR chemical shift perturbation data, 2D lineshape analysis (NMR-TITAN), 15N-CPMG relaxation dispersion, 15N spin relaxation, PFG-NMR diffusion, SAXS, HADDOCK docking, AlphaFold-Multimer and AlphaFold3 predictions
- **Missing materials affecting confidence** Supplementary figures and tables referenced but not provided; AlphaFold prediction details (e.g., multiple sequence alignments, confidence metrics per model) not fully described; raw SAXS curves and fitting details not shown; HADDOCK cluster statistics not fully reported

## Reviewer
- **Overall assessment** This manuscript presents a rigorous and well-executed biophysical characterization of BRD4BD2 dimerization, combining multiple orthogonal NMR methods with SAXS and integrative modeling. The experimental work is thorough, and the finding that BRD4BD2 dimerizes weakly (Kd ~400 µM) with a short lifetime (~1 ms) is well supported. The extension to family-wide AlphaFold predictions is interesting but less well validated, and the authors appropriately acknowledge limitations. The manuscript is clearly written and will appeal to structural biologists and biophysicists interested in protein-protein interactions, weak oligomerization, and the application of AlphaFold to transient complexes. However, several technical concerns regarding the interpretation of the CPMG data, the AlphaFold validation strategy, and the generalizability of the conclusions need to be addressed.

- **Who would be interested in the results, and why** Structural biologists studying bromodomain-containing proteins and BET family members; biophysicists interested in weak protein-protein interactions and transient oligomerization; computational biologists using AlphaFold for complex prediction; researchers studying transcriptional regulation and biomolecular condensates.

- **Major strengths** (1) The combination of multiple orthogonal biophysical methods (CSPs, lineshape analysis, CPMG, spin relaxation, PFG-NMR, SAXS) provides a compelling and internally consistent picture of BRD4BD2 dimerization. (2) The quantitative agreement between the NMR-TITAN-derived Kd and the CPMG-derived kinetic parameters strengthens confidence in the results. (3) The authors are appropriately cautious in their interpretation of the AlphaFold predictions, acknowledging the moderate ipTM scores and the need for experimental validation. (4) The discussion of the potential functional relevance of weak dimerization in the context of biomolecular condensates is thoughtful and well-reasoned.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that the CPMG-detected chemical exchange process is concentration-dependent and that increasing the total protein concentration from 0.91 mM to 1.6 mM decreased the values of Rex, indicating that the population of the minor state decreases with total protein concentration.
- **Evidence pointer** Results section "Characterizing BRD4BD2 dimerization by CPMG relaxation dispersion"; Figure 2; supplementary material Fig. 6
- **Concern** The interpretation of the CPMG data as reporting on monomer-dimer exchange requires careful scrutiny. In a monomer-dimer equilibrium, the population of the minor state (monomer) should increase with decreasing total protein concentration, which is consistent with the observed decrease in Rex at higher concentration. However, the authors state that the minor state corresponds to the monomer, yet they also state that they "directly observed cross-peaks from the dimeric conformation while the monomer remained 'invisible.'" This is confusing. If the monomer is the minor state and is "invisible," then the observed cross-peaks must arise from the dimer, which is the major state. The CPMG experiment detects exchange between a visible major state and an invisible minor state. If the dimer is the major state and is visible, then the minor state (monomer) is invisible, which is consistent. However, the authors need to clarify this point more explicitly. More importantly, the CPMG data were collected at a single static magnetic field strength, which the authors acknowledge. Fitting single-field CPMG data with both kex and pB as free parameters is known to be prone to parameter correlations. The authors fixed pB based on the NMR-TITAN-derived Kd, which is a reasonable approach, but this means the CPMG analysis is not fully independent of the lineshape analysis. The authors should discuss the potential impact of this constraint on the reported kinetic parameters.
- **Why it matters** The kinetic parameters (kex, koff, kon) are central to the claim that BRD4BD2 dimerization is transient and weak. If the CPMG analysis is not robust, the quantitative conclusions about the lifetime of the dimer are called into question.
- **Resolution test** The authors should provide a more detailed explanation of the CPMG fitting procedure, including how the fixed pB value was propagated into the error estimates for kex and koff. Ideally, they should also show that the fitted parameters are not strongly dependent on the choice of pB within the uncertainty of the NMR-TITAN-derived Kd. If possible, collecting CPMG data at a second magnetic field strength would strengthen the analysis.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the top-scoring HADDOCK cluster yields a dimeric complex with a buried surface area (BSA) of 1120 Å2 per subunit" and that the AlphaFold3-predicted model of the BRD4BD2 dimer "involves similar interfacial residues that we detected here by NMR spectroscopy."
- **Evidence pointer** Results section "Structural modeling of the BRD4BD2 dimer"; Figure 4; supplementary material Fig. 8
- **Concern** The HADDOCK docking was performed using CSP-derived restraints, but the authors do not provide sufficient detail on how the CSP data were converted into ambiguous interaction restraints (AIRs). Specifically, it is unclear which residues were defined as "active" and "passive" and how the solvent accessibility threshold was applied. Furthermore, the comparison between the HADDOCK model and the AlphaFold3 prediction is qualitative. The authors state that the AlphaFold3 model has a backbone RMSD of 1.5 Å relative to the second-best HADDOCK cluster, but they do not provide a quantitative comparison of the interfacial residues between the two models. The claim that the AlphaFold3 model "involves similar interfacial residues" needs to be supported by a direct residue-level comparison.
- **Why it matters** The structural model of the BRD4BD2 dimer is a key output of this work. If the model is not well-validated, the subsequent family-wide AlphaFold predictions lack a solid experimental anchor.
- **Resolution test** The authors should provide a detailed description of the HADDOCK setup, including the definition of active and passive residues. They should also provide a residue-level comparison of the interfacial residues in the HADDOCK model versus the AlphaFold3 model, perhaps in a supplementary table. A quantitative measure of interface similarity, such as the fraction of shared interfacial residues, would be helpful.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors state that "there are 15 other bromodomains with similar or higher mean ipTM scores than BRD4BD2, suggesting that bromodomain dimerization may be more widespread than appreciated."
- **Evidence pointer** Results section "AlphaFold predictions of human bromodomain dimers"; Figure 6; supplementary material Tables 2 and 3
- **Concern** The family-wide AlphaFold screen is presented as a major finding, but the validation of these predictions is limited. The authors compare ipTM scores to BRD4BD2, for which they have experimental evidence of dimerization, and to BRD4BD1, for which NMR data suggest it is monomeric. However, they do not provide any experimental validation for any of the other predicted dimers. The claim that "bromodomain dimerization may be more widespread" is speculative and based solely on computational predictions. The authors do acknowledge this limitation, but the strength of the claim in the abstract and discussion is not fully matched by the evidence.
- **Why it matters** The family-wide predictions are a significant part of the paper's broader impact. If the predictions are not validated, the claim of widespread dimerization is not established.
- **Resolution test** The authors should temper the claim in the abstract and discussion, or provide at least one additional experimental validation of a predicted dimer (e.g., for a bromodomain with a high ipTM score that has not been previously characterized). Alternatively, they could provide a more detailed analysis of the predicted interfaces, such as conservation analysis or comparison to known protein-protein interaction interfaces, to strengthen the case.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the percent change in diffusion that we measured upon increasing the BRD4BD2 concentration from 150 to 1000 µM (21.8%) is consistent with a monomer-to-dimer transition."
- **Evidence pointer** Results section "Hydrodynamic properties of the BRD4BD2 dimer from 15N relaxation, PFG-NMR, and SAXS"; Figure 3
- **Concern** The interpretation of the PFG-NMR diffusion data is complicated by the fact that both monomer and dimer are present in significant populations at both concentrations and interconvert during the diffusion delay. The authors acknowledge this, but they do not quantitatively model the diffusion data to extract the monomer and dimer populations. The observed 21.8% change in diffusion is compared to a theoretical expectation of ~20% for a monomer-to-dimer transition, but this comparison is only valid if the populations at the two concentrations are significantly different. Given the Kd of ~400 µM, the fraction of dimer at 150 µM is approximately 27%, while at 1000 µM it is approximately 71%. The observed change in diffusion should be interpreted in the context of this population shift, not as a simple monomer-to-dimer transition.
- **Why it matters** The diffusion data are used as supporting evidence for the dimerization model. If the interpretation is not quantitatively rigorous, the strength of this supporting evidence is diminished.
- **Resolution test** The authors should model the diffusion data using the known Kd and the populations of monomer and dimer at each concentration to extract the diffusion coefficients of the pure monomer and dimer. This would provide a more rigorous test of the dimerization model.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that the Kd is "near 400 µM" and the lifetime is "near 1 ms." These values are presented without error estimates. Given that the errors from the bootstrap analysis are reported in the main text (Kd = 391 ± 12 µM), it would be helpful to include the uncertainty in the abstract.
- **Required correction** Include the error estimates for Kd and lifetime in the abstract, or state that the values are approximate.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods section "15N-CPMG relaxation dispersion"
- **Evidence pointer** Methods section
- **Issue** The authors state that they used a modified form of the 15N ST-CW-CPMG pulse sequence but do not provide a reference for the original sequence. They also do not specify the exact modification.
- **Required correction** Provide a reference for the original pulse sequence and describe the modification in sufficient detail for reproduction.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section "BRD4BD2 dimerization detected by NMR spectroscopy"
- **Evidence pointer** Results section; Figure 1
- **Issue** The authors state that "residues exhibiting CSPs greater than or equal to 0.05 ppm include Q353, K395, R423, L424, S427, N428, Y430, Y432, N433, H437, A441, R444, K445, Q447, E451, F454, D459, and E460." It would be helpful to indicate the threshold used to define "significant" CSPs and how this threshold was chosen.
- **Required correction** State the threshold for significant CSPs and justify its choice.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods section "SAXS"
- **Evidence pointer** Methods section
- **Issue** The SAXS data analysis is described only briefly. The authors state that "the PRIMUS software suite was used for all subsequent analysis steps" but do not specify which analysis steps were performed (e.g., Guinier analysis, P(r) distribution, Kratky plot).
- **Required correction** Provide more detail on the SAXS data analysis, including the specific procedures used to extract the radius of gyration and any model fitting.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion
- **Evidence pointer** Discussion
- **Issue** The discussion of the potential functional relevance of dimerization in condensates is interesting but somewhat speculative. The authors state that "BRD4BD2 is additionally expected to be exposed to a high local effective concentration of acetylated lysine residues" but do not provide quantitative estimates of the concentrations involved.
- **Required correction** Provide a more quantitative discussion of the potential for dimerization to occur in condensates, or temper the speculation.

## Risk / unsupported claims
- The claim that "bromodomain dimerization may be more widespread than appreciated" is based solely on AlphaFold predictions and is not experimentally validated for any bromodomain other than BRD4BD2 and BRD2BD1.
- The claim that the AlphaFold3-predicted model of the BRD4BD2 dimer "involves similar interfacial residues" to the HADDOCK model is not quantitatively supported.
- The interpretation of the PFG-NMR diffusion data as evidence for a monomer-to-dimer transition is not quantitatively modeled and may be an oversimplification.
- The statement that the CPMG-detected exchange process is concentration-dependent is based on data at only two concentrations and a single magnetic field strength, which limits the robustness of the conclusion.