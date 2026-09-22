## Review setup
- **Input scope** Full manuscript text, including abstract, results, discussion, experimental procedures, and figure legends
- **Assessment boundary** Scientific validity, technical soundness, and conceptual advance of the claims presented, based solely on the provided manuscript text
- **Shared manuscript claim summary** The authors propose that ATP-competitive small molecule kinase inhibitors (SMKIs) of the indole maleimide class (BimI, sotrastaurin) allosterically displace the Gly-rich loop (G-loop) of PKCα, disrupting a newly identified C1a-kinase domain regulatory interaction, exposing the C1a DAG-binding site, and enhancing PKCα membrane translocation in vitro and in live cells.
- **Visible evidence base** FRET-based intramolecular interaction assays, in vitro kinase activity assays, live cell membrane translocation imaging, supported lipid bilayer recruitment assays, multiscale molecular dynamics simulations (GNEIMO-REMD and all-atom MD), sequence conservation analysis, and computational binding site identification (FindBindSite)
- **Missing materials affecting confidence** Raw numerical data for FRET and activity assays, statistical test details for all comparisons, MD simulation convergence metrics, force field validation details, full figure panels (especially Fig. 2C correlation plot), and supplementary figures S1–S4

## Reviewer

- **Overall assessment** This manuscript presents an interesting and potentially important finding: that certain ATP-competitive kinase inhibitors can exert allosteric effects beyond the catalytic site by disrupting a regulatory intramolecular interaction, thereby enhancing rather than simply inhibiting PKCα function. The integration of multiscale MD simulations with FRET-based experimental validation is a commendable approach. However, the manuscript has several technical weaknesses that need to be addressed before the central claims are fully established. The correlation between computational predictions and experimental measurements is presented qualitatively, and key statistical details are missing. The mechanistic model, while plausible, relies heavily on simulations that are not fully validated against experimental structures. The distinction between inhibitor classes in their allosteric effects is intriguing but requires more rigorous quantitative support. Overall, the work is conceptually novel and of potential interest to the kinase biology and drug discovery communities, but the current evidence does not fully support all claims as presented.

- **Who would be interested in the results, and why** Researchers in kinase biology, particularly those studying PKC isoforms and their regulation, would find this work relevant. The demonstration that SMKIs can have allosteric effects on regulatory interactions has implications for drug development, as it suggests that inhibitor efficacy may be influenced by effects on protein localization and substrate access. The integrated computational-experimental pipeline could be of interest to structural biologists and computational chemists studying protein dynamics. The findings may also be relevant to clinicians using PKC inhibitors, as the paradoxical enhancement of membrane translocation could have implications for drug efficacy and side effects.

- **Major strengths**
  1. The study addresses a significant gap in understanding the allosteric effects of SMKIs beyond the catalytic site, using a combination of computational and experimental approaches.
  2. The identification and validation of a novel C1a-kinase domain interaction interface is a valuable contribution, given the lack of full-length PKC structures.
  3. The correlation between MD simulation predictions and FRET measurements across multiple inhibitors provides a compelling internal consistency.
  4. The use of multiple experimental systems (in vitro FRET, live cell imaging, supported lipid bilayers) strengthens the biological relevance of the findings.
  5. The study has potential translational implications for understanding how kinase inhibitors may paradoxically enhance certain aspects of PKC function.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of computational predictions
- **Claim pointer** The authors claim that MD simulations predict that BimI and sotrastaurin displace the G-loop, which in turn weakens the C1a-kinase domain interaction, and that these predictions correlate with experimental FRET measurements.
- **Evidence pointer** Results section "Select ATP-competitive SMKIs displace regulatory-kinase domain interactions", Fig. 4C, Experimental procedures "All-atom MD simulations of C1a-kinase domain-PS complex with inhibitors"
- **Concern** The correlation between computational interaction energy changes and experimental FRET measurements is stated qualitatively ("show good correlation") without providing quantitative metrics such as correlation coefficients, confidence intervals, or statistical significance. The MD simulations are performed on a model derived from GNEIMO-REMD, which itself is based on constraints from known interactions, potentially introducing bias. The manuscript does not report convergence of the MD simulations, nor does it validate the force field parameters for the inhibitors against experimental binding data. The choice of the "most occupied conformation cluster" for representative structures is not justified, and the sensitivity of the results to this choice is not explored.
- **Why it matters** The central mechanistic claim relies on the accuracy of the MD simulations. Without quantitative correlation metrics and proper validation, the reader cannot assess whether the simulations genuinely predict the experimental outcomes or whether the agreement is coincidental or forced by the modeling constraints. This is critical because the proposed allosteric mechanism is the main conceptual advance of the paper.
- **Resolution test** Provide quantitative correlation statistics (e.g., Pearson or Spearman correlation coefficients with p-values) between computed interaction energies and experimental FRET changes. Report MD convergence metrics (e.g., RMSD stability, block averaging) and validate inhibitor force field parameters against known binding affinities or crystal structures. Perform sensitivity analysis by testing alternative clustering criteria and starting structures.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor of experimental data
- **Claim pointer** The authors claim that BimI and sotrastaurin significantly inhibit the regulatory-kinase domain interaction, and that staurosporine and tetrahydrostaurosporine have minimal effects, based on FRET measurements.
- **Evidence pointer** Fig. 1C–F, Fig. 2C, Fig. 5D–E, Experimental procedures "FRET measurements"
- **Concern** The manuscript reports significance levels for individual comparisons (e.g., p < 0.0001) but does not provide effect sizes, confidence intervals, or details on multiple comparison corrections. For Fig. 2C, the correlation between FRET measurements and interaction energies is shown for a small number of mutants, but the statistical significance of this correlation is not reported. In Fig. 5, the live cell imaging data show substantial variability, and the statistical comparison between inhibitor conditions is not fully described. The number of independent experiments (N) is stated but the number of cells per condition in live cell imaging is not clearly specified.
- **Why it matters** The conclusions about differential effects of inhibitor classes depend on the reliability of the FRET and imaging measurements. Without proper statistical reporting, the reader cannot determine whether the observed differences are robust or could arise from experimental variability. This is particularly important for the claim that ATP analogs have no effect, which is a negative result that requires adequate statistical power to support.
- **Resolution test** Provide effect sizes with confidence intervals for all key comparisons. Report the number of cells analyzed per condition in live cell imaging and the statistical model used. For the correlation in Fig. 2C, report the correlation coefficient and p-value. Specify whether multiple comparison corrections were applied and, if not, justify their omission.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Biological relevance of the proposed mechanism
- **Claim pointer** The authors claim that SMKI-mediated displacement of the C1a domain exposes the DAG-binding site, enhancing PKCα membrane translocation, and that this is a novel allosteric mechanism with potential implications for PKC inhibitor function.
- **Evidence pointer** Results section "Simulations suggest that inhibitor displacement of the C1a domain unmasks a diacylglycerol binding site", Fig. 5, Fig. 6
- **Concern** The link between the in vitro FRET measurements, the MD simulations, and the live cell membrane translocation data is largely correlative. The manuscript does not directly demonstrate that the enhanced membrane translocation is due to the specific mechanism proposed (G-loop displacement leading to C1a release and DAG site exposure). Alternative explanations, such as inhibitor-induced conformational changes in the C1a domain itself or effects on membrane fluidity, are not ruled out. The experiments are performed with overexpressed fluorescent protein-tagged PKCα, which may not reflect endogenous protein behavior. The concentrations of inhibitors used in live cell experiments are not clearly stated in the results section.
- **Why it matters** The claim of a novel allosteric mechanism has implications for understanding PKC regulation and inhibitor pharmacology. If the mechanism is not directly demonstrated, the conclusions may be overstated. The potential for alternative explanations weakens the conceptual advance and the translational relevance.
- **Resolution test** Perform experiments that directly test the proposed mechanism, such as using PKCα mutants that disrupt the C1a-kinase domain interface and examining whether the inhibitor effect on membrane translocation is abolished. Use endogenous PKCα or more physiologically relevant expression levels. Provide inhibitor concentrations used in live cell experiments and demonstrate that the effects are dose-dependent and specific to the proposed mechanism.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of the computational approach
- **Claim pointer** The authors claim that the integrated computational-experimental paradigm can be applied to investigate parallel allosteric mechanisms in other kinases.
- **Evidence pointer** Discussion section, Experimental procedures "Atomistic model of the C1a-kinase domain binding interface"
- **Concern** The computational pipeline relies on prior knowledge of at least one interaction interface (e.g., PS-kinase domain) to constrain the simulations. For kinases where such information is unavailable, the approach may not be directly applicable. The manuscript does not discuss the limitations of the approach or the conditions under which it would be expected to work. The transferability of the specific findings to other PKC isoforms or other kinases is not addressed experimentally.
- **Why it matters** The claim of generalizability is part of the broader significance of the work. If the approach is limited to cases with known constraints, the impact may be more modest than implied. The reader needs to understand the scope and limitations of the proposed paradigm.
- **Resolution test** Discuss the limitations of the approach in the discussion section. Provide examples or a clear framework for how the method could be applied to kinases without known interaction interfaces. If possible, include preliminary data on another kinase or PKC isoform to demonstrate generalizability.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure presentation
- **Affected element** Fig. 2C
- **Evidence pointer** Results section "De novo identification and validation of the C1a-kinase domain–binding interface"
- **Issue** The correlation between FRET measurements and interaction energies in Fig. 2C is described but the figure itself is not available in the manuscript text. The reader cannot visually assess the quality of the correlation or the scatter of the data points.
- **Required correction** Ensure the figure is clearly presented with labeled axes, error bars, and a fitted line with correlation statistics. Consider including the correlation coefficient and p-value directly on the figure.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Experimental procedures, "Mammalian cell culture and live cell imaging"
- **Evidence pointer** Experimental procedures section
- **Issue** The concentration of DiC8 used for stimulation is stated, but the concentrations of inhibitors used in live cell imaging are not explicitly listed in the results or methods. The DMSO control is mentioned but the final DMSO concentration is not stated.
- **Required correction** Provide the final concentrations of all inhibitors used in live cell imaging experiments and the DMSO concentration in the control condition.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of negative results
- **Affected element** Fig. 1C–F
- **Evidence pointer** Results section "Select ATP-competitive SMKIs displace regulatory-kinase domain interactions"
- **Issue** The manuscript states that ATP analog inhibitors (sangivamycin, toyocamycin) have minimal effects on the regulatory-kinase domain interaction. However, the statistical power to detect a small effect is not discussed. The absence of a significant effect is interpreted as no effect, which may not be justified.
- **Required correction** Discuss the statistical power to detect small effects or provide confidence intervals for the null results. Consider stating that the data are consistent with no effect within the detection limits of the assay.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology precision
- **Affected element** Abstract and Discussion
- **Evidence pointer** Abstract, Discussion section
- **Issue** The term "allosterically disrupt" is used to describe the mechanism. While the authors provide evidence for disruption of an interaction, the term "allosteric" implies a specific mechanism (binding at a site distinct from the orthosteric site). The manuscript could clarify whether the effect is truly allosteric or whether it results from direct competition at the C1a binding site.
- **Required correction** Clarify the use of "allosteric" in the context of the proposed mechanism, and discuss whether the observed effects are consistent with an allosteric model or could also be explained by direct competition.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Data availability statement
- **Affected element** Data availability section
- **Evidence pointer** Data availability section
- **Issue** The data availability statement indicates that starting structures and trajectories are available upon request. For a computational study, it is increasingly expected that such data be deposited in a public repository to ensure reproducibility.
- **Required correction** Consider depositing the starting structures, simulation parameters, and analysis scripts in a public repository (e.g., Zenodo, Figshare) and providing a DOI in the data availability statement.

## Risk / unsupported claims
- The claim that the identified C1a-kinase domain interface is "structurally conserved" across PKC isoforms is based on sequence conservation analysis, but no structural alignment or experimental validation across isoforms is provided. This claim is partially supported but not fully established.
- The statement that "inhibitor chemotype determined the extent of the observed allosteric effects" is based on a limited set of inhibitors and may not be generalizable. The correlation between chemotype and effect is not systematically analyzed.
- The claim that the computational paradigm can be applied to "other kinases" is speculative and not supported by data in this manuscript.
- The suggestion that SMKI-induced membrane localization could "confound the efficacy of kinase inhibitors" is an interesting hypothesis but is not directly tested in this study.
- The statement that the G-loop pocket is "druggable" is based on computational predictions (FBS) and the ability to accommodate small molecules in silico, but no experimental validation of druggability is provided.