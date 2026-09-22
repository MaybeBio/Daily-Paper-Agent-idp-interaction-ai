## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary figure/table references
- **Assessment boundary** Scientific validity, methodological soundness, claims versus evidence, and presentation quality of the Mpipi coarse-grained model for biomolecular phase separation
- **Shared manuscript claim summary** The authors present Mpipi, a multiscale coarse-grained model parameterised from atomistic simulations and bioinformatics data, which they claim achieves near-quantitative accuracy in predicting protein critical temperatures for phase separation, outperforming seven other residue-level models in benchmarks against experimental radii of gyration and phase diagrams, and capturing complex behaviours including protein-RNA interactions and multiphasic compartmentalisation.
- **Visible evidence base** Main text figures 1-6, supplementary figures S2-S8, supplementary tables I, III, IX, X, XI, XIV, methods section describing PMP calculations, direct-coexistence simulations, and parameterisation procedures
- **Missing materials affecting confidence** Supplementary information content is referenced but not fully provided in the submitted material; specific numerical values for all benchmark comparisons are not fully detailed in the main text; details of the Bayesian parameter-learning procedure for the TSCL-M2 model are not described; full parameter tables are only referenced

## Reviewer
- **Overall assessment** This manuscript presents a timely and potentially valuable contribution to the field of biomolecular phase separation modelling. The Mpipi model addresses a critical gap by combining physics-based parameterisation from atomistic simulations with bioinformatics data, and the authors demonstrate its predictive power across multiple benchmarks. The work is technically sound in its core methodology, and the comparative analysis against seven other models is comprehensive. However, several concerns regarding the robustness of the parameterisation, the interpretation of benchmark results, and the generalisability of the model need to be addressed before the claims of near-quantitative accuracy can be fully accepted.

- **Who would be interested in the results, and why** Computational biophysicists and physical chemists studying biomolecular phase separation will find this work directly relevant, as it provides a new tool with demonstrated accuracy. Experimental biologists studying condensate biology, particularly those investigating sequence determinants of phase behaviour, will benefit from a model that can predict mutational effects. Researchers developing coarse-grained models for other biomolecular systems will be interested in the methodological framework combining bottom-up and top-down approaches. The work also has relevance for the broader soft matter and polymer physics community interested in sequence-specific phase behaviour.

- **Major strengths** The manuscript presents a well-motivated and carefully constructed model that addresses a known limitation in existing coarse-grained approaches. The parameterisation strategy, combining atomistic PMF calculations with bioinformatics data, is innovative and physically grounded. The comprehensive benchmarking against seven other models provides a valuable resource for the community. The demonstration of quantitative accuracy for A1-LCD variants, with a Pearson correlation coefficient of 0.97, is impressive. The extension to protein-RNA interactions and multiphasic compartmentalisation demonstrates the model's versatility. The use of the Wang-Frenkel potential is a thoughtful choice that addresses technical issues with Lennard-Jones-based approaches.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of parameterisation
- **Claim pointer** The authors claim the model is "parameterised from both atomistic simulations and bioinformatics data" and achieves "near-quantitative accuracy" in predicting critical temperatures.
- **Evidence pointer** Methods section, Figure 2, Supplementary Tables I and XI
- **Concern** The parameterisation procedure relies on a combination of PMF calculations and bioinformatics data, but the manuscript does not provide sufficient detail on how these two sources are weighted and integrated. Specifically, the process of converting PMF well depths to Wang-Frenkel parameters is described only qualitatively, and the criteria for adjusting the multiplicative factor for εij values are not specified. The authors state that "we next adjust the values of εij by a suitable multiplicative factor so that the integrals of the well depths of the PMF curves of residue pairs i and j approximate their WF analogues," but the tolerance for this approximation and the iterative procedure are not described. This lack of detail makes it difficult to assess the robustness and reproducibility of the parameterisation.
- **Why it matters** The central claim of the paper is that the Mpipi model achieves quantitative accuracy due to its physics-based parameterisation. If the parameterisation procedure is not fully specified, other researchers cannot reproduce the model or assess whether the results are sensitive to arbitrary choices in the fitting procedure. This is particularly important given that the authors note the model was not optimised on Rg data, yet achieves good agreement, suggesting the parameterisation is critical to its success.
- **Resolution test** Provide a detailed step-by-step description of the parameterisation procedure, including the exact algorithm for fitting PMF curves to the Wang-Frenkel form, the convergence criteria, and the sensitivity of the final parameters to initial choices. Ideally, provide a validation of the parameterisation on a held-out set of residue pairs not used in the fitting.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency for quantitative claims
- **Claim pointer** The authors claim Mpipi "describes almost quantitatively the change in protein critical temperatures as a function of amino-acid sequence" and achieves "near-quantitative accuracy."
- **Evidence pointer** Figure 5, Supplementary Tables, Results section "Recapitulating the phase behaviour of A1-LCD variants"
- **Concern** While the Pearson correlation coefficient of 0.97 for A1-LCD variants is impressive, the manuscript does not provide a comprehensive statistical analysis of the prediction errors. The root mean squared deviation (D) is reported as 9 K for Mpipi, but the range of experimental critical temperatures for the variant set is not clearly stated, making it difficult to assess whether this deviation is indeed "near-quantitative." Additionally, the comparison across models in Figure 5h-m shows correlation coefficients, but the authors do not provide confidence intervals or statistical tests for the differences between models. The claim of "near-quantitative accuracy" would be strengthened by a more rigorous error analysis, including per-variant errors and a discussion of which types of mutations are most and least accurately predicted.
- **Why it matters** The central claim of the paper rests on the quantitative accuracy of the model. Without a thorough error analysis, it is difficult to assess whether the model truly achieves near-quantitative accuracy or whether the high correlation coefficient masks systematic errors for certain types of sequence changes. This is particularly important for the model's utility in predicting the effects of mutations in disease-associated proteins.
- **Resolution test** Provide a detailed error analysis, including per-variant prediction errors, a breakdown of errors by mutation type (e.g., aromatic substitutions, charge changes), and a comparison of the distribution of errors across models. Include confidence intervals for the correlation coefficients and a statistical test for whether the differences between models are significant.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalisability of the model
- **Claim pointer** The authors claim the model "can account for protein-RNA interactions, correctly predicts the multiphase behaviour of a charge-matched poly-arginine/poly-lysine/RNA system, and recapitulates experimental LLPS trends for sequence mutations on FUS, DDX4 and LAF-1 proteins."
- **Evidence pointer** Figure 6, Results section "LLPS of other proteins and multiphasic compartmentalisation", Supplementary Section S7
- **Concern** The demonstration of generalisability is limited to a small number of systems. For FUS, DDX4, and LAF-1, the manuscript states that Mpipi achieves "good qualitative agreement" and "in some cases quantitative accuracy," but the specific results are not shown in the main text and are only referenced in the supplementary information. The multiphasic compartmentalisation result is demonstrated for a single model system (polyR/polyK/RNA). The authors do not discuss potential limitations of the model for systems with different physicochemical characteristics, such as proteins with high charge content or those where hydrophobic interactions dominate. The claim of generalisability would be strengthened by testing the model on a more diverse set of phase-separating systems.
- **Why it matters** The utility of a coarse-grained model depends on its ability to predict behaviour across a wide range of sequences and conditions. If the model is only accurate for a narrow class of systems, its practical value is limited. The authors' claim of generalisability is currently based on a limited set of examples, and it is unclear whether the model would perform equally well for systems with different interaction profiles.
- **Resolution test** Provide the specific results for FUS, DDX4, and LAF-1 in the main text or a more detailed supplementary section. Discuss the range of applicability of the model, including potential limitations for systems with different physicochemical properties. Ideally, test the model on additional systems with diverse sequence compositions and interaction profiles.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Comparison with other models
- **Claim pointer** The authors benchmark Mpipi against seven other residue-level coarse-grained models and claim it achieves the best agreement with experiment.
- **Evidence pointer** Figures 3-5, Results sections "Estimating single-molecule radii of gyration" and "Recapitulating the phase behaviour of A1-LCD variants"
- **Concern** The comparison with other models is comprehensive, but the manuscript does not discuss potential sources of bias in the comparison. For example, the other models were parameterised using different strategies and may have been optimised for different properties. The authors note that some models were optimised on Rg data, but they do not discuss whether the comparison is fair given the different parameterisation targets. Additionally, the manuscript does not discuss the computational cost of the different models, which is an important practical consideration for users. The comparison would be more informative if the authors discussed the trade-offs between accuracy and computational efficiency.
- **Why it matters** The claim that Mpipi outperforms other models is a key selling point of the paper. However, if the comparison is not fair or does not account for differences in model design and parameterisation, the conclusion may be misleading. Users need to understand the trade-offs between different models to make informed choices for their specific applications.
- **Resolution test** Discuss the potential sources of bias in the model comparison, including differences in parameterisation targets and computational cost. Provide a more detailed analysis of the strengths and weaknesses of each model relative to Mpipi, and discuss the practical implications of these differences for users.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 1
- **Evidence pointer** Figure 1
- **Issue** The schematic in Figure 1 is informative but could be clearer in showing the workflow from atomistic simulations and bioinformatics data to the final coarse-grained model parameters. The connection between the different panels is not immediately obvious.
- **Required correction** Consider adding arrows or a step-by-step flow diagram to make the parameterisation workflow more explicit.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section, parameter tables
- **Evidence pointer** Supplementary Table XI
- **Issue** The full parameter table is only available in the supplementary information, and the main text does not provide a summary of the key parameters or their physical interpretation. This makes it difficult for readers to understand the model without accessing the supplementary material.
- **Required correction** Include a summary table of key parameters in the main text, with a discussion of their physical significance and how they compare to values used in other models.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigour
- **Affected element** Figure 5
- **Evidence pointer** Figure 5h-m
- **Issue** The correlation plots in Figure 5h-m do not show error bars or confidence intervals, making it difficult to assess the uncertainty in the predictions.
- **Required correction** Add error bars or confidence intervals to the correlation plots, or provide a table of prediction errors with uncertainties.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** RNA parameterisation
- **Evidence pointer** Methods section, "Mpipi model"
- **Issue** The parameterisation of RNA nucleotides is described briefly, and the authors note that "in subsequent work, we aim to refine our RNA parameters." This suggests the RNA parameters are preliminary, which is not clearly stated in the main text.
- **Required correction** Clearly state the preliminary nature of the RNA parameters in the main text and discuss the potential implications for the accuracy of protein-RNA predictions.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The discussion section focuses on the successes of the model but does not adequately address its limitations, such as the lack of explicit temperature dependence, the pairwise approximation, and the potential importance of higher-order interactions.
- **Required correction** Expand the discussion of limitations and future directions, including a more detailed consideration of when the model might fail and how it could be improved.

## Risk / unsupported claims
- The claim of "near-quantitative accuracy" is supported for A1-LCD variants but is extrapolated to other systems where only qualitative agreement is demonstrated; the manuscript should more carefully qualify the accuracy claims for different systems.
- The statement that Mpipi "can account for protein-RNA interactions" is based on a single demonstration with polyR/polyK/RNA; this is insufficient to establish general applicability to protein-RNA systems.
- The claim that the model "recapitulates experimental LLPS trends for sequence mutations on FUS, DDX4 and LAF-1 proteins" is not directly supported by data shown in the main text; the results are only referenced in the supplementary information.
- The assertion that the Wang-Frenkel potential "obviates the need for truncating and shifting the potential" and is therefore superior to Lennard-Jones-based approaches is presented as an advantage but is not systematically tested in the benchmarks.
- The statement that "one set of measurements, be it experiments or simulations, will be unlikely to yield the complete picture" is a reasonable conclusion but is presented as a general principle without specific evidence from this work.