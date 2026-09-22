## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results and discussion, conclusions, materials and methods) as provided
- **Assessment boundary** Scientific content, experimental design, data interpretation, and internal consistency of the provided manuscript text only; no external literature verification or access to supplementary figures/tables beyond what is referenced
- **Shared manuscript claim summary** The authors design a library of single-stranded DNAs with varying degrees of predicted structural order and palindromic dimerization elements, and combine spectroscopic, scattering, computational, and phase-behavior assays to show that (i) an HIV NC-derived peptide (HNP) promotes DNA compaction, (ii) increasing DNA structural order suppresses liquid–liquid phase separation (LLPS) with HNP, (iii) disordered architectures and palindromic dimerization enhance LLPS and increase condensate viscosity, and (iv) aromatic peptide residues are critical for LLPS with most DNA constructs
- **Visible evidence base** Main text figures referenced (Figures 1–5 approximately, though figure numbering is partially obscured in the provided text), supplementary figures S1–S36 and tables S1–S9 as referenced, methods section with experimental protocols
- **Missing materials affecting confidence** Actual figure panels and data plots are not visible; supplementary information content is not provided; exact sequences of DNA constructs are only partially described; statistical details for some comparisons are not fully reported in the visible text

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question: how nucleic acid structural order and sequence-encoded dimerization motifs control peptide/nucleic acid phase behavior. The systematic DNA library design, combining predicted structural order with palindromic elements, is a strength. The integration of multiple experimental techniques (CD, FRET, SAXS, turbidity, microscopy, FRAP, fusion assays) with coarse-grained simulations provides a multi-scale perspective. However, several concerns limit the strength of the conclusions as currently presented. The relationship between dilute-solution structural measurements and condensate behavior is inferred rather than directly demonstrated. The mechanistic distinction between DNA0 and DNAp, both described as disordered, requires clearer structural evidence. The role of Mg2+ appears to differ qualitatively between DNAp and other constructs, yet the interpretation is somewhat speculative. The claim of "chaperone-like" activity for HNP is evocative but may overreach given the peptide is cationic and the observed compaction could be largely electrostatic in origin. The manuscript would benefit from clearer presentation of quantitative data and error analysis in the visible text.

- **Who would be interested in the results, and why** Researchers in biomolecular condensates and LLPS, particularly those studying nucleic acid/protein phase separation; virologists interested in retroviral assembly and nucleocapsid protein function; synthetic biology and biomaterials communities interested in programmable condensates; biophysicists studying nucleic acid structure and dynamics. The design rules proposed (structural order suppresses LLPS, palindromic dimerization enhances it) could inform engineering of synthetic condensates and understanding of viral genome packaging.

- **Major strengths**
  1. Systematic design of a DNA library with graded structural order and controlled palindromic elements, enabling causal inference about sequence-structure-phase behavior relationships
  2. Multi-technique approach spanning single-molecule (FRET), ensemble (CD, SAXS), and mesoscale (microscopy, turbidity, FRAP, fusion) measurements
  3. Integration of coarse-grained simulations to provide mechanistic molecular-level context
  4. The finding that a single phenylalanine-to-alanine substitution abolishes LLPS for most DNA constructs is striking and highlights the importance of aromatic interactions beyond simple electrostatics
  5. The DNAp construct provides a clear demonstration that palindromic dimerization can dramatically enhance LLPS propensity and alter condensate material properties

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength for causal claim
- **Claim pointer** The authors claim that "increasing DNA structural order suppresses LLPS propensity" and that this is a general design principle
- **Evidence pointer** Phase diagrams (Figure 4a–e approximately), CD and FRET data (Figures 1–2), supplementary tables S1–S2
- **Concern** The correlation between predicted structural order and Csat is presented as a monotonic trend, but the visible text reports only three intermediate constructs (DNA0, DNA50, DNA75, DNA100). The differences between DNA50, DNA75, and DNA100 in CD melting behavior appear small (T m values of 26.4, 31.9, and 32.2 °C without Mg2+), yet these constructs show a 1.5-fold difference in Csat (50 vs 75 μM). The statistical significance of these differences is not reported in the visible text. More critically, the causal link between "structural order" and "LLPS suppression" is inferred from correlation. The authors do not directly measure the conformational state of the DNAs within the condensed phase, so it remains possible that the observed differences in phase behavior arise from differences in sequence composition, base-pairing patterns, or effective charge density rather than "order" per se. The claim that this constitutes a "design principle" requires demonstration that the relationship is predictive across a broader sequence space.
- **Why it matters** The central thesis of the manuscript is that structural order is a programmable determinant of phase behavior. If the relationship is not robust or is confounded by other sequence features, the design rules proposed would not be generalizable.
- **Resolution test** Provide quantitative comparison of phase diagrams across all constructs with statistical analysis (e.g., confidence intervals on Csat). Ideally, include at least one additional construct with intermediate predicted order to test the monotonicity of the relationship. Direct measurement of DNA conformation within condensates (e.g., via FRET inside droplets) would substantially strengthen the causal claim.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic interpretation
- **Claim pointer** The authors state that "DNAp condensation is dominated by DNA–DNA interactions enabled by palindromic self-association and Mg2+-mediated charge screening, with the peptide playing a role in network stabilization"
- **Evidence pointer** Phase diagrams (Figure 4e), urea resistance data (Figure S18), FRAP data (Figure 5a–c), fusion assays (Figure 5d–f), simulation data (Figures S11–S17)
- **Concern** The mechanistic distinction between DNAp and the other constructs is a key finding, but the evidence presented in the visible text is largely indirect. The urea resistance of DNAp condensates is interpreted as evidence for DNA–DNA interactions, but urea also disrupts hydrogen bonding and hydrophobic interactions generally, so this does not uniquely identify DNA–DNA interactions. The simulation data are used to propose specific dimer structures (pore-like, head-to-tail), but the relationship between these simulated dimers and the experimentally observed condensates is not established. The claim that Mg2+ is "critical" for DNAp LLPS is based on the observation that DNAp requires Mg2+ for LLPS, but the mechanistic role of Mg2+ (charge screening vs. specific coordination) is not resolved. The authors mention "Mg2+-mediated charge screening" but also note that Mg2+ "facilitates folding of the DNA into compact conformations," which suggests a structural role. These are different mechanisms with different implications.
- **Why it matters** The manuscript proposes two distinct mechanisms for LLPS enhancement: one for disordered DNAs (peptide-mediated, aromatic-dependent) and one for palindromic DNAs (DNA–DNA-mediated, Mg2+-dependent). If this distinction is not robustly supported, the conceptual framework of the paper is weakened.
- **Resolution test** Provide direct experimental evidence for DNA–DNA interactions in DNAp condensates, such as FRET between differentially labeled DNAp molecules within condensates, or demonstrate that a non-palindromic control with similar composition but no dimerization motif does not show the same Mg2+ dependence. Clarify the role of Mg2+ by testing other divalent cations or by varying Mg2+ concentration systematically.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of FRET data
- **Claim pointer** The authors claim that HNP induces compaction of all DNAs, with DNA100 showing the largest increase in FRET efficiency, and that this represents a "chaperone-like" activity
- **Evidence pointer** FRET data (Figure 2e–h), SAXS data (Figure S5), simulation data (Figures S8–S9)
- **Concern** The FRET measurements are performed at 50 nM DNA, where intermolecular interactions are stated to be unlikely. However, the addition of HNP at a 1:1 charge ratio introduces a cationic peptide that could, in principle, cause DNA collapse via charge neutralization rather than specific "chaperone-like" folding. The distinction between "compaction" and "collapse" is not addressed. The SAXS data show an increase in Rg for DNA100 upon HNP addition, which the authors interpret as formation of larger complexes, but this seems inconsistent with the FRET data showing increased compaction. The authors reconcile this by suggesting HNP decorates the DNA scaffold, but this interpretation is not directly tested. The term "chaperone-like" implies a specific activity analogous to protein chaperones, but the observed effects could be explained by generic polyelectrolyte behavior.
- **Why it matters** The "chaperone-like" framing connects the work to viral biology and suggests a specific mechanism of action. If the effect is generic electrostatic compaction, the biological implications are different and the claim of "chaperone-like" activity is overstated.
- **Resolution test** Perform control experiments with a non-aromatic cationic peptide of similar charge density to distinguish specific from generic electrostatic effects. Address the apparent discrepancy between FRET (compaction) and SAXS (expansion) more explicitly, perhaps by measuring FRET and SAXS under identical conditions. Consider whether the term "chaperone-like" is justified or whether "compaction" is more accurate.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of conclusions
- **Claim pointer** The authors conclude that their findings "provide a general design principle for engineering synthetic DNA/peptide condensates with tunable physicochemical properties"
- **Evidence pointer** Conclusions section, phase diagrams (Figure 4), material property measurements (Figure 5)
- **Concern** The study uses a single peptide (HNP) and one peptide variant (F5A). The DNA library, while systematic, is limited to sequences derived from a tRNA scaffold. The claim of "general design principles" requires demonstration that the relationships hold across different peptide sequences, different nucleic acid lengths, and different sequence contexts. The authors do show that F5A fails to induce LLPS for most DNAs, which is informative, but this is a single comparison. The role of peptide length, charge distribution, and aromatic content is not explored. The authors also do not test whether the design principles apply to RNA, which would be more biologically relevant for the viral context they invoke.
- **Why it matters** The stated goal of the work is to provide generalizable design rules. If the findings are specific to this particular DNA/peptide pair, the broader impact is diminished.
- **Resolution test** Include at least one additional peptide with different aromatic content or charge distribution, and ideally one RNA construct, to test the generality of the proposed design principles. Alternatively, temper the claims of generality in the conclusions.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure numbering and referencing
- **Evidence pointer** Throughout the text, figure references appear as "Figure a, b" or "Figure g, h" without clear numbering
- **Issue** The figure references in the provided text are incomplete, making it difficult to map specific claims to specific data panels
- **Required correction** Ensure all figure references include the figure number (e.g., "Figure 2a, b") and that all panels are clearly labeled in the figures

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Quantitative comparisons throughout
- **Evidence pointer** Phase diagrams, FRAP data, fusion assays, CD melting temperatures
- **Issue** The text reports mean values (e.g., T m = 26.4 ± 3.8 °C) but does not consistently report the number of replicates, the statistical test used, or the significance level for key comparisons (e.g., Csat differences between constructs, FRAP recovery differences)
- **Required correction** Add statistical details for all quantitative comparisons, including sample sizes, statistical tests, and p-values or confidence intervals

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology precision
- **Affected element** Use of "chaperone-like" and "structural order"
- **Evidence pointer** Abstract, Results section, Conclusions
- **Issue** The term "chaperone-like" is used to describe HNP activity, but the evidence presented supports compaction rather than folding into a specific structure. Similarly, "structural order" is used to describe the predicted secondary structure, but the experimental measurements (CD, FRET) report on compactness, which is related but not identical to structural order
- **Required correction** Consider using more precise terminology, such as "compaction" instead of "chaperone-like" where appropriate, and clarify the relationship between predicted structural order and experimentally measured compactness

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** FRET calculations in simulations
- **Evidence pointer** Methods section, Computational Details, FRET Efficiency subsection
- **Issue** The empirical method for calculating FRET efficiency from simulations (Equation 2) is described but the justification for this approach and its validation against experimental FRET measurements is not provided
- **Required correction** Add a brief justification for the empirical FRET calculation method and, if possible, a comparison between simulated and experimental FRET efficiencies

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Conclusions section
- **Evidence pointer** Conclusions
- **Issue** The conclusions do not acknowledge the limitations of the study, such as the use of a single peptide, the limited sequence space explored, and the indirect nature of some structural inferences
- **Required correction** Add a brief limitations paragraph to the conclusions or discussion

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Biological relevance framing
- **Affected element** Introduction and Conclusions
- **Evidence pointer** Introduction, Conclusions
- **Issue** The introduction frames the work in the context of viral replication and NC protein function, but the connection between the minimal peptide system and the full-length NC protein is not thoroughly discussed. The conclusions mention "viral genome organization" but do not specify how the findings translate to the viral context
- **Required correction** Add a brief discussion of how the minimal system relates to the full-length NC protein and what additional factors might be relevant in the viral context

## Risk / unsupported claims
1. The claim that "increasing DNA structural order suppresses LLPS" is presented as a general principle but is only demonstrated for four DNA constructs with a single peptide. The causal relationship between structural order and LLPS suppression is inferred from correlation and is not directly tested.
2. The claim that HNP acts as a "chaperone-like" agent is not fully supported. The observed compaction could be explained by generic electrostatic interactions, and the distinction between "chaperone-like" activity and electrostatic collapse is not addressed.
3. The mechanistic distinction between DNAp (DNA–DNA dominated) and other constructs (peptide-mediated) is based on indirect evidence. The urea resistance data and simulation results are suggestive but do not uniquely establish the proposed mechanisms.
4. The claim that the findings provide "general design principles" for engineering synthetic condensates is not supported by the limited parameter space explored (one peptide, one peptide variant, DNA-only, tRNA-derived sequences).
5. The relationship between dilute-solution structural measurements (CD, FRET, SAXS) and the conformational state of DNAs within condensed phases is not established. The authors acknowledge this limitation in the conclusions but do not address it experimentally.
6. The role of Mg2+ in DNAp condensation is described as "charge screening" but could also involve specific coordination or structural effects. The data presented do not distinguish between these possibilities.
7. The claim that DNA50 and DNA75 "possess some degree of structural rigidity, as predicted, but that the level of order of these two DNAs is not substantially different" is based on CD and FRET data that show relatively small differences. The significance of these differences is not reported.