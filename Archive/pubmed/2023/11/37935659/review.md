## Review setup
- **Input scope** Full manuscript text including abstract, main text, methods, and figure legends
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and technical validity as presented in the provided manuscript
- **Shared manuscript claim summary** The authors propose that antimicrobial peptides (AMPs) can exert antibacterial effects by inducing phase transitions and compaction of nucleic acids, representing a previously unrecognized mechanism of action. They use machine learning predictions, in vitro phase separation assays, biophysical characterization, and cell-based imaging to support this claim.
- **Visible evidence base** Main text figures 1-7, supplementary figures 1-30, supplementary movies 1-3, methods section
- **Missing materials affecting confidence** Raw source data files, full supplementary information details, peer review file, reporting summary

## Reviewer

- **Overall assessment** This manuscript presents an interesting and potentially significant hypothesis that antimicrobial peptides may act through nucleic acid phase separation. The combination of computational prediction, in vitro biophysical characterization, and cellular imaging provides a multi-pronged approach. However, several technical concerns and gaps in evidence weaken the strength of the central claim. The correlation between phase separation propensity and antimicrobial activity is suggestive but not mechanistically proven. The cellular imaging data, while supportive, does not definitively demonstrate that phase separation is the cause of bacterial cell death. The manuscript would benefit from more direct functional experiments linking phase separation to antimicrobial activity.

- **Who would be interested in the results, and why** Researchers in antimicrobial peptide biology, phase separation and biomolecular condensates, bacterial cell biology, and drug discovery would find this work of interest. The proposed mechanism could inform the design of new antimicrobial strategies and contributes to the growing understanding of phase separation in prokaryotic systems. The methodological approaches, particularly the PhaseScan platform and machine learning predictions, may also appeal to biophysicists and computational biologists.

- **Major strengths** The study addresses an important and timely question about the intracellular mechanisms of AMPs, which are not well understood. The use of multiple complementary techniques (machine learning, in vitro assays, biophysical characterization, cellular imaging) provides a comprehensive approach. The identification of a large fraction of AMPs with predicted phase separation propensity is a novel observation. The quantitative phase diagrams generated using PhaseScan are technically impressive and provide detailed biophysical characterization.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic link
- **Claim pointer** The authors claim that "AMP-driven compaction of nucleic acids and modulation of their phase transitions constitute a previously unrecognised mechanism by which AMPs exert their antibacterial effects."
- **Evidence pointer** Figures 5-7, Results section "The mechanism of action of DNA/RNA-targeting AMPs"
- **Concern** The central claim that phase separation is a mechanism of antimicrobial action is not directly tested. The CFPS experiments show that AMPs inhibit transcription and translation, and the authors interpret this as being due to nucleic acid sequestration. However, alternative explanations such as direct enzyme inhibition, RNA degradation, or non-specific electrostatic interference with the translation machinery are not ruled out. The correlation between phase separation propensity and CFPS inhibition does not establish causation. No experiments directly demonstrate that phase separation is required for antimicrobial activity, such as using phase separation-deficient mutants or conditions that specifically disrupt condensate formation without affecting other AMP activities.
- **Why it matters** The central thesis of the paper rests on establishing phase separation as a bona fide mechanism of action. Without direct functional evidence linking phase separation to antimicrobial activity, the claim remains speculative. This is critical because many cationic peptides can inhibit translation through non-specific electrostatic interactions, and the observed effects may not be specific to phase separation.
- **Resolution test** The authors should perform experiments that directly test whether phase separation is required for antimicrobial activity. This could include: (1) generating AMP variants that maintain nucleic acid binding but are deficient in phase separation and testing their antimicrobial activity; (2) using optical tweezers or other methods to disrupt condensates in living cells and assessing effects on bacterial viability; (3) comparing the antimicrobial activity of AMPs under conditions that promote vs. inhibit phase separation; (4) testing whether overexpression of nucleic acids that compete for AMP binding rescues bacterial growth.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative analysis
- **Claim pointer** The authors state that "the degree of RNA compaction by AMPs was much higher compared to Sp3+ (i.e., 5.5 ± 0.6 nm for Buforin-2 versus 11.6 ± 0.25 nm for Sp3+, at 50 μM of each polycation) supporting the notion that RNA compaction by AMPs cannot be simply explained by charge neutralisation, and suggesting specificity of binding."
- **Evidence pointer** Figure 4c, Results section "Condensate-forming AMPs compact structured RNA"
- **Concern** The comparison between AMPs and Sp3+ is confounded by differences in charge density, molecular weight, and binding mode. Sp3+ is a small trivalent cation, while AMPs are larger peptides with multiple charges and potential for specific interactions. The conclusion of "specificity" based on this comparison is not well supported. Additionally, the rH measurements are performed at a single AMP concentration (50 μM) and may not capture the full concentration-dependent behavior. The authors do not provide binding affinity measurements or stoichiometry data that would support claims of specific versus non-specific interactions.
- **Why it matters** The claim of specificity is important for distinguishing the proposed mechanism from simple electrostatic effects. If AMPs act merely as highly charged cations, the phase separation mechanism would be less novel and less specific. The current data do not adequately support the specificity claim.
- **Resolution test** The authors should provide more rigorous biophysical characterization of AMP-nucleic acid interactions, including: (1) isothermal titration calorimetry or surface plasmon resonance to measure binding affinities and stoichiometries; (2) comparison with a panel of control peptides matched for charge but with different sequences; (3) salt-dependent binding studies to distinguish electrostatic from specific interactions; (4) competition experiments with different nucleic acid sequences to assess sequence specificity.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Cellular relevance
- **Claim pointer** The authors claim that "the addition of these peptides to bacterial cells leads to the formation of intracellular foci-like condensates containing nucleic acids and AMPs."
- **Evidence pointer** Figure 6a, Results section "Condensate-forming AMPs compact structured RNA"
- **Concern** The cellular imaging data show foci formation in E. coli, but the physiological relevance is unclear. The AMP concentrations used (20 μM) may be much higher than those required for antimicrobial activity, and the relationship between foci formation and cell death is not established. The authors do not quantify the fraction of cells with foci, the kinetics of foci formation relative to cell death, or whether foci formation precedes or follows loss of viability. Additionally, the foci could represent non-specific aggregation or membrane disruption artifacts rather than bona fide phase-separated condensates. The authors do not perform FRAP or other biophysical characterization of these intracellular foci to confirm their liquid-like nature.
- **Why it matters** The cellular data are the most direct evidence for the proposed mechanism in a biological context. Without demonstrating that foci formation is causally linked to antimicrobial activity and that these foci are true phase-separated condensates, the physiological relevance of the in vitro observations remains uncertain.
- **Resolution test** The authors should: (1) perform time-lapse imaging to correlate foci formation with cell death kinetics; (2) quantify the fraction of cells with foci at different AMP concentrations and correlate with viability; (3) perform FRAP on intracellular foci to confirm liquid-like properties; (4) test whether conditions that prevent foci formation (e.g., lower AMP concentrations, different salt conditions) also reduce antimicrobial activity; (5) use super-resolution microscopy to better characterize the foci structure.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** The authors state that "a substantial fraction of AMPs are predicted to phase separate either alone or in the presence of nucleic acids" and imply this is a general mechanism for AMPs.
- **Evidence pointer** Figure 1b, Results section "Phase separation propensity of AMPs"
- **Concern** The machine learning predictions are based on a model trained on eukaryotic phase-separating proteins and nucleic acid-binding proteins. The applicability of this model to AMPs, which are short, highly cationic peptides, is not validated. The authors test only three AMPs experimentally, which is a very small sample size given the diversity of AMP sequences and mechanisms. The correlation between predicted phase separation propensity and antimicrobial activity is not systematically tested across a larger panel of AMPs. Additionally, the authors do not compare their predictions with known AMP mechanisms to assess whether phase separation propensity correlates with specific types of antimicrobial activity.
- **Why it matters** The claim of a general mechanism requires evidence that phase separation propensity is a common feature of AMPs and that this property correlates with antimicrobial activity across a diverse set of peptides. With only three experimental examples and no validation of the computational predictions, the generalizability of the proposed mechanism is not established.
- **Resolution test** The authors should: (1) validate the machine learning predictions experimentally on a larger panel of AMPs (at least 10-20 peptides) with diverse sequences and known mechanisms; (2) test whether phase separation propensity correlates with antimicrobial activity across this panel; (3) include AMPs with known non-phase-separation mechanisms as negative controls; (4) compare phase separation propensity with other known AMP features such as membrane disruption activity to assess specificity.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Experimental details
- **Affected element** Methods section, in vitro phase separation assays
- **Evidence pointer** Methods, "Imaging of the condensates in vitro"
- **Issue** The methods for in vitro phase separation assays lack important details. The authors do not specify the buffer conditions for the phase separation experiments beyond "50 mM HEPES pH 7.3" and do not report the temperature at which experiments were performed. The concentration ranges tested are not systematically described, and it is unclear how the phase boundaries in Figure 3 were determined from the raw data.
- **Required correction** The authors should provide complete buffer compositions, temperature, and a detailed description of how phase boundaries were determined, including the criteria for classifying a droplet as phase-separated.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical analysis
- **Affected element** Figure 3, phase diagrams
- **Evidence pointer** Figure 3, Results section "Quantification of AMP phase separation propensity"
- **Issue** The phase diagrams in Figure 3 are presented as heat maps of "estimated phase separation probability," but the statistical methods for this estimation are not described in sufficient detail. The authors state that the probability was estimated by dividing the phase diagram into grids, but do not specify the grid size, the number of replicates per condition, or how the probability was calculated from the binary phase-separated/not-phase-separated data.
- **Required correction** The authors should provide a detailed description of the statistical methods used to generate the phase diagrams, including grid size determination, number of replicates, and the exact formula for probability estimation.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 5, CFPS experiments
- **Evidence pointer** Figure 5, Results section "The mechanism of action of DNA/RNA-targeting AMPs"
- **Issue** The CFPS data in Figure 5 are presented as fitted curves, but the raw data points are not shown. This makes it difficult to assess the quality of the fits and the variability between replicates. The authors report EC50 values with RMSD, but do not provide confidence intervals or statistical comparisons between conditions.
- **Required correction** The authors should show raw data points alongside the fitted curves and provide confidence intervals for the EC50 values. Statistical comparisons between different AMPs and between DNA- and mRNA-initiated reactions should be included.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction and Discussion
- **Evidence pointer** Introduction, Results and discussion
- **Issue** The discussion of previous work on AMP-nucleic acid interactions is limited. The authors mention that some AMPs interact with intracellular targets, but do not discuss in detail the existing literature on AMP-induced DNA condensation or RNA binding. This makes it difficult to assess the novelty of the proposed mechanism.
- **Required correction** The authors should provide a more comprehensive review of previous studies on AMP-nucleic acid interactions and clearly articulate how their proposed mechanism differs from or extends prior work.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 6, cellular imaging
- **Evidence pointer** Figure 6a, Results section "Condensate-forming AMPs compact structured RNA"
- **Issue** The cellular imaging data in Figure 6a are of limited quality. The foci are small and difficult to distinguish from background fluorescence. The authors do not provide quantitative image analysis, such as the number of foci per cell, the size distribution of foci, or the fraction of cells containing foci.
- **Required correction** The authors should provide higher-resolution images and quantitative analysis of foci formation, including the percentage of cells with foci, the number of foci per cell, and the size distribution.

## Risk / unsupported claims
- The claim that phase separation is a "previously unrecognised mechanism" of AMP action is not fully supported, as the authors do not rule out alternative mechanisms such as direct enzyme inhibition or non-specific electrostatic interference.
- The claim of "specificity" in AMP-nucleic acid interactions based on comparison with Sp3+ is not well supported due to confounding variables.
- The generalizability of the proposed mechanism to the broader AMP family is not established given the small number of experimentally tested peptides.
- The physiological relevance of the intracellular foci observed in E. coli is not demonstrated, as the relationship between foci formation and antimicrobial activity is not established.
- The machine learning predictions of phase separation propensity for AMPs are not experimentally validated on a diverse panel of peptides.
- The statement that "the development of antimicrobials that target nucleic acid phase transitions may become an attractive route" is speculative and not directly supported by the data presented.