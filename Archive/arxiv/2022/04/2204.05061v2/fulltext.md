## Surfactancy in a tadpole model of proteins

We model the environment of eukaryotic nuclei by representing macromolecules by only their entropic properties, with globular molecules represented by spherical colloids and flexible molecules by polymers. We put particular focus on proteins with both globular and intrinsically disordered regions, which we represent with ‘tadpole’ constructed by grafting single polymers and colloids together. In Monte Carlo simulations we find these tadpoles support phase separation via depletion flocculation, and demonstrate several surfactant behaviours, including being found preferentially at interfaces and forming micelles in single phase solution. Furthermore, the model parameters can be tuned to give a tadpole a preference for either bulk phase. However, we find entropy too weak to drive these behaviours by itself at likely biological concentrations.


## 1 Introduction

Liquid-liquid phase separation (LLPS) has been identified as a mechanism for eukaryotic cells to organise their constituent biomolecules without needing the lipid bilayer membranes used by conventional organelles [ 1 , 2 , 3 ] . The resulting droplets are sometimes called ‘membraneless organelles’ [ 4 ] . The best and longest known example of these is the nucleolus, which is involved in the production of ribosomes [ 5 ] , but more recent work has identified a variety of similar - albeit smaller - liquid aggregates inside both the nucleus and the cell cytoplasm [ 4 ] . Their locations, functions and compositions vary, but they frequently feature proteins with long sections of polypeptide chain that remain flexible instead of folding into rigid secondary and tertiary structures [ 3 , 6 , 7 , 8 ] . These sections are called intrinsically disordered regions (IDRs) and can be found anywhere along the polypeptide chain. In this article we will model IDRs at either the carboxy terminal domain (CTD) or amino terminal domain, leading to proteins with a flexible chain attached to a single globular region.

The role of these IDRs in LLPS remains uncertain, with most work to date focusing on weak attractive interactions between IDRs, especially those between charge dipoles, aromatic groups and net charges in amino acid residues [ 9 ] . The idea being that having longer IDRs provides more weak interactions with which to hold the droplet together.

These energetic considerations are not alone in driving phase behaviour, however, as entropy also plays a role. This has several contributions: entropy of mixing drives systems to mix, and thus hinders LLPS; conformational entropy of IDRs multiplies the number of microstates utilising the chemistry above [ 10 ] ; and even without chemistry the conformational entropy introduces crowding effects that give IDRs an effective repulsion from globular molecules. Crowding effects, which are the focus of this work, are not new to cell biology. Studies have included the organisation of DNA at different length scales [ 11 , 12 , 13 , 14 , 15 ] , the influence of crowding on transcription rates [ 16 ] and on LLPS [ 11 , 17 , 18 , 19 , 20 ] . However, to our knowledge purely replusive models of proteins with both IDRs and globular regions have not yet been studied.

Physics can provide insights into such systems by drawing analogy to polymer-colloid systems, which are characterised by the ratio of polymer radius of gyration and colloid radius q = R g / R col q=R_{g}/R_{\mathrm{col}} . Behaviour in the ‘colloid limit’, q ≪ 1 q\ll 1 , is very well established, with mixtures of non-adsorbing polymers and colloids separating via depletion flocculation [ 21 , 22 , 23 ] . The story in the ‘protein limit’, q > 1 q>1 , is similar, but with the key difference that phase separation is less sensitive to R g R_{g} than the correlation length of the polymer mesh [ 24 ] . Recent work has argued similar mechanisms can play a role in biology where it can separate nuclear transport receptors in nuclear pores [ 25 ] .

Interesting behaviour also arises when the polymers are grafted to proteins. In the colloid limit, it is common practice to coat the colloids with polymers, stabilising them against the van der Waals forces driving flocculation by exploiting the entropic repulsion of the polymers [ 26 ] . In the protein limit, polymer-colloid grafts are often called grafted nanoparticles (GNPs), and have been studied extensively in the last two decades [ 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 ] . This work has focused largely on materials science, usually aiming to improve the properties of nanocomposites [ 32 ] or using specific interactions of the GNPs in the design of materials [ 33 ] . Research into GNPs with only one grafted polymer - an appropriate analogue to proteins with a single IDR - has been comparatively sparse [ 27 , 28 , 29 , 33 ] .

Similarly to the biological LLPS literature, we are unaware of any work that has sought to quantify the importance of entropy in GNP behaviour. Hence, by modeling proteins with IDRs as single-chain GNPs with no attractive interactions, this article simultaneously fills gaps in both fields.

Finally, we recognise solvent entropy can also play a role via hydration effects and has been shown to be important in protein aggregation, even for proteins without IDRs [ 35 , 36 , 37 , 38 , 39 ] . In this work we only consider explicitly the entropic properties of the macromolecules, with solvent entropy folded into net local solute interactions which we assume to be fully repulsive.


## 2 Methods

To study the role of IDRs’ entropy in LLPS, we run dynamic Monte Carlo simulations in continuous, 3-dimensional, periodic boxes. The box dimensions are L x × L y × L z L_{x}\times L_{y}\times L_{z} , where we always set L x = L y L_{x}=L_{y} and take L z L_{z} as the box’s longest dimension. These dimensions will vary between sections, where they are stated.

We coarse grain macromolecules into collections of spheres where the i i th particle has hard core radius R i R_{i} . Since we focus solely on their entropic properties, these particles experience no attractions and repel each other with the hard sphere potential

when particles i i and j j are distance r i ​ j r_{ij} apart.

Spherical particles are joined together into the 3 molecule species depicted in Fig. 1 . Colloids are single large beads with radius R col R_{\mathrm{col}} representing low-entropy (globular) macromolecules. Polymers are flexible, linear chains of N mono N_{\mathrm{mono}} small beads, each with radius R mono R_{\mathrm{mono}} , that represent molecules with high conformational entropy. Finally, ‘tadpoles’ represent IDR-containing proteins with a globular region attached to a single IDR. These two regions are represented by a large ‘head’ bead with radius R head R_{\mathrm{head}} , and a ‘tail’ chain of N tail N_{\mathrm{tail}} small beads with radii R tail R_{\mathrm{tail}} . To reduce the number of parameters in this work, we set R head = R col R_{\mathrm{head}}=R_{\mathrm{col}} and R tail = R mono R_{\mathrm{tail}}=R_{\mathrm{mono}} , so a tadpole can be viewed as a colloid grafted to a polymer when N tail = N mono N_{\mathrm{tail}}=N_{\mathrm{mono}} . This helps minimise the number of parameters used in this work, but limits our ability to make quantitative comparisons to experiments.

All intra-molecular bonds are enforced with the hard square well potential

which acts alongside U HS U_{\mathrm{HS}} .

These molecules are placed in an implicit solvent and do not experience any hydrodynamic effects beyond their diffusivity being set by the usual Stokes-Einstein expression D i = k B ​ T / ( 6 ​ π ​ η ​ R i ) D_{i}=k_{\mathrm{B}}T/(6\pi\eta R_{i}) . Rather than specify the viscosity η \eta explicitly, we define the time unit by the time taken for small particles to diffuse their own size, as listed in Table 1 . Similarly, we use the thermal energy k B ​ T k_{\mathrm{B}}T as our energy unit.

This diffusivity is achieved by displacing particles with the noise term used in the Brownian dynamics algorithm [ 40 ] ,

where W is a Gaussian-distributed random vector with zero mean and unit variance in all 3 directions. The conservative interactions are implemented with a Metropolis acceptance test, passing with probability

With our hard systems, this means only accepting displacements if the particle’s final energy is zero. To maintain a high acceptance rate in this hard environment we set the time increment δ ​ t \delta t such that 2 ​ D i ​ δ ​ t < R tail \sqrt{2D_{i}\,\delta t}<R_{\mathrm{tail}} .

The values of parameters used in this work are listed in Table 1 . Our choices for particle sizes lead to q ≈ 2.3 q\approx 2.3 when N tail = 30 N_{\mathrm{tail}}=30 , which approximates the ratio for human RNA polymerase II’s globular region and the flexible CTD on its largest subunit [ 41 , 7 ] .

Our criterion for equilibration is described in Appendix A . Except where otherwise stated, our quantitative results average over the last 10 system configurations in each simulation, each separated in time by at least 3 × 10 4 ​ τ 3\times 10^{4}\tau to allow for local re-equilibration. We then further averaged over at least 7 independent simulation runs for each system, giving us a minimum of 70 configurations contributing to each data point.


## 3 Entropic phase separation

Before showing the results of these simulations, it is helpful to explain the physics driving phase behaviour in our minimal model. By only considering hard interactions, all allowed states have the same energy and the temperature does not affect equilibrium states (although it does still play a role in dynamics). Free energy differences can therefore be written only in terms of the entropy:

Here we have split the entropy of mixing ( S m S_{m} ) and conformational entropy ( S c S_{c} ), characterising arrangements of molecule centres of mass and intra-molecule arrangements respectively.

This split is relevant for crowding effects where flexible chains are obstructed by nearby rigid bodies, reducing the number of available conformations of the chain, and in turn leading to a significant reduction in S c S_{c} . The archetypal system for this is a mixture of colloids and polymers, in which the two species can phase separate via depletion flocculation, where the dominance of S c S_{c} over S m S_{m} drives the colloids to cluster to minimise the contact of the two species, thus allowing the polymers to adopt the maximum number of conformations [ 21 ] .

The expectation is that this remains significant in our systems with tadpoles present, and hence that proteins may have evolved IDRs to exploit it.


## 4 Results


## 4.1 Qualitative phase behaviour

We first confirm depletion flocculation occurs in our simulations by simulating systems with only polymers and colloids present. For this we used highly stretched periodic boxes, with dimensions 4 × 4 × 27 4\times 4\times 27 , that produce well-defined planar interfaces perpendicular to the z z -axis, and whose widths are much smaller than the bulk phases. The transverse dimensions of the box are large enough to prevent molecules interacting with their own periodic images, but are quite small to keep the computational cost of simulations manageable. Such systems are shown in Fig. 2 , in which the denser system in part (a) shows a clear separation into polymer- and colloid-rich phases, as expected. The interfaces between these phases are also predictably close to planar and perpendicular to the box’s long axis.

Reducing the system density allows for a greater concentration of the minority component in each phase, which is particularly noticeable by the number of colloids in the polymer-rich phase in Fig. 2 (b). Reducing the densities further ultimately reaches fully mixed states, and this will be analysed more quantitatively in Sec. 4.2 .

Next, we add tadpoles to our systems, utilising the properties of our model molecules to make the replacement polymer + colloid → \rightarrow tadpole. In this way the total number of large particles (colloids and tadpole heads) is kept constant, as is the number of small particles (in polymers and tadpole tails). This process can be viewed as the addition of N tad N_{\mathrm{tad}} bonds fusing polymers to colloids. Starting from the systems in Fig. 2 , the concentrations are high enough that nonlinear terms in the osmotic pressure dominate, so the osmotic pressure is close to constant in each series of systems thus created, despite the number of molecules being reduced by N tad N_{\mathrm{tad}} from the initial polymer + colloid system.

Snapshots from such a series of simulations starting from Fig. 2 (a) are shown in Fig. 3 . Part (a) demonstrates that adding a small number of tadpoles this way has minimal impact on the volumes of the two bulk phases, and that of the two they prefer the polymer-rich phase. Fig. 4 (a), which averages volume fractions in systems that have fused together 47 tadpoles, quantitatively shows the tadpole density drops to almost zero in the colloid-rich phase.

Furthermore, in Fig. 3 (a) there appears to be a higher density of tadpoles at the interfaces than in the bulk. This would make intuitive sense as their heads and tails each prefer different phases when not bonded together, and hence one might expect tadpoles to want to straddle the interface to satisfy the preference of both their head and tail. This surfactant-like behaviour is confirmed quantitatively in Fig. 4 (a). Here, the tadpole density peaks at the interfaces, and close inspection finds the tadpoles tend to orient themselves so their heads and tails reside in the colloid and polymer phases respectively, as seen by the peaks of the head density being closer to the colloid phase than the corresponding peaks in tail density.

When half of the polymers have been fused into tadpoles, shown in Fig. 3 (b), the two phases remain separated but the polymer-rich phase expands to accommodate the additional volume of the tadpole heads. The interfaces have become more jagged, suggesting a reduction in interface tension (a point we will return to in Sec. 4.4 ), which is expected if the tadpoles are acting as surfactants. The tadpoles do not perfectly line the interfaces, however, which is indicative of the limited strength of the entropic ‘forces’ holding them there.

Adding yet more tadpoles, ultimately to the complete removal of polymers, yields the microphase separation seen Fig. 3 (c). In this case we find bicontinuous phases of tadpole tails and tadpole heads + colloids. By changing species concentrations, we can coax the tadpoles into forming micelles. Snapshots of these in shorter simulation boxes, 4 × 4 × 8 4\times 4\times 8 , are shown in Fig. 5 . In part (a), colloid density has been increased from the bicontinous phase, producing a cylindrical micelle with tadpole tails inwards, and whose axis is along the x x -axis (front-to-back). For part (b), replacing colloids with polymers inverts the micelle so that the tadpole tails now point outwards, leaving a rod-like cluster of heads at its centre. These microphases are commonly produced by surfactant molecules [ 42 ] , adding further evidence that tadpoles act as entropic surfactants.


## 4.2 Phase diagrams

We have constructed a phase diagram for our model in Fig. 6 , using species volume fractions ϕ \phi as axes. For the volume of each species, we sum the volumes of individual particles within them, multiplied by the number of those molecules present. Since the polymer pervaded volume is more important than its bare volume fraction for phase behaviour, its volume fraction is shown on different scale from the colloid to improve the clarity of results; similar applies for the tadpoles. Note this shears the contours in our ternary plot, which are shown in Fig. 6 (a). Also, because our systems are compressible with varying total volume occupied by our particles, the implicit solvent needs including as its own component, hence including the solvent volume fraction ϕ s = 1 − ϕ col − ϕ tad − ϕ poly \phi_{\mathrm{s}}=1-\phi_{\mathrm{col}}-\phi_{\mathrm{tad}}-\phi_{\mathrm{poly}} .

Our primary motivation is to determine where these systems undergo macrophase separation, as is believed to happen inside the cell nucleus and cytoplasm. To that end, we have run several series of simulations as per the previous section, from which we map the binodal volume from the tie lines of macrophase-separating states. The end points of these tie lines were found by measuring the volume fractions in each bulk phase, and averaging this over our independent simulations. We can then compare this to the range of biologically relevant concentrations [ 43 ] , shown as the shaded volume calculated using the Statistical Associating Fluid Theory (SAFT) formalism detailed in Appendix B [ 44 , 45 , 46 , 47 ] . We use this formalism as a way to estimate the contribution of bonded chains in the pressure, which is difficult to measure in our hard systems, making it challenging to compare pressures directly. However, SAFT differs from our model in that it fixes bond lengths to exactly R i + R j R_{i}+R_{j} , and we found it over-predicts the number of our polymers required for a given pressure, as evidenced by the slightly different gradients of our tie lines and the shaded region’s lower edge in Fig. 6 (a). However, this will not alter our conclusions.

It is again helpful to focus first on the colloid + polymer systems with no tadpoles present. This face of the phase diagram is shown in Fig. 6 (a), in which the blue and red data respectively encompass the two systems shown in Fig. 2 . This demonstrates quantitatively that as the density decreases (towards ϕ s = 1 \phi_{\mathrm{s}}=1 ), the number of colloids found in the polymer-rich phase increases, although the density of polymers found in the colloid-rich phase remains small until the systems are a low enough density to mix. Since such systems are nothing new [ 23 ] , our main interest is in its overlap of its binodal and the shaded biological concentrations. While there is indeed some overlap, we caution that it is confined to the high concentration (low ϕ s \phi_{\mathrm{s}} ) edge, and note that the author of Ref. [ 43 ] believed the lower osmotic pressures to be the most accurate. We are therefore mindful that the overlap we see may only exist due to inaccurate measurements extending the shaded region further than it should.

Whether that is the case or not, we infer from the limited overlap that entropy is unlikely to be strong enough by itself to drive biological phase separation. Nevertheless, it is strong enough that we believe it should not be neglected as a contributing factor, especially as it is independent of chemistry and thus part of the interaction in all systems.

Fig. 6 (b) shows the phase diagram produced when we add tadpoles as per Sec. 4.1 . The higher density series of systems (in blue) includes those shown in Fig. 3 and extends out from the blue data in Fig. 6 (a). A second, lower density series likewise extends out from the red data. This viewpoint is useful for visualising how these series ‘grow’ the binodal out from the colloid + polymer diagram, ultimately closing when enough tadpoles are added in this way. Further viewpoints are provided in the Supplementary Material to help picture this phase diagram in 3D space.

The best viewpoint for seeing how quickly the binodal closes upon addition of tadpoles is shown in Fig. 6 (c), where the tadpole volume fraction increases rightwards away from the colloid-polymer plane (now found at the left edge). Here we see both series of simulations map out planes in the binodal that are viewed nearly edge-on and that run close to parallel to the lower boundary of the shaded volume. Interpolating the binodal between our series shows us that adding tadpoles decreases the overlap with the shaded volume. Hence, the addition of tadpoles does not help entropy drive phase separation, as compared to the polymer + colloid case. It therefore requires some inter-molecular attraction to account for biological phase separation.

Finally, we note that the micelle-producing systems in Fig. 5 were significantly more dense than biological systems (see the green triangles near the base of Fig. 6 (c)). So while this is important behaviour for characterising the general properties of our tadpoles, we do not expect it to have much biological relevance.


## 4.3 Differences when N tail = 15 N_{\mathrm{tail}}=15

We now investigate what changes when reduce the length of our tadpole tails from 30 to 15 beads, which would biologically represent shorter IDRs, e.g. the shorter CTDs of RNA Polymerase II in yeast as compared to the human variant [ 7 ] . We keep the length of polymers unchanged, to represent an otherwise unchanged environment. Consequently, the replacement of colloids and polymers for an equal number of tadpoles no longer keeps the total number of beads fixed, and nor does the osmotic pressure remain approximately constant.

The phase diagram for these shorter tails is shown in Fig. 6 (d). In this we show data series starting from the same two colloid + polymer systems as before, and again more viewpoints are provided in the Supplementary Material. We kept the same axes as in the N tail = 30 N_{\mathrm{tail}}=30 phase diagram to aid in their comparison, but due to the shorter tails, more tadpoles are required to create the same pressure. This is why the shaded volume now extends down to a larger value on the ϕ tad \phi_{\mathrm{tad}} axis. Our procedure for adding tadpoles now also increases ϕ s \phi_{\mathrm{s}} , leading to the data series rising as tadpoles are added. So, where the tie lines and the base of the shaded volume were nearly co-planar with N tail = 30 N_{\mathrm{tail}}=30 , they now pass through each other. On its own, this would help bring the binodal into the shaded volume.

However, we also find that the binodal now closes at a lower tadpole density for both data series. This shrinking of the binodal is the larger effect of the two, resulting in an overall reduction in the capacity for tadpoles with shorter tails to support phase separation, as would be expected from their smaller conformational entropy. We acknowledge, however, that longer tails also provide more interactions sites when chemistry is accounted for, such that analogous differences in experiments cannot easily be attributed solely to differences in entropy.

Another major change with shorter tails is their shifting preferences for bulk phases. Where the N tail = 30 N_{\mathrm{tail}}=30 tadpoles had a strong preference for the polymer-rich phase, Fig. 4 (b) shows the concentration of tadpoles with N tail = 15 N_{\mathrm{tail}}=15 is approximately equal in both bulk phases. Tail length can therefore be utilised to tune a macromolecule’s preference for the separating phases. It also has the advantage of being biologically accessible through mutations that repeat polypeptide sequences, as is thought to have happened with the CTD of RNA Polymerase II, without changing chemical interactions in the process.


## 4.4 Interfacial tensions

We now seek to quantitatively confirm that the interfacial tension γ \gamma in our systems decreases with the addition of tadpoles. γ \gamma is difficult to access with hard potentials due to having infinitely poor statistics of the infinite forces present, so for this section we soften our system by using the Weeks-Chandler-Anderson (WCA) potential for particle repulsion,

where s = r / R W s=r/R_{\textrm{W}} scales the particle separation, r r , by the length scale of the WCA potential, R W R_{\textrm{W}} . Bond potentials are also softened by using finitely extensible non-linear elastic (FENE) bonds with energy

The new parameters were set to u W = k B ​ T = ε u_{\textrm{W}}=k_{\mathrm{B}}T=\varepsilon , R W = R i + R j R_{\textrm{W}}=R_{i}+R_{j} , R F = R i + R j + 4 ​ R tail R_{\textrm{F}}=R_{i}+R_{j}+4R_{\mathrm{tail}} between particles of species i i and j j . To match mean bond lengths to the hard systems, we set k F = 7.822 ​ ε / ℓ 2 k_{\textrm{F}}=7.822\varepsilon/\ell^{2} between pairs of tail/polymer beads, and k F = 2.558 ​ ε / ℓ 2 k_{\textrm{F}}=2.558\varepsilon/\ell^{2} between tadpole heads and tails.

With these potentials we have well-defined forces that can be calculated from system configurations. This in turn lets us calculate the stress tensor 𝝈 \bm{\sigma} and hence γ \gamma via the Kirkwood-Buff expression [ 48 ]

where having 2 interfaces in the system contributes the front factor of 1/2.

Finally, we change the box dimensions to 6 × 6 × 12 6\times 6\times 12 , which preserves the volume and hence particle numbers, but increases the ratio of interface area to bulk volume, improving our statistics. In these shorted boxes we ran 3 sets of simulations equivalent to those in the higher density series in Sec. 4.1 fusing colloids and polymers into tadpoles with N tail = 30 N_{\mathrm{tail}}=30 . To improve our statistics we ran these for longer to generate 200 independent snapshots, and in which we measured the interfacial tensions in Table 2 . These show a clear reduction in γ \gamma with the addition of tadpoles, as expected if they act as surfactants. These absolute values are in line with the commonly used estimate γ ≈ k B ​ T / δ 2 \gamma\approx k_{\mathrm{B}}T/\delta^{2} , with δ \delta being the interface width. We can also compare to the experimental values of 1 to 5 ​ μ ​ Nm − 1 5\mu\mathrm{Nm}^{-1} measured by Jawerth et al. [ 49 ] , which overlaps with our range when we convert our units to SI, as shown in the fourth column of Table 2 .


## 5 Conclusions

We have used minimal, equilibrium Monte Carlo simulations of hard sphere systems to investigate the role of entropy in biological liquid-liquid phase separation. By constructing phase diagrams for solutions of polymers, colloids and tadpole molecules representing biomolecules with different entropic properties, we were able to compare the concentrations at which such systems are unstable to macrophase separation with concentrations found in real cell nuclei. In doing so, we found entropy to be able to drive phase separation only at the upper estimates of biological concentrations. We conclude that the entropy from macromolecules is a significant contribution, but insufficient without some further attractions.

An important agenda for further work would be to assess the source, strength and impact of attractive macromolecular interactions, and whether that leaves them weak enough for IDRs to remain flexible. Within the implicit solvent paradigm, this requires intermolecular interactions net of solvent effects, and the balance of exposed hydrophobic vs hydrophilic residues is a possible starting point. Beyond this there are explicit solvent effects to be considered, including solvent entropy. The latter has been argued to be a significant driver of some LLPS, though its relevance where the solvent is not excluded from one phase is unclear [ 50 , 51 , 6 ] .

Our simulations with tadpoles identified these molecules as entropic surfactants, exhibiting several typical surfactant behaviours: microphase separations such as micelles and bicontinuous phases; a preference for interfaces; and a reduction in interfacial tensions as tadpoles are added. If such behaviour is present in vivo , it would be a major step forwards in understanding the biological importance of IDRs and their influence on liquid drop formation and structure. Indeed, if they exhibit strong segregation to the liquid drop interface, then the structure of ‘membraneless organelles’ might be closer to that of regular organelles than was previously realised.

Another avenue for further work could be to model IDR-containing proteins with different morphologies, such as a “pearl necklace” model for IDRs connected to globular regions at both ends. We speculate that pearl necklace molecules would make less effective surfactants since both ends have low conformational entropy and would prefer the colloid-rich phase. However, this will be sensitive to the length of the IDR, which could tune the preference for the two phases and the interface like the length our tadpoles’ tails does.

Finally, in this article we simplified our model by matching particle sizes. There remains the task of exploring parameter space where particle sizes are not matched, which will be an important step towards obtaining quantitative results for comparison with experiment.


## Authors’ contributions

O.T.D.: data curation, formal analysis, investigation, methodology, software, visualisation, writing - original draft, and writing - review & editing. R.C.B.: conceptualisation, formal analysis, funding acquisition, supervision, and writing - review & editing.


## Funding

This work was funded by EPSRC (Grant number: EP/T002794/1).


## Acknowledgements

We thank Dan Hebenstreit and Juntai Liu, and all the research team associated with that grant, for many discussions throughout the project. We acknowledge the Warwick Scientific Computing RTP for providing the computational resources used.


## Data accessibility

The simulation and analysis codes can be found along with all data in the repository: http://wrap.warwick.ac.uk/163395/


## Appendix A Verifying equilibration

To determine when systems have equilibrated, we first calculate the radial distribution functions between all species i i and j j , at each time t t : g i ​ j ​ ( r , t ) g_{ij}(r,t) . When doing this, we exclude pairs of particles within the same molecule.

We then integrate these like so

where the upper limit roughly corresponds to the radius of the first minimum in a typical liquid RDF. I i ​ j ​ ( t ) I_{ij}(t) then quantifies the relaxation of the RDF. Fig. 7 shows examples of this for a variety of systems evolving between different mixed and separated states. In all plots we show I cc , I pp I_{\mathrm{cc}},~I_{\mathrm{pp}} and I cp I_{\mathrm{cp}} to show the relaxation of the two bulk phases. Where tadpoles are present, we also show I ct I_{\mathrm{ct}} and I tp I_{\mathrm{tp}} to characterise their relaxation with respect to both phases.

We used Fig. 7 (a) to confirm our systems relax to separated states, and generated pre-separated states for systems containing tadpoles. In Figs. 7 (b) and (c), which correspond to systems shown in Fig. 4 , the tadpoles started in the polymer phase where they mostly stayed in (b) though they do prefer the interface leading to a notable increase in I c ​ t I_{ct} over time. In part (c), many tadpoles leave the polymer phase, leading to a larger increase in I ct I_{\mathrm{ct}} and decrease in I tp I_{\mathrm{tp}} . The high densities made this a slow process, but exponential fits to our relaxation curves show we simulated out to about 6 times the relaxation time, making changes small enough at the end of the time series to treat as equilibrated.

In Fig. 7 (d) the tadpoles started with uniform density and the minority polymer component mixes with the colloid phase over time. This is seen by I pp I_{\mathrm{pp}} relaxing from a large value as polymers lose sight of each other.


## Appendix B The SAFT formalism

Statistical associating fluid theory (SAFT) provides a formalism for estimating the free energy in systems of associating particles, including polymers. Here we summarise the SAFT expressions in Ref. [ 47 ] , using our hard sphere potentials, starting by breaking the Helmholtz free energy is into 4 terms

These respectively represent the ideal gas term, the contribution from individual particles in the absence of bonds, the contribution from intra-chain interactions, and the contribution from inter-chain interactions.

For our hard systems F assoc = 0 F_{\mathrm{assoc}}=0 , while the ideal gas term is the usual sum over molecule species

with the system volume V V and the thermal wavelength λ th \lambda_{\mathrm{th}} .

The particle term uses an average contribution per particle calculated as

where

and σ i \sigma_{i} is the diameter of particles of species i i . Applying this to all particles gives

Finally, the chain term accounts for covalent bonds holding connected bead centres a distance ( σ i + σ j ) / 2 (\sigma_{i}+\sigma_{j})/2 apart. I.e., the hard spheres are in contact. This is accounted for through the value of the radial distribution function at contact

in which

Then

counting all the bonds between tadpole heads, h, tadpole tail beads, t, and polymer beads, p.

From the free energy expression, we get the (osmotic) pressure from p SAFT = − ( ∂ F SAFT / ∂ V ) T , N p_{\mathrm{SAFT}}=-\left(\partial F_{\mathrm{SAFT}}/\partial V\right)_{T,N} . In this work, we solved this numerically to identify combinations of molecule densities with pressure equal to the upper and lower bounds found experimentally [ 43 ] . This range is then shown as the shaded volume in Fig. 6 .


## References