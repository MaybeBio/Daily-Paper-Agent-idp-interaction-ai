## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods) as provided
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided text; no external data or supplementary figures were available for independent verification
- **Shared manuscript claim summary** The authors propose that the shelterin component TRF2 drives both single-chain DNA compaction and multi-chain phase separation through multivalent interactions, and that the binding partner hRap1 modulates these processes, acting as a specificity switch between nucleic acid types. They further argue that single-chain condensation and multi-chain phase separation are two outcomes of the same underlying molecular interactions, consistent with the theoretical framework of Post and Zimm.
- **Visible evidence base** Single-molecule force spectroscopy (optical tweezers, magnetic tweezers), turbidity assays, DIC and fluorescence microscopy, FRAP, coarse-grained Monte Carlo simulations, and phase diagram construction
- **Missing materials affecting confidence** Supplementary figures and tables (S1–S10), detailed FRAP analysis methods, phase diagram tie-line construction details, simulation parameter tables, and raw data traces; these are referenced but not provided in the submitted text

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question in telomere biology and biomolecular condensate research: whether the shelterin protein TRF2 can drive nucleic acid condensation and phase separation, and how binding partners modulate these processes. The authors combine a commendable array of biophysical techniques, including single-molecule force spectroscopy, turbidity measurements, microscopy, FRAP, and coarse-grained simulations, to build a case for a unified framework linking single-chain compaction and multi-chain phase separation. The central hypothesis, grounded in the polymer physics framework of Post and Zimm, is intellectually appealing and potentially significant. However, the manuscript as presented has several critical gaps that prevent full assessment of the claims. The most significant concerns relate to the interpretation of the force spectroscopy data, the quantitative rigor of the phase diagram construction, the lack of direct evidence for the proposed hRap1 mechanism, and the absence of key methodological details. The work is promising and likely of interest to the condensate and telomere communities, but the current evidence does not fully establish the central claims.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates and phase separation, particularly those interested in nucleic acid-protein interactions and chromatin organization. The telomere biology community will also find this relevant, given the proposed role of shelterin components in telomere compaction and clustering. Additionally, biophysicists using single-molecule techniques and coarse-grained simulations to study polymer condensation will be interested in the methodological approach and the proposed link between single-chain and multi-chain phenomena.

- **Major strengths**
  1. The manuscript addresses a significant and timely question with broad implications for both telomere biology and the phase separation field.
  2. The combination of multiple orthogonal techniques (single-molecule force spectroscopy, turbidity, microscopy, FRAP, simulations) is commendable and provides complementary perspectives.
  3. The theoretical framing via the Post and Zimm framework provides a coherent conceptual basis for linking single-chain compaction and multi-chain phase separation.
  4. The inclusion of coarse-grained simulations to recapitulate experimental trends adds a valuable layer of mechanistic insight.
  5. The identification of hRap1 as a modulator of TRF2-mediated condensation is a novel and potentially important finding.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Data interpretation and claim support
- **Claim pointer** The authors claim that TRF2 promotes single-chain dsDNA condensation based on optical tweezer and magnetic tweezer experiments, and that this compaction is cooperative and force-dependent.
- **Evidence pointer** Results section "TRF2 promotes single-chain dsDNA condensation"; Figures 2A–G
- **Concern** The force spectroscopy data as described are difficult to interpret quantitatively. In the optical tweezer experiments, the authors report that upon lowering the drag force in the presence of TRF2, the DNA compacts rapidly and completely, with the free bead eventually being pulled into the active trap. This behavior is described as "dramatic" and "rapid," but no quantitative analysis of the compaction kinetics, the force threshold for compaction, or the reversibility of the process is provided. The magnetic tweezer data show a wide range of behaviors across individual tethers, including irreversible compaction at high force, which suggests significant heterogeneity. The authors state that this is "suggestive of a highly cooperative mode of DNA condensation," but no quantitative measure of cooperativity (e.g., Hill coefficient) is presented. The hysteresis between relaxation and pulling is mentioned but not quantified. Without these quantitative details, the claim that TRF2 drives cooperative single-chain compaction is not fully supported by the presented evidence.
- **Why it matters** The central premise of the manuscript is that TRF2 drives single-chain DNA compaction. If this claim is not rigorously established with quantitative force spectroscopy analysis, the entire framework linking compaction to phase separation is weakened. The heterogeneity in the magnetic tweezer data, in particular, raises questions about whether the observed compaction is a well-defined, cooperative process or a more stochastic, aggregation-like phenomenon.
- **Resolution test** Provide quantitative analysis of the force-extension curves, including: (1) the distribution of compaction forces across multiple tethers, (2) a measure of cooperativity (e.g., Hill coefficient or a two-state analysis), (3) the reversibility of compaction upon force increase, and (4) a comparison of compaction behavior between telomeric and non-telomeric DNA with appropriate statistical analysis. If the process is truly cooperative, a clear two-state transition should be evident in the force-extension data.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative rigor of phase diagram
- **Claim pointer** The authors claim to have constructed a two-dimensional phase diagram with a closed-loop binodal for TRF2 and dsDNA, and that the phase boundaries shift systematically upon addition of hRap1.
- **Evidence pointer** Results section "hRap1 modulates single DNA chain condensation and the phase-separation propensity of TRF2"; Figure 7A–B; Supplementary Information (referenced but not provided)
- **Concern** The construction of the phase diagram is a critical element of the manuscript, as it provides quantitative support for the phase separation claim and the modulatory role of hRap1. However, the methods for determining the binodal and tie-lines are only briefly described, with details relegated to the Supplementary Information, which was not provided for review. The authors state that measurements were carried out using 50 nM of labeled protein or DNA mixed with excess unlabeled components, but the rationale for this labeling strategy, the potential effects of labeling on phase behavior, and the method for determining concentrations in the dense and dilute phases are not described. The claim that the phase boundaries shift toward higher saturation concentrations upon hRap1 addition is presented qualitatively, without quantitative values or error analysis. The tie-line slopes are stated to be positive, supporting co-phase separation, but the uncertainty in these measurements is not reported.
- **Why it matters** The phase diagram is the quantitative centerpiece of the manuscript. Without a rigorous description of how it was constructed, including the methods for concentration determination, the treatment of labeling effects, and the statistical analysis of the binodal and tie-lines, the claim that TRF2 and DNA undergo bona fide phase separation with a closed-loop binodal is not fully verifiable. The modulatory effect of hRap1, a key novel finding, depends entirely on the reliability of these phase boundary measurements.
- **Resolution test** Provide a detailed description of the phase diagram construction, including: (1) the method for determining protein and DNA concentrations in both phases (e.g., fluorescence calibration curves, controls for labeling effects), (2) the number of independent measurements and the error bars on each binodal point, (3) a quantitative comparison of the binodal with and without hRap1, including a statistical test for the shift in phase boundaries, and (4) the method for determining tie-line slopes and their uncertainties.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic claim for hRap1
- **Claim pointer** The authors claim that hRap1 modulates the phase separation propensity of TRF2 by reducing the strength of TRF2-nucleic acid interactions, and that this is mediated by the acidic region of hRap1 interfering with the basic domain of TRF2.
- **Evidence pointer** Results section "hRap1 modulates single DNA chain condensation and the phase-separation propensity of TRF2"; Figures 6A–G; Discussion
- **Concern** The proposed mechanism for hRap1 modulation is speculative and not directly tested. The authors show that hRap1 binding to TRF2 reduces DNA compaction and shifts phase boundaries, and they note that the TRF2-interacting domain of hRap1 is preceded by a highly acidic region. However, no experiments are presented that directly test the role of this acidic region. For example, a mutant hRap1 lacking the acidic region, or a chimeric construct, could be used to test whether the acidic region is necessary for the modulatory effect. Additionally, the claim that hRap1 acts as a "specificity switch" for different nucleic acid types is based on the observation that hRap1 abolishes phase separation with ssNAs but not with dsDNA. However, the mechanism for this differential effect is not explained. The authors suggest that hRap1 reduces non-specific DNA binding more severely than specific telomeric repeat binding, but this is not directly measured.
- **Why it matters** The modulatory role of hRap1 is a central novel finding of the manuscript. If the mechanism is not established, the broader claim that shelterin components can tune the phase behavior of telomeric DNA is weakened. The "specificity switch" concept is potentially important for understanding how telomeres might regulate their physical state, but it requires direct mechanistic support.
- **Resolution test** Perform experiments to directly test the role of the hRap1 acidic region, such as using a deletion mutant or a charge-neutralizing mutation. Measure the binding affinity of TRF2 and TRF2-hRap1 for telomeric vs. non-telomeric DNA and for ssDNA vs. dsDNA to directly test the proposed differential effect. If the acidic region is important, show that its removal abolishes the modulatory effect of hRap1.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability of the model
- **Claim pointer** The authors claim that their results support a general model in which the same molecular interactions drive both single-chain compaction and multi-chain phase separation, and that this framework can be extended to other nucleic acid-protein systems.
- **Evidence pointer** Discussion; Figure 3; Supplementary Figure S9 (referenced but not provided)
- **Concern** The manuscript presents a compelling correlation between conditions that favor single-chain compaction and those that favor multi-chain phase separation, but the causal link is not directly established. The simulations are used to support the model, but the coarse-grained model is highly simplified (single bead per protein, no sequence specificity) and the parameter space explored is not fully described. The claim that this framework can be generalized to other systems is speculative and not supported by data from other protein-nucleic acid pairs. The authors mention that "recent experimental evidence indicates that HP1a... can also form liquid droplets" and draw parallels, but no direct comparison is made.
- **Why it matters** The manuscript aims to provide a general framework for understanding protein-mediated nucleic acid condensation. If the link between single-chain and multi-chain behavior is only correlative, and the model is not tested in other systems, the generalizability claim is not established. This weakens the broader significance of the work.
- **Resolution test** Provide direct experimental evidence for the causal link between single-chain compaction and multi-chain phase separation, for example by showing that mutations that disrupt single-chain compaction also disrupt phase separation in a predictable manner. Alternatively, test the model in a second protein-nucleic acid system to demonstrate generalizability. If the model is intended to be system-specific, temper the generalizability claims accordingly.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Relevance to cellular context
- **Claim pointer** The authors suggest that their in vitro observations may be relevant to telomere organization in cells, including the formation of telomere-induced foci and the clustering of telomeres.
- **Evidence pointer** Introduction; Discussion
- **Concern** The manuscript does not include any experiments in cells or with cellular extracts. The concentrations used in the in vitro experiments (e.g., 10 μM TRF2) are likely much higher than the local concentrations at telomeres in cells. The authors acknowledge this limitation in the discussion but do not provide any quantitative estimate of whether the observed phase separation could occur at physiologically relevant concentrations. The link between the in vitro phase separation and the observed telomere clustering in cells is speculative.
- **Why it matters** The significance of the work for telomere biology depends on the relevance of the in vitro observations to the cellular context. Without any attempt to bridge this gap, the physiological significance of the findings remains unclear.
- **Resolution test** Provide a quantitative estimate of the local concentrations of TRF2 and telomeric DNA at telomeres in cells and compare these to the phase boundary concentrations measured in vitro. If possible, perform experiments with cellular extracts or in cells to test whether the proposed mechanisms operate under more physiologically relevant conditions. Alternatively, temper the claims of cellular relevance.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and completeness of methods
- **Affected element** Materials and Methods, "Coarse-grained simulations"
- **Evidence pointer** Materials and Methods section
- **Issue** The description of the coarse-grained simulations is brief and lacks key details. The authors state that simulations were performed using the PIMMS simulation engine but do not describe the interaction potentials, the mapping between the model and the real TRF2/DNA system, or the equilibration and sampling protocols. The conversion from lattice units to nanometers is presented but the rationale for the chosen conversion factor is not explained.
- **Required correction** Provide a more detailed description of the simulation model, including the interaction potentials, the parameterization procedure, and the equilibration and sampling protocols. Justify the choice of the lattice-to-nanometer conversion factor and discuss its impact on the estimated concentrations.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical analysis
- **Affected element** Turbidity experiments
- **Evidence pointer** Materials and Methods, "Turbidity experiments"
- **Issue** The authors state that "the reported error bars are from three independent readings" but do not specify whether these are technical replicates or independent experiments. The statistical treatment of the data is not described, and no significance tests are reported for comparisons between conditions (e.g., with and without hRap1).
- **Required correction** Clarify the nature of the replicates and provide appropriate statistical analysis for the comparisons made. Report the number of independent experiments and the statistical tests used.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Figure quality and data presentation
- **Affected element** Figures 2, 4, 6
- **Evidence pointer** Results section
- **Issue** The text refers to multiple figures and supplementary figures, but the figures themselves were not provided for review. It is therefore impossible to assess the quality of the data presentation, the clarity of the figures, or whether the data support the claims made in the text.
- **Required correction** Ensure that all figures are provided in a format that allows for careful review. Pay attention to the clarity of the data presentation, including appropriate axis labels, error bars, and figure legends.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology and consistency
- **Affected element** Throughout
- **Evidence pointer** Abstract, Results, Discussion
- **Issue** The terms "condensation," "compaction," and "phase separation" are used throughout the manuscript, but their precise meanings are not always consistent. For example, "condensation" is used to describe both single-chain compaction and multi-chain phase separation, which could be confusing. The authors should define these terms clearly and use them consistently.
- **Required correction** Define the terms "condensation," "compaction," and "phase separation" at the outset and use them consistently throughout the manuscript.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion would benefit from a more thorough treatment of the limitations of the study, particularly regarding the use of purified components, the high concentrations required for phase separation, and the simplified simulation model.
- **Required correction** Expand the discussion of limitations and consider how these limitations might affect the interpretation of the results and their relevance to cellular biology.

## Risk / unsupported claims
- The claim that TRF2 drives cooperative single-chain DNA compaction is not fully supported by quantitative analysis of the force spectroscopy data; the heterogeneity in the magnetic tweezer data and the lack of a quantitative measure of cooperativity leave this claim partially unsupported.
- The claim that hRap1 acts as a "specificity switch" for different nucleic acid types is not directly tested; the proposed mechanism involving the acidic region of hRap1 is speculative.
- The claim that the phase diagram for TRF2 and dsDNA has a closed-loop binodal is not fully verifiable without the detailed methods and data presented in the Supplementary Information.
- The claim that the observed in vitro phase separation is relevant to telomere organization in cells is speculative and not supported by any cellular experiments or quantitative estimates of physiological relevance.
- The generalizability of the model to other protein-nucleic acid systems is not established; the claim is based on a single system and a simplified simulation model.