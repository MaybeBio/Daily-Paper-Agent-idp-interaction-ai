## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, materials and methods, and supplementary figure legends as provided.
- **Assessment boundary** Scientific soundness, technical rigor, evolutionary and mechanistic claims, and alignment with Nature-style criteria. No assessment of editorial fit or publication decision.
- **Shared manuscript claim summary** The authors propose that isoform-specific variations in the C-terminal tail of DCLK family kinases, arising from alternative splicing, confer distinct autoinhibitory mechanisms. They identify an ATP-mimetic segment in DCLK1.2 that completes the catalytic spine and mimics the gamma phosphate of ATP upon phosphorylation, and they support this with phylogenetic analysis, molecular dynamics simulations, and in vitro mutational and biochemical assays.
- **Visible evidence base** Phylogenetic tree of 36 DCLK sequences; sequence alignments; exon-intron mapping; molecular dynamics simulations of DCLK1.1 and DCLK1.2 variants; thermal shift assays (DSF); peptide phosphorylation assays; LC-MS/MS phosphosite mapping; mutational analysis of contact residues.
- **Missing materials affecting confidence** No structural coordinates for MD starting models beyond PDB 6KYQ and AlphaFold2 predictions; no raw MD trajectory files or convergence metrics; no kinetic parameters (KM, Vmax) for all mutants in main text; no statistical details for phylogenetic branch support beyond bootstrap values; no raw mass spectrometry data or phosphosite localization scores; no cell-based functional validation.

## Reviewer
- **Overall assessment** This manuscript presents a compelling and integrative analysis of isoform-specific autoinhibition in DCLK kinases, combining evolutionary sequence analysis, computational modeling, and biochemical validation. The identification of an ATP-mimetic C-tail segment that completes the catalytic spine is novel and mechanistically insightful. However, several technical concerns regarding the robustness of MD simulations, the interpretation of mutational effects, and the generalizability of the "supercharging" concept require clarification before the case is fully established.
- **Who would be interested in the results, and why** Researchers studying kinase regulation, particularly CAMK family members and intrinsically disordered regions in signaling proteins. The work also appeals to those interested in the evolution of regulatory mechanisms and the design of kinase inhibitors or degraders targeting DCLK1 in cancer and neurodegeneration.
- **Major strengths** 1. Novel identification of an ATP-mimetic C-tail segment that completes the catalytic spine, providing a structural basis for autoinhibition. 2. Integration of phylogenetic, computational, and experimental approaches to address isoform-specific regulation. 3. Clear demonstration that alternative splicing generates functionally distinct autoinhibitory properties. 4. Mutational analysis effectively links specific residues to thermal stability and catalytic activity. 5. The "Swiss Army Knife" model is a useful conceptual framework for understanding multifunctional regulatory segments.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (MD simulation robustness), R1-M2 (mutational interpretation), R1-M3 (phosphorylation evidence), R1-M4 (evolutionary inference).
- **Assessment against Nature-style criteria** **Originality**: High. The ATP-mimetic concept for a C-tail segment is novel and extends beyond prior CAMK studies. **Scientific importance**: Moderate to high. DCLK kinases are understudied but clinically relevant; the findings may inform therapeutic strategies. **Interdisciplinary readership**: Moderate. The work bridges evolutionary biology, biophysics, and biochemistry, but the focus on one kinase family may limit broader appeal. **Technical soundness**: Generally sound but with concerns about MD simulation validation and the strength of phosphosite evidence. **Readability for nonspecialists**: Good. The manuscript is clearly written, with helpful figures and a logical flow, though some sections assume familiarity with kinase nomenclature.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding MD simulation validation, phosphosite evidence, and the generalizability of the "supercharging" model.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that MD simulations demonstrate stable docking of the C-tail in DCLK1.2 and instability in DCLK1.1, supporting differential autoinhibition.
- **Evidence pointer** Results section "Isoform-specific variations encode changes in MD, thermostability, and catalytic activity in DCLK1"; Figure 5; Figure 5—source data 1.
- **Concern** The MD simulations are described as 1-µs-long with three replicates, but no convergence metrics, RMSD plots, or free energy analyses are provided. The claim that the C-tail is "stably docked" in DCLK1.2 relies on qualitative RMSF comparisons. Additionally, the use of AlphaFold2 models for DCLK1.1 and DCLK1cat introduces potential bias, as these models may not accurately represent the conformational ensemble of the C-tail. The authors should provide quantitative measures of simulation convergence, such as RMSD over time, and ideally perform replicate simulations with different initial velocities to ensure reproducibility.
- **Why it matters** The central mechanistic claim hinges on differential C-tail dynamics between isoforms. Without robust MD validation, the conclusion that DCLK1.2 has a stably docked ATP-mimetic segment while DCLK1.1 does not is not fully supported.
- **Resolution test** Provide RMSD and RMSF plots with error bars across replicates, convergence analysis (e.g., block averaging), and possibly umbrella sampling or metadynamics to estimate binding free energies of the C-tail. If AlphaFold2 models are used, validate them against the crystal structure (6KYQ) and discuss potential limitations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that mutations in the C-tail (V682T/V684T, D691A) and G-loop (D398A, N400A) relieve autoinhibition, as evidenced by increased catalytic activity and reduced thermal stability.
- **Evidence pointer** Results section "Mutational analysis support isoform-specific allosteric control of catalytic activity by the C-terminal tail"; Figure 8B–D; Figure 8—figure supplement 1.
- **Concern** The mutational analysis is interpreted as evidence for physical uncoupling of the C-tail, but the data are largely correlative. For example, D398A and N400A mutations in the G-loop increase activity but do not reduce thermal stability, which the authors interpret as "compromised" rather than "uncoupled" interactions. However, no direct biophysical evidence (e.g., hydrogen-deuterium exchange, NMR, or SAXS) is provided to demonstrate C-tail uncoupling. Additionally, the KM[ATP] values for mutants are not consistently reported in the main text, making it difficult to assess whether increased activity is due to improved ATP binding or relief of autoinhibition.
- **Why it matters** The conclusion that specific mutations relieve autoinhibition by uncoupling the C-tail is central to the proposed model. Without direct evidence of conformational changes, alternative explanations (e.g., allosteric effects on the active site) cannot be excluded.
- **Resolution test** Perform direct binding assays (e.g., ITC or SPR) to measure C-tail affinity for the kinase domain in WT and mutants. Alternatively, use HDX-MS or NMR to compare conformational dynamics. Report KM[ATP] and Vmax for all mutants in the main text or supplement.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that phosphorylation of Thr 688 in DCLK1.2 mimics the gamma phosphate of ATP and stabilizes the autoinhibited state, based on MD simulations and published phosphoproteomics data.
- **Evidence pointer** Results section "An autoinhibitory ATP-mimic completes the C-spine and mimics the gamma phosphate of ATP"; Figure 7; Figure 7—figure supplement 1C.
- **Concern** The evidence for Thr 688 phosphorylation is indirect. The authors cite published phosphoproteomics data but do not experimentally validate phosphorylation of Thr 688 in their own system. The MD simulations of a phosphothreonine-containing DCLK1.2 are described, but no details on how the phosphorylation was modeled (e.g., force field parameters, protonation state) are provided. Furthermore, the functional significance of Thr 688 phosphorylation is not tested experimentally, despite the claim that it "mimics the gamma phosphate of ATP."
- **Why it matters** The proposed regulatory role of Thr 688 phosphorylation is a key aspect of the "supercharging" model. Without experimental validation, this claim remains speculative.
- **Resolution test** Generate phosphomimetic (T688E) and phosphodead (T688A) mutants and assess their catalytic activity, thermal stability, and ATP binding. Use mass spectrometry to confirm phosphorylation status in vitro or in cells. Provide details of MD simulation setup for phosphothreonine.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that the "supercharging" of DCLK1.1 catalytic activity, relative to DCLK1.2, is an evolutionarily selected feature that contributes to isoform-specific functions.
- **Evidence pointer** Results section "Origin and evolutionary divergence of DCLK family members"; Discussion section "Evolutionary divergence and functional specialization of DCLKs".
- **Concern** The evolutionary narrative is intriguing but speculative. The phylogenetic analysis shows that DCLK1 and DCLK2 diverged recently, and that the C-tail length varies, but the functional significance of this divergence is not directly tested. The claim that DCLK1.1 is "supercharged" relative to DCLK1.2 is based on in vitro assays, but the physiological relevance of this difference is unclear. No cell-based or in vivo experiments are presented to support the idea that isoform-specific autoinhibition is functionally important.
- **Why it matters** The title and abstract emphasize evolutionary insights, but the evidence for adaptive evolution is indirect. Overstating the evolutionary significance could mislead readers.
- **Resolution test** Perform ancestral sequence reconstruction or compare DCLK1/2 orthologs from diverse species to test whether the "supercharged" phenotype is conserved. Alternatively, express DCLK1.1 and DCLK1.2 in relevant cell lines and assess functional differences (e.g., microtubule binding, cell migration).

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The term "supercharging" is used without definition, which may confuse readers unfamiliar with the concept.
- **Required correction** Define "supercharging" early in the abstract or introduction, e.g., "we define supercharging as the enhanced catalytic output resulting from reduced autoinhibition."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Materials and methods, Molecular dynamics
- **Evidence pointer** Materials and methods section "Molecular dynamics"
- **Issue** The MD simulation parameters are described, but no information is provided on the number of ions added, salt concentration, or equilibration protocol details (e.g., NPT vs. NVT).
- **Required correction** Provide full simulation details, including ion concentration, equilibration steps, and any restraints applied.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 8
- **Evidence pointer** Figure 8D; Figure 8—figure supplement 1
- **Issue** Kinetic parameters (KM[ATP], Vmax) are mentioned but not fully reported for all mutants in the main text.
- **Required correction** Include a table summarizing KM[ATP] and Vmax for all WT and mutant proteins, or clearly reference the supplement.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion section "Discovery of the DCLK1 ATP-mimic region"
- **Issue** The authors suggest that the ATP-mimetic segment could be targeted by small molecules, but no docking or inhibitor studies are presented.
- **Required correction** Soften this claim or add a brief statement that this is speculative and requires future investigation.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1
- **Evidence pointer** Figure 1; Table 1
- **Issue** The nomenclature for DCLK1 isoforms (1.1–1.4) and the ΔDCLK1 variants may be confusing, especially for readers not familiar with the field.
- **Required correction** Add a schematic diagram in Figure 1 that clearly shows the domain organization and isoform differences, and consider a brief explanation in the legend.

## Risk / unsupported claims
- The claim that Thr 688 phosphorylation "mimics the gamma phosphate of ATP" is not experimentally validated and relies on indirect evidence from MD simulations and published data.
- The evolutionary significance of "supercharging" is inferred from phylogenetic patterns but not directly tested.
- The "Swiss Army Knife" model, while heuristic, is not fully supported by direct structural or biophysical evidence.
- The statement that DCLK1.1 is "supercharged" relative to DCLK1.2 is based on in vitro assays with recombinant proteins and may not reflect physiological conditions.
- The potential therapeutic implications for DCLK1 inhibitors are speculative and not supported by experimental data in this manuscript.