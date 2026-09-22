## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, funding, acknowledgements) as provided by the user. Supplementary data referenced but not provided.
- **Assessment boundary** Scientific content, technical soundness, logical coherence, and support of claims based solely on the provided manuscript text. No external literature verification or access to supplementary materials.
- **Shared manuscript claim summary** The authors propose that MDP1, via its intrinsically disordered region (mIDR), compacts mycobacterial DNA by a "double-sided tape" cross-linking mechanism between adjacent DNA duplexes, which induces a dormant, non-replicating state. This model is supported by HS-AFM imaging, CGMD simulations, and functional assays with truncated mutants.
- **Visible evidence base** Main text figures referenced (Figures 1–6), supplementary figures/tables/videos referenced but not visible, methods partially described (bacterial strains, reagents; other methods in supplementary).
- **Missing materials affecting confidence** Supplementary data (all supplementary figures, tables, videos, detailed methods), full methods for HS-AFM, CGMD simulation parameters, gel retardation assay details, biolayer interferometry data, flow cytometry gating, statistical analysis details, and strain construction details.

## Reviewer
- **Overall assessment** This manuscript presents a compelling and novel model for DNA compaction by an intrinsically disordered protein, MDP1, using a combination of high-speed atomic force microscopy and coarse-grained molecular dynamics simulations. The "double-sided tape" mechanism is conceptually interesting and distinct from known HU-mediated DNA bending. The functional data linking mIDR length to compaction and growth suppression strengthen the biological relevance. However, the manuscript's reliance on supplementary materials for critical methodological details and quantitative data limits the ability to fully assess technical rigor. Several claims, particularly regarding the "hijacking" of HU function and the direct induction of dormancy, require more direct evidence or clearer logical framing. The monomeric state of MDP1 and its functional implications are also not fully reconciled with existing structural data.
- **Who would be interested in the results, and why** Researchers in bacterial physiology, mycobacterial biology, DNA-protein interactions, intrinsically disordered proteins, and biophysics. The study provides a new paradigm for how IDPs can compact DNA, which is relevant to understanding dormancy and persistence in pathogens. The HS-AFM methodology will also be of interest to the single-molecule biophysics community.
- **Major strengths**
  1. Novel mechanistic model: The "double-sided tape" cross-linking model is a fresh conceptual framework for IDP-mediated DNA compaction, distinct from the rigid scaffolding of H-NS or the bending of HU.
  2. Multi-technique approach: Combining real-time HS-AFM imaging with CGMD simulations provides complementary views of the dynamic process, lending credibility to the proposed mechanism.
  3. Functional relevance: The demonstration that mIDR length correlates with DNA compaction in vitro and growth suppression in bacteria directly links the biophysical mechanism to a biological phenotype.
  4. Clear writing: The manuscript is generally well-structured and the logic is easy to follow, making the complex findings accessible.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The claim that MDP1 is predominantly monomeric in solution and that this monomeric form is the functional unit for DNA cross-linking.
  - **Evidence pointer** Results section "mIDR bands or tapes two dsDNAs together by the monomer form"; Supplementary Figure S4A, S4B; Discussion.
  - **Concern** The manuscript states that SV-AUC and GA-cross-linking show MDP1 is mostly monomeric, but the provided text only shows a single SV-AUC trace for MDP1Mtb and a gel for MDP1Msm. The quantification of the monomer/dimer ratio is not shown in the main text. More critically, the functional significance of the monomer is inferred from HS-AFM observations of 1HUR-1TRX sets. However, the manuscript does not address how a monomeric MDP1, which lacks the canonical dimeric HU fold, achieves stable DNA binding and cross-linking. The CGMD model uses a single MDP1 molecule, but the parameters and validation of this model are not fully described. The claim that the monomer is the functional species is central to the proposed model and needs stronger experimental support, including a direct comparison of the DNA-binding and cross-linking activity of the monomer versus the dimer.
  - **Why it matters** If MDP1 functions as a dimer in vivo, the proposed "double-sided tape" model would be fundamentally incorrect. The manuscript's own data show a significant dimer population (~20-30%), and the functional role of this population is not explored. The model's foundation rests on the monomer being the active species, which is not convincingly established.
  - **Resolution test** Provide clear quantification of the monomer/dimer equilibrium under the exact conditions used for HS-AFM and functional assays. Perform and present experiments (e.g., size-exclusion chromatography coupled with DNA-binding assays, or site-specific cross-linking) that directly correlate the oligomeric state with DNA compaction activity. The CGMD model should be validated against these experimental data.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The claim that mIDR "hijacks" HU function, based on experiments with HUα-mIDR and HUβ-mIDR fusion proteins.
  - **Evidence pointer** Results section "mIDR hijacks the HU functions"; Figure 6A–E.
  - **Concern** The "hijacking" claim is an interpretation of experiments where mIDR is artificially fused to E. coli HU. While these experiments show that the fusion protein can compact DNA and induce growth suppression, they do not demonstrate that mIDR "hijacks" HU function in a natural context. MDP1 is not a fusion of HU and mIDR; it has its own unique N-terminal HUR. The experiments show that mIDR can confer new properties to HU, but this is a synthetic biology demonstration, not evidence of a natural mechanism. The claim overreaches the data.
  - **Why it matters** The term "hijack" implies a specific biological interaction or competition that is not demonstrated. This overstatement could mislead readers about the natural role of mIDR and its relationship to HU. The distinction between "mIDR can confer DNA-compaction activity to HU" and "mIDR hijacks HU function" is significant.
  - **Resolution test** Rephrase the claim to accurately reflect the data, e.g., "mIDR can confer DNA-compaction and growth-suppression activities to a heterologous HU protein." Alternatively, provide direct evidence for a natural interaction or competition between MDP1 and HU in mycobacteria.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Support for conclusions
  - **Claim pointer** The claim that the "double-sided tape" mechanism is the reason for the "resuscitable non-replicating dormant mycobacteria" and that this is a "reasonable model for MDP1 suppression of the genomic function."
  - **Evidence pointer** Abstract; Results section "mIDR induces mycobacterial dormancy"; Figure 6F–H; Discussion.
  - **Concern** The manuscript demonstrates a correlation between mIDR length, DNA compaction, and growth suppression. However, the causal link between the specific "double-sided tape" mechanism and the induction of a dormant, resuscitable state is not established. The growth suppression and viability data (OD600, CFU, flow cytometry) show that mIDR expression can halt growth without significant cell death, but this is a phenotypic observation. The manuscript does not directly test whether the "double-sided tape" compaction is necessary or sufficient for this phenotype. Other mechanisms, such as non-specific DNA sequestration or altered gene expression, could also explain the growth suppression.
  - **Why it matters** The title and abstract make a strong claim about the mechanism of dormancy induction. If the link between the specific molecular mechanism and the complex biological phenotype is not proven, the central thesis of the paper is weakened. The claim goes beyond the data presented.
  - **Resolution test** Perform experiments that directly test the model. For example, use a mutant mIDR that can bind DNA but cannot cross-link (if such a separation is possible) and test its effect on growth suppression. Alternatively, use a chemical inhibitor or optogenetic tool to disrupt the "double-sided tape" interaction in vivo and observe the effect on dormancy. At minimum, the discussion should be tempered to clearly state that the "double-sided tape" model is a proposed mechanism that is consistent with, but not proven to be the cause of, the observed dormancy phenotype.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Figure 1E
  - **Evidence pointer** Results section "MDP1 compacts DNA duplexes via side-by-side DNA bundling"
  - **Issue** The text mentions "compaction of a relatively large open region was less frequent (Figure 1E, indicated by arrows)". The figure is not visible, and the description is vague. It is unclear what constitutes a "large open region" and how "frequency" was quantified.
  - **Required correction** Provide a clearer description of the quantification method for this observation, or move the detailed analysis to the supplementary materials with a clear reference.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** CGMD simulation
  - **Evidence pointer** Results section "CGMD model of the DNA cross-linking by MDP1 mIDR"; Supplementary Figure S6; Supplementary Table S4.
  - **Issue** The description of the CGMD model is very brief. The force field parameters, the representation of the DNA and protein, the simulation length, and the number of replicates are not described in the main text. The validation of the model against experimental data is not shown.
  - **Required correction** Provide a more detailed description of the simulation setup in the main text or refer to a detailed methods section in the supplementary materials. The validation of the model should be explicitly stated.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Figure 5D
  - **Evidence pointer** Results section "mIDR length-dependent DNA compaction and growth suppression"
  - **Issue** The text states that "T173Msm and T191Msm mutants showed similar DNA compaction activity as full-length MDP1Msm." It is unclear if this is a statistically significant finding or a qualitative observation.
  - **Required correction** Include statistical analysis for the compaction data in Figure 5D, or state clearly that the observations are qualitative.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Readability
  - **Affected element** Discussion
  - **Evidence pointer** Discussion section
  - **Issue** The discussion is somewhat repetitive and could be more focused. The comparison with H-NS is interesting but could be more concise.
  - **Required correction** Streamline the discussion to highlight the key novel findings and their implications, avoiding restating results.
- **Technical failings that need to be addressed before the case is established**
  - R1-M1: The functional role of the MDP1 monomer versus dimer is not established.
  - R1-M2: The "hijacking" claim is an overinterpretation of the fusion protein experiments.
  - R1-M3: The causal link between the "double-sided tape" mechanism and dormancy induction is not proven.
- **Assessment against Nature-style criteria**
  - **Originality**: High. The "double-sided tape" model for IDP-mediated DNA compaction is a novel concept that challenges existing paradigms of bacterial chromatin organization.
  - **Scientific importance**: High. Understanding dormancy in mycobacteria, including M. tuberculosis, is of significant medical importance. A new mechanism for DNA compaction that induces a dormant state could have implications for drug development.
  - **Interdisciplinary readership**: Moderate to High. The work bridges microbiology, biophysics, and structural biology. The use of HS-AFM and CGMD will appeal to biophysicists, while the biological context will appeal to microbiologists.
  - **Technical soundness**: Currently not fully assessable. The core claims rely heavily on supplementary data and methods that were not provided. The concerns about the monomer/dimer issue and the causal link to dormancy are significant.
  - **Readability for nonspecialists**: Good. The manuscript is well-written and the concepts are explained clearly, making it accessible to a broad scientific audience.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is novel and interesting, but the manuscript needs to address the concerns about the functional monomer, the overinterpretation of the "hijacking" data, and the causal link to dormancy. The authors should also provide more details on the methods and quantitative data in the main text or make the supplementary materials available for review.

## Risk / unsupported claims
- The claim that the "double-sided tape" mechanism is the direct cause of the "resuscitable non-replicating dormant" state is not supported by the provided evidence. The data show a correlation, not causation.
- The claim that mIDR "hijacks" HU function is an overstatement of the fusion protein experiments.
- The claim that MDP1 is predominantly a functional monomer is not fully supported by the data presented in the main text.
- The quantitative aspects of the HS-AFM analysis (e.g., "compaction of a relatively large open region was less frequent") are not described in sufficient detail to be assessed.
- The CGMD simulation results are presented as supporting the model, but the model's parameters and validation are not described in the provided text, making the results unassessable.