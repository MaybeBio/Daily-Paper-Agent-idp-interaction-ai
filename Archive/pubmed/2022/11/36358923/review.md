## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions) as provided.
- **Assessment boundary** Scientific content, methodological soundness, data interpretation, and alignment with stated claims. Editorial or formatting issues are noted only where they affect clarity or reproducibility.
- **Shared manuscript claim summary** The authors report that proline-rich region II (PRR2) of tau is a major binding site for heparin and heparan sulfate (HS), with higher affinity than the previously characterized R2 repeat domain. This is supported by NMR chemical shift perturbation (CSP) mapping on full-length tau and isolated constructs (PRR2* and R2*), with binding affinities derived from residue-based fitting.
- **Visible evidence base** Abstract; Introduction; Materials and Methods (Sections 2.1–2.5); Results (Sections 3.1–3.5); Discussion; Conclusions. Figures are referenced but not provided in the supplied text.
- **Missing materials affecting confidence** Figures 1–5 (including NMR spectra, CSP plots, and titration curves) are cited but not included. Raw NMR data, assignment tables, and detailed fitting statistics are not provided. Experimental details for heparin 7-mer synthesis are referenced to prior work but not described. No information on replicate measurements or error analysis is given.

## Reviewer
- **Overall assessment** The manuscript addresses a relevant question in tau biology, namely the molecular determinants of tau–glycan interactions that mediate prion-like spreading in Alzheimer's disease. The use of NMR to map binding sites on full-length tau and isolated domains is appropriate, and the identification of PRR2 as a high-affinity binding region is potentially significant. However, the evidence as presented is incomplete. The key quantitative claims (binding affinities, relative importance of PRR2 vs R2) rest on data that are not fully visible, and several methodological details are missing. The conclusion that PRR2 is "crucial" or "more important" than R2 is not fully supported by the data shown in the text, particularly given the aggregation issues with heparin titrations and the indirect nature of the affinity comparison. The manuscript is technically sound in its overall approach but requires substantial additional evidence and clarification before the claims can be considered established.
- **Who would be interested in the results, and why** Researchers studying tau pathology, particularly those focused on the molecular mechanisms of tau uptake, spreading, and aggregation in Alzheimer's disease and other tauopathies. The work also has relevance for investigators working on glycosaminoglycan–protein interactions and on the development of therapeutic strategies targeting the tau–HS interface. The NMR methodology and construct design may interest structural biologists studying intrinsically disordered proteins.
- **Major strengths** The study addresses a gap in the field by quantitatively comparing binding affinities of individual tau domains to a glycan ligand. The use of full-length tau in addition to truncated constructs is a strength, as it acknowledges the limitations of domain-only studies. The NMR-based approach is appropriate for intrinsically disordered proteins and provides residue-level resolution. The identification of PRR2 as a binding site with higher affinity than R2, if confirmed, would be a novel and important finding.
- **Major Concerns** 
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The authors claim that PRR2 is a "crucial domain" for tau–heparin and tau–HS interaction, with higher binding affinity than R2 (abstract, Section 3.4, Section 4).
  - **Evidence pointer** Section 3.4, Figure 4 (not provided), Section 4
  - **Concern** The quantitative comparison between PRR2* and R2* affinities is based on residue-based CSP fitting, but the actual data (CSP plots, fitted curves, KD values with errors) are not shown in the provided text. The reported KD ranges (0.37–0.67 mM for PRR2* vs 1.90–5.12 mM for R2*) are presented without statistical analysis or error estimates. Furthermore, the claim that PRR2 is "more important" than R2 is an interpretation that goes beyond the affinity data, as the functional relevance of these affinities in the context of full-length tau or cellular uptake is not demonstrated.
  - **Why it matters** The central conclusion of the manuscript rests on this affinity comparison. Without visible data and statistical support, the claim is not verifiable. The interpretation of "importance" requires functional validation, not just binding affinity.
  - **Resolution test** Provide the full CSP titration data, fitted curves, and KD values with confidence intervals for all residues in both constructs. Include a statistical comparison (e.g., t-test or ANOVA) between PRR2* and R2* affinities. If possible, perform a competitive binding experiment or a functional assay (e.g., cellular uptake) to directly compare the roles of PRR2 and R2.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Methodological completeness
  - **Claim pointer** The authors state that NMR titrations of PRR2* and R2* with heparin led to aggregation, precluding quantitative analysis (Section 3.5).
  - **Evidence pointer** Section 3.5, Figure 5 (not provided)
  - **Concern** The aggregation issue is mentioned but not characterized. The authors conclude that aggregation implies "much higher binding affinity" to heparin than to Arixtra, but this is speculative. No data on the extent of aggregation, the conditions under which it occurred, or attempts to mitigate it (e.g., lower concentrations, different buffer) are provided. The lack of quantitative heparin data weakens the claim that PRR2 is important for heparin binding, as the only quantitative data are with Arixtra, a smaller and less sulfated ligand.
  - **Why it matters** The manuscript's title and conclusions emphasize tau–glycan interaction, with heparin as a key model. If quantitative heparin data cannot be obtained, the relevance of the Arixtra findings to heparin/HS binding must be justified more carefully. The aggregation observation alone is insufficient to support the affinity claim.
  - **Resolution test** Provide details on the aggregation experiments, including conditions, observed changes in NMR signal, and any attempts to obtain quantitative data (e.g., using lower heparin concentrations, different salt conditions, or alternative ligands). If quantitative heparin data are not feasible, clearly state this limitation and temper the conclusions accordingly.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Interpretive overreach
  - **Claim pointer** The authors speculate that PRR2 binding to glycan is driven by electrostatic interactions and that proline isomerization may impact tau–glycan interaction (Section 4).
  - **Evidence pointer** Section 4
  - **Concern** The electrostatic argument is based on charge counts (11 positive vs 2 negative residues in PRR2*), but no direct evidence (e.g., salt-dependent binding, mutation studies) is provided. The proline isomerization speculation is not supported by any experimental data in this manuscript.
  - **Why it matters** These speculations are presented in the Discussion as plausible mechanisms, but they are not tested. While speculation is acceptable in a Discussion, the authors should clearly distinguish between supported findings and hypotheses. The electrostatic claim, in particular, is used to support the "importance" of PRR2, so it should be backed by at least preliminary evidence.
  - **Resolution test** Either provide experimental evidence (e.g., binding assays at different salt concentrations, mutations of charged residues) or clearly label these as untested hypotheses that require future work.
- **Minor Comments** 
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Section 2.2, CSP equation
  - **Evidence pointer** Section 2.2
  - **Issue** The CSP equation is written as "CSP=100×ΔH2+ΔN2" which is ambiguous. It should be clear whether the square root is taken and what the factor of 100 represents.
  - **Required correction** Rewrite the equation explicitly, e.g., CSP = 100 × sqrt(ΔH² + ΔN²), and define the units.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Section 2.3, construct design
  - **Evidence pointer** Section 2.3
  - **Issue** The description of the PRR2* and R2* constructs is brief. The choice of boundaries (G207-K257 for PRR2*, G261-S304 for R2*) is not justified, and it is unclear whether these boundaries correspond to defined structural or functional domains.
  - **Required correction** Provide a rationale for the chosen boundaries, referencing the full-length tau sequence and any prior structural or functional data.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Data presentation
  - **Affected element** Section 3.1, Figure 1
  - **Evidence pointer** Section 3.1, Figure 1 (not provided)
  - **Issue** The text states that PRR2 residues T212-K254 exhibited "comparable CSPs" to R2, but the actual CSP values or a quantitative comparison are not given.
  - **Required correction** Provide a quantitative summary of CSP values for key residues in both regions, or include a supplementary table.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** Section 3.3, "Arixtra"
  - **Evidence pointer** Section 3.3
  - **Issue** The term "pentasaccharride" is misspelled (should be "pentasaccharide").
  - **Required correction** Correct the spelling.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Section 4, Discussion
  - **Evidence pointer** Section 4
  - **Issue** The Discussion mentions that full-length tau binds heparin with a 10 nM KD, but this value is not referenced or contextualized. It is unclear whether this is from the authors' own data or from prior literature.
  - **Required correction** Provide a citation for this value or clarify its source.

## Technical failings that need to be addressed before the case is established
- R1-M1: The central affinity comparison between PRR2* and R2* is not supported by visible data or statistical analysis.
- R1-M2: The aggregation data with heparin are not characterized, and the conclusion of higher affinity is speculative.
- R1-M3: The electrostatic mechanism is asserted without direct evidence.

## Risk / unsupported claims
- The claim that PRR2 is "more important" than R2 for tau–glycan interaction is not supported by the data as presented, as it relies on an indirect comparison of affinities with a small ligand (Arixtra) and lacks functional validation.
- The statement that aggregation with heparin implies "much higher binding affinity" is speculative and not quantitatively supported.
- The electrostatic binding mechanism is plausible but untested.
- The speculation on proline isomerization affecting tau–glycan interaction is not supported by any data in this manuscript.

## Assessment against Nature-style criteria
- **Originality** Moderate. The identification of PRR2 as a high-affinity binding site for heparin/HS is a novel contribution, as prior work focused on the repeat domains. However, the concept that multiple tau regions bind glycosaminoglycans is not entirely new.
- **Scientific importance** Potentially high, given the role of tau–HS interactions in disease propagation. If confirmed, the finding could inform therapeutic strategies targeting the tau–HS interface. However, the lack of functional data limits the immediate impact.
- **Interdisciplinary readership** The work will appeal to structural biologists, biochemists, and neuroscientists. The NMR methodology is standard, and the topic is of broad interest in the neurodegeneration field.
- **Technical soundness** The overall approach is sound, but the manuscript is incomplete in its current form. Key data are missing, and the quantitative claims are not fully supported. The aggregation issue with heparin is a significant limitation that is not adequately addressed.
- **Readability for nonspecialists** The manuscript is generally well-written and accessible, but the Methods section assumes familiarity with NMR techniques. The Discussion could be clearer in distinguishing supported findings from speculation.

## Recommendation posture
Currently not established from the provided evidence. The manuscript addresses an important question and the approach is appropriate, but the central quantitative claims are not verifiable from the supplied material. The authors should provide the missing data (CSP plots, fitted curves, statistical analysis) and address the aggregation issue with heparin. If these concerns are resolved, the manuscript could be considered for publication in a specialized journal, though it may not meet the broad-impact threshold for Nature.