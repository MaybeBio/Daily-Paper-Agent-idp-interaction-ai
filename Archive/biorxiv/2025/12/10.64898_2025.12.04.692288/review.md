## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no figures, methods, or supplementary material provided
- **Shared manuscript claim summary** The authors report the first application of native mass spectrometry (nMS) to characterise the full Cullin RING E3 ligase complex CRL2VHL and its interactions with PROTACs, POIs, E2, and ubiquitin, including binary, ternary, and higher-order complexes, benchmarked with two POI/PROTAC systems (BRD4 BD2/MZ1 and KRAS/ACBI3).
- **Visible evidence base** Abstract text only; no experimental details, spectra, or quantitative data
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, supplementary information, raw nMS data, sample preparation details, and statistical analyses

## Reviewer
- **Overall assessment** The abstract presents a potentially valuable methodological advance for the targeted protein degradation field, namely the use of nMS to characterise large, multiprotein E3 ligase complexes and their PROTAC-mediated assemblies. The claim of being the first to characterise a full E3 complex and E3-E2 interactions by nMS is notable and, if substantiated, would be of interest to a broad audience. However, the abstract alone provides no experimental evidence, and several claims regarding the observation of specific complexes and the benchmarking across two systems cannot be evaluated without the underlying data. The technical feasibility of nMS for such high-mass, heterogeneous complexes is plausible but requires careful validation, particularly regarding resolution, stoichiometry assignment, and preservation of noncovalent interactions.
- **Who would be interested in the results, and why** Researchers in targeted protein degradation, particularly those developing PROTACs and molecular glues, would be interested because the method could provide a routine, scalable biophysical tool for validating ternary complex formation and E3 engagement. Structural biologists and mass spectrometrists specialising in native protein complexes would also find the methodological advance relevant. Additionally, medicinal chemists and drug discovery scientists seeking alternative characterisation methods when cryo-EM or crystallography are impractical would benefit.
- **Major strengths** The proposed application of nMS to a full CRL complex addresses a genuine gap in the field, as current structural methods are often limited for transient and flexible assemblies. The choice of CRL2VHL as a foundational E3 and the inclusion of two distinct POI/PROTAC systems (BRD4 BD2/MZ1 and KRAS/ACBI3) suggests an attempt at generalisability. The abstract clearly articulates the potential for nMS to complement existing biophysical methods.
- **Major Concerns** 
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The authors claim that "we characterise binary, ternary and higher order complexes that comprise CRL2VHL, including the multiprotein systems of POI-PROTAC-CRL2VHL, CRL2VHL-E2-Ub, and POI-PROTAC-CRL2VHL-E2-Ub, all of which are essential in facilitating productive POI ubiquitination and degradation."
  - **Evidence pointer** Abstract only; no figures or tables provided
  - **Concern** The abstract asserts the observation of multiple specific multiprotein complexes, but no experimental data are presented to support these assignments. Native mass spectra of such large complexes (CRL2VHL is pentameric and likely exceeds 200 kDa, with higher-order assemblies larger still) require careful interpretation to distinguish specific complexes from nonspecific adducts or dissociation products. The claim of observing all relevant complexes across both systems is strong and requires direct spectral evidence with mass assignments and stoichiometry validation.
  - **Why it matters** Without evidence, the central claim of the manuscript cannot be assessed. If the complex assignments are incorrect or ambiguous, the methodological advance would be undermined. The field requires reliable tools, and overclaiming based on unvalidated nMS data could mislead other researchers.
  - **Resolution test** Provide representative nMS spectra for each claimed complex, with deconvolved masses matching theoretical values within acceptable error, and demonstrate that control experiments (e.g., individual components, nonbinding PROTACs) do not produce similar signals.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors state that "Native mass spectrometry (nMS) can be used to characterise protein complexes but has not previously been used to characterise a full E3 or any E3-E2 interactions."
  - **Evidence pointer** Abstract only; no literature review or methods provided
  - **Concern** The novelty claim is central to the manuscript's significance, but the abstract provides no comparative analysis of prior nMS studies on E3 ligases or E3-E2 complexes. It is possible that partial E3 complexes or E3-E2 interactions have been studied by nMS, and the authors' claim of "first" requires a thorough literature context that is not visible here.
  - **Why it matters** If the novelty claim is overstated, the manuscript's contribution would be diminished. Conversely, if it is accurate, it needs to be clearly established with appropriate citations and discussion.
  - **Resolution test** Provide a comprehensive literature search in the manuscript demonstrating that no prior nMS study has characterised a full E3 complex or E3-E2 interactions, with specific citations and a clear statement of the gap.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Reproducibility
  - **Claim pointer** The authors state that "We benchmarked the nMS with two POI examples (BRD4 BD2 and KRAS) with their respective PROTACs (MZ1 and ACBI3) and were able to observe all relevant complexes across both systems."
  - **Evidence pointer** Abstract only; no experimental conditions provided
  - **Concern** The abstract does not describe the nMS experimental conditions, including ion source parameters, collision energies, buffer composition, or sample concentrations. These parameters are critical for preserving noncovalent interactions and for the reproducibility of the method. Without this information, other laboratories cannot replicate the experiments.
  - **Why it matters** Reproducibility is a cornerstone of scientific validity. For a methodological paper, detailed experimental protocols are essential. The absence of such details in the abstract is expected, but the full manuscript must provide them; the current assessment cannot verify this.
  - **Resolution test** In the full manuscript, provide a detailed methods section with all nMS parameters, sample preparation steps, and data processing procedures, and demonstrate reproducibility with replicate measurements.
- **Minor Comments** 
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Terminology
  - **Evidence pointer** Abstract, first sentence
  - **Issue** The phrase "binding of PROTACs to their partner ubiquitin E3 ligase (E3) and a protein of interest (POI)" is slightly ambiguous, as PROTACs bind to both the E3 and the POI simultaneously, but the phrasing could be read as two separate binding events.
  - **Required correction** Rephrase to clarify that PROTACs bind bivalently to both the E3 and the POI, forming a ternary complex.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Benchmarking rationale
  - **Evidence pointer** Abstract, last paragraph
  - **Issue** The choice of BRD4 BD2 and KRAS as benchmarking examples is stated but not justified. These are structurally and biophysically distinct targets, which is presumably intentional, but the rationale is not explained.
  - **Required correction** Add a sentence in the abstract or introduction explaining why these two POIs were selected (e.g., differing size, flexibility, or relevance to clinical PROTACs).
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Scope
  - **Affected element** Generalisability claim
  - **Evidence pointer** Abstract, final sentence
  - **Issue** The claim that nMS "will open avenues for nMS to integrate as an alternative experimental method" is forward-looking but not directly supported by the data presented in the abstract. It is a reasonable speculation, but it should be framed as a perspective rather than a conclusion.
  - **Required correction** Soften the language to indicate that the results suggest potential for broader application, rather than asserting a definitive future role.

## Risk / unsupported claims
- The claim of being the first to characterise a full E3 complex and E3-E2 interactions by nMS is unverifiable from the abstract alone and requires a thorough literature review in the full manuscript.
- The observation of all listed multiprotein complexes (binary, ternary, higher-order, including POI-PROTAC-CRL2VHL, CRL2VHL-E2-Ub, and POI-PROTAC-CRL2VHL-E2-Ub) is unsupported without spectral data and mass assignments.
- The benchmarking across two POI/PROTAC systems is stated but not evidenced; no comparative data are shown.
- The functional relevance of the observed complexes to "productive POI ubiquitination and degradation" is asserted but not experimentally demonstrated (e.g., no ubiquitination assays are mentioned).

## Assessment against Nature-style criteria
- **Originality** Potentially high, if the novelty claim holds. The application of nMS to a full CRL complex and E3-E2 interactions would be a first, but this cannot be confirmed from the abstract alone.
- **Scientific importance** Moderate to high. A routine biophysical method for characterising PROTAC-induced complexes would be valuable to the targeted protein degradation field, which currently relies on more laborious structural methods.
- **Interdisciplinary readership** Moderate. The work bridges structural biology, mass spectrometry, and chemical biology, and would appeal to researchers in these areas, but the abstract's technical focus may limit broader appeal.
- **Technical soundness** Not assessable from the abstract. The absence of any experimental details or data prevents evaluation of the technical quality of the nMS measurements.
- **Readability for nonspecialists** The abstract is generally clear but uses field-specific terminology (e.g., "Cullin RING E3 Ligase," "ternary complex") without explanation, which may hinder nonspecialist readers.

## Recommendation posture
Currently not established from the provided evidence. The abstract presents a promising and potentially significant methodological claim, but the absence of any experimental data, methods, or literature context means that the core assertions cannot be evaluated. A decision would require the full manuscript, including nMS spectra, mass assignments, control experiments, and a detailed methods section. If the full data substantiate the claims, the work could be suitable for a high-impact journal, but as presented, the case is not yet made.