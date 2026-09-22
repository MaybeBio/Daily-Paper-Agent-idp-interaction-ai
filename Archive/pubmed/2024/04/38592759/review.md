## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods) as provided by the user.
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims by the evidence presented in the manuscript. No external validation or replication of results was performed.
- **Shared manuscript claim summary** The authors use coarse-grained (CG) and all-atom (AA) molecular dynamics simulations to argue that differences in charge distribution, particularly in disordered regions, dictate the distinct liquid-liquid phase separation (LLPS) propensities of human HP1 paralogs (HP1α, HP1β, HP1γ). They further claim that DNA modulates phase separation and co-localization of these paralogs, with HP1α acting as a scaffold and HP1β as a client, while HP1γ cooperatively co-phase separates.
- **Visible evidence base** Simulation results presented in Figures 1–6 and associated supplements, including Rg distributions, phase coexistence densities, contact maps, and phase diagrams. Methodological details in Materials and methods.
- **Missing materials affecting confidence** Supplementary files (e.g., Supplementary file 1, 1a, 1b) referenced but not provided. Simulation parameter files, force field parameters, and analysis scripts are only partially available via GitHub. Experimental validation data (e.g., in vitro LLPS assays) are cited but not shown. Specific numerical values for Csat and critical temperatures are not tabulated in the main text.

## Reviewer
- **Overall assessment** This manuscript presents a systematic computational study of HP1 paralog phase separation, leveraging a well-established CG simulation framework. The work addresses a timely and important question in chromatin biology, and the findings are potentially significant for understanding heterochromatin organization. However, the manuscript has several technical and presentational issues that need to be addressed. The evidence for some claims, particularly regarding the role of folded domains and the behavior of heterodimers, is not fully convincing from the data presented. The lack of experimental validation and incomplete methodological details further limit the current impact.
- **Who would be interested in the results, and why** Researchers in the fields of phase separation, chromatin biology, and biophysics of intrinsically disordered proteins. The study provides a molecular-level framework for understanding how sequence-encoded charge properties govern LLPS, which is of broad interest. The specific findings on HP1 paralog co-localization and DNA-mediated regulation are relevant to those studying heterochromatin formation and gene silencing.
- **Major strengths**
  1. The study uses a state-of-the-art CG simulation approach that has been validated in previous work, lending credibility to the methodology.
  2. The systematic comparison of three paralogs with well-characterized sequence differences provides a clear structure for the investigation.
  3. The inclusion of DNA in the simulations adds a relevant biological dimension that is often missing in computational studies of LLPS.
  4. The identification of specific interaction networks (e.g., NTE-hinge, CD-hinge) provides testable predictions for experimentalists.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that "the folded domains, particularly the CD domain, also substantially contribute to the multivalent interactions required for the formation of oligomeric networks and phase separation" based on domain-swapping simulations.
  - **Evidence pointer** Figure 3g–l and Figure 3—figure supplement 1f–k
  - **Concern** The domain-swapping experiments show that replacing the CD of HP1α with that of HP1β or HP1γ enhances phase separation. However, the authors attribute this to the more negative charge and larger SASA of the swapped CD domains. This interpretation is speculative. The enhanced phase separation could also be due to altered interactions with the hinge or other domains that are not directly related to the CD's charge properties. The contact maps (Figure 3l) show increased contacts in the CD and hinge, but the causal relationship is not established. A more rigorous analysis, such as mutating specific charged residues on the CD to test their contribution, would be needed to support this claim.
  - **Why it matters** The claim that the CD domain plays a direct role in LLPS is a novel finding that goes beyond the current understanding of HP1 phase separation, which primarily focuses on disordered regions. If not properly supported, this could mislead future research directions.
  - **Resolution test** Provide additional simulations with point mutations in the CD domain to directly test the role of specific charged residues. Alternatively, perform simulations with a neutralized CD surface to see if the enhanced phase separation is abolished.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors state that "DNA can significantly reshape the stability of a minimal condensate formed by HP1 paralogs due to competitive interactions of HP1α with HP1β and HP1γ versus DNA."
  - **Evidence pointer** Figure 5 and Figure 6
  - **Concern** The simulations with DNA are performed at a single, low mole fraction of DNA (0.01). The authors do not systematically vary the DNA concentration or length to explore the phase behavior. The claim that DNA "reshapes" stability is based on a limited set of conditions. Furthermore, the model treats DNA as a rigid or semi-flexible rod, which may not capture the conformational flexibility of DNA in a condensate. The competitive interactions are inferred from contact maps, but a quantitative analysis of binding affinities or free energies is not provided.
  - **Why it matters** The interaction with DNA is a central aspect of the manuscript's title and a key claim. Without a more thorough investigation, the conclusions about DNA's role in shaping phase separation and localization are not robustly established.
  - **Resolution test** Perform simulations with varying DNA concentrations and lengths. Calculate binding free energies or potentials of mean force between HP1 paralogs and DNA. Compare the results with experimental data on DNA-induced LLPS of HP1α.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Claim pointer** The authors propose a model where "HP1α is central in regulating DNA compaction and initiating protein condensation... HP1γ preferentially enters and cooperatively enhances HP1α condensates... HP1β creates a phase boundary and fine-tunes HP1-DNA phase separation."
  - **Evidence pointer** Figures 5–7
  - **Concern** The proposed model is largely based on simulations of binary and ternary mixtures at specific concentrations. The extrapolation to the complex nuclear environment, where many other factors (e.g., histone modifications, RNA, other proteins) are present, is a significant leap. The authors acknowledge this in the discussion, but the model is presented as a definitive picture in the abstract and conclusion. The biological relevance of the specific concentration ratios used in the simulations is not discussed.
  - **Why it matters** The model has implications for understanding heterochromatin organization, but if it is not clearly framed as a simplified in silico model, it could be over-interpreted by readers.
  - **Resolution test** Clearly state the limitations of the model in the abstract and conclusion. Discuss how the simulation conditions relate to physiological concentrations. Suggest experimental approaches to test the model's predictions.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Abstract
  - **Evidence pointer** Abstract
  - **Issue** The abstract uses technical terms like "charge patterning" and "coarse-grained simulation framework" without sufficient context for a general reader. The significance of the findings for chromatin biology could be stated more clearly.
  - **Required correction** Briefly explain what "charge patterning" means and why it is important. Add a sentence in the abstract that explicitly states the potential implications for understanding heterochromatin function.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Materials and methods
  - **Evidence pointer** Materials and methods, "Coarse-grained MD simulation protocol"
  - **Issue** The description of the CG model is brief. The authors state they use the HPS-Urry model but do not provide specific parameters for the interaction strengths or the mapping of amino acid types to bead types. This makes it difficult to reproduce the simulations.
  - **Required correction** Provide a more detailed description of the model parameters, either in the main text or as a supplementary table. Reference the original model papers more explicitly.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Interdisciplinary readership
  - **Affected element** Discussion
  - **Evidence pointer** Discussion, paragraph 3
  - **Issue** The discussion of the biological implications is somewhat speculative and could benefit from a more balanced view that acknowledges alternative mechanisms for HP1 function, such as specific protein-protein interactions that are not captured by the CG model.
  - **Required correction** Add a sentence or two acknowledging that the model does not account for all possible interactions and that experimental validation is needed.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Figure 2—figure supplement 1
  - **Evidence pointer** Figure 2—figure supplement 1a–h
  - **Issue** The comparison between CG and AA simulations is mentioned, but the details of the AA simulations are not fully described in the main text. It is unclear if the same force field and simulation length were used for all three paralogs.
  - **Required correction** Provide more details on the AA simulation setup, including simulation length, number of replicates, and how the contact maps were calculated and compared.
- **Technical failings that need to be addressed before the case is established**
  - R1-M1: The causal role of the CD domain in enhancing phase separation is not established.
  - R1-M2: The DNA simulations are not sufficiently comprehensive to support the claims about DNA's role.
- **Assessment against Nature-style criteria**
  - **Originality** The work is original in its systematic comparison of HP1 paralogs and its inclusion of DNA in CG simulations of LLPS. However, the general concept of charge-driven phase separation is well-established, and the novelty lies in the specific application to HP1 paralogs.
  - **Scientific importance** The findings are important for the field of chromatin biology and phase separation. The proposed model of differential paralog behavior and DNA-mediated regulation has the potential to influence future research. However, the lack of experimental validation limits the immediate impact.
  - **Interdisciplinary readership** The topic is of interest to biophysicists, cell biologists, and chromatin researchers. The manuscript is written in a way that is accessible to these groups, but some technical details may be challenging for nonspecialists.
  - **Technical soundness** The methodology is generally sound, but there are concerns about the interpretation of domain-swapping experiments and the limited scope of DNA simulations. The lack of detailed parameters for the CG model is a weakness.
  - **Readability for nonspecialists** The manuscript is generally well-written, but the abstract and some sections of the results could be made more accessible. The use of figures is helpful, but some figure captions are not fully self-explanatory.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses a significant question and presents a plausible computational model. However, the concerns about the CD domain's role and the DNA simulations need to be addressed with additional analysis or simulations. The authors should also provide more methodological details to ensure reproducibility.

## Risk / unsupported claims
- The claim that the CD domain "substantially contributes" to LLPS is not fully supported by the data, as the mechanism is not directly tested.
- The claim that DNA "significantly reshapes" phase stability is based on a limited set of simulation conditions and is not quantitatively supported.
- The proposed model of heterochromatin organization (Figure 7) is a speculative extrapolation from simplified in silico systems and should be clearly labeled as such.
- The statement that "HP1β creates a phase boundary" is based on simulation observations but lacks a clear physical or biological definition of "phase boundary" in this context.