## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, conclusions, materials and methods) with supplementary material descriptions
- **Assessment boundary** Scientific claims, methodological soundness, interpretation of results, and alignment with stated conclusions
- **Shared manuscript claim summary** The authors use 2D IR spectroscopy and MD simulations to show that water dynamics within a peptide-nucleic acid biocondensate are slower than in dilute solution, attributing the slowdown to local electrostatic interactions and bound water rather than global network disruption.
- **Visible evidence base** FTIR spectra (Figure 1), 2D IR spectra (Figure 2), CLS decay data (Figure 3), MD H-bond autocorrelations (Figure 4), diffusion coefficient histograms (Figure 5), supplementary figures and tables referenced (Figures S8, S9; Tables S4, S5)
- **Missing materials affecting confidence** Raw 2D IR spectra, CLS fitting parameters and uncertainties, full MD trajectory analysis details, force field validation data, experimental replicates and error analysis, sample characterization data (e.g., droplet size, concentration verification)

## Reviewer
- **Overall assessment** The manuscript presents a technically sophisticated application of 2D IR spectroscopy to a biologically relevant model system, with complementary MD simulations. The central claim that water dynamics slow within condensates is supported by the data shown, and the distinction between local electrostatic effects and global network disruption is a valuable contribution. However, several methodological details and quantitative comparisons require clarification before the conclusions can be fully accepted.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, hydration dynamics, and ultrafast spectroscopy. The work bridges physical chemistry and cell biology, and the finding that local interactions dominate water dynamics has implications for understanding biochemical reaction rates and molecular mobility within condensates.
- **Major strengths** The combination of multiple vibrational probes provides complementary views of the local environment. The use of MD simulations to interpret experimental observables is well integrated. The comparison between dilute, peptide-only, and condensate phases allows systematic attribution of dynamical changes. The manuscript is clearly written and the figures are informative.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Quantitative rigor of CLS analysis
  - **Claim pointer** The authors state that CLS decay times slow by ~2x to 6x between bulk and condensate phases for the various probes.
  - **Evidence pointer** Figure 3, Section "Experimental Measure of H-bond Dynamics in the Bulk and Condensate Phases"
  - **Concern** The CLS analysis is described qualitatively, but no uncertainties, fitting errors, or replicate measurements are reported. The claim of specific slowdown factors (e.g., 6x for arginine) requires quantitative support, particularly given the congested spectra and the need for difference spectra to isolate individual components.
  - **Why it matters** The magnitude of the slowdown is a central quantitative claim. Without error bars or replicate measurements, it is impossible to assess whether the reported differences between phases are statistically significant or within experimental noise.
  - **Resolution test** Provide CLS decay curves with fit uncertainties, report the number of independent measurements, and include error propagation in the reported time constants. If possible, show representative raw 2D IR spectra at multiple waiting times to demonstrate data quality.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Simulation-experiment comparability
  - **Claim pointer** The authors state that MD simulations "provide an atomistic interpretation" and that H-bond autocorrelations "agree qualitatively" with experimental slowdowns.
  - **Evidence pointer** Figure 4, Section "Slowdown of Dynamics within the Condensate Phase"
  - **Concern** The comparison between experimental CLD decay times (0.38-2.26 ps) and simulated H-bond autocorrelation times (reported as 3.2-4.2 ps for C=O, 1.5-3.4 ps for arginine) is not quantitatively reconciled. The experimental observable (frequency fluctuations) and simulated observable (H-bond lifetime) are related but not identical, and the manuscript does not explain how these are expected to correspond.
  - **Why it matters** The claim of agreement between experiment and simulation is central to the interpretation. Without a clear mapping between the two observables, the qualitative agreement could be coincidental or could mask important discrepancies.
  - **Resolution test** Provide a quantitative framework connecting CLS decay times to H-bond correlation times, or explicitly state the limitations of direct comparison. Consider computing the FFCF from simulations to enable direct comparison with experimental observables.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Attribution of slowdown mechanism
  - **Claim pointer** The authors conclude that "local interactions, and not the percolation networks, dominate the slowdown in dynamics."
  - **Evidence pointer** Section "Slowdown of Dynamics within the Condensate Phase", Figure 5
  - **Concern** The diffusion coefficient histograms (Figure 5) show a population of slow water in the condensate, but the attribution of this slowdown specifically to local electrostatic interactions rather than confinement or crowding effects is not directly tested. The comparison between dilute and condensate phases includes both concentration and interaction changes, which are not fully disentangled.
  - **Why it matters** The mechanistic conclusion is the main conceptual advance of the paper. If the slowdown could equally be explained by geometric confinement or excluded volume effects, the interpretation would need revision.
  - **Resolution test** Perform additional simulations with varying interaction strengths or concentrations to isolate the contribution of electrostatics versus crowding. Alternatively, compare with a neutral crowding agent to separate these effects.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Sample characterization
  - **Affected element** Methods, Sample Preparation
  - **Evidence pointer** Section "Sample Preparation"
  - **Issue** The manuscript does not report verification of phase separation (e.g., microscopy images, turbidity measurements) or droplet size distribution for the specific samples used in spectroscopy.
  - **Required correction** Include a representative microscopy image or turbidity measurement confirming phase separation under the exact experimental conditions used for 2D IR.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Spectral assignment
  - **Affected element** Results, FTIR interpretation
  - **Evidence pointer** Figure 1D
  - **Issue** The assignment of the 1645 cm-1 band to amide I in a disordered peptide is stated but not justified with secondary structure analysis or comparison to model compounds.
  - **Required correction** Provide reference spectra or secondary structure analysis supporting the assignment, or acknowledge the ambiguity in this region.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Simulation validation
  - **Affected element** Methods, MD Simulations
  - **Evidence pointer** Section "Molecular Dynamics Simulations"
  - **Issue** The force field choice (CHARMM36) is stated but no validation of the force field for this specific system (e.g., comparison to experimental structural or dynamical data) is provided.
  - **Required correction** Add a brief validation statement or reference supporting the use of CHARMM36 for poly-arginine and AMP systems.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Statistical treatment
  - **Affected element** Results, CLS analysis
  - **Evidence pointer** Figure 3
  - **Issue** The number of independent measurements or scans used for each CLS data point is not reported.
  - **Required correction** State the number of replicates and how uncertainties were propagated in the fitting procedure.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** Throughout
  - **Evidence pointer** Abstract, Discussion
  - **Issue** The term "bound water" is used without a precise operational definition, which could be confused with the more established concept of protein-bound water in the biophysics literature.
  - **Required correction** Define "bound water" operationally in the context of the simulation analysis and clarify how it relates to previous definitions.

## Technical failings that need to be addressed before the case is established
- R1-M1: Lack of quantitative uncertainty in CLS decay times
- R1-M2: Unclear mapping between experimental and simulated observables

## Assessment against Nature-style criteria
- **Originality** The application of 2D IR spectroscopy to biocondensates is novel, and the distinction between local electrostatic and global network effects on water dynamics is a fresh perspective. However, the general concept of slowed water dynamics in crowded environments is well established.
- **Scientific importance** Understanding water dynamics in condensates is relevant to the rapidly growing field of phase separation and has implications for biochemical reaction rates. The work provides a foundation for future studies, though the model system is relatively simple.
- **Interdisciplinary readership** The work bridges ultrafast spectroscopy, biophysics, and cell biology. The writing is accessible to nonspecialists in each field, though some familiarity with 2D IR methodology is assumed.
- **Technical soundness** The experimental approach is sound in principle, but the lack of quantitative error analysis and the unclear experiment-simulation comparison weaken the technical case. The simulation methodology is standard but not fully validated for this system.
- **Readability for nonspecialists** The manuscript is generally well written, with clear figures and logical flow. The abstract effectively communicates the main findings. Some sections, particularly the MD analysis, may be challenging for readers without simulation experience.

## Recommendation posture
Supportive if technical concerns are resolved. The core finding is likely correct and interesting, but the quantitative claims require stronger statistical support and the experiment-simulation comparison needs clarification. The mechanistic interpretation, while plausible, requires additional evidence to exclude alternative explanations.

## Risk / unsupported claims
- The specific slowdown factors (2x, 6x, 20%) are presented without uncertainties, making them unverifiable from the provided data.
- The claim that "local interactions, and not the percolation networks, dominate the slowdown" is not directly tested and could be influenced by confounding factors.
- The statement that simulations "predict that a fraction of water molecules are highly constrained" is supported by the diffusion analysis, but the quantitative relationship to the experimental observable is not established.
- The assertion that the 20% amide I slowdown is "comparable to previous measurements of crowded environments" is made without direct quantitative comparison to the cited literature.
- The claim that the "dilute" phase in simulations captures the same physics as the experimental dilute phase is not validated, given the different concentrations and compositions.