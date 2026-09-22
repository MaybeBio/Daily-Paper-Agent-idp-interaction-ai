## Review setup
- **Input scope** Full manuscript text (main text, Materials and Methods, figure legends not provided in full)
- **Assessment boundary** Structural biology claims, model building methodology, functional interpretations, and comparison to prior literature as presented in the provided text
- **Shared manuscript claim summary** The authors report four cryo-EM structures of the human MLL1-WRAD complex bound to an H2B-ubiquitinated nucleosome, use cross-linking mass spectrometry to guide modeling of previously unresolved regions (Ash2L IDR, SPRY insertion, DPY30-SDI), and propose that ubiquitin and DPY30/Ash2L position the complex in an active conformation on the nucleosome.
- **Visible evidence base** Main text, Materials and Methods, references to SI Appendix figures and tables, PDB/EMDB accession codes
- **Missing materials affecting confidence** SI Appendix figures and tables (S1–S6, Tables S1–S4), Dataset S1 (cross-links), figure panels referenced but not shown, validation reports, full methods for cryo-EM data processing

## Reviewer
- **Overall assessment** This manuscript presents a technically demanding cryo-EM study of a challenging, dynamic protein complex on a modified nucleosome substrate. The use of cross-linking MS to guide modeling of disordered regions is appropriate and adds value. However, the central functional claim that ubiquitin orients the complex into an active conformation is largely inferential, and the resolution of the MLL1-WRAD portions of the maps (5–9.5 Å) limits the confidence in the detailed structural interpretations. The four states are described as putative assembly intermediates, but the evidence for ordered assembly is correlative. The manuscript is of interest to the chromatin and transcription communities, but the case for the mechanistic conclusions is not fully established from the provided evidence.
- **Who would be interested in the results, and why** Researchers studying histone methylation, particularly H3K4 methyltransferases and their regulation by H2B ubiquitination; structural biologists interested in dynamic multi-subunit complexes on nucleosomes; those studying the WRAD complex and its role in MLL1 activity. The integrative modeling approach combining cross-linking MS with cryo-EM will also interest methodologists.
- **Major strengths** 1) The study addresses a biologically important question: how H2B ubiquitination stimulates MLL1 activity. 2) The use of cross-linking MS to model previously unresolved regions is a rigorous approach. 3) The identification of multiple conformational states adds to the understanding of complex dynamics. 4) The comparison to prior structures and discussion of discrepancies is thoughtful.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (resolution of MLL1-WRAD regions), R1-M2 (functional claim based on limited evidence), R1-M3 (assembly pathway speculation)
- **Assessment against Nature-style criteria** **Originality**: Moderate to high. The structures are new, but the overall architecture has been reported previously (6KIV, 6PWV). The novelty lies in the additional states and modeling of Ash2L regions. **Scientific importance**: High for the chromatin field, as the mechanism of H2B-ubiquitin stimulation of MLL1 is a long-standing question. **Interdisciplinary readership**: Moderate. Primarily of interest to structural biologists and chromatin biochemists; broader interest is limited by the specialized nature of the topic. **Technical soundness**: Generally sound methodology, but the resolution limitations in the regions of interest are a significant concern. **Readability for nonspecialists**: The Significance statement is clear, but the main text assumes substantial background knowledge. The manuscript is written in a style appropriate for a specialist journal.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding the resolution of the MLL1-WRAD regions and the strength of the functional conclusions.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim to have determined four distinct MLL1-WRAD states bound to the nucleosome, with overall resolutions of 3.4–4.7 Å, and to have modeled Ash2L IDR, SPRY insertion, and DPY30-SDI into density at 7–9.5 Å resolution.
- **Evidence pointer** Results, "Structure Determination of Multiple MLL1-WRAD States"; SI Appendix, Figs. S1 and S2
- **Concern** The overall resolutions reported (3.4–4.7 Å) apply to the entire complex, but the MLL1-WRAD regions of interest are resolved to only 5–9.5 Å. At these resolutions, side-chain placement is not justified, and even secondary structure assignment can be ambiguous. The authors acknowledge that side chains are included "solely for model completeness and cross-link validation," but the models are then used to draw functional conclusions about specific residue contacts (e.g., K419/K421 near DNA, K205/K206/K207 helix). The validation of these models relies heavily on cross-links, but cross-links provide distance restraints, not structural information at the level of secondary or tertiary structure. The manuscript does not provide sufficient evidence that the models are reliable at the level of detail claimed.
- **Why it matters** The functional interpretations, particularly the role of Ash2L in DNA contacts and the proposed coupling of DPY30 binding to IDR ordering, depend on the accuracy of these low-resolution models. If the models are incorrect, the functional conclusions are unsupported.
- **Resolution test** Provide local resolution estimates for the MLL1-WRAD regions in each state. Show that the models are justified by the density at the relevant contour levels, or explicitly state that the models are speculative and not validated by the density. Provide cross-validation (e.g., half-map FSC for the modeled regions) and clearly separate what is experimentally determined from what is modeled based on cross-links and homology.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance / claim strength
- **Claim pointer** The authors state that "the presence of ubiquitinated H2B-K120 orients the MLL1-WRAD complex on the nucleosome and that the resulting docking represents the active conformation."
- **Evidence pointer** Discussion, first paragraph; Results, "Role of Ubiquitin and Ash2L/DPY30 in Positioning the MLL1 Complex on Nucleosomes"
- **Concern** The claim that ubiquitin orients the complex into an active conformation is based on a comparison of structures from different studies with different constructs, different nucleosome substrates, and different sample preparation conditions. The authors did not determine a structure of MLL1-WRAD bound to an unmodified nucleosome in the same study, so the comparison is indirect. The twofold stimulation of activity by ubiquitin is modest, and it is not demonstrated that the "active" orientation is the cause of this stimulation. The authors also note that a subset of particles in a prior study adopted the active orientation even without ubiquitin, which weakens the claim that ubiquitin is the primary determinant of orientation.
- **Why it matters** The central functional conclusion of the manuscript rests on this claim. If the orientation difference is due to other factors (e.g., construct differences, sample preparation, or intrinsic dynamics), the conclusion is not supported.
- **Resolution test** Determine a structure of MLL1-WRAD bound to an unmodified nucleosome under identical conditions, or provide direct experimental evidence (e.g., mutagenesis of the ubiquitin-RbBP5 interface) that the ubiquitin contact is responsible for the orientation and that this orientation is required for activity.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance / overinterpretation
- **Claim pointer** The authors speculate that the four states "may represent an apparent progressive assembly of subunits from state 1, which contains RbBP5 and partial density for WDR5, through state 4 (the active state), which contains all five subunits."
- **Evidence pointer** Results, "Four MLL1-WRAD States Represent Putative Assembly Intermediates"; Discussion, final paragraph
- **Concern** The interpretation of the four states as assembly intermediates is speculative. The states could equally represent disassembly products, alternative binding modes, or artifacts of grid preparation (the authors acknowledge the possibility of air-water interface stripping). No time-resolved or biochemical evidence is provided to support an ordered assembly pathway. The hydrodynamic analysis cited (ref. 53) was performed in the absence of nucleosomes and does not directly support the proposed nucleosome-bound assembly order.
- **Why it matters** The title and framing of the manuscript emphasize the multistate nature of the complex. If the states do not represent assembly intermediates, the significance of the finding is reduced to a catalog of binding modes.
- **Resolution test** Provide biochemical evidence for ordered assembly (e.g., subunit titration experiments, kinetic analysis, or mutagenesis that traps specific intermediates). Alternatively, temper the language to describe the states as alternative binding modes without implying a temporal order.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Cross-linking MS methodology
- **Evidence pointer** Materials and Methods, "Cross-Linking MS"
- **Issue** The cross-linking MS was performed on the MLL1-WRAD complex alone, not on the complex bound to the nucleosome. The authors use these cross-links to guide modeling of the nucleosome-bound complex, but the conformation of the free complex may differ from the bound state.
- **Required correction** Acknowledge this limitation explicitly and discuss how the cross-links might be affected by nucleosome binding. If possible, perform cross-linking on the nucleosome-bound complex.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Readability
- **Affected element** Figure callouts
- **Evidence pointer** Results, throughout
- **Issue** The manuscript refers to figures and SI Appendix items extensively, but the figures are not provided in the submitted text. This makes it difficult to evaluate the claims.
- **Required correction** Ensure that all figures and SI Appendix items are included in the submission and that the callouts are accurate.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Model building for state 2
- **Evidence pointer** Materials and Methods, "Model Building and Refinement"
- **Issue** The state 2 model was built by rigid-body fitting of the state 4 components into the state 2 map, followed by real-space refinement. It is unclear whether the Ash2L and MLL1 regions in state 2 were modeled de novo or simply placed from state 4. Given the lower resolution of these regions, this distinction is important.
- **Required correction** Clarify the modeling procedure for state 2 and state the resolution limits for the MLL1-WRAD regions in this state.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion of alternative models
- **Evidence pointer** Results, "Four MLL1-WRAD States Represent Putative Assembly Intermediates"
- **Issue** The authors note that the density at SHL −6 to SHL −7 in state 2 "may correspond to a slight peeling away of the DNA from the histone core, although the density is not sufficiently well resolved to rule out alternative models that place additional protein in this location." This is an important caveat, but it is not discussed further.
- **Required correction** Expand on this alternative interpretation and its implications for the proposed assembly model.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability
- **Affected element** Significance statement
- **Evidence pointer** Significance section
- **Issue** The Significance statement is clear but could be more specific about the mechanistic insight gained from the multistate structures.
- **Required correction** Consider revising to state explicitly what new understanding of MLL1 regulation emerges from the four states.

## Risk / unsupported claims
- The claim that ubiquitin orients MLL1-WRAD into an active conformation is not directly supported by the data presented, as no structure of the complex on an unmodified nucleosome was determined in this study.
- The interpretation of the four states as assembly intermediates is speculative and not supported by biochemical or kinetic evidence.
- The models of Ash2L IDR, SPRY insertion, and DPY30-SDI at 7–9.5 Å resolution are presented with a level of detail (side chains, specific contacts) that is not justified by the resolution.
- The statement that the active orientation "represents the active conformation" is an inference based on comparison to prior structures and activity data, not a direct demonstration.
- The functional importance of specific residues (K419/K421, K205/K206/K207) is inferred from the low-resolution models and prior mutagenesis, but the structural basis for their role is not experimentally validated here.