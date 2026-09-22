## Review setup
- **Input scope** Full manuscript text (abstract, introduction, main review sections, conclusion, author contributions, conflict of interest, publisher's note, glossary)
- **Assessment boundary** Scientific content, structural coherence, evidence quality, and alignment with stated review aims; no assessment of editorial fit or publication decision
- **Shared manuscript claim summary** The authors argue that the androgen receptor N-terminal domain (AR-NTD) is a critical driver of castration-resistant prostate cancer (CRPC) and a viable therapeutic target, despite challenges posed by its intrinsic disorder. They review sequence-structure-function relationships, catalog current NTD-targeting inhibitors, and propose future directions for structure-based drug design.
- **Visible evidence base** Narrative review with cited primary literature; descriptions of experimental methods (cell-based assays, SPR, NMR, MD simulations, virtual screening); clinical trial data for EPI-506 and EPI-7386; structural models from cryo-EM and computational studies
- **Missing materials affecting confidence** No figures or tables were provided for inspection; no supplementary data; no primary experimental results; no systematic search methodology or inclusion criteria for literature selection; no PRISMA-style reporting; no critical appraisal of included studies

## Reviewer
- **Overall assessment** This is a broad, narrative review covering the AR-NTD as a therapeutic target in CRPC. The topic is timely and clinically relevant, and the authors have assembled a substantial body of literature. However, the review suffers from structural disorganization, uneven depth across sections, and a lack of critical synthesis. Several claims are made without adequate supporting evidence or with overstatement relative to the cited data. The review would benefit from a clearer framework, more rigorous evaluation of the evidence, and a more balanced discussion of limitations and alternative perspectives.
- **Who would be interested in the results, and why** Researchers in prostate cancer biology, drug discovery scientists focused on intrinsically disordered proteins, medicinal chemists developing AR-targeted therapies, and clinicians managing CRPC. The review provides a consolidated overview of NTD-targeting strategies that may inform future research directions and therapeutic development.
- **Major strengths** The topic addresses a genuine gap in the field, as most AR-targeted therapies focus on the LBD. The authors cover a wide range of inhibitor classes and experimental approaches, including recent developments such as PROTACs and covalent binders. The discussion of intrinsic disorder as a drug design challenge is conceptually important and well contextualized. The inclusion of clinical trial data for EPI-506 and EPI-7386 adds translational relevance.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (overstated claim regarding NTD as "major therapeutic barrier"), R1-M2 (unsupported claim about virtual screening success), R1-M3 (incomplete clinical trial reporting), R1-M4 (lack of critical appraisal of inhibitor evidence)
- **Assessment against Nature-style criteria**  
  *Originality*: Moderate. The review consolidates known information but does not offer a novel conceptual framework or new synthesis. The discussion of intrinsic disorder and drug design is not new to the field.  
  *Scientific importance*: High. The topic is clinically significant, and a well-executed review could influence research priorities. However, the current execution limits its impact.  
  *Interdisciplinary readership*: Moderate. The content bridges cancer biology, structural biology, and medicinal chemistry, but the presentation is not sufficiently accessible to nonspecialists in each area.  
  *Technical soundness*: Weak. Several claims are overstated or lack adequate support, and the review does not critically evaluate the quality of the evidence it presents.  
  *Readability for nonspecialists*: Poor. The text is dense, with abrupt transitions and insufficient signposting. Technical terms are introduced without definition, and the logical flow is difficult to follow.
- **Recommendation posture** Currently not established from the provided evidence. The review has merit in scope and topic, but substantial revisions are required to improve rigor, balance, and clarity before it can be considered a reliable contribution.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim accuracy
- **Claim pointer** The title and abstract assert that the NTD is "a major therapeutic barrier" for treating CRPC, implying a well-established and dominant role.
- **Evidence pointer** Title; Abstract; Introduction (location not provided)
- **Concern** The claim that NTD is a "major therapeutic barrier" is presented as established fact, but the evidence cited in the review does not quantitatively or qualitatively support this level of emphasis. The authors do not provide comparative data on the relative contribution of NTD versus other resistance mechanisms (e.g., AR mutations, splice variants, coactivator upregulation, intratumoral androgen synthesis). The term "major" is used without a defined threshold or comparative analysis.
- **Why it matters** Overstating the role of NTD could mislead readers about the relative importance of this target compared to other mechanisms, potentially skewing research priorities and resource allocation.
- **Resolution test** The authors should either provide a quantitative or qualitative comparative analysis of resistance mechanisms, or temper the claim to reflect the current state of evidence (e.g., "a promising therapeutic target" rather than "major therapeutic barrier").

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The section on VPC-220010 states that "three million compounds from the ZINC database are docked into two selected crystal structures of the AR using Glide SP program" and that this led to the discovery of active compounds.
- **Evidence pointer** Section "Novel NTD-targeting compounds identified by structured based virtual screening" (location not provided)
- **Concern** The description of the virtual screening workflow is incomplete and potentially misleading. The authors do not specify the docking target (full-length AR, NTD alone, or a specific conformation), the scoring function details, or the hit selection criteria. More critically, the claim that docking against LBD-containing crystal structures (PDB 2PNU and 3L3X) led to NTD-targeting compounds is not mechanistically explained. The authors do not clarify how compounds identified against LBD structures would be expected to bind the NTD.
- **Why it matters** Virtual screening results are highly dependent on the target structure and methodology. Without this information, the reader cannot assess the validity of the approach or the credibility of the identified compounds as NTD binders.
- **Resolution test** The authors should provide a detailed description of the docking protocol, clarify the target structure used, and explain the rationale for how LBD-based screening yielded NTD-targeting compounds. If the compounds were subsequently validated as NTD binders, this should be stated explicitly with supporting data.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Data completeness
- **Claim pointer** The clinical trial section states that EPI-506 was tested in a phase 1 trial (NCT02606123) and that "signs of efficacy were shown by reduction of serum PSA in some patients receiving higher doses."
- **Evidence pointer** Section "Testing NTD inhibitors in clinical trials" (location not provided)
- **Concern** The clinical trial reporting is incomplete and potentially misleading. The authors do not report the number of patients who showed PSA reductions, the magnitude of these reductions, the duration of response, or the criteria used to define "signs of efficacy." They also do not discuss the reasons for trial termination beyond "poor oral bioavailability," omitting any mention of efficacy endpoints, disease progression, or adverse events beyond those listed as DLTs.
- **Why it matters** Incomplete reporting of clinical trial results can lead to misinterpretation of the therapeutic potential of NTD inhibitors. Readers need context on the strength of the efficacy signal and the reasons for termination to assess the viability of this approach.
- **Resolution test** The authors should provide a more complete summary of the trial results, including patient numbers, PSA response rates, duration of treatment, and a balanced discussion of why the trial was terminated. If the data are not publicly available, this should be stated explicitly.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Critical appraisal
- **Claim pointer** The review summarizes multiple NTD inhibitors (EPI derivatives, sintokamides, niphatenones, QW07, ASR-600, biaryl isoxazoles, VPC compounds) without critically comparing their potency, selectivity, or development status.
- **Evidence pointer** Sections on individual inhibitor classes (location not provided)
- **Concern** The review presents each inhibitor class in isolation, without a comparative analysis of their relative merits, limitations, or stage of development. There is no discussion of whether any of these compounds have progressed beyond preclinical studies, nor is there a critical assessment of the quality of the evidence supporting their mechanism of action. The authors also do not address potential off-target effects or toxicity concerns for any of the compounds.
- **Why it matters** A comprehensive review should help readers understand the competitive landscape and identify the most promising candidates for further development. Without critical comparison, the review reads as a catalog rather than a synthesis.
- **Resolution test** The authors should add a comparative table or section that evaluates the inhibitors across key parameters (potency, selectivity, mechanism, development stage, limitations) and provides a critical assessment of which approaches are most promising and why.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section "The conformation shift of N/C interaction"
- **Evidence pointer** Section text (location not provided)
- **Issue** The section begins with "There Newly synthesized AR" which appears to be a typographical error. The intended phrasing is unclear.
- **Required correction** Revise to "Newly synthesized AR" or "There, newly synthesized AR" depending on intended meaning.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Section "The sequence of mono-amino acid in NTD endues the nature of intrinsic disorder"
- **Evidence pointer** Section text (location not provided)
- **Issue** The term "mono-amino acid" is used to describe homopolymeric repeats (e.g., polyQ, polyP). This is not standard terminology; the field typically uses "homopolymeric amino acid repeats" or "amino acid repeat tracts."
- **Required correction** Replace "mono-amino acid" with "homopolymeric amino acid" or "amino acid repeat" throughout the section.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Accuracy
- **Affected element** Section "The sequence of mono-amino acid in NTD endues the nature of intrinsic disorder"
- **Evidence pointer** Section text (location not provided)
- **Issue** The text states "polyQ1 and polyG are polymorphic" but does not specify the nature of this polymorphism (e.g., length variation, single nucleotide polymorphisms). The term "polymorphic" is ambiguous in this context.
- **Required correction** Clarify what type of polymorphism is meant (e.g., "variable length" or "genetic polymorphism") and provide appropriate references.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Section "Activation function-1 within disordered N-Terminal domain is essential for AR transactivation"
- **Evidence pointer** Section text (location not provided)
- **Issue** The text states "transcriptional activation unit-1 (Tau-1, 101–361 aa)" and later "transcriptional activation unit-5 (Tau-5, 362–487 aa)". The numbering of these units is not explained, and it is unclear why units 2–4 are not discussed.
- **Required correction** Either briefly explain the numbering system or note that only Tau-1 and Tau-5 are discussed for brevity.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section "Bispecific antibodies targeting NTD are developed in vitro experiments"
- **Evidence pointer** Section text (location not provided)
- **Issue** The section title is grammatically awkward ("are developed in vitro experiments") and the content describes only one bispecific antibody (BiAb 3E10-AR441). The section would benefit from a clearer title and a brief discussion of the broader potential and limitations of this approach.
- **Required correction** Revise the title to "Bispecific antibodies targeting NTD: in vitro development" or similar, and add a brief discussion of the approach's potential and challenges.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section "Novel NTD-targeting compounds identified by structured based virtual screening"
- **Evidence pointer** Section text (location not provided)
- **Issue** The section title contains a typo: "structured based" should be "structure-based."
- **Required correction** Correct the typo in the section title.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section "Potential breakthroughs for discovering novel NTD-inhibitors"
- **Evidence pointer** Section text (location not provided)
- **Issue** The section on "Identifying short linear motifs to design peptide-drugs" discusses SLiMs generally but does not provide specific examples of SLiMs within AR-NTD that could be targeted, nor does it discuss the challenges of targeting SLiM-mediated interactions (e.g., large binding interfaces, competition with endogenous partners).
- **Required correction** Add specific examples of AR-NTD SLiMs and a balanced discussion of the feasibility and challenges of this approach.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Accuracy
- **Affected element** Section "Search for recurring conformation to explore transient binding pockets"
- **Evidence pointer** Section text (location not provided)
- **Issue** The text states "The cavities in IDPs could have a larger surface area, volume, and cavity depth, as compared to those in folded proteins, suggesting the possibility of strong ligand binding." This is an oversimplification; larger cavities do not necessarily correlate with stronger binding, and the relationship between cavity properties and ligand affinity is complex.
- **Required correction** Soften the claim and provide a more nuanced discussion of the relationship between cavity properties and ligand binding.

## Risk / unsupported claims
- The claim that NTD is a "major therapeutic barrier" (title, abstract) is not quantitatively supported by the evidence presented.
- The assertion that "over 52,000 compounds from the NCI or Chembridge libraries were tested with little to no hits" is presented without a reference or methodological detail, making it unverifiable.
- The statement that "molecular dynamics simulations reveal that compounds can induce the formation of collapsed helical states" is presented as a general finding, but the specific simulations and compounds are not identified, and the claim may overgeneralize from limited studies.
- The clinical trial section reports "signs of efficacy" for EPI-506 without providing the number of responders, magnitude of PSA reduction, or duration of response, making the claim unquantifiable.
- The statement that "the NTD can undergo liquid-liquid phase separation in vitro, with longer polyQ1 sequences phase separating more readily" is presented without discussion of the physiological relevance or the concentration conditions required for phase separation.
- The claim that "AR-NTD has little sequence similarity (<15%) to other steroid hormone receptors" is presented without a reference or specification of the comparison method, making it difficult to verify.
- The section on VPC-220010 implies that virtual screening against LBD-containing structures yielded NTD-targeting compounds, but the mechanistic rationale for this is not explained, leaving the claim unsupported.
- The statement that "SC428 is selective towards NTD as SC428 being inactive against GR" is presented without data on selectivity against other nuclear receptors or off-target effects.
- The claim that "UT-143 possesses drug-like pharmacokinetics and metabolism properties" is presented without specific data on absorption, distribution, metabolism, excretion, or toxicity.
- The conclusion that "these novel emerging inhibitors... have a promising prospective for producing even more successful outcomes" is speculative and not supported by the clinical data presented, which show limited efficacy and poor pharmacokinetics for the lead compound.