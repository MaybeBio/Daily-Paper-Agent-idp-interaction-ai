## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary figure/table references.
- **Assessment boundary** Scientific validity, methodological soundness, claims versus evidence, and significance of findings as presented in the provided manuscript.
- **Shared manuscript claim summary** The authors demonstrate that On-the-fly Probability Enhanced Sampling (OPES) in the multithermal ensemble can efficiently generate atomistic conformational ensembles for intrinsically disordered proteins (IDPs) of 15–71 residues. They show that OPES produces ensembles consistent with REST2 and unbiased simulations while accelerating convergence and exploring low-population states. For ACTR, OPES reveals transient tertiary structures with cooperatively folded helices, consistent with NMR and SAXS data, suggesting functional relevance for folding-upon-binding.
- **Visible evidence base** Main text figures 1–5, tables 1–2, supplementary figures 1–18 (referenced), supplementary tables 2–8 (referenced), methods section with simulation and analysis details.
- **Missing materials affecting confidence** Supplementary figures and tables are referenced but not provided in the submitted material. Movies 1–3 are referenced but not provided. PDB structure 1KBH is cited but not included. Experimental data (NMR, SAXS) are referenced but raw data files are not provided.

## Reviewer
- **Overall assessment** This manuscript presents a timely and potentially valuable methodological advance for sampling IDP conformational ensembles. The comparison of OPES against REST2 and unbiased simulations across multiple systems is thorough, and the identification of transient tertiary structure in ACTR is biologically interesting. However, the central claim that OPES uniquely reveals these states requires stronger evidence that they are not artifacts of the enhanced sampling method. The manuscript would benefit from clearer presentation of convergence criteria and a more critical discussion of the limitations of the approach. The writing is generally clear, though some methodological details are dense.
- **Who would be interested in the results, and why** Computational biophysicists and chemists developing or applying enhanced sampling methods to disordered proteins; experimentalists studying IDP conformational ensembles by NMR or SAXS who need validated simulation approaches; researchers interested in folding-upon-binding mechanisms and drug discovery targeting IDPs.
- **Major strengths** 1) Systematic comparison of OPES with REST2 and unbiased MD across four systems of increasing complexity. 2) Use of multiple complementary metrics (autocorrelation, blocking, cumulative averages, 2D projections) to assess convergence and sampling efficiency. 3) Integration of extensive experimental data (NMR, SAXS) for validation and reweighting. 4) Identification of a specific, biologically relevant phenomenon (transient tertiary structure in ACTR) that is not captured by other methods. 5) Practical guidance for implementing OPES, including a simple formula for estimating temperature steps.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence for central claim
  - **Claim pointer** "OPES reveals transiently structured states in which multiple α-helices involved in partner binding fold cooperatively and form tertiary contacts" and "these states were not sampled in REST2 or in unbiased simulations"
  - **Evidence pointer** Figure 5, Supplementary Figures 15–17, Supplementary Tables 7–8
  - **Concern** The central claim that OPES uniquely samples transient tertiary structures in ACTR rests on the assertion that REST2 and unbiased simulations do not access these states. However, the evidence presented is indirect: the comparison relies on 2D projections and effective coverage metrics, and the REST2 simulations show substantially reduced temperature diffusion for full-length ACTR. It is unclear whether the difference is due to OPES being fundamentally better at sampling these states, or simply because the REST2 simulations were not run long enough or with sufficient replica exchange efficiency. The authors note that REST2 simulations had an order-of-magnitude decrease in replica round trips, which suggests the REST2 comparison may be underpowered.
  - **Why it matters** The title and abstract emphasize the discovery of transient tertiary structure in IDPs. If this is simply a consequence of more efficient sampling rather than a unique capability of OPES, the novelty is diminished. The claim that these states are "not sampled" by other methods is strong and requires more rigorous support, such as demonstrating that longer REST2 or unbiased simulations still do not access them, or providing free energy estimates that show the states are thermodynamically relevant.
  - **Resolution test** Provide evidence that the transient tertiary states are not accessed even with substantially longer REST2 or unbiased simulations, or demonstrate that the states are thermodynamically significant (e.g., via free energy calculations or multiple independent OPES runs with different initial conditions). Alternatively, soften the claim to state that OPES samples these states more efficiently rather than uniquely.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Validation of reweighted ensemble
  - **Claim pointer** "the OPES-derived ensemble showed improved agreement with the left-out RDC and PRE data" and "the resulting reweighted ensembles" are accurate representations of the ACTR ensemble
  - **Evidence pointer** Figure 5b–c, Supplementary Figure 15
  - **Concern** The reweighting procedure is complex, involving multiple experimental datasets (CS, SAXS, RDC, PRE) with different forward models and error treatments. The manuscript reports improved agreement with left-out data for the OPES ensemble, but the improvement is modest (e.g., RDC Q-factor 0.45 vs. 0.55; SAXS reduced χ2 1.40 vs. 1.19 for REST2). It is not clear whether these differences are statistically significant given the uncertainties in the forward models and the reweighting procedure. The choice to focus on the CS+PRE reweighted ensemble is justified, but the sensitivity of the conclusions to this choice is not fully explored.
  - **Why it matters** The biological conclusions about transient tertiary structure depend on the reweighted ensemble being accurate. If the reweighting is not robust, the identified states could be artifacts of the procedure rather than genuine features of the ACTR ensemble.
  - **Resolution test** Provide a more detailed uncertainty analysis of the reweighting, including bootstrap or jackknife estimates of the reweighted ensemble properties. Show that the key conclusions (e.g., presence of transient tertiary states) are robust to variations in the reweighting parameters, the choice of experimental datasets, and the treatment of forward model errors.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Methodological validation
  - **Claim pointer** "OPES achieves multithermal sampling within a single simulation replica, without replica exchange or extensive parameter tuning" and "yields reweighted ensembles broadly consistent with REST2 and unbiased simulations"
  - **Evidence pointer** Figures 2–4, Supplementary Figures 1–14
  - **Concern** The validation of OPES against REST2 and unbiased simulations is performed for specific systems and conditions. The generalizability of the approach to other IDPs, particularly larger or more complex ones, is not established. The authors note that the success rate for converging bias potentials decreases with system size (from 50% for the 15-residue peptide to 10% for ACTR), which raises questions about the practical applicability of the method to larger systems. The empirical formula for estimating temperature steps is useful but may not be universally applicable.
  - **Why it matters** The manuscript positions OPES as a "robust and accessible approach" for IDP simulations. If the method becomes increasingly difficult to converge for larger systems, its practical utility is limited. The decreasing success rate should be discussed more critically, and guidance for when alternative methods might be preferable should be provided.
  - **Resolution test** Discuss the limitations of the approach more explicitly, including the decreasing success rate with system size. Provide guidance on when OPES is likely to be advantageous over REST2 or other methods, and when it may not be suitable. If possible, include a demonstration on a larger or more challenging IDP system.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Abstract
  - **Evidence pointer** Abstract, line "OPES yields reweighted ensembles broadly consistent with REST2 and unbiased simulations"
  - **Issue** The abstract states that OPES yields ensembles "broadly consistent" with other methods, but the results show some differences (e.g., higher helical content in OPES for HTTex1 and ACTR). The term "broadly consistent" is vague and could be misinterpreted.
  - **Required correction** Specify the degree of consistency more precisely, e.g., "consistent within statistical uncertainty for most observables, with modest differences in helical content for larger systems."
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methods, "OPES multithermal simulations"
  - **Evidence pointer** Methods section, paragraph on bias convergence
  - **Issue** The criteria for determining when a bias potential is "converged" are described qualitatively (c(t) reaching a constant value, sampling score above 0.8). More specific quantitative criteria would improve reproducibility.
  - **Required correction** Provide explicit numerical thresholds for convergence, e.g., the maximum allowed fluctuation in c(t) over a specified time window, and the exact definition of the sampling score.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Statistical rigor
  - **Affected element** Figure 2d, autocorrelation analysis
  - **Evidence pointer** Figure 2d, right panels
  - **Issue** The acceleration factors estimated from autocorrelation times and error bars differ substantially (e.g., 2.0–2.5x from ACF vs. 2–3x from error bars for (AAQAA)3, but larger discrepancies for other systems). The manuscript does not discuss why these metrics give different estimates.
  - **Required correction** Add a brief discussion of why the acceleration factors differ between metrics and what this implies for the reliability of the estimates.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Figure 5, panel h
  - **Evidence pointer** Figure 5h
  - **Issue** The free energy landscape in panel h uses a "helical bundle reference structure" that is not clearly defined. It is unclear how this reference was constructed and how it differs from the bound state reference used in panel e.
  - **Required correction** Clarify the definition of the helical bundle reference structure and how it was generated.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Interpretation
  - **Affected element** Discussion, paragraph on functional implications
  - **Evidence pointer** Discussion, "These transiently structured states may reflect an energetic compromise between conformational selection and induced fit"
  - **Issue** The discussion of functional implications is speculative and goes beyond the data presented. While interesting, the connection between the observed transient states and the folding-upon-binding mechanism is not directly tested.
  - **Required correction** Clearly label this section as speculative and consider softening the language, e.g., "may" instead of "could" or "might."

## Risk / unsupported claims
- The claim that OPES uniquely samples transient tertiary states in ACTR that are "not sampled" by REST2 or unbiased simulations is not fully supported, as the comparison may be confounded by differences in sampling efficiency and simulation length.
- The statement that the reweighted OPES ensemble provides "detailed insights into the apo state of ACTR" is somewhat overstated given the modest improvements in agreement with experimental data and the complexity of the reweighting procedure.
- The generalizability of OPES to larger IDP systems is uncertain given the decreasing success rate for bias convergence with system size, which is not discussed critically.
- The functional implications of the transient tertiary states for folding-upon-binding are speculative and not directly tested in this work.
- The claim that OPES is "robust and accessible" is not fully supported by the data, as the method requires careful monitoring of bias convergence and the success rate is low for the largest system studied.

## Assessment against Nature-style criteria
- **Originality** The application of OPES multithermal sampling to IDPs is novel and timely. While enhanced sampling methods for IDPs exist, the systematic comparison with REST2 and unbiased simulations across multiple systems, and the identification of transient tertiary structure in ACTR, provide new insights. The work is original in its specific focus and findings.
- **Scientific importance** The manuscript addresses a significant challenge in the IDP field: generating converged atomistic ensembles that capture rare, functionally relevant states. The demonstration that OPES can access such states in ACTR has implications for understanding folding-upon-binding and for drug discovery targeting IDPs. The methodological guidance is practically useful.
- **Interdisciplinary readership** The work will appeal to computational biophysicists, experimentalists studying IDPs by NMR/SAXS, and researchers in drug discovery. The writing is generally accessible, though the methods section is dense. The biological context of ACTR and its relevance to disease (implicitly) broadens the appeal.
- **Technical soundness** The simulation protocols are well-described and follow best practices. The use of multiple convergence metrics is commendable. However, the central claim about unique sampling of transient states requires stronger evidence, and the reweighting procedure could benefit from more detailed uncertainty analysis. The decreasing success rate for bias convergence is a concern that should be addressed.
- **Readability for nonspecialists** The abstract and introduction are clear and accessible. The results section is well-structured, but the methods section is highly technical and may be challenging for nonspecialists. The figures are informative, but some (e.g., Figure 5h) could be better annotated.

## Recommendation posture
**Supportive if technical concerns are resolved.** The manuscript presents a valuable methodological advance with potentially important biological findings. However, the central claim about unique sampling of transient tertiary structure needs to be substantiated with stronger evidence, and the reweighting procedure requires more rigorous validation. If these concerns are addressed, the work would be suitable for publication in a high-impact journal.