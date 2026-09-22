## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, materials and methods, and supplementary figure legends as referenced.
- **Assessment boundary** Scientific validity, technical soundness, reproducibility, and interpretation of results as presented. No assessment of editorial fit or publication policy.
- **Shared manuscript claim summary** The authors report that co-expression of the bacterial chaperone Trigger Factor enhances the solubility of recombinant HTLV-1 Tax protein fused to maltose-binding protein (MBP) in *E. coli*. A two-step purification strategy using a hexahistidine tag enables isolation of Tax from the MBP moiety after HRV 3C protease cleavage. The purified protein activates NF-κB in an in vitro assay, indicating functionality. AlphaFold2-based molecular dynamics simulations suggest three putative domains, which were expressed and purified in soluble form. The authors propose this work as a first step toward structural studies of Tax.
- **Visible evidence base** Figures 1-5, Supplementary Figures S1-S9, Table 1 (primers), Materials and Methods section. Figure legends are described in text but individual figure panels are not directly viewable.
- **Missing materials affecting confidence** Raw gel images, quantification data, molecular dynamics simulation parameters and trajectories, AlphaFold confidence metrics (pLDDT, PAE), and detailed purification yields are not provided. The NF-κB assay data are shown only as representative blots without replicates or quantification.

## Reviewer

- **Overall assessment** This manuscript addresses a practical and important problem: the production of soluble, functional recombinant HTLV-1 Tax protein for structural studies. The core observation that Trigger Factor enhances solubility of MBP-fused Tax is potentially useful and technically plausible. However, the evidence presented is largely qualitative, with limited quantification, no replicates shown, and several claims that extend beyond what the data directly support. The in silico domain prediction and subsequent expression of predicted fragments are interesting but preliminary, and the connection to the solubility mechanism is not rigorously established. The manuscript would benefit from more quantitative solubility assessments, replicate data, and a clearer demonstration that the purified protein is monomeric, properly folded, and suitable for structural studies.

- **Who would be interested in the results, and why** Researchers studying HTLV-1 biology, particularly those interested in Tax structure-function relationships, would find this protocol valuable. The broader community working on intrinsically disordered proteins and their recombinant production in bacterial systems would also be interested, as the use of Trigger Factor to improve solubility of a challenging protein is a generally applicable strategy. Structural biologists attempting to obtain Tax or similar proteins for crystallography, NMR, or cryo-EM studies would be the primary audience.

- **Major strengths**
  1. The problem addressed is significant and well-articulated: Tax is a key viral pathogenic factor, and its structural characterization has been hampered by insolubility.
  2. The use of Trigger Factor is a rational and potentially generalizable approach, building on established chaperone biology.
  3. The two-step purification strategy using MBP and a relocated hexahistidine tag is practical and clearly described.
  4. The functional validation via NF-κB activation is appropriate and includes a relevant negative control (M22 mutant).
  5. The combination of experimental solubility data with in silico domain prediction is a creative approach to guide future structural work.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "The bacterial chaperone Trigger Factor significantly enhances the solubility of HTLV-1 Tax fused to maltose-binding protein (MBP) as a solubility tag."
- **Evidence pointer** Figure 1C, 1D; location not provided
- **Concern** The claim of "significantly enhances" is not supported by quantitative data. The figures show representative gels, but there is no quantification of soluble versus insoluble fractions, no replicate experiments, and no statistical analysis. The improvement with Trigger Factor appears modest in the described results, particularly for the GST-Tax construct (Fig. 1C), where the text states only "slightly improved" solubility. For the MBP-Tax construct (Fig. 1D), the enhancement is described as "most pronounced," but again without quantification.
- **Why it matters** The central premise of the paper is that Trigger Factor enables soluble Tax production. Without quantitative solubility data across multiple independent experiments, the reader cannot assess the robustness or practical utility of this approach. A modest improvement that is not reproducible would undermine the main contribution.
- **Resolution test** Provide densitometric quantification of soluble versus insoluble fractions from at least three independent biological replicates, with statistical comparison between conditions with and without Trigger Factor. Report yields of purified protein per liter of culture.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "The purified recombinant protein activated NF-κB, indicating that the recombinant protein, solubilised by Trigger Factor, was functional."
- **Evidence pointer** Figure 3A-C; location not provided
- **Concern** The NF-κB activation assay is shown as a single representative experiment without replicates, quantification, or dose-response data. The text states that "equivalent amounts of cell lysate and the respective test protein were loaded," but no loading controls or protein quantification are shown. The M22 mutant negative control is appropriate, but the assay lacks a positive control (e.g., TNF-α stimulation) to demonstrate that the assay system is responsive.
- **Why it matters** Functional validation is critical to demonstrate that the solubilized protein is properly folded and biologically active. Without replicates and quantification, the reader cannot determine whether the observed IκB phosphorylation is robust, specific, and dose-dependent. This is particularly important given that Tax is known to be prone to aggregation, and the observed activity could be due to a minor properly folded fraction.
- **Resolution test** Perform the NF-κB assay with at least three independent protein preparations, include a dose-response curve, quantify phospho-IκB levels normalized to total IκB and loading controls, and include a positive control (e.g., TNF-α) to validate assay performance.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** "A molecular thermodynamics simulation, using a 3D model generated by AlphaFold2 as the initial state, suggested two putative domains within the Tax protein."
- **Evidence pointer** Figure 4C, 4D; location not provided
- **Concern** The molecular dynamics simulation is described in minimal detail. The methods state a 100 ns simulation with OpenMM and AMBER14SB, but no information is provided on the number of replicates, convergence criteria, equilibration protocol, or how the domain boundaries were determined from the distance fluctuation analysis. The claim of "two putative domains" (residues 1-95 and 100-240, with 250-320 also mentioned) is based on a single simulation trajectory, and the statistical significance of these domain boundaries is not assessed.
- **Why it matters** The domain prediction is used to design truncation constructs for subsequent experiments. If the simulation is not robust or the domain boundaries are not well-supported, the design of the truncation constructs may be flawed, and the interpretation of their solubility properties could be misleading.
- **Resolution test** Provide additional details on simulation setup, run at least three independent simulations to assess reproducibility, and use established methods (e.g., principal component analysis or dynamical network analysis) to validate domain boundaries. Alternatively, provide experimental validation of domain boundaries using limited proteolysis or hydrogen-deuterium exchange.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "These predicted domains could also be expressed and purified in the presence of exogenous Trigger Factor."
- **Evidence pointer** Figure 5A, 5B; location not provided
- **Concern** The solubility and purification of the three predicted domain fragments are shown, but the data are again qualitative. The text notes that the fragment spanning amino acids 95-322 showed "inefficient binding to the Ni-NTA resin," which is attributed to possible misfolding or aggregation, but no follow-up experiments are described to address this. The yields and purity of the fragments are not quantified.
- **Why it matters** The utility of the domain constructs for structural studies depends on their yield, purity, and monodispersity. The inefficient binding of one fragment suggests potential heterogeneity or aggregation, which would complicate structural analysis. Without quantitative assessment, the practical value of these constructs is unclear.
- **Resolution test** Provide yields and purity for each fragment, assess monodispersity using size-exclusion chromatography or dynamic light scattering, and optimize purification conditions for the problematic fragment.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** "Tax is potentially a heme-binding protein."
- **Evidence pointer** Figure 5C, 5D; location not provided
- **Concern** The observation of a brownish color in full-length Tax and the N-terminal domain (1-91) is intriguing, and the presence of CP motifs is noted. However, no direct evidence of heme binding is provided. The claim is speculative and based solely on color and sequence motifs. No spectroscopic analysis (e.g., UV-visible absorbance, pyridine hemochrome assay) or binding studies (e.g., heme titration, competition) are shown.
- **Why it matters** The heme-binding claim is presented as a significant finding, but the evidence is circumstantial. If heme binding is real, it could have important implications for Tax function and structure. However, without direct biochemical evidence, this claim is not established and could mislead readers.
- **Resolution test** Perform UV-visible spectroscopy on the purified protein to detect heme absorbance (Soret band around 400 nm), conduct a pyridine hemochrome assay to confirm heme content, and perform heme titration experiments to determine binding affinity and stoichiometry.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Materials and Methods, Protein expression
- **Evidence pointer** Section "Protein expression"; location not provided
- **Issue** The induction conditions for chaperone co-expression are described, but the concentrations of antibiotics used to maintain the chaperone plasmids are not specified. The copy number of the chaperone plasmids and the selection markers are also not stated.
- **Required correction** Specify antibiotic concentrations, plasmid copy numbers, and selection markers for all plasmids used.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Materials and Methods, Molecular dynamics simulation
- **Evidence pointer** Section "Molecular dynamics simulation"; location not provided
- **Issue** The simulation is described in a single paragraph with minimal detail. No information is provided on the solvation box size, salt concentration, temperature coupling method, pressure coupling method, or the number of steps for equilibration and production.
- **Required correction** Provide a complete description of the simulation parameters, including software version, force field parameters, water model, ion concentration, equilibration protocol, and production run length. Consider adding a supplementary methods section with full details.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, "Tax is potentially a heme-binding protein"
- **Evidence pointer** Figure 5C, 5D; location not provided
- **Issue** The text states that the brownish color was observed "during the preparation of these Tax fragments," but it is unclear at which step the color was noted and whether it was present in all preparations or only some.
- **Required correction** Clarify when the color was observed, whether it was consistent across preparations, and whether the color persisted after purification.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Materials and Methods, In vitro NF-κB activation assay
- **Evidence pointer** Section "In vitro NF-κB activation assay"; location not provided
- **Issue** The assay description states that "approximately 1 µM of test protein" was used, but the exact concentration is not specified, and no protein quantification method is described.
- **Required correction** Specify the exact protein concentration used and the method of quantification (e.g., Bradford, BCA, absorbance at 280 nm).

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, "Separation of Tax from the solubility tag"
- **Evidence pointer** Figure 2E; location not provided
- **Issue** The text states that Tax was eluted with 200 mM imidazole, but the purity of the final Tax preparation is not assessed beyond SDS-PAGE. It is unclear whether the protein is sufficiently pure for structural studies.
- **Required correction** Provide an assessment of purity (e.g., densitometry of the SDS-PAGE gel, mass spectrometry) and state the final yield.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Lack of quantitative solubility data
  - R1-M2: Lack of replicate and quantitative NF-κB assay data
  - R1-M3: Insufficient detail and robustness of molecular dynamics simulation
  - R1-M4: Lack of quantitative assessment of domain fragment purity and monodispersity

- **Assessment against Nature-style criteria**
  - **Originality** Moderate. The use of Trigger Factor to solubilize a challenging viral protein is not entirely novel, as chaperone co-expression is a known strategy, but its specific application to HTLV-1 Tax is new. The domain prediction approach is creative but not groundbreaking.
  - **Scientific importance** Moderate. The work addresses a practical bottleneck in Tax structural biology, which is important for understanding HTLV-1 pathogenesis. However, the findings are primarily methodological and do not yet provide new biological insights into Tax function or structure.
  - **Interdisciplinary readership** Limited. The primary audience is structural biologists and retrovirologists. The methods are specific to protein production and would not broadly appeal to other disciplines.
  - **Technical soundness** Currently insufficient. The lack of quantitative data, replicates, and detailed methods for the simulation undermines the technical rigor. The functional assay is appropriate but underpowered.
  - **Readability for nonspecialists** Acceptable. The manuscript is clearly written and the logic is easy to follow. However, some sections, particularly the domain prediction, assume familiarity with computational methods.

- **Recommendation posture** Currently not established from the provided evidence. The core claim of Trigger Factor-mediated solubility enhancement requires quantitative support. The functional validation needs replicates and quantification. The domain prediction is interesting but requires more rigorous simulation details and validation. The heme-binding claim is speculative and needs direct biochemical evidence. If these concerns are addressed with additional data, the manuscript could become a useful methodological contribution.

## Risk / unsupported claims
- The claim that Trigger Factor "significantly enhances" Tax solubility is not quantitatively supported.
- The claim that the purified protein is "functional" based on a single NF-κB assay without replicates or quantification is not fully established.
- The identification of "two putative domains" from a single molecular dynamics simulation is not robustly supported.
- The claim that Tax is "potentially a heme-binding protein" is speculative and not supported by direct binding data.
- The statement that the recombinant protein is suitable for structural studies is premature without assessment of monodispersity, aggregation state, or conformational homogeneity.