## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods) as provided
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided text; no supplementary files, figures, or source data were available for direct inspection
- **Shared manuscript claim summary** The authors propose that the intrinsically disordered N-terminal domain of dynein intermediate chain (IC) from Chaetomium thermophilum adopts a compact, autoinhibited conformation through long-range intramolecular contacts between the N-terminal single α-helix (SAH) and the C-terminal region overlapping the LC7 binding site. They further propose that multivalent binding of the three dynein light chains (Tctex, LC8, LC7) relieves this autoinhibition, thereby regulating the differential binding of IC to the non-dynein partners p150Glued and NudE. The authors also report the first recombinant expression and biophysical characterization of full-length IC and its reconstitution with light chains.
- **Visible evidence base** Text descriptions of SV-AUC, SE-AUC, SEC-MALS, CD, ITC, and NMR experiments; figures referenced but not directly viewable; Supplementary file 1 referenced for ITC fitting parameters
- **Missing materials affecting confidence** Figures and figure supplements (referenced extensively but not provided); Supplementary file 1 (ITC data); source data files; specific numerical values for binding affinities beyond those stated in text; NMR assignment details and peak lists

## Reviewer
- **Overall assessment** This manuscript addresses a significant and timely question in dynein biology: how the intrinsically disordered intermediate chain coordinates interactions with multiple regulatory partners. The authors employ an impressive suite of biophysical techniques and introduce a new, longer IC construct (IC1-260) that reveals autoinhibitory behavior not observed in shorter constructs. The central claim that long-range intramolecular contacts between the SAH region and the LC7 binding site mediate autoinhibition, and that light chain multivalency relieves this inhibition, is conceptually novel and mechanistically plausible. However, the evidence presented in the text is largely qualitative, with key quantitative data (binding affinities, NMR peak assignments, ITC fits) relegated to supplementary materials that were not available for review. The distinction between direct competition and allosteric/autoinhibitory mechanisms is not fully resolved. The full-length IC experiments, while a valuable contribution, are limited to AUC and would benefit from orthogonal validation. Overall, the work is potentially important but requires careful scrutiny of the quantitative data and additional experimental support for the proposed mechanism.
- **Who would be interested in the results, and why** Researchers studying dynein regulation, cytoplasmic dynein assembly and cargo recruitment, intrinsically disordered proteins, multivalent protein interactions, and the molecular basis of motor protein regulation. The work is also relevant to those interested in the biophysical characterization of challenging disordered protein systems and the development of methods to study them.
- **Major strengths** (1) The use of a long IC construct (IC1-260) that encompasses the entire N-terminal domain is a significant advance over previous shorter constructs and reveals new regulatory behavior. (2) The combination of multiple orthogonal biophysical techniques (AUC, SEC-MALS, CD, ITC, NMR) provides a comprehensive characterization. (3) The first recombinant expression and characterization of full-length IC is a notable technical achievement. (4) The proposed model of autoinhibition and its relief by light chain multivalency is conceptually interesting and provides a testable framework for future studies. (5) The work addresses a fundamental question about how disordered proteins achieve specificity and regulation in multi-protein assemblies.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The authors claim that "autoinhibition caused by long-range intramolecular interactions between the N-terminal single α-helix of IC, the common site for p150Glued and NudE binding, and residues closer to the end of the N-terminal domain" is responsible for the reduced binding affinity of IC1-260 to p150Glued and NudE.
  - **Evidence pointer** Results section "Interactions using Ct IC1-260"; Figure 5; Figure 6C; Figure 7
  - **Concern** The central claim of autoinhibition relies on the observation that IC1-260 binds more weakly to p150Glued and NudE than shorter constructs, and on NMR data showing peak disappearances. However, the text does not provide quantitative binding affinities for the IC1-260 interactions (only qualitative statements such as "weak endothermic binding" and "no binding"). The NMR data are described qualitatively (peak disappearances) without specific residue assignments or quantitative analysis. The evidence that the SAH region specifically contacts the LC7 binding site is based on titration experiments with IC216-260, but the text does not provide details on which residues are involved or the affinity of this intramolecular interaction. Without quantitative data, it is difficult to assess whether the observed effects are due to a specific autoinhibitory interaction or to non-specific aggregation, conformational heterogeneity, or other factors.
  - **Why it matters** The autoinhibition model is the central conceptual advance of the manuscript. If the quantitative support is insufficient, the mechanistic claim is not established. The distinction between autoinhibition and other possible explanations (e.g., avidity effects, non-specific interactions, or conformational sampling) is critical for the interpretation of the results.
  - **Resolution test** Provide quantitative binding affinities (Kd values) for IC1-260, IC1-88, and IC1-150 interactions with p150CC1B and NudECC from ITC or other methods. Provide specific NMR data showing which residues of the SAH region and the LC7 binding site are involved in the intramolecular interaction, with quantitative analysis of the interaction (e.g., Kd for the intramolecular interaction). Show that the autoinhibitory interaction is specific and saturable, and that disruption of the putative contact sites (e.g., by mutation) relieves autoinhibition.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Experimental support for mechanism
  - **Claim pointer** The authors claim that "multivalency relieves IC autoinhibition" and that light chain binding regulates the interaction of IC with p150Glued and NudE.
  - **Evidence pointer** Results section "Multivalency relieves IC autoinhibition"; Figure 8; Figure 9
  - **Concern** The evidence that light chain binding relieves autoinhibition is based on AUC experiments showing that the IC1-260/light chain complex has a larger sedimentation coefficient when bound to p150CC1B or NudECC. However, the text does not provide quantitative binding data for the ternary complexes. The claim that "binding to IC1-260 is significantly enhanced in the presence of the light chains" is based on a comparison of sedimentation coefficients, which is an indirect measure of binding. The mechanism by which light chain binding relieves autoinhibition is not directly demonstrated. The authors propose that LC7 binding is required to release the SAH region, but the evidence for this is indirect (AUC shifts) and the text does not show direct binding data for LC7 to the full-length IC or the IC1-260 construct.
  - **Why it matters** The claim that multivalency relieves autoinhibition is the second major conceptual advance. If the evidence is only indirect, the mechanism is not established. Understanding how light chain binding relieves autoinhibition is important for the model and for understanding the regulatory logic of the system.
  - **Resolution test** Provide direct binding data (e.g., ITC, MST, or NMR titrations) showing that light chain binding to IC1-260 or ICFL enhances the affinity for p150CC1B and NudECC. Show that the effect is specific to the light chains and not due to non-specific effects. Provide evidence that LC7 binding specifically disrupts the SAH-LC7 site interaction, e.g., by NMR or mutagenesis.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Generalizability and biological relevance
  - **Claim pointer** The authors state that "autoinhibition in IC regulation emphasizes interplay of disorder and multivalency" and imply that this mechanism is relevant to dynein function in vivo.
  - **Evidence pointer** Discussion section
  - **Concern** The experiments are performed entirely in vitro with recombinant proteins. The authors do not provide any evidence that autoinhibition occurs in the context of the full dynein complex or in cells. The relevance of the proposed mechanism to dynein function in vivo is speculative. The authors acknowledge this limitation in the Discussion, but the claim that this is a "testable model" is not supported by any in vivo or cellular data.
  - **Why it matters** The significance of the work depends on the biological relevance of the proposed mechanism. Without any evidence that autoinhibition occurs in the cellular context, the impact of the work is limited.
  - **Resolution test** Provide evidence that the autoinhibitory interaction is conserved in IC from other species, or that mutations that disrupt autoinhibition affect dynein function in cells. Alternatively, provide a clear statement that the in vivo relevance is unknown and requires future investigation.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity of presentation
  - **Affected element** Results section "Ct IC1-260 is stabilized by long-range contacts"
  - **Evidence pointer** Figure 3; Figure 3—figure supplement 1
  - **Issue** The text states that IC1-260 is "stabilized by long-range contacts" based on CD thermal denaturation data, but the specific data (melting temperatures, comparison to shorter constructs) are not described in the text.
  - **Required correction** Provide the melting temperatures and a clear comparison of the thermal stability of IC1-260 versus shorter constructs in the text or in a table.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Data presentation
  - **Affected element** Results section "Identifying disordered domains of Ct IC in the context of IC1-260"
  - **Evidence pointer** Figure 4
  - **Issue** The NMR data are described qualitatively. The text states that "the limited chemical shift dispersion at 10°C" and "appearance of the majority of the peaks in the CLEANEX experiment" indicate disorder, but no quantitative measures (e.g., secondary chemical shifts, order parameters) are provided.
  - **Required correction** Provide quantitative measures of disorder, such as secondary chemical shift analysis or heteronuclear NOE data, to support the conclusion that the observed peaks correspond to disordered regions.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Interpretation of AUC data
  - **Affected element** Results section "Multivalency relieves IC autoinhibition"
  - **Evidence pointer** Figure 8C; Figure 9B
  - **Issue** The interpretation of sedimentation coefficients in terms of binding and conformational changes is complex. The text states that the f/f0 ratio for the NudECC complex is 2.38, indicating an elongated shape, but does not discuss alternative explanations (e.g., conformational heterogeneity, dynamic equilibrium).
  - **Required correction** Discuss alternative interpretations of the AUC data and consider additional experiments (e.g., SEC-MALS of the complexes) to confirm the stoichiometry and shape of the complexes.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Completeness of methods
  - **Affected element** Materials and methods section "Isothermal titration calorimetry"
  - **Evidence pointer** Supplementary file 1
  - **Issue** The ITC data are referenced to Supplementary file 1, but the fitting models and parameters are not described in the text. The text mentions "single-site or a two-site binding model" but does not specify which model was used for which interaction.
  - **Required correction** Provide a summary of the ITC fitting results in the text or a table, including the model used, Kd values, and thermodynamic parameters for each interaction.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Figure quality
  - **Affected element** Figure 1
  - **Evidence pointer** Figure 1
  - **Issue** The model shown in Figure 1B is described as a "simplified model" but the text does not clearly explain the basis for the model or what evidence supports it.
  - **Required correction** Clarify in the figure legend or text that the model is a schematic representation based on the data presented in the manuscript and previous studies.

## Risk / unsupported claims
- The claim that "autoinhibition caused by long-range intramolecular interactions between the N-terminal single α-helix of IC... and residues closer to the end of the N-terminal domain" is not fully supported by quantitative data presented in the text; the NMR and ITC data are described qualitatively.
- The claim that "multivalency relieves IC autoinhibition" is based on indirect AUC measurements; direct binding data for the ternary complexes are not provided in the text.
- The claim that "the addition of LC7 is sufficient to allow binding of p150CC1B and NudECC to ICFL" is based on AUC data and is not supported by direct binding measurements.
- The biological relevance of the proposed autoinhibition mechanism to dynein function in vivo is speculative and not supported by any cellular or in vivo data.
- The statement that "IC1-260 is, to date, the longest IC construct from any species made recombinantly and extensively studied by NMR, ITC, and SV-AUC" is a claim of priority that cannot be verified from the provided text alone.

## Assessment against Nature-style criteria
- **Originality** The concept of autoinhibition in the disordered N-terminal domain of dynein IC, and its relief by multivalent light chain binding, is novel and not previously reported. The use of a long IC construct and full-length IC is a significant advance. The work offers a new perspective on how disordered proteins can achieve regulatory specificity.
- **Scientific importance** The work addresses a fundamental question in dynein biology: how the IC coordinates interactions with multiple regulatory partners. The proposed mechanism has implications for understanding dynein function, cargo selection, and the role of disorder in protein-protein interactions. The findings could be important for the field.
- **Interdisciplinary readership** The work is primarily of interest to biophysicists, biochemists, and cell biologists studying dynein, motor proteins, and intrinsically disordered proteins. The methods used (AUC, ITC, NMR, CD) are standard in biophysics, and the results are presented in a way that is accessible to these communities. The broader cell biology community may find the work interesting, but the in vitro focus and lack of cellular validation may limit its appeal.
- **Technical soundness** The experimental design is generally sound, and the use of multiple orthogonal techniques is a strength. However, the lack of quantitative data in the text for key claims (binding affinities, NMR assignments) is a concern. The interpretation of AUC data in terms of conformational changes is complex and would benefit from additional support. The full-length IC experiments are limited to AUC and would benefit from orthogonal validation.
- **Readability for nonspecialists** The manuscript is generally well-written and the logic is clear. However, the heavy reliance on biophysical terminology and the qualitative description of data may make it challenging for nonspecialists to fully appreciate the significance of the findings. The model in Figure 10 is helpful for conceptual understanding.

## Recommendation posture
Supportive if technical concerns are resolved. The central claims are potentially important and novel, but the evidence presented in the text is not sufficient to fully establish the autoinhibition mechanism and its relief by light chain binding. The authors should provide quantitative data (binding affinities, NMR assignments) and additional experimental support (e.g., mutagenesis, direct binding measurements) to strengthen the case. The work is currently not fully established from the provided evidence, but the conceptual framework is promising and warrants further investigation.