## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodology, validity of claims, and presentation quality
- **Shared manuscript claim summary** The authors use coarse-grained simulations with constant-pH Monte Carlo to study charge regulation and conformation of short peptides with diblock and alternating sequences of acidic and basic amino acids, varying the pKA difference (ΔpKA). They report that sequence has little effect on total charge due to cancellation of effects, but significantly affects conformation. They validate against potentiometric titration and NMR experiments for one new peptide (Tyr5-Lys5) and reference prior validation for two others.
- **Visible evidence base** Abstract, full text including Methods, Results and Discussion, Conclusions, Figures 1-10 (described in text), Tables 1-2 (described in text), references to ESI sections
- **Missing materials affecting confidence** Electronic Supplementary Information (ESI) referenced but not provided; raw numerical data for figures not provided; experimental details for NMR and titration only summarized, not fully described

## Reviewer
- **Overall assessment** This manuscript presents a systematic computational study of charge regulation in short model peptides, addressing an important gap in understanding how sequence and pKA differences affect ionization and conformation in flexible polyampholytes. The work builds logically on prior validated models and extends them to a broader parameter space. The central finding that sequence affects conformation but not total charge (due to cancellation) is interesting and potentially useful. However, the manuscript has several weaknesses: the experimental validation for the new peptide is incomplete (no CZE, large NMR uncertainties), the chain-length study is limited to one sequence type, and some claims about "quantitative agreement" appear overstated given the acknowledged systematic shifts. The presentation is generally clear but some figure descriptions lack quantitative detail. The work is likely of interest to the polymer physics and peptide biophysics communities, though its direct biological relevance is somewhat limited by the highly simplified model.

- **Who would be interested in the results, and why** Researchers studying charge regulation in weak polyelectrolytes and polyampholytes, computational polymer physicists developing coarse-grained models, and scientists working on pH-responsive materials or intrinsically disordered proteins where sequence-dependent charge effects are relevant. The demonstration that sequence affects conformation but not total charge could inform design principles for peptide-based materials.

- **Major strengths** 
  1. Systematic exploration of ΔpKA space, from strongly negative to zero, using both real and hypothetical amino acids
  2. Clear demonstration that total charge is nearly sequence-independent while conformation is strongly sequence-dependent, with a mechanistic explanation
  3. Use of a model previously validated against experiments, lending credibility to predictions
  4. Inclusion of experimental validation for a new peptide sequence (Tyr5-Lys5)
  5. Investigation of chain-length effects, extending relevance beyond the short peptides studied experimentally

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental validation
- **Claim pointer** "The comparison of total charge in Figure 6a reveals a quantitative agreement between the simulations and titrations" and "we may still conclude that simulation predictions are in agreement also with this experimental method" (Section 3.2)
- **Evidence pointer** Section 3.2, Figure 6
- **Concern** The experimental validation for Tyr5-Lys5 is substantially weaker than claimed. The authors acknowledge that CZE could not be performed, that the titration data required an arbitrary shift to correct for TFA counterions, and that NMR uncertainties are large. The statement "quantitative agreement" appears to rely on a shifted curve with an adjustable parameter (xTFA), which undermines the claim of parameter-free validation. The NMR comparison shows worse agreement, attributed to "simplified method" of analysis. Given these caveats, the validation is more qualitative than quantitative.
- **Why it matters** The manuscript's credibility rests partly on experimental validation of the simulation model. If the validation is only qualitative, the strength of subsequent predictions about unvalidated peptide sequences is reduced. The claim of "quantitative agreement" without CZE data and with adjustable shifts is potentially misleading.
- **Resolution test** Provide a more careful and honest assessment of the level of agreement, distinguishing between qualitative trend capture and quantitative accuracy. If possible, quantify the uncertainty in the titration-derived charge and show whether the simulation falls within experimental error bars. Alternatively, present the validation as qualitative and temper the language accordingly.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Scope of chain-length study
- **Claim pointer** "Finally, we looked into the role of chain length, using just one selected peptide" (Section 4) and the general claim that "as the chain length is increased, the magnitude of all effects increases"
- **Evidence pointer** Section 3.4, Figures 9-10
- **Concern** The chain-length study is limited to Lys-Asp peptides only. The authors do not investigate whether the observed trends (increased deviation from ideal ionization, more compact conformations for diblock) hold for other ΔpKA values, particularly the ΔpKA≈0 case where the behavior is most complex. The claim that "all effects" increase with chain length is therefore only demonstrated for one specific peptide pair.
- **Why it matters** The conclusions about chain-length effects are presented as general, but the evidence base is narrow. For the ΔpKA≈0 case, where ionization of both acid and base groups changes simultaneously, chain-length effects could differ qualitatively. The generalization limits the utility of the findings for designing longer peptides or proteins.
- **Resolution test** Either extend the chain-length study to at least one additional ΔpKA value (e.g., the hypothetical ΔpKA=0 case), or explicitly restrict the conclusions to the Lys-Asp system and discuss why generalization may or may not be appropriate.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Mechanistic explanation
- **Claim pointer** "we showed that changing the sequence while keeping the same overall composition has a profound effect on the conformation, whereas it practically does not affect total charge on the peptide" and the explanation involving "cancellation of effects"
- **Evidence pointer** Section 3.1, Figures 3-5
- **Concern** The claim that sequence does not affect total charge is presented as a robust finding, but the mechanistic explanation of "cancellation of effects" is somewhat vague. The authors state that diblock and alternating sequences exhibit similar total charge but do not provide a detailed quantitative decomposition of the competing effects (e.g., enhanced vs. suppressed ionization of individual groups) that would make the cancellation mechanism transparent. The explanation is largely qualitative.
- **Why it matters** The central scientific contribution is the decoupling of charge from conformation. Without a clear mechanistic understanding of why this decoupling occurs, the finding remains descriptive rather than explanatory. A quantitative analysis of the individual group ionization contributions would strengthen the paper and make the cancellation mechanism concrete.
- **Resolution test** Provide a quantitative decomposition of the ionization of acid and base groups separately for diblock vs. alternating sequences, showing how the enhanced ionization of one group is offset by suppressed ionization of the other, and how this balance depends on ΔpKA.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Model limitations
- **Claim pointer** "This agreement provides a very promising perspective of using similar modeling techniques to predict charge regulation and concomitant conformational changes not only in short oligopeptides but also in flexible disordered proteins or synthetic ampholytes" (Section 4)
- **Evidence pointer** Section 4, Section 2.1
- **Concern** The extrapolation to intrinsically disordered proteins and synthetic ampholytes is speculative. The model is highly coarse-grained, with implicit solvent, no explicit hydrogen bonding, no secondary structure, and no sequence-specific interactions beyond electrostatics. Real proteins have diverse side-chain chemistries, backbone effects, and hydrophobic interactions that are absent here. The claim of "promising perspective" is not supported by any evidence that the model captures these additional complexities.
- **Why it matters** Overstating the applicability of the model to biological systems could mislead readers about its predictive power. The model may be useful for understanding generic electrostatic effects, but its relevance to specific proteins requires demonstration, not assertion.
- **Resolution test** Either temper the claim to specify that the model captures generic electrostatic effects relevant to disordered proteins, or provide a brief discussion of what additional physics would be needed for quantitative predictions of real proteins.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure descriptions
- **Evidence pointer** Figures 3-5, 7, 9-10
- **Issue** The text describes trends in figures but often lacks quantitative detail (e.g., "slightly lower," "somewhat higher," "much more pronounced"). Without numerical values or error bars in the text, it is difficult for readers to assess the magnitude of effects.
- **Required correction** Add quantitative values (e.g., differences in charge or Re at specific pH values) or refer to specific data points in the figures to support qualitative statements.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodology
- **Affected element** Simulation parameters
- **Evidence pointer** Section 2.1.4
- **Issue** The simulation protocol states 10 chains per box and 105 cycles, but no information is given about the number of independent runs or how statistical uncertainties were propagated to derived quantities like pKA shifts.
- **Required correction** Provide details on the number of independent simulations, block averaging procedures, and how error bars in figures were computed.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Experimental methods
- **Affected element** NMR analysis
- **Evidence pointer** Section 2.3.3, Section 3.2
- **Issue** The method for extracting a single chemical shift value from overlapping peaks is described as "simplified" but the details are not given. The uncertainty in NMR-derived charge is acknowledged as large but not quantified.
- **Required correction** Provide a brief description of the peak-fitting or center-of-mass method used, and report the estimated uncertainty in the NMR-derived ionization degree.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction
- **Evidence pointer** Section 1
- **Issue** The introduction cites prior work on polyelectrolyte simulations and charge regulation but does not discuss recent experimental or computational studies on sequence-dependent charge effects in intrinsically disordered proteins, which are directly relevant.
- **Required correction** Add a brief discussion of how this work relates to recent findings on charge patterning in disordered proteins (e.g., effects of charge blockiness on conformation).

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract and Section 3.1
- **Evidence pointer** Abstract, Section 3.1
- **Issue** The term "charge regulation" is used to describe both the general phenomenon of pH-dependent ionization and the specific deviations from ideal Henderson-Hasselbalch behavior. This dual usage could confuse readers.
- **Required correction** Define the term clearly at first use and consider using "non-ideal ionization" or "electrostatic modulation of pKA" for the specific deviations.

## Risk / unsupported claims
- The claim of "quantitative agreement" with titration data for Tyr5-Lys5 is not fully supported given the adjustable shift for TFA correction and the acknowledged systematic issues (Section 3.2, Figure 6)
- The extrapolation to intrinsically disordered proteins and synthetic ampholytes (Section 4) is speculative and not supported by evidence presented
- The statement that "all effects" increase with chain length (Section 3.4) is only demonstrated for the Lys-Asp system
- The claim that sequence "practically does not affect total charge" is presented as general but is only shown for the specific peptide lengths and compositions studied
- The mechanistic explanation of "cancellation of effects" is qualitative and not quantitatively demonstrated
- The assertion that the model could be used to "predict" charge regulation in real proteins (Section 4) overstates the model's capabilities given its simplifications