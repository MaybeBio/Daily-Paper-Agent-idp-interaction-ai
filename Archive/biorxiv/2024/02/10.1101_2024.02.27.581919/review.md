## Review setup
- **Input scope** Full manuscript text (summary, introduction, results, discussion, experimental procedures) without figures, tables, or supplementary materials
- **Assessment boundary** Scientific claims, methodological soundness, and internal consistency based solely on the provided text; structural biology and biophysical claims assessed from narrative descriptions only
- **Shared manuscript claim summary** The authors propose a two-step "dock-and-lock" model for EB1's EBH domain interaction with SxIP-containing ligands, where the SxIP motif provides initial low-affinity docking into a partially formed pocket, followed by induced folding of the EBH C-terminus that locks the complex and provides the majority of binding affinity. They support this with NMR structures, dynamics, ITC, and live-cell imaging, and demonstrate rational affinity enhancement to nanomolar levels.
- **Visible evidence base** Narrative descriptions of NMR spectroscopy (HSQC titrations, relaxation, CEST, structure calculation), ITC measurements, molecular docking predictions, and live-cell imaging experiments; Table 1 referenced but not visible; Figures 1-5 referenced but not visible; Supplementary Figures S1-S10 and Tables S1 referenced but not visible
- **Missing materials affecting confidence** All figures, tables, supplementary materials, structural coordinates, and raw data; the actual NMR structure (PDB 7OLG) and chemical shift assignments (BMRB 34629) are deposited but not accessible from the manuscript text alone; no quantitative data visible for any binding measurements

## Reviewer

### Overall assessment
This manuscript addresses a significant question in microtubule plus-end tracking biology: how EB1 achieves selective yet tunable interactions with diverse SxIP-containing ligands. The proposed "dock-and-lock" model is conceptually appealing and consistent with the emerging understanding of coupled folding and binding in intrinsically disordered protein regions. The authors provide a plausible mechanistic framework supported by multiple biophysical techniques. However, the manuscript as presented has substantial limitations. The most critical issue is that the central quantitative claims, including the two orders of magnitude affinity enhancement and the kinetic parameters for each step, cannot be evaluated from the text alone. The narrative describes results but does not present the actual data. The distinction between the "dock" and "lock" steps, while mechanistically reasonable, rests on indirect evidence, and the authors themselves acknowledge that the intermediate state could not be directly detected. The live-cell experiments, while conceptually important, appear to show only modest effects for the monomeric constructs, and the interpretation is complicated by the use of a different fluorescent tag than previous studies. The manuscript would be substantially strengthened by presenting the actual binding data, structural statistics, and imaging quantifications.

### Who would be interested in the results, and why
Cell biologists studying microtubule dynamics and plus-end tracking proteins would find the mechanistic insight into EB1-ligand recognition valuable. Structural biologists interested in coupled folding and binding of intrinsically disordered proteins would appreciate the two-step model and the dissection of energetic contributions. Researchers in cancer biology might be interested given the involvement of EB1-interacting proteins like APC in tumor suppression. Additionally, those working on drug discovery targeting protein-protein interactions involving disordered regions could find the rational affinity enhancement strategy informative. The work bridges biophysics and cell biology in a way that should appeal to a broad readership.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim a two-step "dock-and-lock" model where the SxIP motif initially binds to a partially formed EBH pocket, followed by induced folding of the C-terminus, and that this model is validated by their structural and dynamics data.
- **Evidence pointer** Results sections "SxIP gives specificity in binding to EB1" and "Peptide binding changes the structure and dynamics of the EBH C-terminus"; Figure 1C-D, 2A-C; Supplementary Figures S1-S5
- **Concern** The central mechanistic claim of a two-step process rests on the assertion that the intermediate "dock" state could not be directly observed. The authors state that folding occurs "too fast" for direct detection, and the evidence for the two-step model is therefore indirect, based on comparisons between full-length and C-terminally truncated constructs. While this is a reasonable inference, the manuscript does not present the actual data that would allow assessment of whether alternative models (e.g., conformational selection, or a single-step induced fit with no kinetically distinguishable intermediate) are adequately excluded. The claim that the "lock" step is fast is based on the absence of exchange broadening, which is an argument from silence. The authors should present a more rigorous kinetic analysis, including simulations showing that the two-step model is required to explain the data and that simpler models fail.
- **Why it matters** The two-step "dock-and-lock" model is the central conceptual contribution of the manuscript. If the evidence does not distinguish this model from simpler alternatives, the mechanistic claim is not established. The distinction between "dock" and "lock" has implications for how the authors interpret the energetic contributions of different peptide regions and for the design of inhibitors.
- **Resolution test** Provide quantitative evidence, such as global fitting of titration data to competing models with statistical comparison, or direct detection of the intermediate state through experiments designed to populate it (e.g., mutations that stabilize the dock state, or experiments at lower temperatures). Alternatively, present simulations showing that the two-step model uniquely explains the observed line shapes and relaxation data.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Data accessibility
- **Claim pointer** The authors report dissociation constants ranging from approximately 10 mM for the 4-residue peptide to 16 ± 3 nM for the optimized VLLRK peptide, and kinetic parameters for each step of the proposed model.
- **Evidence pointer** Table 1; Results sections on peptide optimization and kinetics; Supplementary Figures S1, S3, S8-S10
- **Concern** None of the actual binding data are visible in the manuscript text. Table 1 is referenced but not shown. The ITC thermograms, NMR titration curves, and CEST profiles are described but not presented. This makes it impossible to assess the quality of the fits, the appropriateness of the models used, or the reliability of the reported values. For a manuscript whose primary contribution is quantitative biophysical characterization, this is a critical deficiency. The reader cannot verify that the reported KD values are well-determined, that the single-site model is appropriate for the ITC data, or that the dimer model used in TITAN is justified by the data.
- **Why it matters** The quantitative claims are the foundation of the manuscript. Without access to the actual data, the reported affinities and kinetic parameters cannot be evaluated. The claim of "two orders of magnitude" affinity enhancement, which is central to the rational design narrative, depends entirely on the accuracy of the KD measurements.
- **Resolution test** Include the actual figures and tables in the manuscript. Provide ITC thermograms with fits, NMR titration curves with fitted binding isotherms, and CEST profiles with fits. Present the complete Table 1 with all measured values and errors. If space is a concern, ensure that all data are available in the supplementary materials and clearly referenced.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Functional validation
- **Claim pointer** The authors state that the enhanced affinity of the VLLRK peptide leads to enhanced recruitment to microtubule plus ends in live cells, and that this validates the functional relevance of the affinity optimization.
- **Evidence pointer** Results section "Peptide optimisation in the post-SxIP region" and "High affinity peptides localise into comet-like structures in cells"; Figure 5A-C
- **Concern** The live-cell experiments show that the monomeric VLLRK peptide has a comet-to-cytoplasm ratio of approximately 0.02, which the authors describe as "extremely low." Only the dimeric construct shows substantial localization. This raises the question of whether the affinity enhancement from 3.5 µM to 16 nM is functionally meaningful for monomeric ligands in the cellular context, or whether avidity effects dominate. The authors acknowledge this but do not fully address the implications. If monomeric nanomolar affinity is insufficient for effective plus-end localization, then the physiological relevance of the affinity range explored here is unclear. Additionally, the comparison with previous work by Honnappa et al. is complicated by the use of mTFP instead of EGFP, and the authors attribute differences to EGFP dimerization but do not provide direct evidence for this claim.
- **Why it matters** The manuscript claims that the affinity optimization has functional consequences. If the monomeric peptide still does not localize effectively, the practical significance of the nanomolar affinity is questionable. The interpretation of the cell data depends on resolving the discrepancy with previous studies.
- **Resolution test** Provide quantitative imaging data with appropriate controls, including the EGFP-tagged constructs for direct comparison. Address whether the low localization of monomeric peptides reflects a fundamental limitation of monomeric ligands or a technical issue. Discuss the implications for the physiological relevance of the affinity range.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Model generalizability
- **Claim pointer** The authors suggest that their "dock-and-lock" model can be used to predict EBH affinity for different natural ligands and as a rationale for designing small-molecule inhibitors.
- **Evidence pointer** Discussion section; Supplementary Figure S8A
- **Concern** The manuscript demonstrates the model for one ligand, MACF, and one optimized variant. The claim of generalizability to other SxIP-containing ligands is not tested. The authors note that the post-SxIP region is not conserved, which implies that the "lock" step would vary substantially across ligands. The sequence comparison in Supplementary Figure S8A is mentioned but not shown. Without testing the model on multiple natural ligands with diverse post-SxIP sequences, the predictive power of the model is not established. The claim about inhibitor design is speculative and not supported by any data.
- **Why it matters** The broader significance of the work depends on whether the model applies to the diverse family of SxIP-containing proteins. If the "lock" step is highly sequence-dependent, the model may have limited predictive utility.
- **Resolution test** Test the model on at least 2-3 additional SxIP-containing peptides with different post-SxIP sequences. Present the sequence comparison and show that the model correctly predicts relative affinities. Alternatively, temper the claims of generalizability and inhibitor design.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Throughout
- **Issue** The term "dock-and-lock" is used consistently, but the authors also refer to "induced fit" in the discussion. The relationship between these terms is not explicitly clarified. The "dock" step is described as binding to a "partially formed pocket," which implies conformational selection rather than induced fit. The terminology should be used more carefully.
- **Required correction** Clarify the relationship between the proposed model and established concepts such as induced fit and conformational selection. Define "dock" and "lock" precisely in terms of structural and kinetic features.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Internal consistency
- **Affected element** Peptide nomenclature
- **Evidence pointer** Experimental Procedures, Peptides section
- **Issue** The peptide sequences listed in the Experimental Procedures do not match the names used in the text. The text refers to 4MACF, 6MACF, 9MACF, 11MACF, 11MACF-VLL, 11MACF-LLL, 11MACF-VLLRK, and 13CK5P2, but the sequences listed are 4MACF (SKIP), 6MACF (SKIPTP), 9MACF (SKIPTPQRK), 11MACF (KPSKIPTPQRK), 11MACF-VLL (KPSTAKSKIPVLL), 11MACF-LLL (KPSTAKSKIPLLL), 11MACF-VLLRK (KPSTAKSKIPVLLRK), and 13CK5P2 (KKSRLPRILIKRSR). The 11MACF-VLL and 11MACF-LLL sequences appear to have a different N-terminal context (KPSTAKS vs KPS) compared to the wild-type 11MACF. This discrepancy is not explained.
- **Required correction** Clarify the sequence context of the mutant peptides. If the N-terminal region was modified, explain why and how this affects the interpretation of the results.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Statistical analysis
- **Evidence pointer** Experimental Procedures, ITC section
- **Issue** The ITC experiments are stated to have been performed in triplicate, but no statistical analysis is presented in the text. The errors on the reported KD values are not visible (Table 1 not shown). For a quantitative biophysical study, error analysis is essential.
- **Required correction** Present the mean and standard deviation for all reported KD values. If the errors are in Table 1, ensure the table is included in the main text or supplementary materials.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure references
- **Evidence pointer** Results sections
- **Issue** The text refers to Figure 1A and 1B as showing the crystal structure and solution structure, respectively, but the figure is not visible. The description of the structures in the text is brief and does not allow the reader to understand the key structural features being referenced.
- **Required correction** Provide a more detailed description of the structural features in the text, or ensure the figures are available for review.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Negative controls
- **Evidence pointer** Cell experiments, Figure 5
- **Issue** The cell experiments compare the localization of wild-type and mutant peptides, but no negative control is described (e.g., a peptide with a mutated SxIP motif that should not bind EB1). The GFP control is mentioned but not described in detail.
- **Required correction** Describe the negative controls used in the cell experiments and how they support the specificity of the observed localization.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Accuracy
- **Affected element** Reference to previous work
- **Evidence pointer** Introduction, Discussion
- **Issue** The authors reference Honnappa et al. 2009 for the crystal structure and previous binding studies, but the description of the previous findings is brief. The claim that EGFP dimerization explains the difference in localization between their study and the previous work is presented without direct evidence.
- **Required correction** Provide a more detailed comparison with the previous study and present evidence for the EGFP dimerization claim, or acknowledge it as a hypothesis.

### Technical failings that need to be addressed before the case is established
R1-M1 (two-step model not directly evidenced), R1-M2 (quantitative data not accessible), R1-M3 (functional significance of monomeric affinity unclear). These are the primary technical issues that prevent the manuscript from establishing its central claims.

### Assessment against Nature-style criteria
**Originality**: The "dock-and-lock" model for EB1-SxIP interactions is a novel conceptual contribution. While induced folding upon binding is well-established for IDPs, applying this framework specifically to EB1's EBH domain and dissecting the energetic contributions of different peptide regions is original. The rational affinity enhancement approach is also creative.

**Scientific importance**: The work addresses a fundamental question in microtubule biology: how EB1 achieves selective yet tunable interactions with diverse ligands. The finding that the SxIP motif alone provides specificity but not affinity, and that flanking regions control affinity, has implications for understanding plus-end tracking network assembly. The potential for inhibitor design is interesting but speculative.

**Interdisciplinary readership**: The work bridges structural biology, biophysics, and cell biology. The NMR and ITC approaches will appeal to biophysicists, the structural analysis to structural biologists, and the cell experiments to cell biologists. The broader significance for microtubule biology and disease should attract a wider audience. However, the technical density of the NMR analysis may limit accessibility for non-specialists.

**Technical soundness**: The combination of NMR, ITC, and cell imaging is appropriate and powerful. However, the manuscript as presented does not allow assessment of the technical quality of the data. The absence of visible figures and tables is a significant limitation. The indirect evidence for the two-step model is a concern. The cell experiments are described too briefly to assess their rigor.

**Readability for non-specialists**: The manuscript is generally well-written and the conceptual framework is clearly explained. The "dock-and-lock" model is intuitive. However, the NMR methodology sections are dense and may be challenging for readers without a biophysics background. The discussion of kinetic parameters and model fitting assumes significant expertise.

### Recommendation posture
Supportive if technical concerns are resolved. The conceptual model is interesting and the approach is appropriate, but the manuscript as presented does not provide sufficient evidence to establish the central claims. The authors must present the actual data, provide a more rigorous test of the two-step model, and address the functional significance of the affinity enhancement. If these issues are resolved, the work could make a valuable contribution to the field.