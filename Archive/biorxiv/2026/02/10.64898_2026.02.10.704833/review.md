## Review setup
- **Input scope** Full manuscript text (Abstract, Introduction, Materials and Methods, Results, Discussion, Acknowledgments) as provided in the submission
- **Assessment boundary** Scientific content, methodological soundness, interpretation of results, and alignment with stated claims. Editorial quality and formatting are noted only where they affect comprehension.
- **Shared manuscript claim summary** The authors report that the isolated bZIP domain of the yeast transcription factor Gcn4 undergoes DNA-induced liquid-liquid phase separation in the absence of its activation domain. Using SAXS, all-atom MD simulations, and EOM, they identify a minor conformational population with a kink at the basic region-leucine zipper junction, and propose that SAXS can quantitatively probe protein conformations within condensates.
- **Visible evidence base** SAXS data for DNA, protein, and complex; EOM ensemble selection; MD trajectory analysis; optical microscopy of condensates; secondary structure and RMSF analyses; comparison with crystal structure (PDB 1YSA)
- **Missing materials affecting confidence** Supplementary figures (S1-S5) are referenced but not provided. Full MD simulation details are described as "elsewhere (Mattossovich et al., in preparation)" and are not available. Raw SAXS curves, fitting residuals, and validation metrics beyond χ² are not shown. No turbidity or quantitative phase diagram data are presented. The manuscript is a preprint and has not undergone peer review.

## Reviewer
- **Overall assessment** This manuscript reports a potentially interesting observation: that the isolated bZIP domain of Gcn4 can undergo DNA-induced phase separation without its activation domain, and that SAXS can be used to extract conformational information from phase-separated samples. The combination of SAXS with all-atom MD and EOM is methodologically ambitious. However, the central claims are not fully established from the evidence presented. The phase separation observation is largely qualitative, the assignment of the kinked conformation to a specific phase is speculative, and the quantitative interpretation of SAXS data from a phase-separated sample requires more careful justification. The manuscript would benefit from additional controls, quantitative characterization of the phase behavior, and a more rigorous treatment of the SAXS data analysis.
- **Who would be interested in the results, and why** Researchers studying transcription factor phase separation, particularly those interested in the role of DNA-binding domains in condensate formation. The work may also interest structural biologists using SAXS to study proteins in complex environments, and computational biologists working on ensemble methods for intrinsically disordered proteins. The claim that SAXS can probe conformations within condensates, if substantiated, would be of broad methodological interest.
- **Major strengths** The observation that a structured DNA-binding domain can drive phase separation in the absence of an activation domain challenges a prevailing assumption in the field. The use of all-atom MD to generate the EOM pool is a methodological improvement over coarse-grained approaches. The identification of a kinked conformational subpopulation is a novel finding that could have functional implications. The authors are transparent about the limitations of their approach in the Discussion.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (phase separation characterization), R1-M2 (SAXS interpretation in condensates), R1-M3 (EOM pool generation and fitting), R1-M4 (assignment of kinked conformation to phase)
- **Assessment against Nature-style criteria** Originality: The claim that a structured bZIP domain alone can drive DNA-induced phase separation is original and challenges current models. However, the observation is not quantitatively characterized, and the mechanistic insight is limited. Scientific importance: If fully substantiated, the findings would be important for understanding the minimal requirements for transcription factor condensate formation. The methodological claim about SAXS in condensates is potentially significant but requires more rigorous validation. Interdisciplinary readership: The topic bridges structural biology, biophysics, and gene regulation, and would appeal to a broad readership if the claims are properly supported. Technical soundness: The SAXS data collection appears standard, but the analysis and interpretation in the context of phase-separated samples raise concerns. The MD simulations are described only in brief, and the EOM analysis has potential issues. Readability for nonspecialists: The manuscript is generally well-written and accessible, though some technical sections assume familiarity with SAXS and ensemble methods.
- **Recommendation posture** Currently not established from the provided evidence. The central claims are plausible and interesting, but the evidence presented is insufficient to support them. The manuscript requires substantial additional work, including quantitative characterization of the phase behavior, more rigorous SAXS analysis, and additional controls, before the case can be made.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental evidence for phase separation
- **Claim pointer** The authors claim that the isolated bZIP domain undergoes DNA-induced phase separation in the absence of its activation domain, and that this is "in contrast with previous reports" (Bremer et al., 2025).
- **Evidence pointer** Results section, Figure 3, "location not provided" for quantitative data
- **Concern** The evidence for phase separation is limited to visual observation of turbidity and optical microscopy images. No quantitative characterization is provided: no turbidity measurements as a function of concentration, no determination of a phase boundary or saturation concentration, no fluorescence recovery after photobleaching (FRAP) to demonstrate liquid-like behavior, no rheological measurements, and no controls with non-cognate DNA or with a DNA sequence lacking the Gcn4 binding site. The claim that the bZIP domain is "sufficient" to induce phase separation requires demonstration that the observed behavior is specific to the bZIP-DNA interaction and not a general electrostatic effect between a positively charged protein and negatively charged DNA. The discrepancy with Bremer et al. (2025) is noted but not resolved; the authors speculate about differences in construct length, DNA sequence, and conditions, but do not test any of these possibilities.
- **Why it matters** The central claim of the manuscript is that DNA binding drives phase separation of the bZIP domain. Without quantitative characterization and appropriate controls, this claim is not established. The field has been plagued by artifacts in phase separation studies, and the standard of evidence is now high. The authors must demonstrate that the observed droplets are equilibrium liquid phases, that they form specifically due to the bZIP-DNA interaction, and that the phase behavior is reproducible and well-characterized.
- **Resolution test** Provide quantitative phase diagrams (e.g., turbidity or droplet formation as a function of protein and DNA concentration), FRAP or other evidence of liquid-like behavior, controls with non-cognate DNA and with a DNA sequence lacking the Gcn4 recognition site, and a systematic comparison with the Bremer et al. (2025) conditions to identify the source of the discrepancy.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** SAXS interpretation in phase-separated samples
- **Claim pointer** The authors claim that "SAXS allows us to probe the complex also in a phase-separated sample" and that the data "must reflect the average of the complex conformation in both the dilute and the droplet phases."
- **Evidence pointer** Results section, Figure 1, Table 1
- **Concern** The interpretation of SAXS data from a phase-separated sample is not straightforward. The authors argue that the droplet radius (1-10 µm) is too large to contribute to the scattering in the measured q-range, and that the droplets are smaller than the beam size, so the data represent an average. However, this argument is incomplete. First, the concentration of the complex within the droplets is likely much higher than in the dilute phase, and the scattering intensity scales with concentration. The relative contribution of the two phases to the scattering signal depends on the partition coefficient, the volume fraction of each phase, and the contrast. The authors do not provide any estimate of these quantities. Second, the presence of a significant structure factor from the concentrated droplets could affect the scattering at low q, even if the form factor of the droplets themselves does not contribute. Third, the authors do not address whether the complex undergoes any conformational change upon partitioning into the droplet phase, which would affect the scattering. The claim that the data represent a simple average of the two phases is an assumption, not a demonstrated fact.
- **Why it matters** The methodological claim of the manuscript is that SAXS can quantitatively probe conformations within condensates. This claim is not supported by the analysis presented. If the interpretation is incorrect, the derived conformational ensemble may be biased or wrong. The authors need to either provide a rigorous framework for interpreting SAXS data from phase-separated samples or temper their claims.
- **Resolution test** Provide a quantitative model for the contribution of each phase to the scattering, including estimates of the partition coefficient, volume fraction, and contrast. Alternatively, perform SAXS measurements as a function of concentration across the phase boundary and show that the derived conformational ensemble is invariant. If possible, use a technique that can selectively probe the droplet phase (e.g., microfluidic mixing or spatial filtering) to validate the interpretation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** EOM analysis and MD simulation
- **Claim pointer** The authors claim that EOM analysis of the SAXS data reveals two conformational populations, with a 9:1 ratio of straight to kinked conformations.
- **Evidence pointer** Results section, Figure 4, Table 2
- **Concern** The EOM analysis has several potential issues. First, the MD simulation used to generate the pool was only 100 ns in length. Given the size of the system (a bZIP dimer bound to a 336 bp DNA), 100 ns may not be sufficient to sample the conformational space adequately, particularly for a rare event such as the kink formation. The authors do not provide any convergence analysis. Second, the EOM fit is reported to have a χ² of 214, which is very poor. The authors attribute this to the phase separation, but this is not demonstrated. A poor fit undermines the reliability of the derived ensemble. Third, the EOM method selects a small number of conformations from a large pool, and the results can be sensitive to the pool composition and the genetic algorithm parameters. The authors do not report any sensitivity analysis. Fourth, the kinked conformation is identified as a minor population, but the structural details of this conformation are not described in sufficient detail. What is the nature of the kink? Is it a rigid bend or a flexible hinge? How does it relate to the known flexibility of the bZIP domain?
- **Why it matters** The identification of a novel kinked conformation is a key finding of the manuscript. If the EOM analysis is not reliable, this finding is not established. The poor χ² value is particularly concerning and needs to be addressed.
- **Resolution test** Provide convergence analysis for the MD simulation. Report the EOM fit quality in more detail, including the q-range of the discrepancy and possible sources. Perform sensitivity analysis on the EOM parameters and pool size. Validate the kinked conformation using an independent method (e.g., NMR residual dipolar couplings, or a different computational approach).

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Assignment of kinked conformation to phase
- **Claim pointer** The authors suggest that the straight conformation may dominate in the droplet phase and the kinked conformation in the dilute phase, based on the "conceptual similarity" of the droplet environment to the crystal.
- **Evidence pointer** Discussion section
- **Concern** This assignment is purely speculative. The authors provide no experimental or computational evidence to support the differential partitioning of the two conformations between phases. The argument from "conceptual similarity" to the crystal is not compelling, as the droplet environment is not necessarily similar to a crystal lattice. The authors themselves note the "relatively modest difference in the population ratio (9:1)" and attempt to rationalize it through contrast effects, but this rationalization is not quantitative. The claim that the kinked conformation could be relevant for DNA binding and flexibility is also speculative, as no functional data are presented.
- **Why it matters** The manuscript's title and abstract emphasize the conformational ensemble in the diluted and condensate phases. If the assignment of conformations to phases is not supported, this aspect of the claim is not established. The authors should either provide evidence for the differential partitioning or clearly state that this is a hypothesis.
- **Resolution test** Perform experiments that can distinguish the conformations in each phase. This could include SAXS with contrast matching, solid-state NMR, or fluorescence-based assays that report on the kink conformation in the droplet phase. Alternatively, perform simulations of the complex in a crowded environment that mimics the droplet and compare the conformational ensemble to that in dilute solution.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of phase separation observation
- **Affected element** Results section, Figure 3
- **Evidence pointer** Figure 3
- **Issue** The optical microscopy images are described as showing "droplets and circular particles ranging in size from 2 µm to 15 µm." It is not clear whether these are all liquid droplets or whether some are aggregates or vesicles. The authors state that "the smallest particles were in motion, while the largest ones were stable," which is consistent with liquid-like behavior, but no quantitative analysis of the motion is provided.
- **Required correction** Provide higher-resolution images, and if possible, time-lapse images showing coalescence or fusion events. Quantify the size distribution and the fraction of the sample that is in the droplet phase.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** pH dependence
- **Affected element** Results section, "Interaction between Gcn4 bZIP and ARG-1A leads to phase separation"
- **Evidence pointer** "location not provided"
- **Issue** The authors state that they observed similar effects at pH 5.7 and 7.4, but no data are shown for the pH 7.4 condition. The choice of pH 5.7 is unusual, as most phase separation studies are conducted at physiological pH. The authors should clarify why pH 5.7 was chosen and show the pH 7.4 data.
- **Required correction** Show the pH 7.4 data, or provide a justification for why pH 5.7 is the relevant condition.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Molecular weight estimation
- **Affected element** Results section, Table 1
- **Evidence pointer** Table 1
- **Issue** The molecular weight of the complex estimated by the Vc method is 26.0 kDa, close to the theoretical 28.4 kDa. However, the authors note that the Vc method is not accurate for mixed protein-nucleic acid systems. This limitation should be acknowledged more prominently, and the molecular weight should be treated as a rough estimate.
- **Required correction** Acknowledge the limitation of the Vc method for protein-nucleic acid complexes in the main text, not just in a parenthetical remark.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Comparison with previous work
- **Affected element** Introduction, Discussion
- **Evidence pointer** "location not provided"
- **Issue** The authors state that their observation is "in contrast with previous reports" (Bremer et al., 2025) but do not provide a detailed comparison of the experimental conditions. The Bremer et al. study is cited but not described in sufficient detail for the reader to assess the discrepancy.
- **Required correction** Provide a more detailed comparison of the constructs, DNA sequences, and conditions used in the two studies, and discuss possible reasons for the discrepancy.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical analysis
- **Affected element** Results section, Figure 5
- **Evidence pointer** Figure 5
- **Issue** The angle distributions in Figure 5 are described as having "a main, dense cluster" and "a less dense one," but no statistical analysis is provided. It is not clear whether the two clusters are significantly different or whether the distribution is continuous.
- **Required correction** Provide a statistical analysis of the angle distributions, such as a bimodality test or a Gaussian mixture model fit.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Evidence pointer** "location not provided"
- **Issue** The term "condensate phases" is used in the title and throughout, but the authors do not clearly define what they mean by this term. Do they refer to the dense phase of the phase-separated system, or to a specific type of condensate?
- **Required correction** Define the term "condensate phases" at first use and use it consistently.

## Risk / unsupported claims
- The claim that the bZIP domain alone is sufficient for DNA-induced phase separation is not quantitatively supported (no phase diagram, no saturation concentration, no controls).
- The claim that SAXS can quantitatively probe protein conformations within condensates is not established; the interpretation of the SAXS data from the phase-separated sample relies on unverified assumptions about the relative contributions of the two phases.
- The assignment of the straight conformation to the droplet phase and the kinked conformation to the dilute phase is speculative and not supported by any direct evidence.
- The claim that the kinked conformation is "previously unrecognized" is not verifiable from the provided text, as the authors do not provide a comprehensive literature search.
- The claim that the findings "open new avenues for the structural chemistry of phase-separated systems" is overstated given the limitations of the current analysis.
- The discrepancy with Bremer et al. (2025) is noted but not resolved; the authors' speculation about the source of the discrepancy is not tested.