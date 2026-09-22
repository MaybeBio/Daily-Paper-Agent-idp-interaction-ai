## Review setup
- **Input scope** Full manuscript text, including abstract, main text, figures and figure legends, and author declarations.
- **Assessment boundary** Scientific content, technical soundness, clarity of argument, and support for claims as presented in the supplied material. Editorial or stylistic preferences are noted only where they affect comprehension.
- **Shared manuscript claim summary** The authors argue that integrating NMR spectroscopy and cross-linking mass spectrometry (XL-MS) provides a synergistic framework for characterizing protein dynamic conformations and interaction networks in living cells, overcoming the individual limitations of each method in resolution, molecular weight range, and throughput. They review applications across intrinsically disordered proteins, multi-domain proteins, and protein complexes, and propose future directions including hyperpolarized NMR, photo-cross-linking, organelle-resolved analysis, and AI-guided integrative modeling.
- **Visible evidence base** Abstract, Introduction, four main sections (technical foundations, IDPs, multi-domain proteins, protein complexes), Conclusions and Perspectives with four subsections, six figures with legends, CRediT statement, competing interests declaration, acknowledgments. Reference list not provided.
- **Missing materials affecting confidence** Reference list, figure files (only legends visible), any supplementary information, and details of specific experimental studies cited. Without the reference list, the provenance and quality of cited evidence cannot be verified.

## Reviewer
- **Overall assessment** This is a well-structured and clearly written review that addresses a timely and important topic: moving structural biology from in vitro reconstitution to in vivo characterization. The central argument, that NMR and XL-MS are complementary and can be integrated to study protein dynamics and interactions in cells, is sound and well articulated. The authors demonstrate a strong command of both techniques and their respective strengths and limitations. The review is likely to be of interest to structural biologists, biophysicists, and cell biologists. However, several concerns limit the current impact. The review is largely descriptive and programmatic, with limited critical evaluation of the actual successes and failures of the integrated approach. The figures, as described in legends, are mostly reproduced from prior work and do not add new conceptual value. The treatment of AI-guided integrative modeling is superficial and does not engage with the substantial methodological challenges. The claim of "high-throughput" in the title is not fully substantiated by the content, which focuses on relatively low-throughput, case-by-case studies. The manuscript would benefit from a more critical and quantitative assessment of what the NMR-XL-MS integration has actually delivered so far, and what specific bottlenecks remain.
- **Who would be interested in the results, and why** Structural biologists using NMR or mass spectrometry, researchers studying intrinsically disordered proteins and phase separation, cell biologists interested in protein behavior in native environments, and method developers in integrative structural biology. The review provides a useful conceptual framework and a survey of recent work that could help researchers in these fields identify opportunities for combining NMR and XL-MS in their own studies.
- **Major strengths**
  - Clear and logical structure that progresses from technical principles to applications across three protein classes, then to future directions.
  - Accurate and balanced description of the strengths and limitations of NMR and XL-MS individually, including molecular weight limits, labeling requirements, and resolution characteristics.
  - Effective articulation of the complementary nature of the two methods in terms of spatial scale (short-range dense vs. long-range sparse restraints) and temporal resolution.
  - Good use of specific examples, such as HMG-I/Y and hnRNP A1, to illustrate the integrated approach.
  - The discussion of quinary structure and the importance of the cellular environment is timely and relevant.
  - The future directions section, while speculative, identifies plausible and important areas of development.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Support for central claim
- **Claim pointer** The review claims that the integration of NMR and XL-MS "establishes a powerful synergistic framework" and "enables comprehensive characterization of protein dynamic conformations and interaction networks in native environments."
- **Evidence pointer** Sections "Intrinsically disordered proteins", "Multi-domain proteins", "Protein complexes"; Figures 3, 4, 5
- **Concern** The central claim of a powerful synergistic framework is asserted rather than demonstrated through critical evaluation. The examples provided, such as HMG-I/Y and hnRNP A1, show that XL-MS data can be used to refine or filter conformational ensembles, but the specific added value of NMR in these integrated studies is not clearly delineated. In several cases, the NMR contribution appears to be limited to providing starting structures or validating XL-MS results, rather than providing genuinely complementary dynamic information. The review does not critically assess cases where the integration failed, where NMR and XL-MS data conflicted, or where the combined approach did not outperform either method alone. Without such critical assessment, the claim of a "powerful synergistic framework" remains programmatic rather than evidence-based.
- **Why it matters** A review that asserts a methodological synergy without critically evaluating its actual achievements risks overstating the maturity of the approach. Readers, especially those considering adopting these methods, need to understand not only the potential but also the current limitations and failure modes. The scientific case for integration is plausible, but the evidence presented here is largely anecdotal and selected for success.
- **Resolution test** The authors should either (a) provide a more systematic and critical evaluation of published integrated NMR-XL-MS studies, including cases with limitations or conflicts, or (b) temper the claim to reflect that the framework is promising but not yet comprehensively validated. Specific quantitative outcomes, such as how many structures or ensembles have been determined by this integrated approach versus by single methods, would strengthen the case.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Support for "high-throughput" claim
- **Claim pointer** The title states "Going high-throughput" and the abstract claims the integration enables "high-throughput" characterization.
- **Evidence pointer** Title; Abstract; Sections "Technical foundations", "Intrinsically disordered proteins", "Multi-domain proteins", "Protein complexes"
- **Concern** The term "high-throughput" is used in the title and abstract, but the content does not substantiate this characterization. The examples described are detailed, case-by-case studies of individual proteins or complexes, requiring extensive sample preparation, isotope labeling, and specialized expertise. In-cell NMR remains limited by sensitivity and spectral resolution, and XL-MS, while more scalable, still requires extensive fractionation and mass spectrometry time. The review does not provide any quantitative information on throughput, such as the number of proteins or interactions that can be characterized per unit time, nor does it compare throughput with other methods such as AlphaFold-based screening or affinity purification-mass spectrometry. The future directions mention "single-cell-level applications" but this is speculative.
- **Why it matters** The title and abstract set an expectation of a methodological advance in throughput. If the content does not support this, readers may be misled about the current state of the art. The term "high-throughput" has a specific meaning in the life sciences, and using it loosely weakens the scientific precision of the review.
- **Resolution test** The authors should either provide quantitative evidence or a reasoned argument for how the NMR-XL-MS integration achieves higher throughput than alternative approaches, or revise the title and abstract to reflect the actual scope, such as "toward high-throughput" or "enabling in vivo structural studies."

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Depth of future directions
- **Claim pointer** The section "Conclusions and perspectives" claims that AI-guided integrative modeling will "transform our ability to resolve the true functional states of proteins inside cells."
- **Evidence pointer** Section "Multimodal integration and artificial intelligence augment"
- **Concern** The discussion of AI-guided integrative modeling is superficial. The authors state that experimental data will "serve as physical priors" and "guide deep learning correction of prediction errors," but they do not engage with the substantial methodological challenges. These include: how to represent conformational ensembles in a way that is compatible with deep learning architectures, how to handle the sparsity and heterogeneity of XL-MS data, how to avoid overfitting when integrating multiple data types, and how to validate models when ground truth is unavailable. The authors also do not cite specific existing work in this area, such as integrative modeling platforms (e.g., Integrative Modeling Platform, HADDOCK) or recent deep learning approaches for protein structure prediction that incorporate experimental restraints. The claim that this will "transform" the field is therefore not supported by a concrete discussion of how this transformation will occur.
- **Why it matters** The future directions section is a key part of a review's value, as it guides the field. A superficial treatment of AI-guided integrative modeling, which is one of the most active and promising areas, is a missed opportunity and may mislead readers about the maturity of these approaches.
- **Resolution test** The authors should expand this subsection to include: (a) a discussion of specific existing computational frameworks for integrative modeling, (b) a description of the key technical challenges with reference to recent work, and (c) a more measured statement of what is currently achievable versus what is aspirational.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility and evidence quality
- **Claim pointer** The review states that "recent proteome-scale XL-MS studies have revealed a substantial gap between annotated interactomes and experimentally validated interactions."
- **Evidence pointer** Section "XL-MS: an in vivo ruler for protein topology and interaction networks"; reference [10]
- **Concern** The reference list is not provided, so the specific proteome-scale XL-MS studies cited cannot be evaluated. More importantly, the review does not provide any quantitative information about this "substantial gap," such as the number of interactions annotated versus validated, the overlap between datasets, or the false positive rates. The claim is presented as a fact without supporting data. This is a testable claim that should be substantiated with specific numbers or at least a more detailed description of the studies.
- **Why it matters** The claim about the gap between annotated and validated interactomes is used to justify the need for experimental methods like XL-MS. If this claim is not properly supported, the rationale for the review's central argument is weakened.
- **Resolution test** The authors should provide specific quantitative information from the cited studies, such as the number of interactions identified, the validation rate, and the comparison with existing databases. If the reference list is added, the relevant data should be summarized in the text.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section "NMR: probing structural and dynamic ensembles at atomic resolution"
- **Evidence pointer** Paragraph on paramagnetic approaches
- **Issue** The sentence "Notably, when proteins exist in multiple conformational equilibria, paramagnetic effects can amplify the signal contributions from lowly populated states" is somewhat unclear. The mechanism by which paramagnetic effects amplify lowly populated states is not explained. This is a key point for understanding the power of NMR in studying dynamic ensembles.
- **Required correction** Add one or two sentences explaining the physical basis for this amplification, such as the r−6 distance dependence of PRE leading to preferential attenuation of signals from states where the paramagnetic center is closer to the observed nucleus, thereby enhancing the relative contribution of states where the center is farther away.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section "Intrinsically disordered proteins"
- **Evidence pointer** Paragraph on in-cell NMR of IDPs
- **Issue** The statement that "the conformational flexibility of IDPs confers unique NMR observational advantages inside cells" is made, but the subsequent explanation is brief. The point about rotational diffusion restriction being weaker for IDPs is correct, but the review could benefit from a more explicit comparison with folded proteins in the same cellular context.
- **Required correction** Expand slightly to explain that the faster tumbling of IDPs relative to folded proteins of the same molecular weight leads to slower transverse relaxation and thus sharper lines, which is the key advantage. This would make the argument more accessible to nonspecialists.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Accuracy
- **Affected element** Section "Multi-domain proteins"
- **Evidence pointer** Paragraph on in-cell NMR challenges
- **Issue** The phrase "sparse sampling and selective labeling strategies yield only limited NOE signals, which are far below the density required for de novo structure determination" is accurate but could be more precise. The review does not specify what "limited" means in quantitative terms, nor does it explain why selective labeling strategies are needed.
- **Required correction** Provide a brief explanation of why selective labeling (e.g., amino-acid-type-specific labeling) is used in in-cell NMR, and give an approximate number of NOE restraints that would be needed for de novo structure determination versus what is typically obtained in-cell.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section "Protein complexes"
- **Evidence pointer** Paragraph on STINT and 19F NMR
- **Issue** The description of the STINT approach is very brief and may be unclear to readers unfamiliar with the method. The sentence "the STINT approach enables selective observation of binary protein interactions in cells through sequential expression and labeling strategies" does not explain how the method works.
- **Required correction** Add one or two sentences describing the basic principle of STINT, such as the sequential expression of two proteins with different isotope labeling patterns, allowing the observation of the interaction by NMR.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Section "Conclusions and perspectives", subsection "Organelle-resolved cellular structural biology"
- **Evidence pointer** Paragraph on organelle-resolved analysis
- **Issue** The claim that "in recent years, through organelle isolation techniques, NMR has been applied to directly detect the structural states of proteins inside mitochondria" is not accompanied by any citation or specific example. This is a specific and notable claim that should be supported.
- **Required correction** Add a citation to a specific study demonstrating this application, or remove the claim if it cannot be supported.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section "Conclusions and perspectives", subsection "Rational cross-linker design"
- **Evidence pointer** Paragraph on cross-linker design
- **Issue** The statement that "NMR studies combined with computational simulation have shown that both the polarity and rigidity of cross-linkers influence the outcome of in-cell cross-linking experiments" is vague. The review does not specify which NMR studies or what the outcome was.
- **Required correction** Provide a specific example or citation, and briefly describe what was learned about how polarity and rigidity affect cross-linking efficiency or specificity.

## Risk / unsupported claims
- The claim of a "powerful synergistic framework" for NMR-XL-MS integration is asserted but not critically evaluated with quantitative evidence (R1-M1).
- The "high-throughput" characterization in the title and abstract is not supported by the content, which describes case-by-case studies (R1-M2).
- The claim that AI-guided integrative modeling will "transform" the field is not supported by a concrete discussion of methods or challenges (R1-M3).
- The claim about a "substantial gap between annotated interactomes and experimentally validated interactions" is not quantified (R1-M4).
- The claim that NMR has been applied to detect protein structures inside mitochondria is not cited (R1-m5).
- The claim that cross-linker polarity and rigidity influence in-cell cross-linking outcomes is not supported with specific examples (R1-m6).
- The statement that "photochemically induced dynamic nuclear polarization (photo-CIDNP) with various 19F probes promises to enhance sensitivity by several orders of magnitude" is not supported with a citation or quantitative estimate.
- The statement that "the integration of both methods holds promise for constructing complete catalytic cycle maps" is speculative and not supported by any demonstrated example.
- The statement that "combining NMR and XL-MS with single-molecule Förster resonance energy transfer and fluorescence correlation spectroscopy will enable validation of ensemble-averaged results at the single-cell level" is speculative and not supported by any demonstrated example.
- The overall claim that the integration "opens a new paradigm for high-throughput analysis of dynamic interactomes in native cellular environments" is not supported by the evidence presented, which shows limited, proof-of-concept applications.