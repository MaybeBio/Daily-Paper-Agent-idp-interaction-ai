## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, discussion, and conclusion
- **Assessment boundary** Scientific content, methodological rigor, validity of claims, and presentation quality as presented in the provided manuscript
- **Shared manuscript claim summary** The authors calculate and compare conformational ensembles of the intrinsically disordered protein Sic1 using three different initial pools (two MD force fields, a03ws and a99SBdisp, and one statistical coil generator, TraDES-SC) and two optimization methods (ENSEMBLE and Bayesian Maximum Entropy). They report that differences between ensembles optimized from different priors are greater than differences arising from using different optimization methods on the same prior, and conclude that physics-based generation of initial ensembles is important for accurate ensemble determination.
- **Visible evidence base** Full text including methods descriptions, results sections, and discussion; references to figures and tables (Figures 1-6, Tables 1-2, Supplementary Figures S1-S7) but no actual figure/table content provided
- **Missing materials affecting confidence** Figures and tables referenced but not included; supplementary material not provided; specific numerical results and statistical values not visible; details of BME implementation and ENSEMBLE parameter settings incomplete

## Reviewer

- **Overall assessment** This manuscript addresses a timely and important question in the field of intrinsically disordered protein structural biology: how do choices of initial conformational pools and optimization algorithms affect the resulting experimentally validated ensembles? The systematic comparison of two MD force fields and a statistical coil generator, combined with two contrasting optimization approaches, is a valuable contribution. The authors demonstrate appropriate use of multiple experimental restraints (SAXS, CS, PRE, smFRET) and validation strategies. However, the manuscript has several weaknesses that need to be addressed. The presentation of results relies heavily on figures that are not available for review, making it difficult to fully assess the validity of the claims. The statistical treatment of uncertainties, particularly for the BME method, requires clarification. The conclusion that prior choice dominates over optimization method is interesting but needs stronger quantitative support. The discussion of molecular interactions (H-bonds, pi-contacts) is somewhat speculative given the acknowledged limitations of the experimental data. Overall, this is a solid methodological comparison that would benefit from more rigorous quantitative analysis and clearer presentation of key results.

- **Who would be interested in the results, and why** Researchers working on intrinsically disordered proteins, particularly those involved in ensemble calculation and validation, will find this work directly relevant. The comparison of force fields and optimization methods addresses practical questions faced by practitioners in the field. The work is also relevant to method developers working on integrative structural biology approaches, as it highlights the sensitivity of ensemble calculations to prior choices. Additionally, researchers studying Sic1 specifically, and phosphorylation-regulated disordered proteins more broadly, will be interested in the structural insights presented. The findings have implications for the growing use of ensemble approaches in understanding protein function and disease mechanisms.

- **Major strengths** 
  1. Systematic comparison of three priors and two optimization methods provides a comprehensive assessment of the ensemble calculation landscape
  2. Use of multiple complementary experimental techniques (SAXS, CS, PRE, smFRET) as restraints and validation is methodologically sound
  3. The study addresses an important and under-explored question about the relative influence of priors versus optimization methods
  4. The use of independent validation data (PRE) for BME parameter selection is a good practice
  5. The analysis of molecular interactions (H-bonds, pi-contacts) provides insight beyond global properties
  6. The authors are transparent about limitations and provide practical recommendations for future work

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "differences between ensembles optimized from different priors were greater than when using the same prior with different optimization methods" (Abstract and Conclusion)
- **Evidence pointer** Figures 3-6, Tables 1-2; location not provided
- **Concern** The central claim of the paper, that prior choice dominates over optimization method, is presented without sufficient quantitative support. The manuscript describes qualitative comparisons of DSSP distributions, contact maps, and interaction frequencies, but does not provide a rigorous quantitative metric for comparing ensemble similarity or difference. Without such a metric, the claim that differences between priors are "greater than" differences between methods is not substantiated. The authors should provide a quantitative measure of ensemble dissimilarity (e.g., Jensen-Shannon divergence, earth mover's distance, or similar) applied systematically across all six ensembles.
- **Why it matters** This is the primary conclusion of the paper and has implications for how the field approaches ensemble calculation. If the claim is not rigorously supported, the main message of the paper is weakened. A quantitative comparison would also allow readers to assess the magnitude of the differences, not just their existence.
- **Resolution test** Provide a quantitative comparison metric applied to all pairs of ensembles, with appropriate statistical testing (e.g., bootstrapping) to assess significance. Show that the within-prior/across-method differences are consistently smaller than across-prior differences for multiple structural properties.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that for a03ws, the agreement with PRE data initially improves then worsens as theta is set beyond the elbow region, while for a99SBdisp and TraDES-SC, agreement with PRE validation data monotonically worsens as theta decreases (Section 3.1.1)
- **Evidence pointer** Figure 1, Table 1; location not provided
- **Concern** The selection of theta values for the BME method is described qualitatively, but the criteria for choosing the "optimal" theta are not fully specified. For a03ws, the minimum PRE validation score is used, while for a99SBdisp and TraDES-SC, the "elbow" region is used. This inconsistency in theta selection criteria between priors could introduce bias in the comparison. The authors should justify why different selection criteria are appropriate for different priors, or apply a consistent criterion across all cases. Additionally, the sensitivity of the results to the choice of theta should be assessed.
- **Why it matters** The BME results depend critically on the theta parameter. If theta is selected differently for different priors, the comparison between priors may reflect the theta selection criteria rather than genuine differences in the priors themselves. This could undermine the validity of the main conclusion.
- **Resolution test** Apply a consistent theta selection criterion across all three priors (e.g., L-curve curvature maximum, or a fixed target chi-squared value) and show that the main conclusions are robust to this choice. Alternatively, provide a sensitivity analysis showing how results vary with theta for each prior.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors conclude that "the analysis also provides insights into designing new experiments that report on the least restrained features among the optimized ensembles" (Abstract) and identify specific residue pairs for future FRET labelling (Section 3.2.2)
- **Evidence pointer** Section 3.2.2, Figure 4; location not provided
- **Concern** The identification of "least restrained features" and specific FRET labelling positions is based on the comparison of inter-residue distance maps across ensembles. However, the manuscript does not clearly explain how the degree of "restraint" is quantified or how the specific residue pairs (e.g., approximately 1,40 vs approximately 40,70) were identified as being less or more restrained. The criteria for selecting these positions should be made explicit and quantitative.
- **Why it matters** This is presented as a practical outcome of the work with direct experimental implications. If the criteria for identifying these positions are not transparent and reproducible, the recommendation could be misleading for experimentalists planning new measurements.
- **Resolution test** Provide a clear quantitative definition of "restraint" (e.g., variance across ensembles, Shannon entropy of distance distributions, or similar) and show the values for all residue pairs, with the recommended positions highlighted. Demonstrate that the identified positions are indeed those with the highest uncertainty across ensembles.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the analysis also provides insights into designing new experiments" and discuss the importance of force field choice, but the manuscript does not include a systematic comparison of the computational cost or convergence of the different methods
- **Evidence pointer** Section 2, Section 3.1; location not provided
- **Concern** The manuscript compares ensembles generated from MD simulations (a03ws, a99SBdisp) with those from statistical coil generation (TraDES-SC), but does not discuss the computational expense, sampling convergence, or practical feasibility of each approach. For practitioners, this information is crucial for deciding which approach to use. The authors should comment on the computational requirements and whether the MD simulations were sufficiently converged for the purposes of this comparison.
- **Why it matters** The practical utility of the findings depends on the feasibility of the approaches. If the MD-based priors require orders of magnitude more computational resources without clear benefits, this should be stated. Conversely, if the MD priors are essential for accurate ensembles, this strengthens the case for investing in such simulations.
- **Resolution test** Add a discussion of computational costs, simulation lengths, convergence metrics (e.g., block averaging, autocorrelation times), and practical recommendations for when each type of prior is most appropriate.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction, Section 1
- **Evidence pointer** Section 1; location not provided
- **Issue** The introduction assumes significant prior knowledge of ensemble calculation methods and terminology. Terms such as "ill-posed problem," "Bayesian Maximum Entropy," and "statistical coil" are introduced without sufficient explanation for readers who may be new to the field.
- **Required correction** Provide brief explanations of key concepts and methods when first introduced, or add a short "Background" subsection to make the manuscript more accessible to a broader readership.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, Section 2
- **Evidence pointer** Section 2; location not provided
- **Issue** The description of the ENSEMBLE method states that "the optimization terminates when all experimental restraints are below their respective target energies that are set by default in ENSEMBLE." The specific target energies and how they are determined are not described.
- **Required correction** Provide the specific target energy values or describe how they are set, and justify the choice of these values.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, Section 2
- **Evidence pointer** Section 2; location not provided
- **Issue** The manuscript states that for BME, "the hyperparameter theta is determined by tuning" but does not describe the tuning procedure in detail. The range of theta values tested and the step size used are not specified.
- **Required correction** Describe the theta tuning procedure in more detail, including the range of values tested and the criteria for selecting the final value.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, Section 3.1.1
- **Evidence pointer** Section 3.1.1, Table 1; location not provided
- **Issue** The manuscript reports reduced chi-squared values for each experimental dataset but does not explain how these are calculated or what constitutes a "good" fit. The degrees of freedom for each dataset are not specified.
- **Required correction** Provide the formula used for reduced chi-squared calculation and specify the number of data points and degrees of freedom for each experimental dataset.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Results, Section 3.2.3
- **Evidence pointer** Section 3.2.3; location not provided
- **Issue** The discussion of H-bonds and pi-contacts is detailed but would benefit from a brief explanation of why these specific interactions are relevant for IDP structure and function, particularly for readers not specialized in molecular interactions.
- **Required correction** Add a brief introductory paragraph to Section 3.2.3 explaining the biological relevance of H-bonds and pi-contacts in IDPs.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, Section 2
- **Evidence pointer** Section 2; location not provided
- **Issue** The manuscript states that MD simulations were resampled with a stride of 40 frames, resulting in Δt=7.2 ns between consecutive frames. The total number of frames and the total simulation time for each force field are not stated.
- **Required correction** Provide the total simulation time and number of frames for each MD-based prior ensemble.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion, Section 3.2.1
- **Evidence pointer** Section 3.2.1, Figure 3; location not provided
- **Issue** The comparison of DSSP-derived secondary structure propensities with SSP scores from chemical shift data is interesting but brief. The authors note that three of six helical patches match, but do not discuss the implications of the three that do not match.
- **Required correction** Expand the discussion of discrepancies between DSSP and SSP results, and consider whether these discrepancies reflect limitations of the methods or genuine structural features.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Conclusion
- **Evidence pointer** Conclusion; location not provided
- **Issue** The conclusion is somewhat technical and does not clearly state the broader implications of the findings for the field of IDP research or for understanding protein function and disease.
- **Required correction** Add a brief paragraph in the conclusion that summarizes the broader significance of the work and its potential impact on future research in the field.

## Risk / unsupported claims
- The central claim that "differences between ensembles optimized from different priors were greater than when using the same prior with different optimization methods" is not quantitatively supported in the provided text. Figures and tables that would provide this support are not available for review.
- The claim that specific residue pairs (approximately 1,40) are "less restrained" than others (approximately 40,70) is not supported by explicit quantitative criteria in the text.
- The statement that "the analysis also provides insights into designing new experiments" is presented as a conclusion but the specific insights are not clearly delineated or quantified.
- The claim that "experimental data makes the ensembles more similar" is stated without quantitative evidence in the provided text.
- The assertion that "the physics model of the prior, i.e., the force field parametrization, is by far the most important factor that drives formation of stable/transient secondary structure motifs" is a strong claim that requires more systematic evidence than presented.
- The discussion of H-bonds and pi-contacts as determinants of ensemble properties is presented as if these are established findings, but the text acknowledges that experimental data is insufficient to define these interactions, creating some tension in the interpretation.
- The manuscript claims that ENSEMBLE optimization "prioritizes agreement with experimental data" while BME "seeks a balance between agreement with experiments and deviation from the prior," but the quantitative trade-offs are not fully characterized.