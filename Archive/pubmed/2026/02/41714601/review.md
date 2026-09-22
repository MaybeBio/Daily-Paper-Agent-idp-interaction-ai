## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and figure legends
- **Assessment boundary** Scientific content, methodological rigor, validity of claims relative to presented evidence, and alignment with Nature-style criteria
- **Shared manuscript claim summary** The authors propose that HBV pgRNA genome organization within the capsid is driven by liquid-liquid phase separation (LLPS) between the pgRNA and the disordered C-terminal domain (CTD) of capsid protein, resulting in a hollow shell-like condensate with coexisting low- and high-density regions. They further claim that this phase separation promotes long-range base-pairing and enhances polymerase mobility, potentially facilitating reverse transcription, and that individual virions exhibit symmetry breaking despite ensemble-averaged icosahedral symmetry.
- **Visible evidence base** All-atom MD simulations (100 ns), coarse-grained MD simulations with AICG2+/3SPN.2 models, slab coexistence simulations, bright-field microscopy of CTD-RNA droplets, AFM imaging, and control simulations (ΔCTD, CTD-Neu, CTD-Free)
- **Missing materials affecting confidence** Supplementary figures and movies referenced but not provided; experimental details for droplet assays partially described; no quantitative comparison between simulation and experimental droplet properties; no direct experimental validation of in-capsid phase separation

## Reviewer
- **Overall assessment** The manuscript presents a novel and potentially significant hypothesis that LLPS governs HBV pgRNA organization within capsid confinement. The combination of multiscale simulations with biochemical assays is ambitious and the topic is of broad interest to virology, biophysics, and structural biology. However, the central claim that phase separation occurs inside the capsid relies heavily on computational inference, with limited direct experimental evidence. Several technical aspects require clarification, particularly regarding the coarse-grained model parameterization, the interpretation of "phase separation" in a single-molecule context, and the functional implications for reverse transcription. The manuscript is intellectually stimulating but the case is not fully established from the provided evidence.
- **Who would be interested in the results, and why** Virologists studying HBV replication and capsid assembly would find the proposed mechanism relevant to understanding genome packaging and reverse transcription. Biophysicists and computational biologists interested in phase separation, polymer physics in confinement, and RNA-protein interactions would value the methodological approach. Structural biologists using cryo-EM to study viral genome organization may find the symmetry-breaking observation pertinent. The potential antiviral targeting of phase behavior could interest drug discovery researchers.
- **Major strengths** 1) The study addresses a fundamental and unresolved question about viral genome organization in confined spaces. 2) The multiscale simulation strategy, combining all-atom and coarse-grained approaches, is appropriate and rigorous. 3) The observation of ensemble-averaged icosahedral symmetry with single-particle asymmetry provides a compelling resolution to previous cryo-EM versus single-molecule discrepancies. 4) The control simulations systematically dissect the role of electrostatic interactions and CTD anchoring. 5) The connection to chromatin organization in the discussion is thought-provoking and broadens the conceptual impact.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (single-molecule phase separation definition), R1-M2 (experimental validation gap), R1-M3 (coarse-grained model justification), R1-M4 (polymerase simulation interpretation)
- **Assessment against Nature-style criteria** **Originality**: High. The application of LLPS concepts to viral genome organization within capsid confinement is novel, and the symmetry-breaking observation at the single-particle level offers a fresh perspective. **Scientific importance**: Potentially high, as it could reshape understanding of HBV replication and offer new antiviral targets, but the functional significance requires stronger evidence. **Interdisciplinary readership**: The topic bridges virology, biophysics, and soft matter physics, appealing to a broad audience. **Technical soundness**: The simulation methodology is generally sound, but concerns about model parameterization and the interpretation of phase separation in a single-molecule system temper confidence. **Readability for nonspecialists**: The manuscript is clearly written and the figures are informative, though some simulation details may be dense for experimental readers. Overall, the manuscript has strong potential but requires revisions to fully meet Nature-level standards of evidence.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly the definition and evidence for phase separation in the capsid context and the functional claims regarding reverse transcription.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Conceptual validity
- **Claim pointer** The manuscript claims that pgRNA undergoes LLPS inside the capsid, forming a hollow shell-like condensate with coexisting low- and high-density regions.
- **Evidence pointer** Results sections "Structural organization of pgRNA genome in HBV capsid" and "Phase separation of pgRNA genome within capsid confinement"; Figures 1d-f, 2d-i
- **Concern** The concept of LLPS typically applies to multi-molecular systems where many molecules demix into dense and dilute phases. In the HBV capsid, there is only a single pgRNA molecule. The authors describe "phase separation" of a single polymer chain into regions of different density along the capsid surface. This is conceptually distinct from canonical LLPS, which involves collective behavior of many molecules. The manuscript does not adequately address this distinction or justify why the single-molecule density heterogeneity should be termed "phase separation" rather than, for example, "surface-induced condensation" or "microphase segregation." The phase diagram in Figure 2i, derived from density binning of a single molecule, may not represent a true thermodynamic phase transition.
- **Why it matters** The central thesis of the paper rests on the LLPS framework. If the phenomenon is not genuine phase separation, the conceptual framing and the proposed antiviral strategy targeting "phase behavior" would be misleading. The distinction is critical for the scientific accuracy and generalizability of the findings.
- **Resolution test** The authors should either (a) provide a rigorous thermodynamic or kinetic argument demonstrating that the observed density heterogeneity represents a phase transition (e.g., showing bimodal density distributions that sharpen with system size or time, or demonstrating nucleation-growth behavior), or (b) reframe the phenomenon as "surface-induced condensation" or "polymer segregation" without invoking LLPS, and adjust the title and discussion accordingly.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental validation
- **Claim pointer** The abstract and discussion state that "biochemical assays" supplement the simulations, and the results claim experimental validation of CTD-RNA phase separation in bulk solution.
- **Evidence pointer** Results section "Phase separation of pgRNA genome in bulk system"; Figure 3d-h; Methods section "Bright field microscopy imaging of droplets"
- **Concern** The experimental validation is limited to bulk-phase droplet assays with CTD peptides and short A15 RNA oligomers. These experiments demonstrate that CTD and RNA can phase separate in solution, but they do not directly validate that phase separation occurs inside the intact capsid with full-length pgRNA. The connection between the bulk experiments and the in-capsid simulations is inferential. Additionally, the droplet assays appear to use only A15 RNA, not the full 3200-nt pgRNA, and the CTD peptides may not fully recapitulate the behavior of the capsid-anchored CTD. The manuscript does not report any experiments that perturb phase separation in the capsid context (e.g., mutating CTD charges, altering salt concentration in intact capsids) to test the model predictions.
- **Why it matters** The claim that LLPS drives pgRNA organization in the capsid is a strong statement that requires direct evidence. Without experimental validation in the capsid context, the physiological relevance of the proposed mechanism remains uncertain. The bulk assays are suggestive but not conclusive.
- **Resolution test** The authors should either (a) perform experiments in intact capsids or capsid-like particles that directly test the phase separation hypothesis (e.g., FRET-based RNA compaction assays, cryo-EM of capsids under different salt conditions, or mutagenesis of CTD charged residues followed by structural analysis), or (b) temper the claims to clearly state that the in-capsid phase separation is a computational prediction requiring experimental verification.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Methodological rigor
- **Claim pointer** The coarse-grained simulations are used to map the phase diagram and characterize the condensate structure, with claims of quantitative accuracy (e.g., "the arginine-RNA ratio in the dense phase stabilizes at a characteristic value of ~1.05–1.11").
- **Evidence pointer** Methods section "Residue-resolved coarse-grained MD simulations"; Figures 2, 4, 6
- **Concern** The coarse-grained model combines AICG2+ for the folded NTD and HPS for the disordered CTD, with 3SPN.2 for RNA. The manuscript states that the HPS model was used for CTD interactions, but the specific parameters (e.g., the scaling factor for hydrophobic interactions, the salt-dependent electrostatic treatment) are not fully described. The claim that the model "accurately reproduced the average root mean square fluctuation (RMSF) of HBV capsid protein dimers obtained from previous atomistic MD simulations" is presented without quantitative comparison. Furthermore, the 3SPN.2 model is parameterized for DNA, and its application to RNA may require adjustments that are not described. The sensitivity of the phase diagram to model parameters is not assessed.
- **Why it matters** The quantitative predictions (e.g., density ratios, phase boundaries) depend critically on the force field parameters. If the model is not properly validated for RNA-protein interactions in confined geometries, the specific numbers and the phase diagram may not be reliable. This affects the robustness of the conclusions.
- **Resolution test** The authors should provide a more detailed description of the model parameters, including the HPS scaling parameters and any RNA-specific adjustments to 3SPN.2. They should also perform a sensitivity analysis (e.g., varying the HPS scaling factor or the electrostatic strength) to demonstrate that the qualitative conclusions are robust to parameter choices.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Functional interpretation
- **Claim pointer** The manuscript claims that phase separation "promotes long-range base-pairing and enhances polymerase mobility," which "may facilitate the functional dynamics of polymerase during reverse transcription."
- **Evidence pointer** Results section "Role of phase separation on long-range base-pairing and polymerase mobility"; Figure 7
- **Concern** The simulations with polymerase show that phase separation conditions increase long-range base-pairing and polymerase mobility compared to conditions without phase separation. However, the polymerase is modeled as a rigid body from AlphaFold2, and its interactions with RNA and CTD are not described in detail. The claim that enhanced mobility "may facilitate" reverse transcription is speculative. The manuscript does not demonstrate that the observed mobility differences are functionally relevant, nor does it connect the simulation timescales (100 ns to 1 microsecond) to the biologically relevant timescales of reverse transcription (minutes to hours). The schematic in Figure 7f is illustrative but not evidence.
- **Why it matters** The functional significance of the proposed mechanism is a key selling point for the paper's importance. If the link to reverse transcription is not supported, the impact is reduced to a structural observation. Overstating functional implications could mislead readers.
- **Resolution test** The authors should either (a) provide additional simulations or experiments that directly test the functional role of phase separation in reverse transcription (e.g., in vitro reverse transcription assays with and without phase-separated condensates), or (b) clearly label the reverse transcription implications as speculative and remove or soften the causal language.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 2i phase diagram
- **Evidence pointer** Results section "Phase separation of pgRNA genome within capsid confinement"; Figure 2i
- **Issue** The phase diagram in Figure 2i is described as "mapped via the mean densities of the low- and high-density regions," but the criteria for defining these regions and the threshold values are not clearly stated in the main text. The reader cannot assess how the phase boundary was determined.
- **Required correction** Provide a clear definition of the density thresholds used to classify low- and high-density regions, and describe how the phase boundary was determined (e.g., inflection point, percolation threshold). Consider adding this information to the Methods section or the figure legend.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Simulation protocols
- **Evidence pointer** Methods section "All atom MD simulations" and "Residue-resolved coarse-grained MD simulations"
- **Issue** The Methods section does not specify the number of independent simulations performed for each condition, the total simulation time for the coarse-grained simulations, or the criteria for determining convergence. The manuscript states "three independent simulations" for the polymerase-containing system but not for other systems.
- **Required Correction** Add a table or text specifying the number of replicates, simulation lengths, and convergence criteria for all simulation types. This is essential for reproducibility.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure 2h and other quantitative comparisons
- **Evidence pointer** Results section "Phase separation of pgRNA genome within capsid confinement"; Figure 2h
- **Issue** The manuscript reports "Data are presented as mean +/- standard deviation (SD) derived from 3 independent simulations" but does not report statistical tests for comparisons between conditions (e.g., low vs. high salt). It is unclear whether the observed differences are statistically significant.
- **Required Correction** Perform appropriate statistical tests (e.g., t-test or ANOVA) for key comparisons and report p-values or confidence intervals. If tests are not appropriate, state this explicitly.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion section
- **Evidence pointer** Discussion, paragraph 3
- **Issue** The discussion mentions that "phase separation has been observed during the life cycles of diverse viruses" and cites several examples, but does not discuss how the proposed capsid-confined LLSP differs from or relates to these prior observations in terms of mechanism or function. The comparison to chromatin organization is interesting but brief.
- **Required Correction** Expand the discussion to more explicitly compare and contrast the proposed mechanism with prior viral phase separation studies, and elaborate on the implications of the chromatin analogy.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract and throughout
- **Evidence pointer** Abstract, line 5
- **Issue** The term "liquid-liquid phase separation" is used throughout, but the authors also describe the condensate as "hollow, shell-like" and "along the inner capsid surface." This is a surface-mediated process, which may be better described as "surface-induced phase separation" or "heterogeneous condensation." The terminology could confuse readers familiar with bulk LLPS.
- **Required Correction** Consider using more precise terminology, such as "surface-induced phase separation" or "interfacial condensation," and define the term clearly when first used.

## Risk / unsupported claims
- The claim that "LLPS drives the establishment of microphases composed of nematically aligned RNA hairpin arrays" is based on simulation analysis, but the nematic order parameter calculation is not described in sufficient detail to assess its validity.
- The statement that "the phase separation promotes the establishment of long-range base-pairing interactions and enhance the mobility of the polymerase" is supported by simulation data, but the causal link to reverse transcription efficiency is not demonstrated and should be considered speculative.
- The claim that "targeting the phase behavior of CTD-pgRNA condensates could thus represent a novel antiviral strategy" is presented without any experimental evidence that disrupting phase separation would inhibit viral replication. This is an extrapolation that requires validation.
- The assertion that "the ensemble-averaged density distribution recapitulates the icosahedral symmetry as observed in cryo-EM maps" is based on comparison with published data, but the quantitative agreement is not shown. The authors should provide a direct comparison or overlay to support this claim.
- The statement that "the observed pgRNA condensation is a robust process, largely insensitive to the choice of initial pgRNA structures and force fields" is based on two additional simulations, which is a limited sampling. The robustness claim may be overstated.