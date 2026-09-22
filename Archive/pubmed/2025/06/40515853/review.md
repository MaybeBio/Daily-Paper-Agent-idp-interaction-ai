## Review setup
- **Input scope** Full manuscript text (abstract, introduction, main sections, discussion, conclusions) as provided
- **Assessment boundary** Conceptual/theoretical claims, literature synthesis, and proposed framework; no experimental data or novel computational results are presented
- **Shared manuscript claim summary** The authors propose that proteins exhibit a minimal form of "intelligence" defined through Integrated Information Theory (IIT), network theory, and allostery, characterized by information integration, memory-like behavior (hysteresis), and adaptive responses, with implications for biotechnology and medicine
- **Visible evidence base** Literature citations, qualitative descriptions of known protein systems (hemoglobin, kinesin, prions, PTMs, LLPS), a P-z cartography analysis of 1,420 proteins (referenced to prior work), and conceptual arguments
- **Missing materials affecting confidence** No quantitative Φ calculations for any protein; no new experimental or simulation data; no formal mathematical derivation linking IIT Φ to protein observables; no systematic comparison with alternative frameworks; figure content described but not fully assessable from text alone

## Reviewer
- **Overall assessment** This manuscript presents a provocative and ambitious conceptual synthesis, arguing that proteins can be considered minimally "intelligent" based on IIT-derived information integration, hysteresis, and core-periphery dynamics. The writing is engaging and the breadth of literature covered is impressive. However, the central thesis rests on analogical reasoning rather than demonstrated quantitative application. The key concept, Φ, is introduced but never computed or operationalized for any specific protein system. The manuscript oscillates between metaphorical and literal uses of "intelligence," and the authors themselves acknowledge this tension without resolving it. The scientific value lies primarily in framing questions and suggesting new research directions, but the case for a measurable "protein intelligence" is not established from the provided evidence.
- **Who would be interested in the results, and why** Researchers in protein biophysics, intrinsically disordered proteins, allostery, and systems biology may find the conceptual framework stimulating. Those working on protein engineering, drug design, and synthetic biology might be intrigued by the proposed design principles. Philosophers of biology and complexity scientists may engage with the theoretical arguments. However, the lack of quantitative application limits its immediate utility for experimentalists.
- **Major strengths** 1) Broad and current literature synthesis across IIT, network theory, allostery, IDPs, LLPS, and complex systems. 2) Clear articulation of a testable conceptual framework (core-periphery balance, hysteresis as memory). 3) Honest acknowledgment of limitations and anthropomorphic risks. 4) Thoughtful discussion of potential applications in biotechnology and medicine. 5) The P-z cartography analysis provides a concrete, if preliminary, network-based foundation.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (Φ not operationalized), R1-M2 (hysteresis evidence not critically evaluated), R1-M3 (intelligence definition circularity), R1-M4 (analogy to neural networks unsubstantiated)
- **Assessment against Nature-style criteria** **Originality**: High. The specific combination of IIT with protein biophysics is novel and thought-provoking. **Scientific importance**: Moderate to high if the framework can be operationalized; currently, it is a proposal rather than a demonstration. **Interdisciplinary readership**: Potentially broad, spanning physics, biology, and complexity science, but the lack of quantitative grounding may limit appeal to hard-nosed empiricists. **Technical soundness**: Weak in its current form. The central metric Φ is not computed, and the link between IIT axioms and protein behavior is asserted rather than derived. **Readability for nonspecialists**: Generally well-written and accessible, though some sections (IIT formalism) may be dense. The analogies are helpful.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript is a stimulating perspective piece, but it does not yet make a rigorous scientific case for "protein intelligence" as a measurable property. Major revisions are required to either (a) provide a concrete, quantitative example of Φ computation for a protein system, or (b) reframe the article explicitly as a speculative/position paper with clearly stated hypotheses for future testing.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / Operationalization
- **Claim pointer** "We define protein intelligence using IIT and focus on how proteins integrate information (in terms of the parameter Φ coming from IIT)"
- **Evidence pointer** Section "Integrated information theory (IIT) and proteins", Equations 1 and 2
- **Concern** The central parameter Φ is defined mathematically but never computed, estimated, or even qualitatively bounded for any protein system. The authors state that Φ "represents or quantifies the capacity of an 'intelligent' system to modify its structure" but provide no methodology for how one would calculate Φ for a protein, nor any example. The equations presented are generic IIT definitions, not adapted to protein-specific state spaces or dynamics.
- **Why it matters** The entire thesis rests on the applicability of Φ to proteins. Without a demonstration that Φ is computable, measurable, or even conceptually well-defined for a protein's conformational ensemble, the claim that proteins "integrate information" in the IIT sense remains an unverified analogy. A reader cannot assess whether the framework has any predictive or explanatory power.
- **Resolution test** Provide a worked example, even a simplified one, showing how Φ (or a protein-adapted version) would be computed for a specific protein (e.g., hemoglobin or a small allosteric enzyme). This could be a toy model, a computational estimate from MD simulations, or a clear protocol for experimental estimation. Alternatively, explicitly state that Φ is used only as a conceptual metaphor and provide a different, operationalizable metric.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality / Critical evaluation
- **Claim pointer** "The presence of a hysteresis loop is one of the most fundamental indicators of learning" and subsequent claims that proteins exhibit memory-like behavior
- **Evidence pointer** Section "Conformational memory and learning in proteins", examples of E. coli lactose permease and glucokinase
- **Concern** The manuscript cites examples of hysteresis and conformational memory but does not critically evaluate the strength of this evidence. For instance, the lactose permease example is described as a "lipid-induced conformational change" that persists, but the mechanistic basis and functional relevance of this persistence are not discussed. The leap from hysteresis (a physical phenomenon) to "learning" (a cognitive term) is made without addressing alternative explanations, such as slow relaxation kinetics that are not functionally adaptive.
- **Why it matters** The distinction between "memory" as a functional, information-bearing property and "memory" as a trivial consequence of slow conformational dynamics is crucial. If hysteresis is simply a kinetic artifact, then calling it "learning" is misleading and undermines the scientific credibility of the framework. The authors need to specify what would count as evidence for genuine information storage and retrieval, as opposed to non-equilibrium dynamics.
- **Resolution test** Provide a clear operational definition of "conformational memory" that distinguishes it from slow relaxation. Discuss specific criteria (e.g., reversibility, specificity, functional readout) and evaluate the cited examples against these criteria. If the evidence is currently insufficient, state this explicitly and propose experiments that could test the memory hypothesis.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Conceptual clarity / Definitional rigor
- **Claim pointer** "We have tried to redefine the traditionally metaphorical concept of 'intelligence' in biochemistry as a measurable property"
- **Evidence pointer** Abstract and Section "Defining intelligence in proteins"
- **Concern** The definition of "protein intelligence" risks circularity. The authors define intelligence as information integration (Φ) plus memory (hysteresis) plus adaptability, and then conclude that proteins are intelligent because they exhibit these properties. But the selection of these specific properties as constitutive of "intelligence" is not justified independently of the conclusion. Why these three properties and not others? The authors acknowledge that "intelligence" is a contested concept but do not engage with alternative definitions or justify their choice beyond asserting its utility.
- **Why it matters** If the definition is tailored to fit proteins, then the conclusion that proteins are "intelligent" is trivially true and scientifically uninteresting. The framework needs to either (a) derive the definition from a more fundamental theory (e.g., IIT's axioms) in a way that is not ad hoc, or (b) make falsifiable predictions that distinguish "intelligent" proteins from non-intelligent ones based on the proposed criteria.
- **Resolution test** Clearly state the necessary and sufficient conditions for "minimal intelligence" and show how they follow from IIT or another theory, rather than being chosen post hoc. Provide a hypothetical example of a protein that would NOT be considered intelligent under the proposed definition, to demonstrate that the concept has discriminative power.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance / Novelty of framework
- **Claim pointer** "compare protein behavior to other complex systems like ecosystems and neural networks" and "the parallels between neural networks and proteins highlight the universality of critical behavior in intelligent systems"
- **Evidence pointer** Section "Parallels with critical States in complex systems", subsections on ecosystems, gene regulatory networks, and neural networks
- **Concern** The analogies to ecosystems, GRNs, and neural networks are descriptive and do not add analytical depth. The claim that proteins operate at "criticality" is asserted but not supported by any quantitative analysis of protein energy landscapes or dynamics. The comparison to neural networks, in particular, is superficial: neural networks learn by modifying connection weights, whereas proteins change conformation. The mapping between these processes is not made explicit.
- **Why it matters** The manuscript claims to offer a "unified framework" but the unification is achieved through metaphor rather than mathematical or mechanistic equivalence. Without a formal mapping between the dynamics of proteins and those of neural networks or ecosystems, the claim of universality is unsupported. This weakens the scientific importance of the framework, as it does not provide new insights into either protein function or complex systems theory.
- **Resolution test** Either (a) provide a formal mathematical analogy (e.g., showing that protein conformational dynamics can be mapped onto a Hopfield network with defined energy minima and transition probabilities), or (b) soften the claims and present these parallels as heuristic inspiration rather than evidence for a unified framework.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity / Terminology
- **Affected element** Use of "intelligence" and "learning"
- **Evidence pointer** Throughout
- **Issue** The terms "intelligence," "learning," and "memory" are used in ways that oscillate between literal and metaphorical. This creates confusion about what exactly is being claimed.
- **Required correction** Add a glossary or explicit statement early in the manuscript defining the precise operational meaning of these terms as used in the protein context, and consistently use scare quotes or a qualifier (e.g., "minimal intelligence") throughout.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility / Data availability
- **Affected element** P-z cartography analysis (Figure 2)
- **Evidence pointer** Section "Core-periphery dynamics", Figure 2
- **Issue** The analysis of 1,420 proteins is referenced to a prior paper, but the specific methodology for generating the P-z plots (e.g., which interaction definitions, thresholds) is not described in this manuscript. The reader cannot assess the robustness of the claim of conserved network architecture.
- **Required correction** Briefly describe the methodology in the text or supplement, or clearly state that the figure is reproduced from prior work and provide the citation.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness / Alternative perspectives
- **Affected element** Discussion of criticisms of IIT
- **Evidence pointer** Section "Integrated information theory (IIT) and proteins"
- **Issue** The manuscript does not address significant criticisms of IIT, particularly regarding its measurement (the "unfolding" problem) and its philosophical assumptions. This omission weakens the credibility of using Φ as a foundation.
- **Required correction** Add a brief paragraph acknowledging key criticisms of IIT and explaining why the framework is still considered useful for the protein context, or why these criticisms are less relevant at the molecular scale.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Precision / Overstatement
- **Affected element** Claims about "super-intelligent" proteins
- **Evidence pointer** Section "What might constitute a hypothetical 'super-intelligent' protein?"
- **Issue** The thought experiment is interesting but the criteria listed (rich landscape, full reachability, balance of robustness and sensitivity) are vague and not tied to any measurable quantity. This section reads as speculative without clear connection to the proposed Φ-based framework.
- **Required correction** Either connect these criteria explicitly to Φ or other defined metrics, or clearly label this section as purely speculative and separate from the main framework.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability / Structure
- **Affected element** Section "Parallels with critical States in complex systems"
- **Evidence pointer** Subsections on ecosystems, GRNs, neural networks
- **Issue** These subsections are brief and read as a list of analogies rather than a coherent argument. The connection to protein intelligence is stated but not developed.
- **Required correction** Either expand each subsection to draw specific, testable parallels, or condense them into a single paragraph that makes the common principle explicit.

## Risk / unsupported claims
- The claim that proteins "integrate information" in the IIT sense is unsupported, as Φ is never computed or operationalized for any protein.
- The claim that hysteresis in proteins constitutes "learning" or "memory" is asserted without critical evaluation of alternative explanations (e.g., slow kinetics) or a clear operational definition.
- The claim that proteins operate at "criticality" is unsupported by any quantitative analysis.
- The claim of a "unified framework" connecting proteins, ecosystems, GRNs, and neural networks is based on analogy, not formal equivalence.
- The statement that "the presence of a hysteresis loop is one of the most fundamental indicators of learning" is presented as fact without citation or justification.
- The claim that "all proteins exhibit at least some degree of structural heterogeneity" is overly broad and not substantiated.
- The assertion that "PTMs represent a means of creating and maintaining conformational memory" is plausible but not demonstrated with specific evidence linking PTM dynamics to memory-like behavior in a quantitative way.