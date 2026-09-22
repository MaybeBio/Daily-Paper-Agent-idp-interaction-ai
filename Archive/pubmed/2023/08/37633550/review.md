## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors propose two modified docking strategies, 3SD (three-software docking) and 3SD-RR (three-software docking after removing random coiled IDR), which combine CABS-dock, HPEPDOCK, and HADDOCK to improve prediction of protein-peptide interaction (PpI) poses. They claim constant quality across most targets, enhanced performance for proteins with intrinsically disordered regions (IDRs), and efficient prediction using AlphaFold2-predicted receptors regardless of IDR presence or receptor structure availability.
- **Visible evidence base** Abstract text only; no quantitative results, benchmark datasets, statistical analyses, or methodological details are provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, benchmark datasets, docking scoring details, comparison baselines, statistical significance tests, and any code or data availability statements

## Reviewer
- **Overall assessment** The abstract presents a potentially useful methodological contribution to computational protein-peptide docking, particularly in addressing IDR-related challenges and integrating AlphaFold2 structures. However, the evidence provided in the abstract is insufficient to evaluate the validity, generalizability, or superiority of the proposed methods. No quantitative performance metrics, comparisons to existing methods, or statistical analyses are reported. The claims of "constant quality," "enhanced performance," and "efficient prediction" are unsupported in the current form.
- **Who would be interested in the results, and why** Computational biologists, structural bioinformaticians, and researchers in protein-protein interaction and drug discovery would be interested. The combination of existing docking tools and the handling of IDRs and AlphaFold2-predicted structures addresses practical challenges in the field, making the work relevant to those seeking robust docking pipelines.
- **Major strengths** The proposed strategy is pragmatic, leveraging three established docking tools rather than developing new algorithms, which may lower adoption barriers. The explicit focus on IDRs and AlphaFold2-predicted receptors addresses current bottlenecks in the field. The abstract clearly states the problem context and the intended contribution.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: The combination of three existing docking tools is incremental, though the IDR-removal step and application to AlphaFold2 structures add some novelty. Scientific importance: Potentially relevant to the docking community, but the abstract does not demonstrate a significant advance over existing methods. Interdisciplinary readership: The topic is specialized, and the abstract lacks accessible context for nonspecialists. Technical soundness: Cannot be assessed from the abstract; no methodological or validation details are provided. Readability for nonspecialists: The abstract is dense and assumes familiarity with docking software and IDR concepts, limiting broader accessibility.
- **Recommendation posture** Currently not established from the provided evidence. The abstract alone does not provide sufficient data to support the core claims. A full manuscript with quantitative validation and comparisons would be required to assess the methods.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "We validated our 3SD performance in known protein-peptide interactions (PpIs)" and "ensuring constant quality for most targets"
- **Evidence pointer** Abstract; location not provided
- **Concern** The abstract claims validation of 3SD on known PpIs and constant quality for most targets, but no quantitative results, benchmark details, or success rates are reported. The term "constant quality" is vague and undefined.
- **Why it matters** Without specific performance metrics (e.g., success rate, ranking accuracy, RMSD values) and a defined benchmark, the claim of improved or consistent performance cannot be evaluated or compared to existing methods.
- **Resolution test** Provide a table or figure in the full manuscript showing 3SD performance on a defined benchmark set, including success rates and comparison to individual software and other combined approaches.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "We also enhanced MD performance in proteins having intrinsically disordered regions (IDRs) by applying the modified 3SD strategy, the three-software docking after removing random coiled IDR (3SD-RR), to the comparable crystal PpI structures"
- **Evidence pointer** Abstract; location not provided
- **Concern** The claim of enhanced performance for IDR-containing proteins is not supported by any comparative data. The abstract does not specify how IDRs were identified, how removal was performed, or what improvement was observed relative to 3SD or other methods.
- **Why it matters** IDRs are a known challenge in docking, and the proposed solution is a key novelty. Without evidence of improvement, the contribution of 3SD-RR is unsubstantiated.
- **Resolution test** Include a comparison of 3SD vs. 3SD-RR on a set of IDR-containing PpI complexes, with metrics such as docking success rate and pose quality, and describe the IDR removal protocol in detail.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "We applied 3SD-RR to the AlphaFold2-predicted receptors, yielding an efficient prediction of PpI pose with high relevance to the experimental data regardless of the presence of IDRs or the availability of receptor structures"
- **Evidence pointer** Abstract; location not provided
- **Concern** The claim of efficient prediction with high relevance to experimental data is not quantified. No correlation coefficients, success rates, or comparisons to experimental structures are provided. The phrase "regardless of the presence of IDRs or the availability of receptor structures" is overly broad and unsupported.
- **Why it matters** The use of AlphaFold2-predicted structures is a significant practical contribution, but the claim of robustness across conditions requires empirical validation. Without data, the generalizability is speculative.
- **Resolution test** Provide a validation set with AlphaFold2-predicted receptors, including cases with and without IDRs, and report quantitative agreement with experimental PpI structures (e.g., interface RMSD, fraction of native contacts).

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract; location not provided
- **Issue** The terms "three-software docking" and "constant quality" are not defined. The former is clear from context, but the latter is ambiguous and could be misinterpreted.
- **Required correction** Define "constant quality" operationally, e.g., as a consistent success rate across a benchmark set, and clarify the abbreviation 3SD at first use.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Method description
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract does not specify how the three software tools are combined (e.g., consensus scoring, ranking aggregation, or selection criteria). This is essential for reproducibility.
- **Required correction** In the full manuscript, describe the combination strategy in detail, including any scoring functions or decision rules used to integrate outputs from CABS-dock, HPEPDOCK, and HADDOCK.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scope
- **Affected element** Generalizability claim
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract claims "constant quality for most targets" and "regardless of the presence of IDRs or the availability of receptor structures," but the scope of "most targets" and the range of tested conditions are not specified.
- **Required correction** Specify the number and diversity of test cases, and qualify claims to reflect the actual benchmark coverage.

## Risk / unsupported claims
- "Ensuring constant quality for most targets" is unsupported without a defined benchmark and success metrics.
- "Enhanced MD performance in proteins having IDRs" is unsupported without comparative data.
- "Efficient prediction of PpI pose with high relevance to the experimental data regardless of the presence of IDRs or the availability of receptor structures" is unsupported without quantitative validation.
- The overall claim of an "improved solution" to PPI docking challenges is not established from the abstract alone.