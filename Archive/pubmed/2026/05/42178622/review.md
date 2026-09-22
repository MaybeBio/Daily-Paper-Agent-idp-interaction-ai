## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods, data availability)
- **Assessment boundary** Scientific validity, methodological soundness, reproducibility, and interpretation of the BioEmu-based SAXS ensemble modeling workflow as presented
- **Shared manuscript claim summary** The authors implement BioEmu, a generative deep-learning biomolecular emulator, as a sequence-based, physically informed prior for generating conformational pools in SAXS ensemble analysis. They demonstrate on CLIC5 and a cohort of 20 SASBDB entries that BioEmu-derived pools, combined with GAJOE selection, can fit experimental SAXS data with substantially smaller pool sizes (~1000 conformers) than standard EOM approaches, while providing physically plausible conformations.
- **Visible evidence base** Results sections with figures referenced (Figures 1-4, S1-S3), Table 1 and Table 2 referenced, methods descriptions, data availability statement with SASBDB accession codes
- **Missing materials affecting confidence** Figures and tables themselves are not provided; only their captions/references in text. Supplementary figures S1-S3 not available. Table 1 (cohort details) and Table 2 (SAXS data collection parameters) not available. No quantitative error bars or statistical tests described in text. No comparison of computational cost (time/resources) between BioEmu and RANCH beyond qualitative statements.

## Reviewer
- **Overall assessment** The manuscript presents a timely and potentially useful application of a generative deep-learning emulator to SAXS ensemble analysis. The core idea, using BioEmu as a physically informed prior for conformational pool generation, is conceptually appealing and addresses a recognized limitation of the standard EOM pipeline. The proof-of-concept on CLIC5 is well motivated, and the convergence analysis across five systems provides practical guidance on pool sizes. However, several technical aspects require clarification and additional validation before the case is fully established. The generalizability claim based on 20 SASBDB entries is weakened by the lack of quantitative comparison metrics and the absence of the actual data in the provided material. The manuscript would benefit from more rigorous statistical treatment and clearer reporting of computational costs.

- **Who would be interested in the results, and why** Structural biologists using SAXS to study flexible proteins and IDPs; computational biologists working on ensemble modeling methods; developers and users of deep-learning-based structure prediction tools; researchers interested in integrating generative models with experimental biophysical data. The work is relevant to the broad community of protein biophysics and structural bioinformatics.

- **Major strengths** 1) The conceptual advance of using a learned equilibrium prior for SAXS pool generation is novel and addresses a real bottleneck in the field. 2) The proof-of-concept on CLIC5 is well designed, leveraging prior experimental data to validate the approach. 3) The convergence analysis provides practical, actionable guidance on pool sizes. 4) The generalizability test across 20 diverse SASBDB entries is commendable in scope. 5) The authors appropriately emphasize that BioEmu provides a prior, not a final answer, and that experimental selection remains necessary.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "The unweighted BioEmu pool average did not reproduce the experimental scattering, indicating that EOM-guided selection remained necessary" and "BioEmu also generated elongated conformations with exposure of the interdomain interface ab initio"
- **Evidence pointer** Results section, Figure 2; location not provided
- **Concern** The manuscript reports a χ2 of 71.0 for the unweighted BioEmu pool average for CLIC5, which is extremely poor. While the authors use this to justify the need for GAJOE selection, this very poor fit raises questions about whether the BioEmu prior is capturing the correct physical landscape at all. The fact that GAJOE can select a subset that fits well (χ2 = 0.66) is expected, since GAJOE is designed to optimize fit. The key question is whether the BioEmu pool contains the correct conformations with sufficient diversity, or whether the good fit is achieved by selecting a few outliers that happen to match the data. The manuscript does not provide a comparison of the selected ensemble from BioEmu pool versus the selected ensemble from a RANCH pool in terms of physical plausibility, conformational diversity, or agreement with known structural features.
- **Why it matters** The central claim of the paper is that BioEmu provides a better prior than RANCH. If the unweighted BioEmu pool is so far from the experimental data, and the only evidence for its utility is that GAJOE can select a fitting ensemble, then the advantage over RANCH is not clearly demonstrated. The authors need to show that the BioEmu-derived selected ensemble is physically more plausible or more reproducible than what would be obtained from a RANCH pool of similar size.
- **Resolution test** Provide a direct comparison of selected ensembles from BioEmu and RANCH pools of equal size, using metrics such as ensemble-averaged Rg distributions, fraction of conformers with exposed hydrophobic surfaces, and agreement with any available experimental constraints beyond SAXS (e.g., cross-links, FRET). Additionally, show that the selected ensemble from BioEmu is stable across multiple GAJOE runs and that the fit quality is not achieved by selecting a small number of outlier conformers.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** "Convergence analysis across five distinct flexible protein systems showed that EOM fit quality plateaus at ~1000 BioEmu conformers pool"
- **Evidence pointer** Results section, Figure 3; location not provided
- **Concern** The convergence analysis is described qualitatively. The manuscript states that fit quality "plateaus" at ~1000 conformers, but no quantitative criteria for plateau are provided. What is the threshold for improvement? How much does χ2 change from 1000 to 5000 conformers? Is the plateau consistent across all five systems? The text mentions "triplicate" runs, but no error bars or standard deviations are reported. Without quantitative convergence criteria and variability estimates, the claim of "~1000 conformers" as a sufficient pool size is not rigorously supported.
- **Why it matters** The practical recommendation of ~1000 conformers is a key takeaway of the paper. If this number is not rigorously determined, users may under-sample or over-sample their pools, affecting the reliability of their ensemble models. The reproducibility of the workflow depends on clear guidance on pool size.
- **Resolution test** Report the actual χ2 values (mean and standard deviation from triplicates) for each pool size tested (50, 100, 1000, 2000, 5000) for all five systems. Define a quantitative plateau criterion (e.g., change in χ2 < 5% when pool size doubles). Show that the selected ensemble properties (e.g., Rg distribution) are also converged at the recommended pool size.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** "we demonstrate the generalizability of BioEmu implementation for SAXS analysis on a diverse cohort of 20 SASBDB entries, ranging from intrinsically disordered to multi-domain proteins"
- **Evidence pointer** Results section, Figure 4, Table 1; location not provided
- **Concern** The generalizability claim is based on 20 SASBDB entries, but the manuscript does not provide quantitative results for this cohort. No χ2 values, no comparison to published results, no details on how "fit quality comparable to the published analyses" was assessed. Table 1 is referenced but not provided. The text states "systematic differences from the published Rg distributions" but does not describe the nature or magnitude of these differences. Without this data, the generalizability claim is not verifiable.
- **Why it matters** The title and abstract emphasize the broad applicability of the method. If the cohort results are not presented with sufficient detail, the reader cannot assess whether the method works across the claimed diversity of systems or only for specific cases.
- **Resolution test** Provide Table 1 with all 20 entries, including protein name, type (IDP, multi-domain, etc.), length, published χ2, and BioEmu-EOM χ2. Show a scatter plot or table comparing published vs. BioEmu-EOM Rg distributions. Report any cases where the BioEmu-EOM fit was significantly worse than published results and discuss possible reasons.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "BioEmu sampled compact and rare elongated, interface-exposed conformations ab initio"
- **Evidence pointer** Results section, Figure 2; location not provided
- **Concern** The claim that BioEmu sampled "rare elongated, interface-exposed conformations" is based on visual inspection of Figure 2, which is not provided. The manuscript does not quantify how rare these conformations are, nor does it provide any validation that these conformations are physically meaningful (e.g., by comparison to known structures, mutational data, or other biophysical measurements). The term "interface-exposed" is not defined in the text.
- **Why it matters** The ability to sample rare but functionally relevant conformations is a key advantage claimed for BioEmu. Without quantitative evidence and validation, this claim remains anecdotal.
- **Resolution test** Quantify the fraction of BioEmu-generated conformations in the elongated state (e.g., Rg > 28 Å) and compare to the fraction in the RANCH pool. Provide structural analysis of the interface-exposed conformations, such as solvent-accessible surface area of the interface residues, and discuss whether these conformations are consistent with any experimental data (e.g., mutagenesis, cross-linking).

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "BioEmu offers a prior that often assigns high probability to compact, native-like states while still sampling rarer elongated conformations"
- **Evidence pointer** Discussion section; location not provided
- **Concern** The manuscript does not provide a systematic comparison of the BioEmu prior distribution to the RANCH prior distribution across the test systems. The claim that BioEmu assigns "high probability to compact, native-like states" is only supported by the CLIC5 example. It is unclear whether this is a general property of BioEmu or specific to CLIC5. Additionally, the manuscript does not discuss how the BioEmu prior distribution depends on the training data or whether it might be biased toward certain fold classes.
- **Why it matters** The central premise of the paper is that BioEmu provides a better prior than RANCH. This claim needs to be supported by systematic comparison across diverse systems, not just a single proof-of-concept.
- **Resolution test** For all five convergence test systems and the 20 SASBEX entries, compare the Rg distributions of the BioEmu pool, the RANCH pool, and the selected ensembles. Quantify the overlap between the BioEmu prior and the selected ensemble, and discuss whether the BioEmu prior consistently favors compact states across all systems.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states "BioEmu sampled compact and rare elongated, interface-exposed conformations ab initio" but does not define "interface-exposed" in the context of CLIC5. This term is ambiguous.
- **Required correction** Define "interface-exposed" in the abstract or rephrase to "conformations with exposed interdomain interfaces" for clarity.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Materials and Methods
- **Evidence pointer** Materials and Methods, "Conformational ensemble generation with BioEmu"; location not provided
- **Issue** The methods state that BioEmu was run with the "--filter_samples" option, but no details are given on the number of samples initially requested versus the number retained after filtering. This information is important for reproducibility and for understanding the effective pool size.
- **Required correction** Report the number of samples requested and the number retained after filtering for each system, or at least provide typical values.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, Convergence analysis
- **Evidence pointer** Results section, Figure 3; location not provided
- **Issue** The text states "In most cases, moving from 100 to 1000 conformers produced a clear reduction in χ2, whereas further expansion toward ~10,000 conformers yielded only marginal additional gains." The term "marginal" is subjective and not quantified.
- **Required correction** Provide the actual χ2 values for each pool size and define a quantitative threshold for "marginal" improvement.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion
- **Evidence pointer** Discussion section; location not provided
- **Issue** The discussion mentions "virtuous cycle" and "emulators provide scalable, interpretable ensemble hypotheses, while experiments provide the needed constraints to systematically improve the fidelity of the learned equilibrium distributions." This is an interesting idea but is not developed with concrete examples or future directions.
- **Required correction** Expand this point with a specific example of how SAXS data could be used to fine-tune the BioEmu prior, or remove the speculative language.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Data Availability
- **Evidence pointer** Data Availability Statement; location not provided
- **Issue** The data availability statement lists SASBDB accession codes for five in-house datasets but does not mention whether the BioEmu-generated pools and selected ensembles for the 20 SASBEX entries are available.
- **Required correction** State whether the BioEmu pools and selected ensembles for the 20 SASBEX entries are available and where they can be accessed.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, Generalizability
- **Evidence pointer** Results section, Figure 4; location not provided
- **Issue** The text states "the BioEmu-generated pools exhibited systematic differences from the published Rg distributions" but does not describe the nature of these differences. Are the BioEmu pools more compact, more extended, or shifted in some other way?
- **Required correction** Describe the systematic differences (e.g., "BioEmu pools were consistently more compact than published Rg distributions") and discuss possible reasons.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Introduction
- **Evidence pointer** Introduction; location not provided
- **Issue** The introduction states "the quality and interpretability of any ensemble solution hinges on pool generation" but does not cite specific examples of how poor pool generation has led to incorrect biological conclusions.
- **Required correction** Add a specific example or citation demonstrating the impact of pool generation on ensemble interpretation.

## Risk / unsupported claims
- The claim that BioEmu "captured the relevant conformational landscape" for the 20 SASBEX entries is not supported by quantitative data in the provided material.
- The claim that BioEmu "reduces the reliance on random sampling" is plausible but not directly demonstrated; no comparison of computational cost or sampling efficiency between BioEmu and RANCH is provided.
- The statement that BioEmu "may be better positioned to reflect sequence-encoded preferences in linker-mediated inter-domain organization" is speculative and not tested in this work.
- The claim that the selected ensembles are "physically viable" is based on the assumption that BioEmu's internal filtering ensures physical plausibility, but no independent validation (e.g., Ramachandran analysis, clash scores) is provided.
- The assertion that "fit quality comparable to the published analyses" was achieved for the 20 SASBEX entries is not verifiable without the actual χ2 values and comparison metrics.