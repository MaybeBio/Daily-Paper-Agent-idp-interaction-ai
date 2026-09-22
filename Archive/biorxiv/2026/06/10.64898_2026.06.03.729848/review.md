## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no figures, methods, or supplementary materials were provided
- **Shared manuscript claim summary** The authors use molecular dynamics simulations to show that the two intrinsically disordered regions flanking the RRM domain of human FUS become stabilized upon binding U1 snRNA, adopt distinct interaction modes with different regions of the stem-loop RNA, and form persistent hydrogen bonds through specific residues, thereby actively contributing to RNA recognition rather than acting as passive linkers
- **Visible evidence base** Abstract text only; no simulation details, structural parameters, interaction analyses, or statistical validations are visible
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, simulation parameters, force field choices, convergence criteria, replica or repeat information, and any experimental validation

## Reviewer
- **Overall assessment** The abstract presents a plausible and potentially interesting computational study on the role of FUS IDRs in RNA recognition. The central claim that IDRs actively participate in RNA binding through distinct mechanisms is biologically relevant. However, the abstract alone provides insufficient detail to evaluate the technical rigor of the simulations, the statistical robustness of the findings, or the biological significance of the observed differences. The conclusions are stated with confidence that exceeds what can be assessed from the provided material.
- **Who would be interested in the results, and why** Researchers studying RNA-binding proteins, particularly those with disordered regions, would find this relevant. The work also speaks to the broader community interested in the molecular mechanisms of neurodegeneration, given FUS involvement in ALS and FTD. Computational biophysicists studying IDR dynamics and RNA recognition may also be interested, though they would require full methodological details to assess novelty and rigor.
- **Major strengths** The abstract addresses a timely and important question about the functional role of IDRs in RNA recognition. The comparative design between Apo and RNA-bound states is appropriate. The observation that the two IDRs use distinct interaction modes is a potentially valuable finding that could advance understanding beyond treating IDRs as generic flexible linkers.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3  
  - R1-M4
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3  
  - R1-m4
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria**  
  Originality: The question of IDR function in RNA recognition is not new, but the specific focus on FUS IDRs and their distinct interaction modes may offer a fresh angle. However, without seeing how this advances beyond prior computational studies of FUS or other IDR-containing RNA-binding proteins, originality cannot be fully assessed.  
  Scientific importance: The topic is important given FUS relevance to neurodegeneration, but the abstract does not establish whether the findings have implications beyond the specific system studied.  
  Interdisciplinary readership: The work could appeal to structural biologists, computational chemists, and neurobiologists, but the abstract is written in a way that assumes familiarity with simulation jargon and RNA structural terminology, which may limit broader accessibility.  
  Technical soundness: Cannot be evaluated from the abstract. No simulation parameters, convergence checks, force field details, or error analyses are provided.  
  Readability for nonspecialists: The abstract is reasonably clear but uses terms such as "3 10 helices" and "correlated movements" without explanation, which may hinder nonspecialist comprehension.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a coherent narrative, but the absence of methodological detail and quantitative results prevents verification of the central claims. A supportive posture would require access to the full manuscript and its supporting data.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors claim that RNA binding stabilizes the IDRs and reduces their conformational flexibility based on comparison of structural parameters and molecular interactions.  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The abstract provides no information about simulation length, number of replicas, force field parameters, water model, ionic conditions, or convergence criteria. Without these details, it is impossible to determine whether the observed stabilization is statistically meaningful or an artifact of insufficient sampling.  
- **Why it matters** Molecular dynamics simulations of IDRs are notoriously sensitive to force field choice and sampling time. Claims about reduced flexibility and stabilization require rigorous convergence analysis and ideally multiple independent simulations to be credible.  
- **Resolution test** Provide full methods including simulation setup, length, replicas, and convergence metrics. Show that the structural parameters reported are stable across the simulation trajectory and reproducible across independent runs.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence strength  
- **Claim pointer** The authors claim that the N-terminal IDR interacts mainly with nucleotides near the terminal regions of the stem-loop snRNA, while the C-terminal IDR preferentially associates with the central double-stranded region through minor groove interactions.  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The abstract states these distinct interaction modes as findings but provides no quantitative data such as contact frequencies, binding free energies, or interaction occupancies. The distinction between "mainly" and "preferentially" is not supported by any visible numbers or statistical tests.  
- **Why it matters** The claim of distinct recognition modes is a central novelty of the work. Without quantitative evidence showing that these differences are significant and reproducible, the claim remains anecdotal.  
- **Resolution test** Provide per-residue contact maps, interaction occupancy percentages, and statistical comparisons between the two IDRs. Show that the observed preferences are consistent across simulation replicates and not driven by a single trajectory event.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors claim that RNA binding causes rearrangement of backbone dihedral angles and limits formation of secondary structures such as alpha-helices and 3 10 helices.  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** No details are given on how secondary structure was assigned, which dihedral angles were analyzed, or what statistical significance was attached to the observed changes. The claim that secondary structure formation is "limited" implies a quantitative comparison between Apo and bound states that is not visible.  
- **Why it matters** Secondary structure propensity in IDRs is a key observable, and changes upon binding could be functionally important. However, without proper assignment methods and error analysis, the claim cannot be evaluated.  
- **Resolution test** Specify the secondary structure assignment algorithm used, report the distribution of dihedral angles in both states, and provide statistical tests showing significant differences.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Biological relevance  
- **Claim pointer** The authors conclude that the flanking disordered regions of FUS actively participate in RNA recognition through distinct interaction mechanisms.  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The abstract does not discuss whether the identified interactions are functionally relevant in a cellular context. No experimental validation, mutational analysis, or comparison with known FUS mutations associated with disease is mentioned.  
- **Why it matters** The claim of active participation implies functional significance. Without any link to biology, such as disease-associated mutations affecting the identified interaction residues, the relevance of the computational findings remains speculative.  
- **Resolution test** Discuss whether any disease-associated FUS mutations map to the identified interaction residues. If possible, include experimental validation such as mutagenesis or binding assays to support the functional role of the identified contacts.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Abstract terminology  
- **Evidence pointer** Abstract text  
- **Issue** The term "3 10 helices" is used without definition or context, which may confuse readers unfamiliar with this secondary structure type.  
- **Required correction** Define the term on first use or replace with a more accessible description such as "310 helices" with a brief explanation.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Simulation details  
- **Evidence pointer** Abstract only  
- **Issue** The abstract does not state the length of the simulations or the number of independent runs, which are essential for interpreting the reliability of the results.  
- **Required correction** Include simulation time and replicate information in the abstract or ensure the full manuscript clearly reports these details.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Precision  
- **Affected element** Claim wording  
- **Evidence pointer** Abstract text  
- **Issue** The phrase "persistent hydrogen bonds" is used without defining what threshold constitutes "persistent."  
- **Required correction** Define the persistence criterion, such as occupancy above a certain percentage of simulation time, in the abstract or methods.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Generalizability  
- **Affected element** Conclusion scope  
- **Evidence pointer** Abstract text  
- **Issue** The abstract concludes that IDRs "actively participate in RNA recognition" but does not discuss whether this is specific to FUS or generalizable to other IDR-containing RNA-binding proteins.  
- **Required correction** Add a sentence in the discussion or conclusion addressing the potential generalizability or system-specific nature of the findings.

## Risk / unsupported claims
- The claim that RNA binding stabilizes the IDRs and reduces conformational flexibility is unsupported without convergence and statistical analysis.
- The claim of distinct interaction modes for the N- and C-terminal IDRs is unsupported without quantitative contact data.
- The claim that secondary structure formation is limited upon binding is unsupported without assignment details and statistical tests.
- The claim that specific residues form persistent hydrogen bonds is unsupported without occupancy thresholds.
- The overall conclusion that IDRs actively participate in RNA recognition is not established from the abstract alone, as no functional or experimental evidence is provided.