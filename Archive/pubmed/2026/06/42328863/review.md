## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, data availability, acknowledgments)
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided text. Figures, tables, and supplemental materials are referenced but not directly examined.
- **Shared manuscript claim summary** The authors propose that in *Corynebacterium glutamicum*, Wag31's N-terminal domain (NtD) mediates septal recruitment via protein-protein interactions, while the C-terminal domain (CtD) drives self-association and polar accumulation. They further propose that an actinobacteria-specific intrinsically disordered insert separates these functions and that proper NtD-mediated septal priming is essential for balanced Wag31 distribution and correct septum placement.
- **Visible evidence base** Text descriptions of: conditional depletion strain construction and phenotyping (Fig. 1); cell envelope analysis including PG incorporation, mycomembrane staining, SEM, and TLC (Fig. 2); phylogenetic and AlphaFold structural analyses (Figs. 3, 4); localization studies of truncation and mutant constructs (Figs. 5, 6); supplemental figures S1, S2, S4, S5; Table S1.
- **Missing materials affecting confidence** Actual figures and supplemental data not provided; quantitative imaging data (e.g., fluorescence intensity distributions, statistical outputs) not visible; full phylogenetic tree and alignment details not shown; AlphaFold confidence metrics not directly assessable; lipid binding assay raw data not shown; strain construction validation details (beyond sequencing summary) not fully described.

## Reviewer
- **Overall assessment** This manuscript addresses a significant gap in understanding Wag31/DivIVA function in actinobacteria, specifically in *C. glutamicum*. The evolutionary analysis revealing a structural cutoff between Firmicutes and Actinobacteria is compelling and provides a useful framework. The functional dissection of NtD versus CtD roles is well conceived, and the finding that NtD-mediated septal recruitment is protein-interaction-driven rather than membrane-binding-driven is an important contribution. However, several claims require stronger quantitative support, particularly regarding the "asymmetry" phenotype and the proposed priming model. The viability of the depletion strain over multiple generations also warrants more careful discussion given prior reports of essentiality.
- **Who would be interested in the results, and why** Researchers studying bacterial cell morphogenesis, particularly those focused on actinobacterial systems including mycobacteria (given the relevance to *M. tuberculosis* and *M. smegmatis*). The evolutionary analysis will interest comparative microbiologists. The domain-function mapping provides a foundation for mechanistic studies of Wag31 and may inform work on related coiled-coil scaffolding proteins in other organisms.
- **Major strengths** 1) The evolutionary/phylogenetic analysis combined with AlphaFold predictions provides a novel structural framework distinguishing actinobacterial Wag31 from Firmicutes DivIVA. 2) The use of a conditional depletion strain allows for controlled studies of an essential gene. 3) The functional separation of NtD (septal recruitment) and CtD (self-association) is clearly demonstrated through localization studies. 4) The finding that NtD septal recruitment is independent of membrane binding, contrary to the Firmicutes paradigm, is significant. 5) The observation that dysfunctional NtD leads to more severe phenotypes than complete depletion is intriguing and well documented.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Experimental support for central claim
  - **Claim pointer** "Interfering with the NtD systematically leads to asymmetric distribution of Wag31 to one pole, suggesting that correct priming at the septum prior to cytokinesis is essential for cellular repartitioning of the elongasome scaffold."
  - **Evidence pointer** Fig. 6, Fig. S4, Fig. S5; location not provided
  - **Concern** The claim of "systematic" asymmetric distribution is based on qualitative descriptions in the text. The manuscript states that Cohen's d values were used to describe effect sizes, but the actual quantitative distributions, number of cells analyzed per condition, and statistical comparisons are not presented in the text provided. The representative images described cannot establish "systematic" behavior without quantitative population-level analysis.
  - **Why it matters** The central model proposing that NtD-mediated septal priming is essential for balanced distribution rests on this asymmetry claim. If the asymmetry is not quantitatively robust and reproducible across biological replicates, the model is substantially weakened.
  - **Resolution test** Provide quantitative fluorescence intensity distributions (e.g., box plots or violin plots) for Wag31 localization across cell populations for each construct, with clear statistical comparisons (e.g., effect sizes with confidence intervals) between conditions. Specify the number of cells and biological replicates analyzed.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Viability claim vs. prior essentiality data
  - **Claim pointer** "Depleted cells were viable after 24 h of growth and kept growing in a second exponential phase in the presence of myo-inositol following an overnight depletion and re-dilution."
  - **Evidence pointer** Fig. 1c; location not provided
  - **Concern** The manuscript reports viability of Wag31-depleted cells over multiple generations, which contradicts prior reports of essentiality in *C. glutamicum* and related species. The growth curve shown in Fig. 1c is described but the actual data are not visible. The text does not address the discrepancy with earlier studies in sufficient depth, nor does it provide a mechanistic explanation for how cells remain viable without this supposedly essential protein.
  - **Why it matters** If Wag31 is truly essential, the depletion system may be "leaky" and residual protein may be present, which would confound all subsequent experiments. The authors need to demonstrate convincingly that depletion is complete and that viability is genuine, not an artifact of incomplete depletion.
  - **Resolution test** Show Western blot time course demonstrating complete depletion kinetics. Provide growth curves with statistical comparisons. Discuss potential reasons for discrepancy with prior essentiality claims (e.g., strain differences, growth conditions, genetic redundancy). Consider whether a second Wag31 paralog or functional homolog exists in *C. glutamicum*.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Mechanistic support for NtD-protein interaction model
  - **Claim pointer** "The N-ter is necessary for septal recruitment, independent of membrane binding capacities."
  - **Evidence pointer** Fig. 5, Fig. S2; location not provided
  - **Concern** The conclusion that NtD septal recruitment is mediated by protein-protein interactions rather than membrane binding rests on: (a) a liposome sedimentation assay showing no lipid binding, and (b) a triple mutant (Ile18-Asp, Lys20-Ser, Arg21-Ser) that retains septal localization. However, the text does not describe whether the triple mutant was tested for lipid binding. If the mutant also fails to bind lipids, the conclusion is strengthened; if it still binds lipids, the interpretation is ambiguous. Furthermore, the specific protein interaction partner (GlpR) is mentioned but the interaction data are referenced to prior work (ref 41), not shown here.
  - **Why it matters** The proposed model distinguishes actinobacterial Wag31 from Firmicutes DivIVA by suggesting protein-interaction-based recruitment rather than membrane curvature sensing. This is a key conceptual advance, but it requires direct evidence that the NtD does not bind membranes and that the mutant specifically disrupts protein interactions without affecting other NtD functions.
  - **Resolution test** Include lipid binding data for the triple mutant. Provide direct evidence (e.g., co-immunoprecipitation, pull-down, or two-hybrid) that the NtD interacts with GlpR in the context of the full-length protein. Show that the triple mutant disrupts this interaction.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Evolutionary claim robustness
  - **Claim pointer** "Using AlphaFold predictions and evolutionary analysis, we found a clear sequence and structure cutoff between Firmicutes and Actinobacteria, correlating with their different functions."
  - **Evidence pointer** Figs. 3, 4; location not provided
  - **Concern** The evolutionary analysis is described as showing a "clear cutoff," but the text does not provide details on the number of species analyzed, the statistical support for the phylogenetic tree, or the criteria used to define the "cutoff." The statement that one ancestral actinobacterial species "may represent a transition" is intriguing but not elaborated. The correlation between structural features and function is asserted but not systematically tested.
  - **Why it matters** The evolutionary framework is a major contribution of this work and underpins the functional interpretation. If the phylogenetic signal is weak or the structural classification is subjective, the conclusions are less robust.
  - **Resolution test** Provide the full phylogenetic tree with support values, specify the number of taxa and the methods used for tree inference, and define objective criteria for classifying the presence/absence of the disordered insert. Consider testing the correlation between insert presence and functional attributes (e.g., essentiality, polar growth) statistically.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity of strain nomenclature
  - **Affected element** Strain names and constructs
  - **Evidence pointer** Throughout; location not provided
  - **Issue** The manuscript uses several similar names (Cglu_Pino-wag31, Wag31NtD-mNeon, Wag31CtD-mNeon, Wag313mut-mNeon, mNeon-Wag31) that could be confusing. The distinction between the depletion strain and the various complementation constructs is not always clear in the text.
  - **Required correction** Consider a table summarizing all strains and constructs with their key features and purposes. Use consistent naming throughout.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Statistical reporting
  - **Affected element** Quantitative analyses
  - **Evidence pointer** Methods, Fig. 1e; location not provided
  - **Issue** The text mentions Cohen's d for effect sizes but does not report confidence intervals or exact p-values. The interpretation of "similar" or "different" without these metrics is difficult.
  - **Required correction** Report effect sizes with confidence intervals and specify the statistical tests used. For key comparisons, provide exact p-values or confidence intervals.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Discussion of limitations
  - **Affected element** Discussion section
  - **Evidence pointer** Discussion; location not provided
  - **Issue** The discussion does not address potential limitations of the study, such as the use of overexpression for complementation studies, potential artifacts from fluorescent protein tagging, or the possibility that the observed phenotypes are influenced by the expression system.
  - **Required correction** Add a paragraph acknowledging these limitations and discussing how they might affect interpretation.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Figure accessibility
  - **Affected element** All figures
  - **Evidence pointer** Not applicable
  - **Issue** The text references figures but the actual figures are not provided in the manuscript text. This is standard for a journal submission, but the descriptions in the text should be self-sufficient for understanding the key findings.
  - **Required correction** Ensure that all key quantitative results are also reported in the text or figure legends, not only in the figures themselves.
- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative support for asymmetry claim), R1-M2 (demonstration of complete depletion and resolution of essentiality discrepancy), R1-M3 (direct evidence for protein-interaction-based NtD recruitment).
- **Assessment against Nature-style criteria**  
  *Originality*: The work is original in its evolutionary-structural framing of Wag31/DivIVA diversity and in the functional dissection of N-terminal versus C-terminal domains in an actinobacterial context. The proposal that septal priming determines polar distribution is a novel conceptual contribution.  
  *Scientific importance*: The findings are important for understanding actinobacterial cell morphogenesis, with potential implications for mycobacterial pathogenesis given the essentiality of Wag31 in that context. The evolutionary analysis provides a framework for interpreting divergent DivIVA functions across bacterial phyla.  
  *Interdisciplinary readership*: The work bridges evolutionary biology, structural biology, and cell biology. The phylogenetic analysis and AlphaFold predictions will interest structural and evolutionary biologists, while the functional studies will appeal to microbiologists and cell biologists. The broader significance to bacterial cell biology is clear.  
  *Technical soundness*: The experimental approaches are generally appropriate, but the lack of quantitative rigor in the localization analyses and the unresolved essentiality question are concerns. The AlphaFold predictions are used appropriately as hypothesis-generating tools, but the functional validation is incomplete.  
  *Readability for nonspecialists*: The manuscript is generally well-written and accessible. The introduction provides sufficient background, and the figures are described clearly. However, the distinction between the various constructs and strains could be made clearer for nonspecialists.
- **Recommendation posture** Supportive if technical concerns are resolved. The conceptual framework and evolutionary analysis are valuable, and the functional dissection is well conceived. However, the central claims regarding asymmetry and the priming model require stronger quantitative support, and the viability question must be resolved to ensure that all experiments were performed under conditions of genuine Wag31 depletion.

## Risk / unsupported claims
- The claim that Wag31 depletion leads to "fully formed cell envelope" is based on TLC and staining data not visible in the provided text; the resolution of this analysis is unclear.
- The statement that the NtD septal recruitment is "likely mediated by protein-protein interactions" is presented as a conclusion but the supporting data (liposome assay, mutant localization) are only described qualitatively.
- The proposed model in Fig. 7 (priming at septum determines polar distribution) is a reasonable hypothesis but is not directly tested; it is inferred from the localization phenotypes.
- The evolutionary claim of a "clear cutoff" between Firmicutes and Actinobacteria is based on analyses not fully described; the number of species and statistical support are not provided.
- The statement that "the NtD is necessary and sufficient for septum localization" is strong; sufficiency is claimed but the text only describes NtD localization, not whether NtD alone can recruit other components or rescue any function.
- The discrepancy between the observed viability of the depletion strain and prior reports of essentiality is not resolved or adequately discussed.