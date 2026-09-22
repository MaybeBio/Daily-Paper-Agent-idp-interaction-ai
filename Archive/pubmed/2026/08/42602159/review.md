## Review setup
- **Input scope** Full manuscript text (title, abstract, introduction, methods, results, discussion, conclusion, supplementary references)
- **Assessment boundary** Scientific soundness, methodological rigor, validity of conclusions relative to evidence, and suitability for a molecular neuroscience readership
- **Shared manuscript claim summary** The authors use an integrated computational pipeline to identify two PINK1 missense mutations (T313M and L347P) and characterize their effects on PINK1–ubiquitin binding via docking, molecular dynamics, and MM/PBSA analyses, concluding that these mutations impair phospho-Ser65 ubiquitin recognition and thus contribute to mitophagy dysfunction in autosomal recessive Parkinson's disease.
- **Visible evidence base** Computational predictions only: SIFT, PolyPhen-2, EVE, SNP&GO, Missense3D, CUPSAT, HADDOCK docking, 200-ns MD simulations (3 replicates), MM/PBSA, PCA, DCCM, IUPred/ANCHOR disorder predictions, PRALINE conservation analysis, PrankWeb pocket prediction
- **Missing materials affecting confidence** No experimental validation (biochemical, cellular, or animal); no raw MD trajectory data or convergence metrics; no force field validation details; no docking scoring function details; no information on how phosphorylation was modeled; no structural coordinates for the modeled complexes; no statistical significance testing for MD differences; no information on how the "phosphorylated state" of PINK1 was constructed

## Reviewer

### Overall assessment
This manuscript presents a purely computational analysis of two PINK1 mutations and their potential impact on PINK1–ubiquitin interactions. The pipeline is extensive and the authors have employed a reasonable suite of bioinformatics tools. However, the central claim that these mutations impair phospho-Ser65 ubiquitin recognition is not directly tested. The docking and MD simulations model PINK1–ubiquitin binding, but the key phospho-Ser65 interaction is inferred rather than demonstrated. The MM/PBSA results explicitly show no significant difference in binding free energy between wild-type and mutants, which directly contradicts the title's claim of a "vital molecular perturbation" at the phospho-Ser65 recognition point. The manuscript would benefit from substantial revision to align its conclusions with the actual evidence presented.

### Who would be interested in the results, and why
Researchers studying PINK1/Parkin-mediated mitophagy, computational biologists interested in variant effect prediction, and clinicians or geneticists working on early-onset Parkinson's disease may find the variant prioritization pipeline and structural analysis of interest. The identification of T313M and L347P as high-confidence deleterious variants with predicted structural consequences could inform future experimental studies. However, the lack of experimental validation limits the direct utility of these findings for understanding disease mechanism.

### Major strengths
1. Comprehensive multi-tool variant prioritization pipeline with clear filtering criteria
2. Integration of multiple computational approaches (sequence, structure, dynamics, energetics)
3. Explicit acknowledgment of limitations and the need for experimental validation
4. Use of replicate MD simulations to improve statistical robustness
5. Detailed analysis of IDRs and PTMs, which are often overlooked in structural studies

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim-evidence mismatch
- **Claim pointer** The title and discussion claim that T313M and L347P cause a "vital molecular perturbation" at the "phospho-Serine 65 ubiquitin recognition point," impairing PINK1–ubiquitin recognition.
- **Evidence pointer** Results section "Binding energetics of PINK1-ubiquitin complexes"; Table 2; MM/PBSA section
- **Concern** The MM/PBSA results show mean binding free energies of −1551.84 ± 559.87 (WT), −1547.44 ± 556.01 (T313M), and −1546.54 ± 558.16 (L347P) kcal/mol. These values are statistically indistinguishable given the enormous standard deviations. The authors themselves state that "MM/PBSA analysis indicated broadly comparable binding energetics across all systems." This directly contradicts the central claim that the mutations impair ubiquitin recognition. The docking scores show a trend (−88.4 → −81.9 → −77.4), but these are not statistically tested and the standard deviations overlap substantially.
- **Why it matters** The title and abstract promise a mechanistic explanation for how these mutations impair phospho-Ser65 ubiquitin recognition. If the binding energetics are comparable, the claimed mechanism is unsupported. The manuscript's central thesis is not established by the evidence presented.
- **Resolution test** The authors must either (a) provide statistical evidence that the observed differences in docking scores and MM/PBSA energies are significant, (b) revise the title and conclusions to reflect that the mutations cause structural/dynamic perturbations without significantly altering binding affinity, or (c) provide additional analyses (e.g., free energy decomposition, per-residue energy contributions) that identify specific interactions disrupted at the phospho-Ser65 recognition site.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological validity
- **Claim pointer** The authors claim to model "the activated PINK1 kinase state" with phosphorylation at Ser228 and Ser65, ATP, and Mg2+.
- **Evidence pointer** Methods section "Baseline structural modeling and stereochemical quality assessment"; Results section "Model optimization and system preparation"
- **Concern** The manuscript does not describe how the phosphorylated residues were modeled. Were phosphoserine parameters used? How was the phosphorylation state of Ser228 and Ser65 constructed? How were ATP and Mg2+ positioned? The authors cite "previously characterized structural orientations" but provide no specific reference or validation. The AlphaFold model of PINK1 is an unphosphorylated, apo structure; introducing phosphorylation, ATP, and Mg2+ requires careful parameterization and validation that is not described.
- **Why it matters** The entire simulation is predicated on this modeled activated state. If the phosphorylation and ligand placement are not properly validated, all downstream results are questionable. The methods as described are not reproducible.
- **Resolution test** Provide a detailed description of how phosphoserine residues were parameterized, how ATP and Mg2+ were placed (including the reference structure used), and validation of the modeled complex (e.g., comparison to known PINK1 structures, RMSD of the modeled ligands to crystallographic references).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of MD analysis
- **Claim pointer** The authors claim that MD simulations demonstrate "mutation-induced structural reorganization" and that T313M produces "the greatest structural and dynamic perturbations."
- **Evidence pointer** Results section "Mutation-induced structural reorganization"; Figures 6–8; Supplementary Table 6
- **Concern** The manuscript reports average RMSD, RMSF, Rg, and SASA values with standard deviations, but no statistical tests are performed to determine whether the observed differences between WT and mutants are significant. For example, WT RMSD is 0.9785 ± 0.1050 nm and T313M is 1.0700 ± 0.2185 nm. Given the overlap in standard deviations, it is unclear if this difference is meaningful. Additionally, the authors do not report whether the simulations reached equilibrium, what the equilibration period was, or how convergence was assessed beyond a qualitative statement.
- **Why it matters** Without statistical testing and convergence analysis, the claim that T313M causes "the greatest" perturbation is not supported. The differences could be within normal simulation variability.
- **Resolution test** Perform statistical tests (e.g., block averaging, bootstrap) to compare MD observables between systems. Report convergence metrics (e.g., RMSD vs time plots, block-averaged errors). State the equilibration period excluded from analysis.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Overinterpretation of computational predictions
- **Claim pointer** The discussion states that "L347P is positioned within the kinase domain and is predicted to influence the ubiquitin-binding interface due to its proximity to conserved structural elements, whereas T313M may exert more indirect effects by perturbing regulatory features, including phosphorylation-associated interactions."
- **Evidence pointer** Discussion section; Results section "Structural and regulatory landscape"
- **Concern** The manuscript presents a detailed mechanistic dichotomy between the two mutations, but the evidence for this distinction is thin. The docking and MD results show both mutants destabilize the complex to varying degrees, but the specific claim that T313M affects phosphorylation-associated interactions is speculative. The PTM analysis identifies T313 as a potential phosphorylation site, but no simulation or analysis directly tests whether T313M disrupts phosphorylation. The authors acknowledge this is a prediction, but the discussion presents it with more certainty than warranted.
- **Why it matters** Readers may take these mechanistic claims as established findings rather than hypotheses. The distinction between the two mutations' mechanisms is not directly tested by any experiment or simulation presented.
- **Resolution test** Soften the language to clearly frame these as hypotheses requiring experimental testing. Alternatively, perform additional analyses (e.g., phosphorylation site prediction with multiple tools, molecular dynamics of the phospho-mimetic vs. phospho-dead variants) to provide more direct evidence.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility and completeness
- **Claim pointer** The methods describe a multi-step pipeline involving 825 variants, multiple prediction tools, docking, and MD simulations.
- **Evidence pointer** Methods section throughout
- **Concern** Several methodological details are missing: (1) The specific version and parameters for SIFT, PolyPhen-2, SNP&GO, and EVE are not fully described; (2) The HADDOCK docking protocol (number of models generated, scoring function details, AIR definitions) is incomplete; (3) The MD simulation parameters (temperature coupling, pressure coupling, constraints, time step) are not fully specified; (4) The MM/PBSA calculation parameters (dielectric constant, radii set) are not described; (5) The criteria for selecting the "top-ranked cluster" from docking are not clearly defined.
- **Why it matters** Reproducibility is a core requirement for computational studies. Without complete methodological details, other researchers cannot replicate or build upon this work.
- **Resolution test** Provide complete methodological details in the main text or supplementary materials, including software versions, parameter files, and analysis scripts.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and organization
- **Affected element** Introduction section
- **Evidence pointer** Introduction, first paragraph
- **Issue** The manuscript contains two separate Introduction sections. The first is a brief abstract-like paragraph, and the second is a full introduction. This appears to be a formatting error.
- **Required correction** Remove the duplicate introduction and retain only the full version.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Table 2 and docking results
- **Evidence pointer** Results section "Binding energetics of PINK1-ubiquitin complexes"; Table 2
- **Issue** The docking scores are presented as mean ± SD, but the units are not specified. Additionally, the HADDOCK score is a dimensionless score, but the authors report it as if it were an energy.
- **Required correction** Clarify the units and the meaning of the HADDOCK score. If the score is dimensionless, state this explicitly.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** MD simulation results
- **Evidence pointer** Results section "Mutation-induced structural reorganization"; Figures 6–8
- **Issue** The authors report average values with standard deviations but do not report the number of independent samples used to compute these statistics (e.g., number of frames, number of blocks).
- **Required correction** Report the number of samples used for each average and the method used to compute standard deviations.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature support
- **Affected element** Discussion section
- **Evidence pointer** Discussion, paragraph on T313M phosphorylation
- **Issue** The claim that "phosphorylation at Thr313 contributes to PINK1 kinase activity" is supported by a citation to Guo et al., 2017, but this reference is not listed in the reference list provided.
- **Required correction** Ensure all cited references are included in the reference list and verify the accuracy of the citation.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figures 1–9
- **Evidence pointer** Figures throughout
- **Issue** The figures are referenced but not provided in the manuscript text. Without seeing the figures, it is difficult to assess the quality of the data presentation.
- **Required correction** Ensure figures are included and clearly labeled with appropriate axis labels, legends, and units.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Language and grammar
- **Affected element** Throughout
- **Evidence pointer** Multiple sections
- **Issue** The manuscript contains numerous grammatical errors and awkward phrasings (e.g., "portending overt compromise of structural coherence," "conjointly attest," "eroded interfacial robustness"). These detract from readability.
- **Required correction** Thorough proofreading and editing for clarity and grammatical correctness.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Supplementary material organization
- **Affected element** Supplementary tables and figures
- **Evidence pointer** Supplementary material section
- **Issue** The supplementary material is referenced extensively but not provided. The numbering of supplementary items appears inconsistent (e.g., Supplementary Table 1 is referenced for both variant filtering and IDR analysis).
- **Required correction** Ensure all supplementary items are provided and consistently numbered.

### Technical failings that need to be addressed before the case is established
1. **R1-M1**: The MM/PBSA results directly contradict the central claim of impaired ubiquitin recognition. This must be resolved.
2. **R1-M2**: The construction of the phosphorylated, ATP/Mg2+-bound PINK1 model is not described in sufficient detail to be reproducible or validated.
3. **R1-M3**: No statistical testing of MD observables; the claim that T313M causes the "greatest" perturbation is unsupported.

### Assessment against Nature-style criteria
- **Originality**: Moderate. The application of an integrated computational pipeline to PINK1 mutations is not conceptually novel, though the specific focus on T313M and L347M and the combination of tools may offer some new insights. The field has seen many similar computational variant-effect studies.
- **Scientific importance**: Limited. The findings are entirely computational and provide no experimental validation. The central claim is not supported by the binding energy data. The potential importance for understanding ARPD is speculative.
- **Interdisciplinary readership**: Narrow. The work is primarily of interest to computational biologists and PINK1 researchers. The lack of experimental validation limits its appeal to a broader neuroscience or clinical audience.
- **Technical soundness**: The individual computational tools are well-established, but the overall pipeline has significant methodological gaps (model construction, statistical analysis, convergence assessment). The conclusions are not consistently supported by the data.
- **Readability for nonspecialists**: Poor. The manuscript is dense and contains jargon-heavy prose that would be difficult for a nonspecialist to follow. The duplicate introduction and grammatical errors further detract from readability.

### Recommendation posture
Currently not established from the provided evidence. The manuscript's central claim that T313M and L347M impair phospho-Ser65 ubiquitin recognition is not supported by the binding energy calculations, which show no significant differences. The methodological details are insufficient for reproducibility, and the statistical analysis of MD results is inadequate. The work may have potential as a hypothesis-generating computational study, but substantial revisions and additional analyses are required before the case is established.