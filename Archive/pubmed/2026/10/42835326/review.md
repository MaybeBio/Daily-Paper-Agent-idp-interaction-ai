## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, materials and methods, and figure legends
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors report that CDK1/Cyclin B phosphorylates the intrinsically disordered C-terminal domain of dynein light intermediate chain 2 (LIC2-C) at five primary sites without altering secondary structure propensity. Phosphorylation modulates long-range intramolecular contacts, selectively enhances BICD2 contacts with Helix-2, and enables high-affinity Pin1 binding, which in turn reduces BICD2 binding affinity while leaving SPDL1 and HOOK3 largely unaffected. The authors propose a phosphorylation-dependent, Pin1-mediated mechanism that tunes dynein-adaptor interactions.
- **Visible evidence base** NMR spectroscopy (HSQC, 3D triple-resonance experiments, PRE), mass spectrometry, microscale thermophoresis (MST), secondary structure propensity calculations, sequence alignments
- **Missing materials affecting confidence** Figures and supplementary figures referenced but not provided; raw NMR spectra; MST raw data and fit parameters; mass spectrometry raw data and spectra; experimental replicates for MST; details of NMR titration protocols; statistical analysis details

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question in dynein biology: how phosphorylation of the light intermediate chain 2 C-terminal domain regulates cargo-adaptor interactions. The combination of NMR-based structural analysis with binding assays is appropriate and potentially powerful. However, the manuscript as presented has several significant gaps in data presentation, quantitative analysis, and experimental rigor that prevent full evaluation of the claims. The central conclusions regarding Pin1-mediated modulation of adaptor binding are intriguing but require stronger quantitative support and clearer mechanistic evidence. The work is likely of interest to the dynein motor and intracellular transport communities, but the current evidence base is insufficient to fully establish the proposed model.

- **Who would be interested in the results, and why** Researchers studying cytoplasmic dynein regulation, microtubule-based motor proteins, cargo adaptor selectivity, and the role of post-translational modifications in motor protein function. The work also has relevance to those interested in intrinsically disordered proteins and their regulation by phosphorylation and prolyl isomerization. The potential connection to mitotic progression and dynein function during cell division would interest cell biologists studying mitosis.

- **Major strengths** The study addresses a poorly characterized isoform (LIC2) and fills a gap in understanding LIC2 C-terminal domain regulation. The combination of NMR and mass spectrometry for phosphorylation site identification is methodologically sound. The use of PRE to probe conformational changes upon phosphorylation is appropriate. The finding that Pin1 binds phosphorylated LIC2-C with submicromolar affinity and modulates BICD2 binding is novel and potentially significant. The comparison of three different adaptors provides useful specificity information.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors claim that phosphorylation of LIC2-C "selectively enhances BICD2 contacts with Helix-2" and that Pin1 binding "reduces BICD2's binding affinity" based on NMR peak intensity changes and MST measurements.
- **Evidence pointer** Figures 3, 4, 6; Table 2; Results sections "LIC2-C binds adaptors in regions of transient α-helical propensity" and "Pin1 binds phosphorylated LIC2-C but not unphosphorylated LIC2-C"
- **Concern** The quantitative basis for the claim that phosphorylation enhances BICD2 contacts with Helix-2 is not clearly established. The NMR peak intensity ratios shown in Figure 4G-I are described qualitatively, but no statistical analysis is provided. More critically, the MST data show a KD of 43.5 ± 22.3 μM for pLIC2-C+BICD2 in the presence of Pin1, which has a very large uncertainty (approximately 50% of the measured value). This large error makes the claimed "order of magnitude difference" between conditions unreliable. Additionally, the MST experiments with Pin1 present use a 1:100 ratio of pLIC2-C to Pin1, but the authors do not demonstrate that this ratio fully saturates the binding sites or that the observed KD changes are not due to competitive binding effects rather than conformational modulation.
- **Why it matters** The central mechanistic claim of the paper is that Pin1 binding to phosphorylated LIC2-C modulates adaptor interactions. If the quantitative binding data are unreliable, this conclusion is not supported. The large uncertainty in the key KD measurement undermines confidence in the proposed model.
- **Resolution test** Provide MST data with replicates and error analysis for each condition, demonstrate saturation of Pin1 binding at the concentration used, and show that the KD changes are statistically significant. Alternatively, provide an independent binding assay (e.g., ITC or SPR) to corroborate the MST results.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental design
- **Claim pointer** The authors state that "phosphorylation enables high-affinity binding of the peptidyl-prolyl isomerase Pin1" and that this binding is specific to phosphorylated LIC2-C.
- **Evidence pointer** Figure 5; Results section "Pin1 binds phosphorylated LIC2-C but not unphosphorylated LIC2-C"
- **Concern** The NMR experiments demonstrating Pin1 binding to pLIC2-C are performed with a heterogeneous population of phosphorylated species, as the authors acknowledge that "NMR reports the average behavior of such a heterogeneous population of in-vitro phosphorylated species." The manuscript does not clarify which specific phosphorylation sites are required for Pin1 binding. The authors identify five primary phosphorylation sites, but do not test which combinations of phosphosites are necessary or sufficient for Pin1 interaction. Furthermore, the claim that Pin1 does not bind unphosphorylated LIC2-C is based on the absence of significant spectral changes, but the authors do not provide a positive control demonstrating that the Pin1 preparation is active and capable of binding a known substrate under the same conditions.
- **Why it matters** Without identifying the specific phosphosites required for Pin1 binding, the mechanistic model remains incomplete. The heterogeneity of the phosphorylated sample complicates interpretation of the NMR data. A negative result for unphosphorylated LIC2-C requires a positive control to rule out inactive Pin1 preparations.
- **Resolution test** Generate LIC2-C mutants with individual or combinatorial phosphosite mutations (S-to-A) to identify the minimal requirement for Pin1 binding. Include a positive control for Pin1 activity, such as binding to a known phosphorylated peptide or protein.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Data interpretation
- **Claim pointer** The authors propose that phosphorylation "modulates long-range intramolecular contacts, especially in the segment spanning the Helices including the interhelical region" and that this leads to a conformational change where "the N-terminal region repositions to be closer to Helix 2 and the interhelical linker."
- **Evidence pointer** Figure 2B-D; Results section "Phosphorylation favors long-range contacts of Helix-2 but reduces those with Helix-1"
- **Concern** The PRE data are interpreted as evidence for a conformational change, but the interpretation is largely qualitative. The authors state that phosphorylation causes "less peak reduction in Helix-1 and more peak reduction in Helix-2," but no quantitative analysis of PRE rates or distance restraints is provided. The model shown in Figure 2D is speculative and not directly supported by the data. The authors do not discuss alternative explanations for the observed PRE changes, such as phosphorylation-induced changes in local dynamics or oligomerization state. Additionally, the claim that the N-terminal region "repositions" is not directly demonstrated by the PRE data, which only report distances from the spin label at position 396.
- **Why it matters** The proposed conformational change is central to the mechanistic model. If the PRE data do not robustly support a specific conformational rearrangement, the model is not established. The distinction between local dynamic changes and long-range structural reorganization has important implications for how phosphorylation regulates adaptor binding.
- **Resolution test** Provide quantitative PRE analysis with calculated distances or distance ranges for key residue pairs in both phosphorylated and unphosphorylated states. Include controls for potential oligomerization or aggregation effects. Consider additional experiments (e.g., SAXS, smFRET) to directly test the proposed conformational change.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Completeness
- **Claim pointer** The authors state that "the engagement of cargo adaptors BICD2 but not SPDL1 or HOOK3 is altered" by phosphorylation, and that Pin1 binding reduces BICD2 affinity while leaving SPDL1 and HOOK3 largely unaffected.
- **Evidence pointer** Figures 3, 4, 6; Table 2; Results sections on adaptor titrations and MST measurements
- **Concern** The manuscript does not provide a clear mechanistic explanation for why phosphorylation and Pin1 selectively affect BICD2 but not SPDL1 or HOOK3. The authors note that BICD2 and SPDL1 share a CC1 box while HOOK3 has a HOOK domain, but this does not explain the differential effect between BICD2 and SPDL1. The NMR data show that SPDL1 and HOOK3 binding to pLIC2-C is similar to unphosphorylated LIC2-C, but the MST data show a modest (though not statistically significant) change for SPDL1 in the presence of Pin1 (2.8 to 5.5 μM). The authors do not address whether this trend is biologically meaningful. The proposed model in Figure 7 is not well supported by the data.
- **Why it matters** The specificity of the Pin1 effect is a key aspect of the proposed regulatory mechanism. Without a clear explanation for why BICD2 is selectively affected, the biological significance of the finding is unclear. The model in Figure 7 implies a regulatory switch that favors some adaptors over others, but this is not directly demonstrated.
- **Resolution test** Provide additional experiments to test the specificity of the Pin1 effect, such as competition assays between adaptors, or mutagenesis of the BICD2 binding interface to identify residues that mediate the differential response. Discuss alternative models for how Pin1 could selectively modulate BICD2 binding.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The abstract states that "LIC-C of both LIC1 and LIC2 isoforms are largely intrinsically disordered" but the manuscript focuses exclusively on LIC2. The relevance of LIC1 is mentioned in the introduction and discussion but not experimentally addressed.
- **Required correction** Clarify in the abstract that the study focuses on LIC2, or provide a brief justification for why LIC1 findings are relevant to the LIC2-focused study.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 1
- **Evidence pointer** Figure 1D-G
- **Issue** The chemical shift perturbation data in Figure 1E are described as showing "significant" changes, but no threshold for significance is defined. The authors state that "the largest CSPs" are from specific residues, but the criteria for "largest" are not specified.
- **Required correction** Define the CSP threshold used to identify significant perturbations and provide the calculated CSP values for key residues.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Methodology
- **Affected element** MST measurements
- **Evidence pointer** Table 2; Methods section "MST binding measurements"
- **Issue** The MST measurements for pLIC2-C+Pin1 with adaptors use a 1:100 ratio of pLIC2-C to Pin1. The authors do not explain how this ratio was chosen or whether lower ratios were tested. The presence of high concentrations of Pin1 could potentially interfere with MST measurements through non-specific effects.
- **Required correction** Provide a rationale for the 1:100 ratio and include control experiments showing that Pin1 alone does not affect MST signals in the absence of pLIC2-C.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion, paragraph on Pin1 mechanism
- **Issue** The authors speculate that Pin1 may act as a "negative regulator" of BICD2 binding during mitosis, but no cellular experiments are presented to support this claim. The discussion goes beyond the in vitro data presented.
- **Required correction** Clearly distinguish between conclusions supported by the presented data and speculative implications for cellular function. Consider adding a paragraph on limitations of the in vitro approach.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods
- **Evidence pointer** Methods section "NMR spectroscopy"
- **Issue** The methods describe the NMR experiments but do not provide details on data processing parameters, such as the number of scans for 3D experiments, relaxation delays, or the software used for peak picking beyond what is mentioned.
- **Required correction** Provide complete NMR acquisition and processing parameters to allow reproducibility.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data availability statement
- **Evidence pointer** Data availability section
- **Issue** The data availability statement says "Data will be made available on request." For a study relying heavily on NMR and MST data, this is insufficient for transparency and reproducibility.
- **Required correction** Deposit NMR chemical shift assignments in BMRB (already mentioned for LIC2-C, but pLIC2-C assignments should also be deposited) and provide MST raw data as supplementary material.

## Risk / unsupported claims
- The claim that phosphorylation "selectively enhances BICD2 contacts with Helix-2" is based on qualitative NMR peak intensity comparisons without statistical analysis.
- The claim that Pin1 binding "reduces BICD2's binding affinity" by an order of magnitude is based on MST data with very large uncertainty (43.5 ± 22.3 μM).
- The proposed conformational model in Figure 2D is speculative and not directly supported by quantitative PRE analysis.
- The claim that Pin1 acts as a "negative regulator" during mitosis is not supported by any cellular or in vivo experiments.
- The statement that "phosphorylation enables high-affinity binding of Pin1" is supported by NMR data, but the specific phosphosites required for binding are not identified.
- The differential effect of Pin1 on BICD2 versus SPDL1 and HOOK3 is observed but not mechanistically explained.
- The manuscript claims that phosphorylation does not alter secondary structure propensity, but this is based on SSP calculations that may not be sensitive to subtle conformational changes in disordered proteins.