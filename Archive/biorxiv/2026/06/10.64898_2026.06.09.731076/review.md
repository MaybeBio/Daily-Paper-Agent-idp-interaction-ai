## Review setup
- **Input scope** Full manuscript text (abstract, main text sections, figure legends referenced but not provided in full)
- **Assessment boundary** Scientific claims, methodology, evidence quality, and internal consistency based solely on the supplied text
- **Shared manuscript claim summary** The authors report that NANOG, a transcription factor critical for pluripotency, forms self-limiting micelle-like assemblies driven by its intrinsically disordered tryptophan repeat domain. These micelles expose DNA-binding domains, act as multivalent crosslinkers of DNA, and drive a sol-gel transition with aging behavior at physiological concentrations. The authors propose that this gelation modulates genome dynamics rather than genome folding, potentially ingraining mechanical memory in gene regulatory networks.
- **Visible evidence base** Abstract, main text sections on gelling/aging, simulation results, experimental validation (cryo-EM, mass photometry, DLS), NANOG-DNA microrheology, conclusions, acknowledgements
- **Missing materials affecting confidence** Full figures and figure legends, supplementary information (SI) including Fig. S1-S5, detailed methods section, experimental protocols, statistical analysis details, raw data

## Reviewer
- **Overall assessment** This manuscript presents a novel and potentially significant finding: NANOG forms self-limiting micelles rather than unbounded condensates, and these micelles act as aging crosslinkers of DNA. The combination of simulations, biophysical characterization, and microrheology is ambitious and appropriate. However, the evidence as presented has several gaps that prevent full confidence in the central claims. The simulation results are described but key quantitative details are missing. The experimental validation is suggestive but the heterogeneity of the assemblies and the lack of structural resolution limit interpretation. The physiological relevance argument, while intriguing, relies on extrapolation from in vitro conditions that differ substantially from the nuclear environment. The manuscript would benefit from clearer presentation of methods, quantitative comparisons, and a more cautious interpretation of the in vivo implications.
- **Who would be interested in the results, and why** Researchers in the fields of phase separation and condensate biology, transcription factor regulation, chromatin organization, and biophysics of intrinsically disordered proteins. The finding that a transcription factor forms self-limiting micelles rather than unbounded condensates challenges current paradigms and may have broad implications for understanding gene regulation. The rheological characterization of protein-DNA mixtures is also relevant to the emerging field of nuclear mechanics.
- **Major strengths** 1) The discovery of self-limiting micelle formation by NANOG is novel and contrasts with the prevailing view of unbounded condensate formation by IDPs. 2) The multi-technique approach (simulations, cryo-EM, mass photometry, DLS, microrheology) provides complementary evidence. 3) The connection between molecular assembly and macroscopic rheological properties is conceptually interesting. 4) The proposal that NANOG modulates genome dynamics rather than folding is a testable and potentially important hypothesis.
- **Major Concerns** 
  - R1-M1: The simulation evidence for micelle formation is described qualitatively without sufficient quantitative support.
  - R1-M2: The experimental validation of self-limiting assemblies is incomplete; cryo-EM shows heterogeneous shapes and no structural resolution.
  - R1-M3: The claim that NANOG-DNA gels form at "physiological concentrations" is not well supported by the data presented.
  - R1-M4: The mechanism linking micelle formation to gelation and aging is not fully established.
  - R1-M5: The physiological relevance argument is speculative and not directly tested.
- **Minor Comments** 
  - R1-m1: The manuscript would benefit from a clearer description of the microrheology methodology.
  - R1-m2: The relationship between the estimated overlap concentration and the observed gelation threshold should be clarified.
  - R1-m3: The authors should discuss potential alternative explanations for the observed sub-diffusive behavior.
  - R1-m4: The manuscript should acknowledge limitations of the Mpipi model for capturing the full complexity of NANOG behavior.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** 
  - Originality: High. The concept of self-limiting micelle formation by a transcription factor is novel and distinct from the prevailing condensate paradigm.
  - Scientific importance: Potentially high, but the physiological relevance is not yet established. If confirmed in vivo, this could reshape understanding of transcription factor function.
  - Interdisciplinary readership: The work bridges biophysics, molecular biology, and polymer physics, which could appeal to a broad audience. However, the presentation may be too specialized for nonspecialists in some sections.
  - Technical soundness: The combination of techniques is appropriate, but the evidence as presented has gaps. The simulation results need more quantitative support, and the experimental validation is incomplete.
  - Readability for nonspecialists: The abstract is clear, but the main text assumes significant background knowledge in both biophysics and molecular biology. Some concepts (e.g., Maxwell fluids, generalized Stokes-Einstein relation) are introduced without sufficient explanation for a general audience.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is novel and potentially important, but the evidence as presented does not fully establish the claims. The authors should strengthen the quantitative analysis, provide more complete experimental validation, and temper the physiological relevance claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "Simulations reveal NANOG assembles into self-limiting micelles" and "NANOG molecules form a micelle-like structure, where the WR occupies the cluster core, the DNA binding domain occupies the intermediate layer and the N-terminal domain forms the outer layer"
- **Evidence pointer** Section "Simulations reveal NANOG assembles into selflimiting micelles", Figure 2a-d, location not provided
- **Concern** The simulation results are described qualitatively. The authors state that NANOG forms clusters of approximately 30 proteins with a micelle-like structure, but no quantitative data is provided on cluster size distributions, free energy calculations, or comparison with control simulations. The claim that the clusters are "self-limiting" and "thermodynamically stable" is based on a single re-equilibration experiment after forced mixing, which is insufficient to establish thermodynamic stability. Additionally, the simulation conditions (M=50 proteins, density 0.1 g/cm3) may not be representative of the experimental conditions, and the relationship between simulation timescales (20 µs) and experimental timescales (hours) is not discussed.
- **Why it matters** The micelle formation is the central structural claim of the manuscript. Without robust quantitative evidence from simulations, the interpretation of the experimental data as evidence for micelle formation is weakened. The self-limiting nature of the assemblies is critical to distinguish them from unbounded condensates, and this claim requires stronger support.
- **Resolution test** Provide quantitative cluster size distributions, free energy profiles or potential of mean force calculations, and control simulations with disrupted tryptophan repeats. Show that the cluster size is independent of initial conditions and protein concentration. Demonstrate that the micelle-like organization is robust across multiple simulation parameters and replicates.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "Cryo-EM reproducibly identified NANOG complexes that were monodisperse in size, approximately 25 nm and compatible with the size expected for a globular assembly of 20-30 NANOG monomers" and "Mass photometry also identified assemblies with molecular weight MW ≃ 0.8 MDa, compatible with ≃ 22-25 NANOG WT monomers"
- **Evidence pointer** Section "Experimental validation of self-limiting NANOG assemblies", Figure 2e-f, location not provided
- **Concern** The experimental validation is incomplete. Cryo-EM shows heterogeneous shapes and the authors state they "could not solve their structure," which limits the interpretation of the assemblies as well-defined micelles. Mass photometry provides a single molecular weight estimate without error bars or replicate measurements. The DLS data shows a shift in hydrodynamic size with time, but the interpretation of this as evidence for self-limiting behavior is not fully justified. The authors do not provide a direct comparison between the experimentally measured size and the size predicted from the simulation structure.
- **Why it matters** The experimental validation is crucial to confirm that the micelle-like structures observed in simulations actually form in solution. Without high-resolution structural data or more complete biophysical characterization, the claim that NANOG forms "self-limiting micelles" rather than amorphous aggregates or other assemblies is not fully supported.
- **Resolution test** Provide more detailed cryo-EM analysis, including 2D class averages and 3D reconstructions if possible, or at least a quantitative analysis of particle size distribution and shape heterogeneity. Include replicate mass photometry measurements with error bars. Perform size-exclusion chromatography or analytical ultracentrifugation to confirm the monodispersity and molecular weight of the assemblies. Compare experimental size measurements with simulation predictions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** "NANOG-DNA solutions form aging gels at physiological concentrations" and "the presence of DNA triggers aging and gelation despite using an 18-fold lower protein concentration than the estimated overlap concentration"
- **Evidence pointer** Section "NANOG-DNA solutions form aging gels at physiological concentrations", Figures 3-4, location not provided
- **Concern** The claim that gelation occurs at "physiological concentrations" is not well supported. The authors use a DNA concentration of 250 ng/µl (7.9 nM for λ-DNA), which is described as "around 10-fold larger than λ-DNA overlapping concentration." However, the physiological relevance of this DNA concentration is not established. The nuclear DNA concentration in mammalian cells is typically much higher, but the DNA is organized into chromatin, which has different physical properties than naked DNA in solution. The NANOG concentrations used (10 nM to 10 µM) are stated to be "in broad agreement with the values reported in vivo," but the authors also note that NANOG forms foci with higher local concentrations. The relationship between the in vitro conditions and the in vivo nuclear environment is not clearly established.
- **Why it matters** The physiological relevance of the observed gelation is a key part of the manuscript's significance. If the conditions used in the experiments are not representative of the nuclear environment, the claims about NANOG's role in regulating genome dynamics in vivo are weakened.
- **Resolution test** Provide a more detailed justification for the choice of DNA and protein concentrations, including references to nuclear concentrations and chromatin density. Perform experiments with chromatinized DNA or with DNA at concentrations closer to those found in the nucleus. Discuss how the presence of other nuclear proteins and chromatin structure might affect the observed gelation.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "This result suggests that in vivo, NANOG foci may act as solid-like gel microenvironments that restrict DNA dynamics" and "the aging of NANOG micelles may physically ingrain memory in a regulatory gene network"
- **Evidence pointer** Sections "NANOG-DNA solutions form aging gels at physiological concentrations" and "Conclusions", Figures 3-4, location not provided
- **Concern** The mechanism linking micelle formation to gelation and aging is not fully established. The authors propose that NANOG micelles act as "aging crosslinkers" that stabilize DNA entanglements, but the molecular details of this process are not provided. The aging behavior is attributed to "molecular reorganization of the intrinsically disordered domains within the assembly," but this is speculative. The authors also note that their time-cure superposition analysis "does not align with the one expected for simple Maxwell fluids," which suggests the gelation mechanism is more complex than described, but this is not explored further.
- **Why it matters** Understanding the mechanism of gelation and aging is essential for evaluating the biological significance of the findings. Without a clear mechanistic model, it is difficult to predict how NANOG would behave in the complex nuclear environment or to design experiments to test the in vivo relevance.
- **Resolution test** Provide a more detailed mechanistic model for how NANOG micelles crosslink DNA and how aging occurs. Perform experiments to test specific predictions of the model, such as the effect of tryptophan mutations on crosslinking efficiency or the reversibility of the aging process. Use rheological measurements to characterize the gel structure and dynamics more fully.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** "NANOG may contribute to regulate gene expression by creating local gel-like environments that restrict genome dynamics and that its aging may ingrain mechanical memory in gene regulatory networks"
- **Evidence pointer** Conclusions, location not provided
- **Concern** The physiological relevance of the findings is speculative. The authors propose that NANOG micelles create gel-like environments that restrict genome dynamics, but no direct evidence is provided for this in cells. The connection between the in vitro rheological properties and in vivo gene regulation is not established. The authors suggest that "areas where NANOG is enriched (foci) should correlate with slow chromatin dynamics," but this prediction is not tested.
- **Why it matters** The significance of the work for understanding NANOG function in embryonic stem cells depends on the physiological relevance of the observed gelation. Without direct evidence for gel-like environments in cells, the broader implications of the findings remain uncertain.
- **Resolution test** Provide preliminary data from cell-based experiments, such as fluorescence recovery after photobleaching (FRAP) or single-particle tracking of chromatin loci in NANOG-enriched regions. Alternatively, discuss how the in vitro findings could be tested in vivo and what specific predictions the model makes.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Methods description
- **Evidence pointer** Section "Gelling and aging of NANOG solutions", location not provided
- **Issue** The microrheology methodology is described briefly without sufficient detail for replication. The authors mention "passive tracers" and "2D mean squared displacement" but do not provide details on tracer size, surface chemistry, or the number of experiments performed.
- **Required correction** Provide a more detailed description of the microrheology protocol, including tracer preparation, imaging conditions, and data analysis procedures. Include information on the number of replicates and the statistical analysis used.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Concentration estimates
- **Evidence pointer** Section "Experimental validation of self-limiting NANOG assemblies", location not provided
- **Issue** The relationship between the estimated overlap concentration (c* ≃ 0.14 mM) and the observed gelation threshold is not clearly explained. The authors state that gelation is observed at 1 mM, which is approximately 7-fold higher than c*, but the significance of this ratio is not discussed.
- **Required correction** Provide a more detailed discussion of the relationship between c* and the gelation threshold, including how this compares to other systems and what it implies about the gelation mechanism.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Alternative explanations
- **Evidence pointer** Section "NANOG-DNA solutions form aging gels at physiological concentrations", location not provided
- **Issue** The authors do not discuss alternative explanations for the observed sub-diffusive behavior of tracers in NANOG-DNA solutions. For example, non-specific DNA-protein interactions or the formation of large aggregates could also lead to reduced tracer mobility.
- **Required correction** Discuss potential alternative explanations and how the data distinguish between them. Consider performing control experiments with non-DNA-binding proteins or with DNA alone.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Model limitations
- **Evidence pointer** Section "Simulations reveal NANOG assembles into selflimiting micelles", location not provided
- **Issue** The limitations of the Mpipi model for capturing the full complexity of NANOG behavior are not discussed. The model is parameterized on bioinformatics data and all-atom simulations, but it may not capture all relevant interactions, particularly those involving the DNA-binding domain.
- **Required correction** Acknowledge the limitations of the coarse-grained model and discuss how they might affect the conclusions. Consider comparing the simulation results with experimental data more quantitatively.

## Risk / unsupported claims
- The claim that NANOG micelles are "thermodynamically stable" is not fully supported by the evidence presented. The re-equilibration experiment after forced mixing is suggestive but not conclusive.
- The claim that NANOG-DNA gels form at "physiological concentrations" is not well established, as the relationship between the in vitro conditions and the nuclear environment is not clearly defined.
- The proposal that NANOG "may contribute to regulate gene expression by creating local gel-like environments" is speculative and not directly tested.
- The claim that the aging of NANOG micelles "may ingrain mechanical memory in gene regulatory networks" is a conjecture without direct evidence.
- The statement that "NANOG may behave similarly to a block co-polymer" is an analogy that is not quantitatively tested.
- The claim that the observed gelation is "unconventional" because it is driven by micelles that act as aging crosslinkers is not compared to other unconventional gelation mechanisms in the literature.