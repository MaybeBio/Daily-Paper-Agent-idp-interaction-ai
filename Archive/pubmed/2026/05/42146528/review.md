## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion) from bioRxiv preprint
- **Assessment boundary** Scientific validity of claims as supported by the presented data; no assessment of editorial fit or publication venue appropriateness
- **Shared manuscript claim summary** The authors report that mTORC2-mediated phosphorylation at a single conserved serine in the disordered RRM2-KH1 linker of IGF2BP1 and IGF2BP3 acts as a configurational switch, reorganizing long-range arrangements of RNA-binding domains without altering secondary structure or substantially changing RNA-binding affinity. They further claim that the resulting configurational landscapes differ between the two paralogs despite high sequence identity, and that these differences likely underlie paralog-specific RNA recognition and functional outcomes.
- **Visible evidence base** Methods sections for protein expression, pSer incorporation, fluorescence anisotropy, CD, nanoDSF, mass photometry, NMR, XL-MS, CW-EPR, and DEER spectroscopy; Results sections describing outcomes of these experiments; Figures 1–8 referenced but not directly viewable; Supplementary Tables 1–4 and Supplementary Figures 1–2 referenced but not directly viewable
- **Missing materials affecting confidence** Figures and supplementary materials not provided; raw data, fitting parameters, and statistical details for several experiments not fully described; no information on replicate numbers for XL-MS or EPR/DEER experiments; NMR assignments and resonance-specific CSP analysis not shown; no data for IGF2BP2 despite title referencing three paralogs

## Reviewer

- **Overall assessment** This manuscript addresses an important and timely question: how post-translational modification of intrinsically disordered regions in multi-domain RNA-binding proteins modulates function. The combination of genetic code expansion for site-specific pSer incorporation with multiple biophysical techniques is methodologically ambitious and appropriate. The central claim that phosphorylation acts as a configurational rather than conformational switch is plausible and potentially significant. However, the evidence as presented has several gaps that prevent full evaluation. The most significant concerns are: (1) the absence of quantitative structural data supporting the configurational interpretation, (2) the lack of direct comparison between the two paralogs under identical conditions, (3) the limited functional validation linking configurational changes to biological outcomes, and (4) the absence of IGF2BP2 data despite the title and framing referencing all three paralogs. The manuscript would be strengthened by additional experiments or clearer presentation of existing data.

- **Who would be interested in the results, and why** Researchers studying RNA-binding proteins, post-translational modification, intrinsically disordered regions, and the IGF2BP family specifically. The work is also relevant to those interested in how multi-domain proteins achieve binding specificity through conformational ensembles rather than static structures. The methodological approach combining genetic code expansion with multiple biophysical techniques may interest structural biologists and chemical biologists. Given the oncofetal nature of IGF2BPs and their roles in cancer, the work has potential translational relevance for cancer biology.

- **Major strengths** The use of genetic code expansion for site-specific pSer incorporation is technically sophisticated and appropriate for studying a defined phosphorylation event. The multi-technique approach (fluorescence anisotropy, CD, nanoDSF, NMR, XL-MS, EPR/DEER) provides complementary views of the system. The finding that phosphorylation does not dramatically alter RNA-binding affinity despite functional consequences is an important observation that challenges simple affinity-based models of regulation. The comparison between two highly similar paralogs is a useful approach to understand specificity determinants.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency for central claim
- **Claim pointer** The central claim that phosphorylation acts as a "configurational switch" that "reorganizes long-range arrangements of RNA-binding domains and linkers" is presented as the main finding of the manuscript.
- **Evidence pointer** Results sections on XL-MS (Figures 6–7), NMR (Figure 4), and Discussion
- **Concern** The evidence for configurational rearrangements is largely indirect. The XL-MS data show changes in crosslinking patterns, but the interpretation that these reflect "configurational switches" requires validation. The NMR data show only a few CSPs, and the authors acknowledge that local conformational changes cannot be excluded. The CD data show modest changes in helical content that are opposite in direction between the two paralogs. No direct structural measurement (e.g., SAXS, smFRET, or integrative modeling) is presented that would quantitatively define the configurational changes claimed.
- **Why it matters** The central claim of the manuscript is that phosphorylation induces configurational changes. If the evidence only supports local conformational changes or altered dynamics, the conclusion is overstated. The distinction between "configurational" and "conformational" changes is central to the paper's thesis and must be supported by data that can distinguish these possibilities.
- **Resolution test** Provide quantitative structural data (e.g., SAXS-derived radius of gyration and pair-distance distribution functions, or FRET-based distance measurements) comparing unmodified and phosphorylated proteins in both RNA-free and RNA-bound states. Alternatively, use integrative modeling combining XL-MS restraints with molecular dynamics to demonstrate distinct domain arrangements.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Completeness of paralog comparison
- **Claim pointer** The title and framing reference "IGF2BP RNA Binding Paralogs" and the abstract states that "the resulting architectures differ markedly between IGF2BP1 and IGF2BP3 despite >70% sequence identity." The introduction describes all three paralogs (IGF2BP1–3).
- **Evidence pointer** Title; Abstract; Introduction; Results sections on XL-MS (Figures 6–7)
- **Concern** The manuscript presents data for IGF2BP1 and IGF2BP3 but not IGF2BP2. The title references "paralogs" generically, and the introduction describes all three. If the conclusions are meant to apply to the family, IGF2BP2 data are needed. If the conclusions are specific to IGF2BP1 and IGF2BP3, the title and framing should be adjusted. Additionally, the claim that the two studied paralogs show "markedly different" configurational landscapes is based on qualitative comparison of XL-MS patterns; no quantitative metric of similarity or difference is provided.
- **Why it matters** The scope of the claims must match the data. A title referencing all paralogs while data exist for only two creates a mismatch. Furthermore, the claim of paralog-specific differences requires quantitative comparison to be convincing.
- **Resolution test** Either include IGF2BP2 data (even preliminary) or revise the title and framing to specify IGF2BP1 and IGF2BP3. Provide a quantitative comparison metric for XL-MS patterns (e.g., correlation coefficients, distance difference matrices) to support the claim of paralog-specific differences.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Functional relevance
- **Claim pointer** The abstract and discussion state that the phosphorylation-dependent configurational landscapes "likely underlie differences in mRNA recognition modes and functional outcomes" and that the work "program[s] target mRNA selection, processing, and translational fate."
- **Evidence pointer** Abstract; Discussion
- **Concern** The manuscript does not include any functional experiments linking the observed configurational changes to mRNA recognition, processing, or translational outcomes. The connection between the biophysical observations and the claimed functional consequences is entirely speculative. While the authors cite prior work on the functional importance of these phosphorylation sites, the present study does not directly test whether the configurational changes they observe are responsible for any functional difference.
- **Why it matters** The significance of the work depends on the functional relevance of the observed changes. Without functional validation, the manuscript describes structural/biophysical observations whose biological importance remains uncertain.
- **Resolution test** Include at least one functional experiment (e.g., mRNA target binding in cells, reporter assays with phospho-null and phospho-mimetic mutants, or analysis of downstream mRNA targets) that links the phosphorylation-dependent configurational changes to a measurable biological outcome.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative rigor of binding data
- **Claim pointer** The abstract states that phosphorylation has "only modest effects on RNA-binding affinity." The Results section reports KD values for IGF2BP1 (6.7±1.7 nM) versus IGF2BP1-pSer181 (17.3±3.1 nM) and IGF2BP3 (17.2±4.2 nM) versus IGF2BP3-pSer184 (58.4±15.5 nM).
- **Evidence pointer** Results section "Phosphorylation at the mTORC2 sites moderately affects the RNA binding affinity of both IGF2BP1 and IGF2BP3"; Figure 3
- **Concern** The reported changes represent approximately 2.5-fold and 3.4-fold reductions in affinity for IGF2BP1 and IGF2BP3, respectively. Whether these are "modest" is a matter of interpretation, but the error bars overlap substantially for IGF2BP3 (17.2±4.2 vs. 58.4±15.5). The statistical significance of these differences is not reported. Additionally, only one RNA substrate was used for each protein, and it is unclear whether these substrates are the optimal or physiologically relevant targets.
- **Why it matters** The claim of "modest effects" is central to the paper's thesis that regulation occurs through configurational changes rather than affinity changes. If the affinity changes are not statistically significant, the claim is weakened. If they are significant, the interpretation of "modest" needs justification.
- **Resolution test** Report statistical analysis (e.g., t-tests or ANOVA) for the KD comparisons. Test additional RNA substrates to determine whether the affinity changes are substrate-specific. Provide a rationale for why the chosen substrates are representative.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of EPR/DEER data
- **Claim pointer** The Results section states that DEER data "support the binding of two RNA molecules to IGF2BP1, and this signal is enhanced for IGF2BP1-pSer181" and that "populations 2 and 3 mainly represent intermolecular distance contributions from the 3′ and 5′ ends, respectively."
- **Evidence pointer** Results section on CW-EPR and DEER spectroscopy; Figure 8
- **Concern** The DEER experiments were performed on RNA with spin labels at two positions. The interpretation of distance populations as reflecting specific RNA conformations requires careful validation. The assignment of populations 2 and 3 to intermolecular contributions is based on comparison of singly- and doubly-labeled samples, but the analysis is not fully described. The authors state that "a decrease in population 1 indicates that IGF2BP1 binding partially promotes unfolding and extension of the RNA," but the structural basis for this interpretation is not clear.
- **Why it matters** The DEER data are used to support the claim that phosphorylation changes the structure of bound RNA. If the interpretation is not robust, this aspect of the conclusion is weakened.
- **Resolution test** Provide a more detailed description of the DEER data analysis, including how distance populations were assigned and how the singly-labeled controls were used. Consider complementary approaches (e.g., smFRET) to validate the RNA conformational changes.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** Abstract; Introduction; Discussion
- **Evidence pointer** Throughout
- **Issue** The distinction between "configurational" and "conformational" changes is introduced but not rigorously defined. The authors state that configurational changes refer to "the relative position of one domain with respect to another" while conformational changes are "structural changes within a single domain." However, in practice, the techniques used (CD, NMR CSPs, XL-MS) may not cleanly distinguish these categories.
- **Required correction** Provide a clearer operational definition of configurational versus conformational changes and explicitly state which techniques report on which type of change. Consider whether the data can truly distinguish these categories or whether the distinction is more conceptual.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results sections on fluorescence anisotropy, CD, nanoDSF
- **Evidence pointer** Figure 3; Supplementary Table 3
- **Issue** The number of independent replicates for each experiment is not consistently reported. For the fluorescence anisotropy measurements, it is unclear how many independent protein preparations and measurements were performed. For CD and nanoDSF, the text mentions "three independent measurements" but does not specify whether these are technical or biological replicates.
- **Required correction** Clearly state the number of biological and technical replicates for each experiment. Report statistical tests and p-values where relevant.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Figure accessibility
- **Affected element** All figures
- **Evidence pointer** Figures 1–8
- **Issue** The figures are not provided in the manuscript text, making it impossible to evaluate the quality of the data presentation. Key claims about XL-MS patterns, NMR CSPs, and DEER distance distributions cannot be assessed without seeing the actual data.
- **Required correction** Ensure figures are available for review. Consider whether the current figure design clearly supports the claims made in the text.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction; Discussion
- **Evidence pointer** References 45–51
- **Issue** The discussion of prior work on IGF2BP phosphorylation is brief. The authors cite several papers on the functional importance of mTORC2-mediated phosphorylation but do not discuss in detail how their structural findings relate to or extend these prior observations.
- **Required correction** Expand the discussion of prior functional studies and explicitly state how the current structural findings provide new insight beyond what was already known.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Methods section on DEER spectroscopy
- **Evidence pointer** Methods section "Continuous wave (CW)-EPR and DEER spectroscopy"
- **Issue** The DEER data analysis is described briefly. The manuscript mentions "home-written software (DeerA)" and that "the distance distribution is assumed to consist of a sum of Gaussians," but does not provide details on how the number of Gaussians was determined or how the statistical criterion was applied.
- **Required correction** Provide additional detail on the DEER data analysis, including the model selection procedure and any validation of the fitting approach.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Scope of conclusions
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion extrapolates from the in vitro biophysical observations to broad claims about "paralog-specific RNA regulatory functions" and "programming target mRNA selection, processing, and translational fate." While these speculations are reasonable, they go beyond the data presented.
- **Required correction** Clearly distinguish between what the data directly show and what is speculative. Consider softening the language in the discussion to avoid overstatement.

- **Technical failings that need to be addressed before the case is established** R1-M1 (configurational switch claim requires more direct structural evidence), R1-M2 (missing IGF2BP2 data relative to title claims), R1-M4 (statistical significance of binding affinity changes not reported)

- **Assessment against Nature-style criteria** 
  - Originality: The application of genetic code expansion to study phosphorylation in IGF2BP proteins is novel, and the concept of phosphorylation as a configurational rather than conformational switch is an interesting contribution. However, the general idea that IDR phosphorylation modulates protein function is well established, and the specific findings here are incremental rather than paradigm-shifting.
  - Scientific importance: The IGF2BP family is biologically important in development and cancer, and understanding how phosphorylation regulates their function has potential significance. However, the manuscript does not yet establish the functional consequences of the observed configurational changes, limiting the immediate importance.
  - Interdisciplinary readership: The work bridges structural biology, biophysics, and RNA biology, which could appeal to a broad audience. However, the technical nature of the methods may limit accessibility to non-specialists.
  - Technical soundness: The methods are generally appropriate and well-executed, but several concerns remain: the interpretation of XL-MS and DEER data requires more rigorous quantitative analysis, and the statistical treatment of binding data is incomplete.
  - Readability for nonspecialists: The manuscript is generally well-written and the concepts are explained clearly. However, the distinction between configurational and conformational changes could be made more accessible, and the significance of the findings for RNA biology could be better contextualized for a general audience.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an interesting question with a sophisticated methodological approach, and the core observation that phosphorylation induces paralog-specific configurational changes without altering secondary structure or dramatically affecting affinity is potentially valuable. However, the central claim requires more direct structural evidence, the paralog comparison is incomplete, and the functional relevance remains speculative. These issues should be addressed before the case is fully established.

## Risk / unsupported claims
- The claim that phosphorylation acts as a "configurational switch" reorganizing long-range domain arrangements is not directly supported by the data presented; the evidence is indirect and alternative interpretations (local conformational changes, altered dynamics) are not excluded.
- The claim that the configurational landscapes "differ markedly" between IGF2BP1 and IGF2BP3 is based on qualitative comparison of XL-MS patterns without quantitative metrics.
- The claim that the observed changes "likely underlie differences in mRNA recognition modes and functional outcomes" is speculative and not tested in this manuscript.
- The title references "IGF2BP RNA Binding Paralogs" generically, but data are presented for only two of the three paralogs.
- The statement that phosphorylation has "only modest effects on RNA-binding affinity" is not supported by statistical analysis; the reported changes may or may not be significant.
- The interpretation of DEER data regarding RNA conformational changes and the assignment of distance populations to specific structural features is not fully validated.