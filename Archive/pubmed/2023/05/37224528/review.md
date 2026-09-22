## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, materials and methods, results, discussion, data availability, and supplementary figure/table legends as referenced.
- **Assessment boundary** Scientific validity, technical soundness, interpretation of results, and support for claims, based solely on the provided manuscript text. No external data, supplementary files, or raw experimental records were available for inspection.
- **Shared manuscript claim summary** The authors identify a conserved motif (ConMot) within the intrinsically disordered linker of human MLH1, demonstrate that its deletion or scrambling abolishes DNA mismatch repair (MMR) activity, show that a cancer-associated variant (p.Arg385Pro) also inactivates MMR, and report that exogenous ConMot peptide can restore MMR activity in deletion and p.Arg385Pro mutant contexts. They further propose, based on AlphaFold2 predictions and mutational analysis, that ConMot interacts with the MLH1 C-terminal domain (CTD), potentially modulating endonuclease activity.
- **Visible evidence base** Western blot expression analysis (Figures 2A, 3C, 6C); in vitro MMR activity assays (Figures 2B, 3D, 4A-D, 5, 6D); sequence conservation analyses (Figures 1C-D, 3B, Supplementary Figure S1); circular dichroism and melting analysis (Supplementary Figure S2C-D); AlphaFold2 structural model (Figures 6A-B, 7, Supplementary Figure S5); peptide titration and complementation experiments (Figures 4, 5).
- **Missing materials affecting confidence** Supplementary figures S3-S6 and Supplementary Tables S1-S2 were referenced but not provided. Raw quantification data for Western blots and MMR assays, statistical details beyond P values, and full AlphaFold2 model confidence metrics were not available. Experimental details for peptide synthesis purity and controls were incomplete.

## Reviewer

- **Overall assessment** This manuscript presents a novel and potentially significant finding: a conserved motif within the disordered linker of human MLH1 that is essential for MMR activity. The identification of a functional element in a region previously considered non-functional is of considerable interest. The experimental approach is logical, combining bioinformatic analysis, mutagenesis, functional assays, and peptide complementation. However, several technical concerns and gaps in evidence limit the strength of the conclusions as currently presented. The peptide complementation data, while intriguing, require more rigorous controls and mechanistic interpretation. The proposed interaction with the MLH1 CTD is supported by only indirect evidence. Overall, the core finding is promising but the case is not fully established from the provided materials.

- **Who would be interested in the results, and why** Researchers in the fields of DNA repair, cancer genetics, and Lynch syndrome diagnostics would be the primary audience. The finding that a specific motif in a disordered region is functionally critical challenges current assumptions about MLH1 structure-function relationships. The demonstration that a cancer-associated variant in this motif impairs MMR has direct implications for variant classification and genetic counseling. The peptide rescue phenomenon, if confirmed, could open new avenues for therapeutic intervention, though this is speculative at present. The work also contributes to the broader understanding of short linear motifs (SLiMs) in disordered protein regions.

- **Major strengths**
  1. Identification of a previously unrecognized conserved motif (ConMot) in a region of MLH1 considered non-conserved and functionally inert.
  2. Clear demonstration that deletion or scrambling of ConMot abolishes MMR activity, establishing its functional importance.
  3. The finding that a cancer-associated variant (p.Arg385Pro) in ConMot impairs MMR provides a plausible mechanism for pathogenicity.
  4. The peptide complementation approach is creative and, if validated, offers a unique tool for dissecting ConMot function.
  5. The use of AlphaFold2 predictions to generate testable hypotheses about ConMot interactions is forward-looking.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "Deletion of the ConMot or scrambling of the motif abolished mismatch repair activity" and "the MMR defect of the ConMot variants could be restored by addition of a ConMot peptide containing the deleted sequence."
- **Evidence pointer** Figures 2B, 4A-D, 5; Materials and Methods "Mismatch repair assay"
- **Concern** The MMR assay relies on a single experimental readout (restoration of restriction site cleavage) without demonstration of assay linearity, reproducibility across biological replicates, or inclusion of a positive control peptide with known MMR-related activity. The peptide complementation experiments lack a dose-response analysis for the scrambled peptide control, and the specificity of the rescue effect is not fully established. The claim that the 20-mer peptide is inactive due to "target binding, not activation" being compromised is speculative without direct binding data.
- **Why it matters** The central conclusion that ConMot is vital for MMR and that peptide can rescue function depends entirely on the reliability and specificity of the MMR assay. If the assay has artifacts (e.g., peptide effects on restriction enzyme activity or DNA stability), the conclusions would be invalid. The mechanistic interpretation of peptide rescue requires demonstration of specific binding.
- **Resolution test** Provide full dose-response curves for both active and control peptides, include a known MMR-inhibitory peptide as a negative control, show assay linearity with respect to protein concentration, and present data from at least three independent biological replicates with statistical analysis. Direct binding studies (e.g., pull-down, surface plasmon resonance, or NMR) should be performed to demonstrate ConMot-target interaction.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** "Based on the experimental data and AlphaFold2 predictions, we suggest that the ConMot may bind close to the C-terminal MLH1-PMS2 endonuclease and modulate its activation during the MMR process."
- **Evidence pointer** Figures 6A-D, 7; Supplementary Figure S5
- **Concern** The proposed interaction between ConMot and the MLH1 CTD is based solely on AlphaFold2 predictions and indirect mutational analysis. The p.Arg385Tyr/p.Tyr750Arg double mutant experiment, while suggestive, shows only partial rescue (50.2% vs 22.4% activity) and does not demonstrate direct physical interaction. The AlphaFold2 model confidence for the disordered linker region is not reported, and the prediction of a structured interaction in a region predicted to be disordered is questionable. No biochemical evidence (co-immunoprecipitation, cross-linking, or structural data) is provided to support the proposed interaction.
- **Why it matters** The proposed mechanism of ConMot function is a key part of the manuscript's significance. Without direct evidence of the interaction, the model remains speculative. The partial rescue in the double mutant could be explained by other mechanisms (e.g., global conformational changes, altered protein stability).
- **Resolution test** Provide direct biochemical evidence of ConMot-CTD interaction, such as co-immunoprecipitation of full-length proteins, peptide pull-down assays, or cross-linking mass spectrometry. Alternatively, use hydrogen-deuterium exchange or limited proteolysis to demonstrate conformational changes. Report AlphaFold2 confidence metrics (pLDDT, PAE) for the ConMot-CTD interface.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation
- **Claim pointer** "The p.Arg385Pro alteration displayed a mismatch repair defect... suggesting that this variant is likely pathogenic and therefore causative for Lynch syndrome in this family."
- **Evidence pointer** Figure 2B; Discussion "Human variants in the ConMot"
- **Concern** The pathogenicity claim for p.Arg385Pro is based on a single functional assay in a heterologous overexpression system. The variant is listed as "uncertain significance" in clinical databases, and the authors acknowledge insufficient clinical data. The population frequency data (low frequency in Asian and European populations) is mentioned but not critically evaluated. The manuscript does not address whether the variant affects protein-protein interactions with PMS2, MSH2, or other MMR components beyond the MMR assay readout.
- **Why it matters** Classifying a variant as pathogenic has significant clinical implications for Lynch syndrome diagnosis and management. Overinterpretation of functional data without corroborating clinical evidence could lead to incorrect variant classification.
- **Resolution test** Provide additional functional evidence (e.g., MMR assay in a different cell line, biochemical characterization of the variant protein, interaction studies with PMS2) and discuss the variant in the context of ACMG/AMP classification guidelines. If possible, include co-segregation data or tumor characteristics from the original family.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "The ConMot peptide restores mismatch repair capacity of ΔConMot" and "the p.Arg385Pro variant abolishes the interaction of the MLH1-ConMot with its target binding site."
- **Evidence pointer** Figures 4B, 5; Materials and Methods "Mismatch repair assay"
- **Concern** The peptide complementation experiments use a 32-mer peptide at concentrations up to 75 μM, which is in large molar excess over the estimated 280 fmol MLH1 in the reaction. The specificity of the rescue is not fully established: the scrambled peptide control was only tested at a single concentration, and the 20-mer peptide was inactive but this could be due to loss of binding affinity rather than loss of activation function. The mechanism of peptide action (competitive vs. allosteric) is not addressed.
- **Why it matters** The peptide rescue is a novel and potentially important finding, but the mechanism is unclear. If the peptide acts by binding to a target site, it should compete with the endogenous ConMot; however, the lack of inhibition of wild-type MMR by excess peptide (Figure 4A) is inconsistent with a simple competitive model. This discrepancy needs to be addressed.
- **Resolution test** Perform competition experiments with wild-type MLH1 in the presence of increasing peptide concentrations to determine if inhibition occurs. Test the 20-mer peptide at higher concentrations to rule out insufficient dosing. Use a peptide with a single amino acid substitution in the conserved MVRTD core as an additional specificity control. Consider biophysical binding assays to determine KD and stoichiometry.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1A
- **Evidence pointer** Figure 1A
- **Issue** The PONDR analysis is mentioned but the figure is not described in sufficient detail. The reduced PONDR score in the ConMot region is stated but the magnitude and significance of this reduction are not quantified.
- **Required correction** Provide the PONDR score values or a statistical comparison of the ConMot region versus flanking linker regions. Clarify the threshold used to define "reduced disorder."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Materials and Methods "Mismatch repair assay"
- **Evidence pointer** Materials and Methods
- **Issue** The MMR assay description lacks details on the preparation of nuclear extracts, the specific activity of the restriction enzyme used for readout, and the quantification method for repair efficiency.
- **Required correction** Provide a more detailed protocol or reference to a prior publication with full methodological details. Specify how repair efficiency was quantified (e.g., densitometry, radioactive counting) and the number of replicates.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion "The potential role of the ConMot in MLH1 function"
- **Evidence pointer** Discussion
- **Issue** The discussion of the "handcuffing" experiments (reference 77) is brief and does not fully reconcile the differences between those results and the current findings. The authors state that N-terminal handcuffing conferred decreased MMR activity, but do not discuss how this relates to the proposed ConMot-CTD interaction.
- **Required correction** Expand the discussion to address how the handcuffing results support or conflict with the proposed model of ConMot function, and how the current findings refine the interpretation of those earlier experiments.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure 6D
- **Evidence pointer** Figure 6D
- **Issue** The statistical analysis for the double mutant rescue experiment is mentioned (P = 0.0028) but the statistical test used is not stated, and the number of independent experiments is not provided.
- **Required correction** Specify the statistical test used, the number of biological replicates, and whether the data met the assumptions of the test. Consider presenting individual data points alongside mean ± SD or SEM.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Supplementary Figure S2C-D
- **Evidence pointer** Supplementary Figure S2C-D
- **Issue** The circular dichroism and melting analysis of the ConMot peptide is described as showing "no evidence for secondary structure formation," but the raw data and analysis parameters (e.g., temperature range, buffer conditions, peptide concentration) are not provided in the main text.
- **Required correction** Provide the CD spectra and melting curves in the supplementary material with full experimental conditions. State the detection limit of the method for the peptide length used.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion "Human variants in the ConMot"
- **Evidence pointer** Discussion
- **Issue** The authors state that "the average age at cancer diagnosis is rather high in the family with the p.Arg385Pro variant" but do not provide the actual ages or family pedigree information.
- **Required correction** Provide the clinical details of the family, including ages at diagnosis and tumor spectrum, to support the suggestion of a milder phenotype. If this information is not available, temper the claim accordingly.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Materials and Methods "Bioinformatic analyses"
- **Evidence pointer** Materials and Methods
- **Issue** The AlphaFold2 model building is described but the specific parameters, input sequences, and quality metrics are not reported. The statement "max_recycles parameter which was increased from 3 to 12" is provided but no justification for this choice is given.
- **Required correction** Provide the AlphaFold2 version, input sequence boundaries, and output confidence metrics (pLDDT, PAE) for the regions discussed. Justify the choice of max_recycles and describe any manual curation of the model.

## Risk / unsupported claims
- The claim that ConMot peptide "restores" MMR activity in ΔConMot and p.Arg385Pro mutants is supported by the data shown, but the mechanism (binding vs. allosteric effect) is not established.
- The proposal that ConMot binds to the MLH1 CTD and modulates endonuclease activation is speculative and not directly supported by biochemical evidence.
- The suggestion that p.Arg385Pro is "likely pathogenic" for Lynch syndrome is based on limited functional data and requires corroborating clinical evidence.
- The statement that "the ConMot may bind close to the C-terminal MLH1-PMS2 endonuclease" is based on AlphaFold2 predictions without experimental validation.
- The claim that the 20-mer peptide is inactive due to "target binding, not activation, is compromised" is not directly tested.
- The assertion that "germline mutations of the human MMR gene MLH1 are the major cause of Lynch syndrome" is a general statement that is well-established in the literature but not specifically supported by data in this manuscript.
- The statement that "small coding variations in these regions found in patients are considered non-pathogenic" is presented as a general fact but is not systematically documented in this manuscript.