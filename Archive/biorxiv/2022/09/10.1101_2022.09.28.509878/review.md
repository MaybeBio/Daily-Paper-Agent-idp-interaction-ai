## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods) as provided
- **Assessment boundary** Scientific claims, methodological soundness, and internal consistency of the presented evidence; no assessment of data availability beyond the provided text
- **Shared manuscript claim summary** The authors report that fusion of aggregation-prone hRNPs (FUS, TDP-43, hCPEB3) to an engineered spider silk domain (NT*) enables native purification and controlled liquid-liquid phase separation (LLPS) by pH adjustment. Using native ion mobility-mass spectrometry (nMS/IM-MS) and molecular dynamics (MD) simulations, they report distinct conformational transitions and assembly mechanisms for each protein: FUS undergoes an unfolded-to-globular compaction, TDP-43 forms partially disordered dimers/trimers via N-terminal domain interactions, and hCPEB3 favors fibrillar aggregation over LLPS. The authors propose that these distinct assembly architectures have functional implications for RNA processing and translation.
- **Visible evidence base** Abstract; Introduction; Results sections (four subsections); Discussion; Materials and Methods (reagents, protein production, microscopy, pH-dependent solubility assay, RNA binding assays, nMS/IM-MS, CCS database searches, MD simulation protocols for NT*-hCPEB3, FUS, and TDP-43, negative stain EM); Conflict of interest; Data availability; Acknowledgements. Supplementary figures and movies are referenced but not provided.
- **Missing materials affecting confidence** Supplementary figures (S1–S5), supplementary discussion, Movie S1, raw mass spectra, IM-MS arrival time distributions, CCS calibration data, MD simulation trajectories and convergence metrics, negative stain EM images, and full-length protein sequence information for the NT* fusion constructs

## Reviewer
- **Overall assessment** This manuscript presents a technically ambitious approach to a challenging problem: obtaining structural information on phase-separated states of aggregation-prone RNA-binding proteins. The combination of a solubility-enhancing spider silk tag with native MS and MD simulations is creative and potentially valuable. However, the evidence as presented is insufficient to fully support the central claims. Key concerns include the lack of direct evidence that the species observed by nMS originate from liquid droplets, the absence of quantitative validation for the MD-derived models, and the limited demonstration that the NT* tag does not fundamentally alter the assembly behavior of the proteins under study. The manuscript would benefit from additional control experiments, quantitative analysis of the MS data, and clearer presentation of the structural models.
- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation, membraneless organelle biogenesis, and the molecular mechanisms of neurodegeneration (ALS, FTD) would find the methodological approach and comparative analysis of three hRNPs of interest. The use of native MS to probe conformational states in the context of LLPS is a relatively underexplored application that could attract attention from the structural biology and biophysics communities. The proposed distinct assembly mechanisms for FUS, TDP-43, and hCPEB3, if validated, would be relevant to understanding how sequence and domain architecture dictate phase behavior and aggregation propensity.
- **Major strengths** 1) The use of a spider silk-derived solubility tag to enable native purification of full-length, aggregation-prone hRNPs is a practical and potentially generalizable advance. 2) The combination of nMS/IM-MS with MD simulations is a sophisticated multi-scale approach that could provide insights inaccessible to either method alone. 3) The comparative analysis of three hRNPs with similar domain architectures but distinct assembly behaviors is a useful framework for understanding the determinants of LLPS versus aggregation. 4) The pH-controlled LLPS system is simple and well-suited for MS analysis.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5
- **Assessment against Nature-style criteria** **Originality:** The approach of using native MS to probe conformational states during LLPS is not entirely new, but the specific application to full-length hRNPs using a solubility tag is a creative combination. The comparative analysis of three proteins is a useful contribution. **Scientific importance:** The question of how hRNPs assemble into droplets versus fibrils is of high importance for understanding neurodegeneration and RNA biology. However, the current evidence does not yet establish the claimed distinct mechanisms with sufficient rigor. **Interdisciplinary readership:** The topic bridges structural biology, biophysics, and cell biology, and would appeal to a broad readership if the claims are well-supported. **Technical soundness:** The MS methodology is generally sound, but the lack of quantitative analysis and the absence of key controls (e.g., demonstrating that MS signals originate from droplet-associated species) weaken the technical case. The MD simulations are described but not validated against experimental data. **Readability for nonspecialists:** The manuscript is generally well-written and accessible, but some sections (e.g., the description of MD simulations) assume familiarity with specialized techniques. The figures are referenced but not provided, making it difficult to fully assess clarity.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important problem with a creative approach, but the current evidence does not fully establish the central claims. Substantial revisions and additional experiments are required.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The authors claim that nMS can observe proteins "in liquid droplets" and that the loss of MS signal at pH 7.5 for NT*-FUS is due to incorporation into assemblies "not detectable by MS."
- **Evidence pointer** Results section "NT*-FUS and NT*-TDP-43 in liquid droplets can be observed by nMS"; Figure 2
- **Concern** The manuscript does not provide direct evidence that the species observed by nMS at pH 10.5 or the loss of signal at pH 7.5 are specifically associated with liquid droplets. The correlation between microscopy observations and MS data is suggestive but not conclusive. The loss of MS signal could be due to precipitation, non-specific aggregation, or adsorption to surfaces, rather than incorporation into liquid droplets. The claim that collisional activation releases monomers from "assemblies" is not quantitatively supported; the data in Figure S2 are not provided.
- **Why it matters** The central premise of the manuscript is that nMS can report on conformational states relevant to LLPS. Without direct evidence linking the MS-observed species to the droplet state, the interpretation of the data is ambiguous.
- **Resolution test** Provide control experiments showing that the loss of MS signal at pH 7.5 is reversible (e.g., by raising pH) and that the released monomers after collisional activation have the same mass and conformation as the input material. Alternatively, use a fluorescently labeled protein to confirm that the material in the MS sample is in droplet form. Quantify the MS signal loss and correlate it with the fraction of protein in droplets as determined by microscopy.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that IM-MS data reveal "distinct conformational signatures" for NT*-FUS and NT*-TDP-43 during LLPS, specifically an unfolded-to-globular transition for FUS and partial disorder for TDP-43.
- **Evidence pointer** Results section "Distinct conformational signatures of NT*-FUS and NT*-TDP-43 during LLPS"; Figure 3
- **Concern** The interpretation of CCS data for disordered proteins in the gas phase is complex and can be influenced by factors such as charge state, ion activation, and the presence of residual solvent or salt adducts. The manuscript does not provide sufficient detail on how the CCS values were calibrated, whether the arrival time distributions were deconvoluted, or how the "partially disordered" state was defined. The comparison to "the behavior of globular proteins" is qualitative and lacks a quantitative benchmark. The claim that the CCS data are "in agreement with recent NMR and EPR studies" is not substantiated with specific comparisons.
- **Why it matters** The conformational conclusions are a key part of the manuscript's central claim. If the CCS data are not rigorously analyzed and interpreted, the conclusions about distinct assembly mechanisms are weakened.
- **Resolution test** Provide a detailed description of the IM-MS calibration and data analysis, including error bars on CCS values. Include control experiments with well-folded and fully disordered proteins of similar mass to benchmark the interpretation. If possible, compare the experimentally determined CCS values with those predicted from the MD models.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The authors claim that MD simulations reveal "structural models of FUS and TDP-43 assembly intermediates" and that these models support the distinct assembly mechanisms.
- **Evidence pointer** Results section "Structural models of FUS and TDP-43 assembly intermediates"; Figure 4; Materials and Methods "Modelling and simulation of FUS" and "Modelling and simulation of TDP-43"
- **Concern** The MD simulations are described but the results are not presented in sufficient detail to evaluate their validity. For FUS, a single 500 ns all-atom simulation is described, which is likely too short to sample the conformational ensemble of a 526-residue protein. For TDP-43, the coarse-grained simulations are described but the convergence of the simulations is not demonstrated. The "contact maps" and "electrostatic energies" are mentioned but not shown in the provided text. The claim that the models reveal "assembly intermediates" is not supported by the described methodology, which appears to simulate monomers, dimers, and trimers in solution, not the process of assembly itself.
- **Why it matters** The MD models are used to support the proposed assembly mechanisms. If the simulations are not converged or are not appropriately analyzed, the structural conclusions are not reliable.
- **Resolution test** Provide evidence of simulation convergence (e.g., RMSD plots, block averaging). Show the contact maps and electrostatic energy calculations. If possible, validate the models against experimental data (e.g., CCS values from IM-MS, or known structural information on the NTD of TDP-43).

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the NT* tag "enhances hRNP stability without abolishing LLPS" and that the observed assembly behaviors are specific to each hRNP and "unlikely to be affected by the presence of the NT* domain."
- **Evidence pointer** Results section "A spider silk tag enhances hRNP stability without abolishing LLPS"; Discussion; Supplementary discussion (referenced but not provided)
- **Concern** The manuscript does not provide a direct comparison of the phase behavior and conformational properties of the untagged proteins versus the NT*-tagged proteins. The claim that the NT* tag does not affect assembly is based on a referenced supplementary discussion, which is not available for review. The NT* domain is a charge-reversed mutant of the spider silk N-terminal domain, and it is plausible that it could influence the conformational ensemble of the fusion protein, particularly given its role in pH-sensitive dimerization in the native context.
- **Why it matters** The entire study is performed on NT*-tagged proteins. If the tag significantly alters the assembly mechanism, the conclusions may not be relevant to the untagged, physiologically relevant proteins.
- **Resolution test** Provide the supplementary discussion for review. Ideally, include control experiments with untagged proteins (if they can be purified) or with a different, inert solubility tag to demonstrate that the observed behaviors are specific to the hRNP moiety.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The authors claim that hCPEB3 "favors aggregation over LLPS" based on the absence of spherical droplets and the presence of fibrillar aggregates, and that nMS shows it "remains fully disordered."
- **Evidence pointer** Results section "The conformational balance of hCPEB3 favors aggregation over LLPS"; Figure 5
- **Concern** The evidence for hCPEB3's preference for aggregation is based on microscopy and nMS, but the manuscript does not provide a quantitative comparison of the aggregation propensity of hCPEB3 versus FUS and TDP-43 under the same conditions. The nMS data show a "large population of highly charged ions," but this is not quantified or compared to the other proteins. The claim that the protein "remains fully disordered" is based on the charge state distribution, but this interpretation is not validated. The negative stain EM data are mentioned but not shown.
- **Why it matters** The comparison between the three proteins is a key part of the manuscript's message. If the evidence for hCPEB3's behavior is not as robust as for the other proteins, the comparative conclusions are weakened.
- **Resolution test** Provide quantitative analysis of the nMS data (e.g., average charge state, CCS distributions) for all three proteins under all conditions. Show the negative stain EM images. Include a quantitative measure of aggregation (e.g., ThT fluorescence intensity, sedimentation assay) for all three proteins.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that the authors "find that NT*-FUS monomers undergo an unfolded-to-globular transition, whereas NT*-TDP-43 oligomerizes into partially disordered dimers and trimers." This is a strong claim that is not fully supported by the evidence presented in the main text, as the conformational interpretation relies on indirect MS measurements.
- **Required correction** Soften the language in the abstract to reflect the indirect nature of the evidence, e.g., "consistent with an unfolded-to-globular transition" or "suggesting partial disorder."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Materials and Methods, "Native and ion mobility mass spectrometry"
- **Evidence pointer** Materials and Methods
- **Issue** The description of the nMS/IM-MS methods lacks important details, such as the capillary voltage, source temperature, and the specific settings for the ion mobility separation. The calibration procedure is described but the accuracy of the CCS measurements is not stated.
- **Required correction** Provide a more detailed description of the MS parameters and the calibration procedure, including the expected error in the CCS measurements.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section "Structural models of FUS and TDP-43 assembly intermediates"
- **Evidence pointer** Results section
- **Issue** The description of the MD models is brief and lacks specific details on the structural features that distinguish the assembly intermediates. The "corkscrew" structure of the TDP-43 NTD trimer is mentioned but not described in detail.
- **Required correction** Provide a more detailed description of the structural models, including key contacts and conformational features, and refer to the relevant figures.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results section "The conformational balance of hCPEB3 favors aggregation over LLPS"
- **Evidence pointer** Results section
- **Issue** The negative stain EM data are mentioned but not shown or described in detail. The conditions under which the fibrillar aggregates were formed are not clearly stated.
- **Required correction** Show the EM images and provide a description of the fibrillar morphology. State the conditions under which the aggregates were formed.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion
- **Evidence pointer** Discussion
- **Issue** The discussion of the functional implications of the distinct assembly mechanisms is speculative and not directly supported by the data. The statement that the "orientation of bound RNAs" may differ between FUS and TDP-43 assemblies is not tested experimentally.
- **Required correction** Clearly distinguish between conclusions supported by the data and speculative interpretations. Consider removing or softening the speculative statements.

## Risk / unsupported claims
- The claim that nMS can observe proteins "in liquid droplets" is not directly supported; the MS signal loss at pH 7.5 could be due to non-specific aggregation or precipitation.
- The claim that NT*-FUS undergoes an "unfolded-to-globular transition" is based on indirect MS measurements and is not validated by other structural methods.
- The claim that NT*-TDP-43 forms "partially disordered dimers and trimers" is based on indirect MS measurements and MD simulations that are not fully described or validated.
- The claim that the NT* tag does not affect the assembly behavior of the hRNPs is not supported by direct comparison with untagged proteins.
- The MD simulations for FUS (single 500 ns run) and TDP-43 (coarse-grained) are not demonstrated to be converged, and the results are not presented in sufficient detail to evaluate their validity.
- The claim that hCPEB3 "favors aggregation over LLPS" is based on qualitative observations and lacks quantitative comparison with FUS and TDP-43.
- The functional implications discussed (e.g., "vectorial channeling" for hCPEB3) are speculative and not supported by experimental evidence in this manuscript.