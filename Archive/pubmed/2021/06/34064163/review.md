## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, technical soundness, and clarity of the review article as provided
- **Shared manuscript claim summary** The manuscript argues that molecular flexibility of the SARS-CoV-2 nucleocapsid protein (NCoV2) is central to its functions in drug binding, RNA binding, and liquid-liquid phase separation (LLPS), and proposes neutron scattering as a promising method to characterize structure and dynamics of NCoV2 within droplets.
- **Visible evidence base** Full text including sections on NCoV2 structure, drug binding simulations, LLPS, and a perspective on neutron scattering methods. Figures and tables are referenced but not provided.
- **Missing materials affecting confidence** Figures 1-7 and Table 1 are cited but not included. Primary data from cited simulation and experimental studies are not available for independent verification. No supplementary information was provided.

## Reviewer
- **Overall assessment** This is a well-organized and readable review that synthesizes recent findings on NCoV2 structure, dynamics, and phase separation behavior. The author makes a reasonable case for the importance of molecular flexibility in NCoV2 function and offers a thoughtful perspective on neutron scattering as a future tool. However, the manuscript is largely descriptive and relies heavily on a small number of primary studies. The novelty is limited, and several claims are presented without sufficient critical evaluation. The proposed neutron scattering strategy, while plausible, is speculative and lacks feasibility analysis. The manuscript would benefit from a more balanced treatment of alternative methods and a clearer articulation of what is established versus what is hypothesized.

- **Who would be interested in the results, and why** Structural biologists, biophysicists, and virologists studying coronavirus nucleocapsid proteins, particularly those interested in intrinsically disordered regions, protein-RNA interactions, and phase separation. Researchers involved in antiviral drug development targeting NCoV2 may also find the drug binding sections relevant. The neutron scattering perspective could interest specialists in biophysical methods, though its audience is narrower.

- **Major strengths** The manuscript provides a clear and concise summary of NCoV2 domain architecture and known structural features. The discussion of drug binding simulations is useful and highlights the role of flexibility in a practical context. The LLPS section is timely and integrates recent experimental findings well. The proposal to use neutron scattering is creative and could inspire methodological innovation. The writing is accessible and logically structured.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript states that "the degree of flexibility in the disordered region has a large effect on drug binding rate" and that this "suggests the importance of molecular flexibility for the NCoV2 function."
- **Evidence pointer** Section 2, reference [51]
- **Concern** This claim is based on a single two-dimensional random walk simulation study. The model approximates NCoV2 as two circles connected by a flexible linker, which is a substantial simplification of the actual protein. The relevance of this model to real drug binding kinetics is not critically assessed. The manuscript does not discuss limitations of the simulation, such as the absence of electrostatic interactions, solvent effects, or the actual three-dimensional structure of the linker. The claim that flexibility "has a large effect" is presented as a general finding, but it is derived from a highly idealized system.
- **Why it matters** The central thesis of the manuscript is that molecular flexibility is critical for NCoV2 function. If the key supporting evidence is from a simplified simulation that has not been validated against experimental data, the overall argument is weakened. Readers may overinterpret the significance of this finding without appropriate caveats.
- **Resolution test** The author should either provide additional experimental or computational evidence supporting the role of linker flexibility in drug binding, or explicitly acknowledge the limitations of the simulation and temper the strength of the claim. A discussion of how the simulation predictions could be tested experimentally would strengthen the case.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript proposes that neutron scattering, specifically small-angle neutron scattering (SANS) and incoherent neutron scattering (iNS), can be used to characterize the structure and dynamics of NCoV2 within LLPS droplets.
- **Evidence pointer** Section 4, Figures 6 and 7
- **Concern** The proposed experimental strategy is described in considerable detail, but no feasibility analysis is provided. Key practical issues are not addressed, including the need for large quantities of deuterated proteins and RNA, the stability of droplets during neutron scattering measurements, the potential for radiation damage, and the difficulty of interpreting scattering data from a multi-component, dynamic system. The manuscript also does not discuss whether the time and length scales accessible by neutron scattering are appropriate for the questions being asked. The claim that iNS can provide information on "the mode of molecular and atomic motions unique to NCoV2 in droplets" is speculative and not supported by any preliminary data or proof-of-concept experiments.
- **Why it matters** The perspective section is presented as a promising direction for future research. If the proposed methods are not practically feasible or are unlikely to yield interpretable results, the manuscript's forward-looking contribution is significantly diminished. Readers may be misled into pursuing an approach that is not well-founded.
- **Resolution test** The author should include a critical assessment of the practical challenges and limitations of the proposed neutron scattering experiments. This could include a discussion of sample requirements, measurement times, data analysis challenges, and comparison with alternative methods such as cryo-electron microscopy or solid-state NMR. A more balanced perspective would strengthen the manuscript.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The manuscript states that "the recent findings that NCoV2, RNA, other viral proteins and a stress granule protein are concentrated into a different phase from its surroundings suggest that the NCoV2 droplet formed through LLPS is the main arena where molecular events critical for the virus replication take place."
- **Evidence pointer** Section 3, references [64-70]
- **Concern** The claim that LLPS droplets are "the main arena" for viral replication is an overstatement. While the cited studies demonstrate that NCoV2 can form droplets and that these droplets contain viral components, the functional significance of these droplets in the viral life cycle is not fully established. The manuscript does not critically evaluate whether LLPS is essential for replication or whether it is a consequence of high local concentrations of viral components. Alternative models, such as replication occurring on membranes or in other subcellular compartments, are not discussed.
- **Why it matters** The manuscript's emphasis on LLPS as central to viral replication may overstate the current evidence. A more nuanced discussion would acknowledge the uncertainty in the field and avoid leading readers to an unjustified conclusion.
- **Resolution test** The author should revise the language to reflect the current state of evidence, for example by stating that LLPS "may play an important role" rather than "is the main arena." A discussion of alternative models and open questions would improve the scientific balance of the manuscript.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 1, description of NCoV2 domain architecture
- **Evidence pointer** Section 1, Figure 1
- **Issue** The description of the N-terminal domain (NTD) and C-terminal domain (CTD) boundaries is somewhat unclear. The text states that NTD spans residues 49-174 and CTD spans 247-364, but the disordered regions between and flanking these domains are not precisely defined. The reader is left uncertain about the exact boundaries of the linker region.
- **Required correction** Provide a clear statement of the residue ranges for all regions, including the N-tail, NTD, linker (with SR-R and LQ-R subregions), CTD, and C-tail. A table or a more detailed figure legend would help.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 2, drug binding studies
- **Evidence pointer** Section 2, references [31-37]
- **Issue** The manuscript summarizes several drug binding studies but does not provide a comparative table of the compounds, their binding affinities, and their target sites. This makes it difficult for the reader to compare the results across studies.
- **Required correction** Consider adding a summary table listing the compounds, their binding energies, target domains, and whether they overlap with RNA binding sites. This would improve the accessibility of the information.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical accuracy
- **Affected element** Section 4, description of neutron scattering
- **Evidence pointer** Section 4, Table 1 and Figure 6
- **Issue** The description of coherent and incoherent scattering cross-sections is simplified and may be misleading. The text states that "the scattering cross-section of hydrogen atoms is much larger than any other atom and deuterium," which is true for incoherent scattering but not for coherent scattering. The distinction is not clearly made.
- **Required correction** Clarify that the large hydrogen cross-section applies specifically to incoherent scattering, and explain why this property is advantageous for iNS but not for SANS.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section 3, LLPS discussion
- **Evidence pointer** Section 3, references [65-70]
- **Issue** The discussion of LLPS conditions is dense and could benefit from a summary of the key experimental conditions (e.g., protein concentration, RNA length, salt concentration, pH) under which droplets form. The current text mentions these parameters but does not synthesize them into a coherent picture.
- **Required correction** Consider adding a brief summary paragraph or table that consolidates the conditions under which NCoV2 LLPS has been observed, highlighting any discrepancies between studies.

- **Technical failings that need to be addressed before the case is established** The manuscript's central argument that molecular flexibility is critical for NCoV2 function relies heavily on a single simplified simulation study (R1-M1). The proposed neutron scattering strategy (R1-M2) is presented without feasibility analysis. The overstatement of LLPS significance (R1-M3) also needs revision. These issues must be addressed before the manuscript's claims can be considered well-supported.

- **Assessment against Nature-style criteria** Originality: The manuscript offers a perspective that is not entirely novel, as the importance of protein flexibility and LLPS in viral systems has been discussed elsewhere. The specific focus on neutron scattering for NCoV2 droplets is somewhat original but not groundbreaking. Scientific importance: The topic is relevant and timely, but the manuscript does not provide new data or a sufficiently critical synthesis to elevate its importance. Interdisciplinary readership: The manuscript bridges virology, biophysics, and structural biology, which could appeal to a broad audience, but the technical detail in Section 4 may limit accessibility. Technical soundness: The descriptions of existing studies are generally accurate, but the uncritical acceptance of simulation results and the lack of feasibility analysis for the proposed methods are weaknesses. Readability for nonspecialists: The manuscript is generally well-written and accessible, though some sections assume familiarity with biophysical methods. Overall, the manuscript does not meet the bar for a Nature-style publication in its current form, as it lacks the depth, critical analysis, and novelty expected.

## Risk / unsupported claims
- The claim that linker flexibility has a "large effect" on drug binding rate is based on a single idealized simulation and is not supported by experimental validation.
- The statement that LLPS droplets are "the main arena" for viral replication overstates the current evidence.
- The proposed neutron scattering strategy is speculative and not supported by feasibility analysis or preliminary data.
- The claim that "the unique mode of protein motions inside the droplets would be the determinants of interactions between other molecules inside the droplets" is speculative and not directly supported by cited studies.
- The assertion that "all this information would eventually be beneficial" for drug development and other applications is presented without a clear pathway or evidence.