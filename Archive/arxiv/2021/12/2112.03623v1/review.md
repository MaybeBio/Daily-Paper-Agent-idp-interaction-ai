## Review setup
- **Input scope** Full manuscript text, including main text, methods, and appendices.
- **Assessment boundary** The scientific and technical validity of the proposed platform, the soundness of the simulation methodology, and the strength of the claims made relative to the presented evidence.
- **Shared manuscript claim summary** The authors propose a platform for single-molecule structure determination of proteins in situ, based on near-surface group-V donor qubits in silicon. They claim that through a combination of quantum control protocols (the Nuclear Spin Storage protocol) and the intrinsic properties of silicon donor qubits, atomic-level 3D imaging of molecular structure is achievable, as demonstrated by simulations of a transmembrane protein-lipid system.
- **Visible evidence base** The manuscript provides a theoretical framework, detailed descriptions of the proposed protocols, and results from numerical simulations. This includes tight-binding calculations of the donor wave function, simulations of the NSS protocol's behavior, and simulated image reconstructions of a model protein-lipid system.
- **Missing materials affecting confidence** The manuscript is a theoretical proposal. No experimental data is presented. The simulations, while detailed, rely on several key assumptions about the system's parameters (e.g., coherence times, decoupling efficiency, noise levels) that are not experimentally validated in this work. The computational methods for image reconstruction are described but the specific algorithms and their limitations are not fully detailed.

## Reviewer
- **Overall assessment** This manuscript presents a highly ambitious and creative theoretical proposal for a new approach to single-molecule structural biology. The core idea of using a silicon donor qubit as a nanoscale MRI probe is novel and leverages significant advances in quantum computing. The authors have developed a sophisticated theoretical framework, including a new protocol (NSS) to address the challenges of nanoscale frequency encoding. The simulations, while preliminary, suggest the concept is worthy of consideration. However, the work is entirely theoretical, and the path from these simulations to a working experimental platform is fraught with immense practical challenges that are not fully addressed. The claims of "atomic-level structure determination" are strong and are not fully supported by the evidence presented, which relies on idealized simulation conditions. The manuscript is well-written and the logic is clear, but the gap between the proposed concept and its demonstrated feasibility is the central concern.
- **Who would be interested in the results, and why** Researchers in quantum sensing and quantum information, particularly those working on silicon-based qubits, would be interested in the novel application of their technology. Structural biologists, especially those focused on membrane proteins and intrinsically disordered proteins, would be interested in the potential for a new imaging modality that could overcome the limitations of ensemble-averaging techniques. The work could also be of interest to the broader nanoscience community.
- **Major strengths**
    1.  The proposal is highly original, representing a significant conceptual leap in applying quantum sensing to structural biology.
    2.  The authors have provided a detailed and thoughtful theoretical treatment of the problem, including a novel protocol (NSS) to address the specific challenges of nanoscale MRI.
    3.  The use of a realistic and biologically relevant test system (M2 proton channel in a lipid bilayer) strengthens the potential impact of the proposal.
    4.  The consideration of practical issues, such as surface termination and optimal donor depth, shows a good understanding of the experimental constraints.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical Soundness
    - **Claim pointer** The manuscript claims that the platform enables "scalable atomic-level structure-determination of individual molecular systems in native environments."
    - **Evidence pointer** Section II.6, Appendices I-M.
    - **Concern** The central claim of atomic-level structure determination is based on simulations that appear to be highly idealized. The simulated imaging of the M2 channel shows average deviations of 0.36 Å and 1.3 Å for the sectional and extended modes, respectively. However, these simulations do not appear to account for several critical sources of experimental error and noise. For example, the impact of imperfect qubit initialization, readout, and control pulse errors on the final image quality is not systematically analyzed. The manuscript mentions robustness to "shot noise" but does not address other, potentially more significant, sources of error such as magnetic field inhomogeneities, temperature fluctuations, or the precise positioning of the molecule relative to the qubit. The claim of "atomic-level" resolution is therefore not convincingly established from the provided evidence.
    - **Why it matters** The entire premise of the paper rests on the ability to achieve atomic resolution. If the technique is only capable of lower resolution under realistic conditions, its value proposition for structural biology is significantly diminished. The simulations need to be far more comprehensive and include realistic noise models to support the central claim.
    - **Resolution test** The authors should provide a detailed error budget for the proposed imaging protocol, including the effects of decoherence, control pulse imperfections, and magnetic field noise on the final reconstructed image. The simulations should be repeated with these realistic noise sources included to demonstrate that atomic-level resolution is still achievable.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical Soundness
    - **Claim pointer** The manuscript states that the NSS protocol "successfully embeds dynamical dipole-dipole decoupling (such as CORY-24 sequence) into the gradient magnetic field produced by the donor wave function" and that this allows for "careful sampling and extraction of structural information."
    - **Evidence pointer** Section II.3, Appendix D.
    - **Concern** The NSS protocol is the core enabling technology, but its description and validation are insufficient. The manuscript provides a high-level description and some simulation results, but the details of the protocol's implementation are not fully specified. For instance, the exact sequence of pulses, the timing parameters, and the method for achieving phase-matched interleaving are not described with enough precision to be reproduced. More critically, the simulations in Appendix D appear to be for a small, idealized cluster of spins. The scalability of the protocol to a realistic protein with hundreds or thousands of coupled nuclear spins is not demonstrated. The computational cost and the complexity of the control sequence for a real system are not addressed.
    - **Why it matters** A protocol that works in a simplified model may not be feasible for a real biological sample. The complexity of the control sequence and the computational resources required to design and implement it for a large spin system could be prohibitive. Without a clear demonstration of scalability, the practical utility of the NSS protocol is questionable.
    - **Resolution test** The authors should provide a more detailed and quantitative description of the NSS protocol. They should also present simulations that demonstrate the protocol's performance on a larger, more realistic spin system, including an analysis of the computational resources required to generate the control sequences.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific Importance
    - **Claim pointer** The manuscript claims that the proposed platform "could have far-reaching consequences for the understanding of membrane biology and drug development."
    - **Evidence pointer** Section I, Section III.
    - **Concern** While the potential impact is clear, the manuscript does not adequately address the significant practical challenges that stand between the theoretical proposal and a working experimental system. The most critical is the sensitivity of the technique. The signal from a single nuclear spin is extremely weak, and the proposed detection scheme relies on the qubit's ability to sense this signal. The manuscript does not provide a detailed analysis of the expected signal-to-noise ratio for a realistic experimental setup, considering factors such as the qubit's sensitivity, the measurement efficiency, and the required integration time. The challenge of preparing a biological sample on a silicon chip in a way that is compatible with the technique (e.g., maintaining the protein's native state in vitrified ice) is also not discussed in detail.
    - **Why it matters** The proposal is only scientifically important if it is experimentally feasible. If the sensitivity is too low or the sample preparation is too challenging, the platform will not be able to deliver on its promise. The authors need to provide a more realistic assessment of the experimental hurdles and how they might be overcome.
    - **Resolution test** The authors should provide a quantitative estimate of the expected signal-to-noise ratio for a realistic experimental implementation, including a discussion of the required integration times and the challenges of sample preparation. They should also discuss potential strategies for overcoming these challenges.

- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Readability for Nonspecialists
    - **Affected element** Section II.2, Figure 2
    - **Evidence pointer** Section II.2
    - **Issue** The description of the dipole field and its control is dense and may be difficult for a reader who is not an expert in magnetic resonance or quantum control to follow. The concept of "dipolar slices" and the use of parameters like θ and φ could be explained more intuitively.
    - **Required correction** Consider adding a more accessible explanation of the imaging concept, perhaps with a schematic that illustrates how the dipole field creates distinct spatial "slices" and how these are sampled.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Appendix F
    - **Evidence pointer** Appendix F
    - **Issue** The analysis of the optimal donor depth is based on the assumption that the surface is hydrogen-terminated. The authors note that oxide termination would lead to reductions in the sensing volume, but they do not quantify this effect or discuss the relative merits of different surface terminations in more detail.
    - **Required correction** A brief quantitative comparison of the sensing volume and gradient strength for different surface terminations would be helpful.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Section II.6, Appendix M
    - **Evidence pointer** Appendix M
    - **Concern** The simulated imaging of the entire protein-lipid system is performed on the nitrogen sub-density, which is relatively sparse. The authors state that imaging higher-density sub-structures (H, C) would require greater numerical resources. It would be useful to know if the technique is fundamentally limited in its ability to image dense structures, or if this is just a computational limitation.
    - **Required correction** A brief discussion of the potential challenges and limitations of imaging high-density structures would be valuable.

- **Technical failings that need to be addressed before the case is established**
    - R1-M1: The lack of a comprehensive error budget and realistic noise models in the simulations undermines the central claim of atomic-level resolution.
    - R1-M2: The NSS protocol is not described in sufficient detail to be reproduced, and its scalability to realistic, large spin systems is not demonstrated.

## Risk / unsupported claims
- The claim of "scalable atomic-level structure-determination" is not supported by the evidence, as the simulations are idealized and do not account for realistic experimental imperfections.
- The claim that the NSS protocol "successfully embeds" decoupling and enables "careful sampling" is not fully supported, as the protocol's implementation and scalability are not adequately detailed.
- The assertion that the platform is "particularly well suited to the high-value lipid-membrane context" is plausible but not quantitatively supported by the simulations, which do not model the complexities of a realistic lipid bilayer environment.
- The estimated imaging times (2-6 hours) are presented as a positive feature, but the assumptions behind these estimates (e.g., coherence times, measurement rates) are not critically examined.