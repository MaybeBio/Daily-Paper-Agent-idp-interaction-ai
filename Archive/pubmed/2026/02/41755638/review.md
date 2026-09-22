## Review setup
- **Input scope** Full manuscript text including abstract, introduction, materials and methods, results, discussion, and supplementary data references
- **Assessment boundary** Scientific content, methodological rigor, data interpretation, and claims as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors report that the intrinsically disordered transactivation domain (TAD) of N-myc interacts directly with the DNA-binding domain (DBD) of TFIIIC5, a subunit of the RNA Polymerase III assembly factor TFIIIC. They map two regions of N-myc (around residues 16-38 and 74-89) that bind to the TFIIIC5 DBD, determine that the acidic C-terminal plug of TFIIIC5 inhibits N-myc binding, and show that N-myc competes with DNA for binding to TFIIIC5. The study integrates NMR spectroscopy, hydrogen-deuterium exchange mass spectrometry, pull-down assays, isothermal titration calorimetry, fluorescence polarization, co-immunoprecipitation, X-ray crystallography, and AlphaFold modelling.
- **Visible evidence base** Results sections describing pull-down assays (Fig. 1C, 1E), NMR titrations (Fig. 2A-C, Supplementary Fig. S1), peptide pull-downs (Fig. 2D-E), HDX-MS (Fig. 3A-C), fluorescence polarization (Fig. 4B, 5A-D), ITC (Supplementary Fig. S2), X-ray crystallography (Supplementary Fig. S3, Supplementary Table S4), AlphaFold2/3 modelling (Fig. 8A-F, Supplementary Fig. S4-S5), EMSA (Fig. 7A-B), TRIC (Fig. 7E), and co-immunoprecipitation (Fig. 9)
- **Missing materials affecting confidence** Actual figures and supplementary figures not viewable; numerical values for KD determinations, statistical analyses, and error estimates not fully reported in text; detailed crystallographic data and refinement statistics not provided; NMR assignment completeness not described; full details of AlphaFold model validation not provided

## Reviewer
- **Overall assessment** This manuscript presents a comprehensive and methodologically diverse characterization of the interaction between the N-myc TAD and the TFIIIC5 DBD. The study addresses an important question in understanding how myc family oncoproteins interface with general transcription factors. The integrated approach combining multiple biophysical techniques is commendable and generally supports the central claim that N-myc binds to the DNA-binding surface of TFIIIC5. However, several concerns regarding quantitative rigor, validation of computational models, and the physiological relevance of the observed affinities need to be addressed before the case is fully established.
- **Who would be interested in the results, and why** Researchers studying myc oncoprotein function, transcription factor regulation, RNA Polymerase III biology, and intrinsically disordered protein interactions. The findings may also interest structural biologists studying protein-DNA binding surface competition and those investigating therapeutic targeting of myc interactions.
- **Major strengths** The study employs an impressive array of orthogonal techniques to map the interaction interface. The identification of two distinct binding regions in N-myc and the demonstration that the acidic plug of TFIIIC5 regulates N-myc binding provides mechanistic insight. The competition experiments between N-myc and DNA are conceptually important. The use of AlphaFold predictions alongside experimental validation is appropriate, and the authors appropriately caution against overinterpretation of computational models.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative binding data), R1-M2 (AlphaFold model validation), R1-M3 (crystallographic evidence), R1-M4 (cellular validation)
- **Assessment against Nature-style criteria** Originality: The finding that a myc family member binds to the DNA-binding surface of a TFIIIC subunit is novel and extends understanding of myc-TFIIIC interactions. Scientific importance: The work has potential significance for understanding myc-driven transcriptional regulation and mRNA quality control, though the broader physiological implications remain speculative. Interdisciplinary readership: The topic bridges cancer biology, transcription regulation, and structural biology, which could attract readers across these fields. Technical soundness: The methodology is generally sound, but quantitative rigor and validation of computational models require strengthening. Readability for nonspecialists: The manuscript is clearly written and accessible, though some sections assume familiarity with biophysical techniques.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding quantitative binding data, validation of AlphaFold models, and demonstration of physiological relevance.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative binding data
- **Claim pointer** The authors report KD values of 0.060 μM for MB0 and 1.1 μM for the 61-89 peptide binding to TFIIIC5 DBD ΔΔ, and an approximately 8-fold reduction for MB0 and 20-fold reduction for the 61-89 peptide when the acidic plug is present.
- **Evidence pointer** Results section "N-myc TAD binds to TFIIIC5 DBD ΔΔ with high affinity", Fig. 4B, Fig. 6C-D, Supplementary Fig. S2
- **Concern** The KD values are reported with minimal statistical detail. It is unclear how many independent replicates were performed for each measurement, what the error bars represent, and whether the reported values are means with standard deviations or standard errors. The ITC data are only presented in supplementary material, and the stoichiometry is stated to be "very close to 1:1" without providing the actual fitted value. For the FP assays, the fitting model is described, but no goodness-of-fit parameters are reported. The claim that the acidic plug reduces affinity by 8-fold and 20-fold for the two peptides needs supporting statistical analysis to establish significance.
- **Why it matters** Quantitative binding parameters are central to the manuscript's claims about the relative affinities of the two N-myc regions and the regulatory role of the acidic plug. Without proper statistical reporting, the robustness of these conclusions cannot be evaluated.
- **Resolution test** Provide the number of independent replicates, report KD values with appropriate error estimates and confidence intervals, include goodness-of-fit statistics for all binding curves, and perform appropriate statistical tests to compare KD values between conditions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** AlphaFold model validation
- **Claim** The authors state that "AlphaFold modelling predicts with high-confidence a binding mode for the higher affinity N-myc motif that overlaps with the predicted intramolecular binding site of the C-terminal acidic plug of TFIIIC5."
- **Evidence pointer** Results section "Modelling the N-myc:TFIIIC5 interaction", Fig. 8A-F, Supplementary Fig. S4-S5
- **Concern** The manuscript reports ipTM scores for the AlphaFold2 models but does not provide a comprehensive assessment of model reliability. The authors note that "the binding modes of N-myc were variable" in AlphaFold3 modelling of the τA complex, yet the AlphaFold2 models are presented as plausible binding modes. The criteria for selecting the "highest ranked" models are not fully described, and it is unclear how many of the 20 calculated models converged on similar binding modes. The statement that the 19-38 peptide model is "more likely to be correct due to the consistency of the prediction" needs quantitative support, such as the fraction of models that agreed.
- **Why it matters** The computational models are used to interpret the experimental data and to propose a structural mechanism for the interaction. If the models are not adequately validated, the mechanistic conclusions drawn from them are weakened.
- **Resolution test** Provide a more detailed analysis of the AlphaFold model ensemble, including the distribution of predicted binding modes, per-residue confidence scores (pLDDT and PAE), and a clear description of how model quality was assessed. Consider validating key predicted contacts through mutagenesis experiments.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Crystallographic evidence
- **Claim** The authors report determining the crystal structure of the TFIIIC5 DBD ΔΔ to 2.6 Å resolution, and state it is similar to the equivalent domain in S. pombe.
- **Evidence pointer** Results section "Modelling the N-myc:TFIIIC5 interaction", Supplementary Fig. S3, Supplementary Table S4
- **Concern** The crystallographic data are only mentioned briefly, with the structure determination described in a single sentence. No details are provided regarding data collection statistics, refinement statistics, or model quality indicators such as R-factors, Ramachandran statistics, or B-factors. The statement that the structure is "very similar" to the S. pombe structure is supported only by an average backbone RMSD of 1.1 Å, but the number of residues used for the superposition and the sequence identity between the two domains are not reported.
- **Why it matters** The crystal structure serves as the basis for interpreting the AlphaFold models and for understanding the structural context of the N-myc binding site. Without proper crystallographic validation, the reliability of the structural conclusions cannot be assessed.
- **Resolution test** Provide complete crystallographic data collection and refinement statistics in Supplementary Table S4, including resolution limits, completeness, R-work/R-free, RMSD for bonds and angles, and Ramachandran statistics. Include a clear description of the structure determination and validation process.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Cellular validation
- **Claim** The authors state that "Mutation in MB0 reduces the TFIIIC5 interaction with N-myc in cells" based on co-immunoprecipitation experiments showing a ~50% reduction for the F28A-Y29A variant.
- **Evidence pointer** Results section "Mutation in MB0 reduces the TFIIIC5 interaction with N-myc in cells", Fig. 9
- **Concern** The co-immunoprecipitation experiment is described with a single P-value (P = 0.0054), but the number of independent biological replicates is not stated. The manuscript does not report whether the F28A-Y29A mutation affects N-myc protein stability or expression levels, which could confound the interpretation. Additionally, the ~50% reduction in co-immunoprecipitation is described as "consistent with" the in vitro data showing a 3-fold affinity reduction, but the relationship between these two observations is not quantitatively established.
- **Why it matters** The cellular validation is important for establishing the physiological relevance of the interaction. Without proper controls and replicate information, the strength of this validation is unclear.
- **Resolution test** Report the number of independent biological replicates, include Western blot quantification with appropriate loading controls, assess whether the F28A-Y29A mutation affects N-myc protein levels, and provide a more detailed statistical analysis of the co-immunoprecipitation data.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Experimental detail
- **Affected element** NMR spectroscopy methods
- **Evidence pointer** Materials and methods section "NMR titrations"
- **Issue** The NMR experiments are described, but the manuscript does not state how many residues were assigned for the N-myc constructs, what fraction of the sequence was observable, or how the intensity ratios were calculated for residues that may overlap.
- **Required correction** Provide details on the completeness of backbone assignments for the N-myc constructs used, and describe the criteria for including or excluding peaks in the intensity ratio analysis.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** HDX-MS results
- **Evidence pointer** Results section "Hydrogen-deuterium exchange mass spectrometry suggests two binding hotspots on TFIIIC5", Fig. 3A-C
- **Issue** The HDX-MS data are described qualitatively, with "significant" protection or deprotection mentioned, but the threshold for significance and the magnitude of the observed changes are not reported.
- **Required correction** Provide the significance thresholds used in the Deuteros analysis, and report the magnitude of deuterium uptake differences for the key peptides discussed.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Methodological consistency
- **Affected element** Peptide pull-down assays
- **Evidence pointer** Results section "N-myc uses two linear peptide sequences to bind TFIIIC5 DBD ΔΔ", Fig. 2D-E
- **Issue** The peptide pull-down assays use biotinylated peptides spanning the N-myc TAD, but the manuscript does not specify the peptide concentrations used or whether the assays were performed under conditions that would allow quantitative comparison between peptides.
- **Required correction** Report the peptide concentrations used in the pull-down assays and clarify whether the results are qualitative or quantitative.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion of competition mechanism
- **Evidence pointer** Discussion section
- **Issue** The authors propose that N-myc competes with DNA for TFIIIC5 binding, but the discussion of how this competition might be regulated in cells is speculative and does not consider potential allosteric effects or post-translational modifications.
- **Required correction** Acknowledge the speculative nature of the competition model and discuss alternative mechanisms that could regulate the N-myc:TFIIIC5 interaction in cells.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction and Discussion
- **Evidence pointer** Introduction, Discussion
- **Issue** The manuscript does not discuss recent structural studies of myc family members bound to other partners, which could provide context for the proposed binding mode.
- **Required correction** Add a brief discussion of relevant structural studies of myc interactions to place the current findings in a broader context.

## Risk / unsupported claims
- The claim that the AlphaFold2 model of the N-myc 19-38:TFIIIC5 interaction is "more likely to be correct" than the 75-89 model is not fully supported by the data presented, as the manuscript does not provide a quantitative comparison of model convergence or confidence across the 20 calculated models.
- The statement that the endothermic heat signature in ITC "may be due to conformational change in the domain upon binding" is speculative and not directly supported by experimental evidence.
- The physiological relevance of the observed KD values (60 nM for MB0) is discussed without comparison to cellular concentrations of N-myc or TFIIIC5, making the significance of this affinity unclear.
- The claim that the F28A-Y29A mutation reduces co-immunoprecipitation by ~50% "consistent with" the in vitro 3-fold affinity reduction is not quantitatively justified, as the relationship between in vitro affinity changes and cellular co-immunoprecipitation efficiency is not established.
- The discussion of how the N-myc:TFIIIC5 interaction might function in mRNA quality control is acknowledged as speculative by the authors, but the speculative nature of this model should be more prominently flagged in the abstract.