## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no access to full manuscript, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors report long-timescale atomistic simulations of multicomponent tripeptide mixtures with all residue substitutions, finding that peptide mixtures form clusters with inverse hydrophobic order, where multivalent and charged residues localize in the core and nonaromatic hydrophobic residues remain on the surface. They attribute this ordering partly to expulsion of nonspecifically bound water following cluster growth and note an increase in specific water-mediated interactions between polar and charged residues during growth.
- **Visible evidence base** Abstract text only; no quantitative data, simulation details, or methodological descriptions provided
- **Missing materials affecting confidence** Full manuscript, simulation parameters, force field details, system composition, trajectory analysis methods, quantitative results, figures, and supplementary information

## Reviewer
- **Overall assessment** The abstract presents an intriguing observation regarding inverse hydrophobic ordering in multicomponent peptide clusters, with a proposed mechanistic role for water expulsion. However, the current evidence base is insufficient to evaluate the robustness of the claims. Key methodological details, quantitative support, and validation of the simulation approach are absent. The conceptual advance is potentially interesting but not yet established from the provided material.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, and membraneless organelles would find the inverse hydrophobic order concept relevant to understanding condensate internal organization. Computational biophysicists interested in water-mediated interactions and atomistic simulations of peptide systems may also be interested. The work could inform experimental studies on peptide-based condensate design.
- **Major strengths** The study addresses a timely question about how multicomponent mixtures organize within condensates. The use of all residue substitutions in tripeptide mixtures is a systematic approach. The proposed mechanism linking water expulsion to hydrophobic ordering is mechanistically plausible and potentially generalizable.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: The inverse hydrophobic order concept is a potentially novel contribution, but its novelty cannot be fully assessed without comparison to prior literature. Scientific importance: The topic is relevant to condensate biology, but the significance for broader cellular processes is not clearly articulated. Interdisciplinary readership: The abstract is accessible to biophysicists and biochemists, but may be less clear to cell biologists without additional context. Technical soundness: Cannot be evaluated from the abstract alone; simulation methodology and validation are absent. Readability for nonspecialists: The abstract is reasonably clear but uses field-specific terminology without sufficient explanation.
- **Recommendation posture** Currently not established from the provided evidence. The claims are interesting but require full manuscript evaluation to determine whether the simulation evidence supports the conclusions.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that "peptide mixtures form clusters with inverse hydrophobic order" and that "most multivalent and charged residues are localized in the cluster's core, with a large fraction of nonaromatic hydrophobic residues remaining on the surface"
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract provides no quantitative definition of "inverse hydrophobic order" or criteria for core versus surface localization. No data on residue distributions, cluster sizes, or statistical significance are presented. The simulation system composition, including the number of peptides, sequence diversity, and concentration, is not described.
- **Why it matters** Without quantitative metrics and system details, the reader cannot assess whether the observed ordering is robust, reproducible, or an artifact of the specific simulation setup. The core claim of the paper depends entirely on this observation.
- **Resolution test** Provide quantitative residue distribution profiles, cluster size distributions, and statistical comparisons across replicate simulations. Define the criteria for core and surface localization and demonstrate that the inverse hydrophobic order is consistent across different system compositions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that "inverse hydrophobic order in peptide clusters is partly driven by the expulsion of nonspecifically bound water molecules following peptide cluster growth"
- **Evidence pointer** Abstract, location not provided
- **Concern** The mechanistic attribution to water expulsion is presented without supporting evidence. No data on water dynamics, hydration shell structure, or free energy contributions are provided. The phrase "partly driven" implies a quantitative decomposition of driving forces that is not shown.
- **Why it matters** The proposed mechanism is central to the paper's conceptual contribution. Without evidence linking water expulsion to the observed ordering, the mechanism remains speculative and could be confounded by other factors such as direct electrostatic interactions or entropic effects.
- **Resolution test** Provide time-resolved water residence times, radial distribution functions of water around different residue types, and free energy calculations or decomposition analyses that quantify the contribution of water expulsion to cluster organization.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that "growth of clusters is also accompanied by the formation of increasing numbers of specific water-mediated interactions between polar and charged residues"
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract does not define what constitutes a "specific water-mediated interaction" or how these are distinguished from nonspecific water contacts. No quantitative data on interaction counts or their evolution during cluster growth are presented.
- **Why it matters** This claim is presented as a key finding, but without a clear operational definition and quantitative support, it cannot be evaluated. The distinction between specific and nonspecific interactions is critical for the interpretation.
- **Resolution test** Provide a clear definition of specific water-mediated interactions, such as hydrogen-bonded water bridges between specific residue pairs, and show quantitative counts of these interactions as a function of cluster size or simulation time.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Abstract terminology
- **Evidence pointer** Abstract, location not provided
- **Issue** The term "inverse hydrophobic order" is introduced without definition or context. Nonspecialist readers may not understand what this means or why it is significant.
- **Required correction** Define the term explicitly, for example by contrasting with the expected hydrophobic core organization in folded proteins, and explain why the observed ordering is unexpected.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Generalizability statement
- **Evidence pointer** Abstract, location not provided
- **Issue** The final statement that findings "should be helpful for future studies on larger peptides and protein condensation" is vague and not supported by specific arguments for why the tripeptide results would transfer to larger systems.
- **Required correction** Provide a brief rationale for generalizability, such as the universality of water-mediated interactions or the residue-level nature of the observed effects, or temper the claim to reflect the speculative nature of extrapolation.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Simulation methodology
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract mentions "long-timescale atomistic simulations" but does not specify the timescale, force field, or system size. This information is essential for assessing the adequacy of sampling.
- **Required correction** Include key simulation parameters in the abstract or refer to a methods section where these details are provided.

## Risk / unsupported claims
- The claim of inverse hydrophobic order in peptide clusters is unsupported without quantitative residue distribution data.
- The mechanistic role of water expulsion in driving cluster organization is unsupported without water dynamics or free energy data.
- The claim of increasing specific water-mediated interactions during cluster growth is unsupported without operational definitions and quantitative counts.
- The generalizability of findings to larger peptides and protein condensation is speculative and not supported by evidence in the abstract.