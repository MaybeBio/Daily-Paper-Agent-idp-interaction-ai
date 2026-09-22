## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no methods, figures, or quantitative results were available for evaluation
- **Shared manuscript claim summary** The authors use coarse-grained molecular dynamics simulations to study tau-microtubule interactions, reporting that distinct tau sub-regions contribute differentially to binding, that isoform variation modulates interactions via electrostatic tuning, and that Alzheimer's-associated phosphorylation weakens multivalent engagement.
- **Visible evidence base** Abstract text only; no simulation details, parameter sets, validation data, or quantitative outcomes were provided
- **Missing materials affecting confidence** Full manuscript, methods section, simulation parameters, force field details, validation against experimental data, all figures and tables, and any statistical analyses

## Reviewer
- **Overall assessment** The abstract presents a plausible and potentially interesting computational study of tau-microtubule interactions, addressing a relevant problem in neurodegeneration research. However, the claims as stated are broad and largely qualitative, and the absence of methodological detail and quantitative results prevents assessment of technical soundness or the strength of the evidence. The work may be of interest to the computational biophysics and tau biology communities, but the case is not established from the abstract alone.
- **Who would be interested in the results, and why** Computational biophysicists studying intrinsically disordered proteins and multivalent interactions would be interested in the methodological approach. Tau biologists and researchers in neurodegeneration would be interested in the mechanistic implications for tauopathy, particularly the phosphorylation effects. The electrostatic tuning mechanism may also appeal to those studying microtubule-associated protein regulation more broadly.
- **Major strengths** The topic is timely and relevant, addressing a long-standing challenge in characterizing tau-microtubule interactions. The multivalent, sub-regional perspective is a useful framing that could provide mechanistic insight beyond single-site binding models. The inclusion of isoform variation and disease-associated phosphorylation adds biological relevance.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract provides no information on simulation methodology, force field selection, system construction, sampling length, convergence criteria, or validation against experimental data. Without these, the technical soundness of the simulations cannot be evaluated. The absence of quantitative results means that claims about differential sub-region contributions, isoform effects, and phosphorylation effects are not supported by visible evidence.
- **Assessment against Nature-style criteria**  
  - Originality: The multivalent sub-regional perspective is not entirely new but the specific focus on heterogeneous association may offer a fresh angle. Cannot be fully assessed from the abstract.  
  - Scientific importance: Potentially high for tau biology and neurodegeneration, but the significance depends on whether the simulation findings are validated and quantitatively robust.  
  - Interdisciplinary readership: The topic bridges computational biophysics and neurobiology, which could attract a broad audience, but the abstract is written in a way that is accessible to specialists rather than a general scientific readership.  
  - Technical soundness: Not assessable from the abstract alone. No methodological details or validation are provided.  
  - Readability for nonspecialists: The abstract is reasonably clear but uses field-specific terminology without sufficient context for a general audience.
- **Recommendation posture** Currently not established from the provided evidence. The abstract describes a potentially valuable study, but the absence of methodological and quantitative detail means the claims cannot be evaluated. A supportive posture would require access to the full manuscript.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors claim that coarse-grained molecular dynamics simulations capture interactions with both the flexible C-terminal tails of tubulin and the structured tubulin surface.  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The abstract provides no information about the coarse-grained model used, including the resolution of the tau and tubulin representations, the force field parameters, or how the disordered C-terminal tails were modeled. Without this information, it is impossible to assess whether the simulations can faithfully capture the claimed interactions.  
- **Why it matters** Coarse-grained simulations are highly sensitive to model resolution and parameterization. If the model cannot accurately represent the electrostatic and steric properties of the tau-tubulin interface, the reported interactions may be artifacts of the model rather than biologically meaningful.  
- **Resolution test** Provide a detailed methods section describing the coarse-grained model, force field, system setup, and any benchmarking against experimental or atomistic data. Show that the model reproduces known tau-microtubule binding properties.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence strength  
- **Claim pointer** The authors claim that distinct tau sub-regions contribute differentially to binding and that isoform variation modulates interactions through electrostatic tuning.  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The abstract states these findings but provides no quantitative data, such as binding affinities, contact probabilities, or free energy estimates, to support the differential contributions. No comparison between isoforms is shown, and no statistical measures are reported.  
- **Why it matters** The central claims of the paper rest on differential sub-region behavior and isoform-specific modulation. Without quantitative evidence, these claims are unsupported and could be based on qualitative visual inspection of trajectories rather than robust analysis.  
- **Resolution test** Present quantitative metrics for sub-region binding contributions, such as per-residue contact frequencies or binding free energy decompositions, with appropriate error bars and statistical comparisons across isoforms.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence strength  
- **Claim pointer** The authors claim that Alzheimer's-associated phosphorylation disrupts tau-microtubule interactions by weakening multivalent engagement.  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The abstract does not specify which phosphorylation sites were modeled, how phosphorylation was represented in the coarse-grained model, or what quantitative changes in binding were observed. The claim that multivalent engagement is weakened is presented without supporting data.  
- **Why it matters** The phosphorylation claim is a key translational aspect of the study with implications for disease mechanisms. If the phosphorylation sites or their representation in the model are not justified, the biological relevance of the finding is questionable.  
- **Resolution test** Specify the phosphorylation sites modeled, justify their selection based on experimental evidence, describe how phosphorylation was incorporated into the model, and provide quantitative comparisons of binding metrics between phosphorylated and non-phosphorylated states.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Readability  
- **Affected element** Abstract text  
- **Evidence pointer** Abstract; location not provided  
- **Issue** The phrase "heterogeneous association" is used in the title and abstract but is not defined. It is unclear whether this refers to variability in binding modes, transient interactions, or something else.  
- **Required correction** Define "heterogeneous association" explicitly in the abstract or introduction to avoid ambiguity.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Abstract text  
- **Evidence pointer** Abstract; location not provided  
- **Issue** The statement that isoform variation influences "both MT stability and dimer polymerization rates" is made without specifying which isoforms were compared or how these outcomes were measured in the simulations.  
- **Required correction** Clarify which tau isoforms were studied and describe the simulation-based metrics used to assess MT stability and polymerization rates.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Context  
- **Affected element** Abstract text  
- **Evidence pointer** Abstract; location not provided  
- **Issue** The abstract does not mention any comparison with experimental data, which would help contextualize the simulation findings and establish their relevance.  
- **Required correction** Add a sentence in the abstract or results noting whether the simulation predictions align with known experimental observations of tau-microtubule binding.

## Risk / unsupported claims
- The claim that distinct tau sub-regions contribute differentially to binding is unsupported without quantitative data.
- The claim that isoform variation modulates MT stability and polymerization rates through electrostatic tuning is unsupported without specific isoform comparisons and quantitative outcomes.
- The claim that Alzheimer's-associated phosphorylation weakens multivalent engagement is unsupported without specification of phosphorylation sites and quantitative binding metrics.
- The overall mechanistic conclusions are not assessable from the abstract alone due to the absence of methodological detail and validation.