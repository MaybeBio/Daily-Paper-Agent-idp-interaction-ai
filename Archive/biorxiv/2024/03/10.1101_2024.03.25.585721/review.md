## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no methods, figures, tables, or supplementary material were provided
- **Shared manuscript claim summary** The authors present a computational strategy, based on deep learning on molecular surface representations, for designing proteins that bind neosurfaces formed by protein-ligand complexes. They report experimental validation of designed binders against three drug-bound protein complexes, and claim that surface fingerprints trained only on proteins generalize to neosurfaces involving small molecules. They further suggest potential applications in sensing and synthetic biology.
- **Visible evidence base** Abstract text only; no experimental details, quantitative results, or methodological descriptions are available
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, experimental protocols, binding affinity data, structural validation data, and any statistical analyses

## Reviewer
- **Overall assessment** The abstract describes a conceptually interesting approach to a challenging problem in protein design, namely targeting protein-ligand neosurfaces. The claim of generalizability from protein-only training to small-molecule-containing surfaces is notable and, if substantiated, would represent a meaningful advance. However, the abstract alone provides insufficient evidence to evaluate the technical soundness, the robustness of the experimental validation, or the actual degree of generalizability. The central claims are plausible but currently not established from the supplied material.
- **Who would be interested in the results, and why** Researchers in computational protein design, deep learning for structural biology, and chemical biology would find these results relevant. Those working on chemically induced protein-protein interactions, biosensors, and synthetic cellular circuits would also be interested, as the approach could offer new routes to engineer small-molecule-responsive proteins.
- **Major strengths** The problem addressed is timely and of high interest. The use of learned molecular surface representations is a modern and appropriate technical choice. The claim of cross-domain generalizability, if true, is a strong and non-obvious result. Experimental validation against three drug-bound complexes, even if details are not provided here, suggests a commitment to real-world testing rather than purely computational benchmarking.
- **Major Concerns**  
  - **Concern ID** R1-M1  
    **Severity** Major  
    **Blocking** Yes  
    **Axis** Evidence sufficiency  
    **Claim pointer** The authors claim that "surface fingerprints trained only on proteins can be applied to neosurfaces emerging from small molecules, serving as a powerful demonstration of generalizability."  
    **Evidence pointer** Abstract; location not provided  
    **Concern** The abstract provides no quantitative or qualitative evidence supporting this generalizability claim. No metrics, comparisons, or benchmarks are described. It is unclear how generalizability was measured, what baselines were used, or whether the three validated examples are representative or exceptional.  
    **Why it matters** The generalizability claim is the central scientific contribution of the work. Without supporting evidence, the claim is unsupported and cannot be assessed.  
    **Resolution test** Provide quantitative results, such as success rates, binding affinities, or structural validation data, and compare against appropriate baselines or alternative methods.  
  - **Concern ID** R1-M2  
    **Severity** Major  
    **Blocking** Yes  
    **Axis** Experimental validation  
    **Claim pointer** The authors state that they "experimentally validated binders against three drug-bound protein complexes."  
    **Evidence pointer** Abstract; location not provided  
    **Concern** No details are given on the nature of the validation, such as binding affinity measurements, structural characterization, or functional assays. The number of designed candidates tested, the hit rate, and the strength of the observed interactions are not reported.  
    **Why it matters** Experimental validation is the key evidence that the computational approach works in practice. Without details, the reader cannot judge the reliability or significance of the results.  
    **Resolution test** Describe the experimental methods, report quantitative binding data, and provide structural or functional evidence that the designed proteins bind the intended neosurfaces.  
  - **Concern ID** R1-M3  
    **Severity** Major  
    **Blocking** No  
    **Axis** Scope of validation  
    **Claim pointer** The authors imply that the approach is "generalizable" based on three examples.  
    **Evidence pointer** Abstract; location not provided  
    **Concern** Three examples, even if successful, constitute a very small sample size. The abstract does not indicate whether these were selected from a larger set of designs, whether failures occurred, or whether the three complexes represent diverse chemical and structural contexts.  
    **Why it matters** Generalizability is a strong claim that requires evidence of breadth and consistency, not just a few positive cases.  
    **Resolution test** Report the total number of designs tested, the success rate, and the diversity of the target complexes in terms of ligand chemistry and surface topology.
- **Minor Comments**  
  - **Concern ID** R1-m1  
    **Severity** Minor  
    **Axis** Clarity  
    **Affected element** Terminology  
    **Evidence pointer** Abstract; location not provided  
    **Issue** The term "neosurfaces" is used without a formal definition. While the intended meaning is inferable, a precise definition would improve clarity.  
    **Required correction** Define "neosurface" explicitly, for example as the solvent-accessible surface region of a protein that is altered or created upon ligand binding.  
  - **Concern ID** R1-m2  
    **Severity** Minor  
    **Axis** Context  
    **Affected element** Related work  
    **Evidence pointer** Abstract; location not provided  
    **Issue** The abstract does not situate the work relative to existing approaches for designing proteins against protein-ligand complexes or for small-molecule-responsive protein design.  
    **Required correction** Add a brief statement in the abstract or introduction that distinguishes this approach from prior methods.  
  - **Concern ID** R1-m3  
    **Severity** Minor  
    **Axis** Application framing  
    **Affected element** Potential applications  
    **Evidence pointer** Abstract; location not provided  
    **Issue** The statement about "expanding the sensing repertoire and the assembly of new synthetic pathways" is speculative and not tied to any demonstrated functionality.  
    **Required correction** Either provide a concrete example of a demonstrated application or clearly label this as a future possibility.
- **Technical failings that need to be addressed before the case is established** R1-M1 and R1-M2 are blocking. The generalizability claim and the experimental validation are the core of the manuscript, and neither is supported by the abstract alone. Without quantitative results and methodological detail, the case is not established.
- **Assessment against Nature-style criteria**  
  - **Originality** The concept of targeting protein-ligand neosurfaces with deep learning on molecular surfaces appears novel and is not a trivial extension of existing protein surface design methods.  
  - **Scientific importance** If validated, the approach could enable new classes of chemically induced protein interactions, which would be of broad interest in chemical biology and synthetic biology.  
  - **Interdisciplinary readership** The work sits at the intersection of machine learning, structural biology, and protein engineering, and would appeal to readers across these fields.  
  - **Technical soundness** Cannot be assessed from the abstract. The deep learning methodology and the experimental validation are not described in sufficient detail.  
  - **Readability for nonspecialists** The abstract is concise and largely accessible, though the term "neosurfaces" and the nature of the deep learning approach may require some background knowledge.
- **Recommendation posture** Currently not established from the provided evidence. The scientific idea is promising and the direction is of interest, but the abstract does not provide the evidence needed to support the central claims. A full manuscript with detailed methods and results would be required for a proper evaluation.

## Risk / unsupported claims
- The claim that surface fingerprints trained only on proteins generalize to neosurfaces involving small molecules is unsupported in the abstract.
- The claim of experimental validation against three drug-bound complexes is unverifiable without details on methods and results.
- The statement that the designed interactions "hold the potential to expand the sensing repertoire and the assembly of new synthetic pathways" is speculative and not supported by any demonstrated functionality.