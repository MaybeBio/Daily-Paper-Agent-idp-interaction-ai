## Review setup
- **Input scope** Full manuscript text including abstract, results, discussion, methods, and supplementary figure legends
- **Assessment boundary** Scientific content, methodological rigor, and claims as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors report that HOPS condensates formed by DCP1A under hyperosmotic stress exhibit predominantly sub-diffusive motion due to ER tethering, with rare (~2%) super-diffusive events mediated by microtubule-dependent active transport. They further claim that the cytoplasm remains accessible and non-corralled during hyperosmotic compression, based on GEM particle tracking.
- **Visible evidence base** Main figures 1, 2, 4, and 5 (as referenced in text); supplementary figures S1–S7 (legends only); methods section
- **Missing materials affecting confidence** Actual figure images and data values; supplementary figure content; statistical details (exact n, effect sizes, confidence intervals); raw trajectory data; details of GEM particle characterization; control experiments for ER perturbation specificity

## Reviewer

- **Overall assessment** This manuscript addresses an important and timely question regarding the physical environment and dynamics of biomolecular condensates under hyperosmotic stress. The authors present a compelling narrative that challenges the prevailing view of a static, corralled cytosol during osmotic compression. The combination of extended single-particle tracking, pharmacological perturbations, and GEM-based accessibility mapping is innovative and well-suited to the question. However, several technical concerns must be addressed before the central claims are fully established, particularly regarding the interpretation of sub-diffusion as ER tethering, the robustness of the super-diffusion detection, and the quantitative rigor of the accessibility measurements.

- **Who would be interested in the results, and why** Researchers in the fields of phase separation, cell biophysics, intracellular transport, and stress biology would find these results of interest. The work also has relevance for understanding the physical organization of the cytoplasm under physiological stress conditions, which is of broad interest to cell biologists and biophysicists. The methodological advances in long-timescale tracking and GEM-based mapping may also appeal to method developers.

- **Major strengths** The study addresses a significant gap in understanding condensate dynamics under osmotic stress. The extended imaging approach (6.5 min) is a clear improvement over previous short-timescale studies. The combination of multiple complementary techniques (SPT, pharmacological disruption, dual-color imaging, GEM mapping, holotomography) provides converging evidence. The distinction between constrained and confined diffusion is conceptually important and well-articulated.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that sub-diffusion of HOPS condensates is caused by ER tethering, based on colocalization and thapsigargin experiments.
- **Evidence pointer** Figure 4, Methods section "Colocalization quantification" and "Boundary detection and segmentation"
- **Concern** The evidence for ER tethering as the causal mechanism for sub-diffusion is largely correlative. The Manders' coefficient of ~0.4 indicates partial overlap but does not demonstrate physical tethering. The thapsigargin experiment shows reduced displacement but this could result from general cellular stress responses rather than specific disruption of ER-condensate interactions. No direct evidence of physical attachment (e.g., FRAP, optical trapping, or high-resolution imaging) is provided.
- **Why it matters** The central mechanistic claim of the paper rests on this causal link. Without direct evidence of physical tethering, alternative explanations (e.g., increased cytoplasmic viscosity, altered condensate material properties) cannot be excluded.
- **Resolution test** Provide direct evidence of physical ER-condensate attachment, such as FRAP showing fluorescence recovery kinetics consistent with tethering, or demonstrate that thapsigargin treatment specifically disrupts ER-condensate contacts while leaving other cellular properties unchanged. Alternatively, perform a rescue experiment or use an orthogonal approach to disrupt ER-condensate interactions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that only ~2% of HOPS condensate trajectory steps exhibit super-diffusion, and that this represents active transport along microtubules.
- **Evidence pointer** Figure 1g, Figure 2, Methods section "Super-diffusive event detection"
- **Concern** The detection of super-diffusive events relies on threshold-based criteria (step size, displacement, alpha, D) that may be sensitive to noise and tracking errors. The manuscript does not report the false-positive rate of this detection method, nor does it validate the approach on simulated trajectories with known diffusion properties. The claim that Nocodazole completely abolishes super-diffusion is based on a single pharmacological perturbation, and the statistical power of this comparison is not reported.
- **Why it matters** The super-diffusion events are a key novel finding. If the detection method is not robust, the ~2% estimate and the microtubule-dependence claim may be unreliable.
- **Resolution test** Validate the super-diffusion detection on simulated trajectories with known diffusion modes. Report the false-positive and false-negative rates. Provide statistical details (n, effect sizes, confidence intervals) for the Nocodazole comparison. Consider using an independent method (e.g., kymograph analysis of directed motion) to confirm the super-diffusion events.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the cytoplasm remains accessible and non-corralled during hyperosmotic compression, based on GEM particle tracking.
- **Evidence pointer** Figure 3, Methods section "Spatial analysis and distance measurements"
- **Concern** The GEM particle analysis is used to argue against physical corralling, but the manuscript does not provide sufficient detail on GEM particle characterization (size, charge, interactions with cellular components) or on the statistical comparison between GEM and condensate mobility. The statement that GEMs exhibit "unrestricted diffusion" is qualitative, and the density map reconstruction (Figure 3b) may be biased by the technical difficulty of detecting GEMs near condensates, as acknowledged in the text.
- **Why it matters** The claim that the cytoplasm remains accessible is a major conceptual point that challenges existing models. If the GEM data are not quantitatively robust, this claim is weakened.
- **Resolution test** Provide quantitative comparison of GEM and condensate diffusion coefficients, including size-matched analysis. Report the detection efficiency of GEMs in different cytoplasmic regions. Consider using an alternative probe (e.g., different-sized nanoparticles) to confirm the accessibility finding.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors generalize their findings from DCP1A to "condensates" broadly, and suggest implications for nuclear condensates and gene regulation.
- **Evidence pointer** Discussion section
- **Concern** The study is performed on a single model protein (DCP1A) in a single cell type (U2OS). The generalization to other HOPS-forming proteins and to nuclear condensates is speculative. The relevance to gene regulation is mentioned but not experimentally addressed.
- **Why it matters** The broader significance of the work depends on the generality of the findings. Without evidence from additional systems, the claims may be overextended.
- **Resolution test** Acknowledge the limitations of single-protein analysis in the discussion. If possible, provide preliminary data on at least one additional HOPS-forming protein or cell type to support generality.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Background section
- **Evidence pointer** Background, first paragraph
- **Issue** The background assumes familiarity with phase separation terminology and the specific context of hyperosmotic shock in kidney physiology. Nonspecialist readers may struggle to understand the significance of the problem.
- **Required correction** Provide a brief explanation of why hyperosmotic shock is physiologically relevant and why condensate dynamics matter, with minimal jargon.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, "Super-diffusive event detection"
- **Evidence pointer** Methods section
- **Issue** The criteria for super-diffusion detection are described, but the rationale for the specific thresholds (e.g., 2 pixels, 5 pixels) is not provided.
- **Required correction** Justify the threshold choices or cite prior work using similar criteria.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Figure 2b, statistical analysis
- **Evidence pointer** Figure 2b
- **Issue** The statistical test used (Welch's t-test with Bonferroni correction) is appropriate, but the number of cells/condensates analyzed is not reported in the text.
- **Required correction** Report n values and effect sizes for all statistical comparisons.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Discussion, paragraph on ANXA11
- **Evidence pointer** Discussion section
- **Issue** The comparison with ANXA11-mediated hitchhiking in neurons is interesting but may be unclear to readers unfamiliar with this system.
- **Required correction** Briefly explain the ANXA11 mechanism and its relevance to the current findings.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, "Cytoskeleton disruption"
- **Evidence pointer** Methods section
- **Issue** The concentrations and incubation times for Nocodazole and Latrunculin A are not provided.
- **Required correction** Include drug concentrations and treatment durations.

- **Technical failings that need to be addressed before the case is established** R1-M1 (causal link between ER and sub-diffusion), R1-M2 (robustness of super-diffusion detection), R1-M3 (quantitative rigor of GEM accessibility analysis)

- **Assessment against Nature-style criteria**  
  *Originality*: The work is original in its focus on long-timescale dynamics of condensates under hyperosmotic stress and in its combination of techniques. The finding of dual-mode dynamics is novel.  
  *Scientific importance*: The results have the potential to reshape understanding of the physical environment during osmotic stress, which is relevant to kidney physiology and stress biology. However, the single-model-system approach limits the immediate impact.  
  *Interdisciplinary readership*: The work bridges biophysics, cell biology, and stress physiology, and should appeal to a broad audience. The methods are accessible, though some background in phase separation is assumed.  
  *Technical soundness*: The experimental design is generally sound, but the concerns above regarding causal evidence and quantitative rigor need to be addressed.  
  *Readability for nonspecialists*: The manuscript is generally well-written, but the background and discussion could be more accessible to nonspecialists.

- **Recommendation posture** Supportive if technical concerns are resolved. The central claims are interesting and potentially important, but the causal link between ER tethering and sub-diffusion, the robustness of super-diffusion detection, and the quantitative basis for the accessibility claim need to be strengthened. If these concerns are adequately addressed, the manuscript would be suitable for publication.

## Risk / unsupported claims
- The claim that ER tethering is the causal mechanism for sub-diffusion is not fully supported by the correlative evidence presented.
- The generalization of findings from DCP1A to other HOPS-forming proteins and to nuclear condensates is speculative and not experimentally supported.
- The claim that the cytoplasm remains "accessible" during hyperosmotic compression is based on qualitative GEM data and requires quantitative validation.
- The relevance of the findings to gene regulation is mentioned but not experimentally addressed.
- The robustness of the super-diffusion detection method is not validated, and the false-positive rate is unknown.