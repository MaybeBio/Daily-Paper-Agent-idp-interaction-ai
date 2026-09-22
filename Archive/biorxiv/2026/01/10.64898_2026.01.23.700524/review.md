## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, case studies, conclusion, supplementary methods) as provided
- **Assessment boundary** Scientific and technical evaluation of the described MAD server update, including the Polymer Builder, Molecule Builder enhancements, database expansion, and case study demonstrations
- **Shared manuscript claim summary** The authors report a major update to the MAD web server, adding a Polymer Builder for automated construction of Martini CG polymer models, enhancing the Molecule Builder with GōMartini 3 and water–protein interaction biases, expanding the database with new compounds including the Martini 3 lipidome, and improving interoperability through a REST API. Case studies demonstrate construction of polysaccharides, disordered proteins, synthetic copolymers, PEG-lipids, and protein complexes.
- **Visible evidence base** Abstract, Introduction, Material and Methods (Overall Organization, Polymer Editor, Database/API, Molecule Builder improvements), Case Studies (dextran, Sic1, PS-PMA copolymer, PEG-lipid, InhA, α-synuclein), Conclusion, Simulation methods, Data availability statement
- **Missing materials affecting confidence** Figures 1-5 referenced but not provided; Table 1 and Table 2 referenced but not provided; no quantitative validation data (e.g., comparison of generated structures to experimental or atomistic references); no performance benchmarks; no user testing data; no detailed error rates or failure statistics for the Polymer Builder

## Reviewer
- **Overall assessment** This manuscript describes a timely and potentially valuable update to a widely used web server in the Martini CG simulation community. The addition of a Polymer Builder and the integration of GōMartini 3 and Martini 3-IDP into the Molecule Builder address clear user needs. However, the manuscript as presented is largely descriptive, with case studies that are qualitative in nature. The absence of quantitative validation, performance metrics, or systematic benchmarking limits the strength of the claims. The scientific case for the update is plausible but not fully established from the provided evidence.
- **Who would be interested in the results, and why** Researchers using Martini CG simulations across biomolecular and soft matter fields, including those studying polymers, disordered proteins, lipid membranes, and protein complexes. The MAD server is a community resource, and updates that expand its capabilities will be of direct practical interest to a broad user base. Developers of similar CG modeling tools and web platforms may also find the architecture and API design informative.
- **Major strengths** The manuscript addresses a clear and growing need in the Martini community for automated polymer construction and more flexible protein modeling. The integration of multiple recent Martini 3 developments (GōMartini 3, Martini 3-IDP, lipidome) into a single platform is a significant practical contribution. The REST API and database expansion improve interoperability and accessibility. The case studies cover a diverse range of systems, demonstrating the breadth of the tools. The authors are transparent about current limitations and future directions.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (lack of quantitative validation), R1-M2 (missing figures and tables), R1-M3 (unsubstantiated claim of being the only tool with interactive Gō bond editing), R1-M4 (incomplete simulation validation details)
- **Assessment against Nature-style criteria** Originality: Moderate. The individual components (Polyply, GōMartini 3, Martini 3-IDP) are not new, but their integration into a unified web platform with a Polymer Builder is a novel contribution. Scientific importance: Moderate to high. The MAD server is a widely used resource, and this update has the potential to streamline workflows for many users. However, the importance is more practical than conceptual. Interdisciplinary readership: Moderate. The tools are relevant to biomolecular simulation, soft matter, and polymer physics communities, but the manuscript is likely to appeal primarily to Martini users. Technical soundness: Not fully assessable from the provided material. The qualitative case studies suggest the tools work, but quantitative validation is lacking. Readability for nonspecialists: The manuscript is generally well written and accessible, though some sections assume familiarity with CG simulation concepts.
- **Recommendation posture** Supportive if technical concerns are resolved. The described update is likely to be a useful contribution, but the manuscript needs quantitative validation and the missing figures and tables must be provided before the claims can be fully assessed.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The case studies demonstrate that the generated models are "stable and suitable for use in standard Martini 3 simulation workflows" and that the tools enable construction of diverse polymer and protein systems.
- **Evidence pointer** Case Studies section, Simulation methods section
- **Concern** The case studies are entirely qualitative. The authors state that short CG simulations confirmed stability, but no quantitative data are provided. There are no comparisons of generated structures to experimental data, atomistic reference simulations, or established benchmarks. For example, the dextran model is said to be consistent with previous work, but no quantitative comparison (e.g., radius of gyration, persistence length, scaling exponents) is shown. Similarly, the InhA and α-synuclein models are described but no metrics of structural fidelity or dynamic behavior are reported.
- **Why it matters** The central claim of the manuscript is that the updated MAD tools produce valid, simulation-ready models. Without quantitative validation, the reader cannot assess whether the tools produce reliable results. This is particularly important for the Polymer Builder, which is a new tool and may generate topologies with errors that are not obvious from visual inspection.
- **Resolution test** Provide quantitative validation for at least a subset of the case studies. This could include comparison of polymer dimensions (Rg, end-to-end distance) to experimental or atomistic data, structural metrics for proteins (RMSD to experimental structures, secondary structure content over time), and demonstration that the generated topologies are thermodynamically stable over production-length timescales. For the InhA example, a comparison of mutant versus wild-type dynamics would strengthen the case.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The manuscript references Figures 1-5 and Tables 1-2 to illustrate the architecture, interface, case study structures, and database contents.
- **Evidence pointer** Figures 1-5, Tables 1-2 (referenced but not provided)
- **Concern** The manuscript cannot be fully evaluated without the referenced figures and tables. Figure 1 (ecosystem architecture), Figure 2 (Polymer Editor interface), Figures 3-5 (case study structures and workflows), Table 1 (database statistics), and Table 2 (API parameters) are all essential to understanding the described functionality. Their absence prevents assessment of the user interface, the complexity of systems that can be built, and the scope of the database expansion.
- **Why it matters** The figures and tables are the primary evidence for the claimed functionality. Without them, the reader cannot verify that the tools work as described or assess the practical usability of the interface.
- **Resolution test** Provide all referenced figures and tables. Ensure that figures clearly show the interface, the graph-based editing workflow, and the resulting structures. Tables should include complete database statistics and API documentation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Claim substantiation
- **Claim pointer** "To our knowledge, MAD:Molecule Builder is currently the only coarse-graining tool that enables interactive editing of inter- or intra-chain Gō bonds."
- **Evidence pointer** Case Studies section, InhA example
- **Concern** This claim is difficult to verify and may be overstated. Other tools in the Martini ecosystem, such as martinize2 itself (which is used as the backend), may offer some degree of Gō bond customization, even if not through a graphical interface. The claim of uniqueness requires a more thorough literature and tool survey.
- **Why it matters** Overstated claims of uniqueness can undermine the credibility of the manuscript. The interactive editing capability is a useful feature, but the claim of being the "only" tool is not necessary to establish its value.
- **Resolution test** Either provide a comprehensive survey of existing tools that demonstrates the uniqueness of this feature, or soften the claim to something like "to our knowledge, no other web-based tool offers this level of interactive Gō bond editing."

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The simulation methods state that "short CG simulations confirmed that the resulting systems are stable" but provide limited details on simulation length, system composition, or analysis criteria.
- **Evidence pointer** Simulation methods section
- **Concern** The description of the validation simulations is insufficient. The authors do not specify the length of the simulations, the size of the systems, the number of replicas, or the specific criteria used to judge stability. Without these details, the claim of stability is not reproducible.
- **Why it matters** Reproducibility is a core requirement for scientific claims. The validation simulations are the only quantitative evidence presented, and they must be described in sufficient detail for others to replicate.
- **Resolution test** Provide a detailed description of the simulation setup, including system composition, simulation length, number of replicas, and the specific metrics used to assess stability (e.g., RMSD plateau, energy convergence, absence of structural distortion).

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that the server "has been updated with new tools, models, and capabilities" but does not mention the REST API, which is a significant new feature described in the main text.
- **Required correction** Consider adding a brief mention of the API in the abstract to accurately reflect the scope of the update.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Readability
- **Affected element** Introduction
- **Evidence pointer** Introduction
- **Issue** The introduction lists several existing tools (bentopy, martinize2, COBY, TS2CG, polyply) but does not clearly explain how MAD differs from or complements these tools beyond the general statement of providing a "comprehensive and evolving platform."
- **Required correction** Add a sentence or two that explicitly positions MAD relative to these tools, highlighting the unique combination of a web-based interface, database integration, and the new Polymer Builder.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical accuracy
- **Affected element** Polymer Editor section
- **Evidence pointer** Polymer Editor section
- **Issue** The text states that the Polymer Editor "represents polymer molecules as graphs" but does not explain how the graph representation handles stereochemistry, branching, or cross-linking, which are relevant for complex polymer architectures.
- **Required correction** Briefly clarify the scope and limitations of the graph representation, or refer to the Polyply documentation for details.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Data and Software Availability
- **Evidence pointer** Data and Software Availability section
- **Issue** The availability statement mentions a repository for case study data but does not specify a license for the MAD server code itself or for the deposited models.
- **Required correction** Add explicit license information for the software and data to facilitate reuse and compliance.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Case Studies section
- **Evidence pointer** Case Studies section, dextran example
- **Issue** The dextran example states that the model is "linear" but dextrans are known to have variable degrees of branching. The authors acknowledge this in the text but do not discuss how the Polymer Builder handles branched polysaccharides.
- **Required correction** Add a brief note on whether the Polymer Builder supports branched architectures and how this was handled in the dextran example.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Conclusion
- **Evidence pointer** Conclusion section
- **Issue** The conclusion mentions "future developments" including "automated topology-generation strategies" but does not provide a concrete timeline or roadmap.
- **Required correction** Consider adding a more specific outline of planned features or a link to a public roadmap to manage user expectations.

## Risk / unsupported claims
- The claim that MAD:Molecule Builder is "currently the only coarse-graining tool that enables interactive editing of inter- or intra-chain Gō bonds" is not substantiated by a comprehensive tool survey.
- The claim that the generated models are "stable and suitable for use in standard Martini 3 simulation workflows" is based on qualitative case studies without quantitative data.
- The claim that the Polymer Builder supports "varying architectures and complexities" is not fully demonstrated, as the case studies cover only a limited set of architectures (linear polysaccharide, linear protein, linear copolymer, branched PEG-lipid).
- The statement that the database has been "substantially enriched" is not quantified; the number of new entries beyond the previously reported 1,274 models is not specified.
- The claim that the API "facilitates integration with external tools and systems" is plausible but not demonstrated with any example integration.