## Review setup
- **Input scope** Full manuscript text (preprint, bioRxiv, 2026)
- **Assessment boundary** Scientific content, methodology, data interpretation, and claims as presented in the provided text. No supplementary figures, tables, or videos were available for direct inspection.
- **Shared manuscript claim summary** The authors present an integrative structural modeling study of HDAC1/2-containing complexes (NuRD, SIN3A, CoREST) using crosslinking mass spectrometry (XL-MS) combined with integrative modeling (IMP), AlphaFold, and HADDOCK docking. They claim to have built structural models of these complexes, modeled the intrinsically disordered C-terminal domain (CTD) of HDAC1 as folding into alpha helices in complex contexts, and constructed a complete model of a NuRD subcomplex containing five subunits and six IDRs.
- **Visible evidence base** Main text, methods summary, figure legends referenced but figures not directly viewable. Supplementary tables and figures referenced but not provided. Data availability statements included.
- **Missing materials affecting confidence** All figures, supplementary tables (S1–S4), supplementary figures (S1–S12), and supplementary videos were not accessible. This significantly limits the ability to assess the quality of the structural models, the XL-MS data, and the validation metrics.

## Reviewer

- **Overall assessment** This manuscript addresses an important and challenging problem: the structural characterization of large, dynamic HDAC1/2-containing complexes with a focus on intrinsically disordered regions. The combination of XL-MS with integrative modeling is appropriate and timely. However, the manuscript as presented has several significant issues that prevent me from endorsing it in its current form. The claims regarding the folding of the HDAC1 CTD into alpha helices are strong and require more rigorous validation than what is described. The lack of accessible figures and supplementary data makes it impossible to verify the quality of the models or the XL-MS data. The novelty of the approach relative to prior work (including the authors' own previous Sin3 study) needs to be more clearly articulated. The manuscript would benefit from a more critical discussion of the limitations of the modeling approach, particularly regarding the use of AlphaFold predictions and the interpretation of crosslinks in disordered regions.

- **Who would be interested in the results, and why** Structural biologists studying chromatin remodeling complexes, researchers interested in intrinsically disordered proteins and their roles in complex assembly, and computational biologists developing integrative modeling approaches. The work also has potential relevance for understanding HDAC inhibitor selectivity and the functional diversity of HDAC1/2 complexes in normal and diseased states.

- **Major strengths**
  1. The study addresses a genuinely difficult and important problem: modeling IDRs within large multi-subunit complexes.
  2. The combination of multiple techniques (XL-MS, IMP, AlphaFold, HADDOCK) is appropriate and reflects current best practices in integrative structural biology.
  3. The use of endogenous complexes from cells (rather than recombinant systems) adds biological relevance.
  4. The authors are transparent about data availability, providing access to raw mass spectrometry data and modeling scripts.
  5. The comparative analysis of HDAC1 behavior in different complex contexts (CoREST vs SIN3A vs NuRD) is a thoughtful approach.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim validity
- **Claim pointer** "We show that the CTD IDR of HDAC1 folds into alpha helices in these complexes."
- **Evidence pointer** Figures 5, 6, S8–S11; location not provided
- **Concern** The central claim that the HDAC1 CTD IDR folds into alpha helices is presented as a definitive finding, but the evidence described in the text is insufficient to support this. The authors state that in the dimeric ISM models, the CTD "showed limited to no contact with the individual protein modeled with it," yet still claim it folds into alpha helices. This is contradictory: if the CTD is not making contacts with the binding partner, what is driving its folding? The authors do not provide any independent validation of this folding (e.g., circular dichroism, NMR, or molecular dynamics simulations). The AlphaFold-only models show the CTD as largely unstructured, and the folding only appears in the XL-MS-guided models. This raises the concern that the folding is an artifact of the modeling constraints rather than a biologically real phenomenon.
- **Why it matters** The folding of a previously unstructured domain into a defined secondary structure upon complex formation is a significant biological claim with implications for understanding IDR function. If this claim is not rigorously supported, it undermines the central contribution of the paper.
- **Resolution test** The authors should provide: (1) a quantitative comparison of the alpha-helical content in the CTD across multiple independent modeling runs, (2) an analysis of the driving forces for CTD folding (e.g., which crosslinks or restraints are responsible), (3) validation using an independent method (e.g., MD simulations, SAXS, or CD spectroscopy on the isolated CTD in the presence of binding partners), and (4) a discussion of whether the folded state is consistent with known IDR folding mechanisms.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "Integrative modeling of the NuRD complex produced effectively a single cluster of models (97% of a total of 28,914 models) with a model precision of 55 Å."
- **Evidence pointer** Figure S3; location not provided
- **Concern** A model precision of 55 Å is extremely low for a complex of this size. This means that the models in the cluster are spread over a very large volume, and the "single cluster" claim is misleading. A precision of 55 Å suggests that the model is not well-defined and that the crosslinks are not providing sufficient constraints to define a unique structure. The authors do not discuss what this low precision means for the biological conclusions they draw. Additionally, the claim that 97% of models fall into a single cluster is not meaningful if the cluster itself is so diffuse.
- **Why it matters** The precision of the model determines the confidence with which biological conclusions can be drawn. A precision of 55 Å means that the relative positions of domains are essentially unknown, and any claims about specific domain-domain interactions or the folding of the CTD are not supported by the model.
- **Resolution test** The authors should: (1) report the precision of individual domains and sub-complexes, not just the overall complex, (2) discuss what structural features are actually well-determined at this precision, (3) compare their precision to other published integrative models of similar complexes, and (4) explain how the low precision affects the interpretation of the CTD folding claim.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "We used an AlphaFold-enabled XL-MS constrained modeling approach to investigate how HDAC1 could assemble into these complexes."
- **Evidence pointer** Methods, Figures 5–6; location not provided
- **Concern** The methodological description of the AlphaFold-enabled approach is insufficiently detailed. The authors state they used AlphaFold3 for initial predictions and then HADDOCK with XL-MS restraints, but critical details are missing: (1) How were the AlphaFold predictions filtered or ranked? (2) What was the confidence of the AlphaFold predictions for the IDR regions? (3) How were the XL-MS restraints converted into HADDOCK ambiguous interaction restraints? (4) What was the success rate of the docking? (5) How many models were generated and how was convergence assessed? Without these details, the approach cannot be reproduced or evaluated.
- **Why it matters** The methodological rigor of the modeling pipeline is central to the validity of the results. If the approach is not fully described, the results cannot be independently verified, and the paper's contribution to the field is diminished.
- **Resolution test** The authors should provide a complete description of the modeling pipeline, including all parameters, filtering criteria, and validation steps. Ideally, this would be in the form of a step-by-step protocol that could be followed by an independent researcher.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** "The approaches used herein are broadly applicable for the study of protein complexes and protein interaction networks that can provide important insights into IDRs."
- **Evidence pointer** Discussion; location not provided
- **Concern** The claim of broad applicability is not well-supported. The approach is applied to three complexes, but the authors do not discuss the limitations of the method or the conditions under which it would or would not be applicable. For example, the approach relies on having a sufficient number of crosslinks, which may not be available for all complexes. The authors also do not compare their approach to other recently published methods for modeling IDRs in complexes.
- **Why it matters** The broader impact of the work depends on its generalizability. If the authors cannot articulate when and how their approach can be applied by others, the impact is limited to the specific complexes studied.
- **Resolution test** The authors should provide a more nuanced discussion of the applicability of their approach, including its limitations and the conditions required for its successful application.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Summary; location not provided
- **Issue** The abstract states "we used HDAC1/2 to isolate their protein interaction networks from cells" which is ambiguous. It should be clarified that HDAC1/2 were used as baits for affinity purification.
- **Required correction** Rephrase to "we used HDAC1/2 as baits to isolate their protein interaction networks from cells."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results section
- **Evidence pointer** "XL-MS Based Protein Interaction Networks of HDAC1 and HDAC2"; location not provided
- **Issue** The authors report 596 non-redundant crosslinks between 359 proteins but do not provide a clear analysis of the false discovery rate for protein-protein interactions. The 1% FDR is mentioned for CSMs, but the protein-level FDR is not discussed.
- **Required correction** Provide a protein-level FDR estimate or discuss why the CSM-level FDR is sufficient.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section
- **Evidence pointer** "Crosslink-guided assembly of HDAC1/2 within the NuRD complex"; location not provided
- **Issue** The description of the NuRD model is dense and difficult to follow. The authors should provide a clearer summary of the key findings before diving into the details of domain localization.
- **Required correction** Add a brief summary paragraph at the beginning of each complex-specific subsection.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods
- **Evidence pointer** "Integrative Protein Complex Prediction via Guided Molecular Docking with HADDOCK"; location not provided
- **Issue** The iterative refinement protocol is described but the convergence criteria are not specified. How did the authors determine that "no further improvement in crosslink satisfaction was observed"?
- **Required correction** Specify the quantitative criteria used to determine convergence.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion
- **Evidence pointer** Discussion; location not provided
- **Issue** The discussion of the functional implications of the CTD folding is brief. The authors should expand on what the alpha-helical structure of the CTD might mean for HDAC1 function and regulation.
- **Required correction** Add a paragraph discussing the potential functional consequences of CTD folding in different complex contexts.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure legends
- **Evidence pointer** Figures 5–7; location not provided
- **Issue** The figure legends are not provided in the text, making it impossible to understand what is shown in each panel.
- **Required correction** Ensure that all figure legends are included and are self-explanatory.

## Risk / unsupported claims
- The claim that the HDAC1 CTD IDR folds into alpha helices in complex contexts is not sufficiently supported by the evidence presented. The authors themselves note that the CTD shows "limited to no contact" with binding partners in dimeric models, yet still claim folding. This is a critical unsupported claim.
- The claim that the NuRD subcomplex model is "complete" is overstated given the 55 Å precision and the fact that only 87% of crosslinks were satisfied.
- The claim of "broad applicability" of the approach is not supported by a critical discussion of limitations.
- The biological significance of the observed differences in HDAC1 CTD flexibility between CoREST and SIN3A complexes is asserted but not experimentally validated.
- The statement that "the presence of IDRs coupled with pre-structured motifs... appear to provide the structural flexibility necessary for conformational selection coupled with an induced fit mechanism" is speculative and not directly tested.
- The claim that the approaches are "broadly applicable" for studying protein complexes and IDRs is not supported by a systematic comparison with other methods or a discussion of failure modes.