## Dynamics of phase separation in non-local elastic networks

Phase separation of a liquid mixture embedded within an elastic network is relevant to a wide range of natural and industrial systems, including biomolecular condensates interacting with the cytoskeleton, structural colouring in bird feathers, and gas bubbles forming within soft sediments. Recent experiments in synthetic polymer gels have demonstrated that when the size of phase-separated domains is comparable to the characteristic pore size of the network, a patterned phase with a well-defined length scale may emerge. Theoretical works based on an equilibrium approach have attributed this pattern formation to non-local elastic effects arising from heterogeneity of the underlying network. Here, we extend these ideas by developing a dynamic theory in which phase separation is coupled to non-local elasticity via the framework of large-deformation poroelasticity. We study our model via both linear stability analysis and numerical simulation, identifying the parameter space in which phase separation occurs, and investigating the impact of different elasticity models. We find that although local elasticity can inhibit phase separation and affect domain count, it is unable to completely suppress coarsening. In contrast, non-local elasticity arrests coarsening to form patterned domains with a well-defined length scale that decreases with increasing stiffness. Our modelling framework thus paves the way for quantitative comparisons between simulations and experiments, for example by considering a strain-stiffening network rheology.


## 1 Introduction

The spontaneous phase separation of two immiscible fluids from a homogeneous mixture is a familiar everyday phenomenon. Fluid–fluid phase separation of a mixture confined within the pore space of a deformable solid network is also widespread throughout natural and industrial settings. Natural examples include sub-cellular condensates interacting with the cytoskeleton ( Wiegand and Hyman 2020 ; Lee et al. 2022 ; Zwicker et al. 2025 ) , and the formation of gas bubbles within soft geophysical materials such as seabed sediments and peatlands ( Wheeler 1988 ; Chen and Slater 2015 ; Paulin et al. 2022 ) . In materials science, phase separation in an elastic network can be utilised for the construction of novel micro-structured ( Fernández-Rico et al. 2022 ; Fernández-Rico et al. 2023 ) and stimulus-responsive ( Celora et al. 2022 ; Celora et al. 2023 ) materials. Finally, the texture and mechanical properties of many food products, such as chocolate and bread, depend sensitively on the size and distribution of small gas bubbles within the product ( Pugh et al. 2023 ; Mathijssen et al. 2023 ) , which are in turn determined by the interactions of these bubbles with the surrounding solid material as they are formed.

Historical research into elastically mediated phase separation originated in the study of spinodal decomposition in hydrogel systems ( Onuki and Puri 1999 , e.g. ) . Recently, significant interest in this field has been stimulated by experiments involving polymer gels saturated with an oil–oil mixture that phase separates into micron-scale droplets that exclude the elastic polymer network ( Style et al. 2018 ; Rosowski et al. 2020a ; Rosowski et al. 2020b ; Fernández-Rico et al. 2023 ) . It is now widely recognised that the additional energetic cost of network deformations induced by phase separation can inhibit the onset of phase separation, limit the size of phase-separated domains, and control domain morphology. For gels in which there exists a gradient in material stiffness, phase separation will occur preferentially in softer regions of the gel. This result can lead to an ‘elastic ripening’ effect, in which droplets in softer regions grow at the expense of droplets in stiffer regions ( Rosowski et al. 2020b ; Vidal-Henriquez and Zwicker 2020 ; Kothari and Cohen 2023 ) . Further works have also studied the role of kinetic effects ( Vidal-Henriquez and Zwicker 2020 ) or a strain-stiffening network rheology ( Kothari and Cohen 2020 ; Wei et al. 2020 ) in droplet size control, as well as investigating the impact of network damage ( Vidal-Henriquez and Zwicker 2021 ; Paulin et al. 2022 ) and wetting effects ( Paulin et al. 2022 ; Ronceray et al. 2022 ; Liu et al. 2023 ) .

Recent experiments in the same system have also demonstrated the formation of persistent patterned phases that do not coarsen over time ( figure 1 ), and that can form either droplet-like or bicontinuous morphologies ( Fernández-Rico et al. 2023 ) . It has been hypothesised that these phases are equilibrium states that can form via a continuous phase transition from a homogeneous gel ( Fernández-Rico et al. 2023 ) . Recent theoretical work has suggested that the observed size selection results from a competition between two different length scales: the elasto-capillary length; and a non-locality length arising from heterogeneities in the network mesh structure that manifest in a non-local elastic response ( Qiang et al. 2024 ) . Multi-dimensional extensions to this approach have studied the role of non-local elastic effects in controlling domain morphology ( Mannattil et al. 2024 ; Oudich et al. 2025 ) . The very recent work of Oudich et al. 2025 also explores dynamic simulations of this phenomenon, in a partially linearised elastic framework. First steps towards quantitive comparisons between experiments and theory have been formulated by considering a strain-stiffening rheology for the elastic network ( Fernández-Rico et al. 2025 ) .

Here, we extend the equilibrium theory of Qiang et al. 2024 to study the dynamics of phase separation in a non-local elastic network, taking into account finite (large) deformations of the mesh. Network deformation within swollen regions is typically extremely large, and so a theory that takes into account large deformations is needed. Theories of phase separation in polymer gels that account for finite elastic deformations have previously been developed for studying the volume phase transition and spinodal decomposition in hydrogels ( Onuki and Puri 1999 ; Hong et al. 2008 ; Zhou et al. 2010 ; Hong and Wang 2013 ; Drozdov et al. 2016 ; Bertrand et al. 2016 ; Hennessy et al. 2020 ) . Our modelling approach represents an extension to these works that also incorporates non-local elastic effects. In this manuscript, we first layout our modelling framework ( section 2 ), deriving a one-dimensional (1D) model for simplicity. In section 3 , we then conduct a linear stability analysis of our model, exploring the resulting dispersion relation and constructing phase diagrams. Next, we use our model to conduct numerical simulations of spontaneous phase separation, both for local ( section 4 ) and non-local ( section 5 ) elastic responses. Finally, in section 6 we discuss the implications of our work and connections to other similar studies.


## 2 Model development

To construct our model, we consider a two-component mixture comprising an elastic network and a viscous solvent in 1D. In order to describe the evolution of this mixture within the framework of large-deformation poroelasticity ( MacMinn et al. 2016 ; Hennessy et al. 2020 , e.g. ,) , we begin by defining kinematic relations between an Eulerian lab frame and a Lagrangian reference frame that is attached to the elastic network. Next, we prescribe a free energy functional that describes the energetic properties of the mixture, before constructing transport equations for the mixture via mass balance of each component. Finally, we derive a constitutive law for the elastic stress in differential form that takes into account non-local elastic interactions.


## 2.1 Kinematics

We develop our model in the lab frame, with coordinates denoted by x {x} . Coordinates in the reference frame are denoted by X {X} . Transformations between the two coordinate systems are governed by the deformation J = ∂ x / ∂ X {J}={\partial{x}}/{\partial{X}} , which quantifies the ratio of volumes in the lab and reference coordinate systems. Note that deformation is linked to the Eulerian displacement of the network u ⁡ ( x ) = x − X ⁡ ( x ) {u}({x})={x}-{X}\left({x}\right) via the relation J = ( 1 − ∂ u / ∂ x ) − 1 {J}=\left(1-{\partial{u}}/{\partial{x}}\right)^{-1} . To characterise mixture composition, we define the Eulerian volume fraction of the network and solvent components as ϕ n ​ ( x ) \phi_{\textrm{n}}({x}) and ϕ s ​ ( x ) \phi_{\textrm{s}}({x}) , respectively. Assuming that both the network and solvent are locally incompressible, we can then write the no-void condition ϕ n + ϕ s = 1 \phi_{\textrm{n}}+\phi_{\textrm{s}}=1 , such that only one of ϕ n \phi_{\textrm{n}} and ϕ s \phi_{\textrm{s}} is required to fully determine the composition of the mixture. Finally, the volume fraction of a homogeneous, undeformed network ( J = 1 J=1 ) is given by the relaxed network fraction ϕ n ​ ( x ) = ϕ n 0 \phi_{\textrm{n}}(x)=\phi_{\textrm{n}}^{0} . Network fraction can thus be linked to deformation via J ⁡ ( x ) = ϕ n 0 / ϕ n ​ ( x ) {J(x)=\phi_{\textrm{n}}^{0}/\phi_{\textrm{n}}(x)} .


## 2.2 Free energy

To describe the energetic interactions of the network–solvent mixture, we follow Qiang et al. 2024 and assume that the total free energy Ψ \Psi can be written as a sum of a local part and a non-local part,

where we define the local free energy denity f 0 f_{0} in the lab frame, and the non-local energy density f nl f_{\textrm{nl}} in the reference frame. We take f 0 f_{0} to be a symmetric Flory–Huggins energy of the form

Here, k B k_{\textrm{B}} is the Boltzmann constant, T T is temperature, ν \nu is the molecular size, χ \chi is the Flory interaction parameter, and κ \kappa is an interfacial coefficient. Note also that the integral is taken over the volume element d ​ x \textrm{d}x defined in the lab frame.

For the elastic contribution to the energy, we assume that the network has a compressible Neo-Hookean rheology. For a local elastic model, this rheology is given by a hyperelastic strain-energy density

where G G and K K are the respective shear and bulk moduli of the network. We capture non-local elastic effects by taking the non-local energy to be a convolution of this energy with an isotropic kernel g ξ ​ ( X ) g_{\xi}(X) in the reference frame. The non-local free energy density is then

where J ~ = ∫ J ′ ​ g ξ ​ ( X ′ − X ) ​ d ​ X ′ \tilde{J}=\int J^{\prime}g_{\xi}\left(X^{\prime}-X\right)\textrm{d}X^{\prime} , J ′ J^{\prime} is the value of J J evaluated at X ′ X^{\prime} , and d ​ X \textrm{d}X is the volume element in the reference frame. We use this expression to find a non-local constitutive law for the elastic stress in section 2.4 below.


## 2.3 Transport equations

We now derive transport equations describing the evolution of mixture composition. To begin, we consider conservation of mass of the network, writing the continuity equation in the Eulerian frame as

where v n = J ​ ∂ u / ∂ t {v}_{\textrm{n}}=J\partial{u}/\partial t is the Eulerian velocity of the network. Similarly, conservation of mass for the solvent implies that

where v s {v}_{\textrm{s}} is the Eulerian solvent velocity. Using ϕ n + ϕ s = 1 \phi_{\textrm{n}}+\phi_{\textrm{s}}=1 , and summing equations ( 5 ) and ( 6 ) then gives ∂ q / ∂ x = 0 \partial q/\partial x=0 , where q = ϕ n ​ v n + ϕ s ​ v s {q}=\phi_{\textrm{n}}{v}_{\textrm{n}}+\phi_{\textrm{s}}{v}_{\textrm{s}} is the total mixture flux. In 1D, q q is constant, and is determined by the boundary conditions. Defining the flux of solvent relative to the network as j s = ϕ s ​ ( v s − v n ) {j}_{\textrm{s}}=\phi_{\textrm{s}}({v}_{\textrm{s}}-{v}_{\textrm{n}}) , we can rewrite equation ( 5 ) in terms of q {q} and j s {j}_{\textrm{s}} as

Given an appropriate expression for the solvent flux j s {j}_{\textrm{s}} , equation ( 7 ) then provides a complete description of the dynamics of the mixture. Note that by focussing on a system with periodic boundary conditions, we can set q q to zero without loss of generality.

To find an expression for j s {j}_{\textrm{s}} , we assume that fluxes are driven by gradients in both chemical potential μ \mu and elastic stress σ {\sigma} ( Onuki and Puri 1999 ) ,

where Λ ⁡ ( ϕ n ) \Lambda(\phi_{\textrm{n}}) is the solvent mobility. The exchange chemical potential μ \mu is calculated as the variational derivative of the free energy with respect to composition such that μ = − ν δ Ψ / δ ϕ n \mu=-\nu{\delta\Psi}/{\delta\phi_{\textrm{n}}} . For the free energy defined in equation ( 1 ) , this gives

Similarly, an expression for the elastic stress σ {\sigma} in terms of deformation J J is found by taking the derivative of energy with respect to deformation, as discussed in detail below.


## 2.4 Non-local stress law

To quantify the elastic stress in the Eulerian frame, we work with the Cauchy stress tensor, defined as

For the non-local elastic energy defined in equation ( 4 ) , we thus find that

where we recall that J ~ = ∫ J ′ ​ g ξ ​ d ​ X \tilde{J}=\int J^{\prime}g_{\xi}\textrm{d}X . For a given convolution kernel, it may be possible to write an equation for this non-local stress in differential form. To do this, it is convenient to first split the elastic stress into two parts, such that σ = σ ′ − σ ∗ \sigma=\sigma^{\prime}-\sigma^{*} , where σ ′ = ∫ [ G ​ J ′ + K ⁡ ( J ′ − 1 ) ] ​ g ξ ​ d ​ X ′ \sigma^{\prime}=\int\left[GJ^{\prime}+K(J^{\prime}-1)\right]g_{\xi}\textrm{d}X^{\prime} and σ ∗ = G / J ~ \sigma^{*}=G/\tilde{J} . We then choose the convolution kernel g ξ = exp ( − | X | / ξ ) / 2 ξ g_{\xi}=\exp({-|{X}|/\xi})/2\xi , where ξ \xi is the non-locality scale. In this case, we find that

and

where ∂ / ∂ X = J ∂ / ∂ x \partial/\partial X=J\partial/\partial x is the spatial derivative with respect to coordinates in the reference state, and we recall that J J is linked to network volume fraction via the kinematic relation J = ϕ n 0 / ϕ n {J=\phi_{\textrm{n}}^{0}/\phi_{\textrm{n}}} . Note that in the limit of zero non-locality length ξ = 0 \xi=0 , we recover the local Neo-Hookean stress σ = G ⁡ ( J − 1 / J ) + K ⁡ ( J − 1 ) \sigma=G(J-1/J)+K(J-1) . A detailed derivation of these equations is provided in appendix A .


## 2.5 Model summary and non-dimensionalisation

Equations ( 7 ) –( 9 ), along with equations ( 12 ) and ( 13 ), provide a complete set of coupled partial differential equations that describe the evolution of the network–solvent mixture. Non-dimensionalising our model by length scale κ \sqrt{\kappa} , time scale κ ​ ν / Λ ​ k B ​ T \kappa\nu/\Lambda k_{\textrm{B}}T , and stress scale k B ​ T / ν k_{\textrm{B}}T/\nu motivates introducing the dimensionless variables 𝒢 = G ​ ν / k B ​ T \mathcal{G}=G\nu/k_{\textrm{B}}T , 𝒦 = K ​ ν / k B ​ T \mathcal{K}=K\nu/k_{\textrm{B}}T , and ℓ 2 = ξ 2 / κ \ell^{2}=\xi^{2}/\kappa . Here, 𝒢 \mathcal{G} and 𝒦 \mathcal{K} are the rescaled shear and bulk moduli of the elastic network, respectively, and ℓ \ell quantifies the size of the non-locality length relative to the interfacial width κ \sqrt{\kappa} . Choosing a solvent mobility of the form Λ ⁡ ( ϕ n ) = Λ ⁡ ( 1 − ϕ n ) ​ ϕ n \Lambda(\phi_{\textrm{n}})=\Lambda(1-\phi_{\textrm{n}})\phi_{\textrm{n}} , we now analyse our model via both linear stability analysis ( section 3 ) and numerical simulations ( sections 4 and 5 ). To carry out numerical simulations, we discretise in space on a uniform grid, and approximate spatial derivatives with a centralised finite difference scheme. We then solve for ϕ n \phi_{\textrm{n}} , σ ′ \sigma^{\prime} and σ ∗ \sigma^{*} at each time step with MATLAB’s in-built ode solver ode15s .


## 3 Linear stability analysis

To gain insight into the parameters that control the onset of phase separation, we now conduct a linear stability analysis of our model. We linearise our system about a base state corresponding to a uniformly swollen network with volume fraction ϕ ¯ n \bar{\phi}_{\textrm{n}} . The corresponding base stress state is then σ ¯ = 𝒢 ⁡ ( J ¯ − 1 / J ¯ ) + 𝒦 ⁡ ( J ¯ − 1 ) \bar{\sigma}=\mathcal{G}\left(\bar{J}-1/\bar{J}\right)+\mathcal{K}\left(\bar{J}-1\right) , where J ¯ = ϕ n 0 / ϕ ¯ n \bar{J}=\phi_{\textrm{n}}^{0}/\bar{\phi}_{\textrm{n}} . Setting ϕ n = ϕ ¯ n ​ ( 1 + δ ​ ϕ ^ n ) \phi_{\textrm{n}}=\bar{\phi}_{\textrm{n}}\left(1+\delta\hat{\phi}_{\textrm{n}}\right) and σ = σ ¯ ​ ( 1 + δ ​ σ ^ ) \sigma=\bar{\sigma}\left(1+\delta\hat{\sigma}\right) , where δ ≪ 1 \delta\ll 1 , we arrive at the following linearised equation for the evolution of perturbations in network volume fraction

where Δ ​ f = 2 ​ χ − ϕ ¯ n − 1 − ( 1 − ϕ ¯ n ) − 1 \Delta f=2\chi-\bar{\phi}_{\textrm{n}}^{-1}-(1-\bar{\phi}_{\textrm{n}})^{-1} is the linearised driving force of phase separation. Similarly, we find the linearised stress equation

Substituting the ansatz ϕ ^ n , σ ^ ∝ exp ⁡ ( s ​ t + i ​ k ​ x ) \hat{\phi}_{\textrm{n}},\penalty\ \hat{\sigma}\propto\exp\left(st+ikx\right) , where s s is the growth rate of perturbations with wavenumber k k , we arrive at the dispersion relation

with β = 𝒢 ⁡ ( ϕ n 0 / ϕ ¯ n 2 + 1 / ϕ n 0 ) + 𝒦 ​ ϕ n 0 / ϕ ¯ n 2 \beta=\mathcal{G}\left({\phi_{\textrm{n}}^{0}}/{\bar{\phi}_{\textrm{n}}^{2}}+{1}/{\phi_{\textrm{n}}^{0}}\right)+\mathcal{K}{\phi_{\textrm{n}}^{0}}/{\bar{\phi}_{\textrm{n}}^{2}} a rescaled stiffness, and α = ℓ ​ ϕ n 0 / ϕ ¯ n \alpha=\ell\phi_{\textrm{n}}^{0}/\bar{\phi}_{\textrm{n}} a rescaled non-locality scale. If s ⁡ ( k ) > 0 s(k)>0 , a uniformly swollen network will be unstable to perturbations of wavenumber k k . As such, the homogeneous base state is only stable if s < 0 s<0 for all k k . From equation ( 16 ) , we see that the interfacial ( k 4 k^{4} ) term is always stabilising, and dominates at large k k . The elastic contribution ( β \beta term) is also stabilising for all wavenumbers, and thus acts to inhibit the onset of phase separation. In contrast, the thermodynamic driving force may be either stabilising or destabilising depending on the sign of Δ ​ f \Delta f .

Depending on the relative magnitudes of Δ ​ f \Delta f , β \beta , and α \alpha , we identify four distinct functional forms for s ⁡ ( k ) s(k) , labelled as cases 1 to 4 in figure 2 . Case 1 occurs when s ′ ​ ( k = 0 ) = Δ ​ f − β > 0 s^{\prime}(k=0)=\Delta f-\beta>0 , and corresponds to the classical spinodal instability. In case 2, s ′ ​ ( k = 0 ) < 0 s^{\prime}(k=0)<0 , but s > 0 s>0 for some compact band of wavenumbers k ∈ [ k 1 , k 2 ] k\in[k_{1},k_{2}] . In this case, we expect instabilities to arise at a well-defined finite length scale. We refer to this possibility as the ‘patterned instability’. For both case 3 and 4, s < 0 s<0 for all k k , and so the homogeneous base state is stable. However, s ⁡ ( k ) s(k) may still have a local maximum away from s = 0 s=0 (case 3), thus providing a length scale that is less stable than neighbouring modes. In a noisy system, this mode may be able to induce an instability and nucleate phase-separated domains. In sections 4.1 and 5.1 below, we use the instability criteria derived here to reveal how the onset of these instabilities depends on different model parameters, for both local ( section 4.1 ) and non-local ( section 5.1 ) elasticity laws.


## 4 Phase separation with local elasticity

Before investigating the predictions of our full model, we first focus on the limiting case of local elasticity ( ℓ = 0 \ell=0 ), to compare to the results of previous studies. Previous results have shown that elasticity can suppress phase separation entirely ( Wei et al. 2020 ; Kothari and Cohen 2020 ; Hennessy et al. 2020 ; Paulin et al. 2022 ) , limit the final size of phase-separated domains ( Vidal-Henriquez and Zwicker 2020 ; Vidal-Henriquez and Zwicker 2021 ; Wei et al. 2020 ) , and decrease the rate of post-separation coarsening ( Onuki and Puri 1999 ) .


## 4.1 Elasticity inhibits the onset of phase separation

To begin, we use the linear stability analysis presented in section 3 to identify regions of the parameter space in which we expect a homogeneous mixture with network fraction ϕ ¯ n \bar{\phi}_{\textrm{n}} to phase separate. For a local elasticity law, the dispersion relation (equation 16 ) simplifies to s ⁡ ( k ) = ( Δ ​ f − β ) ​ k 2 − k 4 s(k)=(\Delta f-\beta)k^{2}-k^{4} . As such, only case 1 (classical spinodal instability) and case 4 (stable homogeneous state) of those identified in section 3 are possible.

For local elasticity, the spinodal curve is then defined by Δ ​ f = β \Delta f=\beta . When 𝒢 , 𝒦 = 0 \mathcal{G},\mathcal{K}=0 ( β = 0 \beta=0 ; no elasticity), the standard Flory–Huggins spinodal 2 ​ χ = ϕ ¯ n − 1 + ( 1 − ϕ ¯ n ) − 1 2\chi=\bar{\phi}_{\textrm{n}}^{-1}+(1-\bar{\phi}_{\textrm{n}})^{-1} is recovered. Inside the spinodal curve, a homogenous mixture will be unstable to small perturbations and phase separate into domains of high and low network fraction. As the impact of elasticity increases (increasing 𝒢 , 𝒦 \mathcal{G},\mathcal{K} ), the size of the spinodal region decreases ( figure 3 A). Consistent with previous results ( Wei et al. 2020 ; Vidal-Henriquez and Zwicker 2020 ; Hennessy et al. 2020 ; Paulin et al. 2022 ) , the additional energetic cost associated with deforming the elastic network inhibits the onset of phase separation. Note that the asymmetry of the spinodal curve about ϕ ¯ n = 0.5 \bar{\phi}_{\textrm{n}}=0.5 results from taking the initial homogeneous network to be swollen relative to the reference state ( ϕ ¯ n < ϕ n 0 \bar{\phi}_{\textrm{n}}<\phi_{\textrm{n}}^{0} ), therefore providing a bias away from small network fractions. Figure 3 B shows the spinodal curve as a function of elastic moduli 𝒢 , 𝒦 \mathcal{G},\mathcal{K} and interaction parameter χ \chi , highlighting that phase separation is strongly inhibited at large stiffness.


## 4.2 A stiffer network leads to fewer droplets

To study the time evolution of the mixture predicted by our model, we now perform numerical simulations of equations ( 5 ) –( 13 ) with ℓ = 0 \ell=0 . Figure 4 A shows example simulation results for both a soft (top) and stiff (bottom) network. In both cases, a homogeneous mixture spontaneously phase separates into distinct solvent-rich (droplet; ϕ n ∼ 0 \phi_{\textrm{n}}\sim 0 ) and network-rich ( ϕ n ∼ 1 \phi_{\textrm{n}}\sim 1 ) domains, via the classical spinodal instability. Over time, these domains then coarsen, with the number of droplet domains decreasing ( Figure 4 B). Although coarsening is exponentially slow in 1D, we expect the eventual steady state to consist of a single droplet to minimise total interfacial area.

We find that for a stiff network, mean droplet size is generally slightly larger than for a soft network. However, this size difference is counteracted by a vastly smaller total number of droplets in the stiff case, reconciling the expectation that the total volume of solvent droplet in the system is smaller for a stiffer material. Figure 4 B shows the mean droplet number calculated from many simulations for different elastic moduli 𝒢 , 𝒦 \mathcal{G},\mathcal{K} . We find that the coarsening rate appears relatively insensitive to stiffness, but that the onset of phase separation is slightly delayed for stiffer networks. The initial droplet spacing is set by the spinodal wavenumber k ∗ k_{*} , which can be predicted from the most unstable wavenumber (largest s s ) of the linear stability analysis. Figure 3 B shows k ∗ k_{*} as a function of stiffness for fixed ϕ ¯ n \bar{\phi}_{\textrm{n}} and χ \chi . We see that k ∗ k_{*} decreases with increasing 𝒢 , 𝒦 \mathcal{G},\mathcal{K} , implying that droplets will be more spaced out, hence leading to fewer droplets, in line with the observations from both our numerical simulations and previous studies.


## 5 Phase separation with non-local elasticity

Next, we explore the additional impact of non-local elasticity on phase separation by studying our full model, via both linear stability analysis and numerical simulations. These results extend the work of Qiang et al. 2024 by considering the full temporal evolution of the network–solvent mixture.


## 5.1 Phase plane reveals different modes of instability

Using our linear stability analysis, we now identify the stable and unstable regions of the parameter space for the non-local model ( figure 5 ). As for a local elastic response, we see that increasing network stiffness increases the stability of the mixture, and hence inhibits the onset of phase separation. In contrast to the local elastic case, however, the inclusion of non-local elasticity allows for two distinct modes of instability, as identified in section 3 . When s ′ ​ ( k = 0 ) > 0 s^{\prime}(k=0)>0 (case 1), all sufficiently long wavelengths are unstable to perturbations, resulting in classical spinodal decomposition. The boundary of the region in which this instability occurs is marked by the black curves in figure 5 . When s ′ ​ ( k = 0 ) < 0 s^{\prime}(k=0)<0 (case 2), a discrete band of unstable wavenumbers is now possible, with large wavelength modes now stable. In addition to the classical macroscopic spinodal identified in section 4 , we can thus also identify a ‘patterned’ spinodal region ( figure 5 ; blue line) that corresponds to this case. A homogeneous state is then unstable to perturbations if it is inside either the classical or patterned spinodals.

As stiffness 𝒢 , 𝒦 \mathcal{G},\mathcal{K} increases, the size of the macroscopic spinodal region decreases significantly, but the size of the ‘patterned region’ between the macroscopic (black line) and patterned (blue line) spinodals increases. Non-local elastic effects thus increase the range of parameters for which the homogeneous state is unstable, promoting phase separation relative to local elasticity. Increasing the non-locality length ℓ \ell amplifies this effect ( figure 5 B) by further expanding the boundary of the patterned spinodal.

Figure 5 B also shows the most unstable wavelength k ∗ k_{*} predicted by the linear stability analysis as a function of stiffness, for fixed χ \chi and ϕ ¯ n \bar{\phi}_{\textrm{n}} . A notable feature of this result is that k ∗ k_{*} remains finite at the boundary of the patterned region. This feature is generically true for all points along the patterned spinodal. In contrast, k ∗ = 0 k_{*}=0 where the boundary of the unstable region is defined by the macroscopic spinodal (both for local and non-local elasticity). Finite k ∗ k_{*} at the spinodal implies that a continuous quench across this boundary will preferentially induce a finite wavelength instability. This result raises the possibility of a continuous phase transition across the patterned spinodal, as predicted previously via an equilibrium approach ( Qiang et al. 2024 ) .


## 5.2 Non-local elasticity leads to arrested coarsening

To investigate the long term dynamics of a phase separating mixture, we now turn to numerical simulations of our model. We simulate equations ( 5 ) –( 13 ) up until a fixed end time t end t_{\textrm{end}} , starting from an initial condition corresponding to a homogenous mixture superimposed with small random perturbations. Figure 6 shows the spatial distribution of network fraction ϕ n \phi_{\textrm{n}} and elastic stress σ \sigma at the end time of our simulations for various values of the non-locality length ℓ \ell . Note that each plot shows only a small snapshot of the full simulation domain.

For ℓ = 0 \ell=0 (local elastic limit), we find phase-separated domains of alternating high and low ϕ n \phi_{\textrm{n}} with irregular size and spacing. If simulations were run for a longer time, we would expect these domains to continue to coarsen to the thermodynamic equilibrium of a single domain. Since coarsening is exponentially slow in 1D, we instead choose to end our simulations at t end t_{\textrm{end}} before this final state is reached, and highlight the fact that no regular patterned structure is present in this case. We also note that σ \sigma correlates exactly with ϕ n \phi_{\textrm{n}} , with regions of low network fraction corresponding to high tensile stress. In regions of large ϕ n \phi_{\textrm{n}} , the elastic stress is relatively much smaller, but still in tension since the initial condition corresponds to a highly swollen network relative to the relaxed network fraction ϕ n 0 = 1 \phi_{\textrm{n}}^{0}=1 . For ℓ = 1 \ell=1 and ℓ = 5 \ell=5 , however, we find a regular periodic, or patterned, state at t = t end t=t_{\textrm{end}} , which does not evolve further with time. Here, the non-local elastic contribution spreads the elastic stress over a finite spatial width, leading to much smaller variations in σ \sigma than those observed for ϕ n \phi_{\textrm{n}} . As ℓ \ell increases further, the stress becomes increasingly uniform, and so the pattern length scale increases. In this case, our simulations have reached a steady state by the end of the simulation time, and do not coarsen further.

Figure 7 shows ϕ n \phi_{\textrm{n}} (top) and σ \sigma (bottom) as functions of space and time for different elastic stiffness at fixed non-locality length ℓ = 2 \ell=2 . As before, the results presented here represent a small snapshot of the full simulation domain. At early times, we see that phase separation initiates at the spinodal length scale, forming many small droplets of low network fraction. Initial phase separation is then followed by partial coarsening, with large droplets growing at the expense of small droplets. Eventually, however, coarsening is completely arrested and the system reaches a steady patterned state. This patterned state also persists for much longer simulation times than those presented here. The same phenomenology is observed for all value of elastic stiffness 𝒢 , 𝒦 \mathcal{G},\mathcal{K} , but a larger stiffness results in a smaller pattern length scale. We denote the pattern length scale that emerges from these simulations by L patt L_{\textrm{patt}} . We note that the value of L patt L_{\textrm{patt}} is robust to variations in the size of the simulation domain, indicating that this is an energetically selected length scale, rather than being set by the finite size of our simulations.

To analyse the dependence of the emergent pattern length scale on different model parameters, we now repeat our simulations for 100 100 sets of different realisations of the random perturbations applied to the initial condition. Figure 8 A shows the mean size of droplet domains R ¯ \bar{R} as a function of time. As in figure 7 , we see that initial coarsening is eventually arrested, with the mean droplet size then remaining constant. In contrast to the spinodal length scale (as discussed in section 4.2 ), we find that a stiff network (large 𝒢 , 𝒦 \mathcal{G},\mathcal{K} ) leads to a smaller pattern length scale than a soft network (small 𝒢 , 𝒦 \mathcal{G},\mathcal{K} ), and thus a smaller mean droplet size and larger droplet count. We also observe that a larger stiffness leads to earlier arrest of coarsening. For extremely soft networks, a steady patterned state is not reached within the timeframe of our simulations. For sufficiently large stiffness such that the system is initialised in the patterned region identified in section 5.1 , we find that the mixture immediately phase separates into the patterned state and thus does not coarsen at all. Figure 8 B highlights the dependence of L patt L_{\textrm{patt}} on stiffness explicitly. Although our results show L patt L_{\textrm{patt}} decreasing with stiffness, we note that this dependence is weaker than the square root scaling predicted by previous equilibrium theories ( Qiang et al. 2024 ; Mannattil et al. 2024 ) . We hypothesise that this discrepancy could result from simulations becoming trapped in a non-equilibrium patterned state, due to the finite system size and periodic boundary conditions. We also repeat our simulations for different values of the interaction parameter χ \chi . For all values of χ \chi we see the same qualitative behaviour, but with smaller values of χ \chi resulting in a larger pattern length scale ( figure 8 B).


## 6 Conclusions

Recent experiments with synthetic polymer gels, as well as potential applications to biomolecular condensates, have fuelled significant interest in elastically mediated fluid–fluid phase separation. The presence of a confining elastic network that is permeated by a fluid mixture induces an additional energetic cost to the phase separation of this mixture, and can hence inhibit the onset of phase separation altogether. Further recent experiments have shown that when phase-separated domains are on the scale of network heterogeneities, they can take on a regular pattern structure with a well-defined length scale that does not coarsen over time.

In this manuscript, we have developed a poromechanical phase-field model that describes this phenomenon by considering a non-local elastic response to network deformation. We have used linear stability analysis of our model to identify the parameters for which phase separation can occur in such a system, and to explore the conditions under which elasticity can inhibit phase separation. Numerical simulations of our model reveal that non-local effects are key for arresting phase separation and inducing the formation of a patterned phase. We find that phase separation initialises at small length scales determined by the most unstable mode of the system. The resulting phase-separated mixture then partially coarsens to an equilibrium length scale that depends on the network stiffness. In the absence of non-locality, the mixture instead coarsens completely towards a final state consisting of a single pair of phase-separated domains.

Our modelling approach utilises a large-deformation poromechanical framework that allows simulation of the dynamics of the process, building on the equilibrium approach previously developed by Qiang et al. 2024 . Compared to the similar recent simulations of Oudich et al. 2025 , our model uses a fully non-linear description of the deformation kinematics, and considers non-local contributions to all components of the elastic energy. In order to quantitatively compare the predictions of our model to experimental results, it will be essential to generalise the non-local elastic stress law described here to multiple spatial dimensions and more complex network rheologies ( Fernández-Rico et al. 2025 ) . Nevertheless, the modelling effort and analysis presented here represents an important step towards understanding this physically and conceptually complex system.


## Conflicts of interest

There are no conflicts to declare.


## Data availability

MATLAB codes used to generate the results presented in this manuscript are available at Zenodo via https://doi.org/10.5281/zenodo.16813489 .


## Acknowledgements

The authors thank Filipe Thewes for helpful discussions about non-local interactions, and gratefully acknowledge funding from the Max Planck Society and the European Union (ERC, EmulSim, 101044662).


## Appendix A Derivation of non-local stress law in differential form

For a Neo-Hookean–style non-local energy density of the form

the elastic stress is given in integral form as

where J ~ = ∫ J ′ ​ g ξ ​ d ​ X \tilde{J}=\int J^{\prime}g_{\xi}\textrm{d}X . For the convolution kernel g ξ = exp ( − | X | / ξ ) / 2 ξ g_{\xi}=\exp({-|{X}|/\xi})/2\xi , it is possible to reformulate equation ( A.2 ) in a differential form. First, we split the elastic stress into two parts such that σ = σ ′ − σ ∗ \sigma=\sigma^{\prime}-\sigma^{*} , where

and

Focussing first on σ ′ \sigma^{\prime} , it is then convenient to split the integral in equation ( A.3 ) into two parts,

where g ξ − = exp ( − ( X − X ′ ) / ξ ) / 2 ξ g_{\xi}^{-}=\exp({-(X-X^{\prime})/\xi})/2\xi and g ξ + = exp ( − ( X ′ − X ) / ξ ) / 2 ξ g_{\xi}^{+}=\exp({-(X^{\prime}-X)/\xi})/2\xi . Differentiating equation ( A.5 ) with respect to X X and using that g ξ ± ​ ( 0 ) = 1 / 2 ​ ξ g_{\xi}^{\pm}(0)=1/2\xi , we then find

and hence

Similarly,

and therefore

Inserting the definition of σ ′ \sigma^{\prime} and rearranging, we thus find

Repeating this procedure for equation ( A.4 ) correspondingly yields

Given σ ′ \sigma^{\prime} and σ ∗ \sigma^{*} from equations ( A.10 ) and ( A.11 ), the total elastic stress is then σ = σ ′ − σ ∗ {\sigma=\sigma^{\prime}-\sigma^{*}} .


## References

21