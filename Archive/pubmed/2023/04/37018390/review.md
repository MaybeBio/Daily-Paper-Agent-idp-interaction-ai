## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary figure descriptions
- **Assessment boundary** Scientific claims, experimental evidence, computational methods, and interpretation as presented in the manuscript
- **Shared manuscript claim summary** The authors report a previously unknown oligomerization domain in the disordered linker of coronavirus nucleocapsid proteins, specifically a leucine-rich sequence forming trimeric coiled-coils, which contributes to liquid-liquid phase separation, is required for higher-order protein-nucleic acid complex assembly, and is conserved across coronaviruses
- **Visible evidence base** Sedimentation velocity analytical ultracentrifugation, dynamic light scattering, circular dichroism spectroscopy, molecular dynamics simulations, ColabFold structure predictions, mutational analysis of SARS-CoV-2 genomic databases, and fluorescence microscopy of phase-separated condensates
- **Missing materials affecting confidence** Raw sedimentation coefficient distributions, full CD spectra at all concentrations, complete MD simulation trajectories, supplementary figures S2-S17 referenced but not fully described, statistical details of global multi-method analysis, and raw data files deposited externally

## Reviewer
- **Overall assessment** This manuscript presents a compelling and well-integrated study identifying a novel oligomerization domain in the disordered linker of coronavirus nucleocapsid proteins. The combination of biophysical experiments, computational predictions, and genomic analysis provides strong evidence for the existence and functional relevance of this domain. The work addresses an important gap in understanding SARS-CoV-2 N-protein assembly mechanisms and offers a potential new target for antiviral intervention. However, several technical concerns regarding the interpretation of hydrodynamic data, the strength of the trimer assignment, and the generalizability of the findings warrant careful consideration before the conclusions can be fully accepted.

- **Who would be interested in the results, and why** Structural biologists studying viral nucleocapsid proteins and RNA packaging mechanisms would find this work directly relevant. Researchers investigating liquid-liquid phase separation in biological systems, particularly those focused on viral assembly, would benefit from the identification of a specific oligomerization motif contributing to LLPS. The conservation analysis across coronaviruses makes this relevant to virologists studying coronavirus evolution and pathogenesis. Pharmaceutical scientists interested in developing antiviral therapeutics targeting protein-protein interactions would also find the identified oligomerization interface attractive as a potential drug target.

- **Major strengths** The study employs a complementary array of biophysical techniques to characterize the oligomerization behavior of the linker region. The use of multiple independent methods including SV-AUC, DLS, and CD provides convergent evidence for the self-association behavior. The integration of computational predictions with experimental validation is well executed. The mutational analysis using the extensive GISAID database provides strong evolutionary evidence for the functional importance of the identified residues. The demonstration that the oligomerization motif is conserved across diverse coronaviruses significantly enhances the potential impact of the findings.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of trimer assignment
- **Claim pointer** The authors claim that the observed sedimenting species at approximately 1.31 S corresponds to a trimer of the NLRS peptide, based on comparison with theoretical s-values for dimer, trimer, and tetramer.
- **Evidence pointer** Results section, Figure 2A, hydrodynamic modeling description
- **Concern** The assignment of the oligomeric state as a trimer relies on comparison of the experimentally observed sedimentation coefficient with theoretical values calculated from hydrodynamic modeling. However, the manuscript does not provide sufficient detail on the hydrodynamic modeling parameters, including the treatment of the disordered regions flanking the helix, the assumed shape of the oligomer, and the hydration state. Disordered proteins and peptides often exhibit anomalous hydrodynamic behavior due to their extended conformations and high flexibility. The theoretical s-values of 1.04, 1.33, and 1.69 S for dimer, trimer, and tetramer, respectively, appear closely spaced, and the experimental value of 1.31 S could potentially be consistent with a mixture of oligomeric states or an elongated dimer. The authors should provide more rigorous validation of the trimer assignment, such as sedimentation equilibrium experiments to determine the molecular weight directly, or size exclusion chromatography coupled with multi-angle light scattering.
- **Why it matters** The identification of the oligomeric state as a trimer is central to the structural model proposed for the LRS self-association. If the oligomeric state is incorrectly assigned, the subsequent interpretation of the coiled-coil structure, the molecular contacts, and the functional implications would be compromised. The claim of a trimeric coiled-coil is a key novel finding of this work, and the evidence supporting this specific stoichiometry must be robust.
- **Resolution test** The authors should provide direct molecular weight determination from sedimentation equilibrium experiments at multiple rotor speeds and concentrations, or an alternative method such as SEC-MALS. Additionally, they should present a more detailed description of the hydrodynamic modeling, including sensitivity analysis to assumptions about the disordered regions and hydration.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Functional relevance in full-length protein context
- **Claim pointer** The authors claim that the LRS oligomerization domain contributes to LLPS and is required for the assembly of higher-order protein-nucleic acid complexes in the full-length N-protein.
- **Evidence pointer** Results section, Figures 8 and 9, discussion of T20 binding and T10 ligation experiments
- **Concern** While the peptide studies provide clear evidence for self-association of the isolated LRS, the demonstration that this domain functions similarly in the context of the full-length protein is less direct. The experiments with full-length N-protein rely on mutations (L222P and L222P/R226P) that are presumed to disrupt LRS oligomerization, but the authors do not demonstrate that these mutations specifically disrupt the LRS interaction without affecting other aspects of N-protein structure or function. The T10 ligation experiments show differences in sedimentation behavior, but the interpretation that this reflects LRS-mediated oligomerization is indirect. The authors should provide more direct evidence that the LRS domain mediates the observed effects in the full-length protein, such as cross-linking experiments followed by mass spectrometry to identify specific intermolecular contacts, or fluorescence resonance energy transfer experiments to monitor LRS-LRS interactions in the full-length protein.
- **Why it matters** The central claim of the manuscript is that this oligomerization domain is functionally important in the context of the virus. If the effects observed in the full-length protein cannot be unambiguously attributed to the LRS domain, the significance of the finding for understanding viral assembly is substantially weakened.
- **Resolution test** The authors should perform experiments that directly probe LRS-LRS interactions in the full-length protein, such as chemical cross-linking with mass spectrometry analysis, or introduce mutations that specifically disrupt the LRS interaction while preserving other functions and demonstrate that these mutations phenocopy the effects of the L222P mutations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative analysis of LLPS data
- **Claim pointer** The authors claim that the LRS contributes to LLPS based on temperature-dependent DLS experiments and microscopy observations of condensate formation.
- **Evidence pointer** Results section, Figure 9, optical microscopy imaging methods
- **Concern** The characterization of LLPS relies primarily on qualitative observations of condensate formation and temperature-dependent DLS measurements. The manuscript does not provide quantitative phase diagrams, measurements of saturation concentrations, or systematic characterization of the dependence of LLPS on protein concentration, salt concentration, or RNA concentration. The claim that the LRS contributes to LLPS would be strengthened by quantitative measurements comparing the phase behavior of wild-type N-protein with the LRS-disrupting mutants. Additionally, the microscopy images shown in Figure 9B are described but not shown in the provided text, making it difficult to assess the quality of the evidence.
- **Why it matters** LLPS is a complex phenomenon influenced by multiple factors, and the specific contribution of a single interaction domain needs to be quantitatively assessed. Without quantitative phase diagrams, it is difficult to determine whether the observed effects of the LRS mutations on LLPS are specific or reflect general perturbations of protein stability or solubility.
- **Resolution test** The authors should provide quantitative phase diagrams for wild-type and mutant N-proteins, including measurements of saturation concentrations and the dependence of LLPS on protein and RNA concentrations. They should also include representative microscopy images with appropriate scale bars and quantification of droplet size distributions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of conservation analysis
- **Claim pointer** The authors claim that the oligomerization motif is conserved across related coronaviruses based on sequence alignment and the low mutation frequency in the LRS region of SARS-CoV-2 genomes.
- **Evidence pointer** Results section, Figure 7, mutational landscape analysis
- **Concern** The conservation analysis is based on sequence alignment of a limited set of coronaviruses and mutation frequency data from SARS-CoV-2 genomes. While the low mutation frequency in the LRS region is suggestive of functional importance, the authors do not provide a statistical framework to assess whether this conservation is significantly different from what would be expected for a disordered region of similar length. Additionally, the functional conservation is only demonstrated experimentally for the SARS-CoV-2 LRS peptide; the claim that the oligomerization behavior is conserved across coronaviruses is inferred from sequence conservation rather than demonstrated experimentally. The authors should either provide experimental evidence for oligomerization of LRS peptides from other coronaviruses or temper the claim of functional conservation.
- **Why it matters** The claim of conservation across coronaviruses is important for the potential development of broad-spectrum antiviral therapeutics. If the functional conservation is not experimentally demonstrated, the therapeutic implications are less certain.
- **Resolution test** The authors should either perform experiments with LRS peptides from other coronaviruses to demonstrate functional conservation, or revise the claim to indicate that the sequence conservation suggests but does not prove functional conservation.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 2B description
- **Evidence pointer** Results section, Figure 2B
- **Issue** The description of the DLS data in Figure 2B is somewhat unclear. The text mentions a two-species model representing clusters and the peptide signal, but the relationship between the hydrodynamic radius values and the oligomeric state assignment is not fully explained. The inset showing molecular weight estimates is mentioned but the derivation from the Svedberg equation is not described in sufficient detail.
- **Required correction** The authors should provide a more detailed explanation of the DLS data analysis, including how the two-species model was applied, how the hydrodynamic radius values were converted to molecular weights, and how the estimates relate to the expected values for monomer, trimer, and other oligomeric states.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** MD simulation parameters
- **Evidence pointer** Materials and Methods, MD simulations section
- **Issue** The description of the MD simulation parameters is brief. The manuscript mentions that simulations were carried out at 20°C and 1 atm with 150 mM NaCl, but does not provide details on the force field, water model, simulation box size, or the number of replicas. The reference to a previous study for additional details is helpful but the current manuscript should be self-contained for the key parameters.
- **Required correction** The authors should include the force field, water model, and other key simulation parameters in the methods section, or provide a more detailed summary of the simulation protocol.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical analysis
- **Affected element** GISAID mutation frequency analysis
- **Evidence pointer** Results section, mutational landscape analysis
- **Issue** The manuscript reports mutation frequencies in the LRS region but does not provide confidence intervals or statistical comparisons with mutation frequencies in other regions of the protein. The threshold of 10 observations for filtering sequencing errors is mentioned but the rationale for this threshold is not discussed.
- **Required correction** The authors should provide statistical context for the mutation frequency analysis, including confidence intervals and comparisons with other regions of the N-protein, to strengthen the claim that the LRS is unusually conserved.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 9B
- **Evidence pointer** Results section, Figure 9B
- **Issue** The microscopy images of condensate formation are described in the text but not shown in the provided material. The description mentions that condensates were observed for wild-type N-protein but not for the L222P mutant, but without seeing the images it is difficult to assess the quality of the evidence.
- **Required correction** The authors should ensure that representative microscopy images are included in the final manuscript with appropriate scale bars and that the differences between wild-type and mutant are clearly visible.

## Risk / unsupported claims
- The claim that the observed oligomerization is specifically trimeric is not fully supported by the hydrodynamic data alone; direct molecular weight determination is needed
- The claim that the LRS oligomerization domain is required for higher-order protein-nucleic acid complex assembly in the full-length protein is inferred from mutant studies that may have off-target effects
- The claim that the oligomerization motif is functionally conserved across coronaviruses is based on sequence conservation rather than direct experimental evidence for other coronaviruses
- The quantitative contribution of the LRS interaction to LLPS is not established, as no phase diagrams or saturation concentrations are provided
- The statement that the LRS presents a target for antiviral therapeutics is speculative and not supported by any direct evidence of druggability

## Assessment against Nature-style criteria
- **Originality** The identification of a specific oligomerization domain in the disordered linker of coronavirus N-proteins represents a novel finding. While previous work has suggested the importance of the linker region in N-protein function, the specific identification of a trimeric coiled-coil motif with functional consequences for LLPS and nucleic acid complex assembly is original. The integration of biophysical, computational, and genomic approaches to identify and validate this domain is innovative.
- **Scientific importance** The work addresses a fundamental question in coronavirus biology regarding the molecular mechanisms of N-protein assembly and RNA packaging. The identification of a new protein-protein interaction interface that is conserved across coronaviruses has implications for understanding viral assembly mechanisms and for the development of antiviral strategies. The finding that a disordered region can form a specific oligomeric structure with functional consequences is also of broader significance for understanding the role of disordered proteins in biological processes.
- **Interdisciplinary readership** The work bridges structural biology, biophysics, virology, and computational biology. The findings would be of interest to researchers in each of these fields, as well as to those studying liquid-liquid phase separation and its role in biological systems. The potential therapeutic implications would also attract interest from the drug discovery community.
- **Technical soundness** The experimental approach is generally sound, with appropriate use of multiple complementary biophysical techniques. However, the assignment of the trimeric state requires more rigorous validation, and the functional studies in the full-length protein would benefit from more direct evidence linking the observed effects to the LRS interaction. The computational methods are appropriate but could be more thoroughly described.
- **Readability for nonspecialists** The manuscript is generally well-written and accessible, with clear explanations of the biological context and the significance of the findings. The use of multiple techniques is explained in a way that nonspecialists can follow. However, some sections, particularly the hydrodynamic analysis, may be challenging for readers without a biophysics background. The figures are described clearly but the actual figures were not available for review.