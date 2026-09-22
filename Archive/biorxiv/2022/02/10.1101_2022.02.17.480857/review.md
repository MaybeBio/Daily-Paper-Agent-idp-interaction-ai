## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary figure/table references
- **Assessment boundary** Scientific claims, methodological soundness, data interpretation, and presentation quality based solely on the provided manuscript text
- **Shared manuscript claim summary** The authors report time-resolved serial crystallography at a synchrotron and XFEL capturing the release of azo-combretastatin A4 from tubulin, showing cis-to-trans isomerization, formation of a metastable binding pose, opening of an exit channel, collapse of the binding pocket, and global backbone rearrangements related to microtubule-destabilizing drug action
- **Visible evidence base** Abstract, introduction, results sections (three subsections), discussion, methods (including synthesis, crystallization, data collection, processing, and computational details), data availability statement, author contributions, and references to supplementary figures, tables, movies, and datasets
- **Missing materials affecting confidence** Supplementary figures, tables, movies, and datasets referenced but not provided; no structural statistics tables (R-factors, B-factors, completeness) visible; no difference map quality metrics beyond qualitative description; no raw time-resolved data or validation of extrapolation procedure; no details on the number of crystals per time point or hit rates beyond total indexed patterns

## Reviewer
- **Overall assessment** This manuscript presents a technically ambitious application of time-resolved serial crystallography to a non-photoactive protein target using a photopharmacological ligand. The experimental design is innovative and the temporal coverage from 1 ns to 100 ms is impressive. However, the evidence presented in the text alone is insufficient to fully evaluate the robustness of the structural interpretations, particularly regarding the extrapolation procedure, occupancy estimates, and the assignment of specific conformational states. The claims about ligand release timing and the "molecular gate" mechanism require stronger quantitative support. The work is potentially significant for both photopharmacology and time-resolved crystallography communities, but the current presentation leaves several technical questions unanswered.
- **Who would be interested in the results, and why** Structural biologists using time-resolved crystallography, photopharmacology researchers developing light-sensitive drugs, medicinal chemists targeting tubulin and the colchicine site, and biophysicists studying protein-ligand dynamics. The demonstration that photopharmacological compounds can trigger non-photoactive proteins for time-resolved studies will interest a broad community seeking to expand the applicability of pump-probe crystallography beyond naturally photoactive proteins.
- **Major strengths** 1) Novel application of photopharmacology to enable time-resolved studies on a non-photoactive protein target, expanding the scope of the technique. 2) Wide temporal coverage spanning nine orders of magnitude with nine time points. 3) Combination of synchrotron and XFEL data to achieve both temporal resolution and spatial resolution. 4) Integration of experimental structures with MD simulations to support mechanistic interpretations. 5) Clear articulation of the biological relevance to tubulin-targeting drugs and the colchicine site.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (extrapolation procedure validation), R1-M2 (occupancy scaling), R1-M3 (ligand release timing), R1-M4 (channel diameter interpretation)
- **Assessment against Nature-style criteria** Originality: High. The use of photopharmacological compounds as triggers for time-resolved crystallography on non-photoactive proteins is a novel concept with broad potential applicability. Scientific importance: Moderate to high. The work provides mechanistic insight into photopharmacology and tubulin dynamics, but the direct therapeutic or biological implications beyond the specific system are not fully developed. Interdisciplinary readership: The work bridges photochemistry, structural biology, and pharmacology, and should appeal to researchers across these fields. Technical soundness: The experimental execution appears careful, but the text does not provide sufficient detail to fully assess the validity of the extrapolation and occupancy scaling procedures. Readability for nonspecialists: The manuscript is generally well-written and accessible, though some methodological details in the results sections assume familiarity with serial crystallography concepts.
- **Recommendation posture** Supportive if technical concerns are resolved. The core concept and experimental approach are compelling, but the quantitative basis for several key claims needs strengthening before the conclusions can be fully accepted.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim to have generated atomic models for predominant intermediate states using extrapolated data from the light-activated fraction of structure factors.
- **Evidence pointer** Methods section "Data extrapolation", Results section "Formation of a metastable binding pose after azo-CA4 photoisomerization", Supplementary Table 2
- **Concern** The extrapolation procedure is critical to the structural interpretation, but the text provides insufficient detail to evaluate its validity. The activation level of 22% is described as an average of values fluctuating between 18-27%, yet the manuscript does not report the activation level for each individual time point. If the activation level varies significantly across time points, the extrapolated maps may have different signal-to-noise characteristics, potentially biasing the interpretation of intermediate states. Additionally, the method for determining activation level relies on integrating negative density around nitrogen atoms of the ligand, but the text does not specify how many atoms were used, whether the integration radius was optimized, or how sensitive the final structures are to the chosen activation level.
- **Why it matters** The structural models of intermediate states are the central deliverable of this work. If the extrapolation procedure introduces systematic errors or if the activation level is incorrect, the resulting models could misrepresent the actual conformational states populated during the reaction. This would undermine the mechanistic conclusions about ligand release and protein dynamics.
- **Resolution test** Provide per-time-point activation levels with associated uncertainties, show how the final models change when activation level is varied within the reported range, and include validation metrics such as map-model correlation coefficients or difference map quality indicators for each extrapolated dataset.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that the negative density of the apo state was downscaled to lower occupancy by assuming a roughly 4-fold occupancy increase is similar to a 4-fold increase in the number of observations, resulting in an estimated scaling factor of 0.5.
- **Evidence pointer** Methods section "Integration of negative density around the ligand"
- **Concern** The scaling procedure for comparing apo-state negative density with time-resolved data is not rigorously justified. The assumption that a 4-fold occupancy increase is equivalent to a 4-fold increase in observations, leading to a scaling factor of 0.5, is not derived from any statistical model. The relationship between occupancy and signal-to-noise in difference density maps is not linear in general, and the square-root scaling implied by the factor of 0.5 assumes noise-dominated measurements, which may not hold. This scaling directly affects the interpretation of when ligand release is complete (the claim that release occurs between 1 and 10 ms).
- **Why it matters** The timing of ligand release is a key quantitative claim of the paper. If the scaling is incorrect, the conclusion that residual ligand is present at 10 ms and fully released at 100 ms could be an artifact of the normalization procedure rather than a real physical observation.
- **Resolution test** Provide a rigorous statistical justification for the scaling factor, or present the raw integrated negative density values without scaling and show that the conclusions are robust to reasonable variations in the scaling approach. Alternatively, use an independent method to estimate occupancy at each time point.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Data interpretation
- **Claim pointer** The authors state that "ligand release starts after the 1 ms delay" based on the build-up of negative density around azo-CA4 and the Pearson correlation analysis.
- **Evidence pointer** Results section "Formation of a metastable binding pose after azo-CA4 photoisomerization", Figure 1C
- **Concern** The assignment of ligand release timing relies on visual inspection of difference maps and integration of negative density, but the text does not provide quantitative criteria for when release is considered to have "started." The Pearson correlation analysis identifies three blocks of elevated correlation, but the relationship between these blocks and specific structural events is not rigorously established. The claim that release starts after 1 ms appears to be based on the onset of significant negative density, but no statistical threshold is defined.
- **Why it matters** The temporal sequence of events (isomerization, metastable pose formation, channel opening, ligand release, pocket collapse) is the central narrative of the paper. Without clear quantitative criteria for assigning event timing, the proposed sequence could be subjective.
- **Resolution test** Define explicit criteria for when a structural change is considered significant (e.g., density above a certain sigma threshold in a defined region), apply these criteria consistently across all time points, and show that the resulting event sequence is robust to reasonable variations in the criteria.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Data interpretation
- **Claim pointer** The authors describe the formation of an 8 Å long channel with a diameter of 4-6 Å as a possible exit site for the ligand, and suggest that the channel transiently widens in short-lived intermediates.
- **Evidence pointer** Results section "Binding pocket changes upon azo-CA4 release", Figure 3B-C
- **Concern** The channel dimensions are reported with precision (8 Å length, 4-6 Å diameter) but the text does not specify how these measurements were made, what atoms define the channel boundaries, or what the uncertainty in these measurements is. The suggestion that the channel "transiently widens" is speculative and not directly supported by the data presented, as no short-lived intermediates were observed.
- **Why it matters** The channel is proposed as the exit route for the ligand, which is a key mechanistic claim. If the channel dimensions are not robustly determined, or if the transient widening is purely speculative, the proposed release mechanism is weakened.
- **Resolution test** Provide details on how channel dimensions were calculated (e.g., using CAVER output, pore radius profiles), report uncertainties, and clearly distinguish between observed states and speculative intermediates. If transient widening is proposed, provide supporting evidence from MD simulations or state explicitly that this is a hypothesis.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section "Adapting photopharmacology for time-resolved serial crystallography"
- **Evidence pointer** Figure 1B, Methods section "Pearson correlation of difference maps"
- **Issue** The Pearson correlation analysis is described briefly, and the criteria for defining "three major blocks of elevated correlation" are not specified. The normalization procedure (reducing datasets to match the lowest multiplicity) is mentioned but the rationale and potential impact on the analysis are not discussed.
- **Required correction** Provide a more detailed description of the Pearson correlation analysis, including how blocks were defined, what threshold was used for "elevated" correlation, and how the normalization to 55,065 patterns affects the sensitivity of the analysis.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods section "Time-resolved spectroscopy measurements"
- **Evidence pointer** Supplementary Figure 3
- **Issue** The transient absorption spectroscopy data are mentioned as characterizing the ultrafast regime, but no results from these measurements are presented in the main text. The connection between the spectroscopy data and the crystallographic time points is not explicitly made.
- **Required correction** Briefly summarize the key findings from the spectroscopy experiments in the results or discussion, and explain how they informed the choice of time points for the crystallographic experiments.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section "Global backbone rearrangements"
- **Evidence pointer** Figure 4
- **Issue** The description of backbone movements relies on visual inspection of displacement vectors, but the text does not provide quantitative measures of the magnitude or significance of these movements. The statement that "curvature is reduced significantly" is not supported by statistical analysis.
- **Required correction** Provide quantitative measures of backbone displacements (e.g., RMSD values between states) and statistical analysis of the curvature change, or soften the language to reflect the qualitative nature of the observation.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section "Computational Methods"
- **Evidence pointer** Location not provided
- **Issue** The description of the MD simulation setup is incomplete. The total simulation time is stated as "cumulative 30 μs-long" but the number of replicas, the length of individual simulations, and the convergence criteria are not specified. The WTMD simulation details are also incomplete, with the bias factor and deposition rate given but not the temperature or pressure coupling parameters.
- **Required correction** Provide complete simulation parameters including ensemble, thermostat/barostat settings, number of replicas, individual simulation lengths, and convergence assessment.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Discussion section
- **Evidence pointer** Location not provided
- **Issue** The discussion of the broader applicability of this approach to other protein-ligand systems is brief and somewhat generic. The authors mention that similar photoswitchable compounds could be used for other targets, but do not discuss potential limitations or challenges in generalizing the approach.
- **Required correction** Expand the discussion to address potential limitations, such as the need for high-occupancy binding, the requirement for crystal packing to accommodate conformational changes, and the generalizability of the photopharmacological trigger strategy.

## Risk / unsupported claims
- The claim that ligand release starts after 1 ms is based on qualitative inspection of difference maps without defined statistical criteria.
- The claim that the channel "transiently widens" is speculative and not directly supported by observed data.
- The scaling factor of 0.5 for comparing apo-state and time-resolved negative density is not rigorously justified.
- The claim that global backbone movements "evolve in par with" ligand structural alterations is not quantitatively supported.
- The statement that the approach will be applicable to "kinases, channels, G protein-coupled receptors, and other pharmaceutically relevant protein targets" is speculative and not demonstrated by the current work.
- The activation levels for individual time points are not reported, making it impossible to assess whether the 22% average is representative.