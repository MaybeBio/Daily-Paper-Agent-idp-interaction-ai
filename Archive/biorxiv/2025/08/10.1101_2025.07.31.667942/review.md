## Review setup

- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, conclusion, and materials and methods. Figures, tables, and supplementary information are referenced but not provided.
- **Assessment boundary** Scientific validity of the claims, technical soundness of the NMR methodology, interpretation of results, and coherence of the proposed model. Not assessed: formatting, grammar, or editorial quality.
- **Shared manuscript claim summary** The authors report that the N-terminal domain of FAT10 (N-FAT10-C0) undergoes a conformational change upon binding to the adapter protein NUB1L, transitioning from a folded ubiquitin-like β-grasp structure to a largely disordered state stabilized by an intermolecular β-sheet. This "holdase" mechanism is proposed to prepare FAT10 for rapid proteasomal degradation.
- **Visible evidence base** Abstract, full introduction, results section (narrative only), discussion, conclusion, and materials and methods. Figures S1-S14, Tables S1-S5, and all spectra are referenced but not included in the provided material.
- **Missing materials affecting confidence** All figures and tables, including the key NMR spectra (Figures 1-5), the AlphaFold-Multimer prediction (Figure 5a), the double-REDOR data (Figures 5b,c, S11-S14), and the chemical shift tables (Tables S3-S5). Without these, the experimental evidence cannot be directly evaluated.

## Reviewer

- **Overall assessment** This manuscript presents a potentially significant finding: that the interaction between FAT10 and NUB1L involves a disorder-to-order transition at a specific region, coupled with global unfolding of the FAT10 N-domain. The use of MAS NMR to study a challenging protein-protein interaction involving a partially disordered species is commendable and technically ambitious. However, the manuscript as provided is incomplete, with all primary data confined to figures and supplementary material that were not made available for review. The central claims, particularly the formation of an intermolecular β-sheet and the "holdase" model, rest on evidence that cannot be verified from the text alone. The narrative is coherent and the interpretation is plausible, but the strength of the conclusions cannot be assessed without the underlying spectra and analysis.
- **Who would be interested in the results, and why** Researchers in the fields of ubiquitin-like modifiers, proteasomal degradation, protein folding and misfolding, and structural biology of intrinsically disordered proteins. The proposed "holdase" mechanism for NUB1L, if substantiated, would be of interest to those studying protein quality control and inflammation-linked proteostasis. The methodological approach, using MAS NMR to characterize a fuzzy complex, would also appeal to NMR spectroscopists and structural biologists working on challenging systems.
- **Major strengths** The study addresses a long-standing question about the functional relevance of FAT10's loose folding. The combination of MAS NMR with AlphaFold-Multimer predictions is a modern and appropriate approach. The authors are transparent about the limitations of their data, particularly the disappearance of signals and the distinction between disorder and dynamics. The discussion of the results in the context of prior work, including the hydrogen-deuterium exchange study by Arkinson et al., is thoughtful and balanced.
- **Major Concerns** The absence of all primary data is a fundamental limitation for this review. The central claims rest on spectral assignments and quantitative analyses that cannot be checked. The interpretation of the double-REDOR data, which is critical for establishing the intermolecular interface, is presented only in narrative form. The discrepancy between the AlphaFold-Multimer prediction and the experimental data regarding the extent of the β-sheet is acknowledged but not fully resolved. The functional significance of the "holdase" model, while plausible, is not directly tested.
- **Minor Comments** The manuscript would benefit from a more explicit statement of the hypothesis being tested. The distinction between "disorder" and "dynamics" in the discussion is useful but could be elaborated. The potential role of the C-terminal domain of FAT10 in the interaction with NUB1L is not discussed, despite its likely relevance.
- **Technical failings that need to be addressed before the case is established** The primary technical evidence, namely the MAS NMR spectra, chemical shift assignments, and double-REDOR data, must be made available for evaluation. The quantitative analysis of the double-REDOR data, including the fitting procedures and error estimates, needs to be described in detail. The authors should provide a more rigorous comparison between the experimental β-strand boundaries and the AlphaFold-Multimer prediction, including a discussion of the structural implications of the discrepancy.
- **Assessment against Nature-style criteria**  
  - **Originality** High. The proposed "holdase" mechanism for NUB1L and the observation of a β-sheet-mediated interaction with a largely unfolded FAT10 N-domain are novel.  
  - **Scientific importance** Potentially high, if the model is correct. The work could reshape understanding of how FAT10 is prepared for degradation and how adapter proteins can modulate the folding state of their clients.  
  - **Interdisciplinary readership** Moderate. The topic is of interest to cell biologists, biochemists, and structural biologists, but the specialized NMR methodology may limit broader appeal.  
  - **Technical soundness** Cannot be fully assessed from the provided material. The methodology is appropriate in principle, but the evidence is not visible.  
  - **Readability for nonspecialists** The manuscript is clearly written and the concepts are explained well, but the results section assumes familiarity with NMR spectroscopy and protein structure.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript is promising and the narrative is compelling, but the absence of all primary data prevents a definitive assessment. A revised submission with the full figures and supplementary information would be required for a proper evaluation.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence availability
- **Claim pointer** The authors claim that "a stretch of residues that is intrinsically disordered when the N-domain of FAT10 is in its ubiquitin-like β-sheet fold, becomes part of a regularly structured loop and an intermolecular β-sheet upon binding to NUB1L."
- **Evidence pointer** Figures 2-5, Tables S3-S5, location not provided
- **Concern** All primary data, including the NMR spectra, chemical shift assignments, and the AlphaFold-Multimer prediction, are confined to figures and tables that were not provided for review. The central claims of the manuscript cannot be verified without these data.
- **Why it matters** The conclusions rest entirely on the interpretation of these spectra and analyses. Without access to them, the validity of the assignments, the secondary structure predictions, and the double-REDOR measurements cannot be assessed.
- **Resolution test** Provide the full set of figures and supplementary tables, including annotated spectra, assignment tables, and confidence scores for the AlphaFold-Multimer prediction.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental evidence for the holdase model
- **Claim pointer** The authors propose that "NUB1L stabilizes N-FAT10 in an unfolded state, acting as a holdase."
- **Evidence pointer** Figures 4-5, S11-S14, location not provided
- **Concern** The "holdase" model is inferred from the selective visibility of certain residues in the MAS NMR spectra and the double-REDOR data. However, the evidence that NUB1L actively stabilizes the unfolded state, rather than merely binding to a pre-existing unfolded population, is not presented. The distinction between "stabilizing" and "selecting" an unfolded state is functionally important.
- **Why it matters** The proposed mechanism has implications for how FAT10 is targeted for degradation. If NUB1L merely captures a transiently unfolded state, the model is different from one in which NUB1L actively unfolds FAT10. The current data, as described, cannot distinguish between these possibilities.
- **Resolution test** Provide additional experiments or analyses that address the mechanism of unfolding, such as kinetic measurements, or a more detailed discussion of the equilibrium between folded and unfolded states in the presence and absence of NUB1L.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Functional significance
- **Claim pointer** The authors state that "the ability of FAT10 to interact in folded as well as unfolded form is essential for its role in inflammation-linked proteostasis."
- **Evidence pointer** Discussion, location not provided
- **Concern** The functional significance of the proposed conformational change is not directly tested. The manuscript demonstrates a structural transition but does not show that this transition is required for degradation or that disrupting it would impair FAT10 function.
- **Why it matters** The claim of "essential" function is strong and requires experimental support. Without functional assays, the physiological relevance of the observed structural changes remains speculative.
- **Resolution test** Provide functional data, such as degradation assays with mutants that disrupt the β-sheet interaction or the holdase function, to demonstrate the biological importance of the proposed mechanism.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section, "Valuation of Samples"
- **Evidence pointer** Section "Valuation of Samples", location not provided
- **Issue** The section title "Valuation of Samples" is unusual; "Validation" or "Characterization" would be more standard.
- **Required correction** Rename the section to "Validation of Samples" or "Sample Characterization."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion of the C-terminal domain
- **Evidence pointer** Discussion, location not provided
- **Issue** The manuscript focuses exclusively on the N-terminal domain of FAT10. The potential role of the C-terminal domain in the interaction with NUB1L or in the degradation process is not discussed.
- **Required correction** Add a brief discussion of the C-terminal domain and its possible contributions to the interaction or the degradation mechanism.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Double-REDOR data interpretation
- **Evidence pointer** Figures 5b,c, S11-S14, location not provided
- **Issue** The authors suggest that the lower final S/S0 ratio for the Cα region compared to other regions may be due to longer Cα-H distances in the β-sheet. This interpretation is plausible but could be strengthened by a more quantitative analysis or by comparison with control experiments.
- **Required correction** Provide a more detailed analysis of the double-REDOR data, including error estimates and a discussion of alternative interpretations.

## Risk / unsupported claims

- The claim that NUB1L acts as a "holdase" that stabilizes N-FAT10 in an unfolded state is not directly supported by the provided evidence, as the distinction between active unfolding and selective binding to an unfolded population is not addressed.
- The claim that the ability of FAT10 to interact in both folded and unfolded forms is "essential" for its function is not tested experimentally.
- The assertion that the observed residues in the FAT10-NUB1L complex are at the interface is based on double-REDOR data that are not visible in the provided material.
- The statement that the AlphaFold-Multimer prediction of the β-sheet is "experimentally confirmed" is only partially supported, as the experimental data suggest a longer β-sheet than predicted, and the discrepancy is not fully resolved.