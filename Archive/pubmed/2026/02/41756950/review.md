## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, methods, and supplementary figure/table legends
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and technical soundness as presented in the provided text. No external data or unpublished materials were consulted.
- **Shared manuscript claim summary** The authors propose that recurrent truncating mutations in the epigenetic regulator ASXL1, which are prevalent in myeloid malignancies, promote cancer through the aberrant gain of phase-separated condensate formation. They argue that the wild-type protein suppresses this intrinsic condensation property via a negatively charged, frequently deleted region, and that disease mutations escape this regulation to form nuclear condensates that concentrate BAP1, enhance H2A deubiquitination, and activate leukemogenic transcriptional programs.
- **Visible evidence base** Cell-based imaging of fluorescently tagged ASXL1 constructs; in vitro condensation assays with purified protein fragments; CRISPR-tagged endogenous ASXL1 in K562 cells; patient bone marrow staining; in vitro nucleosome deubiquitination assays; colony formation assays in mouse bone marrow; a mouse transplant model; RNA-seq and transposable element analysis; coarse-grained molecular dynamics simulations; fluorescence correlation spectroscopy.
- **Missing materials affecting confidence** Figures and extended data figures are referenced but not provided in the text. Numerical values for key quantifications (e.g., colocalization coefficients, partition coefficients, survival statistics, RNA-seq effect sizes) are not available. Supplementary tables are described but their contents are not included. The specific details of the MD simulation force field reparameterization and validation are incomplete.

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question: how recurrent mutations in disordered regions of a chromatin regulator drive malignancy. The central hypothesis, that ASXL1 truncations promote cancer through dysregulated phase separation, is conceptually novel and mechanistically plausible. The authors provide a multi-pronged approach spanning cell biology, biochemistry, genomics, and simulation. However, the strength of the conclusions depends critically on data that are not visible in the provided text. The key claim that condensation is causally required for oncogenic activity rests on a limited set of separation-of-function mutants, and the quantitative rigor of the imaging and biophysical analyses cannot be assessed without the figures. The manuscript is potentially significant but currently not fully established from the provided evidence.
- **Who would be interested in the results, and why** Hematologists and oncologists studying myeloid malignancies, particularly those focused on ASXL1 mutations and clonal hematopoiesis. Epigeneticists interested in the role of IDRs and phase separation in chromatin regulation. Cancer biologists studying gain-of-function mechanisms in epigenetic regulators. Biophysicists and computational biologists working on biomolecular condensates and their prediction from sequence.
- **Major strengths**
  1. The study addresses a clinically important and mechanistically unresolved problem: why truncating mutations in a disordered region of ASXL1 are among the most frequent alterations in myeloid cancers.
  2. The finding that the wild-type protein suppresses condensation via a negatively charged region, and that truncation relieves this suppression, is a conceptually interesting and potentially generalizable mechanism for IDR mutations.
  3. The combination of in vitro biochemistry, cell-based imaging, endogenous tagging, patient samples, and in vivo mouse modeling provides a broad evidence base.
  4. The inclusion of molecular dynamics simulations to support the proposed conformational mechanism adds a valuable theoretical layer.
  5. The correlation between mutation frequency, condensation propensity, and leukemogenic activity across a series of patient mutations is a compelling argument for clinical relevance.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Causal evidence
  - **Claim pointer** The authors claim that condensation is "crucially important" for the oncogenic activity of ASXL1 mutants, based on the loss of function in condensation-defective mutants.
  - **Evidence pointer** Results section "Condensates of ASXL1 truncations promote H2A deubiquitination by enriching BAP1 activity" and "Condensates of ASXL1 truncations promote myeloid malignancies"; Extended Data Figures 2, 3, 6; Figure 3
  - **Concern** The causal link between condensation and oncogenic activity rests on the behavior of a small number of point mutants (e.g., 10RA, 25RA). The text states that 10RA "reduced but did not abolish" foci formation, yet it "significantly impaired" H2A deubiquitination and colony formation. This partial reduction in condensation leading to substantial loss of function could indicate a threshold effect, but it could also indicate that the arginine mutations affect other molecular interactions independent of phase separation. The 25RA mutant disrupts BAP1 binding, confounding interpretation. The manuscript does not demonstrate that the oncogenic activity of the mutants is specifically dependent on the condensate state rather than on other properties of the truncated protein, such as altered protein-protein interactions or stability.
  - **Why it matters** The central thesis is that condensation is the driver of oncogenesis. Without a clean separation of condensation from other biochemical activities, the causal claim is not established. This is the difference between a mechanistic insight and a correlation.
  - **Resolution test** The authors should provide a mutant that abolishes condensation without affecting BAP1 or BRD4 binding, and show that this mutant is also defective in oncogenic activity. Alternatively, they could demonstrate that forced condensation of a non-oncogenic ASXL1 fragment (e.g., via an engineered oligomerization domain) is sufficient to drive leukemogenic phenotypes.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Quantitative evidence
  - **Claim pointer** The authors claim that ASXL1 truncations form "dynamic nuclear co-condensates" with BAP1, BRD4, and RNA Pol II, and that these condensates are sites of active transcription.
  - **Evidence pointer** Results section "Endogenous ASXL1 truncations form co-condensates with proteins for transcription activation"; Figure 1g–k; Extended Data Figure 1e, f
  - **Concern** The text describes colocalization and FRAP recovery but provides no quantitative metrics. The degree of overlap between ASXL1 foci and BAP1, BRD4, or Pol II is not given as a coefficient or percentage. The FRAP recovery is described as "seconds" but the half-time, mobile fraction, and statistical comparison to controls are not reported. The claim that these are "co-condensates" implies a shared phase, but the data as described could be consistent with simple enrichment or proximity. The functional significance of the colocalization is inferred but not directly tested.
  - **Why it matters** The model proposes that condensates act as hubs that concentrate BAP1 activity. The quantitative nature of this concentration and its dynamics are essential to support the model. Without numbers, the reader cannot judge the strength of the effect or compare it to known condensate systems.
  - **Resolution test** Provide quantitative colocalization analysis (e.g., Pearson or Manders coefficients) with appropriate controls, FRAP curves with fitted parameters and statistics, and ideally a demonstration that BAP1 enzymatic activity is locally enhanced within the condensates.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Model generalizability
  - **Claim pointer** The authors suggest that "dysregulation of condensation may be a key mechanism for some of the prevalent hotspot disease mutations in the disordered proteomes."
  - **Evidence pointer** Discussion section
  - **Concern** This is a broad generalization based on a single protein. While the authors show a correlation between mutation frequency and condensation propensity for ASXL1 mutants, they do not provide evidence that this mechanism applies to other IDR-mutated proteins. The statement in the abstract and discussion goes beyond the data presented.
  - **Why it matters** The title and framing of the paper suggest a general principle. Overstating the generalizability could mislead the field and dilute the specific, well-supported findings on ASXL1.
  - **Resolution test** Either soften the claim to be specific to ASXL1 and related BAP1-associated factors, or provide preliminary data on another IDR-mutated protein to support the general principle.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical validation
  - **Claim pointer** The authors use coarse-grained MD simulations to support their model that the negatively charged region suppresses condensation by masking the N-terminal region.
  - **Evidence pointer** Methods section "Simulations"; Extended Data Figure 13
  - **Concern** The simulations are described briefly. The reparameterization of the protein-water interaction strength (λ = 1.04) is mentioned but the justification and validation are not provided. The simulation times (5 μs) are short for assessing phase behavior of full-length proteins. The conversion of simulation observations to the proposed "masking" mechanism is qualitative. It is unclear whether the simulations are predictive or merely consistent with the experimental data.
  - **Why it matters** The simulations are used to provide molecular-level insight into the mechanism. If the simulation methodology is not rigorously validated, the mechanistic interpretation is weakened.
  - **Resolution test** Provide validation of the simulation parameters against experimental condensation data, show convergence of the simulations, and ideally perform simulations with the charge-neutralizing mutants to demonstrate the predicted conformational changes.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Introduction, paragraph 1
  - **Evidence pointer** Location not provided
  - **Issue** The statement "research in analyses, identification, and functional understanding of disease mutations in IDRs has far been lagging behind that of structured domains" is grammatically awkward and could be clearer.
  - **Required correction** Rephrase for clarity, e.g., "functional understanding of disease mutations in IDRs lags far behind that of structured domains."
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methods, "Cells" section
  - **Evidence pointer** Location not provided
  - **Issue** The cell culture section does not specify the authentication or mycoplasma testing status of the cell lines used.
  - **Required correction** Add a statement on cell line authentication and mycoplasma negativity testing.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Statistical reporting
  - **Affected element** Methods, "Quantification and statistical analysis"
  - **Evidence pointer** Location not provided
  - **Issue** The text states that "All data were expressed as average ± SD" but does not specify the number of independent experiments for each assay or whether the representative images are from one of multiple replicates.
  - **Required correction** Specify the number of independent biological replicates for each experiment in the figure legends.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Data presentation
  - **Affected element** Results, "The negative charges in the frequently deleted region regulate tumorigenic activities of ASXL1"
  - **Evidence pointer** Figure 5
  - **Issue** The text mentions RNA-seq analyses "on samples recovered both before and after colony formation" but the rationale for the two time points and the differences between them are not explained.
  - **Required correction** Clarify the purpose of the two time points and what each is expected to reveal.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Literature context
  - **Affected element** Discussion
  - **Evidence pointer** Location not provided
  - **Issue** The discussion of therapeutic implications for targeting condensates is brief and does not acknowledge the challenges and ongoing debates in the field regarding the druggability of condensates.
  - **Required correction** Expand the discussion to include a balanced view of the feasibility and potential pitfalls of targeting condensates therapeutically.

## Risk / unsupported claims
- The claim that condensation is "crucially important" for oncogenic activity is not fully supported due to the confounding effects of the separation-of-function mutants (R1-M1).
- The claim that ASXL1 truncations form "co-condensates" with transcription machinery is not quantitatively supported without colocalization coefficients and FRAP parameters (R1-M2).
- The generalization that dysregulation of condensation is a key mechanism for hotspot mutations across the disordered proteome is speculative and not supported by data on other proteins (R1-M3).
- The statement that the charge-neutralizing mutations "turned the otherwise non-colonogenic ASXL1 (1-1067) colonogenic" is presented as a key result, but the effect size and statistical significance are not reported in the text.
- The MD simulation results are described as supporting the model, but the validation and convergence of the simulations are not documented, making the mechanistic claims from simulation difficult to evaluate.
- The claim that the wild-type ASXL1 is "diffuse" in cells is based on imaging data that are not shown; the sensitivity of the assay to detect low-level endogenous condensates is not discussed.