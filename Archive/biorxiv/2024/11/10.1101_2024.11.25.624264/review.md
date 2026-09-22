## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no evaluation of methods, figures, or statistical details beyond what is stated
- **Shared manuscript claim summary** The authors report that GKAP, a postsynaptic scaffold protein with two closely spaced noncanonical LC8 binding sites, forms a defined hexameric complex (2 GKAP molecules and 2 LC8 dimers). NMR data indicate that the LC8-binding segment is intrinsically disordered and that linker flexibility is largely retained in the complex. Molecular dynamics simulations suggest dynamically interchanging interactions beyond the tightly bound residues. The flanking regions of the two binding sites show different interaction patterns, which the authors propose may explain the fixed stoichiometry. The central claim is that constrained stoichiometry can coexist with substantial flexibility in a multivalent system.
- **Visible evidence base** Abstract text only; no figures, tables, methods, or supplementary materials provided
- **Missing materials affecting confidence** Full manuscript, experimental details (NMR acquisition and analysis parameters, MD simulation protocols and force fields), quantitative data (binding affinities, stoichiometry determination methods, error estimates), and any validation or control experiments

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting biophysical finding regarding the interplay between stoichiometric constraint and conformational flexibility in a multivalent protein complex. The claim that a defined hexamer forms despite intrinsic disorder and retained flexibility is conceptually appealing and could be of interest to structural biologists and biophysicists. However, the evidence base available for this review is limited to the abstract, and several key assertions, particularly the mechanism linking flanking region interactions to fixed stoichiometry, are presented without sufficient detail to assess their robustness. The work appears technically sound in its stated approach, but the strength of the conclusions cannot be fully evaluated from the supplied material.
- **Who would be interested in the results, and why** Structural biologists studying multivalent protein assemblies, biophysicists interested in intrinsically disordered proteins and their role in complex formation, and neuroscientists investigating postsynaptic scaffold organization. The finding that defined stoichiometry can coexist with conformational flexibility challenges simple models of multivalent assembly and may inform broader understanding of hub protein interactions.
- **Major strengths** The study addresses a conceptually important question about how multivalent systems achieve defined stoichiometry despite intrinsic disorder. The combination of NMR spectroscopy and molecular dynamics simulations provides complementary perspectives on both experimental and computational levels. The observation that flanking regions exhibit different interaction patterns is a specific and potentially mechanistically informative result.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract does not provide sufficient detail to assess the rigor of the stoichiometry determination, the NMR-based disorder and flexibility analysis, or the MD simulation methodology. Without these details, the central claim that constrained stoichiometry coexists with substantial flexibility cannot be fully verified.
- **Assessment against Nature-style criteria**  
  - Originality: The concept of flexibility coexisting with constrained stoichiometry in a multivalent system is not entirely novel, but the specific system and the proposed mechanism involving flanking region interactions may offer a fresh perspective.  
  - Scientific importance: The findings could have implications for understanding hub protein assemblies and scaffold organization, but the broader significance beyond this specific system is not clearly articulated in the abstract.  
  - Interdisciplinary readership: The topic bridges structural biology, biophysics, and neuroscience, which could attract a broad audience, but the abstract is written in a specialized manner that may limit accessibility.  
  - Technical soundness: The stated methods (NMR, MD) are appropriate, but the abstract lacks the detail needed to judge the quality of the implementation and analysis.  
  - Readability for nonspecialists: The abstract is concise but uses field-specific terminology (e.g., "noncanonical binding sites," "bivalent hub proteins") without sufficient context for a general scientific audience.
- **Recommendation posture** Supportive if technical concerns are resolved. The conceptual claim is interesting and potentially significant, but the current evidence base, limited to the abstract, does not allow full verification of the central conclusions. A complete manuscript with detailed methods and validation would be needed to establish the case.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** The authors claim that "a well-defined hexameric complex is formed, composed of 2 GKAP molecules and 2 LC8 dimers."  
- **Evidence pointer** Abstract, Summary section; location not provided  
- **Concern** The abstract states the hexameric stoichiometry as a finding but does not describe the experimental approach used to determine it (e.g., size exclusion chromatography, multi-angle light scattering, analytical ultracentrifugation, or NMR-based methods). Without this information, the reliability of the stoichiometry assignment cannot be assessed.  
- **Why it matters** The entire conclusion that constrained stoichiometry coexists with flexibility depends on the accuracy of the hexameric assembly model. If the stoichiometry determination is ambiguous or methodologically limited, the central claim is undermined.  
- **Resolution test** Provide a clear description of the stoichiometry determination method, including appropriate controls and error analysis, and demonstrate that the hexameric model is uniquely supported over alternative assemblies.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Claim support  
- **Claim pointer** The authors claim that "the flexibility of the linker region is largely retained even in the complex form" based on NMR spectroscopy.  
- **Evidence pointer** Abstract, Summary section; location not provided  
- **Concern** The abstract does not specify which NMR parameters were used to assess flexibility (e.g., relaxation dispersion, heteronuclear NOE, or residual dipolar couplings) or how the data were interpreted in the context of the complex. The term "largely retained" is qualitative and lacks quantitative support.  
- **Why it matters** The coexistence of flexibility and defined stoichiometry is a key conceptual contribution. If the flexibility assessment is not rigorously quantified or if the NMR data are consistent with alternative interpretations, the novelty of the claim is weakened.  
- **Resolution test** Present quantitative NMR parameters that directly report on backbone dynamics in the complex, compare them to the free state, and provide statistical measures of the difference to support the "largely retained" conclusion.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** No  
- **Axis** Mechanistic interpretation  
- **Claim pointer** The authors propose that "the flanking regions of the two binding sites on GKAP exhibit different interaction patterns, hinting at additional contacts that might explain the fixed stoichiometry of the assembly."  
- **Evidence pointer** Abstract, Summary section; location not provided  
- **Concern** The abstract presents this as a hypothesis ("hinting at," "might explain") but does not provide any direct evidence linking the observed interaction patterns to the stoichiometry. The causal relationship is speculative.  
- **Why it matters** This is the proposed mechanism for the central finding. Without experimental validation (e.g., mutagenesis of flanking regions and assessment of stoichiometry changes), the explanation remains unsupported.  
- **Resolution test** Provide experimental data, such as mutagenesis or cross-linking studies, that directly test the role of flanking region interactions in determining the hexameric stoichiometry.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Terminology  
- **Evidence pointer** Abstract, Summary section; location not provided  
- **Issue** The term "noncanonical binding sites" is used without explanation of what makes them noncanonical relative to known LC8 binding motifs.  
- **Required correction** Briefly define the noncanonical nature of the binding sites or provide a reference for the reader.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Simulation details  
- **Evidence pointer** Abstract, Summary section; location not provided  
- **Issue** The molecular dynamics simulations are mentioned but no details on simulation length, force field, or system setup are given.  
- **Required correction** Include key simulation parameters in the abstract or refer to the methods section for full details.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** General accessibility  
- **Affected element** Abstract readability  
- **Evidence pointer** Abstract, Summary section; location not provided  
- **Issue** The abstract assumes familiarity with hub proteins and scaffold biology, which may limit its accessibility to a broader scientific audience.  
- **Required correction** Add a brief contextual sentence explaining the significance of hub proteins and multivalent interactions in cellular processes.

## Risk / unsupported claims
- The claim that "constrained stoichiometry can coexist with substantial flexibility" is presented as a general principle but is only demonstrated for this specific system; the abstract does not provide evidence for broader applicability.
- The statement that "the LC8-binding segment of GKAP is intrinsically disordered" is stated as fact but the abstract does not describe how this was established (e.g., prediction algorithms, NMR chemical shift analysis, or other methods).
- The assertion that "the hexamer also exhibits several dynamically interchanging interactions" is based on MD simulations, but the abstract does not specify the criteria used to identify these interactions or their statistical significance.