## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) as provided
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and technical soundness based solely on the supplied text
- **Shared manuscript claim summary** The authors report that the FXR N-terminal domain (NTD) engages in interdomain interactions with the LBD and directly binds coregulator proteins. They identify a novel SXXLF motif (SENLF) in the NTD that mediates these interactions, supported by luciferase reporter assays, mammalian two-hybrid (M2H) assays, and molecular dynamics (MD) simulations. Mutation of this motif to SENAA alters conformational dynamics and allosteric coupling in FXR.
- **Visible evidence base** Figures 1, 3, and 4 are referenced in the text; methods for cloning, luciferase assays, M2H assays, and MD simulations are described
- **Missing materials affecting confidence** Figure panels and actual data values are not shown; statistical details for M2H assays are incomplete; MD simulation parameters for heterodimer systems are partially described; no structural validation (e.g., NMR, crystallography) is provided; coregulator interaction data are limited to M2H without orthogonal biochemical validation

## Reviewer
- **Overall assessment** The manuscript addresses an important and understudied aspect of nuclear receptor biology, namely the functional role of the intrinsically disordered NTD in FXR. The identification of a novel SXXLF motif is potentially significant, as it expands the known repertoire of NR interaction motifs. However, the evidence presented is largely based on cell-based reporter assays and computational simulations, with limited orthogonal biochemical validation. Several claims, particularly regarding direct coregulator binding and the mechanistic basis of the observed effects, are not fully established from the provided data. The manuscript would benefit from additional experimental support, including direct binding assays and more detailed structural or biophysical characterization.
- **Who would be interested in the results, and why** Researchers in the nuclear receptor field, particularly those studying FXR biology, intrinsically disordered proteins, and protein-protein interaction motifs. The findings may also be of interest to investigators working on coregulator recruitment mechanisms and allosteric regulation in transcription factors, as well as those developing therapeutic modulators targeting FXR.
- **Major strengths** The study addresses a previously unexplored aspect of FXR biology, namely the function of the NTD. The identification of a novel SXXLF motif is a potentially important contribution. The combination of cell-based assays with MD simulations provides a multi-pronged approach. The authors appropriately acknowledge limitations and propose future directions.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (direct coregulator binding not demonstrated), R1-M2 (M2H assay limitations), R1-M3 (MD simulation support for functional claims is weak), R1-M4 (incomplete statistical reporting)
- **Assessment against Nature-style criteria**  
  *Originality*: The identification of a novel SXXLF motif in the FXR NTD is original and extends the known repertoire of NR interaction motifs. However, the concept of NTD-mediated coregulator interactions is already established in other NRs, so the novelty is incremental rather than paradigm-shifting.  
  *Scientific importance*: The findings have potential importance for understanding FXR regulation and NR biology more broadly, but the current evidence does not fully establish the physiological relevance of the identified motif.  
  *Interdisciplinary readership*: The topic is of interest to structural biologists, biochemists, and molecular endocrinologists, but the narrow focus on FXR may limit broader appeal.  
  *Technical soundness*: The experimental approaches are generally appropriate, but the lack of direct binding assays and incomplete statistical reporting weaken the technical foundation.  
  *Readability for nonspecialists*: The manuscript is clearly written and accessible, with appropriate context provided for the significance of the findings.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding direct evidence for coregulator binding and more rigorous statistical and methodological reporting.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "We also observe that the NTD interacts directly with coregulator proteins" (Abstract); "Peptides from nuclear receptor coregulators interact with the FXR NTD" (Results section heading)
- **Evidence pointer** Results section "Peptides from nuclear receptor coregulators interact with the FXR NTD"; Figure 3F
- **Concern** The claim of direct NTD-coregulator interaction is based solely on M2H assays, which measure protein-protein interactions in a cellular context but do not demonstrate direct physical binding. No pull-down assays, surface plasmon resonance, isothermal titration calorimetry, or other direct binding experiments are described. The M2H assay is indirect and can be influenced by bridging factors or non-specific effects.
- **Why it matters** The central claim of the manuscript is that the NTD directly interacts with coregulators. Without direct biochemical evidence, this claim is not fully supported. The distinction between direct and indirect interactions is critical for understanding the mechanism of action.
- **Resolution test** Provide direct binding data, such as GST pull-down assays with purified NTD and coregulator peptides, or biophysical measurements (e.g., ITC, SPR) demonstrating a direct interaction with defined affinity.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental design
- **Claim pointer** "Using mutagenesis, mammalian two-hybrid assays and molecular dynamics simulations, we identify and validate a novel SXXLF motif in the NTD which mediates interactions with both coregulators and the ligand binding domain" (Abstract)
- **Evidence pointer** Results sections "The FXR NTD interacts with other FXR domains" and "A novel SXXLF motif in the FXR NTD mediates interactions with the LBD"; Figures 1C-D, 3A-E
- **Concern** The M2H assay is used to draw conclusions about interdomain interactions, but the assay measures interactions between fusion proteins in a cellular context and may not accurately reflect intramolecular interactions within the full-length receptor. The authors do not discuss potential artifacts of the M2H system, such as overexpression effects, fusion protein conformational changes, or the possibility that the observed interactions are mediated by endogenous cellular factors. Additionally, the M2H assay does not provide quantitative binding affinities or kinetic information.
- **Why it matters** The conclusions about interdomain interactions and the role of the SENLF motif depend heavily on the M2H assay. If the assay has systematic artifacts, the conclusions may be incorrect. The lack of orthogonal validation (e.g., FRET, co-immunoprecipitation with full-length receptor) weakens the case.
- **Resolution test** Validate key interactions using an orthogonal method, such as co-immunoprecipitation of full-length FXR with coregulators, or FRET-based assays in cells. Provide quantitative data where possible.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "Mutation of the motif induces large changes in conformational and allosteric coupling in FXR" (Abstract); "SXXLF mutation influences interdomain contact and coupling in simulations" (Results section heading)
- **Evidence pointer** Results section "SXXLF mutation influences interdomain contact and coupling in simulations"; Figure 4
- **Concern** The MD simulation results are used to support claims about conformational changes and allosteric coupling, but the simulations are based on AlphaFold3-predicted structures, which are not experimentally validated. The authors do not provide convergence analysis, error estimates, or validation of the force field parameters for the specific system. The functional significance of the observed distance changes is inferred but not directly tested experimentally. The simulations are performed on monomeric and heterodimeric models, but the physiological relevance of these models is not fully discussed.
- **Why it matters** The claim that the SENLF mutation induces large conformational changes is a key part of the mechanistic model. If the simulations are not robust or the models are not representative, this claim is not supported. The lack of experimental validation of the predicted conformational changes is a significant gap.
- **Resolution test** Provide evidence of simulation convergence and robustness (e.g., block averaging, multiple independent runs). Validate key predicted conformational changes experimentally, for example, through hydrogen-deuterium exchange mass spectrometry, cross-linking, or FRET-based conformational sensors.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Statistical rigor
- **Claim pointer** "Compared to WT-FXR, a significant decrease in response (> 50%) is observed in ΔNTD for all ligands" (Results section)
- **Evidence pointer** Results section "The FXR NTD interacts with other FXR domains"; Figure 1B
- **Concern** The statistical analysis is incompletely described. The authors state that "P-values were calculated using two-way ANOVA with Dunnett's multiple comparisons test" but do not report the number of independent experiments, the specific p-values for each comparison, or the effect sizes. The significance thresholds are also unusual (e.g., p > 0.1234 is listed as "ns"), which is not a standard threshold. The figure legends are not provided, so it is unclear what the error bars represent.
- **Why it matters** Without complete statistical reporting, the reader cannot assess the robustness of the reported differences. The unusual significance thresholds raise questions about the appropriateness of the statistical analysis.
- **Resolution test** Provide complete statistical details, including exact p-values, confidence intervals, effect sizes, and the number of independent biological replicates. Use standard significance thresholds (e.g., p < 0.05) and clearly describe the statistical tests used.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section "The FXR NTD interacts with other FXR domains"
- **Evidence pointer** Figure 1C-D
- **Issue** The description of the M2H assay constructs is brief. It is unclear whether the NTD constructs include the full NTD (residues 1-119) or only a portion, and whether the LBD construct includes the hinge region. The authors state that "the presence of the DBD led to a small but significant increase in fold-change" but do not provide the magnitude of this increase or the statistical significance.
- **Required correction** Provide a clear description of all constructs used, including residue ranges and fusion partners. Report the magnitude of the observed effects and the corresponding statistical values.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results section "A novel SXXLF motif in the FXR NTD mediates interactions with the LBD"
- **Evidence pointer** Figure 3A-E
- **Issue** The sequence alignment shown in Figure 3A is not described in detail. It is unclear which species are included and whether the SENLF motif is conserved across species. The authors state that "SENLF is similar to FQNLF in the NTD of the AR" but do not provide a quantitative comparison or discuss the significance of the similarity.
- **Required correction** Describe the sequence alignment in detail, including the species included and the degree of conservation. Provide a more detailed comparison with known motifs in other NRs.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section "SXXLF mutation influences interdomain contact and coupling in simulations"
- **Evidence pointer** Figure 4
- **Issue** The description of the MD simulation analysis is brief. The authors mention "contact analysis" and "correlation" but do not define these terms or describe the specific methods used. The criteria for identifying significant conformational changes (distance < 20 Å, change > 15 Å) are arbitrary and not justified.
- **Required correction** Provide a more detailed description of the simulation analysis methods, including how contacts and correlations were defined and calculated. Justify the criteria used to identify significant conformational changes.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Evidence pointer** Methods section "Molecular dynamics simulations"
- **Issue** The methods for MD simulations are incomplete. The authors state that simulations were run on Anton 3 for the heterodimer but do not provide details on the simulation temperature, pressure, or the length of equilibration. The force field used is mentioned (ff14SB) but not the water model or ion parameters. The number of replicates and the total simulation time are not clearly stated.
- **Required correction** Provide complete details of the MD simulation protocol, including all parameters, simulation lengths, and the number of replicates.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion section
- **Evidence pointer** Location not provided
- **Issue** The discussion of the physiological relevance of the SENLF motif is speculative. The authors suggest that "there may be undiscovered motifs involved in critical NR functions" but do not provide specific predictions or testable hypotheses.
- **Required correction** Provide more specific predictions or hypotheses that could be tested in future studies, and discuss the potential physiological implications of the findings in more concrete terms.

## Risk / unsupported claims
- The claim that the NTD "interacts directly" with coregulator proteins is not supported by direct binding data; only M2H assays are presented.
- The claim that the SENLF motif "mediates interactions with both coregulators and the ligand binding domain" is based on M2H assays and MD simulations, but the M2H data for coregulator interactions are not shown in detail, and the MD simulations are based on unvalidated AlphaFold3 models.
- The claim that "mutation of the motif induces large changes in conformational and allosteric coupling" is based solely on MD simulations and is not experimentally validated.
- The statement that "the NTD is a major contributor to transactivation in FXR" is supported by the ΔNTD data, but the magnitude of the effect and the statistical significance are not fully reported.
- The suggestion that "SENLF may preferentially interact with SRC-1 and SRC-2 but not P300" is based on a single experiment and requires further validation.