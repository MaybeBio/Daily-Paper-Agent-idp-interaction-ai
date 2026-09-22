## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodology, and conclusions as presented in the provided manuscript
- **Shared manuscript claim summary** The authors critically evaluate the REST2 protocol for sampling IDP conformations, identify artificial compaction at high effective temperatures leading to replica segregation, propose a new REST3 protocol with re-calibrated solute-solvent vdW scaling, and demonstrate improved sampling efficiency on two IDP systems.
- **Visible evidence base** Abstract, Introduction, Methods, Results and Discussion, Conclusions, figure references (Figures 1-8, S1-S11), table references (Tables S1-S2)
- **Missing materials affecting confidence** Figures and tables referenced but not provided; simulation parameter details in supplementary tables not accessible; no raw data or trajectory analysis outputs

## Reviewer
- **Overall assessment** The manuscript addresses an important technical limitation in a widely used enhanced sampling method and proposes a practical solution. The identification of REST2-induced compaction is well supported by the described analyses, and the REST3 modification is conceptually sound. However, the evidence base is incomplete due to missing figures and tables, and several claims about sampling efficiency improvements require more rigorous quantitative support. The broader conclusion about limitations of tempering alone is interesting but not fully established from the presented data.
- **Who would be interested in the results, and why** Computational biophysicists and chemists using enhanced sampling methods for disordered proteins, developers of replica exchange protocols, and researchers studying IDP conformational ensembles. The work is directly relevant to those seeking improved sampling efficiency in explicit solvent simulations.
- **Major strengths** Clear identification of a specific artifact in REST2 with mechanistic explanation; proposal of a tunable parameter (κm) that is physically motivated; demonstration on two biologically relevant IDP systems; practical implications for reducing computational cost.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative evidence for sampling improvement), R1-M2 (generality of κm calibration), R1-M3 (convergence assessment methodology)
- **Assessment against Nature-style criteria** Originality: The work identifies a specific and previously underappreciated artifact in REST2 and proposes a novel modification, which is original. Scientific importance: The findings are relevant to a broad community using REST for biomolecular simulations, and the proposed fix has practical value. Interdisciplinary readership: The topic is specialized to computational chemistry and biophysics, limiting broad interdisciplinary appeal. Technical soundness: The methodology is appropriate, but the evidence base is incomplete and some claims lack quantitative rigor. Readability for nonspecialists: The manuscript is written for experts in enhanced sampling; the introduction provides context but assumes familiarity with replica exchange methods.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly the need for quantitative evidence of sampling improvement and demonstration of κm transferability.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "REST3 leads much more efficient temperature random walk and improved sampling efficiency" (Abstract); "REST3 is an effective protocol free of artificial compaction at high effective temperatures and much more suitable for the simulation of dynamic protein conformational ensembles compared to REST2 in general" (Results, section 4)
- **Evidence pointer** Figures 3, 5, 6, 7, 8; location not provided for specific quantitative metrics
- **Concern** The claim of improved sampling efficiency is supported primarily by qualitative descriptions of replica behavior and visual inspection of free energy surfaces. The manuscript reports metrics such as round trips (30.3/μs vs 9-10/μs) and replica segregation, but does not provide a systematic quantitative comparison of conformational ensemble convergence (e.g., block error analysis, autocorrelation times, or statistical efficiency measures) between REST2 and REST3.
- **Why it matters** The central claim of the manuscript is that REST3 improves sampling efficiency. Without rigorous quantitative metrics, the improvement could be anecdotal or system-specific, and the conclusion is not robustly established.
- **Resolution test** Provide quantitative convergence metrics (e.g., ensemble overlap, effective sample size, or autocorrelation times) for key observables (Rg, helicity, PCA projections) comparing REST2 and REST3, with error bars and statistical significance tests.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability
- **Claim pointer** "The new protocol eliminates the exchange bottleneck and greatly improves the efficiency of random walk in the temperature space" (Results, section 4); "REST3 allows one to further reduce the number of replicas required for sufficient sampling" (Conclusions)
- **Evidence pointer** Methods, section "REST algorithm"; Results, section 3; Table S2 (referenced but not provided)
- **Concern** The κm calibration is derived from a single system (p53-NTD) at a single temperature range (298-500 K) with a specific force field (a99SB-disp). The manuscript does not demonstrate that the linear κm relationship is transferable to other systems, force fields, or temperature ranges. The KID test uses the same calibration, but the authors note that KID is less affected by compaction, so this does not constitute a strong test of transferability.
- **Why it matters** If κm must be re-calibrated for each new system, the practical advantage of REST3 over REST2 is diminished, and the claim of general applicability is not supported.
- **Resolution test** Test REST3 with different κm values on at least one additional IDP with different sequence properties and on a folded protein, and show that the same calibration works or provide a systematic procedure for determining κm.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Methodology
- **Claim pointer** "The results suggest that REST3 leads much more efficient temperature random walk and improved sampling efficiency" (Abstract); "REST3 appears to be capable to sample broader metastable states" (Results, section 5)
- **Evidence pointer** Methods, section "Analysis"; Figures 6, 7, 8
- **Concern** The convergence assessment relies on comparing ensembles from two independent simulations (control and folding) initiated from different conformations. While this is a reasonable approach, the manuscript does not describe a quantitative criterion for declaring convergence (e.g., overlap of ensembles, similarity of free energy surfaces). The statement that "substantial residual differences" persist for KID even in REST3 (Results, section 5) suggests that the claimed improvement may be modest.
- **Why it matters** Without a clear convergence criterion, the comparison between REST2 and REST3 is subjective, and the conclusion that REST3 improves convergence is not rigorously supported.
- **Resolution test** Define a quantitative convergence metric (e.g., Jensen-Shannon divergence between ensembles, or a chi-square test on histograms) and apply it to compare REST2 and REST3 at matched simulation times.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods, section "REST algorithm"
- **Evidence pointer** Equations 1-6
- **Issue** The derivation of the κm relationship (Eq. 6) is described in the Results section but not in Methods, which makes the protocol definition incomplete in the Methods section.
- **Required correction** Move the definition of κm and its calibration procedure to the Methods section, or provide a cross-reference from Methods to the relevant Results subsection.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, section "System setup and simulation protocols"
- **Evidence pointer** Table S1 and S2 (referenced but not provided)
- **Issue** The manuscript states that "a total of eight REST simulations were performed" but does not specify the exact number of replicas, temperature spacing, or simulation lengths for each protocol in the main text.
- **Required correction** Provide a summary of simulation parameters in the main text or ensure that Tables S1 and S2 are complete and accessible.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Results, section 1
- **Evidence pointer** Figure 1 and S2
- **Issue** The statement that "p53-NTD adopts spuriously compact ensembles under high temperature conditions in all six force fields" is based on comparison to standard MD at 500 K, but the manuscript does not discuss whether the standard MD simulation itself is converged at 500 K.
- **Required correction** Add a brief discussion of the convergence of the reference standard MD simulations, or acknowledge this as a limitation.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Results, section 5
- **Evidence pointer** Figure 8
- **Issue** The comparison of convergence rates between REST2 and REST3 is described qualitatively ("similar to" and "superior to"), but no numerical values are provided for the convergence times.
- **Required correction** Provide quantitative estimates of convergence times (e.g., time to reach a stable ensemble overlap) for each protocol.

## Risk / unsupported claims
- The claim that REST3 "completely eliminates conformational trapping at high temperatures" is too strong, as it is based on two systems and a single force field; the manuscript itself notes residual convergence issues for KID.
- The claim that "at least about half of the computational sources can be saved compared to REST2" is not directly supported by a systematic scaling analysis; it is inferred from the 8-replica vs 16-replica comparison, which is a single data point.
- The statement that "REST3 leads much more efficient temperature random walk" is supported by round-trip counts, but the statistical significance of the difference is not assessed.
- The general conclusion that "tempering alone" is insufficient for sampling large-scale IDP fluctuations is plausible but not fully established, as the manuscript does not systematically vary the tempering range or compare to other enhanced sampling methods.