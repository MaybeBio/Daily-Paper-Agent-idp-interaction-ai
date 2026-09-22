## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results and discussion, methods, figure legends, and supplementary figure/table descriptions.
- **Assessment boundary** Scientific validity, methodological rigor, data interpretation, and clarity of claims as presented in the provided manuscript. No assessment of editorial fit or journal-specific policy.
- **Shared manuscript claim summary** The authors present a second-generation proteomic peptide phage display (ProP-PD) library (HD2) tiling the intrinsically disordered regions (IDRs) of the human proteome, with ~1,000,000 overlapping peptides. They report screening against 35 bait domains, identifying 2,161 potential SLiM-mediated interactions, benchmarking against known motifs, validating a subset via biophysical and cell-based assays, and providing PepTools for annotation. They claim the method provides amino-acid-resolution binding site footprinting and can pinpoint disease mutations and phosphorylation events.
- **Visible evidence base** Abstract, full introduction, results and discussion sections (including design, construction, quality control, selection metrics, benchmarking, affinity validation, NLS functional assays, and mutation/phosphorylation analyses), online methods, and descriptions of supplementary figures and tables. No raw data, full figures, or supplementary tables were provided for independent verification.

## Reviewer
- **Overall assessment** This manuscript describes a substantial technical advance in the field of SLiM-based interaction discovery. The HD2 library design is thoughtful, and the systematic evaluation of selection parameters is commendable. The benchmarking against known motifs and the inclusion of functional validation for KPNA4 NLSs strengthen the claims. However, several concerns regarding data completeness, statistical rigor, and generalizability of the conclusions need to be addressed. The manuscript would benefit from clearer presentation of certain methodological details and a more cautious interpretation of some results, particularly regarding the confidence scoring system and the biological relevance of the identified interactions.

- **Who would be interested in the results, and why** Researchers in the fields of protein-protein interactions, intrinsically disordered proteins, cell signaling, and proteomics would find this resource valuable. The HD2 library and PepTools provide a scalable platform for identifying SLiM-mediated interactions with binding site resolution, which is of broad interest for understanding cellular regulation and for prioritizing disease-associated variants. The methodological guidelines for ProP-PD will also be useful for groups adopting this technique.

- **Major strengths**
  1. The HD2 library represents a significant improvement over the first-generation HD1 library, with better coverage and quality control, as evidenced by the high percentage of designed sequences recovered.
  2. The systematic evaluation of display formats (P8 vs. P3), library sub-pools, and comparison to combinatorial libraries provides valuable practical guidance for the field.
  3. The inclusion of a benchmarking dataset and the use of multiple metrics (replication, overlap, motif enrichment) to assign confidence levels is a rigorous approach to filtering high-throughput phage display data.
  4. The functional validation of NLSs in cell-based assays, including full-length protein context, adds biological credibility to the identified interactions.
  5. The integration of disease mutations and phosphorylation sites with binding site information demonstrates a clear path toward biological and clinical relevance.

- **Major Concerns**

  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Data completeness and reproducibility
  - **Claim pointer** The authors claim the HD2 library allows screening of ~1,000,000 overlapping peptides in a single binding assay and that the library covers all IDRs of the human proteome.
  - **Evidence pointer** Results section "Design of the HD2 phage library"; Online methods "Computational ProP-PD library design"; SI Table S1
  - **Concern** The manuscript states the library contains 938,427 peptides from 16,969 proteins covering 4,442,952 residues, but the criteria for defining IDRs, the specific thresholds used (e.g., IUPred score cut-off), and the handling of protein isoforms are not fully detailed. The claim of "all IDRs" is strong, and the completeness of coverage relative to the total predicted disordered proteome is not quantified. Additionally, the redundancy and potential biases in the library (e.g., peptide length, amino acid composition) are not fully discussed.
  - **Why it matters** Without a clear definition of the search space and coverage metrics, the generalizability and completeness of the library cannot be assessed. This is critical for users who may rely on this resource for proteome-wide studies.
  - **Resolution test** Provide a detailed breakdown of the IDR prediction method, the number of proteins and residues considered disordered, and the percentage of these residues covered by the library. Include an analysis of potential biases in peptide representation (e.g., length distribution, amino acid composition) and discuss how these might affect selection outcomes.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Statistical rigor of confidence scoring
  - **Claim pointer** The authors define a "Confidence level" score with four categories (High, Medium, Low, Filtered) based on four binary criteria, and use this to filter and rank results.
  - **Evidence pointer** Results section "Evaluation of metrics for ranking of ProP-PD results and defining confidence levels"; Figure 3
  - **Concern** The method for combining the four metrics into a single confidence score is not fully described. It is unclear whether the criteria are weighted, how the cut-offs for each metric were determined (beyond Youden's J), and whether the confidence levels are calibrated against a gold standard. The authors report that the high-confidence set has higher precision but lower recall, but the trade-off is not quantified in a way that allows users to make informed decisions.
  - **Why it matters** The confidence score is a key output of the pipeline and will be used by others to prioritize interactions. A lack of transparency in its derivation undermines its utility and comparability across studies.
  - **Resolution test** Provide a detailed description of the scoring algorithm, including the exact cut-offs for each metric, how they were optimized, and a validation of the confidence levels against an independent set of known interactions. Consider providing a continuous score or a probabilistic framework rather than discrete categories.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Generalizability of benchmarking results
  - **Claim pointer** The authors benchmark the HD2 library against a set of 337 known SLiM-mediated interactions and report a recall of 19.3%.
  - **Evidence pointer** Results section "Phage selections"; SI Table S4
  - **Concern** The benchmarking set is compiled from ELM and PDB, which may be biased toward well-studied motifs and domains. The recall of 19.3% is relatively low, and the authors do not thoroughly discuss the reasons for this, such as the possibility that many known motifs are not represented in the library due to length constraints or that the selection conditions are not optimal for all bait domains. The comparison to HD1 is mentioned but not fully detailed.
  - **Why it matters** The recall rate is a key indicator of the library's sensitivity. A low recall may suggest that the library is missing a substantial fraction of true interactions, which would limit its utility for discovery.
  - **Resolution test** Provide a more detailed analysis of the benchmarking results, including a breakdown of recall by motif class, bait domain, and peptide length. Discuss potential reasons for missed interactions and suggest how the library or protocol could be modified to improve sensitivity.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Validation of novel interactions
  - **Claim pointer** The authors report 2,161 potential SLiM-mediated interactions and validate a subset of 38 by biophysical or cell-based assays.
  - **Evidence pointer** Results section "Validation of SLiM-based interactions through affinity measurements"; Figure 4; SI Table S5
  - **Concern** The validation rate is not clearly stated. Of the 38 tested interactions, how many were confirmed? The authors show affinity data for a few examples, but the overall success rate is not reported. Additionally, the criteria for selecting which interactions to validate are not described, which could introduce selection bias.
  - **Why it matters** The validation rate is a critical measure of the precision of the method. Without this information, the reliability of the remaining ~2,100 interactions is uncertain.
  - **Resolution test** Report the number of tested interactions that were confirmed as binders, the range of affinities observed, and the criteria for selecting interactions for validation. Discuss the potential false positive rate and how users should interpret the confidence levels in light of this.

  - **Concern ID** R1-M5
  - **Severity** Major
  - **Blocking** No
  - **Axis** Functional relevance of disease mutations and phosphorylation
  - **Claim pointer** The authors show that disease mutations and phosphorylation sites can be mapped to binding sites and that some mutations affect binding affinity.
  - **Evidence pointer** Results section "Exploring the effects of mutations and phosphorylation on the motif-based PPI network"; Figure 7
  - **Concern** The analysis is largely descriptive. The authors demonstrate that mutations can affect binding, but they do not systematically assess the predictive power of their approach for identifying functionally relevant variants. The number of tested mutations is small, and the biological consequences of the observed affinity changes are not explored.
  - **Why it matters** The claim that the method can "pinpoint functionally important disease mutations" is a strong one. A more systematic analysis would strengthen this claim and provide a framework for users.
  - **Resolution test** Provide a more comprehensive analysis of the overlap between binding sites and disease mutations/phosphorylation sites, including a statistical assessment of enrichment. For a subset of mutations, test the effect on binding and, if possible, link the affinity changes to cellular phenotypes.

- **Minor Comments**

  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity of figure presentation
  - **Affected element** Figure 3
  - **Evidence pointer** Results section "Evaluation of metrics for ranking of ProP-PD results and defining confidence levels"
  - **Issue** The ROC curves and the derivation of cut-offs are mentioned but not shown in the provided text. The figure is referenced but not available for review.
  - **Required correction** Ensure that Figure 3 clearly shows the ROC curves, the chosen cut-offs, and the resulting precision-recall trade-off. Add a schematic of the confidence scoring workflow.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Terminology consistency
  - **Affected element** Abstract and Results
  - **Evidence pointer** Abstract; Results section "Phage selections"
  - **Issue** The abstract states "35 known SLiM-binding domains" while the results mention "34 bait proteins representing 30 distinct domain families" and later "35 non-control baits." The numbers are inconsistent.
  - **Required correction** Clarify the exact number of baits used and ensure consistency throughout the manuscript.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Discussion of limitations
  - **Affected element** Concluding remarks
  - **Evidence pointer** Concluding remarks section
  - **Issue** The authors acknowledge the limitation of peptide length for capturing certain motifs, but they do not discuss other potential limitations, such as the lack of post-translational modifications in the library or the potential for false negatives due to the in vitro nature of the assay.
  - **Required correction** Add a more comprehensive discussion of the limitations of the approach and how they might be addressed in future iterations.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Data availability
  - **Affected element** Data availability section
  - **Evidence pointer** Data availability section
  - **Issue** The authors state that data is available online, but the specific format and any restrictions on use are not described.
  - **Required correction** Provide a clear description of the data files, their format, and any usage restrictions.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Statistical reporting
  - **Affected element** Results section "Selection metrics"
  - **Evidence pointer** Results section "Selection metrics for the HD2 P8 library"
  - **Issue** P-values are reported for enrichment of shared peptides, but the statistical test used is not described.
  - **Required correction** Specify the statistical test used and the correction for multiple testing, if any.

## Risk / unsupported claims
- The claim that the HD2 library allows "proteome-scale amino-acid resolution footprinting" is supported by the data, but the completeness of coverage and the sensitivity of the method are not fully quantified.
- The claim that the method can "pinpoint functionally important disease mutations" is not fully supported by the limited number of mutations tested. The analysis is suggestive but not conclusive.
- The claim that the HD2 library is an "optimized" version of HD1 is supported by the improved coverage, but a direct head-to-head comparison of performance (e.g., number of known motifs recovered) is not provided.
- The generalizability of the confidence scoring system to other bait domains and experimental conditions is not established.