## Review setup
- **Input scope** Full manuscript text (review article)
- **Assessment boundary** Scientific content, technical accuracy, completeness of the review, and alignment with stated aims
- **Shared manuscript claim summary** The authors present a review of integrative approaches combining sparse NMR and EPR constraints with molecular dynamics simulations to assess structural dynamics of transcription factors, with emphasis on intrinsically disordered TFs and TF-DNA interactions.
- **Visible evidence base** Full text including introduction, three main sections (NMR/MD, EPR/MD, methodological considerations), outlook, figures (5), and references cited within text
- **Missing materials affecting confidence** Figure 1 and Figure 4 are referenced but not fully visible in the provided text; graphical abstract not accessible; full reference list not provided

## Reviewer
- **Overall assessment** This is a well-structured and readable review article that addresses a timely and important topic: the integration of sparse magnetic resonance constraints with molecular dynamics simulations to study transcription factor dynamics, particularly for intrinsically disordered proteins. The authors successfully convey the complementary nature of NMR, EPR, and MD approaches and provide useful illustrative examples from recent literature. The manuscript is generally clear and logically organized. However, several concerns arise regarding the depth of critical analysis, the balance of coverage across methods, and the specificity of methodological guidance. The review would benefit from a more critical appraisal of the limitations and pitfalls of the described approaches, as well as a clearer articulation of best practices for integration.

- **Who would be interested in the results, and why** Structural biologists, biophysicists, and computational chemists working on intrinsically disordered proteins, transcription factor dynamics, and protein-DNA interactions. The review is also relevant for researchers interested in hybrid experimental-computational approaches and those seeking practical guidance on combining NMR or EPR data with MD simulations. The methodological considerations section may appeal to practitioners entering this field.

- **Major strengths** 
  1. Clear and logical organization with a well-defined scope
  2. Good use of illustrative examples from recent literature (e.g., MAX, p53, Brinker)
  3. Effective explanation of the complementarity between NMR, EPR, and MD
  4. Accessible writing style suitable for nonspecialists
  5. Useful figures that visually convey key concepts

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** No
- **Axis** Critical analysis depth
- **Claim pointer** The review claims to provide an overview of recent developments and methodological considerations for integrating NMR, EPR, and MD simulations.
- **Evidence pointer** Sections 2, 3, and 4
- **Concern** The review is largely descriptive and celebratory in tone, with limited critical appraisal of the methods discussed. For example, the authors do not adequately address known challenges such as force field inaccuracies in MD simulations of IDPs, the potential for spin-label artifacts in both NMR and EPR experiments, or the risk of overfitting when sparse constraints are used to refine ensembles. The methodological considerations section lists limitations but does not critically evaluate how these limitations affect the reliability of conclusions drawn from integrated approaches.
- **Why it matters** A review in a methods-focused journal should provide readers with a balanced assessment of what can and cannot be concluded from these integrative approaches. Without critical evaluation, readers may overestimate the reliability of published results or misapply the methods.
- **Resolution test** The authors should add explicit discussion of known failure modes, systematic errors, and validation strategies for each integration approach. For example, how does one assess whether an MD-derived ensemble that reproduces sparse NMR data is unique or overfit? What are the known artifacts of MTSL labeling on IDP conformations?

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Coverage balance
- **Claim pointer** The title and introduction suggest balanced coverage of NMR and EPR integration with MD simulations.
- **Evidence pointer** Sections 2 and 3
- **Concern** The NMR/MD section is substantially longer and more detailed than the EPR/MD section. While the NMR section includes multiple detailed examples (MAX, p53, Brinker, Engrailed 2, HOX factors), the EPR section is comparatively brief and relies heavily on a single example (MAX:MAX). The authors do not adequately cover recent developments in EPR methodology for IDPs, such as pulsed dipolar spectroscopy advances, site-directed spin labeling strategies, or the use of Cu(II) labels beyond the one example shown.
- **Why it matters** The title promises balanced treatment of NMR and EPR approaches. The current imbalance may mislead readers about the maturity and breadth of EPR-MD integration approaches.
- **Resolution test** Expand the EPR section with additional examples from the literature, including different spin-labeling strategies, different types of EPR measurements (e.g., relaxation-based, lineshape analysis), and applications to other TFs or IDPs. Alternatively, revise the title and framing to accurately reflect the emphasis on NMR.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Methodological specificity
- **Claim pointer** Section 4 claims to highlight "selected methodological considerations regarding the combination of NMR and EPR with MD simulations."
- **Evidence pointer** Section 4
- **Concern** The methodological considerations are presented at a high level without specific, actionable guidance. For example, the discussion of maximum entropy approaches mentions the principle but does not explain practical implementation details, such as how to choose the strength of the experimental restraint, how to handle correlated restraints, or how to assess convergence. Similarly, the discussion of force field limitations is generic and does not reference specific recent developments (e.g., improved IDP force fields such as CHARMM36m or ff99SB-disp).
- **Why it matters** Readers seeking to apply these methods would benefit from concrete recommendations, such as which force fields are currently recommended for IDP simulations, how many replicas are typically needed, or what validation metrics should be reported.
- **Resolution test** Add specific, actionable guidance based on current literature. For example, provide a table comparing available force fields for IDP simulations, or a step-by-step outline of a typical integrative workflow with recommended parameters and validation steps.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Completeness of literature coverage
- **Claim pointer** The review claims to provide "a brief overview of recent developments" in integrative approaches.
- **Evidence pointer** Sections 2 and 3
- **Concern** The review appears to rely heavily on a limited set of examples, many from the authors' own work or close collaborators. While the examples are relevant, the review does not adequately cover the broader literature. For instance, there is no mention of recent work using chemical shift perturbations or residual dipolar couplings with MD, no discussion of enhanced sampling methods (e.g., metadynamics, replica exchange) combined with NMR data, and no coverage of the growing field of integrative modeling platforms such as the Integrative Modeling Platform (IMP) or Bayesian approaches beyond maximum entropy.
- **Why it matters** A review should provide a representative overview of the field. The current selection may give readers a skewed view of the state of the art and miss important methodological developments.
- **Resolution test** Expand the literature coverage to include a broader range of approaches and groups. Consider adding a table summarizing key studies with their methods, systems, and main findings.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2, paragraph on MAX
- **Evidence pointer** Figure 1
- **Issue** The description of Figure 1 is somewhat unclear regarding the relationship between the experimental and computed PRE effects. The text states "the match between both data sets is good" but does not specify what metric was used to assess this match or what level of agreement was achieved.
- **Required correction** Provide a brief explanation of how the comparison was quantified (e.g., correlation coefficient, RMSD) and what threshold was considered acceptable.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Section 2, paragraph on facilitated diffusion
- **Evidence pointer** Location not provided
- **Issue** The term "inchworm stepping" is used without definition or citation. While the analogy is evocative, it may not be clear to all readers what specific motion is being described.
- **Required correction** Add a brief explanation of the inchworm stepping mechanism or provide a citation to the original description.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 4, discussion of maximum entropy
- **Evidence pointer** Location not provided
- **Issue** The discussion of maximum entropy approaches mentions the principle but does not cite the key methodological papers or discuss recent developments such as the use of ensemble refinement with replica exchange or the combination of maximum entropy with Bayesian inference.
- **Required correction** Add citations to key methodological papers and briefly discuss recent developments in this area.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Section 3, EPR discussion
- **Evidence pointer** Figure 5
- **Issue** The text states that the crystal structure represents "only the energetic minimum" of the conformational ensemble, but this is an oversimplification. Crystal structures can capture conformations that are not global energy minima, and lattice contacts can influence the observed conformation.
- **Required correction** Rephrase to acknowledge that crystal structures represent one or more conformations that may not fully represent the solution ensemble.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section 4, paragraph on choosing methods
- **Evidence pointer** Location not provided
- **Issue** The paragraph on choosing methods is somewhat generic and could benefit from a decision-tree or summary table to help readers select appropriate methods for their specific system and question.
- **Required correction** Consider adding a summary table or flowchart comparing the suitability of NMR, EPR, and MD for different system sizes, timescales, and research questions.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Accuracy
- **Affected element** Section 2, discussion of PRE timescales
- **Evidence pointer** Location not provided
- **Issue** The text states that PREs can reveal "transient long-range contacts between different protein domains even if the contact time is short (ps-ns timescale)." This is somewhat misleading, as PREs are sensitive to populations and timescales in a more complex manner, and the effective timescale depends on the correlation time of the electron-nuclear interaction.
- **Required correction** Clarify the timescale sensitivity of PREs and note that the interpretation depends on the timescale of conformational exchange relative to the PRE timescale.

## Risk / unsupported claims
- The claim that the MAX:MAX conformational ensemble "could be verified" by the match between experimental and computed PRE effects (Section 2) is overstated. Agreement between experiment and simulation is necessary but not sufficient for verification, as multiple ensembles may reproduce the same sparse data.
- The statement that "NMR alone could not provide three-dimensional models of such dynamic systems in the absence of NOE constraints" (Outlook) is too absolute. Recent developments in NMR-based ensemble determination using chemical shifts, residual dipolar couplings, and paramagnetic restraints can provide structural models without traditional NOE constraints.
- The claim that EPR "is not size limited" (Section 4) is an oversimplification. While EPR does not suffer from the same size limitations as NMR, there are practical limitations related to spin-label mobility, deuteration requirements, and sensitivity at high molecular weights.
- The review implies that maximum entropy approaches are the primary or preferred method for integrating experimental data with MD simulations, but does not discuss alternative approaches (e.g., Bayesian inference, replica-averaged metadynamics) or their relative merits.
- The statement that "faster computers are valuable" (Outlook) is trivially true and does not add substantive insight. The authors could instead discuss specific computational bottlenecks and algorithmic developments that would have the greatest impact.