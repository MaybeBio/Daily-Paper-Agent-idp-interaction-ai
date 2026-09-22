## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, conclusion) without supplementary materials or figures
- **Assessment boundary** Scientific claims, methodology as described, interpretation of results, and internal consistency of the presented evidence
- **Shared manuscript claim summary** The authors combine single-molecule AFM force spectroscopy and QM/MM simulations to show that the Zn4S11 cluster in the α-domain of human metallothionein-III unfolds via multiple pathways with at least eight intermediates, that the metal cluster is highly dynamic and can reconfigure spontaneously in the folded protein, and that cluster topology rather than metal identity determines unfolding behavior.
- **Visible evidence base** Text descriptions of AFM-SMFS experiments, force-extension curves, contour length measurements, kinetic parameters from dynamic force spectroscopy, and QM/MM simulation results. Figures and tables are referenced but not directly viewable.
- **Missing materials affecting confidence** Supplementary figures (S1–S12), Supplementary Notes 1–5, Supplementary Methods, source data files, and all actual figures/tables. Without these, quantitative claims cannot be independently verified.

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question about the dynamic behavior of polynuclear metal clusters in metallothionein, a protein central to metal homeostasis and detoxification. The combination of single-molecule force spectroscopy with QM/MM simulations is well suited to reveal heterogeneity that ensemble methods average out. The observation of multiple unfolding pathways and spontaneous cluster reconfiguration is potentially significant. However, the manuscript as presented has several issues that need to be addressed: the evidence for the key claims is described rather than shown, the statistical treatment of the pathway assignments is not fully described, and the connection between the mechanical unfolding results and the physiological relevance of cluster dynamics requires more careful articulation. The work is likely of interest to the biophysics, metalloprotein, and single-molecule communities, but the current presentation does not fully establish all claims.

- **Who would be interested in the results, and why** Researchers in single-molecule biophysics (AFM-based force spectroscopy), metalloprotein biochemistry, and bioinorganic chemistry would find this work relevant. The demonstration that a polynuclear metal cluster can sample multiple configurations on short timescales has implications for understanding metal exchange, metallation pathways, and the functional versatility of metallothionein. The methodological approach combining AFM with QM/MM simulations may also interest method developers.

- **Major strengths**  
  1. The combination of single-molecule AFM with QM/MM simulations is powerful and appropriate for studying dynamic, heterogeneous systems.  
  2. The observation of multiple unfolding pathways with at least eight intermediates is a novel result that challenges the view of MT domains as rigid, cooperatively unfolding units.  
  3. The comparison between Zn- and Cd-bound forms provides insight into metal-specific effects on cluster stability.  
  4. The spontaneous cluster reconfiguration observed in simulations of the folded protein is an intriguing finding with potential functional implications.

- **Major Concerns**

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** "Unusual multiple unfolding pathways and intermediates are observed for both domains, corresponding to different combinations of M-S bond rupture. None of the pathways is clearly preferred."  
- **Evidence pointer** Section 2.2, Figures 3(b)–3(d), Table 1, Figure S5, Figure S7  
- **Concern** The claim that multiple pathways exist with similar frequencies is based on deconvolution of a measured ΔLc histogram into four Gaussian components (P1–P4). However, the manuscript does not describe how this deconvolution was performed, what fitting criteria were used, whether the number of components was determined statistically (e.g., by AIC or BIC), or how robust the assignment is to alternative fitting models. The reported counts (n = 132, 98, 86, 90) sum to 406, but the uncertainty in these assignments is not given.  
- **Why it matters** The central conclusion of the paper—that multiple unfolding pathways exist with similar probabilities—depends entirely on the correctness of this deconvolution. If the histogram can be fit equally well with fewer or differently positioned components, the conclusion would be weakened.  
- **Resolution test** Provide details of the fitting procedure, including the model selection criteria, confidence intervals for the component positions and areas, and a sensitivity analysis showing that the four-component model is statistically preferred over alternatives. Show the raw histogram with the fitted components overlaid.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** "Simulations indicate that the metal cluster may rearrange, forming and breaking metal-thiolate bonds even when MT is folded independently of large protein backbone reconfiguration."  
- **Evidence pointer** Section 2.3, Figure 5, SI Video  
- **Concern** The QM/MM simulations showing spontaneous cluster reconfiguration are described only briefly. The manuscript states that "reactive MD trajectories" showed bond formation and rupture, but the simulation protocol, the number of trajectories, the timescales, the QM region definition, and the level of QM theory are not described in the main text. The reader is referred to Supplementary Methods, which is not provided. Without these details, it is impossible to assess whether the observed reconfigurations are artifacts of the simulation setup or genuine features of the system.  
- **Why it matters** The claim of spontaneous cluster dynamics in the folded protein is a key finding with implications for MT function. If the simulations are not properly converged or the QM method is inadequate for describing M-S bond breaking, the conclusion may not hold.  
- **Resolution test** Provide full details of the QM/MM setup, including the QM region, basis set, exchange-correlation functional, ensemble, thermostat, simulation length, number of replicas, and criteria for identifying bond breaking/formation events. Show that the observed reconfigurations are reproducible across multiple independent trajectories.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** No  
- **Axis** Interpretation  
- **Claim pointer** "The lower stability of the Zn4S11 cluster is due to shorter Zn-S bonds, which perturbs the ring structure of the polynuclear cluster."  
- **Evidence pointer** Section 2.4, Figures 6(a)–6(b), Figure S11  
- **Concern** The manuscript attributes the faster unfolding kinetics of Zn-αMT compared to Cd-αMT to shorter Zn-S bonds perturbing the ring structure. However, the kinetic measurements (koff = 25 s⁻¹ for Zn, 10 s⁻¹ for Cd) are from dynamic force spectroscopy, which measures the force-dependent rupture of the entire cluster, not individual bond strengths. The connection between bond length differences and the measured kinetic parameters is not directly established. Alternative explanations, such as differences in protein flexibility or solvation, are not discussed.  
- **Why it matters** The mechanistic interpretation of the kinetic difference is important for understanding how metal identity modulates cluster stability. If the interpretation is not well supported, the conclusion about the role of bond lengths may be premature.  
- **Resolution test** Provide additional evidence linking bond lengths to kinetic parameters, such as a correlation between simulated bond lengths and measured rupture forces, or a discussion of alternative mechanisms with supporting data.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Completeness  
- **Claim pointer** "Both MT-III domains may unfold with (two-step) or without (one-step) intermediates."  
- **Evidence pointer** Section 2.2, Figure S6  
- **Concern** The manuscript states that two-step unfolding was also observed for the β-domain, but the analysis is not presented in detail. The text says "their similar ΔLc signals hampered a clear identification and characterization of each cluster, so we studied each domain separately," but the β-domain results are only mentioned in a supplementary figure. The number of events, the pathway assignments, and the statistical significance of the two-step events for βMT are not described.  
- **Why it matters** The claim that both domains exhibit multiple unfolding pathways is part of the paper's central message. If the β-domain data are not analyzed with the same rigor as the α-domain, the claim is not fully supported.  
- **Resolution test** Provide a full analysis of the β-domain two-step events, including the ΔLc distribution, the number of events, and the pathway assignments, either in the main text or in a clearly described supplementary section.

- **Minor Comments**

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Section 2.1, Figure 2(b)  
- **Evidence pointer** "curve 2, Figure 2(b)"  
- **Issue** The text states that apo-MT showed "neither 9 or 11 nm peaks," but the grammar is awkward ("neither...or" should be "neither...nor"). More importantly, it is unclear whether the apo-MT control was performed on the full-length protein or on the individual domains.  
- **Required correction** Clarify which construct was used for the apo-MT control and correct the grammar.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Reproducibility  
- **Affected element** Section 2.2, Table 1  
- **Evidence pointer** Table 1  
- **Issue** The table reports counts for each pathway (P1–P4) but does not report the uncertainty or the criteria for assigning individual events to pathways.  
- **Required correction** Add a description of how events were assigned to pathways and report the uncertainty in the counts.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Section 2.3, Figure 4  
- **Evidence pointer** Figure 4  
- **Issue** The text states that "the same 16 M-S bonds were initially present" in the simulations, but it is not clear whether this refers to the Zn- or Cd-bound form, or both.  
- **Required correction** Specify which metal-bound form is shown in each panel of Figure 4.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Interpretation  
- **Affected element** Section 2.4, Figures 6(c)–6(d)  
- **Evidence pointer** Figures 6(c)–6(d)  
- **Issue** The comparison with rubredoxin is interesting, but the text does not explain why rubredoxin is an appropriate control. The difference in protein size, fold, and metal coordination environment could confound the comparison.  
- **Required correction** Add a brief justification for the rubredoxin comparison and discuss potential limitations.

- **Concern ID** R1-m5  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Section 2.2, Figure 3(c)  
- **Evidence pointer** Figure 3(c)  
- **Issue** The text states that the ΔLc distribution is "broad and continuous ranging from 1 to 10 nm," but the number of bins and the sample size are not given.  
- **Required correction** Report the sample size and the binning parameters for the histogram.

- **Concern ID** R1-m6  
- **Severity** Minor  
- **Axis** Reproducibility  
- **Affected element** Section 2.1, Figure 2(c)  
- **Evidence pointer** Figure 2(c)  
- **Issue** The text reports ΔLc values with standard deviations (e.g., 11.6 ± 0.9 nm, n = 43) but does not state how the contour length was calculated from the force-extension curves.  
- **Required correction** Briefly describe the fitting procedure used to extract ΔLc from the worm-like chain or freely jointed chain model.

- **Technical failings that need to be addressed before the case is established**  
  R1-M1 (histogram deconvolution not described), R1-M2 (QM/MM simulation details not provided), R1-M3 (mechanistic interpretation not fully supported), R1-M4 (β-domain analysis incomplete).

- **Assessment against Nature-style criteria**  
  **Originality:** The work is original in its application of single-molecule force spectroscopy to a polynuclear metal cluster in metallothionein and in its observation of multiple unfolding pathways. The finding of spontaneous cluster reconfiguration in the folded protein is novel.  
  **Scientific importance:** The results have implications for understanding metal homeostasis, metallation pathways, and the functional versatility of metallothionein. The demonstration that metal clusters can be highly dynamic challenges static structural views.  
  **Interdisciplinary readership:** The work bridges single-molecule biophysics, computational chemistry, and metalloprotein biochemistry, and should appeal to readers across these fields.  
  **Technical soundness:** The combination of AFM and QM/MM is appropriate, but the lack of methodological detail for both the histogram deconvolution and the simulations prevents full assessment. The kinetic measurements appear sound but the interpretation requires more support.  
  **Readability for nonspecialists:** The manuscript is generally well written and accessible, but some sections assume familiarity with AFM force spectroscopy and QM/MM methods. The abstract is clear and conveys the main findings effectively.

- **Recommendation posture** Supportive if technical concerns are resolved. The core findings are potentially significant, but the manuscript as presented does not fully establish the claims due to insufficient methodological detail and incomplete analysis. If the authors can provide the missing information and address the concerns raised, the work would be suitable for publication.

## Risk / unsupported claims
- The claim of "at least eight intermediates" is not fully supported without details of the histogram deconvolution and its statistical justification.
- The claim of spontaneous cluster reconfiguration in the folded protein is not fully supported without details of the QM/MM simulation protocol and convergence criteria.
- The claim that "none of the pathways is clearly preferred" is not supported without uncertainty estimates for the pathway counts.
- The claim that "the lower stability of the Zn4S11 cluster is due to shorter Zn-S bonds" is an interpretation that is not directly tested.
- The claim that "the Zn3S9 cluster in the β domain is also highly dynamic" is not supported by the same level of analysis as the α domain.
- The physiological relevance of the observed mechanical unfolding pathways to MT function in vivo is asserted but not discussed in detail.