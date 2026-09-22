## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results and discussion, conclusions, and materials and methods
- **Assessment boundary** Scientific content, structural biology methodology, claims regarding docking domain classification and structural novelty, and consistency of evidence presented
- **Shared manuscript claim summary** The authors characterize a pair of docking domains from the toblerol trans-AT polyketide synthase, show both are intrinsically disordered, solve the NMR structure of their complex, identify a novel 3-helix bundle topology, and propose reclassification of certain docking domain types based on structural comparisons
- **Visible evidence base** NMR structure determination, ITC binding measurements, CD spectroscopy, analytical size-exclusion chromatography, AlphaFold2 predictions, sequence and structural comparisons to previously characterized docking domains
- **Missing materials affecting confidence** Supplementary figures and tables referenced throughout (Fig. S1-S7, Tables S1-S6) were not provided; PDB validation reports not available; raw NMR restraint lists not accessible; AlphaFold2 prediction details and confidence metrics not shown

## Reviewer
- **Overall assessment** This manuscript presents a thorough structural and biophysical characterization of a docking domain pair from a relatively understudied trans-AT PKS system. The work is technically sound, with careful NMR-based structure determination and complementary biophysical validation. The central claim of a novel 3-helix bundle topology is supported by the experimental data, and the comparative analysis with previously characterized docking domains provides useful evolutionary and functional context. However, the broader conceptual advance is incremental, as the finding that alpha-helical docking domains exhibit structural plasticity and can form complexes of varying topology has been suggested by prior work. The manuscript would benefit from clearer articulation of the general principles that emerge beyond the specific system studied.

- **Who would be interested in the results, and why** Researchers in the fields of polyketide biosynthesis, protein-protein interaction design, and synthetic biology would find this work relevant. The characterization of a new docking domain pair expands the available toolkit for engineering modular PKS systems. The demonstration that structurally similar docking domains can form complexes of different topologies has implications for predicting docking compatibility in uncharacterized systems. The detailed biophysical characterization of intrinsically disordered regions folding upon binding is also of interest to the broader structural biology community studying coupled folding and binding phenomena.

- **Major strengths**
  1. Comprehensive biophysical characterization combining NMR, ITC, CD, and SEC to establish both structure and function of the docking domains
  2. High-quality NMR structure determination with extensive restraint information and validation metrics
  3. Thoughtful comparative analysis that places the new structure in the context of known docking domain families
  4. Clear demonstration that both partners are intrinsically disordered, adding to the growing appreciation of disorder in bacterial biosynthetic systems
  5. Practical implications for engineering docking domains in PKS synthetic biology applications

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** No
- **Axis** Evidence sufficiency
- **Claim pointer** The authors state that the toblerol docking domains represent a novel topology ("3HBb") distinct from previously characterized docking complexes, and that this demonstrates "plasticity of alpha-helical DDs, which allow the formation of a diverse topological spectrum of docked complexes."
- **Evidence pointer** Results and discussion, sections on NMR structure determination and structural comparisons; Fig. 6; Table S3
- **Concern** While the NMR structure clearly shows a 3-helix bundle with parallel helices, the claim of "unprecedented topology" requires more careful contextualization. The authors compare to the PAX 3HBa complex, but the structural similarity between the individual TobC CDD and 4HB-type CDDs (TM-scores 0.57-0.66) suggests this may be a variation on a known theme rather than a fundamentally new fold. The distinction between "novel topology" and "rearrangement of known elements" needs sharper definition. Additionally, the functional significance of this particular topology, beyond demonstrating that it works, is not established.
- **Why it matters** The central conceptual claim of the paper rests on the novelty of the observed topology. If this is simply a minor variation of known docking domain structures, the broader significance is diminished. The authors need to articulate what specifically is unprecedented and why this matters for understanding docking domain evolution or for engineering applications.
- **Resolution test** Provide a more rigorous structural classification framework that quantitatively distinguishes the 3HBb topology from previously characterized complexes. This could include analysis of helix packing angles, buried surface area distribution, or interaction interface conservation across all known docking domain structures. Alternatively, demonstrate a functional property of the 3HBb complex that is unique and cannot be achieved by other docking domain types.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Interpretive depth
- **Claim pointer** The authors propose that "individual DDs of equivalent topology can be combined to yield multiple complexes of distinctive structure" and that this reveals "previously unsuspected structural relations between DD types."
- **Evidence pointer** Results and discussion, sections on comparison of TobC CDD to 4HB-type CDDs and re-evaluation of type 2 CDDs; Fig. 2; Tables S4-S6
- **Concern** The comparative analysis is largely descriptive, cataloging structural similarities and differences without providing a mechanistic or evolutionary framework for how these variations arise. The authors note that type 2 CDDs can form complexes of different topologies, but do not address what sequence or structural features determine which topology is adopted. The observation that the same CDD fold can interact with different numbers of helices from the partner is intriguing but the underlying principles are not explored.
- **Why it matters** Without a predictive framework, the observations remain anecdotal. The stated goal of improving docking domain prediction for engineering applications requires understanding the determinants of complex topology, not just documenting that variation exists.
- **Resolution test** Identify specific sequence or structural features that correlate with the different complex topologies observed. This could involve mutational analysis of key interface residues, bioinformatic analysis of docking domain sequences with known structures, or computational modeling to identify determinants of partner helix number and orientation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Functional validation
- **Claim pointer** The authors state that the identified docking domains "should also find utility in modular PKS genetic engineering" and that the measured affinity (KD = 4 uM) is "on par with other pairs of 4HB domains."
- **Evidence pointer** Results and discussion, ITC measurements; Fig. 3
- **Concern** The functional relevance of the characterized interaction is inferred but not directly demonstrated. The authors do not show that these docking domains actually mediate productive intersubunit interactions in the context of the full toblerol PKS, nor do they test whether the domains can function in a heterologous context as claimed. The affinity measurement is useful, but the claim of utility for engineering is speculative without demonstration of portability or functionality in a chimeric system.
- **Why it matters** The stated practical significance of the work rests on the transferability of these docking domains. Without functional validation, the engineering claims are unsupported.
- **Resolution test** Demonstrate that the TobC CDD/TobE NDD pair can mediate functional complementation in a split PKS system, either by replacing a known docking pair in a heterologous system or by showing that the domains can support productive intersubunit interactions in a biochemical assay with tethered substrates.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Nomenclature and classification
- **Evidence pointer** Results and discussion, sections on structural comparisons
- **Issue** The naming convention for the new complex type ("3HBb") and the relationship to existing types (3HBa, 4HB, type 2, type 2-related) is introduced somewhat abruptly. The logic of the classification scheme is not fully explained, and the reader must track multiple type designations without a clear organizing framework.
- **Required correction** Provide a clear table or figure summarizing the classification scheme, including the structural features that define each type and the specific complexes that belong to each category. This would greatly aid comprehension of the comparative analysis.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** AlphaFold2 analysis
- **Evidence pointer** Results and discussion, section on AlphaFold2-based modelling; Fig. S4
- **Issue** The AlphaFold2 predictions are described qualitatively, but no confidence metrics (pLDDT scores, PAE values) are provided in the main text. The authors note that AlphaFold2 was less accurate for the isolated CDD regarding flexibility, but the details of this assessment are not presented.
- **Required correction** Include a supplementary figure showing the AlphaFold2 confidence metrics for both the isolated domains and the complex prediction, and provide a more quantitative comparison between the predicted and experimentally determined structures.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Mutational analysis
- **Evidence pointer** Results and discussion, section on evaluation of charged residues
- **Issue** The authors identify specific charged residues (R2271, R2278 in TobC CDD; D23, D30 in TobE NDD) that potentially contribute to interaction specificity, but only test mutations in TobC CDD. The corresponding mutations in TobE NDD are not examined.
- **Required correction** Either include mutational analysis of the TobE NDD residues to confirm their role, or temper the claims about the importance of these specific interactions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figures
- **Evidence pointer** Fig. 6
- **Issue** The structural figure showing the complex would benefit from clearer labeling of the interface residues and a surface representation to illustrate the buried surface area. The current representation makes it difficult to appreciate the interface features described in the text.
- **Required correction** Add a panel showing the interface in surface representation with key residues highlighted, and include a schematic diagram of the complex topology.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Context
- **Affected element** Introduction
- **Evidence pointer** Introduction section
- **Issue** The introduction provides good background on PKS systems but could more explicitly state the gap in knowledge that this work addresses. The rationale for studying the toblerol system specifically, beyond its novelty, is not fully articulated.
- **Required correction** Add a brief statement in the introduction that explicitly frames the open questions about docking domain diversity in trans-AT PKSs and why the toblerol system is particularly suited to address these questions.

## Risk / unsupported claims
1. The claim that the 3HBb topology is "unprecedented" is not fully supported without a more comprehensive structural comparison across all known docking domain complexes. The comparison to PAX 3HBa and 4HB types is informative but does not exhaustively rule out similar topologies in uncharacterized or unpublished structures.
2. The statement that these docking domains "should find utility in PKS genetic engineering" is speculative and not directly tested in this work.
3. The suggestion that "fuzzy" elements in the disordered regions may contribute to binding kinetics is presented as a possibility but not experimentally investigated.
4. The claim that the identified charged residue pairs contribute to interaction specificity is based on limited mutational data (only TobC CDD mutations tested) and structural inference, not direct binding measurements with all mutant combinations.
5. The assertion that "neither standard secondary structure prediction programs nor AlphaFold2 were able to confidently predict the number and extent of the alpha-helices in TobE NDD" is based on qualitative assessment; quantitative comparison of prediction accuracy is not provided.
6. The evolutionary implications drawn from structural comparisons, while reasonable, are speculative and not supported by phylogenetic or sequence conservation analysis.

## Assessment against Nature-style criteria
- **Originality** Moderate. The characterization of a new docking domain pair is valuable, but the finding that alpha-helical docking domains can form complexes of varying topology is an extension of prior observations rather than a conceptually new insight. The identification of a 3-helix bundle in a PKS system is novel, but the broader principle of structural plasticity in docking domains has been suggested by previous comparative studies.
- **Scientific importance** Moderate. The work provides a useful addition to the growing catalogue of docking domain structures and expands the understanding of structural diversity in these elements. However, the direct implications for understanding PKS function or improving engineering strategies are not fully realized in this manuscript.
- **Interdisciplinary readership** Limited. The manuscript is primarily of interest to specialists in polyketide biosynthesis and structural biology of protein-protein interactions. The broader significance for fields such as protein design or understanding intrinsically disordered proteins is not sufficiently developed to attract a wide interdisciplinary audience.
- **Technical soundness** High. The NMR structure determination appears rigorous, with appropriate validation metrics and deposition of data. The biophysical characterization is thorough and internally consistent. The comparative structural analysis is carefully executed, though the interpretive framework could be strengthened.
- **Readability for nonspecialists** Moderate. The manuscript is clearly written but assumes substantial background knowledge of PKS systems and structural biology techniques. The classification scheme for docking domain types is complex and would benefit from clearer presentation for readers outside the immediate field.