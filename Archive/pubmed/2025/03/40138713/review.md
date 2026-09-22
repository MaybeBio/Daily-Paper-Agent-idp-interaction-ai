## Review setup
- **Input scope** Full manuscript text including abstract, introduction, materials and methods, results, discussion, and figure legends as provided.
- **Assessment boundary** Scientific content, methodological rigor, internal consistency, and support of claims by presented evidence. Editorial or stylistic issues are noted only where they affect comprehension.
- **Shared manuscript claim summary** The authors propose that a dynamic structural unit formed by interactions between the phosphorylated N-terminal tail and basic segments, particularly b4 at the end of the chromodomain, underlies liquid-liquid phase separation of HP1α, and that this interaction is functionally relevant for heterochromatin formation in vivo.
- **Visible evidence base** NMR chemical shift analyses, SEC-MALS, SEC-SAXS, EOM analysis, CGMD simulations with BME reweighting, in vitro LLPS assays, cell-based fluorescence microscopy, and yeast silencing assays.
- **Missing materials affecting confidence** Supplementary figures and tables referenced throughout (Supplementary Figs S1–S18, Tables S1–S2) were not provided. Details of the CGMD force field modification, BME reweighting parameters, and validation metrics for the structural ensembles are only partially described. Raw data and statistical outputs for microscopy quantifications are not fully available.

## Reviewer
- **Overall assessment** This manuscript presents an integrative structural biology approach to dissect the molecular determinants of HP1α phase separation. The combination of solution-state NMR, SAXS, and CGMD simulations is appropriate and potentially powerful for characterizing dynamic, disordered protein systems. The identification of the b4 segment as a key interaction partner for the phosphorylated N-tail is a plausible and interesting finding. However, the manuscript has several significant weaknesses. The distinction between intra- and intermolecular interactions is not always clearly established, particularly for the full-length dimer. The claim that the pΔCSD dimer is "the core structural unit" of LLPS is not fully supported by the data, as the evidence for a specific dimeric intermediate is indirect. The in vivo relevance is suggestive but limited by the use of overexpression and the lack of direct evidence that the b4 interaction is the mechanistic driver of the observed phenotypes. The presentation is dense and sometimes difficult to follow, with key methodological details relegated to supplementary material that was not available for review. Overall, the work is of interest to the chromatin and phase separation communities, but the central claims require stronger experimental support and clearer presentation.

- **Who would be interested in the results, and why** Researchers studying heterochromatin formation, HP1 proteins, liquid-liquid phase separation in chromatin biology, and the role of post-translational modifications in regulating disordered protein interactions. The integrative approach combining NMR, SAXS, and CGMD will also be of interest to structural biologists working on dynamic protein systems.

- **Major strengths**
  1. The use of multiple complementary biophysical techniques (NMR, SEC-MALS, SEC-SAXS, CGMD) to characterize a challenging, dynamic protein system is commendable and appropriate.
  2. The study addresses an important and timely question regarding the molecular basis of HP1α phase separation, which is relevant to heterochromatin function.
  3. The identification of the b4 segment as a specific interaction partner for the phosphorylated N-tail provides a concrete, testable model for how phosphorylation drives LLPS.
  4. The combination of in vitro biophysics with in vivo cell-based and yeast assays strengthens the potential biological relevance of the findings.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence supports claim
- **Claim pointer** The authors state that "the N-tail phosphorylated mutant without CSD still undergoes LLPS, but its structural unit is a dynamic intermolecular dimer formed via the phosphorylated N-tail and a basic segment at the CD end."
- **Evidence pointer** Results section "Overall structural differences in HP1α and pHP1α revealed by SEC-MALS/SAXS and CGMD-SAXS"; Figures 2, 3, 4; Supplementary Figs S5, S7, S10, S11
- **Concern** The claim that a specific "dynamic intermolecular dimer" is the structural unit of LLPS is not convincingly established. The CGMD simulations show interaction probabilities, but the distinction between a stable, specific dimer and transient, non-specific contacts in a concentrated solution is not clear. The SAXS data show concentration-dependent changes in Rg, but these are interpreted as evidence for oligomerization without a clear model-free analysis. The authors do not provide a quantitative comparison of the fitted ensembles to alternative models (e.g., monomer with expanded conformations, or a distribution of oligomeric states). The term "structural unit" implies a defined, repeating building block, but the data presented are more consistent with a dynamic ensemble of weakly associated molecules. To support this claim, the authors should provide a more rigorous analysis, such as a detailed comparison of the SAXS data to models of specific dimeric versus non-specific aggregates, or direct evidence for a stable dimeric intermediate (e.g., from NMR relaxation or diffusion measurements).
- **Why it matters** This is the central structural claim of the paper. If the "structural unit" is not a well-defined dimer, the proposed model for LLPS is not correct, and the interpretation of the in vivo experiments is weakened.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence supports claim
- **Claim pointer** The authors state that "mutation of this basic segment in HP1α affects the size of heterochromatin foci in cultured mammalian cells, suggesting that this interaction plays an important role in heterochromatin formation in vivo."
- **Evidence pointer** Results section "Effect of b4 mutation on the heterochromatic localization"; Figure 7
- **Concern** The in vivo experiments are correlative and do not establish a causal link between the b4 interaction and heterochromatin formation. The authors show that the b4 mutant has smaller foci, but they do not demonstrate that this is due to a loss of the specific N-tail-b4 interaction. The b4 mutation could affect other functions of HP1α, such as nucleosome binding, dimerization, or interactions with other proteins. The authors also do not assess whether the b4 mutant affects global heterochromatin structure or gene silencing beyond the foci size measurement. The yeast silencing assay shows a defect for the SAb4 double mutant, but the single b4 mutant has only a mild effect, which is not fully consistent with the cell-based data. To strengthen this claim, the authors should perform additional experiments, such as complementation with a b4 mutant that specifically disrupts the N-tail interaction but not other functions, or measure direct effects on chromatin compaction or transcriptional silencing.
- **Why it matters** The in vivo relevance is a key part of the paper's significance. Without direct evidence that the b4 interaction is the mechanistic driver, the physiological importance of the proposed model remains speculative.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical rigor
- **Claim pointer** The authors use CGMD simulations with a modified MARTINI force field and BME reweighting to generate structural ensembles.
- **Evidence pointer** Materials and methods section "CGMD simulations"; Supplementary Data (referenced but not provided)
- **Concern** The description of the CGMD simulations and the BME reweighting is insufficient to assess their validity. The modifications to the MARTINI force field are not described in detail, and the parameters for the BME reweighting (e.g., the value of θ, the choice of prior, the convergence criteria) are not given. The authors state that θ was set to 20, but the justification for this value and the sensitivity of the results to this choice are not discussed. The validation of the reweighted ensembles (e.g., comparison to independent experimental data, assessment of ensemble convergence) is not presented. Without these details, it is difficult to evaluate whether the simulated ensembles are reliable.
- **Why it matters** The CGMD simulations are a key component of the structural analysis. If the simulations are not properly validated, the conclusions drawn from them (e.g., the interaction probabilities) are not trustworthy.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Clarity and reproducibility
- **Claim pointer** The authors describe the use of NMR, SEC-MALS, SEC-SAXS, and CGMD to probe HP1α and its mutants.
- **Evidence pointer** Materials and methods section; Results section
- **Concern** The manuscript is difficult to follow in several places. The distinction between experiments performed on the full-length dimer versus the ΔCSD monomer is not always clear. The logic of the experimental design, particularly the order of experiments and how each builds on the previous one, could be presented more clearly. Some figure panels are referenced but not described in the text, and the reader is often directed to supplementary figures for key data. The authors should consider reorganizing the results to present a clearer narrative and ensure that all key data are shown in the main figures.
- **Why it matters** The impact of the work is diminished if the reader cannot easily follow the experimental logic and the evidence for each claim.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The abstract states that HP1α "consists of an N-terminal disordered tail (N-tail), chromodomain (CD), hinge region (HR), and C-terminal chromo shadow domain (CSD)." This is a standard description, but the abstract could be more specific about the novel findings, particularly the identification of the b4 segment.
- **Required correction** Consider revising the abstract to more explicitly state the key new finding: that the b4 segment of the CD is a critical interaction partner for the phosphorylated N-tail in driving LLPS.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Materials and methods, NMR spectroscopy
- **Evidence pointer** Materials and methods section "NMR spectroscopy"
- **Issue** The NMR experiments are described, but the assignment completeness and the quality of the spectra are not discussed. The authors state that "significant chemical shift changes" were observed, but the criteria for significance are not defined.
- **Required correction** Provide a brief statement on the completeness of the backbone assignments and define the threshold for a "significant" chemical shift change.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical analysis
- **Affected element** Results, microscopy
- **Evidence pointer** Results section "Effect of b4 mutation on the heterochromatic localization"; Figure 7C–E
- **Issue** The quantification of foci size and number is presented, but the statistical analysis is not described in detail. The authors state that data were evaluated by Mann-Whitney's U test, but the number of independent experiments and the dispersion of the data are not shown.
- **Required correction** Provide more detail on the statistical analysis, including the number of independent experiments, the number of cells analyzed, and the measure of variability (e.g., SD or SEM) for each condition.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion, paragraph 3
- **Issue** The authors discuss the potential role of DNA and RNA in promoting LLPS, but this is not directly tested in the current study. This is presented as speculation, which is appropriate, but it could be more clearly labeled as such.
- **Required correction** Consider adding a sentence to clarify that the role of DNA/RNA in the b4-mediated interaction is a hypothesis that requires further testing.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Nomenclature
- **Affected element** Throughout
- **Evidence pointer** Figure 1A, Results
- **Issue** The authors use a numbering system for acidic (a1–a7) and basic (b1–b7) segments. This is helpful, but the correspondence between these segments and specific amino acid residues is not always clear in the text.
- **Required correction** Consider providing a table or a more detailed figure legend that maps the segment names to specific residue ranges.

## Risk / unsupported claims
- The claim that the pΔCSD dimer is "the core structural unit" of LLPS is not fully supported by the presented data, as the evidence for a specific, stable dimeric intermediate is indirect.
- The claim that the b4 interaction "plays an important role in heterochromatin formation in vivo" is correlative and not mechanistically established.
- The interpretation of the CGMD simulation results is difficult to assess without the full details of the force field modifications and the BME reweighting procedure.
- The statement that "the phosphorylated N-tail in pHP1α interacts intra- and/or intermolecularly with other basic regions" is based on chemical shift changes, but the specific residues involved in these interactions are not identified with high confidence.
- The relationship between the observed "dynamic dimer" of pΔCSD and the oligomers formed by full-length pHP1α is not clearly established.