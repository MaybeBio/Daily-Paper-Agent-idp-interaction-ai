## Review setup
- **Input scope** Full manuscript text including abstract, main text, results, methods, supplementary information descriptions, and figure legends
- **Assessment boundary** Scientific content, technical soundness, logical coherence, and support of claims by presented evidence; not editorial or stylistic quality
- **Shared manuscript claim summary** The authors propose that PopZ condensates are composed of short filaments formed by longitudinal stacking of hexameric building blocks, that the helical oligomerization domain is necessary and sufficient for filamentation and condensation, that the disordered region inhibits condensation, that phase-dependent conformational changes regulate client binding, and that filament formation is required for PopZ cellular function in vivo
- **Visible evidence base** Cryo-ET of in vitro and in vivo PopZ condensates, mass photometry, analytical ultracentrifugation, smFRET, coarse-grained molecular dynamics simulations, AlphaFold structural predictions, mutagenesis, fluorescence microscopy, FRAP, and bacterial growth assays
- **Missing materials affecting confidence** Supplementary figures and tables referenced but not provided; detailed simulation parameters and validation metrics; raw cryo-ET density maps and segmentation quality metrics; complete statistical analysis details; strain construction and validation details; full FRAP fitting parameters and model selection criteria

## Reviewer
- **Overall assessment** This manuscript presents a comprehensive and ambitious multiscale investigation of PopZ condensate structure and function. The integration of cryo-ET, biochemistry, single-molecule methods, and simulations is commendable and appropriate for the question posed. The central claim that filamentous ultrastructure is required for PopZ function is potentially significant, but the evidence presented has several gaps that need to be addressed. The in vitro structural characterization is thorough, but the causal link between filament formation and in vivo function is not fully established. The finding that the disordered region inhibits condensation while the helical domain drives it is interesting, but the mechanistic details remain incomplete. The manuscript would benefit from clearer presentation of quantitative data and stronger statistical support for key claims.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, particularly those interested in the structural basis of condensate function, will find this work relevant. The bacterial cell biology community, especially those studying Caulobacter crescentus and polar organization, will be interested in the functional implications for PopZ. The broader phase separation community will be interested in the demonstration that filamentous ultrastructure can be functionally important, as this contrasts with the more common view of condensates as amorphous assemblies. Methodologically, the integration of cryo-ET with smFRET and simulations provides a template that could be applied to other condensate systems.

- **Major strengths** 1) The multiscale approach integrating multiple orthogonal techniques is well-designed and appropriate for the question. 2) The cryo-ET visualization of filamentous ultrastructure within condensates is technically impressive and provides direct structural evidence. 3) The identification of specific sequence elements (H2, loop, H3H4, L6) with distinct roles in the assembly pathway is a valuable contribution. 4) The phase-dependent conformational switch model is conceptually novel and provides a mechanistic framework for understanding condensate function. 5) The in vivo functional assays, particularly the growth phenotype and ParB segregation experiments, connect the structural findings to biological relevance.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Causal claim
- **Claim pointer** The title and abstract state that filamentous ultrastructure is "required" for PopZ cellular function, and the main text claims that "perturbing either filament formation or the ability of filaments to condense impairs PopZ function and leads to growth phenotypes"
- **Evidence pointer** Figure 5, Extended Data Figure 9, location not provided for specific data points
- **Concern** The causal relationship between filament formation and in vivo function is not convincingly established. The ΔL6 mutant, which cannot form filaments, shows growth defects and impaired ParB segregation. However, this mutant also has a higher saturation concentration and altered condensate properties. The authors attribute the functional defects to loss of filaments, but the increased csat alone could explain the phenotypes. The authors need to demonstrate that the functional defects are specifically due to loss of filamentous ultrastructure rather than to altered condensate properties more generally. Additionally, the "Loki" mutant that forms filaments but has reduced condensation shows partial function, but the quantitative comparison is not presented clearly.
- **Why it matters** The central claim of the paper is that filamentous ultrastructure is specifically required for function. If the phenotypes are due to altered condensate properties rather than loss of filaments per se, the conclusion is substantially weakened.
- **Resolution test** Provide quantitative comparison of condensate properties (size, number, dynamics) and functional outcomes across WT, ΔL6, Loki, and other mutants. Demonstrate that condensates with similar csat but different filament content have different functional outcomes, or vice versa. Alternatively, rescue experiments where filament formation is restored in ΔL6 background would strengthen the causal claim.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative support
- **Claim pointer** The manuscript claims that filament length distribution follows an exponential distribution with median and mean lengths of 34 nm and 38 nm, respectively, and that this indicates isodesmic polymerization
- **Evidence pointer** Figure 1b, Extended Data Figure 3, location not provided
- **Concern** The statistical support for the exponential distribution and the isodesmic polymerization model is not presented. The R2 value of 0.99 is mentioned, but the number of filaments measured, the fitting procedure, and the comparison to alternative models (e.g., cooperative polymerization) are not described. The claim of isodesmic polymerization is important for the mechanistic model, but the evidence is insufficient. Additionally, the statement that the difference in filament length between WT and OD (3-5 nm) is "smaller than the size of the building block itself" needs quantitative justification.
- **Why it matters** The isodesmic polymerization model is used to support the claim that filament formation is a simple, non-cooperative process. If the data are consistent with other models, the mechanistic interpretation changes.
- **Resolution test** Provide the full fitting procedure, number of filaments analyzed, statistical comparison to alternative models, and confidence intervals for the fitted parameters. Show the raw length distribution data and the fit residuals.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Mechanistic model
- **Claim pointer** The manuscript proposes that "phase-dependent conformational changes prevent interfilament contacts in the dilute phase and expose client-binding sites in the dense phase" and that H1 acts as a competitive inhibitor of client binding in the dilute phase
- **Evidence pointer** Figure 4, Extended Data Figure 8, location not provided
- **Concern** The smFRET data show two populations (extended and compacted) in the dilute phase, and the compacted population is attributed to H1-OD interactions. However, the evidence that this conformational change is specifically responsible for regulating client binding is indirect. The claim that "condensation substantially enhances ChIP–PopZ interactions" is based on recruitment to condensates, but the mechanism by which condensation relieves H1-OD inhibition is not demonstrated. The model in Figure 4f is plausible but not directly tested.
- **Why it matters** The phase-dependent conformational switch is a key mechanistic claim. Without direct evidence that the conformational change regulates client binding, the model remains speculative.
- **Resolution test** Perform smFRET experiments in the presence of client protein to directly test whether client binding competes with H1-OD interactions. Alternatively, use mutants that stabilize or destabilize the compacted state and test their effects on client recruitment in vitro and in vivo.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Simulation validation
- **Claim pointer** The manuscript states that coarse-grained molecular dynamics simulations "validated" the experimental findings and were used to identify interaction hotspots
- **Evidence pointer** Extended Data Figure 5, location not provided
- **Concern** The simulation methodology is described only briefly in the Methods, and the validation against experimental data is not quantitatively presented. The claim that simulations show "qualitative agreement" with experimental data is vague. The specific predictions from simulations that were then tested experimentally are not clearly delineated. The force field parameters and their justification are not provided.
- **Why it matters** The simulations are used to support the mechanistic model and to identify specific residues involved in condensation. Without proper validation and clear presentation, the simulation results cannot be properly evaluated.
- **Resolution test** Provide detailed simulation parameters, convergence metrics, and quantitative comparison between simulation predictions and experimental observations. Clearly state which simulation predictions were tested experimentally and the outcomes.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** In vivo relevance
- **Claim pointer** The manuscript claims that "in cells, perturbing either filament formation or the ability of filaments to condense impairs PopZ function and leads to growth phenotypes"
- **Evidence pointer** Figure 5, Extended Data Figure 9, location not provided
- **Concern** The in vivo experiments are performed with plasmid-based expression of PopZ variants in a ΔpopZ background. The expression levels are described as "low" but not quantified relative to endogenous PopZ levels. The potential for overexpression artifacts or dominant-negative effects is not addressed. The growth phenotypes are shown qualitatively but quantitative growth curves and statistical analysis are not presented.
- **Why it matters** The in vivo relevance of the findings depends on the mutants being expressed at physiologically relevant levels and the phenotypes being robust and reproducible.
- **Resolution test** Quantify expression levels of all PopZ variants relative to endogenous levels. Provide quantitative growth curves with statistical analysis. Include complementation experiments with WT PopZ to demonstrate that the phenotypes are due to the specific mutations.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1a
- **Evidence pointer** Figure 1a, location not provided
- **Issue** The cryo-ET images in Figure 1a are difficult to interpret. The purple boxes indicating magnified regions are not clearly visible, and the filamentous structures highlighted by yellow arrows are not obvious to the reader.
- **Required correction** Provide higher-magnification insets with clearer annotations. Consider adding a schematic representation of the filamentous network alongside the tomographic slices.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Multiple figures
- **Evidence pointer** Figures 3, 4, 5, location not provided
- **Issue** The number of replicates, statistical tests used, and error bar definitions are not consistently reported across figures. Some figure legends mention "mean ± s.d." but do not specify the number of independent experiments.
- **Required correction** Standardize statistical reporting across all figures. Clearly state the number of biological and technical replicates, the statistical tests used, and the definition of error bars in each figure legend.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Mass photometry
- **Evidence pointer** Methods section, location not provided
- **Issue** The mass photometry experiments are described briefly. The calibration procedure, the number of molecules analyzed, and the criteria for assigning oligomeric states are not described in sufficient detail.
- **Required correction** Provide more detailed methods for mass photometry, including calibration standards, data analysis procedures, and criteria for peak assignment.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Figure 3b
- **Evidence pointer** Figure 3b, location not provided
- **Issue** The AUC data show that WT PopZ forms "the largest species" at high concentrations, but the interpretation that this represents filaments is not directly supported. The sedimentation coefficient distribution could also be consistent with large aggregates or clusters.
- **Required correction** Provide additional evidence that the large species observed by AUC correspond to filaments, such as negative-stain EM or size-exclusion chromatography coupled with multi-angle light scattering.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Model presentation
- **Affected element** Figure 6
- **Evidence pointer** Figure 6, location not provided
- **Issue** The mechanistic model in Figure 6 is helpful but could be more detailed. The specific conformational changes and interactions are not clearly depicted.
- **Required correction** Expand the model to show the specific domains and residues involved at each step, and indicate which steps are supported by direct evidence versus inferred from the data.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction and Discussion
- **Evidence pointer** Introduction, Discussion, location not provided
- **Issue** The discussion of other filamentous condensates is brief. A more thorough comparison with systems such as p62, F-actin, and SPOP/DAXX would help contextualize the findings.
- **Required correction** Expand the Discussion to include a more detailed comparison of the mechanisms of filament formation and function across different filamentous condensate systems.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data and code availability
- **Evidence pointer** Methods, location not provided
- **Issue** The statement about data and code availability is brief. The simulation code is mentioned as being on GitHub, but the specific repository and access details are not provided in the main text.
- **Required correction** Provide the full data and code availability statement, including repository URLs and accession numbers for all datasets.

## Risk / unsupported claims
- The claim that filamentous ultrastructure is "required" for PopZ function is not fully supported; the evidence shows correlation but not causation
- The claim of isodesmic polymerization is supported only by a single R2 value without full statistical analysis
- The phase-dependent conformational switch model is plausible but not directly tested
- The claim that "condensation substantially enhances ChIP–PopZ interactions" is based on indirect evidence from condensate recruitment experiments
- The in vivo relevance of the findings depends on expression levels that are not quantified
- The simulation results are described as showing "qualitative agreement" without quantitative validation metrics
- The claim that the IDR "inhibits" condensation is based on the TEV cleavage experiment, but the mechanism of inhibition is not fully characterized
- The statement that "the entire OD is necessary for filamentation" is based on deletion analysis but the specific residues involved are not identified