## Review setup
- **Input scope** Full manuscript text (abstract, results, discussion, conclusions, methods) as provided
- **Assessment boundary** Scientific content, technical soundness, and clarity of claims as presented in the supplied text; no external data or supplementary materials were available for verification
- **Shared manuscript claim summary** The authors report a single-molecule electromechanical nanopore trap based on VDAC to measure dissociation kinetics of α-synuclein from lipid membranes. They observe lipid-composition-dependent distributions of unbinding times, including multi-exponential behavior indicative of distinct membrane-bound conformations, and interpret these via a free-energy model with two parameters: membrane dissociation energy and penetration depth.
- **Visible evidence base** Figures 1–7 as described in text; Methods section; no raw data, supplementary information, or figure panels were provided
- **Missing materials affecting confidence** Actual figure images, numerical data tables, statistical details, fitting residuals, and source code for modeling were not available; these limit quantitative verification of the reported fits and error estimates

## Reviewer
- **Overall assessment** This manuscript presents a technically sophisticated application of a biological nanopore to probe single-molecule dissociation kinetics of a peripherally bound membrane protein. The central observation—that α-synuclein exhibits multiple unbinding timescales on certain lipid compositions—is potentially significant for understanding membrane-protein interactions. However, the strength of the conclusions depends heavily on the modeling framework and on the interpretation of multi-exponential distributions, and several aspects of the evidence chain require clarification or additional support before the claims can be considered fully established.

- **Who would be interested in the results, and why** Researchers in single-molecule biophysics, nanopore sensing, membrane biophysics, and protein-lipid interactions would find this work of interest. The methodological advance—using VDAC as an electromechanical trap to interrogate membrane-bound protein conformations—could be broadly applicable. The specific findings on α-synuclein may also appeal to the Parkinson's disease research community, though the direct disease relevance is not developed in this manuscript.

- **Major strengths** The experimental design is elegant, combining a well-characterized nanopore with a biologically relevant intrinsically disordered protein. The voltage-tunable nature of the trap is a clear advantage, allowing systematic exploration of dissociation kinetics. The use of electrolyte gradients to distinguish retraction from translocation events is a clever and powerful approach. The modeling framework is physically motivated and provides interpretable parameters. The observation of multi-exponential unbinding kinetics is intriguing and potentially important.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of data interpretation
- **Claim pointer** The manuscript claims that multi-exponential distributions of τb indicate the presence of multiple distinct membrane-bound conformations of α-synuclein on the same lipid surface.
- **Evidence pointer** Figures 2, 3, 5; Discussion section "Multiple characteristic dissociation times arise from disordered binding configurations"
- **Concern** The interpretation of multi-exponential unbinding time distributions as evidence for distinct conformational populations rests on the assumption that the observed kinetics are not complicated by other factors, such as voltage-dependent changes in the trap potential, interactions between α-synuclein molecules, or heterogeneity in the lipid membrane itself. The manuscript does not provide a rigorous statistical comparison (e.g., log-likelihood ratio tests or information criteria) between single- and multi-exponential models, nor does it address whether the two-exponential fits are uniquely determined by the data. Additionally, the possibility that the long-lived population arises from α-synuclein oligomers is mentioned but not experimentally distinguished from a monomeric conformational variant.
- **Why it matters** The central novel claim of the paper is the existence of multiple binding conformations. If the multi-exponential behavior can be explained by alternative mechanisms, the conclusion is substantially weakened.
- **Resolution test** Provide statistical model comparison (e.g., AIC or BIC) for single- vs. multi-exponential fits across all conditions; include experiments at varying α-synuclein concentrations to test for oligomerization effects; or provide independent evidence (e.g., single-molecule FRET or MD simulations) for distinct conformational states.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of modeling
- **Claim pointer** The free-energy model with parameters Eb and xb is claimed to quantitatively reproduce the observed τoff(V) for all lipid compositions.
- **Evidence pointer** Figures 3, 4, 6, 7; Methods "Modeling and Optimization"
- **Concern** The model fitting procedure is described only briefly. Key details are missing: the form of the electrokinetic free energy term, the treatment of the membrane dissociation barrier (error function), the choice of prior distributions for MCMC, and the assessment of convergence and identifiability of the two parameters. The manuscript states that confidence intervals are calculated from the last 24,528 of at least 744,528 samples, but no convergence diagnostics (e.g., Gelman-Rubin) are reported. Furthermore, the model assumes a single dissociation barrier, yet the data show multi-exponential behavior; it is unclear how the model accounts for the second, slower population. The fit shown in Figure 7 appears to treat τoff(1) and τoff(2) separately, but the relationship between the two populations and the model parameters is not clearly articulated.
- **Why it matters** The quantitative interpretation of the data in terms of physical parameters (Eb, xb) is a key deliverable of the paper. If the model is not rigorously validated or if parameters are not identifiable, the physical conclusions are not reliable.
- **Resolution test** Provide full model equations, prior distributions, convergence diagnostics, and posterior predictive checks. Clarify how the model is applied to multi-exponential data and whether the two populations are modeled independently or within a unified framework.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance / generalizability
- **Claim pointer** The authors state that the electromechanical nanopore trap provides a "local, single-molecule probe of dissociation kinetics of membrane-bound proteins" with "profound implications for our understanding of protein-lipid interactions."
- **Evidence pointer** Conclusions section
- **Concern** While the method is demonstrated for α-synuclein on a limited set of lipid compositions, the generalizability to other peripheral membrane proteins is not demonstrated. The manuscript does not discuss potential limitations of the approach, such as the requirement for a charged disordered domain for capture, the effect of the lipid bilayer on VDAC gating, or whether the method can be extended to proteins with different structural features. The claim of "profound implications" is somewhat overstated given the single-protein demonstration.
- **Why it matters** The broader significance of the work depends on its applicability beyond the specific system studied. Without discussion of limitations and generalizability, the impact may be overstated.
- **Resolution test** Add a discussion of the scope and limitations of the method, and ideally include a proof-of-concept experiment with a second protein or a mutated α-synuclein variant to demonstrate generalizability.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility and data availability
- **Claim pointer** All experimental results and modeling are presented as described in the text and figures.
- **Evidence pointer** Methods section; Figures 1–7
- **Concern** The manuscript does not state whether raw data or analysis code are available. Given the complexity of the data analysis (event detection, histogram fitting, MCMC optimization), reproducibility would be greatly enhanced by depositing raw current traces, analysis scripts, and model code in a public repository. The Methods section provides some detail but not enough for an independent group to reproduce the analysis without significant effort.
- **Why it matters** Reproducibility is a core expectation for high-impact publications, especially for methods-heavy papers.
- **Resolution test** Provide a data availability statement and deposit raw data and code in a public repository (e.g., Zenodo, GitHub).

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 1F and associated text
- **Evidence pointer** Results section "Determination of dissociation rates using the VDAC nanopore"
- **Issue** The description of the biphasic behavior of τoff(V) and the crossover potential V* is clear, but the relationship between the retraction line and the measured τoff(V) in Figure 1F could be more explicitly described in the text. The reader must infer the meaning of the dashed line and the crossover.
- **Required correction** Add a sentence explicitly defining the retraction line and explaining how V* is determined from the intersection of the two regimes.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figures 2–5
- **Evidence pointer** Results sections; figure captions not provided
- **Issue** The manuscript reports characteristic times and contributions of exponential components (e.g., 64% and 36% for DOPC) but does not report uncertainties on these values. Given the claim of population heterogeneity, error bars or confidence intervals on the fitted fractions would strengthen the interpretation.
- **Required correction** Report uncertainties (e.g., standard errors or confidence intervals) for all fitted parameters, including exponential amplitudes and time constants.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Use of "conformation" throughout
- **Evidence pointer** Abstract; Discussion
- **Issue** The term "conformation" implies a specific structural state. The data presented here report kinetic populations, which may correspond to different conformations, but this is an inference. The manuscript could be more careful in distinguishing between "kinetic populations" and "structural conformations."
- **Required correction** Consider using "kinetic populations" or "binding modes" where structural evidence is not available, and reserve "conformation" for cases where structural information supports it.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Event detection criteria
- **Evidence pointer** Methods "Open and blockage times analysis"
- **Issue** The threshold for event detection is described (0.75 times open current), but the criteria for distinguishing capture events from noise, and for determining the end of an event, are not fully specified. This is important for reproducibility.
- **Required correction** Provide additional detail on event detection, including minimum event duration, filtering parameters, and how baseline drift was handled.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The manuscript does not discuss alternative single-molecule approaches to studying membrane protein dissociation (e.g., optical tweezers, AFM, TIRF-based assays) and how the present method compares in terms of time resolution, force application, and information content.
- **Required correction** Add a brief comparison with existing methods to contextualize the novelty and advantages of the nanopore trap.

## Risk / unsupported claims
- The claim that multi-exponential unbinding kinetics directly reflect "multiple binding conformations" is not fully supported without ruling out alternative explanations (e.g., oligomerization, lipid heterogeneity, voltage effects).
- The statement that the method has "profound implications" for understanding protein-lipid interactions is not supported by the single-protein demonstration presented.
- The quantitative values of Eb and xb derived from the model are presented as reliable, but the lack of convergence diagnostics and model validation makes these values difficult to assess.
- The claim that τoff(1) depends "strongly on the lipid headgroup charge but is relatively insensitive to the type of the headgroup" is based on a limited set of lipid compositions and may not be generalizable.
- The relationship between the two exponential populations (τoff(1) and τoff(2)) and the model parameters is not clearly established; the manuscript does not explain how a single-barrier model produces two distinct timescales.