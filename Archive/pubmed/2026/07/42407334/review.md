## Review setup
- **Input scope** Full manuscript text (abstract, main text, data availability, acknowledgements)
- **Assessment boundary** Scientific content, methodological framing, and internal consistency of the review article as provided; no external literature verification performed
- **Shared manuscript claim summary** The authors review recent experimental and computational advances that link single-molecule properties of biomolecules to the emergent material properties of biomolecular condensates, and propose that integrating single-molecule and mesoscale measurements can reveal mechanistic principles connecting molecular sequence to macroscopic condensate behavior.
- **Visible evidence base** Full text of the review, including descriptions of experimental techniques (e.g., turbidity, sedimentation, micropipette aspiration, FRAP, microrheology, smFRET, FCS, NMR, cryo-ET, SAXS) and simulation methods (e.g., coarse-grained MD, direct coexistence simulations, CLOUD-FIT, Green–Kubo formalism, TRACE method), with figure references (Fig. 1a–f, 2a–f, 3a–f, 4a–e) but no figures or tables included in the provided material.
- **Missing materials affecting confidence** Figures and figure captions; reference list; any supplementary information; publication date is listed as 2026-07-07, which is in the future relative to typical review timelines, but this does not affect assessment of content.

## Reviewer
- **Overall assessment** This is a well-structured and clearly written review that covers a timely and important topic in the biomolecular condensate field. The authors successfully organize a large body of recent work into a coherent narrative that moves from bulk thermodynamic and dynamic measurements to single-molecule approaches and finally to emerging strategies for bridging scales. The review is likely to be useful to both newcomers and practitioners in the field. However, the manuscript would benefit from a more critical and quantitative treatment of the limitations of the methods discussed, and from a clearer articulation of which specific open questions the proposed integrative framework is expected to resolve. The claim that "emerging principles" are outlined is somewhat overstated given the descriptive nature of the synthesis.
- **Who would be interested in the results, and why** Researchers in the biomolecular condensate field, including experimental biophysicists studying phase separation, computational biologists developing coarse-grained models, and cell biologists interested in the functional consequences of condensate material properties. The review would also be of interest to method developers working on single-molecule techniques and to researchers entering the field who seek a broad overview of available tools and their complementarities.
- **Major strengths** The review provides a comprehensive and well-organized survey of both experimental and computational approaches, which is valuable given the multidisciplinary nature of the field. The authors make a deliberate effort to pair experimental and simulation methods for each class of property (thermodynamic, dynamic, single-molecule), which facilitates comparison and highlights complementarity. The discussion of caveats in microrheology (probe size effects, laser heating) and in coarse-grained simulations (accelerated dynamics, force field limitations) demonstrates awareness of technical pitfalls. The final section on linking scales, including the use of graph-theoretical representations and the Deborah number framework, offers a forward-looking perspective that is intellectually stimulating.
- **Major Concerns** The review is largely descriptive and does not critically evaluate the quantitative reliability or inter-method consistency of the measurements it surveys. The claimed "emerging principles" are not explicitly enumerated or critically assessed. The treatment of the relationship between single-molecule behavior and material properties remains at the level of assertion rather than demonstration, and the review does not identify specific testable predictions that would validate the proposed multiscale framework. Additionally, the discussion of NMR and atomistic simulations is brief relative to their potential contributions, and the limitations of coarse-grained models are mentioned but not systematically analyzed.
- **Minor Comments** Several technical terms are introduced without definition (e.g., "Deborah number" is mentioned but not explained for nonspecialist readers). The figure references are frequent but the figures themselves are not available for assessment, making it difficult to evaluate whether the visual content supports the text. The Data Availability statement is appropriate for a review article. The acknowledgements are standard.
- **Technical failings that need to be addressed before the case is established** The manuscript does not present original data, so the standard of technical validation applies to the accuracy of method descriptions and the soundness of the synthesis. No factual errors were identified in the method descriptions, but the review would be strengthened by a more explicit and critical comparison of results obtained from different methods (e.g., do Csat values from simulation agree with experiment across systems? do microrheology and FRAP report consistent dynamics?). Without such comparative analysis, the claim that these methods can be integrated to reveal mechanisms remains programmatic rather than demonstrated.
- **Assessment against Nature-style criteria**  
  *Originality*: The review is not original in the sense of presenting new data or a new theory, but it offers a somewhat distinctive organizational framework by pairing experimental and simulation methods across property classes. This is a modest but real contribution.  
  *Scientific importance*: The topic is of high importance to a growing community, and the review addresses a recognized gap in linking molecular and mesoscale descriptions. The importance is more in the synthesis than in new insights.  
  *Interdisciplinary readership*: The review is likely to appeal to a broad interdisciplinary audience, including biophysicists, computational chemists, and cell biologists. The writing is generally accessible, though some terms could be better defined.  
  *Technical soundness*: The descriptions of methods are accurate based on the text provided, and the authors appropriately note several technical caveats. However, the lack of critical quantitative comparison between methods weakens the technical depth.  
  *Readability for nonspecialists*: The review is clearly written and logically organized, but assumes familiarity with concepts such as phase diagrams, viscoelasticity, and coarse-grained modeling. Some terms (e.g., Deborah number, Kirkwood-Buff formalism) are used without explanation, which may limit accessibility for a general scientific audience.
- **Recommendation posture** Supportive if the authors address the concerns regarding critical synthesis and accessibility. The review is competent and useful, but it would benefit from a more analytical and less descriptive treatment of the literature, and from explicit articulation of the principles it claims to outline.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** No
- **Axis** Synthesis depth
- **Claim pointer** The abstract states that the review "outline[s] emerging principles that connect microscopic interactions to macroscale condensate properties."
- **Evidence pointer** Abstract; Section "Linking single-molecule behavior to macroscopic condensate properties"
- **Concern** The review describes a large number of methods and results but does not explicitly enumerate or critically evaluate the "emerging principles" it claims to outline. The final section asserts that a multiscale framework "provides a powerful framework for uncovering mechanisms" but does not specify what these mechanisms are, how they were derived, or what evidence supports them beyond individual examples.
- **Why it matters** A review that claims to identify principles should provide a clear synthesis that goes beyond summarizing individual studies. Without explicit articulation of these principles and the evidence for them, the review risks being a catalog of methods rather than a conceptual contribution.
- **Resolution test** The authors should add a subsection or table that explicitly lists the proposed principles, the evidence supporting each, and the open questions or limitations associated with each. This would transform the programmatic statement into a testable framework.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Critical comparison of methods
- **Claim pointer** The review states that "computed phase diagrams from simulations using residue-resolution level coarse-grained force fields have been able to achieve near quantitative agreement with experiments."
- **Evidence pointer** Section "Simulation Approaches" under "MEASUREMENT OF CONDENSATE THERMODYNAMICAL PROPERTIES"
- **Concern** The claim of "near quantitative agreement" is presented without specific examples, error estimates, or discussion of which systems and conditions this agreement holds for. Similarly, the review does not compare results obtained from different experimental techniques (e.g., Csat from turbidity vs. sedimentation) or different simulation methods (e.g., direct coexistence vs. CLOUD-FIT) to assess consistency.
- **Why it matters** For a review whose stated goal is to link molecular and mesoscale descriptions, the reliability and cross-validation of the underlying measurements are central. Without critical comparison, readers cannot judge the robustness of the field's current knowledge or the confidence that can be placed in the proposed integrative framework.
- **Resolution test** The authors should provide specific examples of quantitative agreement (or disagreement) between simulation and experiment, including error bars or ranges, and discuss any systematic discrepancies. They should also comment on whether different experimental methods yield consistent results for the same system.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Accessibility for nonspecialists
- **Claim pointer** The review is intended for a broad audience, as implied by its placement in a general structural biology journal and its stated goal of outlining principles.
- **Evidence pointer** Throughout; particularly Section "Linking single-molecule behavior to macroscopic condensate properties"
- **Concern** Several technical terms and concepts are used without definition or explanation, including "Deborah number," "Kirkwood-Buff formalism," "cloud point" (defined only in passing), and "Gaussian Cluster Theory." The review also assumes familiarity with the distinction between viscous and elastic moduli and with the concept of viscoelasticity.
- **Why it matters** The review's stated goal is to bridge scales and disciplines. If it is to be useful to researchers across fields, it must be accessible to those who are not already experts in rheology or statistical mechanics. Undefined jargon limits the readership and reduces the review's impact.
- **Resolution test** The authors should add brief definitions or intuitive explanations for technical terms when they are first introduced, or add a glossary. For example, the Deborah number could be explained as a dimensionless ratio of the material's relaxation time to the observation time, which determines whether a material behaves more like a solid or a liquid.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section "Linking single-molecule behavior to macroscopic condensate properties"
- **Evidence pointer** Location not provided
- **Issue** The phrase "information propagation within the condensate interior" is vague and could be interpreted in multiple ways (e.g., molecular signaling, structural communication, dynamic coupling).
- **Required correction** Clarify what is meant by "information propagation" in this context, or rephrase to be more specific (e.g., "how local molecular rearrangements propagate to affect global condensate properties").

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section "Simulation Approaches" under "MEASUREMENT OF CONDENSATE DYNAMICAL MATERIAL PROPERTIES"
- **Evidence pointer** Location not provided
- **Issue** The discussion of non-equilibrium simulation methods (shear, sinusoidal deformation) is brief and does not mention any specific software or implementation details, unlike the mention of REPTATE for Green–Kubo analysis.
- **Required correction** Consider adding a sentence on practical implementation or referencing specific studies that have used these methods, to guide readers who may wish to apply them.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Section "Simulation Approaches" under "MEASUREMENT OF CONDENSATE DYNAMICAL MATERIAL PROPERTIES"
- **Evidence pointer** Location not provided
- **Issue** The text mentions "G'(w)" and "G''(w)" in the experimental section but the simulation section refers to "G(t)" and "G'(w)" without consistently defining the relationship between time-domain and frequency-domain moduli.
- **Required correction** Briefly state that G'(w) and G''(w) are the frequency-dependent storage and loss moduli obtained from the Fourier transform of G(t), to maintain consistency with the experimental section.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract
- **Evidence pointer** Location not provided
- **Issue** The abstract is dense and lists many techniques without giving the reader a clear sense of the review's main takeaway or argument.
- **Required correction** Consider adding one sentence that states the central thesis or the most important conclusion of the review, to guide the reader's expectations.

## Risk / unsupported claims
- The claim that "emerging principles" connecting microscopic interactions to macroscale properties are outlined is not fully supported by the text, as these principles are not explicitly enumerated or critically assessed.
- The statement that coarse-grained simulations achieve "near quantitative agreement with experiments" for phase diagrams is presented without specific examples or error estimates, making it unverifiable from the provided material.
- The assertion that "recent experimental advances... have revealed that even single-component condensates exhibit pronounced architectural and dynamical heterogeneity" is plausible but is not accompanied by specific citations or data, so it cannot be evaluated from the provided text.
- The claim that the TRACE method "captures molecular behavior inside active condensates that sustain directed fluxes" is described without methodological detail, making it difficult to assess its validity or significance.
- The overall framing that integrating single-molecule and mesoscale measurements "will establish the missing connection between sequence-encoded interaction motifs and macroscopic condensate properties" is programmatic and not demonstrated by the review's content.