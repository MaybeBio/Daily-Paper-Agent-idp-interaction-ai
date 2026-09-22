## Review setup
- **Input scope** Full manuscript text (preprint, arXiv:2510.21430v1)
- **Assessment boundary** Scientific content, methodology, claims, and presentation as provided in the manuscript. No external literature verification performed.
- **Shared manuscript claim summary** The authors propose a general theoretical framework for analyzing spatial self-organization of enzymes in arbitrary catalyzed reaction networks, driven by chemotactic enzyme motion in response to self-generated chemical gradients. They derive a stability criterion and systematically analyze all closed unimolecular reaction networks up to six chemicals, finding that network-wide effects (beyond direct enzyme-substrate/product interactions) can enable or enhance self-organization.
- **Visible evidence base** Main text with equations (1)-(13), Table 1, Figures 1-4 (referenced but not fully visible in text), Methods section, and Supplementary Information references (Tables S1, Figures S1-S2).
- **Missing materials affecting confidence** Figures 1-4 are referenced but not provided in the submitted text. Supplementary figures and tables are mentioned but not included. Numerical validation details (e.g., specific parameter values for Fig. 2) are not fully specified. The manuscript appears to be a preprint and may lack final formatting.

## Reviewer
- **Overall assessment** This manuscript presents a conceptually interesting and potentially significant theoretical contribution to the understanding of enzyme spatial organization in reaction networks. The general framework, culminating in Eq. (9), is elegant and provides a clear criterion for instability. The systematic enumeration of all small closed unimolecular networks is a commendable computational effort. However, the manuscript has several weaknesses that need addressing: the presentation of key results (figures) is incomplete in the provided text, the biological relevance of the specific parameter regimes is not thoroughly discussed, and the connection to experimental observables could be strengthened. The distinction between "direct-phoresis" and "network-induced" mechanisms is a useful conceptual advance, but the practical implications and experimental signatures of these mechanisms require more elaboration.
- **Who would be interested in the results, and why** Researchers in biophysics, systems biology, and nonequilibrium statistical physics would find this work of interest. Specifically, those studying enzyme compartmentalization, metabolon formation, biomolecular condensates, and active matter would benefit from the theoretical framework. The work bridges concepts from chemotaxis, reaction-diffusion systems, and network theory, making it relevant to a broad interdisciplinary audience.
- **Major strengths** 1. The general theoretical framework is concise and applicable to arbitrary networks, representing a significant methodological advance over previous studies limited to simple two-species or single-cycle systems. 2. The systematic enumeration of all 1,052,145 closed unimolecular networks up to six chemicals provides comprehensive and statistically robust results. 3. The identification and characterization of the network-induced (N-I) interaction mechanism, distinct from direct phoresis, is a novel and insightful contribution. 4. The comparison between linear (full interactions) and saturated (naive interactions) kinetics clearly demonstrates the importance of network-wide effects. 5. The manuscript is generally well-written and logically structured.
- **Major Concerns**
- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The manuscript claims that "comparison with the numerical solution of the full eigenvalue problem in (5) confirms that, in order to study the stability of a unimolecular reaction network with uniform parameters, it is sufficient to consider the reduced eigenvalue problem in (12)."
- **Evidence pointer** Figure 2 (referenced but not provided)
- **Concern** The key validation of the reduced eigenvalue problem relies entirely on Figure 2, which is not included in the submitted text. Without seeing this figure, it is impossible to assess the quality and scope of the numerical validation. Specifically, it is unclear how many networks were tested, over what range of parameters, and whether any discrepancies were observed.
- **Why it matters** The reduced eigenvalue problem is central to the entire statistical analysis. If the validation is incomplete or flawed, all subsequent results (Table 1, distributions in Fig. 4) could be compromised.
- **Resolution test** Provide Figure 2 and a detailed description of the numerical validation procedure, including the number of networks tested, parameter ranges, and a quantitative measure of agreement between the reduced and full problems.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Biological relevance
- **Claim pointer** The manuscript states that "spontaneous self-organization through chemotaxis can provide an avenue for the self-regulation of metabolic activity in complex catalyzed reaction networks" and that "signaling molecules could take advantage of this scenario towards their functionality."
- **Evidence pointer** Discussion section
- **Concern** The biological implications are stated somewhat speculatively without concrete examples or quantitative estimates. The parameter regime where the instability occurs (as defined by Eq. 13) is not mapped to realistic biological parameters (e.g., typical enzyme concentrations, diffusion coefficients, chemotactic mobilities, reaction rates). It is unclear whether the predicted instabilities would actually occur in physiological conditions.
- **Why it matters** For the work to have impact beyond theoretical physics, it needs to demonstrate relevance to real biological systems. Without parameter estimates, the reader cannot judge whether the proposed mechanism is plausible in vivo.
- **Resolution test** Add a section or paragraph estimating typical biological parameter values and discussing whether the instability condition (Eq. 13) can be satisfied. Provide at least one concrete example of a metabolic pathway or signaling network where the mechanism might apply.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical rigor
- **Claim pointer** The manuscript claims that "we find that, for saturated kinetics, an interaction network is unstable if and only if it satisfies this self-attraction condition" (referring to negative trace of the interaction matrix).
- **Evidence pointer** Table 1 and accompanying text
- **Concern** This is a strong claim (if and only if) that is stated without a formal proof. While the numerical evidence across all enumerated networks is suggestive, the claim of necessity and sufficiency should be either proven analytically or stated more cautiously as a numerical observation. Additionally, the relationship between the trace condition and the full eigenvalue spectrum of the interaction matrix is not discussed.
- **Why it matters** The "if and only if" claim is a key theoretical result. If it is not rigorously established, it could mislead future work that relies on this criterion.
- **Resolution test** Either provide an analytical proof of the claim for the saturated case, or soften the language to "we observe numerically that..." and discuss any potential counterexamples or limitations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scope of conclusions
- **Claim pointer** The manuscript concludes that "network-wide effects can facilitate self-organization" and that "the ability to self-organize is highly dependent on the relative signs of the chemotactic mobilities... and on the global network structure."
- **Evidence pointer** Table 1, Figures 3-4 (referenced)
- **Concern** The analysis is restricted to closed unimolecular networks with uniform parameters (equal α, equal ρ₀, equal diffusion coefficients). Real biological networks are open, involve bimolecular reactions, and have heterogeneous parameters. The authors acknowledge this in the Discussion but do not provide any analysis of how their conclusions might change under more realistic conditions. The generality of the "network-wide effects" claim is therefore limited.
- **Why it matters** The title and abstract suggest a general phenomenon, but the quantitative results are for a very specific class of networks. Without at least a discussion of robustness to parameter heterogeneity or network openness, the conclusions may be overgeneralized.
- **Resolution test** Add a discussion of how the results might extend to non-uniform parameters, open systems, or bimolecular reactions. If possible, include a small number of test cases with non-uniform parameters to demonstrate robustness.

- **Minor Comments**
- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Eq. (9) and surrounding text
- **Evidence pointer** Results section, "Small wavevector expansion" subsection
- **Issue** The derivation of Eq. (9) is presented very tersely. The quasi-static approximation and the small wavevector expansion are mentioned but not shown in detail. The physical interpretation of the interaction matrix η is given, but the mathematical steps leading to its definition are not fully transparent.
- **Required correction** Expand the derivation, either in the main text or in a supplementary appendix, showing the key intermediate steps from Eq. (5) to Eq. (9). This will make the work more accessible and verifiable.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Table 1
- **Evidence pointer** Table 1
- **Issue** The table is dense and the notation (e.g., "self-attr.") is not defined in the caption. The relationship between the rows (mobility patterns) and the columns (linear vs. saturated kinetics) is clear, but the reader must infer the meaning of "self-attr." from the text.
- **Required correction** Define all abbreviations in the table caption and consider adding a brief explanatory sentence about how to read the table.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods section
- **Evidence pointer** "Generation of strongly connected reaction networks"
- **Issue** The method for generating all strongly connected digraphs is described, but the computational cost and any potential limitations (e.g., memory, time) are not mentioned. The number of graphs (1,052,145) is stated, but it is unclear how long the enumeration and subsequent eigenvalue calculations took.
- **Required correction** Add a brief note on computational resources and runtime, which would be useful for readers wishing to reproduce or extend the analysis.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Referencing
- **Affected element** References section
- **Evidence pointer** References list
- **Issue** Some references appear incomplete or inconsistently formatted (e.g., "Phillips et al. 2012" without full citation details in the reference list). The reference style is not consistent with a standard journal format.
- **Required correction** Ensure all references are complete and formatted consistently according to the target journal's style.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Language
- **Affected element** Discussion section
- **Evidence pointer** "It will be of particular interest to determine which kinds of pathway regulations are possible through phase separation in multi-enzyme systems, and how spontaneously-arising spatial structure affects metabolic output."
- **Issue** The phrase "spontaneously-arising" is awkward; "spontaneously arising" (without hyphen) is more standard.
- **Required correction** Minor language edit.

## Risk / unsupported claims
- The claim that "slightly over 1/2 of interaction networks are unstable for linear kinetics, compared to exactly 3/8 for saturated kinetics" is presented as a robust statistical result, but the precision of "exactly 3/8" for saturated kinetics is not explained. Is this an analytical result or a numerical coincidence? This should be clarified.
- The statement that "signaling molecules could take advantage of this scenario towards their functionality" is speculative and not supported by any specific analysis or example in the manuscript.
- The claim that the network-induced mechanism "can provide an alternate route towards self-organization" for the (0,+) mobility pattern is based on a small proportion of networks (2.167×10⁻⁴ for K≤6). The practical significance of such a rare occurrence is not discussed.
- The manuscript does not address the timescales over which the predicted instabilities would develop, nor does it discuss whether these timescales are biologically relevant. This is a significant gap in establishing the physical plausibility of the proposed mechanism.
- The assumption of equal diffusion coefficients for all chemicals and enzymes is a strong simplification that is not justified or discussed in terms of its potential impact on the results.