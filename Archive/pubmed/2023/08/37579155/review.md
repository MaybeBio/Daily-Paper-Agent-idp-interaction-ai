## Review setup
- **Input scope** Full manuscript text (main text, excluding supplementary figures and tables)
- **Assessment boundary** Scientific claims, methodology, and conclusions as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors propose that phase separation of the TDP-43 C-terminal domain (CTD) is driven by a synergy between site-specific interactions mediated by the conserved region (CR, aa 319-341) and transient interactions involving hydrophobic residues (phenylalanine and methionine) in regions flanking the CR. This claim is supported by atomistic simulations, coarse-grained simulations, and in vitro experiments.
- **Visible evidence base** Main text including Results, Discussion, Methods, and figure references (Figs. 2-5, SI Appendix references)
- **Missing materials affecting confidence** Supplementary figures and tables (SI Appendix Figs. S2-S13, Tables S1-S2), full methods details, simulation parameters, and experimental protocols are not provided in the submitted material

## Reviewer
- **Overall assessment** This manuscript presents a systematic and multi-scale investigation of the molecular determinants of TDP-43 CTD phase separation. The combination of atomistic simulations, coarse-grained modeling, and in vitro experiments provides a compelling case for the role of methionine and phenylalanine residues in modulating phase behavior. The work extends current understanding of the molecular grammar of low-complexity domains by highlighting the contribution of aliphatic residues, particularly methionine, which have been underappreciated in previous studies. The central claim of a synergy between site-specific CR-mediated interactions and transient flanking-region interactions is well-supported by the data presented, though some aspects require additional clarification.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, RNA-binding proteins, and neurodegenerative diseases (ALS, FTD, Alzheimer's) would find this work highly relevant. The findings on methionine's role in phase separation could inform studies on other prion-like domains and low-complexity regions. The methodological approach combining atomistic and coarse-grained simulations with experimental validation serves as a template for similar investigations.
- **Major strengths** 1) Multi-scale approach integrating atomistic simulations, coarse-grained modeling, and in vitro experiments provides complementary evidence. 2) Systematic mutagenesis strategy to dissect residue-specific contributions. 3) Direct experimental validation of computational predictions. 4) Novel insight into methionine's role in phase separation, expanding the molecular grammar framework. 5) NMR-based structural characterization provides mechanistic detail at atomic resolution.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (simulation-experiment quantitative discrepancy), R1-M2 (CG model limitations for CR mutants)
- **Assessment against Nature-style criteria**  
  *Originality*: The work provides novel mechanistic insight into the role of methionine residues in phase separation, which has been largely overlooked. The concept of synergy between site-specific and transient interactions is a fresh perspective.  
  *Scientific importance*: TDP-43 is a clinically relevant protein, and understanding its phase separation mechanism has direct implications for neurodegenerative disease research. The findings may generalize to other prion-like domains.  
  *Interdisciplinary readership*: The work bridges computational biophysics, biochemistry, and cell biology, making it accessible to a broad audience. However, some simulation details may be challenging for experimentalists.  
  *Technical soundness*: The methodology is generally rigorous, but the quantitative discrepancy between simulation and experiment for the 5M→ACR mutant (R1-M1) and the CG model limitations (R1-M2) need to be addressed.  
  *Readability for nonspecialists*: The manuscript is well-structured and clearly written. The significance statement effectively communicates the broader relevance. Some technical jargon in the simulation sections may require careful reading.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly the quantitative discrepancy for the 5M→ACR mutant and the CG model limitations for CR mutations.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative consistency between simulation and experiment
- **Claim pointer** The authors state that "the observed increase in csat for 6F→A and 5M→AIDR mutants is consistent with predictions from CG simulations" and that "5M→ACR variant inhibits phase separation (csat > 120 μM)."
- **Evidence pointer** Results section, Fig. 3D and Fig. 4B
- **Concern** The CG simulations predict a ~two-fold increase in csat for 5M→ACR, but the experiments show a much more dramatic effect (csat > 120 μM, i.e., >6-fold increase compared to WT at ~20 μM). The authors acknowledge this discrepancy in the text but do not provide a satisfactory explanation or attempt to reconcile it. This quantitative mismatch raises questions about the predictive power of the CG model for mutations within the CR, which is a critical region for the proposed mechanism.
- **Why it matters** The central claim of the paper relies on the ability of the CG model to accurately predict the relative contributions of different residues to phase separation. If the model fails quantitatively for CR mutations, the conclusions drawn from the simulation data for other mutants may be less reliable. This discrepancy also limits the utility of the CG model for future predictive studies.
- **Resolution test** The authors should provide a more detailed analysis of why the CG model underestimates the effect of CR methionine mutations. This could include: (1) testing whether the rigid CR helix constraint in the CG model prevents proper sampling of the conformational changes induced by the mutations; (2) performing additional simulations with a more flexible CR representation; (3) providing a quantitative comparison of the simulated and experimental csat values for all mutants, with error bars and statistical significance tests.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Model limitations for CR mutations
- **Claim pointer** The authors state that "we carefully engineered these variants to avoid the disruption of helicity present in the CR, which is critical for CTD self-assembly" and use the CG model to predict csat changes for CR mutants.
- **Evidence pointer** Results section, Fig. 3D, Methods section
- **Concern** The CG model uses a single-bead-per-amino-acid representation and does not explicitly account for secondary structure propensities, except for the rigid CR constraint. The authors acknowledge that the CG model does not capture the difference between 5M→ACR and 5M→AIDR as well as experiments do. However, the model's inability to capture the full effect of CR mutations may be due to a more fundamental limitation: the model does not account for the coupling between secondary structure stability and intermolecular interactions. The methionine-to-alanine mutations in the CR could affect helix stability, which in turn would affect helix-helix interactions, but this coupling is not captured in the CG model.
- **Why it matters** The proposed mechanism of synergy between site-specific and transient interactions relies on the CR maintaining its helical structure while flanking regions provide additional contacts. If the CG model cannot accurately capture the effects of mutations on the CR, the mechanistic conclusions drawn from the simulations for this region are uncertain.
- **Resolution test** The authors should either: (1) provide additional validation of the CG model for CR mutations by comparing with atomistic simulations of the mutant CR peptides; (2) perform atomistic simulations of the full CTD for key mutants to directly assess the effects on helix stability and interactions; (3) clearly state the limitations of the CG model for CR mutations and temper the conclusions drawn from these simulations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of findings
- **Claim pointer** The authors state that "our results suggest that other aliphatic residues except alanine may have similar contributions, expanding the molecular grammar of low-complexity domain phase separation."
- **Evidence pointer** Discussion section
- **Concern** The claim that aliphatic residues generally contribute to phase separation is based on a limited set of mutations (methionine to alanine, leucine, or tyrosine) in a single protein. While the authors provide some supporting evidence from sequence analysis and comparison with other systems, the generalizability of this claim is not fully established. The authors do not test whether other aliphatic residues (e.g., isoleucine, valine) have similar effects, nor do they examine whether the observed effects are specific to the TDP-43 CTD context.
- **Why it matters** The claim of expanding the molecular grammar has broad implications for understanding phase separation in other systems. If the findings are not generalizable, this claim could be misleading.
- **Resolution test** The authors should either: (1) provide additional experimental or computational evidence from other low-complexity domains or prion-like domains to support the generalizability claim; (2) temper the claim to be specific to TDP-43 CTD; (3) provide a more detailed analysis of the physicochemical basis for the observed aliphatic residue contributions.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of simulation details
- **Affected element** Methods section
- **Evidence pointer** Methods section, "Refer to SI Appendix for details"
- **Issue** The Methods section is extremely brief and refers the reader to the SI Appendix for all simulation and experimental details. While this is common practice, the main text should include at least a summary of key parameters (e.g., simulation length, number of replicas, force field parameters, experimental conditions) to allow readers to assess the quality of the work without accessing the SI.
- **Required correction** Add a brief summary of key methodological parameters in the main text Methods section, including simulation time scales, system sizes, and experimental conditions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical analysis
- **Affected element** Fig. 4B and related text
- **Evidence pointer** Results section, Fig. 4B
- **Issue** The csat values for WT and mutants are presented, but it is unclear how many independent replicates were performed and what the error bars represent. The text mentions "nearly two-fold higher csat" and "order of magnitude" differences, but without statistical analysis, it is difficult to assess the significance of these differences.
- **Required correction** Provide information on the number of replicates, error bars, and statistical tests used to compare csat values between WT and mutants.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Figure accessibility
- **Affected element** Figs. 2-5
- **Evidence pointer** Results section
- **Issue** The figures are referenced but not provided in the submitted material. The text descriptions are generally clear, but some specific data points (e.g., exact csat values, contact maps) would benefit from direct visualization.
- **Required correction** Ensure that all figures are included in the final submission and that the text descriptions are sufficient for readers to understand the key findings without needing to access the SI.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Discussion of alternative mechanisms
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The authors propose a synergy between site-specific and transient interactions but do not discuss alternative mechanisms that could explain their observations, such as changes in overall hydrophobicity or charge distribution upon mutation.
- **Required correction** Add a brief discussion of alternative explanations and why the proposed mechanism is favored over these alternatives.

## Risk / unsupported claims
- The claim that "other aliphatic residues except alanine may have similar contributions" is not directly tested and is inferred from limited data.
- The quantitative discrepancy between CG simulation predictions and experimental results for the 5M→ACR mutant is acknowledged but not fully explained.
- The generalizability of the findings to other low-complexity domains is suggested but not directly demonstrated.
- The statement that "methionine residues, surprisingly, substantially contribute toward interactions that drive the phase separation of CTD" is supported by the data, but the mechanistic basis for this contribution (beyond hydrophobicity) is not fully explored.
- The proposed synergy between site-specific and transient interactions is a plausible interpretation of the data, but direct evidence for the synergy (as opposed to additive effects) is not provided.