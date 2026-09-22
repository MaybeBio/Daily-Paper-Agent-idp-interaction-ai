## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and figure legends as provided.
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided text. No external data or supplementary files were accessed.
- **Shared manuscript claim summary** The authors propose an "acidic exposure model" for human activation domains (ADs), in which acidic residues and intrinsic disorder keep hydrophobic motifs (aromatic and leucine residues) solvent-exposed and available for coactivator binding. Using high-throughput mutational scanning of seven ADs, they report that strong AD activity requires a balance between acidic residues and aromatic/leucine residues, and they develop a sequence-composition-based predictor that identifies known and novel ADs in the human proteome.
- **Visible evidence base** Main text figures (Figures 1–6), supplementary figure references (Figures S1–S12), tables (Tables S1–S2), and methods descriptions as embedded in the text. Raw data, full datasets (Data S1–S9), and code are referenced but not provided.
- **Missing materials affecting confidence** Raw activity measurements, complete variant lists, detailed statistical outputs, simulation parameters, and the full predictor algorithm code are not available in the provided material. Supplementary figures and tables are referenced but not included. This limits independent verification of several quantitative claims.

## Reviewer
- **Overall assessment** This manuscript addresses a long-standing problem in transcription factor biology: the sequence determinants of acidic activation domain function. The authors present a large-scale, quantitative dataset generated in human cells, which is a valuable resource. The central claim, that a balance between acidic and hydrophobic residues governs strong AD activity, is plausible and consistent with prior work in yeast. However, the evidence as presented has several gaps. The high-throughput assay's dynamic range and sensitivity are not fully characterized, particularly for weakly active ADs. The predictor's performance is assessed against a small set of annotated ADs, and the permutation test, while suggestive, does not fully establish generalizability. The mechanistic interpretation, while appealing, is supported primarily by indirect correlational data and limited simulations. The manuscript is well-written and the conceptual framework is timely, but the strength of the conclusions currently exceeds the strength of the visible evidence.
- **Who would be interested in the results, and why** Researchers studying transcriptional regulation, intrinsically disordered proteins, and sequence-function relationships. The dataset and predictor will be of practical use to those seeking to identify or engineer ADs. The conceptual model will interest biophysicists and computational biologists working on disordered protein function. The high-throughput assay platform may also appeal to synthetic biologists.
- **Major strengths** 1) Large-scale, systematic mutagenesis dataset in human cells, addressing a gap in the field. 2) Clear and testable conceptual model (acidic exposure) that unifies observations across multiple ADs. 3) Development of a simple, composition-based predictor with experimental validation. 4) Integration of biophysical simulations to support mechanistic claims. 5) Transparent reporting of methods and data availability.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (assay sensitivity and dynamic range), R1-M2 (predictor validation and generalizability), R1-M3 (mechanistic support from simulations), R1-M4 (statistical treatment of multi-variant data).
- **Assessment against Nature-style criteria**  
  *Originality*: High. The systematic, quantitative approach to AD function in human cells is novel, and the acidic exposure model, while building on prior work, is applied here in a new and comprehensive manner.  
  *Scientific importance*: High. Understanding AD sequence determinants is fundamental to transcriptional regulation and has practical implications for gene therapy and synthetic biology.  
  *Interdisciplinary readership*: Moderate to high. The work bridges molecular biology, biophysics, and computational biology. The conceptual model is accessible, but the detailed methods may limit broad appeal.  
  *Technical soundness*: Moderate. The experimental design is generally sound, but several technical aspects (assay sensitivity, statistical power, simulation validation) are not fully addressed in the provided text.  
  *Readability for nonspecialists*: Good. The abstract and introduction are clear, and the main findings are presented in an accessible manner. The discussion effectively contextualizes the results.
- **Recommendation posture** Supportive if technical concerns are resolved. The core findings are likely correct and important, but the current manuscript does not fully establish the claims from the provided evidence. Specific revisions addressing assay characterization, predictor validation, and mechanistic support are required.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental rigor
- **Claim pointer** The authors state that the assay "recapitulates the activity of known mutations in human ADs" and that they can resolve "small changes in activity" with the 28-barcode design.
- **Evidence pointer** Results section, Figure S1, Data S1
- **Concern** The assay's sensitivity and dynamic range are not fully characterized. The average Pearson correlation between replicates is 0.69, which is moderate. The text states that five barcodes were insufficient to resolve small effects in the p53 library, but the threshold for "small" is not defined. For the 28-barcode design, the resolution limit is not quantified. The dynamic range of the assay, as determined by the fluorescence values of the dimmest and brightest bins, is mentioned but not provided in the main text.
- **Why it matters** The central conclusions depend on the ability to distinguish meaningful differences in AD activity. If the assay cannot reliably resolve small effects, then claims about the relative contributions of specific residues or the balance between acidic and hydrophobic residues may be overstated. The moderate correlation between replicates raises concerns about noise.
- **Resolution test** Provide a detailed characterization of the assay's noise floor and dynamic range. Include a plot of measured activity versus known input activity for a set of control variants. Quantify the effect size that can be reliably detected with the 28-barcode design. Report the actual fluorescence values for the bins and the distribution of activities across all variants.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical and computational validation
- **Claim pointer** The authors claim that their predictor "accurately predicts previously unidentified ADs" and that the overlap with known ADs is "far more than expected by chance (p < 1e-5 in permutation tests)."
- **Evidence pointer** Results section, Figure 6, Data S3, Data S4
- **Concern** The predictor's validation is limited. The permutation test compares overlap with a small set of 110 annotated ADs, which may not represent the full diversity of ADs. The 17 predicted ADs that overlap known ADs represent a small fraction of the 144 predictions. The experimental validation tested 150 predicted regions, but the text does not report how many of the 58 "strong" predicted ADs were novel versus known. The choice of thresholds (charge < -9, WFYL > 7) appears arbitrary and may not generalize.
- **Why it matters** The predictor is a key deliverable of the paper. If its performance is not robustly validated, the claim that it can identify new ADs is not established. The small overlap with known ADs could indicate either a high false-positive rate or that the known AD set is incomplete. The arbitrary thresholds raise concerns about overfitting.
- **Resolution test** Provide a more comprehensive validation. Test the predictor on a held-out set of ADs from diverse species. Report the precision and recall of the predictor at various thresholds. Compare the predictor's performance to simpler baselines (e.g., net charge alone, hydrophobicity alone). Provide a sensitivity analysis for the threshold choices. Report the number of novel predictions that were experimentally confirmed as strong ADs.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Mechanistic interpretation
- **Claim pointer** The authors state that "acidic residues and intrinsic disorder keep hydrophobic motifs exposed to solvent" and that this "acidic exposure model" explains the balance requirement.
- **Evidence pointer** Discussion, Figure 7, Figure S7
- **Concern** The mechanistic claim is supported primarily by correlational data (activity vs. composition) and limited all-atom simulations. The simulations show that adding acidic residues increases radius of gyration and adding aromatic residues decreases it, but these are ensemble averages with large dispersion. The link between radius of gyration and coactivator binding is not directly demonstrated. The model is presented as a general explanation, but only seven ADs were studied.
- **Why it matters** The acidic exposure model is a conceptual contribution that goes beyond the data. If the mechanistic interpretation is not well-supported, the paper's impact is reduced. The model may be an oversimplification, as other factors (e.g., specific coactivator interactions, post-translational modifications) are known to influence AD function.
- **Resolution test** Provide direct experimental evidence linking conformational ensemble to activity. For example, measure binding affinity of selected variants to coactivator domains and correlate with predicted solvent exposure. Alternatively, use FRET or other biophysical methods to measure compaction in cells. Acknowledge the limitations of the model and discuss alternative explanations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Statistical treatment of data
- **Claim pointer** The authors report that "most point substitutions had small effects on activity" in the p53 DMS, and they use this to justify focusing on rational mutants.
- **Evidence pointer** Results section, Data S2
- **Concern** The DMS data for p53 are described as too noisy to resolve small effects, but the data are still used to "corroborate trends." The criteria for "corroboration" are not defined. The rational mutant data are presented as "high-quality," but the statistical framework for comparing variants across different ADs is not fully described. The normalization procedure (setting No AD control to 2000) is reasonable, but the variance across replicates is not systematically reported.
- **Why it matters** The conclusions about which residues are important and how they balance each other depend on the statistical treatment. If the DMS data are too noisy to be informative, they should not be used to support any claim. The lack of a clear statistical framework makes it difficult to assess the robustness of the findings.
- **Resolution test** Provide a clear statistical analysis plan. Report the variance across replicates for all variants. For the DMS data, either provide a rigorous analysis that accounts for noise or explicitly state that these data are not used for quantitative claims. For the rational mutant data, report confidence intervals for all activity measurements and specify the statistical test used to identify significant differences.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 1
- **Evidence pointer** Figure 1
- **Issue** The schematic in Figure 1A is helpful, but the relationship between the "acidic exposure model" and the experimental design in Figure 1B is not immediately clear. The figure legend could be more explicit about how the model motivates the specific mutations tested.
- **Required correction** Expand the figure legend to explicitly state how the model predictions (e.g., acidic residues promote exposure, aromatic residues promote collapse) map to the experimental perturbations.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data and code availability section
- **Evidence pointer** Methods, Data and code availability
- **Issue** The text states that data and code are available, but the specific repository links and accession numbers are not provided in the manuscript text.
- **Required correction** Provide the full URLs or accession numbers for all datasets and code repositories in the Data and code availability section.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of negative results
- **Affected element** Results, p65 and Stat3
- **Evidence pointer** Results section, Figure 2
- **Issue** The authors note that p65 and Stat3 were weakly active in the assay, and no variants significantly changed activity. This is presented as a limitation, but it could also be interpreted as evidence that these ADs are not well-suited to the assay conditions. The authors do not discuss whether this reflects a true biological difference or an assay artifact.
- **Required correction** Add a brief discussion of why p65 and Stat3 might be weakly active and whether this limits the conclusions that can be drawn about these ADs.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract, Introduction
- **Issue** The term "acidic activation domains" is used throughout, but the authors do not define a quantitative threshold for "acidic." This could be confusing for readers.
- **Required correction** Define the criteria used to classify an AD as "acidic" (e.g., net charge per residue) in the Introduction or Methods.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Comparison to prior work
- **Affected element** Discussion
- **Evidence pointer** Discussion
- **Issue** The discussion mentions prior work in yeast but does not systematically compare the current findings to those studies. A more detailed comparison would help readers understand what is new and what is confirmatory.
- **Required correction** Add a paragraph in the Discussion that explicitly compares the current results to the yeast studies, highlighting similarities and differences.

## Risk / unsupported claims
- The claim that the "acidic exposure model" is a "general explanation for the function of eukaryotic ADs" is not supported by the data, which only cover seven human ADs.
- The claim that the predictor "accurately predicts previously unidentified ADs" is not fully established, as the experimental validation is limited and the false-positive rate is not reported.
- The claim that "leucine residues make the largest contributions to activity" in human ADs is based on a limited set of ADs and may not generalize.
- The mechanistic interpretation that acidic residues "solubilize" hydrophobic motifs is inferred from simulations and not directly tested experimentally.
- The statement that "the landing pad equalizes the effects of genomic position on expression" is presented as a fact, but the evidence for this is not shown in the provided text.