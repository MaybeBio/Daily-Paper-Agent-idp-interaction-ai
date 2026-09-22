## Review setup
- **Input scope** Full manuscript text (review article)
- **Assessment boundary** Scientific content, technical accuracy, completeness of methodological coverage, clarity of integration frameworks, and quality of illustrative examples
- **Shared manuscript claim summary** The manuscript argues that integrating single-molecule fluorescence spectroscopy (smFRET, FCS, nsFCS) with all-atom and coarse-grained simulations provides synergistic, complementary insights into the conformational behavior and dynamics of intrinsically disordered proteins (IDRs), and that this integration is essential for interpreting experimental data and uncovering molecular mechanisms.
- **Visible evidence base** Abstract, Introduction, Materials and Methods (sections on all-atom simulations, smFRET, FCS, integration approaches), Results (five subsections with case studies), Discussion, Conclusions, Acknowledgements
- **Missing materials affecting confidence** Figures and tables referenced (Figs. 1–6) are not provided; no supplementary information; no explicit statement of literature search strategy or inclusion criteria for cited studies; no detailed comparison of force field performance metrics beyond qualitative statements

## Reviewer
- **Overall assessment** This is a well-written, authoritative review that effectively synthesizes the state of the art in combining single-molecule spectroscopy with simulations for IDR research. The authors are clearly experts in the field, and the manuscript provides a valuable conceptual framework for integrative studies. The technical descriptions of smFRET, FCS, and simulation methods are accurate and appropriately detailed for a methods-oriented audience. The case studies are well chosen and illustrate the power of integration. However, the review would benefit from a more critical and quantitative treatment of the limitations of current integration approaches, particularly regarding force field accuracy, dye modeling, and the assumptions underlying polymer models. The absence of figures in the provided material limits full assessment of the pedagogical value.
- **Who would be interested in the results, and why** Biophysical chemists, computational biologists, and experimentalists studying intrinsically disordered proteins and protein conformational ensembles. The review is also relevant for method developers in single-molecule fluorescence and molecular simulation communities, as it highlights current challenges and future directions for integrative approaches. Graduate students and postdocs entering the IDP field would find this a useful entry point.
- **Major strengths** 1) Authoritative and comprehensive coverage of both experimental and computational techniques. 2) Clear articulation of the complementary strengths and limitations of smFRET and simulations. 3) Well-structured progression from methods to integration frameworks to illustrative case studies. 4) Thoughtful discussion of open challenges, including dye modeling and conformational sampling. 5) Balanced treatment of different integration strategies (direct comparison, explicit dye inclusion, reweighting).
- **Major Concerns** 1) The review lacks a critical quantitative assessment of force field accuracy for IDRs, despite acknowledging this as a key challenge. 2) The discussion of polymer models, while useful, does not adequately address the limitations of these models for capturing sequence-specific effects. 3) The case studies, while illustrative, are presented somewhat uncritically; the authors do not discuss potential artifacts or alternative interpretations in sufficient depth. 4) The section on integration approaches would benefit from a more explicit comparison of the assumptions and failure modes of each method. 5) The review does not address recent developments in machine learning-based approaches for IDR ensemble prediction, which are increasingly relevant.
- **Minor Comments** 1) The abstract is somewhat general and could more explicitly state the specific integration frameworks discussed. 2) The use of "we" in the Results section is inconsistent with the review format. 3) Some technical terms (e.g., "kappa2 = 2/3") are introduced without sufficient context for nonspecialist readers. 4) The Discussion section on open challenges is relatively brief and could be expanded. 5) The Acknowledgements section is unusually detailed and could be shortened.
- **Technical failings that need to be addressed before the case is established** None identified from the supplied material. The technical content appears accurate, but the absence of figures limits verification of quantitative claims.
- **Assessment against Nature-style criteria**  
  *Originality*: Moderate. The review synthesizes existing work rather than presenting novel findings, but the integrative framework and critical perspective offer some original synthesis.  
  *Scientific importance*: High. The topic is of significant current interest, and the review addresses a genuine need for methodological guidance in this rapidly evolving field.  
  *Interdisciplinary readership*: Moderate. The review is primarily accessible to biophysicists and computational chemists; nonspecialists may struggle with some technical details.  
  *Technical soundness*: High. The technical descriptions are accurate and well-referenced, though the lack of figures limits full verification.  
  *Readability for nonspecialists*: Moderate. The writing is clear, but the density of technical detail may be challenging for readers outside the immediate field.
- **Recommendation posture** Supportive if technical concerns are resolved. The review is a valuable contribution, but it would be strengthened by a more critical and quantitative treatment of limitations, and by addressing recent developments in the field.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The manuscript states that "many standard force fields lead to over-compaction of IDRs" and that "substantial effort over the last decade" has addressed this, but does not provide a quantitative comparison of force field performance.
- **Evidence pointer** Section "Limitations of all-atom simulations", location not provided
- **Concern** The review acknowledges force field inaccuracies as a key challenge but does not provide a systematic, quantitative comparison of available force fields (e.g., Amber ff03ws, CHARMM36m, a99SB-disp) in terms of their ability to reproduce experimental IDR dimensions, secondary structure propensities, or dynamics. This is a significant omission for a methods-focused review, as readers would benefit from guidance on force field selection.
- **Why it matters** Force field choice is a critical determinant of simulation accuracy for IDRs. Without quantitative benchmarks, readers cannot make informed decisions about which force field to use for their specific system or question.
- **Resolution test** Add a table or figure comparing the performance of major force fields against experimental data (e.g., radius of gyration, scaling exponents) for a set of benchmark IDRs, with appropriate citations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The manuscript states that "the most straight-forward approach involves performing unbiased molecular simulations... and then comparing those observables with the analogous values obtained from experiment," but does not critically evaluate the conditions under which this approach is valid.
- **Evidence pointer** Section "Approaches for the integration of single-molecule spectroscopy and simulations", location not provided
- **Concern** The review presents direct comparison of unbiased simulations with experiment as the "most straight-forward" approach, but does not adequately discuss the conditions under which this approach fails, such as when force field inaccuracies or sampling limitations are severe. The discussion of reweighting methods is useful, but the criteria for when reweighting is appropriate versus when it masks fundamental force field errors are not clearly articulated.
- **Why it matters** Readers may be misled into thinking that direct comparison is always a valid first step, when in practice it can lead to misleading conclusions if the simulation ensemble is significantly biased. A more nuanced discussion of the limitations of this approach is needed.
- **Resolution test** Add a subsection discussing the conditions under which direct comparison is likely to be reliable, and provide criteria for when reweighting or other correction methods should be employed.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interdisciplinary readership
- **Claim pointer** The manuscript states that "the functional form of the inter-dye probability distribution P(r) is typically approximated using simple polymer models or inferred from molecular simulations," but does not explain the physical basis of these models for nonspecialist readers.
- **Evidence pointer** Section "Single-molecule Förster Resonance Energy Transfer", location not provided
- **Concern** The review introduces polymer models (freely jointed chain, worm-like chain, self-avoiding walk) without providing sufficient physical context for readers who are not experts in polymer physics. The distinction between these models and their relevance to IDR conformations is not clearly explained.
- **Why it matters** The review aims to be accessible to a broad audience, but the polymer model discussion may be opaque to experimentalists or computational biologists without a polymer physics background. This limits the review's utility as an educational resource.
- **Resolution test** Add a brief introductory paragraph explaining the physical basis of polymer models and their relevance to IDR conformations, with a figure illustrating the differences between models.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The manuscript states that "the integration of single-molecule fluorescence spectroscopy and all-atom simulations has been instrumental in our modern understanding of sequence-encoded conformational behavior in disordered proteins," but does not discuss recent machine learning-based approaches for IDR ensemble prediction.
- **Evidence pointer** Discussion section, location not provided
- **Concern** The review does not mention recent advances in machine learning and deep learning methods for predicting IDR conformational ensembles (e.g., AlphaFold-based approaches, variational autoencoders, or neural network potentials). These methods are increasingly relevant for IDR research and represent a complementary or alternative approach to traditional simulation-based methods.
- **Why it matters** The review aims to provide a comprehensive overview of the field, and omitting these developments makes it incomplete and potentially outdated. Readers may miss important new tools and approaches.
- **Resolution test** Add a subsection in the Discussion or Conclusions discussing recent machine learning-based approaches and their potential impact on the field, with appropriate citations.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Abstract
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract is somewhat general and does not explicitly state the specific integration frameworks discussed in the review.
- **Required correction** Add a sentence in the abstract summarizing the main integration approaches covered (e.g., direct comparison, explicit dye inclusion, reweighting).

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Section "Single-molecule Förster Resonance Energy Transfer"
- **Evidence pointer** Section "Single-molecule Förster Resonance Energy Transfer", location not provided
- **Issue** The term "kappa2 = 2/3" is introduced without sufficient context for readers unfamiliar with FRET theory.
- **Required correction** Add a brief explanation of the physical meaning of the orientation factor kappa2 and why the isotropic value of 2/3 is commonly assumed.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section "Approaches for the integration of single-molecule spectroscopy and simulations"
- **Evidence pointer** Section "Approaches for the integration of single-molecule spectroscopy and simulations", location not provided
- **Issue** The review mentions "Bayesian Inference of Ensembles (BioEn), Convex OPtimization for Ensembl Reweighting (COPER), Bayesian/Maximum Entropy (BME), and Extended Experimental Inferential Structure Determination (X-EISD)" but does not provide a comparison of their relative advantages and disadvantages.
- **Required correction** Add a brief comparison of these methods, highlighting their key differences and appropriate use cases.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Section "Conformational dynamics as assessed by single-molecule spectroscopy and simulations"
- **Evidence pointer** Section "Conformational dynamics as assessed by single-molecule spectroscopy and simulations", location not provided
- **Issue** The term "internal friction" is used without a clear definition for readers unfamiliar with polymer dynamics.
- **Required correction** Add a brief definition of internal friction and its physical origin in the context of IDR dynamics.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section "Multi-molecular assemblies as measured by single-molecule spectroscopy and simulations"
- **Evidence pointer** Section "Multi-molecular assemblies as measured by single-molecule spectroscopy and simulations", location not provided
- **Issue** The review states that "the integration of smFRET, nsFCS, and MD simulations has been essential to deconvolve complex heterogeneous systems" but does not provide specific technical details on how these methods are combined in practice.
- **Required correction** Add a brief description of the practical workflow for integrating these methods, including any challenges or pitfalls.

## Risk / unsupported claims
- The claim that "many standard force fields lead to over-compaction of IDRs" is supported qualitatively but not quantitatively; no benchmark data are provided.
- The claim that "the most straight-forward approach involves performing unbiased molecular simulations... and then comparing those observables with the analogous values obtained from experiment" is presented without critical evaluation of its limitations.
- The claim that "the integration of single-molecule fluorescence spectroscopy and all-atom simulations has been instrumental in our modern understanding" is supported by the case studies but is not systematically evaluated across the broader literature.
- The claim that "polarizable force fields offer a potential solution" to dye modeling challenges is speculative and not supported by specific examples or data.
- The claim that "simulations of a few hundred nanoseconds are rarely sufficient for even modestly sized disordered proteins" is plausible but not supported by specific data or references.