## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no figures, tables, methods, or supplementary materials were provided
- **Shared manuscript claim summary** The authors analysed whole genome sequences from clinical Mycobacterium tuberculosis complex (MTBc) isolates across all lineages from over 32,000 patients, identified single nucleotide variations (SNVs), and mapped nonsynonymous mutations onto known and AlphaFold-predicted tertiary structures of ESX-1 related proteins. They report fully conserved regions, some assigned to known quaternary structures and others predicted to be involved in undiscovered interactions. Clonally expanded mutants (found in >1% of isolates) were mostly located on the surface of globular domains, remote from known protein–protein interactions. Fully conserved intrinsically disordered regions (IDRs) were identified and suggested to be crucial for pathogenicity. The authors conclude that fully conserved regions are attractive vaccine antigens and drug targets, and that the approach can be extended to other pathogens.
- **Visible evidence base** Abstract text only; no dataset, methods description, structural analysis details, or statistical results are visible
- **Missing materials affecting confidence** Full manuscript, all figures and tables, methods section, supplementary data, structural coordinates, SNV calling pipeline details, and lineage assignment criteria

## Reviewer
- **Overall assessment** The abstract presents a potentially valuable large-scale genomic and structural analysis of ESX-1 related proteins in MTBc. The scale of the dataset (over 32,000 patients) and the integration of clinical isolate sequencing with structural biology are commendable. However, the abstract alone does not provide sufficient evidence to evaluate the robustness of the methods, the validity of the structural mappings, or the strength of the conclusions. Several claims, particularly those regarding fully conserved regions as therapeutic targets and the functional significance of IDRs, require substantial supporting data that are not visible in the supplied material. The work is of interest to the tuberculosis and structural genomics communities, but the case is not fully established from the abstract alone.
- **Who would be interested in the results, and why** Tuberculosis researchers, structural biologists, evolutionary biologists, and vaccine and drug development scientists would be interested. The identification of conserved regions in virulence-associated proteins across all MTBc lineages has direct implications for designing broadly effective interventions. The methodological approach, combining population genomics with structural prediction, may also appeal to researchers studying other pathogens.
- **Major strengths** The use of a very large clinical isolate dataset spanning all MTBc lineages provides a strong evolutionary foundation. The integration of known and AlphaFold-predicted structures with population-level variation data is a modern and potentially powerful approach. The focus on ESX-1 related proteins, which are central to virulence, gives the work clear biological relevance. The observation that clonally expanded mutations are located away from known interaction interfaces is an interesting and potentially testable finding.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that mapping nonsynonymous SNPs onto known and AlphaFold-predicted tertiary structures revealed fully conserved regions, some assigned to known quaternary structures and others predicted to be involved in yet-to-be-discovered interactions.
  - **Evidence pointer** Abstract only; no figures or tables provided
  - **Concern** The abstract does not describe how structural mappings were performed, how conservation was defined, or how quaternary structure assignments and interaction predictions were validated. AlphaFold predictions have known limitations, particularly for protein complexes and disordered regions, and the abstract provides no indication of confidence metrics or experimental validation.
  - **Why it matters** The central claim of the paper depends on the reliability of structural assignments and the definition of conservation. Without details on thresholds, quality filters, and validation, the reader cannot assess whether the identified regions are truly conserved or whether the structural interpretations are robust.
  - **Resolution test** Provide a detailed methods section describing the structural mapping pipeline, including AlphaFold confidence scores, criteria for defining conserved regions, and any experimental or literature-based validation of quaternary structure assignments. Show representative examples in figures with clear conservation annotations.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Support for conclusions
  - **Claim pointer** The authors conclude that fully conserved regions of ESX-1 related proteins are attractive vaccine antigens and drug targets, and that fully conserved IDRs are crucial for pathogenicity.
  - **Evidence pointer** Abstract only; no functional or immunological data provided
  - **Concern** The abstract provides no direct evidence linking conserved regions to vaccine efficacy or drug susceptibility. The claim that IDRs are crucial for pathogenicity is inferred solely from conservation, which is an indirect proxy. No functional assays, knockout studies, or immune epitope data are mentioned.
  - **Why it matters** The conclusions extend beyond the presented data. Conservation may indicate functional importance, but it does not establish therapeutic relevance. Overstating the implications without functional validation weakens the scientific case and could mislead downstream applications.
  - **Resolution test** Include functional data, such as immune recognition assays for conserved regions, or clearly frame the conclusions as hypotheses. If functional data are not available, temper the language to reflect that the findings generate testable predictions rather than established therapeutic targets.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Clarity and reproducibility
  - **Claim pointer** The authors state that clonally expanded mutants (found in >1% of isolates) were mostly located at the surface of globular domains, remote from known intra- and inter-molecular protein–protein interactions.
  - **Evidence pointer** Abstract only; no statistical analysis or distribution data provided
  - **Concern** The abstract does not specify how clonal expansion was defined beyond the 1% threshold, how many mutants met this criterion, or what statistical test was used to support the claim that they are "mostly" located away from interaction interfaces. The term "mostly" is vague and not quantified.
  - **Why it matters** This finding is presented as a key result, but without quantitative support, it is not possible to evaluate its significance. The claim could be a chance observation or a robust pattern; the abstract does not allow the reader to distinguish between these possibilities.
  - **Resolution test** Provide the number of clonally expanded mutants, the distribution of their locations relative to interaction interfaces, and a statistical comparison (e.g., enrichment analysis) with appropriate confidence intervals.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability
  - **Affected element** Abstract text
  - **Evidence pointer** Abstract, first sentence
  - **Issue** The phrase "ESX-1 genes of interests" contains a grammatical error and is ambiguous. It is unclear whether the authors mean all ESX-1 genes or a subset of interest.
  - **Required correction** Revise to "ESX-1 genes of interest" and clarify whether the analysis covers the full ESX-1 locus or selected genes.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** Abstract text
  - **Evidence pointer** Abstract, "ternary protein structures"
  - **Issue** The term "ternary" is likely a typographical error for "tertiary." Ternary is not standard terminology for protein structure.
  - **Required correction** Replace "ternary" with "tertiary" throughout the abstract.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Abstract text
  - **Evidence pointer** Abstract, "fully conserved regions"
  - **Issue** The abstract does not define what "fully conserved" means in this context. It is unclear whether this refers to 100% identity across all isolates, across all lineages, or some other threshold.
  - **Required correction** Define the conservation threshold explicitly in the abstract or methods.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Scope
  - **Affected element** Abstract text
  - **Evidence pointer** Abstract, final sentence
  - **Issue** The claim that the approach can be extended to other pathogens is speculative and not supported by any data in the abstract.
  - **Required correction** Either remove this sentence or reframe it as a future direction rather than a finding.
- **Technical failings that need to be addressed before the case is established** R1-M1 and R1-M2 are blocking. The structural mapping methodology and the functional significance of conserved regions must be substantiated with detailed methods and supporting data. Without these, the core conclusions are not established from the supplied material.
- **Assessment against Nature-style criteria**  
  Originality: The combination of large-scale clinical isolate genomics with structural mapping on ESX-1 proteins is novel and potentially original. However, the abstract does not demonstrate how this approach differs from prior structural genomics studies.  
  Scientific importance: The topic is of high importance given the global burden of tuberculosis and the need for new interventions. The findings, if validated, could inform vaccine and drug design.  
  Interdisciplinary readership: The work bridges genomics, structural biology, and infectious disease, which would appeal to a broad audience. However, the abstract assumes familiarity with ESX-1 biology and structural prediction, which may limit accessibility.  
  Technical soundness: Not assessable from the abstract alone. The lack of methodological detail is a major limitation.  
  Readability for nonspecialists: The abstract is generally readable but contains jargon and undefined terms (e.g., "clonally expanded," "intrinsically disordered regions") that would benefit from brief explanations.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents an interesting premise, but the absence of methods, figures, and quantitative results prevents a full evaluation. The authors should be encouraged to provide the complete manuscript and supporting data for a thorough review.

## Risk / unsupported claims
- The claim that fully conserved regions are attractive vaccine antigens and drug targets is unsupported by functional or immunological evidence in the abstract.
- The claim that fully conserved IDRs are crucial for pathogenicity is inferred solely from conservation and is not directly tested.
- The claim that clonally expanded mutants are "mostly" located away from interaction interfaces is not quantified or statistically supported.
- The claim that the approach can be extended to other pathogens is speculative and not evidenced.
- The reliability of AlphaFold-predicted structures for quaternary assignments is not discussed, and no confidence metrics are provided.