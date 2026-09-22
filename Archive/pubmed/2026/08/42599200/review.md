## Review setup
- **Input scope** Full manuscript text (main text, methods, and results sections as provided)
- **Assessment boundary** Scientific and technical evaluation of the proposed hierarchical discrete representation approach for protein conformation generation, based solely on the supplied manuscript text
- **Shared manuscript claim summary** The authors propose a hierarchical VQ-VAE-based tokenization scheme with three levels of discrete codebooks (coarse, mid, fine) to represent protein structures, followed by a coarse-to-fine generative framework (discrete diffusion for coarse tokens, autoregressive refinement for finer levels) that aims to overcome the trade-off between conformational diversity and structural validity observed in single-resolution diffusion models
- **Visible evidence base** Main text sections 1-5, including method description, experimental setup, and results tables/figures referenced but not fully visible; supplementary sections referenced but not provided
- **Missing materials affecting confidence** Full experimental results tables (Tables 1-4), figures (Figs 1-6), supplementary sections A-C, detailed hyperparameter settings, baseline implementation details, and complete evaluation metrics definitions

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting and timely approach to protein conformation generation by introducing hierarchical discrete representations. The motivation is well-articulated, and the coarse-to-fine paradigm is a sensible response to known limitations of single-resolution generative models. However, the provided text lacks sufficient quantitative evidence to fully evaluate the claims. The method description contains several ambiguities and potential technical gaps that need clarification. The experimental validation, as described, appears reasonable in scope but the actual results are not visible in the supplied material, making it impossible to assess whether the stated outperformance claims are substantiated. The writing is generally clear but some sections are under-specified.

- **Who would be interested in the results, and why** Computational structural biologists, machine learning researchers working on generative models for biomolecules, and researchers in protein engineering and drug discovery. The hierarchical discrete representation approach could be of interest to those seeking interpretable and scalable representations of protein structure, and the coarse-to-fine generation paradigm may inspire similar strategies in other biomolecular modeling tasks.

- **Major strengths**
  1. The conceptual framing of protein structure as hierarchical discrete tokens is novel and well-motivated, drawing inspiration from successful VQ-VAE approaches in vision
  2. The coarse-to-fine generation strategy directly addresses a known limitation of single-resolution models, namely the diversity-validity trade-off
  3. The validation of coarse token semantics (Section 4.1) is a thoughtful and important step that connects symbolic diversity to physical flexibility
  4. The evaluation across multiple challenging benchmarks (BPTI MD, apo/holo, fold-switch, PED) demonstrates breadth of applicability

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "Through extensive experiments, we demonstrate that our method outperforms state-of-the-art models such as ESMDiff across challenging benchmark datasets"
- **Evidence pointer** Tables 1-4, Figures 4-6; location not provided in supplied text
- **Concern** The central claim of outperformance cannot be evaluated because the actual numerical results are not visible in the supplied material. The text describes outcomes qualitatively (e.g., "significantly lower JS divergence", "outperformed the single-resolution baseline") but the supporting data tables and figures are not included. Without access to these results, it is impossible to verify the magnitude of improvements, statistical significance, or whether the claims are justified.
- **Why it matters** The primary contribution of this work is empirical: demonstrating that hierarchical discrete representations improve upon existing methods. If the results do not clearly support this claim, the manuscript's value proposition is substantially weakened.
- **Resolution test** Provide the full results tables and figures with numerical values, error bars, and statistical significance tests. The claims of outperformance should be directly verifiable from the presented data.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "The entire VQ-VAE framework is trained end-to-end by minimizing the total loss, which is the sum of losses calculated at each level"
- **Evidence pointer** Section 3.1; location not provided
- **Concern** The loss function is referenced but the actual equation is not shown in the supplied text (appears as a placeholder). The description of the training objective is incomplete. Specifically, it is unclear how the reconstruction loss is computed across multiple hierarchy levels, whether there are commitment losses at each level, and how the gradients flow through the hierarchical quantization process. The stop-gradient operator is mentioned but its role in the multi-level context is not fully explained.
- **Why it matters** The training procedure is fundamental to the method's success. Without a clear specification of the loss terms and their interactions, the method cannot be reproduced or properly evaluated.
- **Resolution test** Provide the complete loss function with all terms explicitly defined, including reconstruction losses, commitment losses, and any weighting factors between levels.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "we employ a stochastic autoregressive sampling with top-k truncation followed by manual re-weighting of the selection probabilities into fixed ratios"
- **Evidence pointer** Section 3.2.3; location not provided
- **Concern** The top-k sampling strategy with "manual re-weighting of the selection probabilities into fixed ratios" is described but the specific ratios and re-weighting scheme are not specified. The text states "top-3 sampling at three specific ratios" but these ratios are not given. This is a critical detail for reproducibility and for understanding how diversity is controlled.
- **Why it matters** The diversity-validity trade-off is central to the paper's contribution. The specific sampling strategy directly determines this trade-off, and without the exact parameters, the approach cannot be replicated or compared fairly.
- **Resolution test** Specify the exact re-weighting ratios used for top-3 sampling and justify their selection. Provide sensitivity analysis showing how results vary with different ratios.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "we intentionally controlled our overall architecture size to match theirs, eliminating unfair advantages from simply scaling up the model"
- **Evidence pointer** Section 4; location not provided
- **Concern** The claim of matched architecture size with ESMDiff is stated but no details are provided on how this matching was achieved. The number of parameters, layer dimensions, and other architectural choices for both models are not specified. Without this information, it is unclear whether the comparison is truly fair.
- **Why it matters** Fair comparison with baselines is essential for the validity of the empirical claims. If the architecture sizes are not genuinely matched, the results could be attributed to model capacity rather than the proposed method.
- **Resolution test** Provide a table comparing architectural details (parameter counts, layer sizes, etc.) between the proposed model and all baselines.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Evidence sufficiency
- **Claim pointer** "we curated an evaluation dataset consisting of 110 entries, ensuring the exclusion of any sequences that overlap with the PDB training set"
- **Evidence pointer** Section 4.4; location not provided
- **Concern** The PED evaluation is described but the results are only summarized qualitatively ("competitive results", "matches the performance of MSA-Subs"). The actual MAE values, comparisons with baselines, and statistical significance are not visible. Additionally, the curation process for the 110 entries is not detailed.
- **Why it matters** IDP modeling is a challenging and important application. The claims about performance on this benchmark need to be substantiated with concrete numbers.
- **Resolution test** Provide the full results for the PED benchmark with numerical values and comparisons against all baselines.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 3.1, equation for tokenization
- **Evidence pointer** Section 3.1; location not provided
- **Issue** The equation for the tokenization process is referenced but not shown in the supplied text. The description of how continuous latent representations are quantized via nearest neighbor search is clear conceptually but the formal notation is missing.
- **Required correction** Include the full equations for the quantization process, including the nearest neighbor search and the stop-gradient operator application.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 4, experimental setup
- **Evidence pointer** Section 4; location not provided
- **Issue** The text mentions "Detailed definitions and descriptions of the evaluation metrics used for each dataset are provided in Supplementary Section B" but this section is not available. Key metrics like TM-ens, RMSD-ens, and Validity are mentioned but not defined in the main text.
- **Required correction** Either provide brief definitions of all metrics in the main text or ensure the supplementary material is accessible for review.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 3.2.1, discrete diffusion description
- **Evidence pointer** Section 3.2.1; location not provided
- **Issue** The description of the discrete diffusion process for coarse token generation is brief. The reference to "Austin et al. 2023" is made but the specific adaptation to protein structure tokens is not detailed. It is unclear how the diffusion process operates on discrete token sequences.
- **Required correction** Provide more detail on the discrete diffusion formulation, including the forward noising process, the reverse denoising process, and how it is adapted for protein structure tokens.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section 4, training details
- **Evidence pointer** Section 4; location not provided
- **Issue** Training details such as number of epochs, learning rate, batch size, and computational resources are not mentioned in the main text. These are essential for reproducibility.
- **Required correction** Include a training details subsection or table with all relevant hyperparameters.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure 3
- **Evidence pointer** Figure 3; location not provided
- **Issue** Figure 3 is referenced as illustrating the tokenization process and the coarse-to-fine generation framework, but the figure itself is not visible. The text description is helpful but the figure would likely clarify the architecture significantly.
- **Required correction** Ensure the figure is included and is self-explanatory with clear labels for all components.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Missing results data prevents verification of the central outperformance claim
  - R1-M2: Incomplete specification of the training loss function
  - R1-M3: Underspecified sampling strategy parameters
  - R1-M4: Lack of architectural comparison details with baselines

- **Assessment against Nature-style criteria**
  - **Originality**: The hierarchical discrete representation approach for protein conformation generation is a novel contribution. While VQ-VAE and hierarchical generation have been explored in other domains, their application to protein structure generation with a coarse-to-fine paradigm appears to be a new direction. The idea of using discrete tokens to capture multi-scale structural information is creative and potentially impactful.
  - **Scientific importance**: Protein conformation generation is a significant challenge in structural biology with implications for drug discovery and understanding protein dynamics. If the method delivers on its promises, it could provide a valuable new tool. However, the importance is contingent on the empirical results being strong and the method being broadly applicable.
  - **Interdisciplinary readership**: The work bridges machine learning and structural biology, and would likely appeal to researchers in both communities. The conceptual framing is accessible, though some technical details may require specialized knowledge. The potential applications in drug discovery and protein engineering broaden the potential readership.
  - **Technical soundness**: The overall approach is technically plausible, but several details are under-specified (loss function, sampling strategy, architectural comparisons). The validation of coarse token semantics is a strength, but the lack of visible results prevents full assessment of technical soundness.
  - **Readability for nonspecialists**: The manuscript is generally well-written and the motivation is clearly articulated. The hierarchical decomposition concept is explained in an accessible way. However, some sections (particularly the method details) assume familiarity with VQ-VAE and diffusion models, which may limit accessibility for structural biologists without machine learning background.

- **Recommendation posture** Currently not established from the provided evidence. The conceptual contribution is promising and the approach is well-motivated, but the missing results data and incomplete method specifications prevent a full evaluation. The manuscript could become publishable if the results substantiate the claims and the technical details are clarified. I would be supportive if the technical concerns are resolved and the full results are made available for review.