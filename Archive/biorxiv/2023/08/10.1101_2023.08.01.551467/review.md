## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the supplied abstract; no full text, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors analyze sequence diversity in SARS-CoV-2 nucleocapsid protein to argue that short linear interaction motifs (SLiMs) are abundantly presented, often arise transiently via mutations relative to an ancestral consensus, and collectively sample at least 25% of known eukaryotic motifs, indicating a highly dynamic virus-host interface.
- **Visible evidence base** Abstract text only; no methodological details, sequence datasets, statistical analyses, or visualizations are available
- **Missing materials affecting confidence** Full manuscript, methods, sequence alignment details, motif prediction algorithms, statistical thresholds, control analyses, and all figures or tables

## Reviewer
- **Overall assessment** The abstract presents an intriguing hypothesis about the evolutionary dynamics of SLiMs in a viral protein, with potential implications for understanding virus-host coevolution. However, the current evidence base is insufficient to evaluate the validity of the central claims. Key quantitative assertions, such as the "at least 25% of known eukaryotic motifs" and the classification of motifs as "possibly non-functional," lack supporting methodological detail. The work may be of interest to virologists and molecular evolution researchers, but the case is not established from the supplied material.
- **Who would be interested in the results, and why** Virologists studying SARS-CoV-2 host interactions, molecular evolution researchers interested in sequence diversity and de novo motif emergence, and cell biologists examining SLiM-mediated signaling. The claim of broad motif space exploration could inform therapeutic targeting of virus-host interfaces.
- **Major strengths** The focus on a large, viable sequence record of SARS-CoV-2 is a novel resource for studying motif dynamics. The concept of "ex nihilo" motif emergence through transient mutations is conceptually interesting and could reframe how viral mimicry is understood.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** Originality is moderate to high, as the application of large-scale sequence diversity to SLiM dynamics is not commonplace. Scientific importance is potentially significant for virus-host evolution, but the abstract does not provide enough evidence to judge impact. Interdisciplinary readership is plausible, spanning virology, evolution, and structural biology. Technical soundness cannot be assessed without methods and controls. Readability for nonspecialists is adequate, though terms like "ex nihilo" and "accessible motif space" require clearer definition.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "We observe the abundant presentation of motifs encoding several essential host protein interactions, alongside a majority of possibly non-functional and randomly occurring motif sequences absent in subsets of viable virus species."
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract claims a distinction between functional and non-functional motifs, but no criteria for functional significance, prediction method, or validation against experimental data are described. The term "possibly non-functional" is vague and not operationalized.
- **Why it matters** Without a clear definition of functional versus random motifs, the central observation of "abundant presentation" cannot be distinguished from background noise in sequence analysis. This undermines the foundation of the entire argument.
- **Resolution test** Provide a detailed description of motif prediction algorithms, statistical significance thresholds, and any experimental or literature-based validation for the functional motifs. Show that the classification is robust to alternative prediction methods.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "A large number of motifs emerge ex nihilo through transient mutations relative to the ancestral consensus sequence."
- **Evidence pointer** Abstract; location not provided
- **Concern** The claim of "ex nihilo" emergence is not supported by any phylogenetic or mutational analysis details. It is unclear how the ancestral consensus was defined, how transient mutations were tracked across the sequence record, and what fraction of mutations were considered transient versus fixed.
- **Why it matters** The evolutionary interpretation hinges on distinguishing true de novo emergence from pre-existing motifs that are lost and regained. Without this distinction, the claim of rapid exploration is overstated.
- **Resolution test** Present a clear phylogenetic framework, define the ancestral sequence construction, and quantify the frequency and duration of motif appearance and disappearance across the sequence record. Include sensitivity analyses for alignment and consensus parameters.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative claim
- **Claim pointer** "The observed mutational landscape implies an accessible motif space that spans at least 25% of known eukaryotic motifs."
- **Evidence pointer** Abstract; location not provided
- **Concern** The 25% figure is presented without any statistical derivation, confidence intervals, or comparison to a null model. It is unclear how "accessible motif space" is defined and whether this percentage is specific to the nucleocapsid protein or generalizable.
- **Why it matters** This is the headline quantitative claim and likely a key selling point for broad significance. If the estimate is not rigorously derived, the paper's impact is substantially weakened.
- **Resolution test** Provide a detailed statistical framework for estimating accessible motif space, including a null model of random sequence evolution, confidence intervals, and a clear definition of "known eukaryotic motifs" with the source database.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** "the uniquely vast sequence record of viable SARS-CoV-2 species"
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract does not specify the number of sequences analyzed, the source database, quality filters, or how "viable" was determined. Without this information, the uniqueness and adequacy of the dataset cannot be evaluated.
- **Why it matters** The entire analysis rests on the quality and representativeness of the sequence record. If the dataset is biased or incomplete, all downstream claims are compromised.
- **Resolution test** Specify the exact dataset, including accession numbers, date of retrieval, filtering criteria, and any subsampling strategies. Provide a summary of sequence diversity and coverage.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract; location not provided
- **Issue** The term "ex nihilo" is used without definition, and "accessible motif space" is not explained.
- **Required correction** Define both terms explicitly in the abstract or introduction, with a brief example if needed.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Scope
- **Affected element** Generalizability
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract focuses on SARS-CoV-2 nucleocapsid but does not discuss whether the findings are expected to apply to other RNA viruses or proteins.
- **Required correction** Add a sentence in the discussion or conclusion addressing the potential generalizability and limitations of using a single viral protein.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract structure
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract jumps from observation to implication without a clear logical bridge, making it hard for nonspecialists to follow the argument.
- **Required correction** Restructure the abstract to explicitly state the hypothesis, the approach, the key findings, and the implications in a stepwise manner.

## Risk / unsupported claims
- The claim that "at least 25% of known eukaryotic motifs" are accessible is unsupported without statistical derivation and a null model.
- The classification of motifs as "possibly non-functional" is unsupported without defined criteria.
- The claim of "ex nihilo" emergence is unsupported without phylogenetic and mutational analysis details.
- The assertion of a "uniquely vast sequence record" is unverifiable without dataset specifications.
- The overall implication of "rapidly evolve the virus-host interface" is speculative without functional validation or evolutionary rate measurements.