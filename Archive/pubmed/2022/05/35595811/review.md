## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary figure legends
- **Assessment boundary** Scientific content, methodological rigor, logical coherence, and support of claims by presented evidence
- **Shared manuscript claim summary** The disordered N terminus of the ATP-independent chaperone Spy facilitates client protein release through transient electrostatic interactions with the client-binding cavity, primarily mediated by residue D26, which competes with client proteins for binding and promotes their discharge without ATP input
- **Visible evidence base** Mutagenesis and truncation studies, anti-aggregation activity assays, biolayer interferometry kinetics, NMR spectroscopy including PRE experiments, MD simulations, sequence conservation analysis, and bacterial growth assays
- **Missing materials affecting confidence** Supplementary figures and tables referenced but not fully provided; raw NMR spectra and MD trajectory details not available; source data files not accessible

## Reviewer
- **Overall assessment** This manuscript presents a compelling and mechanistically detailed investigation into how the intrinsically disordered N terminus of the chaperone Spy facilitates client protein release. The combination of biochemical assays, kinetics measurements, NMR spectroscopy, and MD simulations provides a multi-pronged approach that largely supports the central claim. The identification of D26 as a key residue mediating electrostatic interactions with the positively charged concave surface is well supported by mutagenesis and PRE data. The work addresses an important gap in understanding how ATP-independent chaperones release clients, and the proposed competitive displacement mechanism is conceptually novel. However, several concerns regarding quantitative rigor, statistical treatment, and the physiological relevance of the findings require attention before the conclusions can be fully accepted.

- **Who would be interested in the results, and why** Researchers in the fields of protein folding, molecular chaperones, and intrinsically disordered proteins would find this work of significant interest. The study provides mechanistic insight into how disordered regions can actively regulate chaperone function, which has broader implications for understanding the functional roles of IDRs in protein homeostasis. Additionally, those studying Spy as a model chaperone system and those interested in the biophysics of protein-protein interactions involving disordered regions would benefit from these findings. The work may also appeal to researchers investigating autoregulatory mechanisms in other chaperone systems, as the authors draw parallels to Hfq and sHsps.

- **Major strengths** The study employs a well-integrated combination of experimental and computational approaches. The truncation series provides a systematic structure-function analysis. The identification of D26 through a combination of mutagenesis, kinetics, and PRE experiments is logically developed. The MD simulations complement the experimental data and provide a dynamic picture of N terminus behavior. The inclusion of multiple client proteins with different folding states strengthens the generality of the conclusions. The growth assays provide a physiological context for the mechanistic findings.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative rigor of kinetics measurements
- **Claim pointer** The manuscript claims significant differences in dissociation constants and dissociation rate constants between Spy variants, with specific fold-changes reported (e.g., "2.9-8.6 fold increases in the Kd" for aspartate variants in the absence of the N terminus).
- **Evidence pointer** Figure 1d-f, Figure 2c-e, Figure 4c, Supplementary Figures 1d-i and 6
- **Concern** The biolayer interferometry experiments report kinetic parameters, but the manuscript does not provide sufficient detail on the number of independent experiments, the reproducibility of the measurements, or the error analysis. While n values are stated for some experiments, the statistical comparisons between variants appear to be pairwise without correction for multiple comparisons. More critically, the kon values are derived from kobs versus concentration plots, but the concentration range used and the linearity of these plots are not shown. The manuscript also does not report goodness-of-fit parameters for the kinetic models used.
- **Why it matters** The central conclusion that the N terminus specifically affects koff rather than kon depends entirely on the reliability of these kinetic measurements. If the kinetic parameters are not robustly determined, the mechanistic interpretation could be incorrect. The distinction between effects on association versus dissociation is fundamental to the proposed competitive displacement model.
- **Resolution test** Provide full details of the BLI experimental design including number of replicates, concentration ranges, fitting procedures, and goodness-of-fit statistics. Show representative raw sensorgrams and the kobs versus concentration plots used to derive kon. Apply appropriate multiple comparison corrections where multiple variants are compared.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Support for the competitive displacement model
- **Claim pointer** The manuscript claims that "the N terminus can directly compete with the client for binding to Spy, which is the basis for promoting client release" and that the binding sites of the N terminus and clients overlap.
- **Evidence pointer** Figure 5, Figure 6, Supplementary Figures 8-10
- **Concern** The CSP experiments comparing the binding sites of Im7A3 and the N terminus on Spy show similar patterns, but the manuscript does not provide a quantitative comparison of the two binding interfaces. The claim of "overlapping binding regions" is based on visual inspection of CSP patterns rather than a statistical or quantitative analysis. Furthermore, the competition experiments with Nt-pep show inhibition of Spy activity only at high peptide concentrations (14-fold excess), raising questions about whether the proposed competition is physiologically relevant given that the N terminus is present at 1:1 stoichiometry in the native protein.
- **Why it matters** The competitive displacement model is the central mechanistic proposal of the paper. If the binding sites do not truly overlap, or if the competition is too weak to be physiologically relevant, the proposed mechanism would need to be revised. The quantitative weakness of the N terminus binding (Kd of 4.7 mM) compared to client binding raises questions about how effective this competition can be in vivo.
- **Resolution test** Provide a quantitative comparison of the CSP patterns (e.g., correlation analysis or statistical test for similarity). Discuss the physiological relevance of the mM Kd for N terminus binding in the context of in vivo concentrations of Spy. Consider whether the competition mechanism is kinetically feasible given the relative affinities.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** MD simulation methodology and interpretation
- **Claim pointer** The manuscript claims that MD simulations show the N terminus "readily swings into the positively charged, client-binding cavity of Spy" and that mutations of D26 affect this behavior.
- **Evidence pointer** Figure 4d, Supplementary Figures 4 and 7, Supplementary Data 1
- **Concern** The MD simulation methodology has several potential issues. First, the simulations were performed at 310 K while the experimental measurements were at 298 K, and the authors state this was done to increase conformational sampling, but this temperature difference could affect the electrostatic interactions being studied. Second, the filtering procedure to exclude starting conformations where D26 is already in the cavity introduces potential bias. Third, the manuscript does not report convergence criteria, error estimates, or replicate simulations. The distance distributions shown appear to be from single trajectories.
- **Why it matters** The MD simulations are used to support the structural interpretation of the experimental data. If the simulations are not converged or are biased by the starting structure selection, the conclusions drawn from them may not be reliable. The temperature difference and the filtering procedure could both affect the observed behavior of the N terminus.
- **Resolution test** Provide details on simulation convergence, replicate simulations, and error analysis. Justify the temperature choice and the filtering procedure. Show that the conclusions are robust to different starting conditions and analysis methods.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Physiological relevance of the proposed mechanism
- **Claim pointer** The manuscript claims that the N terminus-mediated client release mechanism is evolutionarily conserved and physiologically important, citing sequence conservation of D26 and growth phenotypes.
- **Evidence pointer** Supplementary Figures 11-12
- **Concern** The growth assay data are presented only in supplementary material and the statistical analysis is not described in detail. The manuscript states that overexpression of Spy29-138 in a Δspy strain resulted in decreased fitness, but the magnitude of the effect and its reproducibility are not clear. The sequence conservation analysis shows conservation of acidic residues at position 26, but the analysis is not described in sufficient detail to assess its rigor.
- **Why it matters** The claim that this mechanism is physiologically relevant and evolutionarily conserved strengthens the significance of the work. If the growth phenotypes are weak or the conservation analysis is not rigorous, the broader significance of the findings would be diminished.
- **Resolution test** Provide full statistical details of the growth assays including replicates and effect sizes. Describe the sequence conservation analysis methodology, including the number of sequences analyzed and the criteria for conservation.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure presentation
- **Affected element** Figure 1c
- **Evidence pointer** Figure 1c
- **Issue** The anti-aggregation activity data are presented as relative activities normalized to wild type, but the absolute activities and the raw aggregation curves are not shown for all variants. This makes it difficult to assess the magnitude of the effects.
- **Required correction** Show representative raw aggregation curves for key variants in supplementary material, and clearly state the normalization procedure used.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Throughout results
- **Evidence pointer** Figures 1-4
- **Issue** The manuscript uses "mean ± SD" for some measurements but does not consistently report the number of replicates for all experiments. Some statistical comparisons are described but the specific tests used are not always stated.
- **Required correction** Provide a consistent reporting of n values and statistical tests for all quantitative measurements, either in figure legends or in a dedicated statistics section.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Discussion of alternative mechanisms
- **Affected element** Discussion section
- **Evidence pointer** Discussion
- **Issue** The manuscript proposes the competitive displacement mechanism but does not discuss alternative explanations for the observed effects, such as allosteric regulation or conformational changes in Spy upon N terminus binding.
- **Required correction** Add a brief discussion of alternative mechanisms and why the data support the competitive model over these alternatives.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Nomenclature consistency
- **Affected element** Throughout
- **Evidence pointer** Figures 1-6
- **Issue** The manuscript uses both "Spy29-138" and "SpyΔN" style nomenclature in different places, which could cause confusion.
- **Required correction** Standardize the nomenclature for Spy variants throughout the manuscript.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** MD simulations
- **Evidence pointer** Methods section
- **Issue** The methods for MD simulations lack some details such as the specific water model parameters, the equilibration protocol, and the criteria for determining when the system reached equilibrium.
- **Required correction** Provide complete details of the MD simulation protocol to ensure reproducibility.

## Risk / unsupported claims
- The claim that the N terminus "can directly compete with the client for binding to Spy" is supported by indirect evidence (CSP patterns and peptide competition) but direct competition experiments showing displacement of bound client by the N terminus are not presented
- The statement that "the presence of a negative charge at the 26th position facilitates the release of Spy clients but does not interfere with the initial client-binding process" is based on kon measurements that may not be sufficiently robust
- The physiological relevance claim based on growth assays is not fully supported by the data presented, as the statistical analysis and effect sizes are not clearly described
- The evolutionary conservation argument for D26 is presented without sufficient methodological detail to assess its rigor
- The MD simulation results are used to support structural conclusions but the simulations may not be converged or sufficiently replicated to support these claims definitively