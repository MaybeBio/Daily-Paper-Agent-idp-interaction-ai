## Review setup

- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no full text, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors used molecular dynamics simulations to compare wild-type rhodopsin with clinically relevant P347 mutants in the C-terminal VAPA-COOH motif. They report that conformational fluctuations of the intrinsically disordered C-terminal tail do not affect the transmembrane domain or retinal binding, that the WT motif adopts a unique conformation absent in mutants, and that this structural feature better explains pathogenicity than physicochemical or steric determinants. They also propose that membrane-free C-terminal deca-peptides serve as useful small-size model systems.
- **Visible evidence base** Abstract text only; no methodological details, simulation parameters, statistical analyses, or figures were available
- **Missing materials affecting confidence** Full manuscript, methods section, simulation protocols, force field parameters, convergence criteria, structural figures, quantitative comparisons, and any experimental validation data

## Reviewer

- **Overall assessment** The abstract presents a potentially interesting computational study addressing a clinically relevant question in rhodopsin biology. The central claim that WT VAPA-COOH adopts a unique conformation absent in P347 mutants is intriguing but cannot be evaluated without quantitative structural data or methodological detail. The proposal of deca-peptide model systems is pragmatic, but the evidence supporting their equivalence to full-length systems is not visible. The study's value depends heavily on simulation quality and statistical rigor, none of which can be assessed from the abstract alone.
- **Who would be interested in the results, and why** Researchers studying rhodopsin structure and function, investigators focused on retinitis pigmentosa pathogenesis, computational biologists interested in intrinsically disordered protein regions, and drug developers targeting rhodopsin C-terminal interactions. The proposed small-size model system could also interest method developers in the molecular simulation community.
- **Major strengths** The study addresses a clinically relevant gap in understanding P347 rhodopsin mutations. The comparison between full-length and deca-peptide systems is a practical approach that could enable higher-throughput computational screening. The claim that structural features outperform physicochemical determinants as pathogenicity predictors is a testable hypothesis with potential translational relevance.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that conformational fluctuations of the C-terminal tail do not affect the overall structure of the transmembrane domain, including retinal binding.
  - **Evidence pointer** Abstract, location not provided
  - **Concern** The abstract provides no quantitative metrics for structural stability, no RMSD or RMSF values, no distance measurements between the C-terminal tail and the transmembrane domain, and no assessment of retinal binding stability over simulation time. The claim of no effect on the transmembrane domain is presented as a binary outcome without supporting statistics.
  - **Why it matters** This claim underpins the interpretation that the C-terminal tail acts independently of the transmembrane domain. Without quantitative evidence, the reader cannot distinguish between a genuine lack of coupling and insufficient sampling or inadequate analysis.
  - **Resolution test** Provide RMSD time series for the transmembrane domain, distance distributions between the C-terminal tail and the retinal binding pocket, and statistical comparisons between WT and mutant systems across replicate simulations.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that the WT VAPA-COOH motif adopts a unique conformation not found in pathological mutants, and that structural features better explain pathogenicity than physicochemical or steric determinants.
  - **Evidence pointer** Abstract, location not provided
  - **Concern** No structural ensemble data, clustering results, or conformational populations are presented. The term "unique conformation" is undefined. The comparison against physicochemical and steric determinants is asserted without showing any quantitative analysis of these alternative hypotheses.
  - **Why it matters** This is the central scientific claim of the study. Without a clear definition of what constitutes a unique conformation, how populations were compared, and how alternative explanations were ruled out, the claim remains unsupported.
  - **Resolution test** Show conformational clustering analysis with population percentages, define the structural criteria for uniqueness, and provide quantitative comparisons of physicochemical and steric features between WT and mutants with statistical significance tests.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that membrane-free C-terminal deca-peptides are useful and small-size model systems for further investigations.
  - **Evidence pointer** Abstract, location not provided
  - **Concern** The abstract states that results were confirmed by MD simulations in both full-length and deca-peptide systems, but no comparison metrics are provided. The equivalence of conformational behavior between a free peptide and a membrane-anchored C-terminal tail is not trivial and requires demonstration.
  - **Why it matters** The proposed model system is a key practical contribution. If the deca-peptide does not faithfully reproduce the conformational features of the full-length C-terminal tail, its utility for future studies is compromised.
  - **Resolution test** Provide quantitative comparison of conformational ensembles, secondary structure propensities, and key interaction patterns between the deca-peptide and the full-length C-terminal tail in the membrane context.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Abstract background
  - **Evidence pointer** Abstract, location not provided
  - **Issue** The abstract assumes familiarity with rhodopsin trafficking and the VAPA-COOH motif without briefly explaining their functional significance in accessible terms.
  - **Required correction** Add one sentence clarifying the role of the VAPA-COOH motif in rhodopsin trafficking and why its disruption leads to aggressive RP forms.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Scientific importance
  - **Affected element** Abstract conclusion
  - **Evidence pointer** Abstract, location not provided
  - **Issue** The statement that structural details "might facilitate the understanding" and "will be instrumental" is vague and does not specify how the findings could inform therapeutic strategies.
  - **Required correction** Specify the potential therapeutic implications, such as targeting the unique WT conformation or designing stabilizers of the native C-terminal structure.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Simulation methodology
  - **Evidence pointer** Abstract, location not provided
  - **Issue** The abstract does not mention simulation length, number of replicates, or force field used, which are essential for evaluating the reliability of MD results.
  - **Required correction** Include simulation time, replicate count, and force field in the abstract or methods summary.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3. The abstract lacks quantitative structural evidence, statistical comparisons, and validation of the model system equivalence. Without these, the central claims cannot be verified.
- **Assessment against Nature-style criteria** Originality is moderate; the application of MD to P347 rhodopsin mutants is a reasonable extension of existing work rather than a conceptual breakthrough. Scientific importance is relevant to the RP field but the abstract does not demonstrate a major advance. Interdisciplinary readership is limited to computational biophysics and vision research specialists. Technical soundness cannot be assessed from the abstract alone and is the primary concern. Readability for nonspecialists is acceptable but could be improved with brief contextual explanations.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents plausible hypotheses but lacks the quantitative and methodological detail required to support the central claims. A full manuscript with detailed methods, statistical analyses, and structural comparisons would be needed to evaluate the study properly.

## Risk / unsupported claims

- The claim that WT VAPA-COOH adopts a unique conformation absent in mutants is unsupported without conformational ensemble data.
- The claim that structural features better explain pathogenicity than physicochemical or steric determinants is unsupported without quantitative comparisons.
- The claim that deca-peptide systems faithfully reproduce full-length C-terminal behavior is unsupported without comparative metrics.
- The claim that conformational fluctuations do not affect the transmembrane domain or retinal binding is unsupported without stability and distance measurements.
- The therapeutic implications stated in the conclusion are speculative and not grounded in the presented findings.