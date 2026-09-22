## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no full text, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors report all-atom explicit-solvent replica exchange molecular dynamics simulations of the TDP-43(321-340) peptide monomer and dimer, comparing wild-type and the ALS-linked M337V mutant. They claim that M337V alters residue-specific secondary structure propensities, inhibits helix formation in specific regions, promotes beta-sheet formation, disrupts inter-molecular helix-helix and W334-W334 pi-pi stacking interactions, enhances overall peptide residue-residue interactions, and weakens peptide-water interactions, thereby providing mechanistic insight into impaired phase separation and enhanced fibrillization.
- **Visible evidence base** Abstract text only; no simulation details, convergence metrics, force field parameters, system setup, or quantitative results are visible
- **Missing materials affecting confidence** Full manuscript, all figures and tables, simulation methodology, force field validation, convergence analysis, free energy surfaces, contact maps, and any statistical error analysis

## Reviewer
- **Overall assessment** The abstract presents a plausible and mechanistically motivated computational study addressing a relevant question in ALS research. The central claims are internally consistent and align with prior experimental observations. However, the abstract alone provides insufficient detail to evaluate the technical rigor of the simulations, the statistical significance of the reported differences, or the robustness of the conclusions. The study is potentially valuable, but the case is not fully established from the supplied material.
- **Who would be interested in the results, and why** Researchers in computational biophysics, protein aggregation, and neurodegenerative disease biology would be interested. The work addresses the atomistic basis of a clinically relevant mutation in TDP-43, a protein central to ALS and frontotemporal dementia. Those studying liquid-liquid phase separation and amyloid formation mechanisms would also find the results relevant, as the study connects mutation-induced changes in local conformational ensembles to macroscopic phase behavior.
- **Major strengths** The study addresses a mechanistically important and clinically relevant question. The use of all-atom explicit-solvent replica exchange molecular dynamics is appropriate for exploring conformational ensembles of small peptides. The focus on both monomer and dimer systems allows for a more complete picture of mutation effects. The interpretation linking disrupted pi-pi stacking and helix-helix interactions to impaired LLPS is chemically reasonable and consistent with prior experimental reports.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality is moderate; the approach is not novel, but the specific application to the M337V mutation in the 321-340 region is a reasonable incremental contribution. Scientific importance is potentially high given the clinical relevance of TDP-43 mutations, but the abstract does not demonstrate that the findings extend beyond the specific peptide system. Interdisciplinary readership is plausible, as the topic bridges biophysics, structural biology, and neurobiology. Technical soundness cannot be assessed from the abstract alone; critical simulation details are absent. Readability for nonspecialists is adequate, though some terms such as "pi-pi stacking" and "replica exchange" may require background knowledge.
- **Recommendation posture** Supportive if technical concerns are resolved. The abstract presents a coherent and plausible narrative, but the absence of methodological detail and quantitative evidence prevents full endorsement at this stage.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that M337V mutation "alters the residue regions with high helix/beta-structure propensities" and "inhibits helix formation in the N-terminal Ala-rich region and the C-terminal mutation site region, while facilitating their long beta-sheet formation."
- **Evidence pointer** Abstract only; no figures or tables provided
- **Concern** The abstract reports qualitative changes in secondary structure propensities but provides no quantitative data, such as per-residue propensity values, differences in free energy, or statistical uncertainties. Without these, it is impossible to assess whether the reported differences are significant or within simulation noise.
- **Why it matters** The central mechanistic claim rests on the assertion that M337V shifts secondary structure preferences. If the magnitude of these shifts is small or not statistically robust, the entire interpretation is weakened.
- **Resolution test** Provide per-residue secondary structure propensity plots with error bars or confidence intervals, and report the magnitude of the differences between wild-type and mutant for both monomer and dimer systems.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that M337V "disrupts inter-molecular helix-helix interactions and W334-W334 pi-pi stacking interactions" and "enhances the overall peptide residue-residue interactions and weakens peptide-water interactions."
- **Evidence pointer** Abstract only; no simulation details or interaction analysis provided
- **Concern** No information is provided on how these interactions were quantified, what distance or angle criteria were used for pi-pi stacking, how helix-helix contacts were defined, or whether the differences are statistically significant. Additionally, the simulation length, number of replicas, and convergence criteria are not stated, which is critical for assessing whether the dimer sampling is sufficient to draw conclusions about inter-molecular interactions.
- **Why it matters** The proposed mechanism for LLPS disruption and fibrillization enhancement depends directly on these interaction-level claims. Without evidence of robust sampling and statistically meaningful differences, the mechanistic conclusions are not established.
- **Resolution test** Describe the analysis methods for inter-molecular contacts and pi-pi stacking, report the number of independent samples, and provide statistical tests or confidence intervals for the reported differences.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The authors state they performed "extensive all-atom explicit-solvent replica exchange molecular dynamic simulations."
- **Evidence pointer** Abstract only; no methodology section provided
- **Concern** The abstract does not specify the force field, water model, simulation box size, salt concentration, temperature range, number of replicas, exchange attempt frequency, or total simulation time per replica. These parameters are essential for reproducibility and for assessing whether the sampling is adequate for the claimed conclusions.
- **Why it matters** Replica exchange simulations are sensitive to parameter choices, and inadequate sampling or poor exchange rates can lead to biased ensembles. Without this information, the reliability of the results cannot be evaluated.
- **Resolution test** Provide a complete simulation methodology section, including all relevant parameters, and demonstrate convergence through time-dependent property plots or replica exchange acceptance rates.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract wording
- **Evidence pointer** Abstract, sentence on "minor impact on the average probability of both helix structure and beta-structure"
- **Issue** The phrase "minor impact on the average probability" is ambiguous. It is unclear whether this refers to the average over all residues, over the entire peptide, or over the simulation ensemble, and whether "minor" is a qualitative or quantitative statement.
- **Required correction** Clarify the definition of "average probability" and provide the numerical values or a reference to a figure that quantifies this claim.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Abstract scope
- **Evidence pointer** Abstract, final sentence
- **Issue** The abstract claims to provide "mechanistic insights into the M337V-mutation-induced impairment of phase separation and facilitation of fibril formation," but the simulations are limited to a 20-residue peptide monomer and dimer. The connection to full-length TDP-43 phase behavior is inferential and not directly tested.
- **Required correction** Acknowledge the limitation that the peptide system is a model for the full-length protein and discuss the extent to which the findings are expected to transfer.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract terminology
- **Evidence pointer** Abstract, "W334-W334 pi-pi stacking interactions"
- **Issue** The term "pi-pi stacking" is used without definition. While familiar to specialists, the abstract may be read by a broader audience.
- **Required correction** Add a brief parenthetical explanation, such as "aromatic ring interactions," or define the term on first use.

## Risk / unsupported claims
- The claim that M337V "disrupts inter-molecular helix-helix interactions and W334-W334 pi-pi stacking interactions" is unsupported in the abstract because no quantitative interaction analysis is provided.
- The claim that M337V "enhances the overall peptide residue-residue interactions and weakens peptide-water interactions" is unsupported without data on interaction energies or contact frequencies.
- The claim that the simulations provide "mechanistic insights" into phase separation and fibrillization of the full-length TDP-43 LCD is not directly supported, as the simulations are limited to a short peptide fragment.
- The overall statistical significance of the reported conformational differences between wild-type and mutant is not assessable from the abstract.