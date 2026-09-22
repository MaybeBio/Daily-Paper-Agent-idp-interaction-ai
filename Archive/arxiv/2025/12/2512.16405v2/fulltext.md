## A single-chain nanoparticle-based mean-field theory for associative polymers

Associative polymers are a class of polymers containing attractive stickers that can reversibly bind to each other. Their fully-bonded state gives rise, in dilute conditions, to a fluid phase of so-called single-chain nanoparticles (SCNPs). These constructs have been used in a wide range of applications, from the design of new materials ( e.g. biomolecular condensates) to drug-delivery vectors. The thermodynamic properties of SCNPs sensitively depend on the number of different sticker types, since numerical simulations show that a continuous transition to a network of chains upon increase of polymer concentration in the single sticker-type case can be replaced by an abrupt network formation (via a first-order phase transition) in the multiple sticker-type case. We present here a theory that, using the SCNP fluid as the reference system, quantifies the free energy change associated with transferring an intra-molecular bond to an inter-molecular bond, elucidating the impact on the phase separation process of the sticker topology. Despite its simplicity, the theory highlights which microscopic assumptions (looping statistics, chain-level excluded volume) are most relevant for accurately capturing the thermodynamics of these systems. Our results match available numerical predictions obtained via coarse grained simulations of these systems, highlighting in particular the sensitivity of the phase behaviour on the sequence of the stickers along the chain.


## I Introduction

Polymers are a class of macromolecules with unique properties: their large conformational freedom, combined with their periodic chemical structure, make them an interesting subject of study in many contexts, from statistical mechanics to materials science and biophysics. Relevant applications include, among others, their use in the design of new synthetic materials 12 ; 40 ; 10 ; 9 ; 45 , as drug-delivery vectors 2 ; 20 , or as models for many biological phenomena 24 ; 3 ; 31 .

While extensive research has been dedicated to the description of regular ( i.e. so-called athermal ) polymer solutions, especially with respect to their equilibrium properties and thermodynamic behaviour 14 ; 17 , comparatively less effort has been devoted to the study of so-called associative polymers , i.e. , chains in which special reactive monomers (named stickers ) are distributed along the chain, separated by a number of chemically inert (spacer) monomers 35 ; 7 ; 24 . Usually, spacer monomers are modelled as particles interacting solely through steric repulsion, whereas the much less abundant stickers are relatively small, strongly aggregating functional groups of potentially different types. When stickers are close enough, they are able to form bonds with other stickers through a wide range of interactions, ranging from metal complexation 19 and ionic or hydrophobic interactions 1 to hydrogen 13 ; 8 and even covalent 11 ; 21 bonds. In many cases, each sticker can be involved in no more than a single bond and, in the case of multiple sticker types, only with a sticker of a compatible type. Throughout the years, these foregoing ingredients have been used to develop models that have been successfully applied to several contexts, from biomolecular condensates 6 and RNA-protein mixtures 5 , to vitrimers 36 ; 26 ; 44 and single-chain nanoparticles (SCNPs), which are self-folding macromolecules that are of potential interest in a wide range of applications 23 ; 25 ; 22 ; 39 .

When a bond between two stickers forms, the interacting pair of monomers is constrained to move together, thus reducing the conformational entropy of the system to different extents, which depend on whether the bond is intermolecular ( i.e. , between stickers belonging to different chains) or intramolecular ( i.e. , between stickers within the same chain) 35 . This entropic term, intrinsic to the polymeric nature of the particles, plays a major role in determining the thermodynamics of associative polymers. The dependence on the number and type of attractive sites of said conformational entropy contribution is complex 22 , yet crucial to correctly predict the system’s thermodynamic properties.

For associative polymers with a single type of stickers in a good solvent, theory and experiments have shown that, upon increasing the concentration, the chains form a network continuously, without signs of a thermodynamic phase transition 35 ; 43 ; 5 ; 29 ; 27 . By contrast, it was shown by computer simulations that, if the stickers of the SCNPs along the chain are of two or more different and alternating types, in the fully-bonded limit ( i.e. large monomer-monomer attraction strength compared to the thermal energy) a significant entropic contribution induces a first-order phase transition: the network forms abruptly at a certain concentration 28 ; 27 . Indeed, changing the number of types of reactive monomers affects the ratio of intra- to intermolecular bonds and thus the overall inter-polymer large-scale connectivity. This behaviour has been recently confirmed by realistic simulations of all-DNA-based SCNPs 38 .

The appearance of such a phase transition can be understood by noting that, starting from a chain decorated by only one type of stickers and everything else being equal, converting some of them to a different type de-facto increases the average distance between identical stickers, i.e. the contour length of the loop between bonded stickers. The resulting fully-bonded SCNP will be more dense, and will have a smaller gyration radius. As a further consequence, we envision that there will be a greater entropic gain from swapping intramolecular for intermolecular bonds. We show here that if such a gain is large enough, the system will phase-separate even in the presence of a good solvent. To quantify these expectations, we introduce a mean-field estimate of the free energy cost of swapping intra-molecular to inter-molecular bonds and how such a cost depends on the number of different sticker types. Adding the free-energy cost of swapping to the reference system free energy (where the SCNP reference free energy is estimated up to the second term of the virial expansion) provides predictions for the phase behaviour that recapitulate the numerical results, providing support to the idea of leveraging the sticker sequence to manipulate the thermodynamics of associative polymers.


## II A mean-field theory for sticker association

We consider a solution of associative polymers consisting of chains made by N N monomers. Each chain bears ℳ ≪ N \mathcal{M}\ll N equally-spaced associative groups of m m different types (the stickers ) which alternate along the backbone. Two consecutive stickers are separated by l = N ℳ l=\frac{N}{\mathcal{M}} inert monomers, so that two consecutive stickers of the same type are separated by L ≈ m ​ N ℳ = m ​ l L\approx m\frac{N}{\mathcal{M}}=ml such monomers, as shown in Fig. 1 (a). Inert monomers interact solely through steric repulsion, while each sticker is able to form a single reversible bond with another sticker of the same type. We are interested in developing a theoretical characterisation of the system’s thermodynamic behaviour in the limit in which essentially all bonds are formed. Such a fully-bonded state can be achieved by either considering the low-temperature limit, or the large bond-strength limit. Since all possible bonds are formed, the total number of bonds is fixed, with individual bonds switching from inter-chain to intra-chain and vice versa. Under these conditions, to a first approximation the system internal energy (which is dominated by the bond contribution) remains constant regardless of the way bonds are distributed among the polymers. As such, under these conditions the equilibrium properties of the system are controlled by the maximization of the total entropy.

In the fully-bonded limit, under highly diluted conditions, all bonds are intra-chain. Each polymer constitutes an independent entity, which we call a SCNP. For fully-flexible polymers, the entropic cost of binding (which forces the inert monomers between the bonded sites to form a closed loop) scales with the size of the loop, and therefore intramolecular bonds tend to occur between consecutive stickers of the same kind 35 . If we let the number of stickers of each type be even, the chains fold on themselves in closed, cactus-like structures. On increasing the number of different stickers, the fully-bonded structure becomes increasingly compact, as shown in panels (b) and (c) of Fig. 1 . This solution of weakly interacting fully-bonded SCNPs constitutes the reference system with respect to which inter-chain bonding contributions are considered.

We write the Helmholtz free energy density β ​ f \beta f (here β = 1 k B ​ T \beta=\frac{1}{k_{B}T} , with T T indicating the temperature of the system and k B k_{B} the Boltzmann constant) of the system using a mean-field perturbative approach as:

where c c is the number density of monomers. The first term β ​ f ref \beta f_{\rm ref} is the free energy of a system of independent SCNPs and constitutes the sum of an ideal-gas-of-chains term β ​ f ig ​ ( c ) = c N ​ log ⁡ c N ​ e \beta f_{\rm ig}(c)=\frac{c}{N}\log{\frac{c}{Ne}} (note that e e is Napier’s number and c N \frac{c}{N} is the number density of chains ) and a purely repulsive, steric contribution β ​ f ex \beta f_{\rm ex} . The latter is modelled as a first correction to the ideal gas, i.e.

where B 2 B_{2} is the (purely repulsive) second virial coefficient of the fully-bonded SCNP.

To assess the quality of the approximated reference free energy (Eq. 2 ), we perform simulations of a system of fully intra-bonded SCNPs with one ( m = 1 m=1 ) or two ( m = 2 m=2 ) types of stickers in the limit of large binding strength. Fig. 2 compares the equation of state (EOS) of fully intra-bonded SCNPs with the second-order virial expansion in the chain number density ( c / N c/N ), performed using the B 2 B_{2} value extracted from two-body simulations (see the Methods ). Up to c ≈ 0.04 c\approx 0.04 , a value rather close to the critical density of these systems 28 , the virial expression properly reproduces the EOS. By contrast, a second-order virial expansion at the monomer level ( i.e. in the monomer density c c ), which is what has been often used in the past 35 , greatly overestimates the excess contribution to the pressure of the system.

The second term in Eq. 1 expresses the change in the system when intra-polymer bonds are swapped for inter-polymer bonds. We thus focus on the inter-polymer bonds and on the association phenomenon resulting from the swap between intra- and inter- bonds.

Specifically, we envision two bonded stickers of the same type i i on the same polymer as a chemical species A i ​ 1 A_{i1} , or equivalently a complex of inert monomers separated by two identical stickers. By a bond-swapping process two A i ​ 1 A_{i1} units, each on a different polymer, can react to form a A i ​ 2 A_{i2} intermolecular complex, as illustrated schematically in Fig. 1 (d). Therefore, the process can be formally modelled as a chemical reaction:

In a more precise thermodynamic formalism, the chemical equilibrium can be written as (indicating with N A i ​ 1 N_{A_{i1}} and N A i ​ 2 N_{A_{i2}} the number of A i ​ 1 A_{i1} and A i ​ 2 A_{i2} units and with Q A i ​ 1 Q_{A_{i1}} and Q A i ​ 2 Q_{A_{i2}} their partition functions 16 ; 33 ):

The expressions for Q A i ​ 1 Q_{A_{i1}} and Q A i ​ 2 Q_{A_{i2}} are reported in Appendix A . In terms of the degree of conversion q i q_{i} (the fraction of possible A i ​ 2 A_{i2} units formed), the law of mass action corresponding to the chemical reaction of Eq. ( 3 ) is:

where v L v_{L} is the volume accessible to the chain of length L L separating two consecutive stickers, which we assume to scale as v L = a 3 ​ L 3 ​ ν v_{L}=a^{3}L^{3\nu} , a a is a characteristic length of the order of the monomer diameter and ν \nu is a scaling exponent which will be discussed further below. Since the right-hand side of the previous equation is actually independent of i i , we can consider all the { q i } \{q^{i}\} to be the same and set them to q q . Resolving with respect to q q , we obtain:

To check the accuracy of our estimate of the partition functions of the A i ​ 1 A_{i1} and A i ​ 2 A_{i2} units, we carry out MD simulations of two A i ​ 1 A_{{i1}} units (modelled as polymers of 20 monomers with sticky sites at both ends) and compute q ( 1 − q ) 2 \frac{q}{(1-q)^{2}} (here q q is the fraction of interchain-bonded configurations out of all the fully-bonded configurations obtained) as a function of the monomer concentration c c . We calculate q ( 1 − q ) 2 \frac{q}{(1-q)^{2}} both including and excluding the repulsive interactions between non-adjacent monomers, to test the relation for ideal and self-avoiding polymers. A thorough explanation on how these simulations were carried out can be found in the Methods . The results of these computations are presented in Fig. 3 as symbols. The line through the data is a power-law fit, consistent with Eq. ( 5 ). The best-fit critical exponent ∼ L 3 ​ ν \sim L^{3\nu} is close to the expectation values from standard polymer theory for both ideal ( 3 ​ ν ideal ∗ = 1.5 3\nu^{*}_{\textrm{ideal}}=1.5 ) and self-avoiding ( 3 ​ ν real ∗ = 2.225 3\nu^{*}_{\textrm{real}}=2.225 ) chains, confirming the reliability of our estimate of the inter-chain bonding contribution. It is worth noting that here the expected real chain exponent is higher than the standard Flory estimate ν flory ∗ = 0.588 \nu^{*}_{\textrm{flory}}=0.588 because it takes into account the reduced probability of contact between two A i ​ 1 A_{i1} units due to excluded volume (see e.g. Ref. 35 ), which makes the entropic gain upon intra-chain bond breaking even larger.

We can now finalize the bonding contribution to the free-energy, based on the expressions derived to model associating network forming liquids by Wertheim 42 , as (see Appendix B for a simple derivation based on thermodynamic perturbation theory (TPT) 4 ):

Since q i = q q_{i}=q ∀ i \forall i , such bonding contribution to the free energy density simplifies to

This expression, combined with the reference free-energy, provides the total free energy density of the model:

We now note that β ​ f ​ ( c ) \beta f(c) takes, barring a factor m 2 \frac{m}{2} in β ​ f bond \beta f_{\textrm{bond}} and a different expression for β ​ f ex \beta f_{\rm{ex}} , the same structure as the one derived by Rubinstein and Semenov in Ref. 35 by leveraging a polymer-physics based approach for a system with only one type of sticker.


## III Phase diagram

The proposed free energy expression, derived in the limit of fully-bonded polymers, depends on the two parameters c c and B 2 B_{2} . In such a plane, it is possible to calculate the binodal line (similar to the liquid-gas phase separation) and the critical point. More detailed explanations on the phase diagram calculation procedure are reported in the Methods .

After solving the relevant equations numerically, we find that, for a given set of ℳ \mathcal{M} , l l and m m , there is a critical value of the chain-chain second virial coefficient, B 2 , m crit B_{2,m}^{\rm crit} , above which the system never phase-separates. Figure 4 shows examples for two systems (respectively with m = 1 m=1 and m = 2 m=2 ) previously investigated numerically, for both ideal, Fig. 4 (a), and real, Fig. 4 (b), chains. In the latter case, we also plot the values of the B 2 B_{2} evaluated in simulations for the two types of chains with horizontal dashed lines. The figure shows that, consistently with the numerical findings 27 , the theory predicts that the system with m = 1 m=1 does not phase-separate, while m = 2 m=2 real chains do.

Notably, for the case in which phase separation is present ( m = 2 m=2 ) the theory predicts a value for the concentration of the dense phase c dense ​ a 3 ​ N ≈ 1 c^{\rm dense}a^{3}\sqrt{N}\approx 1 which is in reasonable agreement with the numerical value of ≈ 1.6 \approx 1.6 28 .


## IV Scaling of the critical parameters

In order to theoretically characterise the scaling properties of the critical parameters of the system, we simplify Eq. ( 6 ) by assuming that c ​ v L L ≪ 1 c\frac{v_{L}}{L}\ll 1 for c c close to c crit c_{\rm crit} , which, as we will show a posteriori , is true if ℳ \mathcal{M} is sufficiently large. Since v L ∼ a 3 ​ L 3 ​ ν v_{L}\sim a^{3}L^{3\nu} , the former assumption implies c ​ a 3 ​ L 3 ​ ν − 1 ≪ 1 ca^{3}L^{3\nu-1}\ll 1 . We can now write:

with q ≪ 1 q\ll 1 . As a result, only few stickers are involved in intermolecular bonds, which confirms that the bonding part of the free energy can be treated as a perturbation of the reference state, where only intra-molecular bonds are present. This is coherent with numerical results, which show that close to the critical point the fraction of stickers involved in intermolecular bonds in the high-density phase is ≈ 0.12 \approx 0.12 28 . Because such a small fraction of stickers forms intermolecular bonds, the vast majority of stickers on each chain are engaged in intrachain bonding and thus unavailable for interchain interactions. This suppresses correlations between stickers belonging to the same chain: a free sticker is essentially equally (un)likely to encounter another free sticker from its own chain as from a different one. Consequently, all available stickers become effectively indistinguishable, thereby justifying the use of a mean-field description.

In the aforementioned low- q q approximation, the criticality conditions become:

which can be solved to yield

By using Eq. ( 12 ) we can check that the assumption c m crit ​ v L L ∼ ℳ − 1 2 ≪ 1 \frac{c^{\rm crit}_{m}v_{L}}{L}\sim\mathcal{M}^{-\frac{1}{2}}\ll 1 holds near the critical point at fixed values of ℳ \mathcal{M} and L L when ℳ ≫ 1 \mathcal{M}\gg 1 , confirming that, in this limit, q ≪ 1 q\ll 1 .

Eq. ( 13 ) can be used to rationalise the available numerical data 27 ; 28 , since it shows that increasing m m explicitly increases the tendency to phase-separate. Indeed, at fixed l l , ℳ \mathcal{M} , and N = l ​ ℳ N=l\mathcal{M} , the critical second virial coefficient scales as B 2 , m crit ∼ m 3 ​ ν − 1 B^{\rm{crit}}_{2,m}\sim m^{3\nu-1} .

It is also interesting to look at how B 2 , m c ​ r ​ i ​ t B_{2,m}^{crit} scales when ℳ \mathcal{M} and m m are kept fixed, i.e. when l l (and therefore N N ) change. In this case, for Gaussian chains B 2 , m crit ∼ N 3 2 B^{\rm crit}_{2,m}\sim N^{\frac{3}{2}} , while for real chains B 2 , m crit ∼ N 2.225 B^{\rm crit}_{2,m}\sim N^{2.225} . If we assume that in both cases the second virial coefficients scale with the gyration radius R g R_{g} as B 2 ∼ R g 3 ∼ N 3 2 B_{2}\sim R_{g}^{3}\sim N^{\frac{3}{2}} (as demonstrated for real SCNPs in a good solvent in both experiments 29 and simulations 22 ), we find that B 2 , m crit B 2 \frac{B^{\rm crit}_{2,m}}{B_{2}} is independent of l l for Gaussian chains, while scales as ∼ l 0.725 \sim l^{0.725} for real chains. Therefore, for Gaussian chains the theory predicts that the phase behaviour of a system of associative polymers with ℳ \mathcal{M} stickers of m m types is not affected by l l . By contrast, for real chains the driving force for phase separation increases with l l , so that a given system will eventually phase-separate, provided that l l is large enough. For instance, for the m = 1 m=1 case with ℳ = 24 \mathcal{M}=24 , which does not separate in numerical simulations when l = 10 l=10 , our theory predicts that B 2 , m crit B 2 ≥ 1 \frac{B^{\rm crit}_{2,m}}{B_{2}}\geq 1 , and therefore the system can undergo phase separation, for l ≳ 50 l\gtrsim 50 , a value for which simulations are currently unfeasible. In the future, it would be interesting to test which version of the theory better describes the behaviour of real SCNPs in a good solvent, both via simulations and experiments.


## V Conclusions

In conclusion, we have constructed a mean-field theory able to capture the physics of phase separation in associative polymers decorated with alternating stickers of m m different types, corroborating numerical results showing how increasing m m enhances the driving force for phase separation. We have shown that a virial expansion at the chain level ( i.e. which uses the full-chain excluded volume instead of the monomer excluded volume) for the repulsive term in the free energy is effective at reproducing the equation of state obtained from numerical simulations of SCNPs. Indeed, notwithstanding the approximations, the theory matches numerical results at least semi-quantitatively, correctly predicting the presence of phase separation when m = 2 m=2 .

Overall, our results provide a compact, yet physically transparent framework for understanding how the number and type of stickers control the phase behaviour of SCNP solutions. Forming bonds between different polymers unfreezes some of the entropy captured in the isolated fully-bonded SCNP. The amount of this entropic gain may (or may not, depending on the number of sticker types) be sufficient to drive a macroscopic phase separation process. Despite its simplicity, the theory identifies the dominant entropic mechanisms and highlights which microscopic assumptions (looping statistics, chain-level excluded volume) are most relevant for accurately capturing the thermodynamics of these systems.


## VI Methods


## VI.1 Phase diagram calculation

To compute the binodal lines in Fig. 4 , we have numerically solved the following system of equations enforcing chemical and mechanical equilibrium between the polymer-poor (gas) and polymer-rich (liquid) phases for a given value of the second virial coefficient B 2 B_{2} :

where μ ⁡ ( c , B 2 ) = ∂ f ⁡ ( c , B 2 ) ∂ c \mu(c,B_{2})=\frac{\partial f(c,B_{2})}{\partial c} is the chemical potential and P ⁡ ( c , B 2 ) = c ​ ∂ f ⁡ ( c , B 2 ) ∂ c − f ⁡ ( c , B 2 ) P(c,B_{2})=c\frac{\partial f(c,B_{2})}{\partial c}-f(c,B_{2}) is the associated pressure.

The critical point ( c crit , B 2 crit ) (c^{\rm{crit}},B_{2}^{\rm{crit}}) has been estimated by numerically finding the maximum of the spinodal line ∂ 2 f ⁡ ( c ) ∂ c 2 = 0 \frac{\partial^{2}f(c)}{\partial c^{2}}=0 , for which the following conditions hold:


## VI.2 Molecular simulations

We have simulated polymer chains in the N ​ V ​ T NVT ensemble by coupling the system to an Andersen-like stochastic thermostat 30 . The interaction between two monomers sharing a covalent bond, i.e. between two bonded neighbours, is given by the Kremer-Grest potential 18 :

with r r the distance between the two interacting monomers. The attractive, finitely extensible nonlinear elastic term is:

with K 0 = 30 ​ ϵ LJ σ 2 K_{0}=30\frac{\epsilon_{\rm LJ}}{\sigma^{2}} the bond stiffness and r 0 = 1.5 ​ σ r_{0}=1.5\sigma the maximum extension (where σ \sigma and ϵ LJ \epsilon_{\rm LJ} define the length and energy units). The excluded-volume contribution is given by the purely repulsive WCA potential 41 :

We adopt reduced units and set σ = m = ϵ LJ = 1 \sigma=m=\epsilon_{\rm LJ}=1 . The potential is truncated at 2 1 / 6 ​ σ 2^{1/6}\sigma to remove the attractive contribution.

The interaction between non-bonded neighbours is given by a WCA repulsion (present only for non-ideal chains), Eq. ( 18 ), and by an additional short-range attractive term that acts only between stickers of the same type. The latter potential is modelled after the Stillinger-Weber potential 37 , widely adopted in soft-matter models of short-range attraction 15 ; 32 :

with σ s = 1.05 ​ σ \sigma_{s}=1.05\sigma , r c = 1.68 ​ σ r_{c}=1.68\sigma , C = 8.97 C=8.97 , D = 0.41 D=0.41 . The attraction depth (the energy scale of the bond interaction) is ϵ \epsilon .

To enforce the one-bond-per-sticker condition, we include a three-body potential U 3 ​ b U_{\rm 3b} that suppresses the formation of bonded triplets 34 . Specifically, U 3 ​ b U_{\rm 3b} introduces a repulsive contribution that compensates the energy gained upon forming a second bond. Thus, when monomer i i approaches a bonded pair ( j , k ) (j,k) , it moves along an almost flat energy hypersurface, meaning that configurations where i i binds to either j j or k k (while the third monomer is free to detach) are not separated by any energy barrier.

The three-body potential reads:

where the sum runs over all bonded triplets, defined as configurations in which particle i i is within r c r_{c} from both j j and k k .

The two-body factor U 3 ​ ( r ) U_{\rm 3}(r) is:

where σ s \sigma_{s} is the position of the minimum of U sticker U_{\rm sticker} .

We have performed the following types of simulations:

Simulations of two A i ​ 1 A_{i1} units : two sequences of 20 monomers each (both ideal-chain and real-chain conditions) to reconstruct the mass–action law of Fig. 3 . Each chain contains 2 stickers of the same type separated by 18 inert monomers. Identifying q q with the fraction of fully-bonded configurations in which the two chains are connected to each other via interchain bonds, we have computed ⟨ q / ( 1 − q ) 2 ⟩ \langle q/(1-q)^{2}\rangle at β ​ ϵ = 6 \beta\epsilon=6 and different values of the monomer concentration c c by varying the simulation box size.

B 2 B_{2} calculation : two fully-bonded chains of valence ℳ = 24 \mathcal{M}=24 and sticker-sticker spacing l = 10 l=10 , used to compute the excluded volume B 2 B_{2} for a pair of SCNPs. These simulations have been run at β ​ ϵ = 14 \beta\epsilon=14 . To calculate the second virial coefficient, we start computing the effective interaction between the two fully-bonded chains, with the constraint that only intramolecular bonding is possible. Using the same methodology described in Ref. 27 , we have evaluated the effective potential V eff ​ ( R ) V_{\rm eff}(R) , where R R is the distance between the two centres of mass, for the m = 1 m=1 and m = 2 m=2 cases. Fig. 5 shows that the resulting effective potential can be fitted to a Gaussian, from which we compute the second virial coefficient, defined as:

whence we obtain B 2 ≈ 8200 ​ a 3 B_{2}\approx 8200\,a^{3} for m = 1 m=1 and B 2 ≈ 5400 ​ a 3 B_{2}\approx 5400\,a^{3} for m = 2 m=2 .

Bulk simulations : 100 SCNPs with ℳ = 24 \mathcal{M}=24 and l = 10 l=10 and m = 1 m=1 or m = 2 m=2 , used to compute the equation of state at different values of the monomer concentration c c in Fig. 2 .

Throughout all simulations, the integration time step was set to Δ ​ t = 0.003 \Delta t=0.003 , expressed in natural units σ ​ m ϵ LJ \sigma\sqrt{\frac{m}{\epsilon_{\rm LJ}}} .


## Appendix A Mass action law derivation

We remind here that Q A i ​ 1 Q_{A_{i1}} and N A i ​ 1 N_{A_{i1}} in Eq. 4 indicate the partition function and the number of segments of inert monomers forced to loop by the presence of a bond between two i i -type stickers (see Fig. 1 ). Similarly, Q A i ​ 2 Q_{A_{i2}} and N A i ​ 2 N_{A_{i2}} indicate the canonical partition function and the number of two inter-polymer bonded A i ​ 1 A_{i1} units. The quantity N A i ​ 1 N_{A_{i1}} ranges between 0 0 and N i 2 \frac{N_{i}}{2} , where the latter is the maximum number of possible A i A_{i} units, corresponding to half of the total number of stickers of type i i . Similarly, 0 < N A i ​ 2 < N i 4 0<N_{A_{i2}}<\frac{N_{i}}{4} . Then:

For the A i ​ 1 A_{i1} unit we can write:

where we have explicitly highlighted the centre of mass contribution given by the volume of the system, V V . The term V 0 V_{0} is a volume term encoding the contribution to the A i ​ 1 A_{i1} partition function from all other internal degrees of freedom.

To work out Q A i ​ 2 Q_{A_{i2}} , we start from Q A i ​ 1 Q_{A_{i1}} and compute the total entropy variation Δ ​ S tot \Delta S_{\textrm{tot}} arising from breaking the intramolecular bonds of the two interacting units and forming the new intermolecular bonds.

This entropy difference can be decomposed in three different terms, following the steps depicted in Fig. 6 :

the entropy increase Δ ​ S 1 \Delta S_{1} associated with breaking the intramolecular bond between the stickers in a A i ​ 1 A_{i1} unit to open it. It is such that e Δ ​ S 1 k B = v L v b e^{\frac{\Delta S_{1}}{k_{B}}}=\frac{v_{L}}{v_{b}} ;

the entropy decrease Δ ​ S 2 \Delta S_{2} associated with the formation of a bond between two open chains of length L L , which generates an open chain of length 2 ​ L 2L . It is such that e Δ ​ S 2 k B = 4 ​ v b V e^{\frac{\Delta S_{2}}{k_{B}}}=\frac{4v_{b}}{V} , where the factor 4 accounts for the different ways in which two free chains can bond each other;

the entropy decrease Δ ​ S 3 \Delta S_{3} due to the formation of a closed complex of size 2 ​ L 2L . It is such that e Δ ​ S 3 k B = v b v 2 ​ L = v b 2 3 ​ ν ​ v L e^{\frac{\Delta S_{3}}{k_{B}}}=\frac{v_{b}}{v_{2L}}=\frac{v_{b}}{2^{3\nu}v_{L}} . Here the factor 2 3 ​ ν 2^{3\nu} has been added assuming a generic power scaling law v L ∼ a 3 ​ L 3 ​ ν v_{L}\sim a^{3}L^{3\nu} for SCNPs (for some references on the effective scaling behaviour of SCNPs, see 29 ; 22 ).

Overall, the total entropy contribution due to moving from two intramolecular A i ​ 1 A_{i1} units to a dimer is:

This means that the final expression for the dimer partition function amounts to:

where the factor 2 ! 2! counts the number of indistinguishable states of the system: the two A i ​ 1 A_{i1} in the first step of the transformation in Fig. 6 are identical.

Plugging these expressions in Eq. 4 , one gets:

where N A i = N i 2 = N tot 2 ​ L N_{A_{i}}=\frac{N_{i}}{2}=\frac{N^{\textrm{tot}}}{2L} , with N tot N^{\textrm{tot}} total number of monomers. Plugging this expression in Eq. ( 27 ), we obtain:

with c = N tot V c=\frac{N^{\textrm{tot}}}{V} .


## Appendix B The free energy of an ideal gas of clusters

We review here the expression for the bonding contribution to the Helmholtz free energy 16 ; 42 , following the derivation proposed in Ref. 4 . We focus on the free energy F F of an ideal gas of N N particles in a volume V V which can dimerize (particles with only one binding site). We will generalize this to a mixture of different particles later on. For the one-component case, in the ideal gas limit, if we call q q the probability that one bond is formed, the number of particles in monomeric state is N ⁡ ( 1 − q ) N(1-q) and the number of dimers is N ​ q 2 \frac{Nq}{2} . In the ideal gas, pressure counts the number of clusters, giving β ​ P ​ V = N ⁡ ( 1 − q ) + N ​ q 2 = N − N ​ q 2 \beta PV=N(1-q)+\frac{Nq}{2}=N-\frac{Nq}{2} . Similarly, the chemical potential coincides with the logarithm of the monomer concentration β ​ μ = ln ⁡ ( N ⁡ ( 1 − q ) ​ V 0 / V ) \beta\mu=\ln(N(1-q)V_{0}/V) , where the term V 0 V_{0} is a reference volume encoding the contribution from all other internal degrees of freedom.

Since the Gibbs free energy is N ​ μ N\mu , we have:

and thus:

which can be rewritten as the ideal gas contribution N ⁡ ( ln ⁡ N ​ V 0 V − 1 ) N(\ln\frac{NV_{0}}{V}-1) plus a bonding contribution F bond F_{\rm bond} with

For an ideal gas of different particles, the reference free energy includes the mixing term, but the bond contribution remains identical and needs only to be summed over the different species. As commonly done 42 , the ideal gas free energy is substituted by more accurate reference free energies. We do the same here, using as reference free energy the virial expression for SCNP. For our case, the bonding contribution can then be expresses as in Eq. 7 .


## Acknowledgements

We thank Sanat K. Kumar for helpful discussions. We acknowledge support from Cineca-ISCRA for HPC resources. L.R. acknowledges support from MUR-PRIN Grants No. 20225NPY8P and P2022JZEJR, funded by European Union “NextGenerationEU”, Missione 4 Componente 2-CUP B53D23028570001.


## References