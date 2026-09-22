## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, materials and methods, and conclusions
- **Assessment boundary** Scientific validity of the purification methodology, inhibitor screening approach, binding affinity measurements, and the interpretation of results
- **Shared manuscript claim summary** The authors report a streamlined purification method for full-length SARS-CoV-2 nucleocapsid protein free of nucleic acid contamination, and identify Light Green SF Yellowish as a potential inhibitor with higher affinity for eukaryotic-expressed N protein (KD = 119.7 nM) compared to prokaryotic-expressed N protein (KD = 19.9 × 10³ nM)
- **Visible evidence base** Figures 1-12, Tables 1, Supplementary Figures S1-S3, methods descriptions
- **Missing materials affecting confidence** Raw BLI sensorgram data, statistical analysis details, replicate numbers, negative control data for BLI experiments, purity quantification data, nucleic acid quantification data, cell-based antiviral activity data

## Reviewer
- **Overall assessment** The manuscript addresses a relevant technical challenge in SARS-CoV-2 N protein purification and presents a potentially useful methodological contribution. However, the inhibitor screening component is substantially underdeveloped. The claim that Light Green SF Yellowish is a "potential inhibitor" of SARS-CoV-2 is not supported by the data presented, as no functional antiviral assays were performed. The binding affinity comparison between prokaryotic and eukaryotic N protein is interesting but lacks mechanistic validation. The purification method itself appears reasonable, though quantitative assessments of purity and nucleic acid removal are limited.
- **Who would be interested in the results, and why** Researchers working on SARS-CoV-2 structural biology, nucleocapsid protein biochemistry, and antiviral drug development would find the purification methodology potentially useful. The observation that post-translational modifications affect small molecule binding affinity is of general interest to the drug screening community, as it highlights a potential pitfall in using prokaryotically expressed proteins for inhibitor screening.
- **Major strengths** The purification strategy combining high salt lysis, PEI precipitation, ammonium sulfate precipitation, and nickel affinity chromatography is logical and addresses a known challenge in N protein biochemistry. The comparison between prokaryotic and eukaryotic expression systems for inhibitor binding is a valuable conceptual contribution. The use of both virtual screening and experimental validation (BLI) represents an appropriate screening workflow.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** **Originality**: Moderate. The purification approach combines known techniques in a new sequence, but the individual components are established. The observation regarding differential binding affinity based on expression system is novel. **Scientific importance**: Moderate. The work addresses a practical need but does not provide fundamental new insights into N protein biology or antiviral mechanisms. **Interdisciplinary readership**: Limited. The work is primarily of interest to structural biologists and drug screening specialists. **Technical soundness**: The purification methodology appears technically sound, but the inhibitor characterization is incomplete. The BLI experiments lack critical controls and replicates. **Readability for nonspecialists**: The manuscript is generally readable, though some sections assume familiarity with protein purification terminology.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that Light Green SF Yellowish is a "potential inhibitor" of SARS-CoV-2 N protein and represents "a novel therapeutic candidate for COVID-19"
- **Evidence pointer** Section 2.8, Table 1, Figure 9
- **Concern** The claim that LGSFY is a potential inhibitor of SARS-CoV-2 is not supported by any functional data. The manuscript only presents binding affinity measurements from BLI experiments. No antiviral assays, viral replication inhibition studies, or cell-based experiments were performed. Binding to a protein in vitro does not constitute inhibition of viral function. The conclusion that LGSFY "can specifically bind these free nucleocapsid proteins, inhibiting the formation of ribonucleoprotein complexes and ultimately suppressing viral replication" is speculative and not experimentally validated.
- **Why it matters** The central therapeutic claim of the manuscript rests on the identification of an inhibitor. Without functional validation, the compound cannot be described as an inhibitor, only as a binding ligand. This overinterpretation could mislead readers and the broader scientific community.
- **Resolution test** Provide cell-based antiviral assays (e.g., SARS-CoV-2 infection models) demonstrating that LGSFY inhibits viral replication. Alternatively, provide biochemical assays showing that LGSFY disrupts N protein-RNA interactions in a functional assay system.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical rigor
- **Claim pointer** The manuscript claims a binding affinity of KD = 19.9 × 10³ nM for prokaryotic N protein and KD = 119.7 nM for eukaryotic N protein
- **Evidence pointer** Section 2.8, Table 1, Figure 9
- **Concern** The BLI experiments lack essential details and controls. No information is provided on the number of replicates, error values, or statistical significance of the difference between the two KD values. The sensorgram data are not shown, making it impossible to assess the quality of the binding curves. Additionally, no negative control compounds were tested to demonstrate binding specificity. The concentration range of LGSFY used in the experiments is not specified. Without these details, the reliability of the reported KD values cannot be evaluated.
- **Why it matters** The differential binding affinity between prokaryotic and eukaryotic N protein is a key finding of the manuscript. If the experimental design is flawed or the measurements are not reproducible, this conclusion is invalid.
- **Resolution test** Provide full BLI sensorgrams, include at least three independent replicates with standard deviations, test a negative control compound, and specify the concentration range of the analyte used.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that post-translational modifications, specifically glycosylation at N47, enhance the binding affinity of LGSFY to the N protein
- **Evidence pointer** Section 2.9, Figures 10-12
- **Concern** The molecular modeling results are presented as supporting evidence for the enhanced binding affinity of LGSFY to glycosylated N protein. However, the docking scores (−7.60 vs −6.57 kcal/mol) show a modest difference that may not be significant given the inherent limitations of docking calculations. The claim that glycosylation "may facilitate the association between the N protein and the ligand through conformational remodeling" is presented without experimental validation. No mutagenesis studies were performed to confirm the role of N47 glycosylation in LGSFY binding. The eukaryotic N protein used in BLI experiments was purchased from a commercial source, and its glycosylation status was not verified.
- **Why it matters** The mechanistic explanation for the differential binding affinity is a central claim of the manuscript. Without experimental validation, the proposed mechanism remains speculative.
- **Resolution test** Perform site-directed mutagenesis of N47 to eliminate the glycosylation site and compare LGSFY binding affinity between wild-type and mutant proteins. Alternatively, use enzymatic deglycosylation of the eukaryotic N protein and measure binding affinity before and after treatment.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical rigor
- **Claim pointer** The manuscript claims that a "pure full-length nucleocapsid protein without nucleic acid contamination was obtained"
- **Evidence pointer** Section 2.6, Figure 4, Figure 7
- **Concern** The purity of the final N protein preparation is assessed only by SDS-PAGE and silver staining. No quantitative data are provided for nucleic acid removal efficiency. The A260/A280 ratio, a standard measure of nucleic acid contamination in protein preparations, is not reported. The silver staining shown in Figure 4 is qualitative and does not provide a detection limit for residual nucleic acids. The claim of "without nucleic acid contamination" requires more rigorous validation.
- **Why it matters** The purification method is a primary contribution of the manuscript. If the nucleic acid removal is not quantitatively demonstrated, the methodological advance is not established.
- **Resolution test** Provide A260/A280 ratios before and after purification, quantify residual nucleic acids using a sensitive method (e.g., PicoGreen assay or qPCR), and report the detection limit of the silver staining method.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.4, Figure 3
- **Evidence pointer** Figure 3
- **Issue** The description of the PEI concentration optimization is unclear. The text states that "0.15% PEI resulted in the best nucleic acid precipitation effect" but does not explain why higher PEI concentrations decreased precipitation efficiency.
- **Required correction** Provide a mechanistic explanation for the observed decrease in nucleic acid precipitation at higher PEI concentrations, or acknowledge this as an empirical observation.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 3.7
- **Evidence pointer** Section 3.7
- **Issue** The BLI experimental section lacks details on the concentration of N protein loaded onto the biosensors, the range of LGSFY concentrations tested, and the fitting model used for KD calculation.
- **Required correction** Provide complete experimental parameters for the BLI experiments, including loading concentration, analyte concentration range, and data fitting methodology.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Section 2.8
- **Evidence pointer** Table 1
- **Issue** The manuscript states that LGSFY "exhibited a good affinity for the N protein" based on a KD of 19.9 × 10³ nM for the prokaryotic protein. This value is in the micromolar range, which is generally considered weak binding for a small molecule-protein interaction.
- **Required correction** Provide context for the binding affinity values by comparing them to known N protein inhibitors or typical small molecule-protein interactions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.9, Figure 11
- **Evidence pointer** Figure 11
- **Issue** The structural alignment figure is not clearly described. It is unclear which structures are being compared and what conformational changes are being highlighted.
- **Required correction** Provide a clear figure legend explaining the structural comparison and highlight the specific conformational differences between modified and unmodified N protein.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 2.7
- **Evidence pointer** Section 2.7
- **Issue** The virtual screening results are only briefly mentioned. The top 20 compounds are listed in supplementary figures, but no information is provided on the selection criteria for LGSFY as the lead candidate for experimental validation.
- **Required correction** Provide the scoring criteria and selection rationale for choosing LGSFY from the virtual screening hits.

## Risk / unsupported claims
- The characterization of LGSFY as a "potential inhibitor" and "novel therapeutic candidate for COVID-19" is unsupported by functional antiviral data
- The claim that LGSFY can "inhibit the formation of ribonucleoprotein complexes and ultimately suppress viral replication" is speculative and not experimentally demonstrated
- The mechanistic explanation for differential binding affinity based on glycosylation is not experimentally validated
- The claim of obtaining N protein "without nucleic acid contamination" is not quantitatively supported
- The statement that the purified N protein "exhibited significantly enhanced accessibility for structural and functional virological studies" is not directly demonstrated with comparative data
- The therapeutic relevance of the binding affinity difference between prokaryotic and eukaryotic N protein is overstated without functional correlation