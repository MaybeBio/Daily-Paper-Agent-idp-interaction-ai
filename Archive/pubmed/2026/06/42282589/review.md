## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, limitations) without supplementary figures, tables, or SI notes
- **Assessment boundary** Scientific claims, methodological soundness, and evidence quality as presented in the provided text; experimental validation claims assessed from textual description only
- **Shared manuscript claim summary** The authors present a machine learning framework that inverts physics-based coarse-grained models to design intrinsically disordered proteins (IDPs) with tailored ensemble properties, including stimuli-responsive conformational changes, multicomponent condensate behaviors, and selective localization in living cells
- **Visible evidence base** Main text figures referenced (Figs. 1-4), supplementary figures referenced (Figs. S1-S10), supplementary tables referenced (Table S1), SI notes referenced (Notes 1-4), but none of these materials were provided
- **Missing materials affecting confidence** All figures, supplementary information, SI notes, and experimental protocols; sequence data; computational code; detailed methods

## Reviewer
- **Overall assessment** This manuscript presents a conceptually appealing framework for IDP design by inverting physics-based models, with demonstrations spanning in silico predictions and preliminary cellular validation. The core idea of differentiable inversion of coarse-grained IDP models is timely and potentially impactful. However, the provided text alone does not permit verification of the central claims. Key methodological details, quantitative results, and experimental evidence are relegated to supplementary materials that were not available for review. The cellular validation section, while promising, is described at a level that precludes assessment of statistical robustness or biological significance. The framework's novelty relative to existing IDP design approaches is not fully contextualized. The manuscript would benefit from clearer articulation of design success rates, quantitative benchmarks against existing methods, and more rigorous statistical treatment of the cellular data.

- **Who would be interested in the results, and why** Researchers in protein design and engineering, particularly those working on disordered proteins; computational biologists developing generative models for biomolecules; synthetic biologists interested in programmable condensate formation; cell biologists studying biomolecular condensates and their dysfunction in disease. The framework's scalability and model-agnostic design could attract broad interest from the protein biophysics community.

- **Major Strengths** 
  1. The conceptual advance of inverting physics-based models for IDP design is timely and addresses a recognized gap in the field
  2. The framework demonstrates flexibility across multiple design objectives (single-chain properties, multicomponent mixtures, cellular localization)
  3. The inclusion of cellular validation, even if preliminary, strengthens the translational relevance
  4. The computational efficiency claims (proteome-scale design in minutes) are practically significant
  5. The authors acknowledge model limitations honestly in the Discussion

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "We first program IDPs to tunably sense and respond to diverse biophysical cues and show that IDP ensembles can directly encode complex signal processing, including threshold detection, bandpass filtering, and Boolean-type multi-input logic"
- **Evidence pointer** Figure 2, Table S1, SI Note 1 (location not provided)
- **Concern** The central claim of programmable signal processing by designed IDPs rests entirely on computational predictions validated by molecular dynamics simulations. However, none of the quantitative data, simulation parameters, or design success rates are visible in the provided text. The claim that these designs "encode" logic operations requires demonstration that the designed sequences robustly and reproducibly achieve the specified response profiles across multiple independent design runs and simulation conditions. Without access to the actual response curves, error bars, or statistical comparisons, this claim cannot be evaluated.
- **Why it matters** The signal processing demonstrations are a headline contribution. If the design success rate is low or the responses are noisy, the practical utility of the framework for this application is questionable. The current text provides only qualitative descriptions ("large changes in Rg (~25%)") without statistical context.
- **Resolution test** Provide the actual response curves for threshold, bandpass, and logic gate designs with error estimates across multiple independent design attempts. Report design success rates and demonstrate reproducibility across different random seeds and initial conditions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental validation rigor
- **Claim pointer** "Consistent with predictions, we find that de novo clients partition into while de novo excluders are selectively depleted from the condensate" and "we found that FUS LC condensates were enriched for clients relative to the nuclear background and depleted for excluders"
- **Evidence pointer** Figure 4, Figures S9-S10, SI Note 4 (location not provided)
- **Concern** The cellular validation is described with minimal quantitative detail. The text mentions "3 × 3 μm box" intensity measurements and radial distributions, but provides no information on number of cells analyzed, number of independent biological replicates, statistical tests used, or effect sizes. The statement that "the extent of depletion for excluders is generally not as strong as that for recruitment" suggests potential asymmetry that is not explained. Additionally, the choice of only 2 de novo and 2 biological sequences for validation is a very small sample size.
- **Why it matters** The cellular experiments are the only direct biological validation of the design framework. If the statistical power is insufficient or the effects are modest, the claim of "programmable design" in living cells is overstated. The asymmetry between enrichment and depletion also raises questions about the design principles.
- **Resolution test** Report cell numbers, biological replicates, statistical methods, and effect sizes for all localization measurements. Provide a power analysis justifying the sample size. Address the enrichment/depletion asymmetry explicitly.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Novelty and benchmarking
- **Claim pointer** "Here we present a machine learning framework for proteome-scale de novo IDP design by rationally inverting physics-based models"
- **Evidence pointer** Introduction, Results (Model framework) (location not provided)
- **Concern** The manuscript does not clearly position its contribution relative to existing IDP design methods. While the authors mention that physics-based models "remain challenging to invert," they do not systematically compare their approach to prior IDP design strategies, such as sequence statistics-based methods, generative models, or other inverse approaches. The claim of novelty requires explicit benchmarking against existing tools and demonstration of superior performance or unique capabilities.
- **Why it matters** Without proper benchmarking, the reader cannot assess whether this framework represents a genuine advance or an incremental contribution. The field of protein design is rapidly evolving, and claims of scalability and flexibility need quantitative comparison to alternatives.
- **Resolution test** Include a systematic comparison with at least 2-3 existing IDP design methods on common benchmarks, reporting design success rates, computational cost, and property accuracy. Discuss specific advantages and limitations relative to each.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability and model dependence
- **Claim pointer** "Our framework is model-agnostic" and "it should be noted that the accuracy of any design... is ultimately dependent on the accuracy of the model it was designed over"
- **Evidence pointer** Results (Model framework), Discussion (Limitations) (location not provided)
- **Concern** The authors claim model-agnosticism but only demonstrate the framework with three specific coarse-grained models (dimer, FINCHES, RPA) and three force fields (CALVADOS, Mpipi-GG, HPS). The text does not clarify whether the framework can accommodate fundamentally different model types (e.g., all-atom simulations, machine-learned potentials) or whether the differentiable implementation is specific to the functional forms of the tested models. The scalability claim (10000 sequences in <1 minute) appears to be for a specific model and hardware configuration.
- **Why it matters** The generalizability claim is important for the framework's broader utility. If the differentiable inversion only works for certain model architectures, the "model-agnostic" claim is overstated.
- **Resolution test** Demonstrate the framework with at least one structurally different model type or provide a clear analysis of which model features are required for differentiable inversion. Report hardware specifications for scalability claims.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Biological relevance of design metrics
- **Claim pointer** "we demonstrate that we can tailor ensemble properties" and "design IDPs that selectively localize in or out of condensates"
- **Evidence pointer** Results sections, Figure 4 (location not provided)
- **Concern** The framework optimizes for physics-based model parameters (e.g., χ, ε) that are proxies for biological function. The text does not establish that the designed sequence properties translate to functional outcomes beyond the specific assays tested. For instance, the cellular localization assay measures partitioning into FUS LC condensates, but the relationship between the optimized interaction parameters and the observed partitioning is not quantitatively established. The biological relevance of the designed sequences for endogenous processes is unclear.
- **Why it matters** The ultimate goal is to design IDPs with useful biological functions. If the design metrics do not reliably predict functional outcomes, the framework's practical utility is limited.
- **Resolution test** Provide quantitative correlation between predicted interaction parameters and measured partitioning coefficients. Discuss how the design metrics relate to known functional properties of IDPs in biological contexts.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract (location not provided)
- **Issue** The abstract claims "proteome-scale de novo IDP design" but the scale of validation is much smaller. The term "proteome-scale" could be misleading without clarification that this refers to computational throughput, not validated designs.
- **Required correction** Clarify in the abstract that proteome-scale refers to computational generation capacity, with experimental validation performed on a smaller subset.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods description
- **Evidence pointer** Results (Model framework), SI Notes (location not provided)
- **Issue** The text states that designs were "validated through explicit molecular dynamics simulations" but provides no simulation protocol details in the main text. The SI notes are referenced but not available.
- **Required correction** Include a brief summary of simulation parameters (force field, temperature, salt concentration, simulation length, number of replicates) in the main text or ensure SI notes are accessible.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Cellular quantification
- **Evidence pointer** Figure 4, Figure S10 (location not provided)
- **Issue** The text mentions "averaged protein intensities" and "radial distribution" but does not report variability measures or statistical comparisons in the main text.
- **Required correction** Add at least a sentence summarizing the statistical approach and key quantitative results (e.g., mean enrichment/depletion ratios with confidence intervals) in the main text.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "Boolean-type multi-input logic"
- **Evidence pointer** Abstract, Results (Figure 2) (location not provided)
- **Issue** The term "Boolean-type" is vague. The text describes OR, XOR, and NAND gates, which are standard Boolean functions. The qualifier "type" is unnecessary and potentially confusing.
- **Required correction** Use standard terminology "Boolean logic" or specify the exact gates implemented.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Contextualization
- **Affected element** Comparison to prior work
- **Evidence pointer** Introduction (location not provided)
- **Issue** The introduction mentions "growing interest to design de novo IDPs" but does not cite or discuss specific prior attempts at IDP design, making it difficult to assess the novelty of the approach.
- **Required correction** Add a brief paragraph summarizing prior IDP design efforts and explicitly stating how this work differs.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Data availability
- **Evidence pointer** Data and code availability (location not provided)
- **Issue** The statement "available along with manuscript and/or github" is vague. It is unclear what exactly is deposited where.
- **Required correction** Specify precisely which data, sequences, and code are available at which locations, with accession numbers or DOIs where applicable.

## Risk / unsupported claims
- The claim of "proteome-scale" design capability is unsupported without details on the computational cost per sequence and the hardware used
- The claim that designed IDPs "encode complex signal processing" is not verifiable without the actual response curves and statistical analyses
- The claim of "model-agnostic" framework is not fully supported as only three related coarse-grained models were tested
- The biological relevance of the designed IDPs beyond the specific FUS LC assay is not established
- The statement that designed IDPs are "largely distinct" from human IDPs requires quantitative metrics of sequence dissimilarity that are not provided
- The claim that the framework "establishes a flexible and scalable strategy" is premature given the limited experimental validation (2 de novo sequences tested in cells)
- The relationship between optimized physics-based parameters and observed cellular behavior is not quantitatively established