## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, experimental and computational methods, results and discussion, conclusions, and supplementary figure references.
- **Assessment boundary** Scientific soundness, methodological rigor, internal consistency, and support of stated conclusions based solely on the provided manuscript content.
- **Shared manuscript claim summary** The authors investigate how peptide chain length affects the interaction, translocation, and cushion formation of histatin 5 variants (14Hst5, 24Hst5, 48Hst5) with model lipid bilayers, combining experimental surface techniques (NR, QCM-D, SAXS, CD) with coarse-grained Monte Carlo simulations. They report that at low salt (10 mM NaCl), all variants form a cushion below the bilayer, while at high salt (150 mM NaCl), 24Hst5 shows no interaction, 14Hst5 still forms a cushion, and 48Hst5 forms a cushion plus an additional thick diffuse layer on top of the bilayer. They hypothesize that positively charged patches of lysine and arginine are essential for interaction and translocation.
- **Visible evidence base** Abstract; Introduction; Experimental Section (peptide solutions, vesicle preparation, CD, SAXS, QCM-D, NR); Computational Section (coarse-grained model, MC simulation method); Results and Discussion (solution behavior, interaction with SLBs at low and high salt, simulations); Conclusions; Supplementary Material references; Acknowledgments.
- **Missing materials affecting confidence** Full supplementary information (figures S1, S8, S16, S25, S26, S27, S28, S29; tables S3, S4); raw NR reflectivity curves and fits; QCM-D raw data for all overtones; SAXS scattering profiles; simulation input parameters and force field details; bioinformatic predictor outputs in full; detailed error analysis for NR fits; sequence alignment details for the three peptide variants.

## Reviewer
- **Overall assessment** The manuscript addresses a relevant question in antimicrobial peptide-membrane interactions, specifically the role of peptide chain length in translocation and cushion formation. The combination of experimental and computational approaches is commendable. However, several technical concerns limit the strength of the conclusions. The interpretation of NR data, the discrepancy between QCM-D and NR results, the limited simulation scope, and the lack of quantitative comparison between experiment and simulation weaken the central claims. The hypothesis regarding positively charged patches is plausible but not directly tested. The manuscript would benefit from clearer presentation of data analysis and a more rigorous discussion of alternative interpretations.
- **Who would be interested in the results, and why** Researchers in the fields of antimicrobial peptides, membrane biophysics, and drug delivery. The work provides insights into how peptide length and charge distribution affect membrane translocation, which is relevant for designing peptide-based drug carriers and understanding antimicrobial mechanisms. The methodological combination of NR, QCM-D, and simulations may interest biophysicists studying peptide-membrane interactions.
- **Major strengths** 1. The study addresses a well-defined question with systematic variation of peptide length. 2. The combination of multiple experimental techniques (NR, QCM-D, SAXS, CD) with simulations provides complementary perspectives. 3. The use of partially deuterated lipids for contrast variation in NR is methodologically sound. 4. The observation of a salt-dependent difference in behavior between peptide variants is interesting and potentially significant. 5. The authors acknowledge limitations and propose a plausible mechanistic hypothesis.
- **Major Concerns** 
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness of NR data analysis
  - **Claim pointer** The authors claim that NR data analysis reveals peptide localization in the cushion region, within the bilayer, and on top of the bilayer for different variants and salt conditions.
  - **Evidence pointer** Results and Discussion, "The Effect of Chain Length at Low Salt Concentration" and "The Impact of Salt Concentration"; Figures 2, 3, 4
  - **Concern** The NR data analysis relies on a slab model with multiple free parameters, including layer thicknesses, SLDs, buffer volume fractions, and roughness. The manuscript does not provide sufficient detail on how the model was constrained, how uniqueness of the fit was assessed, or how parameter uncertainties were propagated. The authors state that "different scenarios were evaluated" but do not describe the model selection criteria. Given the high number of parameters relative to the information content of reflectivity data, the risk of overfitting is substantial. The reported structural parameters (e.g., cushion thickness, peptide volume fractions) may not be uniquely determined. Additionally, the conversion of NR-derived volume fractions to peptide amounts and the comparison with QCM-D mass require assumptions about peptide density and hydration that are not fully justified.
  - **Why it matters** The central conclusion that different peptide variants form cushions or accumulate on top of the bilayer depends critically on the correctness of the NR model. If the model is not uniquely constrained, the structural interpretation is not reliable, and the comparison between variants may be invalid.
  - **Resolution test** Provide a detailed description of the fitting procedure, including the number of parameters, constraints applied, and how the best-fit model was selected among alternatives. Show the full set of reflectivity curves with fits for all contrasts and discuss the confidence intervals for key parameters. Perform a parameter correlation analysis or use a more robust model selection criterion (e.g., Bayesian information criterion) to demonstrate that the chosen model is justified.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Quantitative consistency between techniques
  - **Claim pointer** The authors compare NR-derived equivalent thicknesses (Dgap) with QCM-D-derived thicknesses (tQCM) and report values of the same order of magnitude, suggesting consistency.
  - **Evidence pointer** Results and Discussion, "The Effect of Chain Length at Low Salt Concentration"; Figure 2
  - **Concern** The comparison between Dgap and tQCM is presented qualitatively. The manuscript does not provide a quantitative assessment of whether the differences between these values are within experimental uncertainty. For 14Hst5, Dgap = 6 ± 1 Å and tQCM = 11.6 ± 0.4 Å, a factor of approximately 2 difference. For 48Hst5, Dgap = 6 ± 1 Å and tQCM = 5.7 ± 0.3 Å, which are consistent. The authors attribute the discrepancy for 14Hst5 to hydration and model assumptions, but this is not rigorously analyzed. Furthermore, QCM-D measures wet mass including coupled water, while NR measures dry volume fractions; the manuscript does not adequately address how these different quantities should be compared.
  - **Why it matters** The consistency between independent techniques is a key validation of the results. If the discrepancy between NR and QCM-D is not explained, the reliability of both measurements is called into question.
  - **Resolution test** Provide a quantitative comparison of NR and QCM-D results, including a discussion of the expected relationship between Dgap and tQCM given the different measurement principles. Estimate the systematic uncertainties in both techniques and assess whether the observed differences are significant. If the discrepancy is attributed to hydration, provide an estimate of the hydration layer thickness and justify the assumptions.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Support for the role of charged patches
  - **Claim pointer** The authors hypothesize that positively charged patches of lysine and arginine are essential for peptide interaction with and translocation across the bilayer.
  - **Evidence pointer** Results and Discussion, "Bioinformatic Predictors and Charged Patches"; Table 1; Figure 1
  - **Concern** The hypothesis is based on bioinformatic predictions and sequence analysis, but no direct experimental or simulation evidence is provided to test it. The simulations do not systematically vary the charge distribution or remove specific charged patches to assess their role. The comparison between variants is confounded by simultaneous changes in length, charge, and sequence. The authors mention a previous study where KRK was replaced with glycine, but this is not part of the current work. The bioinformatic predictors give inconsistent results (e.g., NLStradamus vs. PSORT II for 24Hst5), and the authors do not resolve these discrepancies.
  - **Why it matters** The central hypothesis of the paper is that charged patches are essential for translocation. Without direct testing, this remains speculative. The manuscript would be strengthened by simulations or experiments that specifically perturb the charged patches.
  - **Resolution test** Perform simulations with modified peptide sequences where charged patches are neutralized or rearranged, and compare the adsorption and translocation behavior. Alternatively, design experiments with peptide variants that lack specific charged patches. At minimum, discuss how the current data distinguish between the role of overall charge versus specific patch arrangement.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Simulation-experiment comparison
  - **Claim pointer** The authors state that "similar trends were observed from the simulations" and use simulations to support the experimental findings.
  - **Evidence pointer** Results and Discussion, "Computer Simulations"; Figures 5, 6; Tables S3, S4
  - **Concern** The comparison between simulations and experiments is qualitative. The simulations model a simplified system (two surfaces, no explicit lipid bilayer structure, implicit salt) that may not capture the full complexity of the experimental system. The manuscript does not provide a quantitative comparison of, for example, peptide volume fractions, layer thicknesses, or adsorption probabilities between simulations and experiments. The simulation results are presented as supporting evidence, but the degree of agreement is not assessed.
  - **Why it matters** The claim that simulations support the experimental conclusions requires a quantitative demonstration of agreement. Without this, the simulations add limited value to the study.
  - **Resolution test** Provide a quantitative comparison of simulation and experimental results, such as comparing the calculated peptide density profiles with NR-derived volume fraction profiles. Discuss the limitations of the simulation model and how they might affect the comparison.

  - **Concern ID** R1-M5
  - **Severity** Major
  - **Blocking** No
  - **Axis** Generalizability of conclusions
  - **Claim pointer** The authors conclude that "electrostatic interactions are important for the interaction between the solid-supported lipid bilayers and the peptide depending on the linear charge density through the primary sequence and the positively charged patches in the sequence."
  - **Evidence pointer** Conclusions; Abstract
  - **Concern** The study is limited to a single lipid composition (PC:PS 9:1) and a single peptide family (histatin 5 variants). The conclusions about the role of charge density and patches may not generalize to other lipid compositions or peptide sequences. The authors do not discuss the potential influence of lipid composition, peptide concentration, or other factors on the observed behavior.
  - **Why it matters** The stated conclusions are broad, but the evidence base is narrow. Overgeneralization could mislead readers about the applicability of the findings.
  - **Resolution test** Acknowledge the limitations of the study system and temper the conclusions accordingly. Alternatively, include additional experiments or simulations with different lipid compositions or peptide sequences to test generalizability.

- **Minor Comments** 
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity of presentation
  - **Affected element** Figure 1
  - **Evidence pointer** Figure 1; Results and Discussion, "Solution Behavior of the Studied Peptides"
  - **Issue** The manuscript states that the peptide sequences are presented in Figure 1, but the figure is not included in the provided text. The charged patches and their positions are discussed but cannot be visualized.
  - **Required correction** Ensure Figure 1 clearly shows the sequences of 14Hst5, 24Hst5, and 48Hst5, with charged residues and patches highlighted. Reference the figure explicitly in the text where the sequences are discussed.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Completeness of methods
  - **Affected element** Bioinformatic predictors
  - **Evidence pointer** Results and Discussion, "Bioinformatic Predictors and Charged Patches"; Table 1
  - **Issue** The manuscript mentions four predictors for CPP and three for antifungal effects but does not list all of them by name. Only some are mentioned in the text.
  - **Required correction** List all predictors used, including version numbers and access dates, in the methods or a supplementary table.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Statistical reporting
  - **Affected element** QCM-D data
  - **Evidence pointer** Results and Discussion, "The Effect of Chain Length at Low Salt Concentration"; Figure 2
  - **Issue** The manuscript reports average values and standard deviations for QCM-D measurements but does not state the number of replicates or whether the reported uncertainties represent measurement variability or fitting errors.
  - **Required correction** Specify the number of independent measurements and the source of the reported uncertainties.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** "Translocation" terminology
  - **Evidence pointer** Abstract; Introduction; Conclusions
  - **Issue** The term "translocation" is used to describe peptide movement across the bilayer, but the experimental evidence primarily shows peptide localization in the cushion region and within the bilayer. The distinction between translocation (complete passage across the bilayer) and partial penetration is not clearly defined.
  - **Required correction** Define "translocation" in the context of this study and discuss whether the experimental evidence supports complete translocation or partial penetration.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Discussion of limitations
  - **Affected element** Simulation model
  - **Evidence pointer** Computational Section; Results and Discussion, "Computer Simulations"
  - **Issue** The simulation model uses a simplified representation of the lipid bilayer (two charged surfaces) that does not capture lipid dynamics, bilayer curvature, or hydrophobic effects. The authors do not discuss how these simplifications might affect the conclusions.
  - **Required correction** Add a paragraph discussing the limitations of the simulation model and the potential impact on the interpretation of results.

  - **Concern ID** R1-m6
  - **Severity** Minor
  - **Axis** Reference to previous work
  - **Affected element** Introduction
  - **Evidence pointer** Introduction, first paragraph
  - **Issue** The introduction references previous work on cushion formation but does not provide sufficient context for readers unfamiliar with the field.
  - **Required correction** Expand the introduction to briefly explain the concept of cushioned lipid bilayers and why they are relevant for studying membrane-protein interactions.

## Risk / unsupported claims
- The claim that "positively charged patches of the amino acids lysine and arginine in all three peptides are essential for them to interact with and translocate over the bilayer" is not directly supported by the data presented. No experiments or simulations specifically test the role of these patches.
- The claim that "similar trends were observed from the simulations" is not quantitatively demonstrated. The degree of agreement between simulations and experiments is not assessed.
- The statement that "the shorter peptide, 14Hst5, is capable to translocate across the bilayer and form a cushion" at high salt is based on NR and QCM-D data, but the manuscript does not provide a detailed error analysis or model validation to support the uniqueness of this interpretation.
- The hypothesis that "electrostatic interactions are important... depending on the linear charge density through the primary sequence and the positively charged patches" is plausible but not rigorously tested. The study does not systematically vary charge density or patch arrangement.
- The bioinformatic predictions are presented as supporting evidence, but the inconsistencies between predictors (e.g., NLStradamus vs. PSORT II for 24Hst5) are not resolved or discussed in depth.
- The claim that the system "opens up the possibility for this system to be used in the research and development of new drugs and pharmaceuticals" is speculative and not supported by the data presented.