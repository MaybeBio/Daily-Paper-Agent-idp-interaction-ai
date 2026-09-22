## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusion) as provided; no figures, tables, or supplementary material were available for inspection.
- **Assessment boundary** Assessment is limited to the scientific content, methodological soundness, and internal consistency of the written manuscript. Claims referencing figures, tables, or supplementary items are evaluated based on textual descriptions only.
- **Shared manuscript claim summary** The authors report that a 15-residue intrinsically disordered mitochondrial localization peptide derived from the androgen receptor N-terminus, and 19 single-point variants at position 2, remain disordered across equilibrium molecular dynamics simulations. They report that global compactness metrics do not distinguish variants, while residue-level secondary structure propensities show subtle, sequence-dependent shifts. Principal component analysis of secondary structure propensities reveals clustering related to substitution chemistry. Well-tempered metadynamics simulations biased on α-helical content do not converge within multi-microsecond timescales, indicating a rugged free-energy landscape.
- **Visible evidence base** Textual descriptions of results; references to Table 1, Figures 1, 2, 4, 5, S1–S14. No actual data, figures, or tables were provided for inspection.
- **Missing materials affecting confidence** All figures, tables, and supplementary data; simulation parameter files; force field assignment details per system; convergence metrics for equilibrium simulations; error bar definitions; PCA loading details; metadynamics parameters (bias factor, deposition rate, width); free energy estimates; and any statistical tests or significance assessments.

## Reviewer
- **Overall assessment** The manuscript addresses a relevant and timely question in the field of intrinsically disordered proteins, specifically how single-residue substitutions modulate the conformational ensemble of a mitochondrial localization sequence. The study design is systematic and the analytical framework is sensible. However, the conclusions are largely qualitative and the evidence base, as described, is insufficient to firmly establish several key claims. The lack of quantitative comparisons, statistical rigor, and convergence assessment for equilibrium simulations weakens the central narrative. The enhanced sampling results are presented as diagnostic, which is honest, but this limits the depth of insight. The manuscript is clearly written and accessible, but the scientific impact is currently modest given the preliminary nature of the findings.
- **Who would be interested in the results, and why** Researchers studying mitochondrial protein import and localization signals, particularly those interested in the conformational properties of targeting peptides. Also, computational biophysicists and chemists working on intrinsically disordered proteins, enhanced sampling methodologies, and the development of force fields for disordered systems. The methodological discussion regarding sampling convergence for short disordered peptides will be of interest to practitioners in the field.
- **Major strengths** 1. Systematic and comprehensive variant library covering all 19 substitutions at a single position. 2. Use of multiple independent replicas to capture ensemble heterogeneity. 3. Combination of equilibrium and enhanced sampling simulations to probe both baseline behavior and sampling limitations. 4. Multivariate analysis (PCA) to integrate residue-level data into a comparative framework. 5. Honest reporting of convergence challenges in enhanced sampling.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The manuscript claims that "residue-level analysis reveals that the identity of the second residue subtly reshapes local structural preferences" and that "small or hydrophobic substitutions enhance transient α-helical sampling, whereas polar or charged substitutions favor increased disorder and β- or polyproline-like conformations."
  - **Evidence pointer** Results section, Figures 2 and 4; location not provided
  - **Concern** The claim of sequence-dependent secondary structure shifts is based on qualitative descriptions of Ramachandran distributions and deviation plots. No quantitative measures, such as per-residue helical propensity differences with associated uncertainties, are reported. The text states that "error bars across parallel simulations remain substantial," which undermines confidence in the reproducibility of the observed differences. Without statistical testing or effect size quantification, it is not possible to determine whether the reported shifts are significant or within noise.
  - **Why it matters** The central conclusion of the paper, that single-residue substitutions bias the conformational ensemble in a chemistry-dependent manner, rests entirely on these subtle differences. If these differences are not statistically robust, the main scientific message is not supported.
  - **Resolution test** Provide quantitative per-residue secondary structure propensity values for each variant with standard errors across replicas. Perform appropriate statistical tests (e.g., permutation tests or bootstrapping) comparing each variant to wild type. Report effect sizes and confidence intervals. If differences are not significant, revise the claims accordingly.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The manuscript claims that "global compactness metrics alone are insufficient to distinguish between MLP variants" based on data for only four variants (wild type, E2A, E2K, E2Q) reported in Table 1.
  - **Evidence pointer** Results section, Table 1; location not provided
  - **Concern** The conclusion that global metrics do not distinguish variants is based on a subset of four variants, not the full panel of 20. The text states "Representative global metrics for the wild-type peptide and three initial variants" but then generalizes to all variants. It is possible that other substitutions produce larger changes in compactness. The claim as stated is overgeneralized from the presented evidence.
  - **Why it matters** The logical flow of the paper depends on establishing that global metrics are uninformative before moving to residue-level analysis. If this is only demonstrated for a subset, the motivation for the subsequent analysis is weakened.
  - **Resolution test** Report global compactness metrics for all 20 variants. If the full dataset is not available, restrict the claim to the four examined variants and acknowledge the limitation.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The manuscript claims that PCA "enables systematic comparison of MLP variants at the ensemble level" and that "variants with similar physicochemical properties at the second position tend to occupy nearby regions of the reduced-dimensional space."
  - **Evidence pointer** Results section, Figure 5 and Figures S8–S10; location not provided
  - **Concern** The PCA results are described qualitatively. No information is provided on the variance explained by the principal components, the loading of individual features, or any quantitative measure of clustering (e.g., silhouette scores, distances between cluster centroids). The claim of chemistry-based clustering is not supported by any statistical or quantitative evidence. Additionally, the input features are derived from secondary structure propensities that themselves have not been shown to be statistically robust (see R1-M1).
  - **Why it matters** The PCA is presented as a key analytical outcome that organizes the variant behavior. Without quantitative support, the clustering claim is anecdotal and does not constitute a rigorous finding.
  - **Resolution test** Report the fraction of variance explained by the first two principal components. Provide loading vectors to show which residues contribute most. Perform a quantitative clustering analysis (e.g., k-means with silhouette scoring) and test whether clusters correspond to physicochemical properties using appropriate statistical tests.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness
  - **Claim pointer** The manuscript states that "the PMFs exhibit pronounced evolution as additional bias is deposited, with changes persisting into the final portions of the trajectories" and concludes that "convergence is not fully achieved even after several microseconds of enhanced sampling."
  - **Evidence pointer** Results section, Figures S11–S14; location not provided
  - **Concern** The enhanced sampling results are presented as demonstrating non-convergence, which is a valid and honest observation. However, the choice of α-helical content as the sole collective variable is acknowledged as insufficient. The manuscript does not discuss alternative collective variables or strategies that could improve convergence, nor does it provide quantitative measures of convergence (e.g., time-dependent free energy differences, histogram overlap). The diagnostic value of these simulations is limited without such analysis.
  - **Why it matters** The enhanced sampling section is intended to highlight methodological challenges. Without a more rigorous convergence analysis or discussion of alternative approaches, the section reads as a preliminary observation rather than a substantive contribution.
  - **Resolution test** Provide quantitative convergence metrics, such as the time evolution of free energy differences between key basins or the overlap of deposited bias histograms. Discuss alternative collective variables or enhanced sampling methods that could address the identified limitations.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methods, Molecular Dynamics Simulations
  - **Evidence pointer** Methods section; location not provided
  - **Issue** The manuscript states that simulations used "either the CHARMM36 or the updated CHARMM36m force field, depending on the specific system under study." This is ambiguous. It is unclear which force field was used for which system and why.
  - **Required correction** Specify the force field used for each variant or provide a rationale for the choice. If both were used, clarify whether results were consistent across force fields.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methods, Enhanced Sampling Simulations
  - **Evidence pointer** Methods section; location not provided
  - **Issue** The manuscript mentions that "two WTM simulation protocols were employed sequentially" but does not provide details on the parameters used (e.g., bias factor, Gaussian width, deposition stride) for either protocol.
  - **Required correction** Provide full parameters for both WTM protocols, including the collective variable definition, bias factor, deposition rate, and simulation length.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Results, Global Compactness
  - **Evidence pointer** Results section, Table 1; location not provided
  - **Issue** The text states that "representative global metrics" are shown in Table 1, but the table itself is not provided. It is unclear which metrics are included and how they are defined.
  - **Required correction** Ensure Table 1 is included in the final manuscript and clearly define all metrics (e.g., Rg, end-to-end distance, SASA) in the caption or text.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Results, PCA
  - **Evidence pointer** Results section, Figure 5; location not provided
  - **Issue** The text mentions "red markers indicated sequences validated by experimental data, and green markers denoted novel predictions." It is unclear which variants are validated by experimental data and what experimental data these refer to.
  - **Required correction** Clarify the source of experimental validation and specify which variants are marked red versus green.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Scientific importance
  - **Affected element** Discussion
  - **Evidence pointer** Discussion section; location not provided
  - **Issue** The discussion mentions a "potential mechanism by which targeting efficiency may be modulated" but does not elaborate on how the observed conformational shifts might translate to functional differences in mitochondrial import.
  - **Required correction** Expand the discussion to provide a more concrete mechanistic hypothesis linking conformational propensities to import efficiency, or explicitly state that such a link remains speculative.
- **Technical failings that need to be addressed before the case is established** R1-M1 (statistical robustness of secondary structure differences), R1-M2 (overgeneralization from subset of variants), R1-M3 (lack of quantitative support for PCA clustering). These are blocking because the core conclusions depend on them.
- **Assessment against Nature-style criteria**  
  *Originality*: Moderate. The application of systematic single-residue mutagenesis to a disordered localization peptide is not entirely novel, but the specific system and the combination of equilibrium and enhanced sampling approaches offer some originality.  
  *Scientific importance*: Moderate. The findings are incremental and largely confirm expectations that disordered peptides remain disordered and that subtle sequence changes have modest effects. The lack of functional validation limits the importance.  
  *Interdisciplinary readership*: Limited. The manuscript is primarily of interest to computational biophysicists and those studying mitochondrial targeting. The broader cell biology community may find the lack of functional data a barrier.  
  *Technical soundness*: Currently insufficient. The lack of quantitative analysis and statistical rigor in the key claims is a significant weakness.  
  *Readability for nonspecialists*: Good. The manuscript is clearly written and the logical flow is easy to follow, though some methodological details are sparse.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript has a sound conceptual framework and addresses a relevant question, but the key claims are not quantitatively supported. Major revisions are required to provide statistical rigor, full data reporting, and a more careful interpretation of the results. If these concerns are addressed, the manuscript could be suitable for a specialized journal, though its impact for a broad audience is likely limited.

## Risk / unsupported claims
- The claim that "small or hydrophobic substitutions enhance transient α-helical sampling, whereas polar or charged substitutions favor increased disorder" is not quantitatively supported and may be overstated given the acknowledged large error bars.
- The claim that PCA reveals chemistry-based clustering of variants is unsupported without quantitative clustering metrics.
- The claim that global metrics are insufficient to distinguish variants is overgeneralized from a subset of four variants.
- The statement that "these results show that even minimal sequence changes can bias the dynamic structural ensemble" is not firmly established given the lack of statistical significance testing.
- The suggestion of a "potential mechanism by which targeting efficiency may be modulated" is speculative and not directly supported by the data presented.