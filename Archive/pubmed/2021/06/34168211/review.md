## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results and discussion, conclusions, and methods
- **Assessment boundary** Scientific claims, methodological soundness, and interpretive validity of the intrinsic disorder analysis of the Chandipura virus proteome
- **Shared manuscript claim summary** The authors report a computational analysis of the dark proteome of Chandipura virus, identifying intrinsic disorder propensities across all five viral proteins, with the phosphoprotein showing the highest disorder level. They support this with molecular dynamics simulations and predict disorder-based binding regions (MoRFs) in all proteins.
- **Visible evidence base** Disorder prediction outputs from seven predictors, 2D disorder plots, MoRF predictions from four tools, homology models, and 500 ns MD simulations of the phosphoprotein
- **Missing materials affecting confidence** Supplementary figures referenced but not provided; raw prediction scores per residue not shown; MD simulation convergence metrics and force field parameters only partially described; no experimental validation data

## Reviewer
- **Overall assessment** This manuscript presents a straightforward computational analysis of intrinsic disorder in the Chandipura virus proteome. The work is technically competent but largely descriptive, applying established prediction tools to a relatively small set of five proteins. The central claim that phosphoprotein has the highest disorder propensity is well supported by the prediction data, and the MD simulations provide additional evidence for structural flexibility. However, the biological significance of these findings remains speculative, and the manuscript would benefit from a more critical interpretation of what the disorder predictions mean for CHPV biology. The study is suitable for a specialized journal but does not offer the conceptual advance expected for a high-impact publication.
- **Who would be interested in the results, and why** Researchers studying Chandipura virus pathogenesis and virology, particularly those interested in the structural biology of rhabdoviral proteins. The disorder predictions may also be of interest to the intrinsically disordered protein community as a case study of a viral dark proteome. However, the audience is likely narrow given the absence of experimental follow-up.
- **Major strengths** The study applies a comprehensive panel of seven disorder predictors, which strengthens the reliability of the predictions. The inclusion of MD simulations for the phosphoprotein adds a dynamic dimension beyond static predictions. The MoRF analysis across multiple tools provides a reasonable basis for identifying potential protein-protein interaction sites. The manuscript is clearly written and the figures are generally informative.
- **Major Concerns** The biological interpretation is largely speculative, with limited connection between predicted disorder and known CHPV biology. The MD simulations are performed on a homology model of uncertain quality, and the authors do not adequately address the limitations of this approach. The claim that disordered regions may serve as drug targets is not substantiated by any analysis of druggability. The comparison with related vesiculoviruses is superficial and does not explore functional conservation of disordered regions.
- **Minor Comments** Several typographical errors are present (e.g., "rgion" for region, "suggsting" for suggesting, "formaton" for formation). The figure legends could be more detailed regarding the color schemes used. The methods section for MD simulations lacks specific details on equilibration protocols and simulation temperature/pressure control.
- **Technical failings that need to be addressed before the case is established** The MD simulation analysis lacks convergence assessment and replica information. The homology model quality for the phosphoprotein is not evaluated with standard metrics. The authors do not provide a statistical comparison of disorder predictions across proteins beyond mean values.
- **Assessment against Nature-style criteria** Originality: The application of disorder prediction to CHPV is novel but methodologically incremental. Scientific importance: The findings are descriptive and do not reveal new biological mechanisms. Interdisciplinary readership: The work is primarily of interest to virologists and structural biologists, with limited broader appeal. Technical soundness: The prediction methodology is sound, but the MD simulation analysis has gaps. Readability for nonspecialists: The manuscript is accessible but assumes familiarity with disorder prediction concepts.
- **Recommendation posture** Supportive if technical concerns are resolved, but the manuscript would require substantial revision to strengthen the biological interpretation and address the methodological gaps in the MD simulation analysis.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that MD simulations up to 500 ns demonstrate the flexibility of the phosphoprotein and support its high disorder propensity.
- **Evidence pointer** Figure 8, Methods section "Modeling of CHPV protein structures"
- **Concern** The MD simulation analysis is presented without critical quality assessment. The authors do not report convergence of the simulations, such as RMSD stabilization over time or block averaging. The homology model used as the starting structure is built via threading with no template of high sequence identity, yet the authors do not evaluate model quality using standard metrics like QMEAN or MolProbity. The simulation protocol is described only briefly, lacking details on equilibration, temperature coupling, and pressure control. The interpretation that loss of secondary structure after 500 ns reflects intrinsic disorder is confounded by the possibility that the starting model was simply unstable due to modeling errors.
- **Why it matters** The MD simulation is a key piece of evidence supporting the central claim about phosphoprotein disorder. If the simulation is not technically reliable, the conclusion that the protein is flexible and disordered is weakened. The authors need to demonstrate that the observed structural changes are biologically meaningful rather than artifacts of poor model quality or inadequate simulation setup.
- **Resolution test** The authors should provide RMSD and RMSF plots with clear convergence assessment, report the quality scores of the homology model, and include details on simulation equilibration and ensemble sampling. Ideally, they should also run replicate simulations to confirm reproducibility of the observed structural transitions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Biological interpretation
- **Claim pointer** The authors state that the identified disordered regions and MoRFs in CHPV proteins may function as potential interacting domains and may serve as novel targets for disorder-based drug designs.
- **Evidence pointer** Conclusions section, Results sections for individual proteins
- **Concern** The biological significance of the disorder predictions is asserted rather than demonstrated. The authors do not map the predicted disordered regions to known functional sites in CHPV proteins, nor do they compare with experimental data on CHPV protein interactions. The suggestion that disordered regions are drug targets is speculative and not supported by any analysis of ligand binding potential or known druggable sites in viral proteins. The connection between predicted MoRFs and actual protein-protein interactions in the CHPV life cycle is not established.
- **Why it matters** The manuscript's broader relevance depends on the claim that these disorder predictions have functional implications. Without experimental or at least structural evidence linking the predicted disordered regions to CHPV biology, the study remains a purely computational exercise with limited translational value.
- **Resolution test** The authors should either temper their claims about functional significance or provide additional analysis, such as mapping disorder predictions onto known functional domains, comparing with experimentally characterized interactions in related viruses, or discussing specific testable hypotheses for how the disordered regions might contribute to CHPV replication or pathogenesis.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors report that the phosphoprotein has the highest disorder propensity with a mean PPID of 48.46%, and that the nucleoprotein and matrix protein are moderately disordered.
- **Evidence pointer** Table 1, Figure 2
- **Concern** The disorder predictions are presented as mean values across seven predictors, but the authors do not report the variability or agreement between individual predictors. Given that different disorder predictors can produce substantially different results, it is important to know whether the ranking of proteins by disorder propensity is robust across all predictors or driven by one or two outliers. The 2D disorder plot provides some information but does not show per-predictor values for each protein.
- **Why it matters** The central claim about phosphoprotein being the most disordered depends on the consistency of the prediction tools. If the ranking is not robust, the conclusion is weakened. The authors should demonstrate that their findings are not an artifact of predictor choice.
- **Resolution test** The authors should provide a table or figure showing the PPID values from each individual predictor for each protein, along with a measure of inter-predictor agreement (e.g., standard deviation or coefficient of variation). This would allow readers to assess the robustness of the disorder ranking.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and presentation
- **Affected element** Abstract
- **Evidence pointer** Abstract, last sentence
- **Issue** The abstract states that disordered regions "may also serve as novel targets for disorder-based drug designs," which is an overstatement given the purely computational nature of the study.
- **Required correction** Rephrase to indicate that these regions "could be explored as potential targets" or "warrant further investigation for drug design," avoiding definitive language.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical completeness
- **Affected element** Methods section
- **Evidence pointer** Methods, "Modeling of CHPV protein structures"
- **Issue** The methods state that the L protein was modeled using Swiss-model due to length limitations of IUPred, but no details are given on template selection, sequence identity, or model quality assessment.
- **Required correction** Provide the template PDB IDs, sequence identity percentages, and quality metrics (e.g., QMEAN, GMQE) for the L protein model.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 8
- **Evidence pointer** Figure 8C and 8D
- **Issue** The percentage of secondary structure elements is reported as approximately 19% after 500 ns, but the figure does not show the initial secondary structure content for comparison, making it difficult to assess the extent of structural loss.
- **Required correction** Include the initial secondary structure content in Figure 8C or state it in the text to allow quantitative comparison.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Language and grammar
- **Affected element** Throughout the manuscript
- **Evidence pointer** Multiple locations
- **Issue** Several typographical errors are present, including "rgion" (Results, phosphoprotein section), "suggsting" (Results, phosphoprotein section), and "formaton" (Results, phosphoprotein section).
- **Required correction** Proofread the manuscript carefully and correct all typographical errors.

## Risk / unsupported claims
- The claim that disordered regions in CHPV proteins may serve as drug targets is unsupported by any druggability analysis or experimental evidence.
- The assertion that the phosphoprotein's disorder is functionally linked to its role as a transcription-replication switch is speculative and not directly tested.
- The statement that the MD simulations demonstrate "flexibility" of the phosphoprotein is not fully supported without convergence analysis and replicate simulations.
- The biological relevance of the predicted MoRFs is asserted without experimental validation or comparison with known interaction data.
- The claim that the nucleoprotein's disordered regions have "implications in the RNA binding ability" is inferred from prediction alone and lacks experimental support.