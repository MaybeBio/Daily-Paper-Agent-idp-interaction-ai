## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as stated in the abstract, without access to full methods, figures, or supplementary data
- **Shared manuscript claim summary** The authors report that the receptor binding domain (RBD) of the SARS CoV2 spike protein undergoes liquid-liquid phase separation (LLPS) in vitro, that molecular dynamics simulations identify multiple structurally disordered regions with high flexibility (deviations up to 6 A over 500 ns), that these disordered regions overlap with epitopes, and that this may challenge vaccine-generated antibody binding and vaccine efficacy.
- **Visible evidence base** Abstract text only; no methods, figures, tables, or supplementary materials provided
- **Missing materials affecting confidence** Full methods, experimental protocols, purification and LLPS assay details, simulation parameters and trajectories, epitope mapping data, statistical analyses, and any control experiments

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting observation that the RBD of the SARS CoV2 spike protein can undergo LLPS in vitro, with a proposed link to structural disorder and a speculative implication for vaccine efficacy. However, the evidence as presented is insufficient to establish the central claims. The abstract lacks methodological detail, quantitative results, and controls, and the leap from in vitro LLPS to vaccine efficacy is not supported by the data described. The work may be of interest to the biophysics and structural biology community, but the current form does not meet the evidentiary standard for a high-impact journal.
- **Who would be interested in the results, and why** Researchers studying protein phase separation, particularly in viral proteins, and those interested in the biophysical properties of the SARS CoV2 spike protein. Structural biologists and computational biophysicists may find the simulation data relevant. The potential implication for vaccine efficacy could attract interest from immunologists and vaccine developers, though this connection is speculative at present.
- **Major strengths** The topic is timely and relevant given the ongoing interest in SARS CoV2 biology. The combination of experimental and computational approaches is appropriate for studying LLPS. The identification of disordered regions within the RBD is a plausible and testable hypothesis.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
  - R1-M4
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** Originality: the observation of LLPS in the RBD is novel, though the broader concept of viral protein phase separation is not new. Scientific importance: potentially significant if the link to vaccine efficacy were established, but the current evidence does not support this. Interdisciplinary readership: the topic bridges biophysics, virology, and immunology, which could appeal to a broad audience, but the speculative conclusion weakens this appeal. Technical soundness: cannot be assessed from the abstract alone; the lack of methodological detail and quantitative results is a major limitation. Readability for nonspecialists: the abstract is generally clear, but the leap from in vitro data to vaccine efficacy is not well explained.
- **Recommendation posture** Currently not established from the provided evidence. The authors should provide full experimental and computational details, quantitative results, and controls before the claims can be evaluated.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that the RBD exhibits LLPS in vitro based on expression and purification of the protein.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract states that LLPS formation was demonstrated but provides no details on the experimental conditions, protein concentration, buffer composition, temperature, or the method used to assess LLPS (e.g., turbidity, microscopy, fluorescence recovery after photobleaching). Without these details, it is impossible to verify that the observed phenomenon is bona fide LLPS rather than aggregation or precipitation.
- **Why it matters** LLPS is a specific biophysical phenomenon with distinct characteristics. The distinction between LLPS and nonspecific aggregation is critical, as the biological implications differ substantially. The claim of LLPS is foundational to the entire manuscript.
- **Resolution test** Provide full methods for LLPS assays, including concentration ranges, buffer conditions, and validation with at least two independent techniques (e.g., microscopy and FRAP). Show that the phenomenon is reversible and concentration-dependent.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Computational evidence
- **Claim pointer** The authors claim that molecular dynamics simulations revealed multiple structurally disordered regions with deviations as high as 6 A over 500 ns.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract provides no information on the simulation methodology, including the force field, starting structure, solvation conditions, or the number of replicates. The metric "deviations as high as 6 A" is ambiguous; it is unclear whether this refers to root-mean-square deviation (RMSD) of the whole protein, per-residue fluctuations, or something else. The relevance of this deviation to disorder is not established.
- **Why it matters** The simulation results are used to support the in vitro findings and to link disorder to epitope overlap. Without methodological rigor and clear metrics, the computational evidence is not interpretable.
- **Resolution test** Provide full simulation parameters, define the deviation metric precisely, show per-residue analysis, and include error estimates or replicate runs. Demonstrate that the identified disordered regions are robust across simulation conditions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim overreach
- **Claim pointer** The authors conclude that structural disorderedness of RBD causes LLPS formation in vitro and may potentially challenge COVID-19 vaccine efficacy.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The causal link between disorder and LLPS is asserted but not demonstrated. The abstract does not provide evidence that the disordered regions are necessary or sufficient for LLPS. Furthermore, the extrapolation from in vitro LLPS to vaccine efficacy is highly speculative. No data are presented on antibody binding, neutralization, or any functional immune assay.
- **Why it matters** The title and conclusion imply a potential impact on vaccine efficacy, which is a strong claim with public health implications. Overreach without direct evidence could mislead readers and is not appropriate for a scientific publication.
- **Resolution test** Provide direct experimental evidence linking disorder to LLPS (e.g., mutants with altered disorder). For the vaccine claim, include data on antibody binding in the presence and absence of LLPS conditions, or clearly reframe the conclusion as a hypothesis requiring further study.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The authors state that the RBD was expressed and purified, and that LLPS was demonstrated.
- **Evidence pointer** Abstract only; location not provided
- **Concern** No information is provided on the expression system, purification tags, purity assessment, or protein quality control. The behavior of recombinant proteins can be highly sensitive to these factors, and artifacts from improper folding or contamination could lead to false LLPS observations.
- **Why it matters** Reproducibility is a core requirement for any scientific claim. Without details on protein preparation, other laboratories cannot replicate the findings, and the validity of the results cannot be assessed.
- **Resolution test** Provide full details of expression and purification, including purity analysis (e.g., SDS-PAGE, mass spectrometry) and evidence of proper folding (e.g., circular dichroism, binding to a known antibody).

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Title
- **Evidence pointer** Title
- **Issue** The title states that LLPS "may challenge the vaccine-generated antibody binding," but the abstract does not present any direct evidence of antibody binding being affected. This is an overstatement.
- **Required correction** Revise the title to reflect the speculative nature of the claim, such as "may have implications for vaccine-generated antibody binding" or remove the vaccine reference from the title.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Precision
- **Affected element** Simulation metric
- **Evidence pointer** Abstract
- **Issue** The phrase "deviations as high as 6 A over 500 ns" is imprecise. It is unclear whether this is a maximum, average, or representative value, and for which residues or regions.
- **Required correction** Specify the metric (e.g., C-alpha RMSD, per-residue RMSF) and provide context, such as the baseline deviation for ordered regions.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "Structural disorderedness"
- **Evidence pointer** Abstract
- **Issue** The term "structural disorderedness" is not standard. The field typically uses "intrinsic disorder" or "disordered regions."
- **Required correction** Use standard terminology, such as "intrinsically disordered regions," to align with the literature.

## Risk / unsupported claims
- The claim that LLPS formation is caused by structural disorderedness is unsupported; no causal evidence is presented.
- The claim that LLPS may challenge vaccine efficacy is unsupported; no antibody binding or functional data are provided.
- The claim that disordered regions overlap with epitopes is unverifiable from the abstract; no epitope mapping data are shown.
- The quantitative simulation result (6 A deviation) is uninterpretable without methodological context.
- The overall conclusion that vaccine efficacy may be affected is speculative and not grounded in the presented evidence.