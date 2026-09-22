## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, supplementary references)
- **Assessment boundary** Scientific content, methodological soundness, database utility, and claims as presented in the provided text
- **Shared manuscript claim summary** The authors present PhaSepDB 3.0, an updated knowledgebase of phase separation-related proteins, built using a novel human-AI collaborative workflow combining an LLM-based agentic system with expert verification. The database contains 3,484 curated entries for 1,849 proteins, more than doubling the previous version. New features include protein-wise summary pages, enriched annotations (functional relevance, intrinsic/extrinsic regulation, experimental evidence), and a redesigned web interface.
- **Visible evidence base** Abstract, Introduction, Materials and Methods (literature collection, AI workflow description, human verification), Results (performance metrics, database content summary, alpha-synuclein example), Discussion, Data availability statement
- **Missing materials affecting confidence** Full figures and tables (Fig. 1A–E, Fig. 2A–E, Table 1, Supplementary Fig. S1, Supplementary Table) are referenced but not provided. Detailed schema definitions, prompt templates, and the full annotation framework structure are not fully described. Quantitative performance metrics are reported but underlying data (e.g., confusion matrices, error analyses) are not shown. The web interface and actual database content cannot be independently assessed from the manuscript text alone.

## Reviewer
- **Overall assessment** This manuscript describes a substantial update to an established and widely used database in the phase separation field. The integration of an LLM-based agentic system with expert verification is timely and potentially transformative for database curation. The reported scale of expansion (more than doubling content) and the new protein-wise summary feature are valuable contributions. However, several methodological details require clarification, particularly regarding the validation of the AI system, the nature of expert verification, and the potential for systematic biases in the curation process. The manuscript would benefit from more rigorous quantitative evaluation of the AI-assisted workflow and clearer documentation of the annotation schema. The database itself appears to be a significant community resource, but the evidence provided in the manuscript text is insufficient to fully assess the reliability and completeness of the curated content.

- **Who would be interested in the results, and why** Researchers studying phase separation, biomolecular condensates, and membraneless organelles would be the primary audience. This includes cell biologists, biophysicists, and biochemists investigating the mechanisms and functions of condensates. Computational biologists developing predictors for phase separation proteins would also benefit from the expanded dataset. Additionally, researchers studying neurodegenerative diseases, cancer, and developmental disorders where aberrant phase separation is implicated would find the disease-relevant annotations valuable. The AI-assisted curation methodology itself may interest bioinformaticians and database curators working on other knowledgebases facing similar literature scalability challenges.

- **Major strengths**
  1. The database represents a significant expansion (more than doubling) of a well-established community resource, addressing a clear need for up-to-date and comprehensive phase separation data.
  2. The novel integration of an LLM-based agentic system with human verification is innovative and addresses the critical challenge of unsustainable manual curation in rapidly growing fields.
  3. The new protein-wise summary pages provide a valuable synthesis feature that addresses knowledge fragmentation, offering users integrated views of a protein's phase separation behavior.
  4. The enriched annotation framework (functional relevance, intrinsic/extrinsic regulation, experimental evidence details) represents a meaningful improvement over previous versions.
  5. The authors provide a concrete example (alpha-synuclein) demonstrating the utility of the integrated data views.
  6. The data availability statement is clear, with both the database and the AI workflow evaluation data publicly accessible.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological soundness
- **Claim pointer** "This agent workflow successfully extracted 91.5% of the entries in the validation set" and "the accuracy for key annotations—such as organism, subcellular location, MLOs, PS-class, and material state—exceeded an average of 70%"
- **Evidence pointer** Results section, Fig. 1B and 1C (figures not provided)
- **Concern** The reported performance metrics are presented without sufficient methodological detail. The definition of "successfully extracted" is unclear. Does this refer to exact match with expert-curated entries, partial match, or something else? The accuracy of 70% for key annotations is concerning, as it suggests that approximately 30% of annotations may be incorrect. The manuscript does not describe how these accuracy metrics were calculated, what the error patterns were, or how errors were corrected during the human verification process. Furthermore, the validation set of 50 publications is relatively small, and the test set of 382 publications is described but no performance metrics for the test set are provided in the text.
- **Why it matters** The reliability of the entire database depends on the accuracy of the AI extraction and the effectiveness of the human verification process. Without clear definitions of performance metrics and a detailed error analysis, readers cannot assess the quality of the curated data. The 70% annotation accuracy is particularly concerning for a database intended to serve as a reference resource.
- **Resolution test** Provide clear definitions of all performance metrics, include a detailed error analysis (e.g., confusion matrices for each annotation type), report test set performance explicitly, and describe the specific criteria used for human verification decisions. Ideally, provide an inter-annotator agreement measure between the AI system and human curators.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Data quality and completeness
- **Claim pointer** "All collected data in PhaSepDB were at least double checked by different expert curators to ensure accurate annotations"
- **Evidence pointer** Materials and Methods, "Human Verification" section; location not provided
- **Concern** The description of the human verification process is insufficiently detailed. The manuscript states that entries are "independently reviewed by two different curators" but does not describe: (1) the qualifications and expertise of the curators, (2) the specific criteria used for approval or rejection, (3) the inter-annotator agreement rate between curators, (4) how disagreements were resolved, (5) the time required per entry, or (6) the proportion of entries that were rejected or required substantial modification. The claim that data were "double checked" is vague and does not provide confidence in the quality control process.
- **Why it matters** The credibility of a curated database depends on the rigor and transparency of its quality control process. Without detailed documentation of the verification workflow, users cannot assess the reliability of individual entries. The "double checked" claim is a key selling point of the database but is not substantiated with sufficient evidence.
- **Resolution test** Provide a detailed description of the human verification workflow, including curator qualifications, approval criteria, disagreement resolution procedures, and quantitative measures of inter-annotator agreement. Report the proportion of AI-generated entries that were accepted without modification, accepted with minor edits, or rejected.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance and novelty
- **Claim pointer** "we have implemented a novel human-AI collaborative workflow that integrates a large language model (LLM)-based agentic system with expert verification"
- **Evidence pointer** Materials and Methods, "LLM-based Agentic System" section; Results, "Performance of the AI-assisted curation workflow" section
- **Concern** While the use of LLMs for database curation is timely, the novelty of the approach is not clearly established. The manuscript does not compare the proposed workflow with other AI-assisted curation methods or with the manual curation approach used in previous versions. The choice of DeepSeek-V2 as the underlying LLM is not justified, and no comparison with alternative models (e.g., GPT-4, Claude) is provided. The prompt engineering process is described only briefly, and the specific prompts are not shown. The claim of "novel" is not supported by a thorough literature review or comparative analysis.
- **Why it matters** For a methods-focused contribution, the novelty and superiority of the proposed approach must be clearly demonstrated. If similar AI-assisted curation workflows have been described elsewhere, the contribution is incremental rather than novel. The lack of comparative analysis makes it difficult to assess whether the specific choices made (LLM, framework, prompt design) are optimal.
- **Resolution test** Provide a more thorough comparison with existing AI-assisted curation approaches, justify the choice of DeepSeek-V2 over alternatives, and include a comparative evaluation (e.g., accuracy, cost, speed) against at least one alternative LLM or curation method.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "The database now provides granular details for 9,257 experimental evidence records, capturing the specific protein constructs, cell lines, and conditions"
- **Evidence pointer** Results, "Database content summary and website" section; Fig. 2D (figure not provided)
- **Concern** The manuscript does not describe the schema or structure of the experimental evidence records. It is unclear what specific fields are captured (e.g., protein construct details, cell lines, experimental conditions, assay types), how these are standardized across different publications, and how the authors handle the inherent heterogeneity in experimental reporting across the literature. The lack of a clear data model for the evidence records raises questions about the consistency and comparability of the curated data.
- **Why it matters** The utility of the database for downstream analyses (e.g., training predictive models, meta-analyses) depends on the consistency and completeness of the underlying data. Without a clear description of the data schema and standardization procedures, users cannot fully exploit the evidence records or assess potential biases.
- **Resolution test** Provide a detailed description of the evidence record schema, including field definitions, controlled vocabularies, and standardization procedures. Include examples of how heterogeneous experimental data from different publications are harmonized into the common schema.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and completeness
- **Affected element** Literature search strategy
- **Evidence pointer** Materials and Methods, "Literature collection" section
- **Issue** The search strategy is described as using the same keywords as previous versions, but the search period (April 1, 2022 to April 20, 2025) is not justified. It is unclear why this specific date range was chosen and whether any publications before April 2022 that were not captured in previous versions were considered.
- **Required correction** Provide a brief justification for the search date range and clarify whether any supplementary searches were conducted to capture publications missed in previous versions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** AI workflow implementation
- **Evidence pointer** Materials and Methods, "LLM-based Agentic System" section
- **Issue** The manuscript mentions the use of the CrewAI framework and DeepSeek-V2 API but does not provide version numbers, configuration details, or the specific prompts used. This limits the reproducibility of the workflow.
- **Required correction** Provide version information for all software components and include the final prompts used in the validation set as supplementary material.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Performance evaluation
- **Evidence pointer** Results, "Performance of the AI-assisted curation workflow" section
- **Issue** The performance metrics are reported as single values without confidence intervals or measures of variability. The validation set of 50 publications is small, and the reported 91.5% extraction rate and 70% annotation accuracy may have wide confidence intervals.
- **Required correction** Report confidence intervals for all performance metrics and consider bootstrapping or other resampling methods to quantify uncertainty.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** User guidance
- **Affected element** Database usage
- **Evidence pointer** Results, "Database content summary and website" section
- **Issue** The manuscript describes the database features but does not provide specific guidance on how users should interpret the different entry types (PS-self vs. PS-other) or how to use the protein-wise summary pages effectively. The alpha-synuclein example is helpful but limited.
- **Required correction** Add a brief "How to use" section or user guide describing best practices for querying and interpreting the database content.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness of comparison
- **Affected element** Related databases
- **Evidence pointer** Introduction, paragraph 1
- **Issue** The introduction mentions "other key resources" (references 9–12) but does not provide a systematic comparison of PhaSepDB 3.0 with these databases in terms of content, features, or curation methodology.
- **Required correction** Add a table or paragraph comparing PhaSepDB 3.0 with other phase separation databases, highlighting the unique contributions and improvements.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Data accessibility
- **Affected element** Download options
- **Evidence pointer** Data availability statement
- **Issue** The data availability statement mentions the database website and a Zenodo repository for the AI workflow evaluation data, but it is unclear whether the full database content is available for bulk download (e.g., as flat files or an API).
- **Required correction** Clarify the data access options, including whether bulk downloads or programmatic access (API) are available.

## Risk / unsupported claims
- The claim that the AI-assisted workflow is "reliable, efficient, and effective" is not fully supported by the evidence presented. The reported 70% annotation accuracy suggests a substantial error rate that requires more detailed analysis.
- The claim that the database provides "comprehensive" coverage of phase separation-related proteins is difficult to assess without knowing the total number of publications screened versus those included, and the criteria for inclusion beyond "experimental validation."
- The statement that the protein-wise summary pages offer "a comprehensive, at-a-glance overview" is a qualitative claim that is not empirically validated.
- The claim that the workflow enables "a scalable and sustainable solution for developing scientific knowledgebases" is forward-looking and not directly supported by the data presented.
- The performance comparison between the validation set and test set is mentioned but test set results are not reported in the text, making the generalizability claim unverifiable from the provided material.
- The specific numbers of entries per protein, the distribution of PS-self vs. PS-other classifications, and the breakdown of organisms represented are not provided, limiting the ability to assess the database's scope and potential biases.