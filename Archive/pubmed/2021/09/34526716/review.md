## Review setup
- **Input scope** Full manuscript text including abstract, main text, methods, and supplementary figure legends
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and technical rigor as presented in the provided manuscript
- **Shared manuscript claim summary** The authors propose that phase separation of UTX, mediated by a core intrinsically disordered region (cIDR), underlies its tumour-suppressive activity. They argue that cIDR-dependent condensation recruits MLL4 into co-condensates, enriches H3K4 methylation, and regulates chromatin modifications and interactions in a condensation-dependent manner. They further suggest that UTY, the Y-linked homolog, forms condensates with reduced dynamics, explaining its weaker tumour-suppressive activity.
- **Visible evidence base** In vitro phase separation assays, cellular imaging (including OptoDroplet and LacO array systems), FRAP and RICS measurements, pulldown-based biochemical assays, RNA-seq, ChIP-seq, PRO-seq, HiChIP, and xenograft tumour assays
- **Missing materials affecting confidence** Raw sequencing data, complete figure panels (only legends visible), statistical source data, and details of replicate numbers for several key experiments

## Reviewer
- **Overall assessment** This manuscript presents a conceptually interesting and potentially important advance in understanding how UTX, a chromatin regulator with tumour-suppressive functions, operates through liquid-liquid phase separation. The central claim that condensation, rather than demethylase activity, underpins UTX function is well-motivated by prior literature and supported by a substantial body of correlative evidence. However, several technical concerns and gaps in the evidence chain reduce confidence in the causal model proposed. The distinction between correlation and causation, particularly regarding the role of condensation in recruiting MLL4 and driving chromatin changes, requires additional experimental support. The manuscript would benefit from clearer quantification, additional controls, and a more rigorous demonstration that the observed phenotypes are specifically due to altered phase separation properties rather than other consequences of the mutations used.
- **Who would be interested in the results, and why** Researchers studying transcriptional regulation, chromatin biology, and the emerging role of biomolecular condensates in gene control. The work also has relevance for cancer biologists interested in tumour suppressor mechanisms and for those studying the functional differences between UTX and UTY. The conceptual framework linking phase separation to tumour suppression may stimulate further work in both basic and translational settings.
- **Major strengths** The study addresses a long-standing puzzle regarding UTX function by proposing a novel mechanism. The use of multiple complementary approaches, including in vitro reconstitution, cell-based imaging, and genomic assays, is commendable. The inclusion of patient-derived mutations and the comparison between UTX and UTY add translational and evolutionary dimensions. The data on condensation-dependent chromatin interactions and transcriptional outcomes are potentially impactful.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5
- **Assessment against Nature-style criteria**  
  *Originality*: High. The concept that phase separation of a tumour suppressor underlies its function is novel and timely.  
  *Scientific importance*: Potentially high, as it may redefine how UTX-mediated tumour suppression is understood and could have broader implications for other chromatin regulators.  
  *Interdisciplinary readership*: Broad appeal across chromatin biology, biophysics of phase separation, and cancer research.  
  *Technical soundness*: Mixed. While many experiments are well-executed, several key claims lack sufficient quantitative support or appropriate controls.  
  *Readability for nonspecialists*: The main text is generally clear, though some sections assume familiarity with phase separation concepts and genomic assays. The abstract is accessible.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is compelling and likely to be of broad interest, but the current evidence does not fully establish the causal role of condensation in UTX-mediated tumour suppression.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Causal inference
- **Claim pointer** The authors claim that "UTX recruits MLL4/KMT2D into the same condensates and enriches the H3K4 methylation activity of MLL4" and that this is a key mechanism underlying UTX's tumour-suppressive function.
- **Evidence pointer** Figure 3, Extended Data Figures 5-7
- **Concern** The evidence that UTX condensation directly recruits MLL4 and enhances its enzymatic activity is largely correlative. The pulldown experiments show co-purification of MLL4 with UTX condensates, but this does not demonstrate that condensation is required for the functional interaction. The in vitro experiments with purified components are not shown for the full-length proteins, and the relevance of the truncated constructs used is unclear. The claim that condensation "enriches" H3K4 methylation activity is not directly tested with a controlled biochemical assay comparing condensate versus non-condensate states at equal enzyme concentrations.
- **Why it matters** The central mechanistic claim of the paper rests on this interaction. If condensation merely correlates with MLL4 association but is not causal for enhanced activity, the proposed model loses its foundation.
- **Resolution test** Provide a direct biochemical assay where MLL4 activity is measured in the presence of UTX condensates versus a non-condensing UTX mutant, with careful normalization for enzyme and substrate concentrations. Alternatively, use an optogenetic system to show that induced UTX condensation acutely enhances MLL4 activity at target loci.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Mutational specificity
- **Claim pointer** The authors use cIDR mutations (SY, SI, NY, HY) and deletions to argue that condensation is required for tumour suppression. They state that "cIDR loss is largely responsible for inactivation of UTX 555* in those patients."
- **Evidence pointer** Figure 1, Extended Data Figures 1-3
- **Concern** The mutations used to disrupt condensation may have effects beyond altering phase separation. For example, replacing all 47 serines with tyrosines or isoleucines could affect protein stability, folding, or interactions with other partners. The authors do not show that these mutants retain proper folding or that their only defect is in condensation. The 555* mutant lacks the cIDR but also other C-terminal regions, so attributing its loss of function solely to cIDR deletion is an overreach without additional rescue experiments.
- **Why it matters** The specificity of the mutations is critical for attributing the observed phenotypes to condensation. If the mutants have pleiotropic effects, the conclusions about phase separation being the key mechanism are weakened.
- **Resolution test** Perform structure-function analysis showing that the cIDR mutants retain overall protein folding and known protein-protein interactions (e.g., with MLL3/4 complexes). Use a complementation approach where condensation is restored in the 555* background by fusing an unrelated cIDR and show functional rescue.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative rigor
- **Claim pointer** The authors state that "UTY cIDR exhibited significantly slower diffusion than UTX cIDR at all times" and that this "may contribute to its weakened tumour suppressive activity."
- **Evidence pointer** Figure 5, Extended Data Figure 11
- **Concern** The FRAP and RICS data are presented without clear quantification of replicate numbers, statistical power, or appropriate controls for photobleaching and sample variability. The claim that reduced dynamics directly explains weaker tumour suppression is speculative, as no experiment directly links the measured diffusion differences to functional outcomes. The comparison between UTX and UTY is complicated by the fact that these proteins differ in multiple regions beyond the cIDR.
- **Why it matters** The quantitative differences in material properties are a key part of the model. Without rigorous statistics and a direct functional link, the claim that "proper material states" are required for tumour suppression is not established.
- **Resolution test** Provide full statistical analysis of FRAP/RICS data with appropriate numbers of independent experiments and cells. Use a chimeric approach where UTY cIDR is replaced with UTX cIDR and show that this rescues both dynamics and tumour-suppressive function.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Genomic data interpretation
- **Claim pointer** The authors claim that "UTX regulates genome-wide histone modifications and high-order chromatin interactions in a condensation-dependent manner."
- **Evidence point** Figure 4, Extended Data Figures 8-10
- **Concern** The genomic analyses (ChIP-seq, PRO-seq, HiChIP) are described in the text but the actual data presentation is limited. The authors do not show clear genome-wide summaries, such as aggregate plots or heatmaps, that would allow assessment of the magnitude and reproducibility of the observed changes. The comparison between WT and ΔcIDR is complicated by potential differences in UTX protein levels or chromatin binding, which are not fully addressed. The HiChIP data interpretation relies on a computational tool (BART3D) that may not be widely validated.
- **Why it matters** The claim that condensation controls genome-wide chromatin states is a major part of the paper. Without clear presentation of the genomic data and appropriate controls, this claim cannot be adequately evaluated.
- **Resolution test** Provide comprehensive genome-wide views of the ChIP-seq, PRO-seq, and HiChIP data, including browser tracks, aggregate plots, and statistical comparisons. Control for UTX expression levels and chromatin binding between WT and mutant conditions.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Physiological relevance
- **Claim pointer** The authors state that "UTX condensation suppresses cancer" and use xenograft assays to support this.
- **Evidence pointer** Figure 1, Extended Data Figures 2-3
- **Concern** The tumour suppression assays are performed in immunodeficient mice with cell lines, which may not fully recapitulate the physiological context of UTX mutations in human cancers. The authors do not show that the condensation-defective mutants have similar protein stability or expression levels as WT in the xenograft setting. The relevance of the THP-1 and MiaPaca2 models to the broader landscape of UTX-mutant cancers is unclear.
- **Why it matters** The physiological relevance of the findings is central to the paper's significance. If the effects are only seen in specific cell lines or under artificial conditions, the broader implications are limited.
- **Resolution test** Use additional UTX-mutant cancer models, including patient-derived xenografts or organoids, and show that restoring condensation rescues tumour suppression. Include analysis of UTX protein levels and stability in the xenograft tumours.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence point** Abstract
- **Issue** The abstract states that "phase separation of UTX underlies its chromatin regulatory activity in tumour suppression" but does not clearly distinguish between condensation being necessary versus sufficient for function.
- **Required correction** Clarify in the abstract whether condensation is proposed as a necessary or sufficient condition for UTX tumour-suppressive activity.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Experimental detail
- **Affected element** Methods, in vitro phase separation
- **Evidence point** Methods section
- **Issue** The methods for in vitro phase separation assays are described but the protein concentrations used and the buffer conditions for each experiment are not fully specified.
- **Required correction** Provide a table or detailed description of all conditions used for in vitro phase separation experiments, including protein concentrations, salt concentrations, and time points.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure legends
- **Evidence point** Figure legends
- **Issue** Several figure legends state "representative images" without specifying how many independent experiments were performed or how many cells/fields were analyzed.
- **Required correction** Add explicit information on replicate numbers and statistical tests used for each figure panel.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data availability statement
- **Evidence point** Data availability section
- **Issue** The data availability statement mentions deposition in GEO but does not provide a reviewer access token or link.
- **Required correction** Provide a reviewer link or token for accessing the deposited data.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence point** Discussion section
- **Issue** The discussion speculates about the role of condensate material properties in disease without fully acknowledging alternative explanations, such as changes in protein stability or interactions.
- **Required correction** Add a paragraph acknowledging alternative interpretations and limitations of the current study.

## Risk / unsupported claims
- The claim that "UTX condensation is required for tumour suppression" is not fully supported because the mutations used may have effects beyond disrupting phase separation.
- The claim that "UTX recruits MLL4 into condensates and enriches its activity" is correlative and lacks direct biochemical proof.
- The claim that "UTY forms condensates with reduced dynamics, explaining its weaker tumour suppression" is speculative and not directly tested.
- The claim that "condensation controls genome-wide chromatin interactions" is based on data not fully presented in the manuscript.
- The claim that "UTX condensation is important for ESC differentiation" is supported by limited data and would benefit from additional functional assays.