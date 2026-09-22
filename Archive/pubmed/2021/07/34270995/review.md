## Review setup
- **Input scope** Full manuscript text, including abstract, significance statement, introduction, materials and methods, results and discussion, conclusions, and author contributions. Figures and tables are referenced but not directly provided; supporting material is mentioned but not included.
- **Assessment boundary** The review assesses the scientific claims, methodology, and interpretation presented in the manuscript. It does not evaluate the editorial fit for a specific journal, as the manuscript is already published in Biophysical Journal. The review focuses on the internal consistency, technical soundness, and evidentiary support of the presented findings.
- **Shared manuscript claim summary** The manuscript claims that molecular dynamics simulations and circular dichroism spectroscopy demonstrate that macromolecular crowding, modeled with polyethylene glycol (PEG) in all-atom and coarse-grained representations, affects the structural dynamics of the hepatitis C virus NS3/4A protease complex. Specifically, it claims that crowding reduces the diffusion of the complex, stabilizes a helical conformation in the N-terminal tail of the NS4A cofactor, and that this stabilization may prime the complex for membrane association, suggesting a functional role for crowding in viral replication.
- **Visible evidence base** The evidence base consists of the manuscript text, including descriptions of simulation protocols, analysis methods, and results. Key evidence includes: (1) calculated translational diffusion coefficients and rotational correlation times (Table 1), (2) contact correlation times (Table 2), (3) radial distribution functions of crowders around the protein (Fig. 4C), (4) wrapping coefficient analyses of NS4A tails (Fig. 6), (5) secondary structure analyses (Fig. 7), (6) CD spectroscopy data (Fig. 8), and (7) structural visualizations (Figs. 3, 5, 9). The actual figures, tables, and supporting material are not directly visible to the reviewer.
- **Missing materials affecting confidence** The actual figures, tables, and supporting material (Document S1, Figs. S1–S10, Tables S1 and S2) are not provided. This limits the ability to independently verify quantitative results, statistical analyses, and the visual representations of structural data. The specific simulation parameters, force field modifications, and analysis scripts are not fully detailed in the visible text. The CD spectroscopy raw data and analysis details are also not fully visible.

## Reviewer
- **Overall assessment** This manuscript presents a well-structured and technically sound computational study investigating the effects of macromolecular crowding on the dynamics of the NS3/4A protease complex. The use of two complementary crowder models (all-atom PEG and coarse-grained) to disentangle excluded volume and interaction effects is a methodological strength. The central finding, that crowding can stabilize a helical conformation in the disordered N-terminal tail of NS4A, is interesting and potentially significant for understanding the function of this viral protein in the cellular environment. However, the statistical significance of the key claim regarding helix stabilization is weak (p-values of 0.2 and 0.35), and the direct link between the observed in silico helix stabilization and the proposed functional role in membrane association remains speculative. The CD experiments provide supporting, but not conclusive, evidence. The manuscript would be strengthened by a more robust statistical analysis and a more cautious interpretation of the functional implications.
- **Who would be interested in the results, and why** Researchers in the fields of computational biophysics, molecular dynamics simulation, and intrinsically disordered proteins would be interested in the methodological approach and the observed effects of crowding on a disordered peptide. Virologists and structural biologists studying hepatitis C virus replication, particularly the NS3/4A protease as a drug target, would be interested in the potential functional implications for membrane anchoring. The work also contributes to the broader discussion on the role of macromolecular crowding in modulating protein behavior in cellular environments.
- **Major strengths**
    1.  The study uses a multi-scale modeling approach, combining all-atom and coarse-grained simulations, to systematically investigate the contributions of excluded volume and weak interactions to crowding effects.
    2.  The focus on the disordered tails of NS4A is timely and relevant, as the behavior of IDPs under crowded conditions is a key area of biophysical research.
    3.  The integration of CD spectroscopy experiments with simulations provides a complementary, albeit qualitative, experimental perspective.
    4.  The manuscript is clearly written and the logic of the study is easy to follow.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Statistical significance and robustness of the central claim
    - **Claim pointer** The manuscript claims that "crowding may stabilize a helical conformation in NS4A, priming it for membrane anchoring" and that "helix formation is more likely in the presence of the PEG crowders with moderate significance (p-value = 0.2) than with CG crowders (p-value = 0.35)."
    - **Evidence pointer** Results and discussion, section "Crowding may stabilize a helical conformation in NS4A, priming it for membrane anchoring"; Figure 7; Figure S10.
    - **Concern** The central claim of the paper, that crowding stabilizes a helical conformation in the NS4A N-terminal tail, is based on statistical analyses with p-values of 0.2 and 0.35. These values are far above the conventional threshold for statistical significance (e.g., p < 0.05) and indicate that the observed differences in helix formation between crowded and non-crowded conditions could easily be due to random chance. The manuscript acknowledges this as "moderate significance," but this is a substantial overstatement. The claim that crowding "stabilizes" a helix is not robustly supported by the presented data.
    - **Why it matters** The entire premise of the paper's functional conclusion, that crowding primes NS4A for membrane association, rests on this observation. If the helix stabilization is not a statistically robust effect, the proposed functional role of crowding is not established. The weak statistical support undermines the confidence in the primary finding.
    - **Resolution test** The authors must provide a more robust statistical analysis. This could include: (1) reporting confidence intervals for the helix formation probabilities, (2) performing a larger number of independent simulations to increase statistical power, or (3) using a more sensitive analysis method. The claim of "stabilization" should be revised to reflect the actual statistical confidence, or the conclusion should be tempered to state that crowding "may promote" helix formation, with the caveat that the effect is not statistically significant in the current dataset.
    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** No
    - **Axis** Functional relevance and extrapolation of in silico findings
    - **Claim pointer** The manuscript concludes that "cellular crowding may act as an enhancer of biological function, in this case assisting with NS3/4A TM helix precursor formation and positioning near the membrane surface to facilitate membrane anchoring and ultimately facilitating viral replication."
    - **Evidence pointer** Conclusions; Results and discussion, section "Crowding may stabilize a helical conformation in NS4A, priming it for membrane anchoring"; Figure 9.
    - **Concern** The leap from the observation of a short, transient helical fragment in a simulation to a functional role in membrane anchoring and viral replication is highly speculative. The simulations do not include a membrane, and the proposed mechanism of "priming" is not directly tested. The spatial proximity of the helix to known membrane-binding regions of NS3 (Fig. 9) is suggestive but does not demonstrate a functional interaction. The CD experiments show that crowding increases helicity of the isolated peptide, but this is a different system from the full NS3/4A complex in a cellular context.
    - **Why it matters** The paper's significance is largely derived from its potential to explain a biological function. If the functional link is not supported by the evidence, the impact of the work is considerably diminished. Overstating the functional implications can mislead readers and is not in line with a rigorous scientific assessment.
    - **Resolution test** The authors should clearly delineate between what is directly observed (a helical fragment in simulations and increased helicity in CD experiments) and what is hypothesized (the role of this fragment in membrane anchoring). The conclusion should be reframed as a testable hypothesis, rather than a definitive statement. The authors could suggest specific future experiments, such as simulations with a membrane model or mutagenesis studies, to directly test the proposed mechanism.
    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Generalizability of the crowder model
    - **Claim pointer** The manuscript uses a coarse-grained (CG) bead-shell model of PEG to represent "inert" crowders that primarily exert excluded volume effects, and all-atom PEG to represent weakly interacting crowders. The conclusions are framed in terms of general crowding effects.
    - **Evidence pointer** Materials and methods, section "Crowder models"; Results and discussion, sections "Crowding reduces diffusion of the protease and crowders" and "Crowding may stabilize a helical conformation in NS4A, priming it for membrane anchoring".
    - **Concern** The study uses a single type of crowder (PEG) in two representations. While this allows for a comparison of interaction strength, it limits the generalizability of the findings. Real cellular environments contain a complex mixture of proteins, nucleic acids, and other macromolecules with diverse shapes, sizes, and interaction properties. The behavior of NS3/4A in a PEG solution may not accurately reflect its behavior in the cytoplasm or near the ER membrane. The authors do not discuss the potential limitations of using PEG as a proxy for the cellular environment.
    - **Why it matters** The paper aims to draw conclusions about the behavior of NS3/4A in a "crowded environment" relevant to a cell. If the crowder model is not representative of the actual cellular environment, the relevance of the findings is questionable. A more nuanced discussion of the model's limitations is necessary.
    - **Resolution test** The authors should explicitly discuss the limitations of using PEG as a crowder and the potential differences between their model and the cellular environment. They could also suggest future studies using more complex crowder mixtures or a more realistic model of the ER membrane environment.
- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity of statistical reporting
    - **Affected element** Statistical analysis of helix formation
    - **Evidence pointer** Results and discussion, section "Crowding may stabilize a helical conformation in NS4A, priming it for membrane anchoring"
    - **Issue** The manuscript reports p-values for the helix formation analysis but does not specify the statistical test used, the number of samples, or the effect size. This makes it difficult to assess the validity of the analysis.
    - **Required correction** The authors should provide a clear description of the statistical methods used, including the test name, sample size, and a measure of effect size (e.g., difference in mean helicity with confidence intervals).
    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Justification of force field modification
    - **Affected element** Force field parameter scaling
    - **Evidence pointer** Materials and methods, section "Force field parameters"
    - **Issue** The authors scaled the epsilon parameter of the Lennard-Jones potential for water interactions by a factor of 1.09 to prevent PEG aggregation. This is a significant modification that could affect the results. The manuscript does not provide a detailed justification for this specific scaling factor or a sensitivity analysis showing how the results depend on this choice.
    - **Required correction** The authors should provide a more detailed justification for the scaling factor, possibly citing previous work that used a similar approach. They should also discuss the potential impact of this modification on the simulation results and ideally show that the main conclusions are robust to reasonable variations in this parameter.
    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Presentation of CD data
    - **Affected element** Figure 8
    - **Evidence pointer** Results and discussion, section "Crowding may stabilize a helical conformation in NS4A, priming it for membrane anchoring"; Figure 8
    - **Issue** The CD spectra are presented as smoothed curves, but the raw data or error bars are not shown. It is difficult to assess the noise level and the significance of the differences between the spectra.
    - **Required correction** The authors should show the raw data points or at least provide error bars representing the standard deviation or standard error of the measurements. This would allow the reader to better assess the reliability of the CD results.
    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Definition of wrapping coefficient
    - **Affected element** Equation 8
    - **Evidence pointer** Materials and methods, section "Protease and crowder contacts"
    - **Issue** The definition of the wrapping coefficient W is not entirely clear. It is defined as a sum of distances normalized by the min and max distance sums, but it is not clear how these min and max values are determined across all simulations. This could lead to ambiguity in interpreting the values.
    - **Required correction** The authors should provide a more precise definition of W, including how s_min and s_max are calculated and what exactly is being measured. A schematic figure or a more detailed textual explanation would be helpful.

## Risk / unsupported claims
- The claim that crowding "stabilizes" a helical conformation in the NS4A N-terminal tail is not robustly supported by the statistical analysis (p-values of 0.2 and 0.35).
- The proposed functional role of the observed helix as a "primer" for membrane association and a facilitator of viral replication is a speculative hypothesis that is not directly tested by the presented experiments or simulations.
- The generalizability of the findings to the complex cellular environment is limited by the use of a single crowder type (PEG) and is not adequately discussed.
- The specific effect of the force field modification (scaling epsilon by 1.09) on the quantitative results is not assessed, making it difficult to evaluate the robustness of the findings to this methodological choice.