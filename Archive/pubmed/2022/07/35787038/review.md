## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific claims, methodology, and interpretation as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors report that phase-separating RNA-binding proteins from the FET family (FUS, EWSR1, TAF15) and hnRNP-A3 form heterogeneous, heavy-tailed distributions of clusters in subsaturated solutions, below the saturation concentration for macroscopic phase separation. They propose that these clusters arise from at least two separable energy scales, consistent with associative polymer behavior, and that this framework better describes condensate formation than simple Flory-Huggins models.
- **Visible evidence base** Main text figures 1-12 as referenced; SI Appendix figures S1-S24 as referenced; methods descriptions for DLS, NTA, MFD, MCS, TEM, mutagenesis, and LaSSI simulations
- **Missing materials affecting confidence** SI Appendix content not provided; raw data not provided; detailed experimental protocols not provided; figure images not provided

## Reviewer
- **Overall assessment** This manuscript presents a potentially important observation that subsaturated solutions of phase-separating proteins contain heterogeneous clusters, challenging the implicit assumption that dilute phases are featureless. The combination of multiple orthogonal biophysical techniques (DLS, NTA, MFD, MCS, TEM) is commendable. However, the evidence base as presented has several gaps that limit confidence in the central claims. The interpretation of DLS data, the quantitative analysis of cluster size distributions, and the connection between simulations and experiments require further scrutiny. The claim that clusters are equilibrium species with heavy-tailed distributions is plausible but not fully established from the provided evidence.
- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, phase separation, intrinsically disordered proteins, and biophysics of macromolecular assembly. The results challenge existing frameworks for understanding condensate formation and may have implications for cellular organization, stress response, and disease mechanisms involving RNA-binding proteins.
- **Major strengths** 1) The study addresses an underappreciated aspect of phase-separating systems, namely the nature of subsaturated solutions. 2) The use of multiple orthogonal techniques (DLS, NTA, MFD, MCS, TEM) to probe different size regimes is methodologically rigorous. 3) The inclusion of mutagenesis and solute perturbation experiments provides mechanistic insight. 4) The connection to associative polymer theory offers a coherent conceptual framework. 5) The authors acknowledge and discuss prior work on clusters in other systems, placing their findings in context.
- **Major Concerns** 
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness of DLS interpretation
  - **Claim pointer** The authors claim that DLS data show heavy-tailed distributions of clusters in subsaturated solutions, with cluster sizes increasing with concentration.
  - **Evidence pointer** Fig. 2, SI Appendix Figs. S2-S4
  - **Concern** The DLS data are presented as intensity-weighted size distributions. Intensity weighting heavily biases toward larger particles, and the conversion from intensity to number or mass distributions requires knowledge of particle shape, refractive index, and optical properties. The authors do not provide details on how the DLS data were inverted to obtain size distributions, nor do they discuss the assumptions made. The claim of "heavy-tailed distributions" is based on intensity-weighted data, which may not reflect the true number-weighted distribution. Additionally, the presence of a small number of large aggregates could dominate the intensity signal and produce apparent heavy tails.
  - **Why it matters** The central claim of the paper, that subsaturated solutions contain heterogeneous clusters with heavy-tailed size distributions, rests critically on the correct interpretation of DLS data. If the apparent heavy tails are artifacts of intensity weighting or dust/aggregate contamination, the main conclusion would be undermined.
  - **Resolution test** The authors should provide number-weighted or mass-weighted size distributions, or at minimum discuss the conversion from intensity-weighted data. They should also show that the results are robust to sample preparation, filtration, and data analysis methods. Control experiments with monomeric proteins of known size would help validate the DLS analysis.
  
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Quantitative analysis of cluster size distributions
  - **Claim pointer** The authors claim that cluster size distributions are heavy-tailed and shift toward larger sizes with increasing concentration, and that the distributions are consistent with isodesmic association models.
  - **Evidence pointer** Figs. 2, 4, 5, 7; SI Appendix Figs. S6, S13
  - **Concern** The manuscript does not provide quantitative fits of the size distributions to specific models (e.g., Weibull, power-law, or isodesmic association models). The claim that distributions are "likely to be exponentials with heavy tails, such as Weibull distributions" is presented without statistical analysis or model comparison. The NTA data (Fig. 4) provide number-based distributions, but the analysis is limited to reporting the fraction of molecules in mesoscale clusters. No quantitative characterization of the full size distribution is provided. The fluorescence anisotropy and MFD data are qualitative indicators of cluster formation but do not provide size distributions.
  - **Why it matters** The distinction between a heavy-tailed distribution and other distribution shapes (e.g., exponential, log-normal) is central to the authors' interpretation that clusters form via isodesmic associations without a threshold. Without quantitative model fitting and statistical comparison, this claim is not established.
  - **Resolution test** The authors should fit the NTA and DLS data to specific distribution models (e.g., exponential, Weibull, power-law) and report goodness-of-fit statistics. They should also test whether the data are consistent with isodesmic association models by comparing predicted and observed concentration dependencies of cluster size distributions.
  
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence for equilibrium nature of clusters
  - **Claim pointer** The authors claim that clusters are equilibrium species that form and dissolve via reversible associations, and that they are not prenucleation clusters or kinetic intermediates.
  - **Evidence pointer** Fig. 7, SI Appendix Figs. S13-S14
  - **Concern** The evidence for reversibility is based on DLS measurements showing that cluster sizes decrease upon dilution and increase with concentration. However, the timescales of these measurements are not clearly stated. If the system has not reached equilibrium at the time of measurement, the observed clusters could be kinetically trapped states. The FRET experiments (Fig. 7E) show exchange between clusters, but the interpretation depends on the timescale of the measurements and the assumption that the FRET signal reflects exchange rather than other processes (e.g., photobleaching, conformational changes). The authors do not provide a quantitative analysis of the kinetics of cluster formation and dissolution.
  - **Why it matters** The claim that clusters are equilibrium species is important for the interpretation that they are relevant to cellular conditions and that their size distribution is thermodynamically determined. If the clusters are kinetic intermediates, the implications for cellular function would be different.
  - **Resolution test** The authors should provide time-resolved measurements showing that cluster size distributions reach a steady state and that the steady-state distributions are independent of the starting conditions (e.g., dilution from high concentration vs. concentration from low concentration). They should also measure the kinetics of cluster formation and dissolution and compare these to predictions from isodesmic association models.
  
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Generalizability to other FET family proteins
  - **Claim pointer** The authors claim that other FET family proteins (EWSR1, TAF15) and hnRNP-A3 also form clusters in subsaturated solutions.
  - **Evidence pointer** Fig. 6, SI Appendix Figs. S9-S12
  - **Concern** The data for EWSR1, TAF15, and hnRNP-A3 are limited to DLS measurements. The authors do not provide NTA, MFD, or MCS data for these proteins, nor do they show that the clusters have similar properties (e.g., reversibility, response to mutations) as those formed by FUS. The claim that this is a general property of the FET family is therefore based on limited evidence.
  - **Why it matters** The generalizability of the findings is important for the broader significance of the work. If the clustering behavior is specific to FUS under the conditions tested, the implications for other RNA-binding proteins would be less clear.
  - **Resolution test** The authors should provide additional characterization of clusters formed by EWSR1, TAF15, and hnRNP-A3 using at least one orthogonal technique (e.g., NTA or fluorescence-based methods). They should also test whether the clusters formed by these proteins respond similarly to mutations and solutes as those formed by FUS.
  
  - **Concern ID** R1-M5
  - **Severity** Major
  - **Blocking** No
  - **Axis** Relevance of simulation results to experimental observations
  - **Claim pointer** The authors claim that simulations of associative polymers with two energy scales reproduce the experimentally observed heavy-tailed cluster size distributions and the decoupling of cluster formation from phase separation.
  - **Evidence pointer** Fig. 12, SI Appendix Fig. S24
  - **Concern** The simulation results are presented as a qualitative demonstration of the conceptual framework, but no quantitative comparison between simulations and experiments is provided. The parameters used in the simulations (e.g., interaction strengths, polymer length, concentration range) are not systematically varied to match experimental conditions. The claim that the simulations "show that systems featuring at least two energy scales behave very differently from those with a single energy scale" is supported, but the connection to the specific experimental systems is not established.
  - **Why it matters** The simulations are used to support the interpretation that the experimental observations are consistent with associative polymer behavior. Without quantitative comparison, the simulations serve only as a proof-of-concept and do not strengthen the specific claims about FET family proteins.
  - **Resolution test** The authors should either provide quantitative predictions from the simulations that can be compared to experimental data (e.g., predicted cluster size distributions as a function of concentration) or clearly state that the simulations are illustrative and not intended as quantitative models of the experimental systems.
  
- **Minor Comments** 
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity of terminology
  - **Affected element** Use of "subsaturated" and "saturation concentration"
  - **Evidence pointer** Throughout
  - **Issue** The terms "subsaturated" and "csat" are used throughout, but the operational definition of csat is only briefly described in the methods. It would be helpful to clarify whether csat is defined as the concentration at which macroscopic phase separation is first detected by the spin-down assay, and whether this is consistent across techniques.
  - **Required correction** Provide a clear operational definition of csat and state whether the same definition is used for all proteins and conditions.
  
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Statistical analysis
  - **Affected element** Quantification of cluster abundance
  - **Evidence pointer** Fig. 4C, SI Appendix Fig. S6
  - **Issue** The fraction of molecules in mesoscale clusters is reported as a single value (0.15% for 250 nM FUS-SNAP) without error bars or replicate information. It is unclear how many independent measurements were performed and what the variability is.
  - **Required correction** Report the number of replicates and provide error estimates for the quantified values.
  
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Interpretation of mutagenesis results
  - **Affected element** Fig. 10, SI Appendix Figs. S18-S22
  - **Issue** The mutagenesis experiments show that mutations affect cluster abundance and phase separation, but the interpretation is somewhat qualitative. For example, the statement that "substitution of aromatic Tyr residues with Ser in the PLD of full-length FUS abrogates phase separation in the low micromolar range while also lowering the abundance of mesoscale clusters by over an order of magnitude" does not specify whether the effect on clusters is proportional to the effect on phase separation.
  - **Required correction** Provide a more quantitative comparison of the effects of mutations on cluster formation versus phase separation, and discuss whether the results support a specific mechanistic model.
  
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Discussion of alternative interpretations
  - **Affected element** Discussion section
  - **Issue** The authors interpret their results as evidence for associative polymer behavior with two energy scales. However, alternative explanations for the observed clusters, such as transient aggregation due to incomplete folding or non-specific interactions, are not discussed in detail.
  - **Required correction** Add a brief discussion of alternative interpretations and why the data favor the associative polymer framework.
  
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Reproducibility of sample preparation
  - **Affected element** Methods section
  - **Issue** The methods state that proteins were expressed in insect cells and purified using two different methods (A and B), but the details are in the SI Appendix. It is unclear whether the clustering behavior is sensitive to the purification method.
  - **Required correction** State explicitly whether the clustering behavior was consistent across purification methods and provide the relevant data or reference to the SI Appendix.
  
- **Technical failings that need to be addressed before the case is established** R1-M1 (DLS interpretation), R1-M2 (quantitative analysis of size distributions), R1-M3 (equilibrium nature of clusters)
- **Assessment against Nature-style criteria** 
  - Originality: The observation that subsaturated solutions of phase-separating proteins contain heterogeneous clusters is novel and challenges existing assumptions. The application of associative polymer theory to this problem is conceptually original.
  - Scientific importance: The findings have potential implications for understanding the early stages of condensate formation and the behavior of phase-separating proteins at physiological concentrations. If confirmed, the results could influence how condensate formation is studied and interpreted.
  - Interdisciplinary readership: The work bridges biophysics, polymer physics, and cell biology, and would be of interest to researchers in these fields. The conceptual framework is accessible, though some technical details may be challenging for non-specialists.
  - Technical soundness: The use of multiple orthogonal techniques is a strength, but the quantitative analysis of the data is incomplete. The DLS interpretation and the lack of model fitting for size distributions are significant weaknesses.
  - Readability for nonspecialists: The manuscript is generally well-written and the main concepts are explained clearly. The significance statement and introduction provide good context. However, some sections, particularly the simulation results, may be difficult for non-specialists to follow.
- **Recommendation posture** Supportive if technical concerns are resolved. The central observation is potentially important, but the evidence as presented does not fully establish the claims of heavy-tailed distributions, equilibrium behavior, and the associative polymer framework. The authors should address the concerns regarding DLS interpretation, provide quantitative analysis of size distributions, and strengthen the evidence for the equilibrium nature of the clusters.

## Risk / unsupported claims
- The claim that cluster size distributions are "likely to be exponentials with heavy tails, such as Weibull distributions" is not supported by quantitative model fitting.
- The claim that clusters are equilibrium species is not fully established, as the timescales of measurements and the kinetics of cluster formation/dissolution are not clearly characterized.
- The claim that the observed clusters are relevant to cellular conditions is speculative, as the experiments are performed in vitro with purified proteins.
- The claim that the simulation results support the experimental observations is not quantitatively demonstrated.
- The generalizability of the findings to other FET family proteins is based on limited data (DLS only for EWSR1, TAF15, hnRNP-A3).