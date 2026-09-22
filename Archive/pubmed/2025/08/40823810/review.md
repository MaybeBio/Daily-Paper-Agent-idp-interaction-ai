## Review setup
- **Input scope** Full manuscript text including abstract, introduction, materials and methods, results, discussion, and supplementary data description
- **Assessment boundary** Scientific claims, methodological soundness, evidence quality, and internal consistency of the presented simulation study
- **Shared manuscript claim summary** The authors use coarse-grained polymer simulations of a nucleus to argue that peripheral heterochromatin tethering to the nuclear lamina is required for chromatin-based nuclear mechanical response, and that heterochromatin crosslinking only contributes to nuclear stiffness when chromatin is tethered
- **Visible evidence base** Simulation results presented in Figures 1-4 and referenced Supplementary Figures S1-S13; methodological descriptions in Materials and methods; comparison to published experimental data cited in the text
- **Missing materials affecting confidence** Supplementary figures and supplementary methods are referenced but not provided in the submitted material; simulation parameter tables and detailed force calibration procedures are not fully described in the main text

## Reviewer
- **Overall assessment** This manuscript presents a systematic computational study addressing an important question in nuclear mechanics: how heterochromatin contributes to nuclear stiffness. The central claim, that peripheral tethering to the lamina is required for heterochromatin to enhance nuclear rigidity, is clearly articulated and supported by the simulation results presented. The study is well-designed with appropriate controls, including comparisons between tethered and untethered systems, varying heterochromatin levels, and different crosslinking conditions. The finding that tethering, not phase separation or affinity interactions alone, is the critical mechanical coupling mechanism is a valuable contribution. However, the manuscript would benefit from clearer presentation of the simulation validation against experimental data, more detailed discussion of parameter choices, and explicit treatment of potential limitations in the coarse-grained approach. The distinction between facultative and constitutive heterochromatin contributions is interesting but requires more mechanistic explanation.

- **Who would be interested in the results, and why** Researchers in nuclear mechanics, chromatin biophysics, mechanotransduction, and computational biology would find these results directly relevant. The work addresses a long-standing question about how heterochromatin stiffens nuclei and provides a mechanistic explanation that reconciles seemingly contradictory experimental observations. The findings have implications for understanding nuclear mechanosensing, gene regulation under mechanical stress, and diseases involving nuclear envelope or chromatin abnormalities. The simulation framework may also be of interest to computational biologists developing polymer models of nuclear organization.

- **Major strengths** The study addresses a mechanistically important question with a well-controlled computational approach. The systematic variation of model parameters (tethering, crosslinking, heterochromatin levels) allows clear attribution of effects. The comparison between tethered and untethered conditions is a particularly clean demonstration of the central claim. The authors also connect their findings to experimental observations, including specific predictions that could be tested experimentally. The discussion of limitations is thoughtful and identifies appropriate caveats.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that their simulation model is "validated by micromechanical measurements and chromosome conformation capture data" (Abstract) and that the model "reproduces the stress-strain responses of isolated nuclei in micromanipulation experiments" (Materials and methods)
- **Evidence pointer** Materials and methods section; Figure 1C; Supplementary Figures S1-S3
- **Concern** The validation of the simulation model against experimental data is described only briefly. The manuscript states that the model reproduces experimental stress-strain responses, but the quantitative comparison is not shown in the main text. The reader cannot assess how well the simulation matches experimental force-extension curves, what specific experimental datasets were used for validation, or what metrics were used to establish agreement. The supplementary figures referenced for this validation are not provided in the submitted material.
- **Why it matters** The central conclusions of the paper depend on the model faithfully representing nuclear mechanics. If the validation is not clearly demonstrated, the reader cannot evaluate whether the simulation results are reliable. The claim that the model captures experimental behavior is foundational to all subsequent findings.
- **Resolution test** Provide a quantitative comparison between simulated and experimental force-extension curves, including the specific experimental datasets used, the fitting procedure, and the quantitative agreement metrics. This could be shown in a main figure or clearly described in the main text with reference to supplementary material that is actually provided.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Parameter justification
- **Claim pointer** The authors state that "interaction strengths between different chromatin types and between heterochromatin and shell subunits were swept and selected to model chromatin phase separation as in previous work" (Materials and methods)
- **Evidence pointer** Materials and methods section; Figure 2D-E
- **Concern** The parameter selection procedure is described only vaguely. The manuscript does not specify the range of interaction strengths tested, the criteria used to select final parameter values, or how sensitive the results are to these choices. The claim that results are robust to parameter variations is not supported by explicit sensitivity analysis. The affinity interaction strengths are central to the phase separation behavior, and the conclusion that affinity interactions do not contribute to nuclear stiffness depends on these parameters being in a realistic range.
- **Why it matters** Without clear parameter justification and sensitivity analysis, the reader cannot determine whether the conclusions are specific to the chosen parameter regime or general. The negative result regarding affinity interactions (Fig. 2D-E) is particularly sensitive to this issue.
- **Resolution test** Provide a systematic parameter sweep showing the range of interaction strengths tested, the selection criteria, and demonstrate that the main conclusions are robust across a reasonable parameter range. Include sensitivity analysis for key results.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Mechanistic interpretation
- **Claim pointer** The authors claim that "tethering only constitutive heterochromatin to the shell does not increase the nuclear spring constant" while "facultative heterochromatin tethering is the main contributor to nuclear rigidity" (Results section, Figure 3A-C)
- **Evidence pointer** Figure 3A-C; Supplementary Figures S7-S8
- **Concern** The mechanistic explanation for why facultative heterochromatin tethering contributes more than constitutive heterochromatin tethering is underdeveloped. The authors mention that facultative heterochromatin has a larger interaction area with the lamina, but the quantitative relationship between tether number, spatial distribution, and mechanical response is not analyzed. The manuscript does not explore whether the difference is due to the number of tethers, their spatial distribution, or intrinsic differences in the chromatin types.
- **Why it matters** Understanding why different heterochromatin types contribute differently to nuclear stiffness is important for interpreting experimental results where specific heterochromatin marks or lamina-associated domains are manipulated. The current explanation is insufficient to guide experimental predictions.
- **Resolution test** Provide analysis of tether number and distribution for facultative versus constitutive heterochromatin, and test whether the observed difference in mechanical response can be explained by tether density alone. This could be done by matching tether numbers between conditions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** The authors state that "our results are general to different types of force application" based on simulations of uniaxial compression (Discussion section, Supplementary Figure S13)
- **Evidence pointer** Discussion section; Supplementary Figure S13
- **Concern** The claim of generality is based on a single additional simulation condition (uniaxial compression) that is only described in the supplementary material. The manuscript does not provide details on the compression protocol, the strain rates used, or the quantitative comparison between tension and compression results. The supplementary figure is not provided in the submitted material.
- **Why it matters** The claim of generality is important for the broader applicability of the findings. If the compression results are not clearly presented, the claim of generality cannot be evaluated.
- **Resolution test** Provide the compression simulation details and a quantitative comparison of the effects of tethering and crosslinking under tension versus compression. If the claim of generality is to be maintained, the evidence must be presented in the main text or clearly accessible supplementary material.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1C description
- **Evidence pointer** Results section, Figure 1C
- **Issue** The description of the force-extension curves in Figure 1C is brief. The text states that the model produces "strain-stiffening force response" but does not describe the shape of the curve in detail or how it compares to experimental curves beyond a general statement of agreement.
- **Required correction** Provide a more detailed description of the simulated force-extension curve, including the strain range over which the response is linear versus nonlinear, and explicitly state the quantitative agreement with experimental data.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Use of "tethering" and "crosslinking"
- **Evidence pointer** Throughout the manuscript
- **Issue** The terms "tethering" and "crosslinking" are used consistently but the distinction between them could be clarified earlier in the manuscript. Tethering refers to chromatin-lamina connections, while crosslinking refers to chromatin-chromatin connections, but this is not explicitly defined until the Results section.
- **Required correction** Define both terms clearly in the Introduction or at the start of the Results section to avoid confusion for readers less familiar with polymer models.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Experimental connection
- **Affected element** Discussion of experimental predictions
- **Evidence pointer** Discussion section
- **Issue** The manuscript makes specific predictions about experimental outcomes (e.g., effects of disrupting tethering proteins on nuclear stiffness), but these predictions are not clearly enumerated or prioritized. The discussion would benefit from a more structured presentation of testable predictions.
- **Required correction** Consider adding a paragraph that explicitly lists the key experimental predictions arising from the model, perhaps in bullet point or numbered format.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Simulation code and data availability
- **Evidence pointer** Data availability section
- **Issue** The manuscript states that data and code are available, but does not specify the version of the code, the simulation software version (beyond LAMMPS), or provide a persistent identifier for the code repository beyond a GitHub URL.
- **Required correction** Provide a versioned release of the code with a DOI (e.g., via Zenodo) and specify the exact software versions used for the simulations.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Variability across replicates
- **Evidence pointer** Materials and methods section
- **Issue** The manuscript states that ten replicates were performed per condition, but the results do not show variability across replicates (e.g., error bars or confidence intervals). It is unclear whether the reported force-extension curves represent single trajectories or averaged results.
- **Required correction** Report the variability across replicates in the figures, or explicitly state that the curves are representative single trajectories and justify this choice.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion of phase separation
- **Evidence pointer** Introduction and Discussion sections
- **Issue** The manuscript discusses heterochromatin phase separation but does not cite or discuss recent experimental work on phase separation of HP1 and heterochromatin in detail. The connection between the simulation results and the broader phase separation literature could be strengthened.
- **Required correction** Add a brief discussion of how the simulation results relate to experimental observations of heterochromatin phase separation and its functional consequences.

## Risk / unsupported claims
- The claim that the model is "validated by micromechanical measurements" is not fully supported by the evidence presented in the main text; the quantitative comparison is not shown
- The claim that results are "general to different types of force application" is based on supplementary material not provided in the submitted manuscript
- The statement that "increases in heterochromatin levels increase nuclear rigidity by increasing the linkages between chromatin and the lamina" is supported for the simulated conditions but the extrapolation to all experimental contexts is not fully justified
- The claim that "crosslinks within heterochromatin can stiffen nuclei, but only if chromatin is peripherally tethered" is supported by the simulations but the quantitative relationship between crosslink density and stiffness is not fully explored
- The assertion that "heterochromatin's internal structure and stiffness may regulate nuclear mechanics via peripheral attachment to the lamina" is presented as a general conclusion but is derived from a specific coarse-grained model with inherent simplifications