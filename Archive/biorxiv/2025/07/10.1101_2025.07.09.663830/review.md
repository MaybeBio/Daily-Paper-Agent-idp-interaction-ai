## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no access to full text, figures, tables, or methods
- **Shared manuscript claim summary** The authors report that the hydrodynamic radius of the highly charged, aspartic and glutamic acid-rich intrinsically disordered protein AGARP decreases in a counterion valency-dependent manner, with divalent cations (Ca²⁺, Mg²⁺) inducing collapse at lower activities than monovalent cations (Na⁺, K⁺). They further claim that monovalent ion effects are quantitatively captured by Debye–Hückel screening, whereas divalent ion binding produces enhanced compaction not explained by screening alone, and that collapse occurs without secondary structure formation. They propose that specific chelation of divalent ions by disordered polyanionic chains is a key mechanism regulating IDP compaction.
- **Visible evidence base** Abstract text only; methods, quantitative data, and figures not provided
- **Missing materials affecting confidence** Full manuscript, experimental protocols, FCS and SEC data, MD simulation details, theory derivations, CD spectra, statistical analyses, and all figures and tables

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting observation regarding the role of counterion valency in modulating the dimensions of a highly charged IDP. The combination of experimental and computational approaches is appropriate in principle. However, the abstract alone does not provide sufficient quantitative detail to evaluate the strength of the claims. The central assertion that divalent ion binding produces enhanced compaction beyond Debye–Hückel screening requires careful scrutiny of the binding model, the activity ranges used, and the consistency between experimental and simulation results. The claim of a "structure-free electrostatic collapse" is plausible but needs direct evidence that no residual secondary structure or aggregation artifacts confound the measurements. The broader implication regarding biological relevance is speculative at this stage.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, protein phase behavior, ion–protein interactions, and biophysical chemistry of polyelectrolytes would find these results relevant. The work may also interest those investigating cellular ionic environments and how divalent cations such as calcium and magnesium modulate IDP conformations in signaling or stress contexts.
- **Major strengths** The study addresses a timely and mechanistically important question about how ion valency governs IDP compaction. The use of multiple orthogonal techniques (FCS, SEC, CD, MD, theory) is commendable. The explicit comparison between monovalent and divalent cations across a range of activities is a useful design. The claim that compaction occurs without secondary structure formation, if well supported, would distinguish this system from other IDPs that gain structure upon collapse.
- **Major Concerns**  
  - **Concern ID** R1-M1  
    **Severity** Major  
    **Blocking** Yes  
    **Axis** Evidence sufficiency  
    **Claim pointer** "divalent cations (Ca²⁺, Mg²⁺) inducing collapse at much lower activities than monovalent cations (Na⁺, K⁺)"  
    **Evidence pointer** Abstract; location not provided  
    **Concern** The abstract does not report the specific activity ranges tested, the magnitude of the hydrodynamic radius changes, or the statistical significance of the differences between ion species. Without these quantitative details, it is impossible to assess whether the valency-dependent effect is robust or within experimental noise.  
    **Why it matters** The central claim of the paper rests on a clear, quantitative demonstration that divalent ions are more effective at inducing collapse. If the activity ranges are not matched appropriately or the effect sizes are small, the conclusion may not be supported.  
    **Resolution test** Provide a table or figure showing hydrodynamic radius as a function of ion activity for each cation, with error bars and statistical tests, and state the activity ranges and the fold-change in radius at comparable activities.  
  - **Concern ID** R1-M2  
    **Severity** Major  
    **Blocking** Yes  
    **Axis** Mechanistic attribution  
    **Claim pointer** "Molecular dynamics simulations, direct sampling, and polyampholyte theory quantitatively capture the Debye–Hückel screening by monovalent ions but not the enhanced compaction driven by divalent ion binding"  
    **Evidence pointer** Abstract; location not provided  
    **Concern** The abstract does not specify how "binding" is defined or quantified in the simulations, nor how the theory was modified to account for divalent ion effects. The claim that screening alone fails to explain the data requires a clear comparison between predicted and observed radii for divalent ions, and a demonstration that the discrepancy is not due to force field inaccuracies or sampling limitations.  
    **Why it matters** The mechanistic conclusion that specific chelation drives collapse depends on ruling out alternative explanations such as ion correlation effects, charge neutralization, or simulation artifacts. Without this, the proposed mechanism remains speculative.  
    **Resolution test** Show quantitative agreement between theory and experiment for monovalent ions, and a clear, statistically meaningful deviation for divalent ions. Provide a binding model with fitted affinities and demonstrate that the model reproduces the observed collapse.  
  - **Concern ID** R1-M3  
    **Severity** Major  
    **Blocking** No  
    **Axis** Structural interpretation  
    **Claim pointer** "Circular dichroism spectroscopy shows that compaction occurs without secondary structure formation"  
    **Evidence pointer** Abstract; location not provided  
    **Concern** The abstract states that no secondary structure forms, but it does not report the CD spectral features, the wavelength range, or the analysis method used to reach this conclusion. It is also unclear whether the CD measurements were performed under the same ionic conditions as the FCS and SEC experiments.  
    **Why it matters** The claim of a "structure-free" collapse is a key distinguishing feature. If the CD data are not collected at matching conditions or are not sensitive enough to detect transient structure, the conclusion may be overstated.  
    **Resolution test** Provide CD spectra at representative ion activities for each cation, with a quantitative analysis (e.g., secondary structure estimation) and a statement confirming that the measurements were performed under conditions identical to those used for size measurements.  
  - **Concern ID** R1-M4  
    **Severity** Major  
    **Blocking** No  
    **Axis** Generalizability  
    **Claim pointer** "suggest that specific chelation of divalent ions by disordered polyanionic protein chains is a key mechanism regulating IDP compaction, with implications for understanding their behavior in biologically relevant ionic environments"  
    **Evidence pointer** Abstract; location not provided  
    **Concern** The abstract generalizes from a single model protein (AGARP) to IDPs broadly. It is not clear whether AGARP is representative of other acidic IDPs, or whether the observed behavior is specific to its sequence composition and charge density.  
    **Why it matters** The broader significance of the work depends on whether the mechanism is generalizable. Without comparative data on other IDPs or a clear rationale for why AGARP is a good model, the claim of broad relevance is not yet established.  
    **Resolution test** Either provide data on additional acidic IDPs or temper the claim to be specific to AGARP and discuss the sequence features that may limit or extend generalizability.

- **Minor Comments**  
  - **Concern ID** R1-m1  
    **Severity** Minor  
    **Axis** Clarity  
    **Affected element** Terminology  
    **Evidence pointer** Abstract; location not provided  
    **Issue** The term "direct sampling" is used without definition. It is unclear whether this refers to a specific simulation technique or a general approach.  
    **Required correction** Define "direct sampling" in the methods or abstract, or replace with a more standard term such as "equilibrium sampling" or "enhanced sampling" as appropriate.  
  - **Concern ID** R1-m2  
    **Severity** Minor  
    **Axis** Completeness  
    **Affected element** Ion species  
    **Evidence pointer** Abstract; location not provided  
    **Issue** The abstract lists Ca²⁺ and Mg²⁺ as divalent cations and Na⁺ and K⁺ as monovalent cations, but it does not state whether other ions were tested or whether the choice was based on biological relevance.  
    **Required correction** Briefly state the rationale for ion selection or note that other ions were tested and excluded for clarity.  
  - **Concern ID** R1-m3  
    **Severity** Minor  
    **Axis** Interpretation  
    **Affected element** Biological relevance  
    **Evidence pointer** Abstract; location not provided  
    **Issue** The claim of "implications for understanding their behavior in biologically relevant ionic environments" is vague. It is not specified which environments or processes are meant.  
    **Required correction** Specify the biological context (e.g., cellular calcium signaling, magnesium-dependent processes) or remove the claim if not directly supported by the data.

## Risk / unsupported claims
- The claim that divalent ion binding produces enhanced compaction beyond Debye–Hückel screening is not quantitatively supported in the abstract.
- The claim that collapse occurs without secondary structure formation is not verifiable without CD data.
- The generalization to IDPs broadly and the biological implications are speculative based on the abstract alone.
- The specific mechanism of "specific chelation" is not defined or evidenced in the abstract.