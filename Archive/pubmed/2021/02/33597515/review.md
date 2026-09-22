## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and figure legends.
- **Assessment boundary** Scientific validity, technical soundness, and support of claims based solely on the provided manuscript content. No external literature or unpublished data were consulted.
- **Shared manuscript claim summary** The authors report that several proteins known to undergo liquid-liquid phase separation (LLPS) at low salt concentrations (FUS, TDP-43, Brd4, Sox2, Annexin A11) exhibit a reentrant phase transition at high salt concentrations (above ~1.5 M KCl). They propose that this high-salt regime is driven by hydrophobic and non-ionic interactions, distinct from the electrostatic contributions at low salt. This is supported by dissolution assays with 1,6-hexanediol, ATP, and poly-U RNA, atomistic simulations of amino acid pairs, and coarse-grained simulations of full-length proteins.
- **Visible evidence base** Figures 1-7, Supplementary Figures 1-4, Supplementary Tables 1-3, and Methods section.
- **Missing materials affecting confidence** Raw imaging data, quantitative analysis of droplet size distributions beyond qualitative statements, full phase diagrams for all proteins (only FUS is shown in detail), and details on the reproducibility of the coarse-grained simulation parameters. The manuscript states "location not provided" for several quantitative claims.

## Reviewer
- **Overall assessment** The manuscript presents a novel and potentially significant observation: reentrant LLPS at high salt concentrations for several disease-relevant proteins. The combination of experimental and computational approaches is commendable. However, the central mechanistic claim that hydrophobic and non-ionic interactions drive this high-salt regime is not fully established by the data presented. The evidence is largely qualitative, and the simulations rely on a reparameterized model whose validation is circular. The manuscript would be strengthened by more quantitative experimental analysis and a more rigorous connection between simulation parameters and experimental observables.
- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, phase separation, protein biophysics, and neurodegeneration. The findings have implications for understanding the driving forces of LLPS, the role of cellular environment in condensate formation, and potential therapeutic strategies targeting condensates.
- **Major strengths** 1. The discovery of reentrant phase behavior at high salt for multiple proteins is a novel and interesting finding that challenges the current understanding of LLPS. 2. The combination of experimental and computational methods provides a multi-scale perspective. 3. The use of multiple proteins (FUS, TDP-43, Brd4, Sox2, A11) suggests a general phenomenon. 4. The dissolution assays with different disruptors are a clever way to probe interaction types.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Evidence supports claim
    - **Claim pointer** The authors claim that "reentrant phase transition in the high-salt regime is driven by hydrophobic and non-ionic interactions, and is mechanistically distinct from the low-salt regime."
    - **Evidence pointer** Figures 3, 5, 6, 7
    - **Concern** The evidence for the mechanistic distinction is indirect. The dissolution assay (Fig. 3) shows that 1,6-hexanediol dissolves high-salt condensates, but this is a standard test for hydrophobic interactions and does not rule out other contributions. The Hofmeister series data (Fig. 5) is consistent with hydrophobic effects but is not a direct measurement. The PMF calculations (Fig. 6) are for isolated amino acid pairs and may not reflect the complex environment within a condensate. The coarse-grained simulations (Fig. 7) are the most direct evidence, but they rely on a reparameterized model where the parameters were adjusted to match the experimental phase behavior (as described in the Methods), making the conclusion somewhat circular.
    - **Why it matters** The central claim of the paper is that the high-salt regime is mechanistically distinct. If this is not convincingly demonstrated, the novelty and impact of the work are significantly reduced.
    - **Resolution test** Provide more direct experimental evidence, such as measuring the contribution of specific interactions (e.g., using mutants that disrupt hydrophobic or π-π interactions) in the high-salt regime. Alternatively, the simulations should be validated against a broader set of experimental observables beyond the phase boundary.
    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Evidence supports claim
    - **Claim pointer** The authors state that "in all cases, high-salt condensates have similar size distributions and shapes as their low-salt counterparts."
    - **Evidence pointer** Supplementary Figure 1
    - **Concern** This claim is based on a qualitative visual comparison. The manuscript states that "An analysis of droplet shape revealed that both low- and high-salt condensates exhibit a high degree of circularity (>95%), and have similar areal distributions (Supplementary Fig. 1)." However, the actual quantitative data (e.g., histograms, statistical tests) are not shown in the main text or the supplementary figure legend. The figure is not provided in the manuscript text.
    - **Why it matters** This claim is used to substantiate the "liquid-like character and structural similarities" of the condensates in both regimes. Without quantitative data, this is an unsupported assertion.
    - **Resolution test** Provide the quantitative analysis of droplet size and shape distributions, including statistical comparisons, for all proteins in both salt regimes.
    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical soundness
    - **Claim pointer** The authors use a reparameterized version of the Mittal coarse-grained model and state that "we developed this reparameterization to recapitulate the higher experimental LLPS propensity at low salt of FUS over its prion-like domain."
    - **Evidence pointer** Methods section, "Experimental validation and refinement of coarse-grained model"
    - **Concern** The reparameterization process is described in a way that suggests the model is being tuned to match the experimental results it is then used to explain. This is a potential circularity issue. The details of the reparameterization (e.g., which parameters were changed, by how much, and based on what criteria) are not fully provided.
    - **Why it matters** The conclusions drawn from the simulations (e.g., that a 10-30% increase in hydrophobicity is sufficient to induce reentrant behavior) are only as valid as the model. If the model is not independently validated, the simulation results are less convincing.
    - **Resolution test** Provide a more detailed description of the reparameterization process and validate the model against a wider range of experimental data (e.g., radius of gyration, critical concentration) for multiple proteins.
- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity
    - **Affected element** Figure 2
    - **Evidence pointer** Figure 2 legend
    - **Issue** The figure legend states that "Brd4 and Sox2 at 50 mM (low salt), 500 mM (intermediate salt), and 2.15 M KCl (high salt)". However, the text in the Results section mentions "above 1.5 M KCl" for the reentrant regime. It is unclear if 2.15 M is the only high-salt condition tested for these proteins.
    - **Required correction** Clarify the range of salt concentrations tested for each protein and specify the exact conditions shown in the figure.
    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Methods, PMF calculations
    - **Evidence pointer** Methods section
    - **Issue** The description of the PMF calculations mentions that "the JC-SPC/E-ion/TIP4P/2005 force field has been optimized for that purpose, and so it was used in this work." However, the main text (Results) states that "We used the state-of-the-art AMBERff03ws force field." This is contradictory.
    - **Required correction** Clarify which force field was used for the PMF calculations and why.
    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Clarity
    - **Affected element** Discussion
    - **Evidence pointer** Discussion section
    - **Issue** The discussion on the implications for the origin of life and druggability is speculative and not directly supported by the data.
    - **Required correction** Consider tempering these statements or clearly labeling them as speculation.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3.

## Risk / unsupported claims
- The claim that high-salt condensates are "mechanistically distinct" from low-salt condensates is not fully supported by the provided evidence.
- The claim that high-salt condensates have "similar size distributions and shapes" as low-salt condensates is not quantitatively supported.
- The claim that the reparameterized coarse-grained model "recapitulates" experimental behavior is potentially circular and not fully validated.
- The statement that "π-π interactions... are dominant driving forces for LLPS in both salt regimes" is an overstatement based on the limited set of amino acid pairs tested in the PMF calculations.
- The relevance of the findings to "druggability" and "origin of life" is speculative and not directly addressed by the experiments.

## Assessment against Nature-style criteria
- **Originality** High. The observation of reentrant LLPS at high salt for multiple proteins is novel and not predicted by current models.
- **Scientific importance** High. The findings challenge the current understanding of the molecular driving forces of LLPS and have implications for the role of the cellular environment in condensate formation.
- **Interdisciplinary readership** Moderate. The topic is of interest to biophysicists, cell biologists, and neuroscientists, but the technical nature of the simulations may limit broader appeal.
- **Technical soundness** Moderate. The experimental methods are standard, but the computational approach has potential circularity issues and the connection between simulation and experiment is not fully rigorous.
- **Readability for nonspecialists** Good. The manuscript is generally well-written and the main concepts are explained clearly, although the simulation methods section is dense.

## Recommendation posture
Supportive if technical concerns are resolved. The core observation is interesting and potentially important, but the central mechanistic claim requires stronger evidence. The authors should provide quantitative experimental data on droplet properties, more direct tests of the interaction types involved, and a more rigorous validation of their computational model.