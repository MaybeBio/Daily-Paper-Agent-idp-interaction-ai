## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and figure legends.
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided manuscript. No external data or unpublished materials were consulted.
- **Shared manuscript claim summary** The authors propose that the paralogous SPOC domain-containing proteins DIDO3 and PHF3 form a complex that bridges RNA Polymerase II (Pol II) elongation machinery with chromatin and RNA processing factors, tethering Pol II in phase-separated condensates. They further claim that these proteins co-regulate gene expression, with both cooperative and antagonistic effects on neuronal genes, and that DIDO3 is upregulated upon PHF3 loss as a compensatory mechanism. Both proteins are reported as essential for neuronal differentiation.
- **Visible evidence base** The manuscript includes RNA-seq, PRO-seq, 3' end sequencing, co-immunoprecipitation followed by mass spectrometry, western blotting, in vitro condensate formation assays, immunofluorescence, and high-resolution Airyscan imaging. Multiple CRISPR/Cas9-generated cell lines are described.
- **Missing materials affecting confidence** The manuscript does not provide full lists of differentially expressed genes, complete mass spectrometry datasets, or detailed statistical outputs for all comparisons. The methods for some imaging quantifications are not fully detailed. The manuscript also lacks a clear description of how the "neuronal clumps" were defined and counted beyond a brief mention. The absence of these details limits the ability to fully assess the robustness of the claims.

## Reviewer
- **Overall assessment** This manuscript presents a comprehensive and largely convincing body of work that significantly advances our understanding of the paralogous proteins DIDO3 and PHF3. The combination of biochemical, cell biological, and transcriptomic approaches is well-suited to the questions posed. The identification of a physical complex between DIDO3 and PHF3, their role in Pol II clustering, and the nuanced cooperative and antagonistic transcriptional regulation are important findings. The proposed compensatory upregulation of DIDO3 upon PHF3 loss is a particularly interesting and novel concept. However, several technical and interpretational issues need to be addressed to fully solidify the conclusions, particularly regarding the directness of the phase separation mechanism in cells and the specificity of the proposed compensation.
- **Who would be interested in the results, and why** This work will be of high interest to researchers in the fields of transcriptional regulation, chromatin biology, RNA processing, and neurodevelopment. The study provides new insights into the function of SPOC domain proteins, which are implicated in these processes. The concept of paralog compensation through isoform switching is broadly relevant to gene regulation and genetic robustness. The link to neuronal differentiation will appeal to those studying stem cell biology and neurodevelopmental disorders.
- **Major strengths**
    1.  The study is well-designed, combining unbiased interactomics with targeted functional assays and transcriptomics.
    2.  The use of multiple CRISPR-generated cell lines, including domain-specific deletions, allows for a detailed dissection of protein function.
    3.  The identification of a physical and functional complex between DIDO3 and PHF3 is a significant advance.
    4.  The finding that PHF3 loss leads to a compensatory upregulation of the SPOC-containing DIDO3 isoform is novel and mechanistically interesting.
    5.  The data strongly support a role for both proteins in neuronal differentiation, with clear phenotypic consequences in a relevant model system.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness / Interpretation
    - **Claim pointer** The authors claim that DIDO3 and PHF3 "tether Pol II in a phase-separated microenvironment" and that their IDRs are critical for this process.
    - **Evidence pointer** Figure 3, Figure 4, and associated text.
    - **Concern** The evidence for phase separation in cells is indirect. The in vitro condensate formation assays are convincing, but the cellular data relies on colocalization with Pol II clusters and changes in cluster size upon IDR deletion. This does not directly demonstrate that DIDO3 and PHF3 are driving phase separation in cells, as opposed to being clients of pre-existing condensates. The altered H3K9me3 clustering in PHF3 ΔIDR cells is interesting but is a downstream consequence and does not directly prove a role in phase separation.
    - **Why it matters** The central claim of the paper rests on the idea that these proteins create a specific microenvironment through phase separation. If the evidence is only correlative, the mechanistic model is weakened. The distinction between a driver and a client of phase-separated condensates is crucial for the proposed model.
    - **Resolution test** The authors should provide more direct evidence for phase separation in cells, such as fluorescence recovery after photobleaching (FRAP) experiments to measure the dynamics of DIDO3 and PHF3 within the clusters, or use of a live-cell imaging approach to show fusion and fission events characteristic of liquid-liquid phase separation. Alternatively, they could temper the claim to state that the proteins "associate with" or "promote the formation of" Pol II clusters, rather than directly tethering Pol II in a phase-separated compartment.
    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical soundness / Data interpretation
    - **Claim pointer** The authors propose that DIDO3 upregulation in PHF3 KO cells is a "compensatory mechanism."
    - **Evidence pointer** Figure 1, Figure 7, and associated text.
    - **Concern** The evidence for compensation is based on the observation that DIDO3 is upregulated and that double knockouts have a more severe phenotype. While this is consistent with compensation, it is not direct proof. The increased severity in the double knockout could also be explained by additive or synergistic effects of losing two independent regulators, rather than the loss of a specific compensatory response. The claim of compensation implies a specific regulatory feedback loop that is not demonstrated.
    - **Why it matters** The concept of paralog compensation is a major conceptual advance of the paper. If the evidence is not definitive, the novelty of this specific claim is diminished. It is important to distinguish between a passive consequence of losing a repressor and an active, evolved compensatory mechanism.
    - **Resolution test** To strengthen this claim, the authors could test whether the upregulation of DIDO3 is functionally relevant. For example, they could knock down DIDO3 specifically in the PHF3 KO background and show that this exacerbates the phenotype more than expected from the single knockouts alone. Alternatively, they could investigate the mechanism of DIDO3 upregulation, such as identifying a transcription factor that is derepressed in PHF3 KO cells and directly activates DIDO3 expression.
    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical soundness / Reproducibility
    - **Claim pointer** The manuscript describes a large number of cell lines and complex phenotypic analyses, including "neuronal clump" formation.
    - **Evidence pointer** Figure 8 and associated text.
    - **Concern** The quantification of neuronal differentiation relies on manual counting of "neuronal clumps," which is a subjective and potentially variable measure. The definition of a "clump" is not clearly defined, and the method is prone to observer bias. This is a critical functional assay, and its robustness is questionable.
    - **Why it matters** The conclusion that DIDO3 and PHF3 are essential for neuronal differentiation is a key finding. If the primary assay for this is not rigorously quantified, the conclusion is weakened.
    - **Resolution test** The authors should provide a more objective and robust quantification method, such as automated image analysis or flow cytometry-based quantification of neuronal markers. They should also provide clear criteria for what constitutes a "neuronal clump" and ideally have the counting performed by an observer blinded to the genotype.
- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity / Reproducibility
    - **Affected element** Methods section
    - **Evidence pointer** Methods, "Proliferation assay" section.
    - **Issue** The proliferation assay description is brief. It is unclear if the "growth rate" is calculated as a fold-change from day 1 or as a doubling time. The statistical test used is not specified for this figure.
    - **Required correction** Please clarify the calculation of growth rate and specify the statistical test used in the figure legend or methods.
    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Clarity / Data presentation
    - **Affected element** Figure 5
    - **Evidence pointer** Figure 5 and associated text.
    - **Issue** The MA plots in Figure 5 are useful, but the number of differentially expressed genes is only shown in a bar chart. It would be helpful to include a Venn diagram or upset plot to show the overlap of differentially expressed genes between the different mutant cell lines, which would more clearly illustrate the shared and unique targets.
    - **Required correction** Consider adding a Venn diagram or similar visualization to show the overlap of differentially expressed genes between the different genotypes.
    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Clarity / Data interpretation
    - **Affected element** Discussion
    - **Evidence pointer** Discussion section.
    - **Issue** The discussion of the antagonistic regulation of neuronal genes is somewhat brief. A more detailed discussion of the potential mechanisms for this antagonism (e.g., competition for binding sites, differential recruitment of co-factors) would be valuable.
    - **Required correction** Expand the discussion on the potential molecular mechanisms underlying the antagonistic regulation of gene expression by DIDO3 and PHF3.

## Risk / unsupported claims
- The claim that DIDO3 and PHF3 "tether Pol II in a phase-separated microenvironment" is not fully supported by the provided evidence, which is largely correlative and based on in vitro assays.
- The claim that DIDO3 upregulation is a "compensatory mechanism" is an interpretation that is consistent with, but not directly proven by, the data.
- The functional significance of the IDRs in mediating the transcriptional changes is inferred from the deletion phenotypes but the direct link to condensate formation in cells is not established.
- The manuscript states that DIDO3 interacts with "chromatin-associated proteins" but the functional significance of many of these specific interactions is not explored.
- The claim that the double SPOC deletion has a "dominant negative effect" is an interpretation that is not fully explored mechanistically.