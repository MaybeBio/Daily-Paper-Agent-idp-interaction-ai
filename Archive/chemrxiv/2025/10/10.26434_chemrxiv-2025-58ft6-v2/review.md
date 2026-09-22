## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the supplied abstract; no figures, methods, or supplementary material were provided
- **Shared manuscript claim summary** The authors report a combined ion mobility-mass spectrometry (IM-MS) and molecular dynamics (MD) study of the intrinsically disordered protein COR15A from Arabidopsis thaliana. They observe two dominant conformational families in the gas phase, generate a pseudo-CCS distribution from MD simulations that closely matches the experimental IM-MS data, and argue that this correspondence indicates the gas-phase conformers represent natively accessible states relevant to dehydration responses.
- **Visible evidence base** Abstract text only; no figures, tables, methods details, or statistical analyses are available
- **Missing materials affecting confidence** Full manuscript, all figures and tables, experimental methods (IM-MS parameters, sample preparation, charge state assignment), MD simulation details (force field, temperature protocol, sampling time, convergence criteria), SAXS comparison data, and any statistical or error analysis

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting application of IM-MS combined with MD to study a dehydration-responsive intrinsically disordered protein. The central claim, that the gas-phase conformational families correspond to natively accessible states, is plausible but cannot be evaluated from the abstract alone. The key evidence, namely the quantitative comparison between experimental CCS distributions and MD-derived pCCS, is described only qualitatively. The work may be of interest to the biophysics and structural biology communities, but the current evidence base is insufficient to assess technical soundness or the strength of the conclusions.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, particularly those involved in abiotic stress responses in plants, would be interested. The methodological combination of IM-MS with elevated-temperature MD for conformational sampling of disordered proteins may also appeal to biophysicists developing hybrid experimental-computational approaches. The potential to observe dehydration-responsive conformational changes in LEA proteins could interest the broader plant stress biology community.
- **Major strengths** The combination of IM-MS with MD-based pseudo-CCS generation is a modern and potentially powerful approach for studying disordered proteins. The observation of two dominant coexisting conformational families with sub-conformers suggests the method has sufficient resolution to distinguish distinct populations. The explicit comparison with SAXS-derived structures under functional conditions is a thoughtful attempt to bridge gas-phase and solution-state data.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The quantitative match between experimental and simulated CCS distributions is asserted but not demonstrated. The relationship between gas-phase conformers and "natively accessible states" requires a clear argument about how the elevated-temperature MD sampling relates to physiological conditions. The claim that IM-MS permits observation of dehydration-responsive conformers is not supported by any data shown in the abstract.
- **Assessment against Nature-style criteria**  
  - Originality: The application of IM-MS with MD to a LEA protein is not entirely novel, but the specific focus on dehydration-responsive conformational populations may offer a fresh angle.  
  - Scientific importance: The functional relevance of conformational heterogeneity in COR15A to dehydration tolerance is potentially significant, but the abstract does not establish a clear link between the observed conformers and biological function.  
  - Interdisciplinary readership: The work bridges mass spectrometry, molecular simulation, and plant stress biology, which could attract a broad audience if the evidence is compelling.  
  - Technical soundness: Cannot be assessed from the abstract; critical details on IM-MS calibration, MD convergence, and comparison methodology are absent.  
  - Readability for nonspecialists: The abstract is reasonably clear, though terms such as "pseudo-CCS distribution" and "sub conformers" may require more explanation in the full text.
- **Recommendation posture** Currently not established from the provided evidence. The abstract describes a plausible and potentially interesting study, but the central claims require the full manuscript to verify. A supportive posture would be possible if the technical concerns are resolved in the full paper.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** The authors claim that the MD-derived pseudo-CCS distribution is "highly similar" to the experimental IM-MS data, and that this provides "compelling evidence" that the gas-phase data corresponds to natively accessible states.  
- **Evidence pointer** Abstract, results description; location not provided  
- **Concern** The abstract states that the pCCS distribution is "highly similar" to the experimental data, but no quantitative metrics are provided. There is no indication of the degree of overlap, the resolution of the comparison, or whether the match is within experimental uncertainty. The claim of "compelling evidence" is therefore unsupported by the visible material.  
- **Why it matters** The central conclusion of the paper rests on the fidelity of the MD-generated pCCS to the experimental CCS distributions. Without quantitative comparison, the reader cannot judge whether the match is meaningful or coincidental, and the claim that gas-phase conformers reflect natively accessible states is not established.  
- **Resolution test** Provide quantitative measures of agreement between experimental and simulated CCS distributions, such as root-mean-square deviation, overlap coefficients, or per-feature comparisons, along with an assessment of whether the match is within experimental and simulation uncertainty.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Conceptual validity  
- **Claim pointer** The authors state that the experimental gas-phase data corresponds to natively accessible states, implying that the conformers observed in IM-MS are representative of the protein's conformational ensemble under functional conditions.  
- **Evidence pointer** Abstract, interpretation section; location not provided  
- **Concern** The abstract does not explain how the elevated-temperature MD simulations relate to the conditions under which COR15A functions in vivo. The protein is expressed in response to cold and dehydration, but the MD simulations are performed at elevated temperature for enhanced sampling. The connection between these simulation conditions and the native or stress-relevant states of the protein is not articulated.  
- **Why it matters** If the MD sampling is performed under conditions that do not mimic the functional environment, the correspondence between simulated and experimental data may not establish that the gas-phase conformers are natively relevant. The claim of native accessibility requires a clear argument about the relationship between simulation conditions, gas-phase transfer, and physiological states.  
- **Resolution test** Provide a detailed explanation of how elevated-temperature MD sampling relates to the conformational ensemble under physiological conditions, including any validation against solution-state data beyond SAXS, and discuss the potential effects of the electrospray ionization process on the observed conformer populations.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Claim support  
- **Claim pointer** The authors claim that IM-MS permits "simultaneous observation of disordered forms as well as conformers populated upon dehydration," implying that the method can distinguish dehydration-responsive conformers from the intrinsically disordered ensemble.  
- **Evidence pointer** Abstract, final sentence; location not provided  
- **Concern** The abstract does not present any data showing dehydration-induced changes in the conformational landscape. No comparison is shown between COR15A under hydrated versus dehydrated conditions, nor is there any indication that the observed conformational families are specifically responsive to dehydration rather than being intrinsic to the protein's gas-phase behavior.  
- **Why it matters** The stated advantage of the method for studying dehydration-responsive LEA proteins is a key motivation for the work. Without evidence that the observed conformers are actually dehydration-responsive, this claim is speculative and the broader significance of the study is weakened.  
- **Resolution test** Include experimental data comparing the conformational distributions of COR15A under conditions that mimic hydrated and dehydrated states, or clearly state the limitations of the current study in addressing dehydration responsiveness.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Terminology  
- **Evidence pointer** Abstract, charge state description; location not provided  
- **Issue** The abstract states that charge states from +5 to +12 are observed, but does not specify whether all charge states were included in the CCS distribution analysis or whether some were excluded due to overlap or low intensity.  
- **Required correction** Clarify whether the reported CCS distributions are derived from all observed charge states or a subset, and justify any exclusions.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** SAXS comparison  
- **Evidence pointer** Abstract, SAXS reference; location not provided  
- **Issue** The abstract mentions comparison with SAXS-derived structures but does not state whether the SAXS data were collected under conditions relevant to the functional state of COR15A, nor how the comparison was performed.  
- **Required correction** Provide details on the SAXS experimental conditions and the method of comparison with the MD-derived conformers.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Precision  
- **Affected element** Conformer description  
- **Evidence pointer** Abstract, CCS values; location not provided  
- **Issue** The abstract reports two dominant conformational families centered at approximately 1200 and 1800 Å2, but does not indicate the width of these distributions or the criteria used to define the families and sub-conformers.  
- **Required correction** Specify the criteria for defining conformational families and sub-conformers, and report the distribution widths or standard deviations.

## Risk / unsupported claims
- The claim that the MD-derived pCCS distribution is "highly similar" to experimental data is unsupported without quantitative comparison.
- The claim that gas-phase conformers correspond to "natively accessible states" is not established from the abstract alone.
- The claim that IM-MS permits observation of dehydration-responsive conformers is unsupported, as no dehydration-specific data are presented.
- The relationship between elevated-temperature MD sampling and physiological conditions is not explained, making the relevance of the simulated ensemble unclear.