## Review setup
- **Input scope** Full manuscript text including main body, appendices, and references
- **Assessment boundary** Scientific claims, methodology, experimental design, statistical analysis, and reproducibility as presented in the provided manuscript
- **Shared manuscript claim summary** The authors propose a novel pretraining objective, masked-position MLM+JEPA, which combines masked language modeling with latent-space prediction at masked positions only, and claim it outperforms MLM-only under matched wall-clock budgets on a 16-task downstream evaluation suite
- **Visible evidence base** Main text Sections 1-7, Appendix A.1-A.10, Tables 1-19, Figures 1-5 (referenced but not fully visible)
- **Missing materials affecting confidence** Actual figures and tables are not provided in the manuscript text; only references to them are visible. The anonymized repository URL is mentioned but not accessible. Full training curves, per-task absolute scores, and statistical details are referenced but not shown in the provided text

## Reviewer
- **Overall assessment** The manuscript addresses a timely and relevant question in protein language model pretraining, namely whether latent-space prediction can complement token-level objectives. The experimental design is thoughtful, with matched wall-clock budgets and multiple backbone families. However, the core claims rest on statistical analyses that are only partially described, and the primary result is presented as a win/loss/tie count rather than effect sizes with confidence intervals. The confound between target position selection and loss function in the headline comparison is acknowledged but not resolved, which limits the interpretability of the main result. The manuscript is well-written and the methodological details are largely clear, but the evidence as presented is insufficient to fully establish the claimed advantages.

- **Who would be interested in the results, and why** Researchers working on protein language model pretraining, self-supervised learning for biological sequences, and foundation models for computational biology. The results are also relevant to the broader self-supervised learning community interested in JEPA-style objectives, particularly those studying whether latent prediction can complement reconstruction-based objectives. The practical implications for continued pretraining of protein models on domain-specific data would interest applied computational biology groups.

- **Major strengths**
  1. The question is well-posed and practically motivated, addressing whether latent prediction can complement MLM under realistic compute constraints
  2. The experimental design includes multiple backbone families, pretrained and random-init settings, and matched wall-clock budgets, which strengthens the generalizability of the findings
  3. The authors are transparent about limitations, including the confound between target position and loss function, and the lack of repeated pretraining seeds for all conditions
  4. The downstream evaluation suite is diverse, covering regression, classification, and retrieval tasks
  5. The finding that all-position JEPA does not reproduce masked-position gains is an important negative result that helps isolate the mechanism

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical validity
- **Claim pointer** The claim that masked-position MLM+JEPA wins 10/3/3 tasks on pretrained ESM2-35M and 11/2/3 on ESM2-150M, with both rejecting H0 at alpha = 0.05
- **Evidence pointer** Section 4.1, Table 1
- **Concern** The primary statistical evidence is based on sign tests over per-task deltas, but the manuscript does not report effect sizes, confidence intervals, or the magnitude of per-task improvements. A win/loss/tie count with a sign test is a weak form of evidence, particularly when the number of tasks is small (n = 16) and the deltas may be heterogeneous across tasks. The manuscript states that per-task seed variability is small, but does not provide the actual standard deviations or the distribution of deltas. Furthermore, the sign test excludes ties, which reduces the effective sample size, and the manuscript does not report how many ties were excluded in each comparison.
- **Why it matters** The central claim of the paper rests on this statistical comparison. Without effect sizes and confidence intervals, the reader cannot assess whether the observed wins are practically meaningful or within noise. The sign test is also sensitive to the choice of tie threshold, which is not specified.
- **Resolution test** Provide per-task delta values with confidence intervals, report the distribution of deltas across tasks, and justify the tie threshold. Consider reporting a paired effect size (e.g., median delta with bootstrap CI) alongside the sign test.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental confound
- **Claim pointer** The claim that masked-position MLM+JEPA is the strongest recipe, with the headline comparison varying both target position set and loss function
- **Evidence pointer** Section 3.3, Section 5
- **Concern** The headline comparison between masked-position MLM+JEPA (cosine loss) and all-position MLM+JEPA (MSE loss) varies two factors simultaneously: the set of positions where the latent loss is applied and the loss function. The authors acknowledge this confound in Section 5 but do not provide a clean ablation. The claim that "the masked-position restriction is what makes the within-family task counts consistent" is not directly supported, as the loss function difference could also contribute. The all-position variant was selected as the best in the sweep, but the sweep was conducted under the all-position regime only, so the interaction between position selection and loss function is unknown.
- **Why it matters** Without a clean ablation, the mechanism underlying the observed gains cannot be attributed to position selection versus loss function. This weakens the theoretical interpretation and the practical guidance for practitioners.
- **Resolution test** Add a 2x2 ablation varying position set (masked vs. all) and loss function (cosine vs. MSE) on at least one backbone, and report the full interaction.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility and data availability
- **Claim pointer** The claim that the evaluation suite is composed of 16 tasks from public benchmarks, and that all results are reported in tables
- **Evidence pointer** Section 3.5, Appendix A.7, Table 17
- **Concern** The manuscript references tables and figures extensively, but the actual data are not visible in the provided text. The anonymized repository is mentioned but not accessible. The task list in Section 3.5 is described, but the exact dataset identifiers, preprocessing steps, and evaluation protocols are only in Appendix A.7, which is referenced but not shown. The claim that "per-task seed variability is small" cannot be verified without the actual standard deviations.
- **Why it matters** Reproducibility is a core requirement for computational biology research. Without access to the actual data, tables, and code, the results cannot be independently verified. The manuscript's reliance on referenced but invisible appendices makes the evidence base incomplete.
- **Resolution test** Provide the full tables and figures in the manuscript or supplement, and ensure the repository is accessible for review. Include the per-task standard deviations and the exact dataset versions used.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of conclusions
- **Claim pointer** The conclusion that masked-position MLM+JEPA is competitive and can outperform pure MLM in pretraining and continued training
- **Evidence pointer** Section 4.1, Section 5
- **Concern** The from-scratch results are mixed, with random-init ESM2-35M showing 6/8/2 (p = 0.79) and ProteinBERT2-35M showing 11/4/1 (p = 0.059). The authors attribute this to architecture sensitivity, but the manuscript does not provide a mechanistic explanation for why ProteinBERT2 benefits while vanilla ESM2 does not. The claim that the recipe "can outperform" in pretraining is therefore only supported for one of two random-init backbones, and the p-value for ProteinBERT2 does not reach the conventional 0.05 threshold.
- **Why it matters** The practical recommendation for from-scratch pretraining is unclear. If the benefit is architecture-dependent, practitioners need guidance on when to expect gains. The manuscript's conclusion is more cautious than the abstract suggests.
- **Resolution test** Provide a more detailed analysis of the architecture differences that might explain the divergent results, or temper the conclusion to reflect the architecture sensitivity more explicitly.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** Section 3.2, Equation 1
- **Evidence pointer** Section 3.2
- **Issue** The notation in Equation 1 is not fully defined in the text. The symbols for the loss components and the weighting parameter lambda are described, but the exact form of the cosine loss and the SIGReg regularizer are not specified in the main text.
- **Required correction** Provide explicit definitions of all terms in Equation 1, including the cosine loss formula and the SIGReg expression, either in the main text or in a clearly referenced appendix.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Section 4.1, Table 1
- **Evidence pointer** Section 4.1
- **Issue** The manuscript reports p-values from sign tests but does not report the number of ties excluded or the effective sample size for each comparison. The statement "effective n ranges from 12 to 16" is vague.
- **Required correction** Report the exact number of wins, losses, and ties for each comparison, and the effective sample size used in each sign test.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of ablation
- **Affected element** Section 3.3, Section 5
- **Evidence pointer** Section 3.3
- **Issue** The all-position variant uses MSE while the masked-position variant uses cosine, as noted in the confound. The authors mention this in Section 5 but do not provide any preliminary data on whether the loss function alone matters.
- **Required correction** At minimum, report the all-position cosine variant result if available, or explicitly state that this condition was not run and why.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity of evaluation protocol
- **Affected element** Section 3.5
- **Evidence pointer** Section 3.5
- **Issue** The description of the linear probe evaluation is brief. It is unclear whether the probes are trained on the same data splits as the pretraining, whether there is any hyperparameter tuning for the probes, and how the three probe seeds are combined.
- **Required correction** Provide a more detailed description of the probe training protocol, including data splits, hyperparameter selection, and how seed variability is aggregated.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Presentation of results
- **Affected element** Section 4.1, Figure 1
- **Evidence pointer** Section 4.1
- **Issue** The text refers to "Figure 1 shows absolute scores on seven benchmarks with the largest within-cell gains," but the figure is not visible. It is unclear which seven benchmarks are shown and how the selection was made.
- **Required correction** List the seven benchmarks explicitly in the text and justify the selection criterion.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Section 5
- **Evidence pointer** Section 5
- **Issue** The discussion of the confound between position set and loss function is brief and does not propose a concrete plan for resolving it.
- **Required correction** Expand the discussion to include a specific proposal for the 2x2 ablation and acknowledge the implications for the interpretation of the headline result.

## Risk / unsupported claims
- The claim that masked-position MLM+JEPA "wins more tasks than it loses" is supported only by sign tests without effect sizes or confidence intervals, making the practical significance unclear
- The claim that the masked-position restriction is the key factor driving gains is not directly supported due to the confound with loss function
- The claim that from-scratch pretraining can benefit from the recipe is only supported for one of two backbones, and the p-value for that backbone does not reach conventional significance
- The claim that "gains are seen for multiple models on 11 of 16 tasks" is not verifiable without the actual per-task data
- The claim that the recipe "establishes a strong, self-supervised pretraining objective" is overstated given the mixed from-scratch results and the unresolved confound
- The reproducibility of the results cannot be assessed without access to the referenced tables, figures, and repository