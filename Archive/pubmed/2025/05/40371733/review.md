## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, materials and methods, and supplementary figure/table references
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors map sequence motifs and activation domains in an Arabidopsis NAC transcription factor clade, characterize the intrinsically disordered region of ANAC046, and demonstrate that two distant activation domain/motif regions bind six regulator domains promiscuously with a hierarchy of affinities, proposing a rheostatic regulatory mechanism
- **Visible evidence base** NMR spectroscopy (chemical shifts, relaxation, PREs), ITC, SAXS, coarse-grained simulations with Bayesian/maximum entropy reweighting, bioinformatic motif identification, AlphaFold 3 modeling
- **Missing materials affecting confidence** Full figures and supplementary tables (S1–S4, S5–S13) not provided; specific NMR assignment details for bound states not fully described; AlphaFold 3 confidence metrics not reported; raw ITC thermograms not shown; details of the yeast-based AD screen thresholds not fully contextualized

## Reviewer
- **Overall assessment** This manuscript presents a comprehensive biophysical characterization of the intrinsically disordered region of the Arabidopsis transcription factor ANAC046, with a focus on two distant activation domain/motif regions and their interactions with six regulator domains. The work combines multiple complementary techniques and addresses an important question in transcriptional regulation. The central claims regarding promiscuous binding, affinity hierarchy, and lack of coupling between the two sites are supported by the presented data. However, several technical concerns regarding data interpretation, particularly around the ITC analysis of the full-length IDR and the extrapolation to a rheostatic mechanism, require clarification before the conclusions can be fully accepted.

- **Who would be interested in the results, and why** Researchers studying transcriptional regulation, intrinsically disordered proteins, and plant stress/senescence signaling would find this work valuable. The demonstration of hierarchical, promiscuous binding in a long IDR with distant activation domains has implications for understanding how transcription factors integrate multiple regulatory inputs. The methodological combination of NMR, ITC, SAXS, and simulations provides a template for studying similar systems. The proposed rheostatic mechanism could inform studies of other transcription factors with multiple activation domains.

- **Major strengths** The study addresses a timely and important question about the interplay between sequence motifs, activation domains, and regulator binding in IDRs. The use of multiple orthogonal biophysical techniques (NMR, ITC, SAXS, simulations) provides a robust characterization. The identification of a hierarchy in binding affinities between two distant sites is a novel and interesting finding. The inclusion of both positive and negative regulators is biologically relevant. The authors are appropriately cautious in some interpretations, particularly regarding aggregation effects.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Data interpretation and claim support
- **Claim pointer** The authors claim that the two activation domain/motif regions in ANAC046 bind regulators independently and uncoupled, based on ITC data showing similar affinities for the full-length IDR and individual fragments
- **Evidence pointer** Results section "The ANAC046 IDR binds regulators promiscuously at overlapping sites", Table 2, Figures S7–S10
- **Concern** The ITC analysis of the full-length ANAC046 IDR (172–338) with RCD1-RST and HAC1-TAZ1 is described as capturing only the high-affinity site (AD2), with the low-affinity site (AD1) not observed. The authors state that this is consistent with the individual fragment affinities, but the data for the full-length protein with HAC1-TAZ1 shows a Kd of 3.0 ± 0.3 μM for AD2, which is approximately 2-fold weaker than the isolated AD2 fragment (6 ± 2 μM for the 300–338 fragment). This discrepancy is not fully explained. More critically, the inability to observe AD1 binding in the full-length context could be due to technical limitations (aggregation, precipitation) rather than true independence. The claim of "uncoupled" binding requires demonstration that AD1 binding is not affected by AD2 occupancy or vice versa, which is not directly shown. The authors should provide a more rigorous analysis, potentially including competition experiments or binding studies with a construct where one site is mutated, to support the independence claim.
- **Why it matters** The central mechanistic conclusion of the paper, that the two distant ADs function independently to enable rheostatic regulation, rests on this claim. If the sites are actually coupled or if the apparent independence is an artifact of technical limitations, the proposed model would need revision.
- **Resolution test** Provide direct evidence for independent binding, such as: (1) ITC or NMR experiments with a full-length construct where AD1 or AD2 is mutated to abolish binding, showing that the remaining site's affinity is unchanged; (2) competition experiments showing that saturating one site does not affect binding at the other; (3) a more detailed analysis of the full-length ITC data that explicitly models two independent sites and demonstrates that the data are consistent with this model.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of binding affinity measurements
- **Claim pointer** The authors report Kd values for AD1/M1-2 binding to RCD1-RST and HAC1-TAZ1 determined by NMR (148 ± 6 μM and 112 ± 6 μM, respectively)
- **Evidence pointer** Results section "The ANAC046 IDR binds regulators promiscuously at overlapping sites", Table 2, Figures S9 and S10
- **Concern** The NMR-based Kd determination for AD1/M1-2 relies on chemical shift perturbations or intensity changes, but the details of the fitting procedure are not fully described. The authors mention that the binding is in fast to intermediate exchange, which can complicate accurate Kd determination. For weak binders in the 100 μM range, the accuracy of NMR-derived Kd values can be highly dependent on the protein concentration used and the specific residues monitored. The authors should provide more details on the fitting methodology, including which residues were used, how the concentration was calibrated, and whether the Kd values were consistent across multiple residues. Additionally, the authors should address whether the presence of the long IDR and potential aggregation affects the reliability of these measurements.
- **Why it matters** The hierarchy in binding affinities between AD1 and AD2 is a key finding. If the AD1 Kd values are inaccurate, the proposed hierarchy and its functional implications would be compromised.
- **Resolution test** Provide a more detailed description of the NMR titration analysis, including the specific residues used for fitting, the concentration ranges, and a demonstration that the Kd values are consistent across multiple independent residues. If possible, corroborate the NMR-derived Kd with an orthogonal method (e.g., fluorescence anisotropy or MST) for at least one interaction.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of the proposed mechanism
- **Claim pointer** The authors suggest that the rheostatic regulatory mechanism proposed for ANAC046 is "likely mirrored in other transcription factors with distantly located activation domains"
- **Evidence pointer** Discussion section
- **Concern** This generalization is based on a single transcription factor and a limited set of regulator domains. While the authors note that similar mechanisms may exist, the evidence presented does not directly support this extrapolation. The sequence analysis shows that the specific SLiM combinations in ANAC046 are not systematically conserved across the clade, and the functional significance of having two distant ADs with different affinities is not directly tested in a biological context. The authors should either temper this claim or provide additional evidence, such as bioinformatic analysis showing that other transcription factors with distant ADs have similar binding hierarchies, or experimental data from at least one additional transcription factor.
- **Why it matters** The broader significance of the work depends on whether the proposed mechanism is general or specific to ANAC046. Overstating the generality could mislead the field.
- **Resolution test** Either revise the claim to be more cautious, or provide additional evidence supporting the generality, such as bioinformatic predictions or preliminary experimental data from another transcription factor with distant ADs.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Functional relevance of the observed interactions
- **Claim pointer** The authors imply that the observed binding of six regulator domains to the two AD/motif regions has functional significance for ANAC046-mediated transcriptional regulation
- **Evidence pointer** Results section "The ANAC046 IDR binds regulators promiscuously at overlapping sites", Discussion
- **Concern** While the authors demonstrate binding in vitro, no functional assays are presented to show that these interactions affect ANAC046 transcriptional activity in a cellular context. The proposed rheostatic model is entirely based on in vitro binding affinities. The authors do not address whether the differences in Kd values (e.g., 0.12 μM for AD2 vs. 148 μM for AD1 with RCD1-RST) would translate into meaningful differences in regulation at physiologically relevant concentrations. Additionally, the potential role of post-translational modifications, which are known to regulate many transcription factors, is not experimentally explored.
- **Why it matters** The physiological relevance of the proposed mechanism is a key aspect of the paper's significance. Without functional validation, the model remains speculative.
- **Resolution test** Provide at least one functional assay, such as a reporter assay in plant protoplasts or a heterologous system, showing that mutations in AD1 or AD2 that affect regulator binding also affect transcriptional output in a manner consistent with the proposed rheostatic model.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and completeness of methods
- **Affected element** Materials and Methods, ITC section
- **Evidence pointer** Materials and Methods, "Isothermal titration calorimetry"
- **Issue** The ITC methods section does not specify the exact buffer conditions used for each experiment, particularly whether the buffer was identical for the full-length IDR and the fragments. Differences in buffer composition could affect binding affinities and complicate comparisons.
- **Required correction** Provide the exact buffer composition for each ITC experiment and state whether the same buffer was used for all constructs.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 3 and associated text
- **Evidence pointer** Results section "The ANAC046 IDR binds regulators promiscuously at overlapping sites"
- **Issue** The NMR titration data for the full-length IDR with the six regulator domains are presented as intensity ratios, but the specific residues affected are not clearly mapped onto the sequence in the main text. This makes it difficult to assess the extent of the binding sites beyond the two identified hotspots.
- **Required correction** Include a sequence-level mapping of the affected residues in the main figures or supplementary material to better illustrate the binding site boundaries.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical analysis
- **Affected element** ITC and NMR Kd values
- **Evidence pointer** Table 2
- **Issue** The Kd values are reported with standard deviations, but the number of independent replicates is not stated for each measurement. This is important for assessing the reliability of the reported values, especially for the weaker interactions.
- **Required correction** State the number of independent replicates for each Kd measurement in Table 2 or the methods section.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation of simulation results
- **Affected element** Coarse-grained simulations and PRE analysis
- **Evidence pointer** Results section "Intramolecular interactions in the ANAC046 IDR", Figure 4
- **Issue** The authors state that the PRE data are in good agreement with the SAXS-reweighted ensemble, but the quantitative comparison is not shown. It would be helpful to see a direct overlay of the predicted and experimental PRE profiles to assess the quality of the agreement.
- **Required correction** Include a direct comparison plot of predicted versus experimental PRE values in the main text or supplementary material.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction and Discussion
- **Evidence pointer** Introduction, Discussion
- **Issue** The discussion of rheostatic regulation could benefit from more explicit comparison with other models of transcription factor regulation by multiple activation domains, such as the "activation by cooperative recruitment" model or the role of allovalency in other systems.
- **Required correction** Add a brief paragraph in the Discussion placing the proposed rheostatic model in the context of existing models of multi-AD transcription factor regulation.

- **Technical failings that need to be addressed before the case is established** The primary technical concern is the lack of direct evidence for independent, uncoupled binding of the two AD/motif regions in the full-length IDR context. The ITC data for the full-length protein only capture the high-affinity site, and the claim of independence is inferred rather than demonstrated. Additionally, the NMR-based Kd values for the weak AD1 interactions need more rigorous validation. The absence of functional assays linking the observed binding to transcriptional regulation is a significant gap that limits the strength of the proposed mechanism.

- **Assessment against Nature-style criteria** 
  - Originality: The work is original in its comprehensive characterization of a plant transcription factor IDR with two distant ADs and its proposal of a rheostatic regulatory mechanism. The combination of techniques applied to this specific system is novel.
  - Scientific importance: The findings have potential importance for understanding transcription factor regulation, particularly in plants, and for the broader field of IDP function. However, the lack of functional validation limits the immediate impact.
  - Interdisciplinary readership: The work will appeal to biophysicists, structural biologists, and plant molecular biologists. The methods and concepts are accessible to these communities.
  - Technical soundness: The technical quality is generally high, with appropriate use of multiple complementary methods. However, the concerns about binding independence and weak affinity measurements need to be addressed.
  - Readability for nonspecialists: The manuscript is well-written and logically organized. The concepts are explained clearly, though some familiarity with NMR and IDP biophysics is assumed. The abstract and introduction are accessible to a broad scientific audience.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript presents a valuable and comprehensive biophysical characterization of an important plant transcription factor. The proposed rheostatic mechanism is interesting and potentially significant. However, the key claim of independent, uncoupled binding needs stronger experimental support, and the functional relevance of the observed interactions should be demonstrated. If these concerns are adequately addressed, the work would be suitable for publication.