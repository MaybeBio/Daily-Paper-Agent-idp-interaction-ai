## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract, without access to full methods, figures, or supplementary data
- **Shared manuscript claim summary** The authors propose a molecular model explaining how specific IQSEC2 mutations dysregulate ARF6 activation via the Sec7 domain. They integrate experimental mutant data with RaptorX-based structure prediction, molecular modeling, and molecular dynamics simulations. The model posits that apoCM binding to IQSEC2 normally inhibits Sec7 access to ARF6, and that Ca2+ relieves this inhibition. Mutations at residue 350 are claimed to cause constitutive ARF6 activation by removing steric hindrance, while a mutation at residue 359 is claimed to cause constitutive hindrance and loss of ARF6 activation.
- **Visible evidence base** Abstract text only; no figures, tables, methods details, or simulation parameters provided
- **Missing materials affecting confidence** Full methods, simulation parameters, structural models, validation metrics, experimental data for mutants, and any statistical analyses

## Reviewer
- **Overall assessment** The abstract presents a plausible mechanistic hypothesis for IQSEC2 mutation effects on ARF6 regulation, but the evidence base is insufficient to evaluate the validity of the proposed model. The claims are qualitative and lack quantitative support from the provided material. The model's novelty is unclear given existing literature on IQSEC2 and ARF6 regulation.
- **Who would be interested in the results, and why** Researchers studying intellectual disability, epilepsy, and autism genetics; cell biologists interested in small GTPase regulation; computational biologists working on protein structure-function relationships. The model could inform therapeutic targeting of ARF6 pathways in IQSEC2-related disorders.
- **Major strengths** The abstract addresses a clinically relevant problem with potential translational implications. The integration of experimental data with computational approaches is appropriate for generating mechanistic hypotheses. The proposed model offers a testable framework linking specific mutations to distinct functional outcomes.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** "Mutations at amino acid residue 350 of IQSEC2 result in loss of steric hindrance of Sec 7 binding with ARF6 leading to constitutive activation of ARF6 by Sec 7"
  - **Evidence pointer** Abstract only; location not provided
  - **Concern** The abstract provides no quantitative or structural evidence supporting the claim that residue 350 mutations specifically remove steric hindrance. No simulation data, binding free energy calculations, or structural comparisons are presented to substantiate this mechanism.
  - **Why it matters** The central mechanistic claim of the model rests on this assertion. Without supporting structural or dynamic evidence, the conclusion is unsupported and cannot be distinguished from speculation.
  - **Resolution test** Provide structural models showing apoCM-bound versus mutant IQSEC2 conformations, with quantitative measures of Sec7 accessibility to ARF6 (e.g., solvent-accessible surface area, distance metrics from simulations) and comparison to wild-type controls.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** "a mutation at amino acid residue 359 of IQSEC2 results in constitutive hindrance of Sec 7 binding to ARF6 leading to the loss of the ability of IQSEC2 to activate ARF6"
  - **Evidence pointer** Abstract only; location not provided
  - **Concern** The claim of constitutive hindrance for residue 359 mutations is presented without any supporting simulation or experimental data. The mechanism by which this mutation creates persistent steric obstruction is not explained or evidenced.
  - **Why it matters** This claim is essential to the model's predictive value for distinguishing loss-of-function from gain-of-function mutations. Lack of evidence undermines the model's utility and credibility.
  - **Resolution test** Show comparative simulations of wild-type, residue 350, and residue 359 mutants with quantified Sec7-ARF6 interaction interfaces, including time-averaged distances and contact maps.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Originality
  - **Claim pointer** "These studies provide a model for dysregulation of IQSEC2 Sec 7 activity by mutant IQSEC2 proteins"
  - **Evidence pointer** Abstract only; location not provided
  - **Concern** The abstract does not situate this model within existing literature on IQSEC2 mutations or ARF6 regulation. It is unclear what novel insights this model provides beyond previously proposed mechanisms for IQSEC2 dysfunction.
  - **Why it matters** For a modeling study, demonstrating novelty relative to prior structural and functional data is critical. Without this context, the contribution's significance cannot be assessed.
  - **Resolution test** Include a comparative discussion of prior IQSEC2 structural models and functional studies, explicitly stating what new predictions or explanations this model offers.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Abstract clarity
  - **Evidence pointer** Abstract text
  - **Issue** The abstract uses specialized terms (apocalmodulin, Sec7 domain, steric hindrance) without brief definitions, which may limit accessibility for readers outside the immediate field.
  - **Required correction** Add brief parenthetical explanations for key technical terms or rephrase to improve accessibility.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Methods transparency
  - **Evidence pointer** Abstract text
  - **Issue** The abstract mentions "molecular dynamics simulations" but provides no details on simulation length, force field, or system setup, making reproducibility impossible.
  - **Required correction** Include key simulation parameters in the abstract or refer to a methods section with full details.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Scientific importance
  - **Affected element** Clinical relevance
  - **Evidence pointer** Abstract text
  - **Issue** The abstract states associations with epilepsy, autism, and intellectual disability but does not connect the proposed model to potential therapeutic implications or patient-specific outcomes.
  - **Required correction** Add a sentence on how this model could inform treatment strategies or patient stratification.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria**  
  Originality: The proposed model may offer a novel integration of IQSEC2 mutation data with structural predictions, but the abstract does not demonstrate sufficient novelty relative to existing literature.  
  Scientific importance: The topic is clinically relevant, but the abstract does not establish broader significance beyond the specific mutations discussed.  
  Interdisciplinary readership: The work bridges genetics, structural biology, and computational biology, but the abstract's technical density may limit appeal to a broad audience.  
  Technical soundness: The core mechanistic claims lack quantitative support from the provided material, and simulation details are absent.  
  Readability for nonspecialists: The abstract is concise but uses field-specific jargon without clarification.
- **Recommendation posture** Currently not established from the provided evidence. The model is plausible but unsupported by the abstract alone. Full methods and results are required to assess technical validity and novelty.

## Risk / unsupported claims
- The claim that residue 350 mutations cause constitutive ARF6 activation via loss of steric hindrance is unsupported by the provided material.
- The claim that residue 359 mutations cause constitutive hindrance and loss of ARF6 activation is unsupported by the provided material.
- The general model of apoCM-mediated regulation of Sec7 access to ARF6 is presented as established but is not evidenced in the abstract.
- The novelty of the proposed model relative to existing IQSEC2 literature cannot be evaluated from the abstract.