## Radially symmetric transition-layer solutions in mass-conserving reaction-diffusion systems with bistable nonlinearity Thanks: Corresponding author: Xiaoqing He, Email: xqhe@cpde.ecnu.edu.cn

Mass-conserving reaction-diffusion (MCRD) systems are widely used to model phase separation and pattern formation in cell polarity, biomolecular condensates, and ecological systems. Numerical simulations and formal asymptotic analysis suggest that such models can support stationary patterns with sharp internal interfaces. In this work, we establish for a general class of bistable MCRD systems the existence of nonconstant radially symmetric stationary solutions with a single internal transition layer on an N N -dimensional ball, for general spatial dimension N N . Our approach incorporates the global mass constraint directly into a refined matched-asymptotic framework complemented by a uniform spectral/linear analysis. Beyond mere existence, our framework yields arbitrarily high-order asymptotic approximations of the constructed solutions together with quantitative uniform error estimates, which provides a quantitative higher-dimensional theory of transition-layer patterns in MCRD systems and a rigorous justification for their use in modeling phase separation and pattern formation in biological and ecological settings.


## 1. Introduction and Statement of Results


## 1.1. Mass-conserving reaction-diffusion system

Pattern formation is a fundamental phenomenon underlying a wide range of processes in biological development and ecological systems. Over the past several decades, various theoretical frameworks have been proposed to elucidate the mechanisms driving such self-organized dynamics. Among these, mass-conserving reaction-diffusion (MCRD) systems have emerged as a powerful paradigm for studying pattern formation in systems where the total quantity of certain chemical species is conserved. A pioneering contribution in this direction was made by Otsuji et al. [ 33 ] and Ishihara et al. [ 18 ] in 2007, who demonstrated that MCRD systems can successfully capture the spatiotemporal dynamics of cell polarity. Subsequently, in 2008, Mori et al. [ 27 ] proposed a related two-component MCRD model with a distinct form of reaction term to further investigate cell polarization. In dimensionless form, their one-dimensional system reads:

where u ⁡ ( x , t ) u(x,t) and v ⁡ ( x , t ) v(x,t) denote the concentrations of two interconverting chemical species. The diffusion coefficients ε 2 \varepsilon^{2} (for u u ) and d d (for v v ) satisfy 0 < ε 2 ≪ d 0<\varepsilon^{2}\ll d ; for instance, Mori et al. [ 28 ] considered ε ≈ 0.03 \varepsilon\approx 0.03 and d ≈ 0.1 d\approx 0.1 . The nonlinear function f ⁡ ( u , v ) f(u,v) models the interconversion from v v to u u and is assumed to be bistable in u u for fixed v v . A canonical example [ 27 , 28 ] is

where γ , δ > 0 \gamma,\delta>0 satisfy γ > 8 ​ δ \gamma>8\delta to ensure bistability. Using formal asymptotic analysis combined with a wave-pinning argument and numerical computations, the authors of [ 28 ] showed that the MCRD system ( 1.1 ) supports propagating traveling fronts that eventually arrest to form stationary internal interfaces. Related work by Gomez et al. [ 13 ] further explored wave-pinning behavior via analysis of the associated shadow system of ( 1.1 ).

Building upon these foundations, Frey’s group [ 14 , 15 , 4 , 5 ] applied two-component MCRD frameworks to investigate mechanisms of intracellular pattern formation, including cell polarization. Siteur et al. [ 39 ] applied MCRD models to describe vegetation patterns in ecosystems. These studies, although primarily focused on modeling and applications rather than rigorous mathematical analysis, highlight the broad applicability of MCRD systems across diverse fields, ranging from cellular dynamics to ecological pattern formation. In parallel, mass-conserving structures also arise in epidemic reaction-diffusion models [ 2 , 7 , 8 , 34 , 35 ] , where the authors focus primarily on thresholds (e.g., basic reproduction numbers) and equilibrium stability rather than spatial pattern formation.

More recently, experimental studies of biomolecular condensates—a class of mesoscale liquid-liquid phase-separated structures—have provided new biological motivation for MCRD modeling. In particular, the authors of [ 24 ] proposed a data-driven MCRD model to describe phase separation phenomena arising in dsDNA-protein interactive co-condensates. In this setting, u ⁡ ( x , t ) u(x,t) and v ⁡ ( x , t ) v(x,t) denote the concentrations of dsDNA-bound protein and free protein, respectively. Experimental measurements [ 23 , 24 ] show that the diffusion coefficient of free protein v v is approximately 18.0 ± 1.1 ​ μ ​ m 2 / s 18.0\pm 1.1\,\mu\text{m}^{2}/\text{s} , whereas that of the dsDNA-bound protein u u is only about 5.1 × 10 − 5 5.1\times 10^{-5} times as large, thereby revealing a pronounced multiscale diffusion hierarchy. Furthermore, the rapid reaction kinetics converting v v to u u , governed by biochemical interactions, renders the system strongly reaction-dominated. Motivated by these experimental evidence and observations, we propose the following generalized MCRD system:

where Ω ⊂ ℝ N \Omega\subset\mathbb{R}^{N} ( N ≥ 1 ) (N\geq 1) is a bounded smooth domain, Δ \Delta is the Laplace operator, and ∂ ν := ν ⋅ ∇ \partial_{\nu}:=\nu\cdot\nabla denotes the outward normal derivative on ∂ Ω \partial\Omega . Here, 0 < ε ≪ 1 0<\varepsilon\ll 1 and D > 0 D>0 are dimensionless parameters that characterize the relative timescales of diffusion and reaction. Setting D = d / ε D=d/\varepsilon recovers the classical scaling in ( 1.1 ). Thus one may regard ( 1.3 ) as a generalized MCRD system that reduces to ( 1.1 ) under this scaling. Moreover, allowing D D to range from O ⁡ ( 1 ) O(1) to O ⁡ ( 1 / ε ) O(1/\varepsilon) provides a mathematically unified framework that connects the biologically motivated multiscale model ( 1.3 ) with the canonical MCRD model ( 1.1 ); see Remark (d) at the end of this section.

Crucially, for any classical solution ( u ⁡ ( x , t ) , v ⁡ ( x , t ) ) (u(x,t),v(x,t)) of ( 1.3 ), the total mass is conserved:

a defining feature that distinguishes MCRD systems from classical non-mass-conserving reaction-diffusion (non-MCRD) systems. This nonlocal mass constraint poses a major analytical difficulty: it couples local dynamics to a global integral condition, obstructing a direct use of matched-asymptotic, spectral techniques and many other methods developed for classical (non-MCRD) singular perturbation problems. Therefore, despite substantial advances in the modeling of MCRD systems for pattern formation in biological and ecological contexts, establishing a rigorous general existence and stability theory for patterned stationary solutions in MCRD systems is a challenging problem.

Our goal in this work is to construct patterned stationary solutions to system ( 1.3 ) that exhibit internal transition layers, for 0 < ε ≪ 1 0<\varepsilon\ll 1 and D > 0 D>0 , under a prescribed mass constraint . Specifically, we consider the steady-state problem:

subject to the mass constraint

where M > 0 M>0 denotes the prescribed averaged total mass.

It is straightforward to verify that system ( 1.4 ) is equivalent to the following reformulated system:

Let ( u , v ) (u,v) be a classical solution of ( 1.6 ) satisfying the mass constraint ( 1.5 ). The Neumann boundary condition then implies that

which, together with ( 1.5 ), yields the identity

where the nonlocal operator 𝒮 ε ​ [ u ] \mathcal{S}^{\varepsilon}[u] is defined by

Substituting ( 1.7 ) into the first equation of ( 1.6 ), we see that u u satisfies the following nonlocal elliptic scalar equation:

In summary, under the mass constraint ( 1.5 ), system ( 1.4 ) is equivalent to the nonlocal scalar elliptic problem ( 1.9 ). More precisely, a pair ( u , v ) (u,v) is a classical solution of ( 1.4 ) satisfying ( 1.5 ) if and only if u u is a classical solution of ( 1.9 ) and v v is given by ( 1.7 ). This equivalence reduces the construction of nonconstant solutions of ( 1.4 ) under ( 1.5 ) to the analysis of the nonlocal scalar equation ( 1.9 ).

We now proceed to introduce the structural assumptions on the nonlinear reaction term f ⁡ ( u , v ) f(u,v) . Throughout this paper, we assume that the nonlinear reaction term f ⁡ ( u , v ) f(u,v) satisfies the following conditions:

( Bistability ). The function f ⁡ ( u , v ) f(u,v) is smooth ( C ∞ C^{\infty} ) on ℝ 2 \mathbb{R}^{2} , and there exist two constants v ¯ < v ¯ \underline{v}<\overline{v} such that for each fixed v ∈ ( v ¯ , v ¯ ) v\in(\underline{v},\overline{v}) , the equation f ⁡ ( u , v ) = 0 f(u,v)=0 has exactly three distinct real roots denoted by h − ​ ( v ) < h 0 ​ ( v ) < h + ​ ( v ) h^{-}(v)<h^{0}(v)<h^{+}(v) . Moreover,

( Transversality ). For each v ∈ ( v ¯ , v ¯ ) v\in(\underline{v},\bar{v}) , the following inequality holds:

( Mass Balance Condition ). For each v ∈ ( v ¯ , v ¯ ) v\in(\underline{v},\bar{v}) , define the function

There exists a v ∗ ∈ ( v ¯ , v ¯ ) v^{\ast}\in(\underline{v},\bar{v}) such that

We remark that condition (A2) ensures the local asymptotic stability of the spatially homogeneous steady states ( u , v ) ≡ ( h ± ​ ( v ) , v ) (u,v)\equiv(h^{\pm}(v),v) of system ( 1.3 ) for all v ∈ ( v ¯ , v ¯ ) v\in(\underline{v},\bar{v}) . Rigorous justifications of this stability result can be found in [ 28 , 13 ] .

In biological applications, the quantities u u and v v often represent concentrations of chemical species and are typically required to be positive. However, our analysis does not impose positivity constraints on u u and v v , and the mathematical framework remains valid even when u u and v v take nonpositive values.

In the one-dimensional case, the authors [ 21 , 17 ] proved the existence of stationary solutions with an internal transition layer for the MCRD system ( 1.1 ), where the u u -component undergoes a jump across a thin layer. Technically, they used an intrinsic patching/gluing construction by introducing an a priori unknown matching point x ( ε ) ∈ ( 0 , 1 ) x^{(\varepsilon)}\in(0,1) and decompose the interval into ( 0 , x ( ε ) ) (0,x^{(\varepsilon)}) and ( x ( ε ) , 1 ) (x^{(\varepsilon)},1) . They then solved the boundary value problems on each subinterval and enforce C 1 C^{1} -matching at x = x ( ε ) x=x^{(\varepsilon)} , together with the global mass constraint via the Implicit Function Theorem.

The authors claimed in [ 21 , Remark 2.2] that one can obtain a k k -th order approximation of the solutions for any k k . However, extending the construction in [ 21 , Theorem 2.1] to higher orders does not appear to be straightforward: one would need to carry out careful recursive computations to verify that the Implicit Function Theorem argument closes at each order, which is a substantial task. For instance, without an explicit understanding of the higher-order terms, it is unclear whether the nondegeneracy condition h + ​ ( v ) − h − ​ ( v ) ≠ 0 h^{+}(v)-h^{-}(v)\neq 0 alone suffices to match an arbitrary higher-order expansion.

In this work, we develop a unified high-order expansion framework for the general MCRD system ( 1.3 ) on N N -dimensional balls, thereby overcoming the above challenges. By incorporating the global mass constraint into a refined matched-asymptotic construction and establishing a uniform spectral/linear theory for the resulting singularly perturbed operators, we derive arbitrarily high-order asymptotic approximations for radially symmetric single transition-layer solutions with explicit error bounds. These approximations and error controls will serve as the principal technical ingredient in the stability analysis of the solutions constructed here, which will be carried out in forthcoming work.


## 1.2. Assumptions and statement of main result

In this subsection, we state the precise statement of our result concerning existence of stationary single transition-layer solutions to the MCRD system ( 1.3 ) with prescribed total mass, i.e., solutions to ( 1.4 )-( 1.5 ) or equivalently ( 1.9 ).

For our purposes, we assume throughout the remainder of this paper that

where B r := B r ​ ( 0 ) B_{r}:=B_{r}(0) denotes the ball of radius r > 0 r>0 centered at the origin in ℝ N \mathbb{R}^{N} . Our objective is to construct radially symmetric solutions to system ( 1.4 ) subject to the mass constraint ( 1.5 ) in Ω \Omega . Specifically, we aim to construct solutions exhibiting an internal transition layer across the sharp interface

where R ∗ ∈ ( 0 , 1 ) R_{*}\in(0,1) denotes the interface location parameter. As will be derived in ( 1.10 ), R ∗ R_{*} is determined in the course of the construction, by the prescribed averaged total mass M M in ( 1.5 ). For notational convenience, we set

to denote the admissible range of the parameter M M throughout the paper.

Since we work with radially symmetric solutions, we shall, by a slight abuse of notation, write g ⁡ ( x ) g(x) and g ⁡ ( r ) g(r) interchangeably for a radial function g g in Ω \Omega , where r = | x | r=|x| .

The main result of this work is stated below.

Assume that conditions (A1)-(A3) hold. Then, for each given

there exists a constant ε ¯ = ε ¯ ​ ( M , D 0 ) > 0 \bar{\varepsilon}=\bar{\varepsilon}(M,D_{0})>0 such that system ( 1.4 ) admits a family of spherically symmetric classical solutions ( u ε , D ​ ( r ) , v ε , D ​ ( r ) ) (u^{\varepsilon,D}(r),v^{\varepsilon,D}(r)) defined for ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} and satisfying the mass constraint

Moreover, these solutions satisfy the following properties:

There exists a constant C = C ⁡ ( M , D 0 , ε ¯ ) > 0 C=C(M,D_{0},\bar{\varepsilon})>0 such that

For each η > 0 \eta>0 , there exist two constants K = K ⁡ ( η ) > 0 K=K(\eta)>0 and ε ¯ ′ = ε ¯ ′ ​ ( M , D 0 , η ) ∈ ( 0 , ε ¯ ] \bar{\varepsilon}^{\prime}=\bar{\varepsilon}^{\prime}(M,D_{0},\eta)\in(0,\bar{\varepsilon}] such that

where

v ε , D ​ ( x ) = 𝒮 ε ​ [ u ε , D ] − ε D ​ u ε , D ​ ( x ) v^{\varepsilon,D}(x)=\mathcal{S}^{\varepsilon}[u^{\varepsilon,D}]-\frac{\varepsilon}{D}u^{\varepsilon,D}(x) and

Theorem 1.1 has several immediate consequences, which we summarize below.

Part (ii) of Theorem 1.1 establishes that the transition layer which separates the high- and low-concentration regions in u ε , D u^{\varepsilon,D} , is sharply localized near the interface r = R ∗ r=R_{*} , which provides directly an accurate characterization of a width of order O ⁡ ( ε ) O(\varepsilon) for the transition layer.

Furthermore, for any fixed δ > 0 \delta>0 with δ < min ⁡ { R ∗ , 1 − R ∗ } \delta<\min\{R_{*},1-R_{*}\} , we see the uniform convergence

By setting D = d / ε D=d/\varepsilon in Theorem 1.1 , one recovers the canonical MCRD scaling considered in [ 27 , 28 ] , thereby obtaining a family of spherically symmetric stationary solutions to system ( 1.1 ).

It is also worth mentioning that the one-dimensional case N = 1 N=1 is considerably simpler; see, for example, the expansion in ( 2.17 ) (2.17) below. The main reason is that for N ≥ 2 N\geq 2 (in the radially symmetric setting) one must deal with differential operators with variable coefficients, such as the radial Laplacian u r ​ r + N − 1 r ​ u r u_{rr}+\frac{N-1}{r}u_{r} , which significantly complicates the analysis. Furthermore, as discussed in Subsection 1.1, deriving high-order asymptotic approximations together with uniform, explicit error bounds requires rather involved computations. It is therefore advantageous to work with a single global closed-form expression, as in our approach.

To establish Theorem 1.1 , we exploit the equivalence shown at the end of the preceding subsection: it suffices to establish the following existence result for the nonlocal scalar problem ( 1.9 ) and then set

Assume that conditions (A1)-(A3) hold. Then, for each given

there exists a constant ε ¯ = ε ¯ ​ ( M , D 0 ) > 0 \bar{\varepsilon}=\bar{\varepsilon}(M,D_{0})>0 such that system ( 1.9 ) admits a family of spherically symmetric classical solutions u ε , D ​ ( r ) u^{\varepsilon,D}(r) defined for ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} . Moreover, these solutions satisfy the following properties:

There exists a constant C = C ⁡ ( M , D 0 , ε ¯ ) > 0 C=C(M,D_{0},\bar{\varepsilon})>0 such that

For each η > 0 \eta>0 , there exist two constants K = K ⁡ ( η ) > 0 K=K(\eta)>0 and ε ¯ ′ = ε ¯ ′ ​ ( M , D 0 , η ) ≤ ε ¯ \bar{\varepsilon}^{\prime}=\bar{\varepsilon}^{\prime}(M,D_{0},\eta)\leq\bar{\varepsilon} such that

where R ∗ R_{*} is defined as in ( 1.10 ).

Our approach to proving Theorem 1.3 consists of two main steps. First, we construct a family of smooth ( C ∞ C^{\infty} ) radially symmetric approximate solutions to problem ( 1.9 ), characterized by an internal transition layer located near the sharp interface Γ ∗ \Gamma_{*} . These approximate solutions are obtained via matched asymptotic expansions, with particular attention to enforcing the mass constraint ( 1.5 ), which is now encoded in the nonlocal term 𝒮 ε ​ [ u ] \mathcal{S}^{\varepsilon}[u] . In the second step, we apply a contraction mapping argument, after a finite-dimensional spectral reduction (via spectral projection), to perturb the approximate solutions to exact ones for sufficiently small ε > 0 \varepsilon>0 , using a Lyapunov-Schmidt-type decomposition to reduce the problem. Crucial ingredients of the analysis include precise asymptotic matching near the transition layer, careful handling of the nonlocal term 𝒮 ε ​ [ u ] \mathcal{S}^{\varepsilon}[u] —which governs the solvability of the coupled inner-outer system—and sharp spectral estimates for the linearized operator around the approximate solutions.

Finally, we conclude this subsection with a discussion of the modeling insights and broader implications of Theorem 1.1 , with particular emphasis on its connections to phase separation, analytical challenges, and multiscale pattern formation in biological systems.

(a) Theorem 1.1 demonstrates that under general structural assumptions (A1)-(A3), MCRD systems admit spatially nonhomogeneous stationary states characterized by phase separation with a droplet-like interface. Such solutions arise when the averaged total mass M M lies strictly between the two critical thresholds v ∗ + h − ​ ( v ∗ ) v^{*}+h^{-}(v^{*}) and v ∗ + h + ​ ( v ∗ ) v^{*}+h^{+}(v^{*}) . Moreover, varying M M within this interval affects only the volume fraction between the high- and low-concentration regions, through the interface location R ∗ = R ∗ ​ ( M ) R_{*}=R_{*}(M) defined in ( 1.10 ). This agrees qualitatively with experimental findings on liquid-liquid phase separation [ 1 , 3 ] and supports the use of MCRD systems as a theoretical model for biomolecular condensate formation.

(b) Patterned solutions with internal/boundary transition layers or spikes have been extensively studied in classical non-mass-conserving reaction-diffusion (Non-MCRD) systems, e.g., in the following form:

See, for instance, [ 10 , 19 , 25 , 26 , 32 , 40 , 36 ] for results in one spatial dimension, and [ 9 , 16 , 31 , 37 , 38 ] for the multi-dimensional setting. However, the analytical techniques developed in these works do not directly apply to MCRD systems due to the presence of the nonlocal mass constraint ( 1.5 ), which fundamentally alters the structure of the problem by coupling local dynamics to a global integral condition.

(c) A classical theory for pattern formation is Turing instability [ 41 ] , which typically predicts the emergence of spatially periodic patterns via linear instability of homogeneous steady states [ 30 ] . In contrast, MCRD systems often exhibit spatiotemporal coarsening dynamics [ 15 , 18 ] , wherein transient patterns evolve toward polarized states consisting of two distinct phases—a dense phase and a dilute phase. A rigorous understanding of the full dynamical pathway leading to such polarized steady states remains a significant and challenging open problem.

(d) Our generalized MCRD model ( 1.3 ) accommodates a range of scaling regimes through the parameter D D . When D D is treated as independent of ε \varepsilon , the model captures a multiscale hierarchy between diffusion and reaction processes. Alternatively, choosing D = d / ε D=d/\varepsilon recovers the classical scaling used in ( 1.1 ). Given that natural pattern-forming systems often involve widely separated spatial and temporal scales, the flexibility in scaling endowed by MCRD models enables them to serve as a unified cross-scale framework for investigating pattern formation across diverse biological and ecological contexts.

The remainder of the paper is organized as follows. In Section 2, we construct a family of smooth ( C ∞ C^{\infty} ) radially symmetric approximate solutions exhibiting internal transition layers and derive sharp asymptotic estimates. Section 3 develops the spectral analysis of the linearized operator about the approximate solutions. In Section 4 we employ a finite-dimensional spectral reduction together with a contraction mapping argument to obtain exact solutions near the approximate family for sufficiently small ε \varepsilon , thereby proving the main results.


## 2. Construction of the approximate solutions

In this section, we construct a family of smooth, spherically symmetric approximate solutions to problem ( 1.9 ) that exhibit an internal transition layer across the interface Γ ∗ \Gamma_{*} . These approximate solutions can achieve arbitrarily high order of accuracy measured in terms of ε k \varepsilon^{k} for any prescribed k ∈ ℕ k\in\mathbb{N} . The width of the transition layer is of order O ⁡ ( ε ) O(\varepsilon) .


## 2.1. Preliminaries

Under the conditions (A1) and (A3), for each s ∈ ( v ¯ , v ¯ ) s\in(\underline{v},\bar{v}) , we consider the determination of the pair ( Q ⁡ ( z , s ) , c ⁡ ( s ) ) (Q(z;s),c(s)) as the solution to the boundary value problem:

The following result follows from [ 11 ] . See also [ 16 , Proposition 2.3] .

Under the condition (A1) , for each s ∈ ( v ¯ , v ¯ ) s\in(\underline{v},\bar{v}) , the problem ( 2.11 ) has a unique solution ( Q ⁡ ( z , s ) , c ⁡ ( s ) ) (Q(z;s),c(s)) satisfying the following properties:

The function Q ⁡ ( z , s ) Q(z;s) (respectively Q z Q_{z} and Q z ​ z Q_{zz} ) approaches the limit h ± ​ ( s ) h^{\pm}(s) (respectively 0 0 ) at an exponential rate as z → ∓ ∞ z\to\mp\infty , and Q z ​ ( z , s ) < 0 Q_{z}(z;s)<0 for z ∈ ℝ z\in\mathbb{R} .

Then the function c ⁡ ( s ) c(s) is explicitly given by

If in addition, (A3) is satisfied, then


## 2.2. Statements on existence of approximate solutions

We begin by constructing a family of approximate solutions to problem ( 1.9 ) that exhibit internal transition layers. The central result of this section is stated as follows.

Assume that conditions (A1)-(A3) hold. Then for each given M ∈ I v ∗ M\in I_{v^{*}} , there exists a family of smooth ( C ∞ ) (C^{\infty}) radially symmetric functions u k ε , D ​ ( r ) u^{\varepsilon,D}_{k}(r) defined for ε > 0 \varepsilon>0 , D > 0 D>0 and k ∈ ℕ k\in\mathbb{N} such that the following statements hold true:

For each D 0 > 0 D_{0}>0 , k ∈ ℕ k\in\mathbb{N} and η > 0 \eta>0 , there exist two constants K = K ⁡ ( η ) > 0 K=K(\eta)>0 and ε ¯ = ε ¯ ​ ( M , D 0 , k , η ) > 0 \bar{\varepsilon}=\bar{\varepsilon}(M,D_{0},k,\eta)>0 such that

where R ∗ = R ∗ ​ ( M ) R_{*}=R_{*}(M) is defined as in ( 1.10 ).

For each D 0 > 0 D_{0}>0 , ε 0 > 0 \varepsilon_{0}>0 and k ∈ ℕ k\in\mathbb{N} , there exists a constant C k = C k ​ ( M , D 0 , ε 0 ) > 0 C_{k}=C_{k}(M,D_{0},\varepsilon_{0})>0 such that

and

where

Set v k ε , D := 𝒮 ε ​ [ u k ε , D ] − ε D ​ u k ε , D v^{\varepsilon,D}_{k}:=\mathcal{S}^{\varepsilon}[u^{\varepsilon,D}_{k}]-\frac{\varepsilon}{D}u^{\varepsilon,D}_{k} , then

and for each k ∈ ℕ k\in\mathbb{N} ,

Note that the results of Theorem 2.2 can also be reformulated within the framework of system ( 1.4 ), due to the equivalence of system ( 1.4 ) under the mass constraint ( 1.5 ) and problem ( 1.9 ).


## 2.3. Outer and inner expansions

Let u ε u^{\varepsilon} be a radially symmetric solution with an internal transition layer to equation ( 1.9 ), i.e., u ε u^{\varepsilon} satisfies the following equation

Note that we have suppressed the explicit dependence of u ε u^{\varepsilon} on the parameters D D and M M for notational simplicity. Our objective in this subsection is to construct the outer expansion of u ε u^{\varepsilon} in regions away from the interface Γ ∗ = ∂ B R ∗ \Gamma_{*}=\partial B_{R_{*}} and the inner expansion in a neighborhood of Γ ∗ \Gamma_{*} , where R ∗ ∈ ( 0 , 1 ) R_{*}\in(0,1) denotes the interface location parameter and is to be determined during the construction (cf. Proposition 2.6 below).

Let us denote

We first construct the outer expansions U j U^{j} for j ∈ ℕ j\in\mathbb{N} by formally expanding the solution u ε u^{\varepsilon} of ( 2.14 ) into a power series in ε \varepsilon of the form

such that the truncated expansion asymptotically satisfies equation ( 2.14 ) in the outer regions Ω \ Γ ∗ = Ω − ∪ Ω + \Omega\backslash\Gamma_{*}=\Omega^{-}\cup\Omega^{+} , where

and is required to be discontinuous at | x | = R ∗ |x|=R_{*} , thus exhibiting a sharp transition layer across Γ ∗ \Gamma_{*} .

To derive the equations satisfied by U j ​ ( x ) U^{j}(x) , it is necessary to also expand the nonlocal term S ε ​ [ u ε ] S^{\varepsilon}[u^{\varepsilon}] in equation ( 2.14 ), which involves the integral of u ε u^{\varepsilon} , into a formal power series in ε \varepsilon . However, since u ε u^{\varepsilon} is not yet known, this expansion cannot be computed explicitly. To proceed, we formally postulate an expansion of the form

where the coefficients A j A_{j} are constants to be determined in conjunction with the outer and inner expansions of u ε u^{\varepsilon} in Proposition 2.6 below. The expansion ( 2.18 ), when applied to the approximate solution obtained via matched asymptotic expansions, will be shown to hold to arbitrarily high order in ε \varepsilon in Proposition 2.6 . This underscores a key analytical challenge in the construction of approximate solutions to ( 2.14 )—namely, the proper handling of the mass constraint ( 1.5 ) which is now encoded in the nonlocal term 𝒮 ε ​ [ u ε ] \mathcal{S}^{\varepsilon}[u^{\varepsilon}] .

Substituting ( 2.16 ) and ( 2.18 ) into ( 2.14 ) and equating coefficients of like powers of ε \varepsilon , one obtains equations for U ± , j U^{\pm,j} given by

where f u ± , 0 := f u ​ ( U ± , 0 , A 0 ) f_{u}^{\pm,0}:=f_{u}(U^{\pm,0},A_{0}) , f v ± , 0 := f v ​ ( U ± , 0 , A 0 ) f_{v}^{\pm,0}:=f_{v}(U^{\pm,0},A_{0}) and f ± , j ​ ( j ≥ 2 ) f^{\pm,j}(j\geq 2) are given by

Note that f ± , j f^{\pm,j} depends only on ( U ± , k , A k ) (U^{\pm,k},A_{k}) with 0 ≤ k ≤ j − 1 0\leq k\leq j-1 .

Since we are looking for solutions with a sharp internal transition layer across Γ ∗ \Gamma_{*} , in accordance with the condition (A1), we choose

as solution of ( 2.19 )-(i). This implies that f u ± , 0 < 0 f_{u}^{\pm,0}<0 by the condition (A1). Note that an alternative choice of ( 2.20 ) would be U ± , 0 ​ ( x ) ≡ h ± ​ ( A 0 ) U^{\pm,0}(x)\equiv h^{\pm}(A_{0}) in Ω ± \Omega^{\pm} receptively. Then we will obtain a different family of transition layer solutions which is structurally symmetric with our current choice. See Theorem 4.3 below. Then by induction on j ≥ 1 j\geq 1 , we see from ( 2.19 ) that

Therefore, U ± , j ​ ( j ≥ 0 ) U^{\pm,j}~(j\geq 0) is determined by A k A_{k} with 0 ≤ k ≤ j 0\leq k\leq j . Note that U ± , j U^{\pm,j} are constant in Ω ± \Omega^{\pm} for all j ≥ 0 j\geq 0 . Henceforth, for notational convenience, we will use U ± , j U^{\pm,j} to denote either the constant value or the corresponding function defined on Ω ± \Omega^{\pm} , without risk of confusion. The expression of f ± , j f^{\pm,j} ( j ≥ 2 ) (j\geq 2) can now be simplified as

To analyze the sharp transition near the interface Γ ∗ \Gamma_{*} , we introduce the stretched variable z = r − R ∗ ε z=\frac{r-R_{*}}{\varepsilon} . Under this transformation, equation ( 2.14 ) is rewritten as:

We will determine the inner expansions w j w^{j} for j ∈ ℕ j\in\mathbb{N} by formally expanding the solution u ε u^{\varepsilon} of ( 2.23 ) into a power series in ε \varepsilon of the form

such that the truncated expansion asymptotically satisfies ( 2.23 ). Substituting ( 2.24 ) and ( 2.18 ) into ( 2.23 ) and equating coefficients of like powers of ε \varepsilon , we obtain equations for w j w^{j} as follows:

and for j ≥ 1 j\geq 1 ,

where

Note that f j f_{j} depends only on lower order terms w k w^{k} ( 0 ≤ k ≤ j − 1 ) (0\leq k\leq j-1) and A k A_{k} ( 0 ≤ k ≤ j ) (0\leq k\leq j) .

For our purposes, we fix a positive constant d 0 d_{0} throughout this paper such that

The constant d 0 d_{0} depends solely on the nonlinearity f f and is independent of the parameters M M , ε \varepsilon and D D . Hence, in what follows, we shall not explicitly trace the dependence of other quantities on d 0 d_{0} .

After both the outer expansions U j ​ ( x ) U^{j}(x) and the inner expansions w j ​ ( z ) w^{j}(z) are obtained, we will smoothly match them across the interface Γ ∗ \Gamma_{*} using a standard cut-off function technique. To facilitate this matching, we extend the domain of each inner expansions w j w^{j} from ( − R ∗ ε , 1 − R ∗ ε ) \left(-\frac{R_{*}}{\varepsilon},\frac{1-R_{*}}{\varepsilon}\right) to ℝ \mathbb{R} , and require that w j w^{j} satisfies the following exponential matching condition for each j ∈ ℕ j\in\mathbb{N} :

where χ \chi denotes the characteristic function of the set indicated, U ± , j U^{\pm,j} are constants (cf. the comment after ( 2.21 )), c j > 0 c_{j}>0 is some constant to be determined along with w j w^{j} .

We now seek solutions of ( 2.25 ) and ( 2.26 ) under the condition ( 2.29 ).

For equation ( 2.25 ) under the assumption ( 2.29 ), it follows from Proposition 2.1 , ( 2.21 )-(i) and assumption (A3) that we must choose

in order to admit a solution for equation ( 2.25 ), which is given by w 0 ​ ( z ) = Q ⁡ ( z + a 0 , v ∗ ) w^{0}(z)=Q(z+a_{0};v^{*}) , where a 0 ∈ ℝ a_{0}\in\mathbb{R} is a translation parameter to be determined later in Proposition 2.6 . For notational simplicity, we will henceforth write Q ⁡ ( z + a 0 ) Q(z+a_{0}) in place of Q ⁡ ( z + a 0 , v ∗ ) Q(z+a_{0};v^{*}) and set

Since w 0 ​ ( z ) − h ∓ ​ ( v ∗ ) w^{0}(z)-h^{\mp}(v^{*}) , w z 0 ​ ( z ) w^{0}_{z}(z) and w z ​ z 0 ​ ( z ) w^{0}_{zz}(z) decay to zero exponentially as z → ± ∞ z\to\pm\infty by Proposition 2.1 , there exists a constant c 0 = c 0 ​ ( a 0 ) > 0 c_{0}=c_{0}(a_{0})>0 such that

which guarantees that condition ( 2.29 ) holds for j = 0 j=0 .

It follows from ( 2.30 ) and ( 2.21 )-(i) that U 0 U^{0} is now determined as

Next, we solve equation ( 2.26 ) subject to the condition ( 2.29 ). We need to establish a technical lemma as a preparation. We begin with introducing the following Banach space

equipped with the norm

We also define the closed subspace 𝒳 0 ⊂ 𝒳 \mathcal{X}_{0}\subset\mathcal{X} consisting of functions that decay exponentially fast to zero at both infinities:

Define the linear operator L 0 L^{0} by

It is easy to see from ( 2.31 ), ( 2.32 ) and Proposition 2.11 that

We then define the closed subspace of 𝒳 \mathcal{X} :

It inherits the Banach space structure from 𝒳 \mathcal{X} .

It is straightforward to verify that solving equation ( 2.26 ) subject to the boundary condition ( 2.29 ) is equivalent to solving ( 2.26 ) in 𝒳 \mathcal{X} . We now claim

Consider the linear inhomogenouse equation

Then the following statements hold.

The problem ( 2.35 ) has a solution φ ∈ 𝒳 \varphi\in\mathcal{X} if and only if g ∈ [ w z 0 ] ⟂ g\in[w^{0}_{z}]^{\perp} .

The operator L 0 L^{0} has a bounded right inverse

That is, for each g ∈ [ w z 0 ] ⟂ g\in[w^{0}_{z}]^{\perp} , the problem ( 2.35 ) has a unique solution in [ w z 0 ] ⟂ [w^{0}_{z}]^{\perp} , which we denote as φ := ( L 0 ) − 1 ​ g \varphi:=(L^{0})^{-1}g and it satisfies

Moreover,

where C > 0 C>0 is a constant depending only on w 0 w^{0} . In fact, φ \varphi can be explicitly expressed as

where

A similar result to Lemma 2.3 has been obtained in [ 16 , Lemma 3.1] . However, a key distinction in our result is that we state it in a suitable functional framework, which confirms that the constant C C in ( 2.37 ) depends only on w 0 w^{0} and is independent of the inhomogeneity g g . This refinement is crucial for the subsequent analysis, where ( 2.37 ) is applied systematically to monitor parameter dependence across a sequence of estimates.

We first prove Part (i). Assume that g ∈ [ w z 0 ] ⟂ g\in[w^{0}_{z}]^{\perp} . It follows directly from variation of constant formula that φ \varphi defined by ( 2.38 ) satisfies equation ( 2.35 ). By applying L’Hôsptical’s rule repeatedly, we can easily show that

where C ⁡ ( ‖ g ‖ 𝒳 , ‖ w 0 ‖ 𝒳 ) > 0 C(\|g\|_{\mathcal{X}},\|w^{0}\|_{\mathcal{X}})>0 is a constant depending only on the variables indicated. This implies the first identity in ( 2.36 ), which combined with the equation for φ \varphi implies that ( φ z ​ z ) ± ∞ = 0 (\varphi_{zz})_{\pm\infty}=0 . Then it follows from the interpolation inequality that ( φ z ) ± ∞ = 0 (\varphi_{z})_{\pm\infty}=0 . Therefore, φ z , φ z ​ z ∈ 𝒳 0 \varphi_{z},\varphi_{zz}\in\mathcal{X}_{0} . This finishes the proof of ( 2.36 ).

On the other hand, suppose ( 2.35 ) has a solution φ ∈ 𝒳 \varphi\in\mathcal{X} . Since g ∈ 𝒳 g\in\mathcal{X} , w z 0 ∈ 𝒳 0 w^{0}_{z}\in\mathcal{X}_{0} and L 0 ​ w z 0 = 0 L^{0}w^{0}_{z}=0 , multiplying both sides of L 0 ​ φ = g L^{0}\varphi=g by w z 0 w^{0}_{z} and integrating over ℝ \mathbb{R} , using integration by parts, we see that ⟨ g , w z 0 ⟩ = 0 \langle g,w^{0}_{z}\rangle=0 , which implies that g ∈ [ w z 0 ] ⟂ g\in[w^{0}_{z}]^{\perp} . This finishes the proof of Part (i).

To finish the proof for Part (ii), it only remains to prove ( 2.37 ). In fact, it is easy to verify that ( L 0 ) − 1 : [ w z 0 ] ⟂ → [ w z 0 ] ⟂ (L^{0})^{-1}:[w^{0}_{z}]^{\perp}\to[w^{0}_{z}]^{\perp} is a continuous operator with closed graph. Then by the closed graph theorem, there exists a constant C > 0 C>0 depending only on w 0 w^{0} such that

Then it follows from the equation for φ \varphi that ‖ φ z ​ z ‖ 𝒳 ≤ C ​ ‖ g ‖ 𝒳 \|\varphi_{zz}\|_{\mathcal{X}}\leq C\|g\|_{\mathcal{X}} . Now ( 2.37 ) follows from the above two estimates and the interpolation inequality. This finished the proof of the lemma. ∎

Now we are ready to solve equation ( 2.26 ) under the condition ( 2.29 ).

Assume that conditions (A1)-(A3) hold. Let A 0 A_{0} , U 0 U^{0} and w 0 w^{0} be defined by ( 2.30 ), ( 2.33 ) and ( 2.31 ) respectively, where R ∗ ∈ ( 0 , 1 ) R_{*}\in(0,1) is the interface location parameter appearing in the definition of Ω ± \Omega^{\pm} (cf. ( 2.15 )) in ( 2.33 ), and a 0 ∈ ℝ a_{0}\in\mathbb{R} is the free parameter in ( 2.31 ). Then, for each D > 0 D>0 , the following statements hold:

For j = 1 j=1 , the equation ( 2.26 ) admits a solution w 1 ∈ 𝒳 w^{1}\in\mathcal{X} if and only if

where

When condition ( 2.39 ) holds, the corresponding solution w 1 w^{1} can be written explicitly as

where a 1 a_{1} is a free parameter and w ^ 1 = − ( L 0 ) − 1 ​ f 1 ∈ [ w z 0 ] ⟂ \widehat{w}^{1}=-(L^{0})^{-1}f_{1}\in[w^{0}_{z}]^{\perp} .

For each j ≥ 2 j\geq 2 , the equation ( 2.26 ) admits a solution w j ∈ 𝒳 w^{j}\in\mathcal{X} if and only if

where G j − 1 G_{j-1} is a smooth function of the variables indicated and a 0 , ⋯ , a j − 2 a_{0},\cdots,a_{j-2} are the free parameters in the expressions of w 0 , ⋯ , w j − 2 w^{0},\cdots,w^{j-2} respectively. When condition ( 2.41 ) holds, the corresponding solution w j w^{j} can be written explicitly as

where a j a_{j} is a free parameter and w ^ j = − ( L 0 ) − 1 ​ f j ∈ [ w z 0 ] ⟂ \widehat{w}^{j}=-(L^{0})^{-1}f_{j}\in[w^{0}_{z}]^{\perp} .

Furthermore, for each D 0 > 0 D_{0}>0 and j ≥ 1 j\geq 1 , there exists a constant

such that for all D ≥ D 0 D\geq D_{0} ,

Proposition 2.5 implies that, for any prescribed averaged total mass M ∈ I v ∗ M\in I_{v^{*}} and fixed D > 0 D>0 , the construction of outer and inner expansions reduces to determining the interface location parameter R ∗ R_{*} and the “free” parameters a j a_{j} for j ≥ 0 j\geq 0 . Once these quantities are specified, all associated quantities—including the constants A j ​ ( j ≥ 1 ) A_{j}~(j\geq 1) (see ( 2.39 ) and ( 2.41 )), the outer expansions U j ​ ( j ≥ 0 ) U^{j}~(j\geq 0) (see ( 2.21 )) and the inner expansions w j ​ ( j ≥ 0 ) w^{j}~(j\geq 0) (see ( 2.31 ), ( 2.40 ) and ( 2.42 )), can then be determined inductively.

We now proceed to determine the interface location parameter R ∗ ∈ ( 0 , 1 ) R_{*}\in(0,1) and the free parameters a j ∈ ℝ a_{j}\in\mathbb{R} for j ≥ 0 j\geq 0 by constructing an approximate solution built from the outer expansions U j U^{j} and the inner expansions w j w^{j} . To this end, we introduce the following shorthand notation for the outer and inner expansions truncated at order k ∈ ℕ k\in\mathbb{N} :

Next, we select a smooth cutoff function θ ⁡ ( z ) \theta(z) satisfying

Let

We then define the k k -th order approximate solution u k ε , D ​ ( r ) u^{\varepsilon,D}_{k}(r) by smoothly gluing the outer and inner expansions near the interface r = R ∗ r=R_{*} as follows:

Assume that conditions (A1)-(A3) hold. Let A 0 A_{0} be defined by ( 2.30 ). Then, for each given

there are constants, R ∗ = R ∗ ​ ( M ) R_{*}=R_{*}(M) defined by ( 1.10 ), a 0 = a 0 ​ ( M , D ) a_{0}=a_{0}(M,D) , a 1 = a 1 ​ ( M , D , a 0 ) a_{1}=a_{1}(M,D,a_{0}) , ⋯ \cdots , a j = a j ​ ( M , D , a 0 , ⋯ , a j − 1 ) a_{j}=a_{j}(M,D,a_{0},\cdots,a_{j-1}) for all j ≥ 1 j\geq 1 , which are determined inductively together with the following quantities:

the constants A j A_{j} for j ≥ 1 j\geq 1 (cf. ( 2.39 ) and ( 2.41 )),

the outer solutions U j U^{j} for j ≥ 0 j\geq 0 (cf. ( 2.21 )), and

the inner solutions w j w^{j} for j ≥ 0 j\geq 0 (cf. ( 2.31 ), ( 2.40 ) and ( 2.42 )),

such that for any ε > 0 \varepsilon>0 and k ∈ ℕ k\in\mathbb{N} , the following expansion holds:

where 𝒮 ε ​ [ ⋅ ] \mathcal{S}^{\varepsilon}[\,\cdot\,] is defined in ( 1.8 ), u k ε , D u^{\varepsilon,D}_{k} is given by ( 2.47 ), and A k + 2 ε , D A_{k+2}^{\varepsilon,D} is the coefficient of the remainder term which depends only on M M , D D , ε \varepsilon and k k .

Moreover, there hold:

For each D 0 > 0 D_{0}>0 and k ∈ ℕ k\in\mathbb{N} , there exists a constant C k ′ = C k ′ ​ ( M , D 0 ) > 0 C^{\prime}_{k}=C^{\prime}_{k}(M,D_{0})>0 such that

which further implies the uniform bounds

For each ε 0 > 0 \varepsilon_{0}>0 , D 0 > 0 D_{0}>0 and k ∈ ℕ k\in\mathbb{N} , there exists a constant C k = C k ​ ( M , D 0 , ε 0 ) > 0 C_{k}=C_{k}(M,D_{0},\varepsilon_{0})>0 such that

Proposition 2.6 establishes that for each prescribed M ∈ I v ∗ M\in I_{v^{*}} and D > 0 D>0 , the interface location parameter R ∗ R_{*} and the “free” parameters a j ​ ( j ≥ 0 ) a_{j}~(j\geq 0) —along with the associated quantities A j A_{j} , w j w^{j} and U j U^{j} defined in Proposition 2.5 and ( 2.21 )—can all be determined inductively so that the asymptotic expansion ( 2.18 ), when applied to the approximate solution u k ε , D u^{\varepsilon,D}_{k} , holds to any prescribed order k + 1 k+1 in powers of ε \varepsilon , with a remainder term of the form ε k + 2 ​ A k + 2 ε , D \varepsilon^{k+2}A_{k+2}^{\varepsilon,D} . Moreover, the uniform bounds stated in ( 2.49 )-( 2.51 ) guarantee that the outer expansions U j U^{j} , the inner expansions w j w^{j} and the approximate solutions u k ε , D u_{k}^{\varepsilon,D} remain uniformly controlled as ε → 0 \varepsilon\to 0 and D → ∞ D\to\infty . These results provide a solid foundation for the perturbative analysis carried out in subsequent sections to construct exact solutions in a neighborhood of u k ε , D u_{k}^{\varepsilon,D} .

We now prove Propositions 2.5 and 2.6 .

We first prove Part (i) for the case j = 1 j=1 . Then equation ( 2.26 ) with j = 1 j=1 reads L 0 ​ w 1 = − f 1 L^{0}w^{1}=-f_{1} with

By ( 2.32 ), we see that f 1 ∈ 𝒳 f_{1}\in\mathcal{X} with f 1 ± ∞ = f v ​ ( h ∓ ​ ( v ∗ ) , v ∗ ) ​ ( A 1 − 1 D ​ h ∓ ​ ( v ∗ ) ) f_{1}^{\pm\infty}=f_{v}(h^{\mp}(v^{*}),v^{*})(A_{1}-\frac{1}{D}h^{\mp}(v^{*})) . Therefore, by Lemma 2.3 (i), to guarantee that ( 2.26 ) with j = 1 j=1 is solvable in 𝒳 \mathcal{X} , we need to verify that f 1 ∈ [ w z 0 ] ⟂ f_{1}\in[w^{0}_{z}]^{\perp} , i.e.,

where in the third equality, we have used the identity

This implies that

Since J ′ ​ ( v ∗ ) ≠ 0 J^{\prime}(v^{*})\neq 0 by the condition (A3), this finishes the proof of ( 2.39 ) and determines A 1 A_{1} . Therefore, U ± , 1 U^{\pm,1} can now be determined by ( 2.21 )-(ii) from A 0 A_{0} and A 1 A_{1} as

Denote w ^ 1 := − ( L 0 ) − 1 ​ f 1 \widehat{w}^{1}:=-(L^{0})^{-1}f_{1} . Then any solution w 1 w^{1} of ( 2.26 ) can be expressed as ( 2.40 ). Applying Lemma 2.3 to the equation L 0 ​ w ^ 1 + f 1 = 0 L^{0}\widehat{w}^{1}+f_{1}=0 , we see from ( 2.32 ) and ( 2.37 ) that ( 2.43 ) with j = 1 j=1 holds. This implies that w 1 w^{1} satisfies condition ( 2.29 ) with j = 1 j=1 . We thus complete the proof of Part (i).

Next we prove Part (ii) for the case j = 2 j=2 . Then equation ( 2.26 ) with j = 2 j=2 reads L 0 ​ w 2 = − f 2 L^{0}w^{2}=-f_{2} with

where W 0 := ( w 0 ​ ( z ) , v ∗ ) W^{0}:=(w^{0}(z),v^{*}) . By ( 2.32 ) and ( 2.43 ) with j = 1 j=1 , we see that f 2 ∈ 𝒳 f_{2}\in\mathcal{X} . Therefore, by Lemma 2.3 (i), to guarantee that ( 2.26 ) with j = 2 j=2 is solvable, we need to verify that f 2 ∈ [ w z 0 ] ⟂ f_{2}\in[w^{0}_{z}]^{\perp} . Plugging w 1 = a 1 ​ w z 0 + w ^ 1 w^{1}=a_{1}w^{0}_{z}+\widehat{w}^{1} from ( 2.40 ) and A 1 A_{1} from ( 2.39 ) into the expression of f 2 f_{2} , we obtain from f 2 ∈ [ w z 0 ] ⟂ f_{2}\in[w^{0}_{z}]^{\perp} that

Here all other terms not involving A 2 A_{2} and a 1 a_{1} have been clumped together into the last term G 1 ​ ( R ∗ , D , a 0 ) G_{1}(R_{*},D,a_{0}) and we do not give an explicit formula for the function G 1 ​ ( R ∗ , D , a 0 ) G_{1}(R_{*},D,a_{0}) . We see from ( 2.52 ) that the coefficient of A 2 A_{2} is equal to − J ′ ​ ( v ∗ ) -J^{\prime}(v^{*}) . Through integrating by parts, we find that the coefficient of ( a 1 ) 2 (a_{1})^{2} is 0 0 . We now compute the coefficient of a 1 a_{1} to show that it is also 0 0 . Differentiating the equation L 0 ​ w ^ 1 + f 1 = 0 L^{0}\widehat{w}^{1}+f_{1}=0 with respect to z z , we obtain that

Therefore, we see from ( 2.32 ) and ( 2.43 ) with j = 1 j=1 and the fact L 0 ​ w z 0 = 0 L^{0}w^{0}_{z}=0 that

Consequently, we obtain that

This finishes the proof of ( 2.41 ) for j = 2 j=2 and determines A 2 A_{2} . Therefore, U ± , 2 U^{\pm,2} can now be determined by ( 2.21 )-(iii) from A 0 , A 1 A_{0},A_{1} and A 2 A_{2} .

Denote w ^ 2 := − ( L 0 ) − 1 ​ f 2 \widehat{w}^{2}:=-(L^{0})^{-1}f_{2} . Then any solution w 2 w^{2} of ( 2.26 ) can be expressed as ( 2.42 ) with j = 2 j=2 . Applying Lemma 2.3 to the equation L 0 ​ w ^ 2 + f 2 = 0 L^{0}\widehat{w}^{2}+f_{2}=0 , we see from ( 2.32 ) and ( 2.37 ) that ( 2.43 ) with j = 2 j=2 holds. This implies that w 2 w^{2} satisfies condition ( 2.29 ) with j = 2 j=2 . We thus finish the proof of Part (ii) for the case j = 2 j=2 .

The proof of Part (ii) for j ≥ 3 j\geq 3 is similar and follows in a inductive way. Since the computation is tedious, we omit the details. ∎

It follows from ( 1.8 ), ( 2.30 ) and ( 2.47 ) that ( 2.48 ) is equivalent to

where

To calculate K j ε K^{\varepsilon}_{j} , we first divide the domain ( − R ∗ ε , 1 − R ∗ ε ) \big({-\tfrac{R_{*}}{\varepsilon}},\tfrac{1-R_{*}}{\varepsilon}\big) of the stretched variable z = r − R ∗ ε z=\tfrac{r-R_{*}}{\varepsilon} into the following three subintervals:

Moreover, we denote

and

where U ± , j U^{\pm,j} are the constants defined in ( 2.21 ) for all j ≥ 0 j\geq 0 (cf. the comment after ( 2.21 )). Then for j = 0 , ⋯ , k j=0,\cdots,k , by direct calculation and ( 2.45 ), we see that

where

Note that K j m K_{j}^{m} do not depend on ε \varepsilon . Plugging ( 2.57 ) and ( 2.33 ) into ( 2.54 ), we obtain

where

and we have used the notations

By equating the coefficients of like powers of ε \varepsilon in ( 2.61 ), we observe that the conditions

together ensure that the expansion ( 2.48 ) holds.

To complete the proof, we solve the system ( 2.63 ) inductively by appropriately choosing:

the interface location parameter R ∗ R_{*} to enforce B 0 = M B_{0}=M ,

the free parameters a j − 1 a_{j-1} to satisfy B j = 0 B_{j}=0 for 1 ≤ j ≤ k + 1 1\leq j\leq k+1 , and

the coefficient A k + 2 ε , D A_{k+2}^{\varepsilon,D} to ensure B k + 2 ε , D = 0 B_{k+2}^{\varepsilon,D}=0 .

We begin by enforcing B 0 = M B_{0}=M in ( 2.63 ). To this end, we set

as defined in ( 1.10 ). To guarantee R ∗ ∈ ( 0 , 1 ) R_{*}\in(0,1) , we require that

Since R ∗ = R ∗ ​ ( M ) R_{*}=R_{*}(M) is determined by the prescribed averaged total mass M M , it follows from ( 2.39 ) and ( 2.21 )-(i)&(ii) that the constants A 1 A_{1} and the outer expansions U 0 U^{0} , U 1 U^{1} are thereby fully determined by M M (via R ∗ R_{*} ) and D D .

We now determine the parameter a 0 a_{0} so that the condition B 1 = 0 B_{1}=0 in ( 2.63 ) is satisfied. Since R ∗ R_{*} , A 1 A_{1} , U 0 U^{0} and U 1 U^{1} have already been determined above, all terms in the expression of B 1 B_{1} in ( 2.62 ) are known except for K 0 0 K_{0}^{0} . To compute K 0 0 K_{0}^{0} , we use its definition in ( 2.58 ) and the formula for w 0 w^{0} given by ( 2.31 ), yielding

where

is a known constant independent of a 0 a_{0} . Substituting this expression for K 0 0 K_{0}^{0} into the formula for B 1 B_{1} in ( 2.62 ), and noting that h + ​ ( v ∗ ) − h − ​ ( v ∗ ) ≠ 0 h^{+}(v^{*})-h^{-}(v^{*})\neq 0 , we conclude that the condition B 1 = 0 B_{1}=0 holds if and only if a 0 a_{0} is given by

where R ∗ = R ∗ ​ ( M ) R_{*}=R_{*}(M) is given by ( 1.10 ), A 1 A_{1} by ( 2.39 ), and U ± , 0 U^{\pm,0} , U ± , 1 U^{\pm,1} by ( 2.21 )-(i)&(ii). Hence, the free parameter a 0 a_{0} is now uniquely determined. Therefore w 0 ​ ( z ) = Q ⁡ ( z + a 0 ) w^{0}(z)=Q(z+a_{0}) is completely determined. As a result, the constants K 0 m K_{0}^{m} for 0 ≤ m ≤ N − 1 0\leq m\leq N-1 can now be explicitly computed from their expressions in ( 2.58 ). Furthermore, it follows from ( 2.41 ) for j = 2 j=2 that A 2 A_{2} can now be determined by G 1 ​ ( R ∗ ​ ( M ) , D , a 0 ) / J ′ ​ ( v ∗ ) G_{1}(R_{*}(M),D,a_{0})/J^{\prime}(v^{*}) . Hence, U ± , 2 U^{\pm,2} can be determined by A 0 A_{0} , A 1 A_{1} and A 2 A_{2} via ( 2.21 )-(iii).

In addition, from the above construction together with ( 2.21 ) and ( 2.32 ), it follows that for each D 0 > 0 D_{0}>0 , there exists a constant C 0 ′ = C 0 ′ ​ ( M , D 0 ) > 0 C^{\prime}_{0}=C^{\prime}_{0}(M,D_{0})>0 such that the uniform bounds ( 2.49 ) and ( 2.50 ) hold for k = 0 k=0 .

We now determine the parameter a 1 a_{1} in a similar manner such that the condition B 2 = 0 B_{2}=0 in ( 2.63 ) is satisfied. Observe that all terms in the expression of B 2 B_{2} in ( 2.62 ) have already been determined in earlier steps, except for K 1 0 K_{1}^{0} . Using ( 2.58 ) and the representation of w 1 w^{1} in ( 2.40 ), we compute:

where

is a known constant, since w ^ 1 = − ( L 0 ) − 1 ​ f 1 \widehat{w}^{1}=-(L^{0})^{-1}f_{1} (cf. Proposition 2.5 (i)) and U ± , 1 U^{\pm,1} are already determined. Substituting the above expression for K 1 0 K_{1}^{0} into the formula for B 2 B_{2} in ( 2.62 ), and noting that h + ​ ( v ∗ ) − h − ​ ( v ∗ ) ≠ 0 h^{+}(v^{*})-h^{-}(v^{*})\neq 0 , we conclude that B 2 = 0 B_{2}=0 holds if and only if

where a 1 ​ ( M , D , a 0 ) a_{1}(M,D,a_{0}) is a smooth function determined by solving a 1 a_{1} from the equation B 2 = 0 B_{2}=0 . Thus, the parameter a 1 a_{1} is now uniquely determined. Once a 1 a_{1} is known, the function w 1 ​ ( z ) w^{1}(z) is completely specified via ( 2.40 ). Consequently, the constants K 1 m K_{1}^{m} for 0 ≤ m ≤ N − 1 0\leq m\leq N-1 can be computed explicitly using ( 2.58 ). Furthermore, it follows from ( 2.41 ) for j = 3 j=3 that A 3 A_{3} can now be determined by G 2 ​ ( R ∗ ​ ( M ) , D , a 0 , a 1 ) / J ′ ​ ( v ∗ ) G_{2}(R_{*}(M),D,a_{0},a_{1})/J^{\prime}(v^{*}) . Hence, U ± , 3 U^{\pm,3} can be determined by A 0 A_{0} , A 1 A_{1} , A 2 A_{2} and A 3 A_{3} via ( 2.21 )-(iii).

Similarly, from the above analysis together with ( 2.21 ), ( 2.32 ), and ( 2.43 ), it follows that for each D 0 > 0 D_{0}>0 , there exists a constant C 1 ′ ​ ( M , D 0 ) > 0 C^{\prime}_{1}(M,D_{0})>0 such that the uniform bounds in ( 2.49 ) and ( 2.50 ) hold for k = 1 k=1 .

We proceed inductively to determine the parameter a j a_{j} such that the condition B j + 1 = 0 B_{j+1}=0 in ( 2.63 ) is satisfied for each 2 ≤ j ≤ k 2\leq j\leq k . Indeed, for any such j j , all terms in the expression of B j + 1 B_{j+1} in ( 2.62 ) have already been determined in previous steps, except for K j 0 K_{j}^{0} . We compute K j 0 K_{j}^{0} using its definition in ( 2.58 ) and the expression for w j w^{j} in ( 2.42 ) as follows:

where

is explicitly computable, as w ^ j = − ( L 0 ) − 1 ​ f j \widehat{w}^{j}=-(L^{0})^{-1}f_{j} (cf. Proposition 2.5 (ii)) and U ± , j U^{\pm,j} are determined in earlier steps. Substituting this expression for K j 0 K_{j}^{0} into the formula for B j + 1 B_{j+1} in ( 2.62 ), and noting that h + ​ ( v ∗ ) − h − ​ ( v ∗ ) ≠ 0 h^{+}(v^{*})-h^{-}(v^{*})\neq 0 , we conclude that the condition B j + 1 = 0 B_{j+1}=0 uniquely determines a j a_{j} . We denote this solution by

where a j ​ ( M , D , a 0 , ⋯ , a j − 1 ) a_{j}(M,D,a_{0},\cdots,a_{j-1}) is a smooth function of the variables indicated.

To summarize, for each M ∈ I v ∗ M\in I_{v^{*}} and D > 0 D>0 , we can recursively determine the interface location and free parameters a j a_{j} as

such that B 0 = M B_{0}=M and B j + 1 = 0 B_{j+1}=0 for j ≥ 0 j\geq 0 , respectively. As a result, the inner profiles w j w^{j} are determined by ( 2.31 ), ( 2.40 ) and ( 2.42 ), the constants A j + 1 A_{j+1} are determined via ( 2.39 ) and ( 2.41 ), and the outer profiles U ± , j U^{\pm,j} follow from ( 2.21 ) for j ≥ 0 j\geq 0 . Each of these quantities is determined recursively and depends smoothly on the quantities determined in previous steps. Furthermore, it follows from ( 2.32 ) and Proposition 2.5 that for each D 0 > 0 D_{0}>0 and k ∈ ℕ k\in\mathbb{N} , there exists a constant C k ′ ​ ( M , D 0 ) > 0 C^{\prime}_{k}(M,D_{0})>0 such that the uniform bounds ( 2.49 ) and ( 2.50 ) hold.

Finally, for each k ∈ ℕ k\in\mathbb{N} , to ensure that the condition B k + 2 ε , D = 0 B_{k+2}^{\varepsilon,D}=0 in ( 2.63 ) holds, we see from the expression of B k + 2 ε , D B_{k+2}^{\varepsilon,D} in ( 2.62 ) that it suffices to set

Then we conclude from ( 2.54 ), ( 2.61 ) and ( 2.63 ) that the expansion ( 2.48 ) holds for all ε > 0 \varepsilon>0 , D > 0 D>0 , and k ∈ ℕ k\in\mathbb{N} .

To complete the proof of the proposition, it remains to establish the uniform bound ( 2.51 ). Fix ε 0 > 0 \varepsilon_{0}>0 , D 0 > 0 D_{0}>0 and k ∈ ℕ k\in\mathbb{N} . In the expression of A k + 2 ε , D A_{k+2}^{\varepsilon,D} in ( 2.64 ), the powers of ε \varepsilon in the first and third summations satisfy j + m − k − 1 ≥ 0 j+m-k-1\geq 0 and j + m − k ≥ 0 j+m-k\geq 0 , respectively. This, combined with the expressions for K j m K_{j}^{m} in ( 2.58 ) and the preceding uniform estimates, ensures that both summations are uniformly bounded by a constant C k = C k ​ ( M , D 0 , ε 0 ) > 0 C_{k}=C_{k}(M,D_{0},\varepsilon_{0})>0 for all ε ∈ ( 0 , ε 0 ] \varepsilon\in(0,\varepsilon_{0}] and D ≥ D 0 D\geq D_{0} . To bound the second and fourth summations, observe that

for all integers 0 ≤ m ≤ N − 1 0\leq m\leq N-1 , 0 ≤ j ≤ k 0\leq j\leq k and i = 1 , 2 i=1,2 , where the supremum depends only on ε 0 \varepsilon_{0} , k k and M M , through the interface location R ∗ R_{*} in ( 1.10 ) and r 0 r_{0} in ( 2.46 ) that appears in the integration domains I 2 I_{2} and I 4 I_{4} (cf. ( 2.55 ) and ( 2.56 )). This bound, together with the expressions for K j , 1 ε K^{\varepsilon}_{j,1} and K j , 2 ε K^{\varepsilon}_{j,2} in ( 2.59 )-( 2.60 ) and the estimates of w j w^{j} in ( 2.32 ) and ( 2.43 ), yields the desired uniform bound ( 2.51 ). This completes the proof of the proposition. ∎


## 2.4. Properties of outer expansions and inner expansions

We first summarize properties of the k k -th order outer expansion U k ε U^{\varepsilon}_{k} defined in ( 2.44 ).

Assume that conditions (A1)-(A3) hold. Let M ∈ I v ∗ M\in I_{v^{*}} and D 0 , ε 0 > 0 D_{0},\varepsilon_{0}>0 be given. Then for each k ∈ ℕ k\in\mathbb{N} , both U k ε | Ω + U^{\varepsilon}_{k}|_{\Omega_{+}} and U k ε | Ω − U^{\varepsilon}_{k}|_{\Omega_{-}} are constant and there exists a constant C k = C k ​ ( M , D 0 , ε 0 ) > 0 C_{k}=C_{k}(M,D_{0},\varepsilon_{0})>0 such that for all ε ∈ ( 0 , ε 0 ] \varepsilon\in(0,\varepsilon_{0}] and D ≥ D 0 D\geq D_{0} ,

where U k ε U^{\varepsilon}_{k} is defined in ( 2.44 ) and u k ε , D u_{k}^{\varepsilon,D} is defined in ( 2.47 ).

The proof of Corollary 2.7 follows directly from the equations for U j U^{j} in ( 2.19 ) and Proposition 2.6 . Thus we omit the details.

Next, we summarize properties of the k k -th order inner expansion w k ε w^{\varepsilon}_{k} defined in ( 2.44 ).

Assume that conditions (A1)-(A3) hold. Let M ∈ I v ∗ M\in I_{v^{*}} and D 0 , ε 0 > 0 D_{0},\varepsilon_{0}>0 be given. Then for each k ∈ ℕ k\in\mathbb{N} , there exists a constant C k = C k ​ ( M , D 0 , ε 0 ) > 0 C_{k}=C_{k}(M,D_{0},\varepsilon_{0})>0 such that for all ε ∈ ( 0 , ε 0 ] \varepsilon\in(0,\varepsilon_{0}] and D ≥ D 0 D\geq D_{0} ,

where w k ε w^{\varepsilon}_{k} is defined in ( 2.44 ) and u k ε , D u_{k}^{\varepsilon,D} is defined in ( 2.47 ).

Note that in the above corollary, we only require the estimate to hold for z ∈ ( − 2 ​ r 0 ε , 2 ​ r 0 ε ) z\in\big(-\tfrac{2r_{0}}{\varepsilon},\tfrac{2r_{0}}{\varepsilon}\big) for each ε ∈ ( 0 , ε 0 ] \varepsilon\in(0,\varepsilon_{0}] , thanks to the definition of u k ε , D u_{k}^{\varepsilon,D} in ( 2.47 ).

Note that for i = 0 , ⋯ , k i=0,\cdots,k , w j w^{j} are chosen via ( 2.25 )-( 2.26 ) so that

Therefore, for each z ∈ ( − 2 ​ r 0 ε , 2 ​ r 0 ε ) z\in\left(-\tfrac{2r_{0}}{\varepsilon},\tfrac{2r_{0}}{\varepsilon}\right) , there exists some τ ∈ ( 0 , ε ) \tau\in(0,\varepsilon) such that

Since R ∗ + ε ​ z ∈ ( R ∗ − 2 ​ r 0 , R ∗ + 2 ​ r 0 ) R_{*}+\varepsilon z\in(R_{*}-2r_{0},R_{*}+2r_{0}) , the conclusion follows directly from ( 2.44 ) and Proposition 2.6 . ∎

In the end of this subsection, we show that the approximate solutions u k ε , D ​ ( r ) u^{\varepsilon,D}_{k}(r) defined by ( 2.47 ) are uniformly bounded and exhibit a sharp transition layer of width O ⁡ ( ε ) O(\varepsilon) across the interface Γ ∗ \Gamma_{*} .

Let M ∈ I v ∗ M\in I_{v^{*}} be given and u k ε , D ​ ( r ) u^{\varepsilon,D}_{k}(r) be the family of smooth radially symmetric functions defined by ( 2.47 ) for ε , D > 0 \varepsilon,D>0 and k ∈ ℕ k\in\mathbb{N} . Then the following statements hold.

For each D 0 , ε 0 > 0 D_{0},\varepsilon_{0}>0 and k ∈ ℕ k\in\mathbb{N} , there there exists a constant C k = C k ​ ( M , D 0 , ε 0 ) > 0 C_{k}=C_{k}(M,D_{0},\varepsilon_{0})>0 such that

For each D 0 > 0 D_{0}>0 , k ∈ ℕ k\in\mathbb{N} and η > 0 \eta>0 , there exist two positive constants K = K ⁡ ( η ) K=K(\eta) and ε ¯ = ε ¯ ​ ( M , D 0 , k , η ) > 0 \bar{\varepsilon}=\bar{\varepsilon}(M,D_{0},k,\eta)>0 such that for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} ,

Part (i) follows directly from ( 2.47 ) and ( 2.50 ).

We now prove Part (ii). By ( 2.33 ), ( 2.44 ) and ( 2.50 ), we see that there exists a constant ε ¯ 1 = ε ¯ 1 ​ ( M , D 0 , k , η ) > 0 \bar{\varepsilon}_{1}=\bar{\varepsilon}_{1}(M,D_{0},k,\eta)>0 such that for any ε ∈ ( 0 , ε ¯ 1 ] \varepsilon\in(0,\bar{\varepsilon}_{1}] and D ≥ D 0 D\geq D_{0} ,

On the other hand, we see from ( 2.44 ), ( 2.32 ) and ( 2.50 ) that there exist two constants K = K ⁡ ( η ) > 0 K=K(\eta)>0 and ε ¯ 2 = ε ¯ 2 ​ ( M , D 0 , k , η ) > 0 \bar{\varepsilon}_{2}=\bar{\varepsilon}_{2}(M,D_{0},k,\eta)>0 such that

Now, setting ε ¯ := min ⁡ { ε ¯ 1 , ε ¯ 2 } \bar{\varepsilon}:=\min\{\bar{\varepsilon}_{1},\bar{\varepsilon}_{2}\} , we see from ( 2.47 ) and the above two estimates that ( 2.67 ) holds. This finished the proof of the corollary. ∎


## 2.5. Proof of Proposition 2.2

In the remainder of this paper, we adopt the notation g ~ ​ ( z ) \widetilde{g}(z) to denote the stretched version of a radial function g ⁡ ( r ) g(r) (with r = | x | r=|x| ) in Ω \Omega , defined by g ~ ​ ( z ) := g ⁡ ( R ∗ + ε ​ z ) \widetilde{g}(z):=g(R_{*}+\varepsilon z) for z ∈ ( − R ∗ ε , 1 − R ∗ ε ) z\in(-\tfrac{R_{*}}{\varepsilon},\tfrac{1-R_{*}}{\varepsilon}) .

We divide Ω \Omega into the following three subregions:

Then by ( 2.47 ), u k ε , D ​ ( r ) u^{\varepsilon,D}_{k}(r) satisfies that

Recall that I i I_{i} for i = 1 , 2 , 3 i=1,2,3 are defined in ( 2.55 ). The derivative of the stretched function u ~ k ε , D ​ ( z ) \widetilde{u}^{\varepsilon,D}_{k}(z) satisfies that

We now prove Proposition 2.2 .

The smoothness of u k ε , D ​ ( r ) u^{\varepsilon,D}_{k}(r) follows obviously from its definition in ( 2.47 ).

Part (i) of Proposition 2.2 follows directly from Corollary 2.9 (ii).

We now proceed to prove Part (ii) of Proposition 2.2 . Let ε 0 > 0 \varepsilon_{0}>0 be a fixed constant throughout the remainder of this proof. The uniform bound in ( 2.12 ) follows directly from Corollary 2.9 (i). To establish ( 2.13 ), we estimate the residual term ℛ ε ​ [ u k ε , D ] \mathcal{R}^{\varepsilon}[u_{k}^{\varepsilon,D}] in the L ∞ L^{\infty} -norm over each subdomain Ω i \Omega_{i} for i = 1 , 2 , 3 i=1,2,3 , where the domains Ω i \Omega_{i} are defined in ( 2.68 ).

On Ω 1 \Omega_{1} , it follows from ( 2.69 ) and Corollary 2.7 that there exists a constant C k = C k ​ ( M , D 0 , ε 0 ) > 0 C_{k}=C_{k}(M,D_{0},\varepsilon_{0})>0 such that for all ε ∈ ( 0 , ε 0 ] \varepsilon\in(0,\varepsilon_{0}] and D ≥ D 0 D\geq D_{0} ,

On Ω 3 \Omega_{3} , it follows from ( 2.69 ) and Corollary 2.8 that there exists a constant C k = C k ​ ( M , D 0 , ε 0 ) > 0 C_{k}=C_{k}(M,D_{0},\varepsilon_{0})>0 such that for all ε ∈ ( 0 , ε 0 ] \varepsilon\in(0,\varepsilon_{0}] and D ≥ D 0 D\geq D_{0} ,

For each x ∈ Ω 2 x\in\Omega_{2} , we have

where we have used ( 2.69 ) and computed the derivatives in terms of the stretched variable z = r − R ∗ ε ∈ I 2 z=\tfrac{r-R_{*}}{\varepsilon}\in I_{2} with r = | x | r=|x| for K 2 ε K_{2}^{\varepsilon} and K 3 ε K_{3}^{\varepsilon} . We next estimate K i ε K_{i}^{\varepsilon} for i = 1 , 2 , 3 i=1,2,3 .

For K 1 ε K_{1}^{\varepsilon} , we see from Proposition 2.6 , Corollary 2.7 , ( 2.69 ), ( 2.32 ) and ( 2.43 ) that there exists a constant C k = C k ​ ( M , D 0 , ε 0 ) > 0 C_{k}=C_{k}(M,D_{0},\varepsilon_{0})>0 such that for all ε ∈ ( 0 , ε 0 ] \varepsilon\in(0,\varepsilon_{0}] and D ≥ D 0 D\geq D_{0} ,

where the estimation for the last term on the right hand side is computed in terms of the stretched variable z = r − R ∗ ε ∈ I 2 z=\tfrac{r-R_{*}}{\varepsilon}\in I_{2} with r = | x | r=|x| .

For K 2 ε K_{2}^{\varepsilon} , By ( 2.44 ), ( 2.32 ) and ( 2.43 ), we see that

Similarly, for K 3 ε ​ ( z ) K_{3}^{\varepsilon}(z) , by direct computation, we see that

Now for fixed M ∈ I v ∗ M\in I_{v^{*}} , it is easy to see that

and the supremum depends only on k k , ε 0 \varepsilon_{0} and M M (via R ∗ R_{*} defined in ( 1.10 ) and r 0 r_{0} defined in ( 2.46 ) that appears in the definition of the interval I 2 I_{2} in ( 2.55 )). Therefore, combining the above estimates for K i ε K_{i}^{\varepsilon} for i = 1 , 2 , 3 i=1,2,3 together, we see that there exists a constant C k = C k ​ ( M , D 0 , ε 0 ) > 0 C_{k}=C_{k}(M,D_{0},\varepsilon_{0})>0 such that for all ε ∈ ( 0 , ε 0 ] \varepsilon\in(0,\varepsilon_{0}] and D ≥ D 0 D\geq D_{0} ,

Finally, combining the above estimates for ‖ ℛ ε ​ [ u k ε , D ] ‖ L ∞ ​ ( Ω i ) \big\|\mathcal{R}^{\varepsilon}[u^{\varepsilon,D}_{k}]\big\|_{L^{\infty}(\Omega_{i})} for i = 1 , 2 , 3 i=1,2,3 , we complete the proof of Proposition 2.2 (ii).

The first statement in Parts (iii) of Theorem 2.2 follows directly from the definition of 𝒮 ε ​ [ ⋅ ] \mathcal{S}^{\varepsilon}[\,\cdot\,] in ( 1.8 ), while the second statement follows from ( 2.48 ), ( 2.49 ), ( 2.51 ) and ( 2.12 ). This finishes the proof of the proposition. ∎


## 3. Spectral analysis of the approximate solutions


## 3.1. Spectral analysis of the approximate solutions

To prove the existence of an exact solution to ( 1.9 ) near the approximate solution u k ε , D u_{k}^{\varepsilon,D} constructed in Theorem 2.2 , we perform a spectral analysis of the linearized operator obtained by linearizing ( 1.9 ) around u k ε , D u_{k}^{\varepsilon,D} . For this purpose, we first introduce some function spaces. For 1 ≤ s ≤ ∞ 1\leq s\leq\infty , let

and

We consider the following nonlocal radial eigenvalue problem with homogeneous Neumann boundary condition in H r ​ a ​ d 2 := W r ​ a ​ d 2 , 2 H_{rad}^{2}:=W_{rad}^{2,2} :

where the operator ℒ k ε \mathscr{L}_{k}^{\varepsilon} is defined by

with

and 𝒮 ε ​ [ ⋅ ] \mathcal{S}^{\varepsilon}[\,\cdot\,] is defined in ( 1.8 ).

Note that for notational simplicity, we have suppressed the explicit dependence of ℒ k ε \mathscr{L}_{k}^{\varepsilon} on the parameters D D and M M . The same convention will be adopted throughout the remainder of this paper for other mathematical notations that depend on these parameters.

To state our results for the eigenvalue problem ( 3.71 ) precisely, we introduce some shorthand notations. Recall that R ∗ = R ∗ ​ ( M ) ∈ ( 0 , 1 ) R_{*}=R_{*}(M)\in(0,1) is defined in ( 1.10 ), Ω − = B R ∗ \Omega^{-}=B_{R_{*}} and Ω + = B 1 \ B ¯ R ∗ \Omega^{+}=B_{1}\backslash\overline{B}_{R_{*}} are defined in ( 2.15 ). We then denote

We further denote

and

where the signs of E E and G G follow from the conditions (A1), (A2) and the fact that R ∗ ∈ ( 0 , 1 ) R_{*}\in(0,1) .

We now state our main result Theorem 3.1 in this section, which will be used in the proof of Theorem 1.3 in Section 4. We also emphasize that all conclusions in this section hold for any integer k ≥ 1 k\geq 1 , where k ∈ ℕ k\in\mathbb{N} is the order of the approximate solution u k ε , D u^{\varepsilon,D}_{k} defined in ( 2.47 ) .

Assume that conditions (A1) - (A3) hold. Let M ∈ I v ∗ M\in I_{v^{*}} be given. Then, for each D 0 > 0 D_{0}>0 and integer k ≥ 1 k\geq 1 , there exist two constants ε ¯ = ε ¯ ​ ( M , D 0 , k ) > 0 \bar{\varepsilon}=\bar{\varepsilon}(M,D_{0},k)>0 and λ ∗ = λ ∗ ​ ( M , D 0 , k ) > 0 \lambda_{*}=\lambda_{*}(M,D_{0},k)>0 such that the following statements hold for the nonlocal radial eigenvalue problem ( 3.71 ):

The nonlocal operator ℒ k ε \mathscr{L}_{k}^{\varepsilon} admits a unique eigenvalue λ 0 ε , k \lambda_{0}^{\varepsilon,k} (called the critical eigenvalue ) in the region ℂ λ ∗ := { λ ∈ ℂ | Re ⁡ λ > − λ ∗ } \mathbb{C}_{\lambda_{*}}:=\{\lambda\in\mathbb{C}\,|\,\re\lambda>-\lambda_{*}\} for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} .

The critical eigenvalue λ 0 ε , k ∈ ℂ λ ∗ \lambda_{0}^{\varepsilon,k}\in\mathbb{C}_{\lambda_{*}} of ( 3.71 ) is real, simple and

where

m ⁡ ( ⋅ ) m(\,\cdot\,) is defined in Proposition 2.1 (ii) and G G is defined in ( 3.1 ).

Let Φ 0 ε , k \Phi_{0}^{\varepsilon,k} denote the L 2 L^{2} -normalized eigenfunction of ℒ k ε \mathscr{L}_{k}^{\varepsilon} corresponding to the eigenvalue λ 0 ε , k \lambda_{0}^{\varepsilon,k} . Then there exists a constant C k = C k ​ ( M , D 0 , ε ¯ ) > 0 C_{k}=C_{k}(M,D_{0},\bar{\varepsilon})>0 such that for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} ,

Let ℒ ^ k ε \widehat{\mathscr{L}}_{k}^{\varepsilon} denote the L 2 L^{2} -adjoint of the nonlocal operator ℒ k ε \mathscr{L}_{k}^{\varepsilon} . Then, for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} , the operator ℒ ^ k ε \widehat{\mathscr{L}}_{k}^{\varepsilon} admits a unique eigenvalue λ ^ 0 ε , k \widehat{\lambda}_{0}^{\varepsilon,k} in the region ℂ λ ∗ \mathbb{C}_{\lambda_{*}} , which is real, simple and satisfies

Denote by Φ ^ 0 ε , k \widehat{\Phi}_{0}^{\varepsilon,k} the eigenfunction of ℒ ^ k ε \widehat{\mathscr{L}}_{k}^{\varepsilon} corresponding to the eigenvalue λ ^ 0 ε , k \widehat{\lambda}_{0}^{\varepsilon,k} . Then Φ ^ 0 ε , k \widehat{\Phi}_{0}^{\varepsilon,k} can be normalized such that

and satisfies that

for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} .

The proof of Theorem 3.1 will be given in Subsection 3.4 .

By elliptic regularity theory, the eigenfunction Φ 0 ε , k \Phi_{0}^{\varepsilon,k} of ℒ k ε \mathscr{L}_{k}^{\varepsilon} belongs to C 2 + α ​ ( Ω ¯ ) C^{2+\alpha}(\bar{\Omega}) for some 0 < α < 1 0<\alpha<1 . The same is true for Φ ^ 0 ε , k \widehat{\Phi}_{0}^{\varepsilon,k} . Hence Φ 0 ε , k \Phi_{0}^{\varepsilon,k} , Φ ^ 0 ε , k ∈ L r ​ a ​ d s \widehat{\Phi}_{0}^{\varepsilon,k}\in L_{rad}^{s} for all 1 ≤ s ≤ ∞ 1\leq s\leq\infty . Note that it is easy to verify that ℒ k ε ​ ( W ν 2 , s ∩ L r ​ a ​ d s ) ⊂ L r ​ a ​ d s \mathscr{L}_{k}^{\varepsilon}(W_{\nu}^{2,s}\cap L_{rad}^{s})\subset L_{rad}^{s} . For each 1 < s ≤ ∞ 1<s\leq\infty , define

where s ′ = s s − 1 s^{\prime}=\tfrac{s}{s-1} and ⟨ ⋅ , ⋅ ⟩ s , s ′ \langle\cdot,\cdot\rangle_{s,s^{\prime}} denotes the pairing between L s ​ ( Ω ) L^{s}(\Omega) and L s ′ ​ ( Ω ) L^{s^{\prime}}(\Omega) . Set

Since the resolvent of ℒ k ε \mathscr{L}_{k}^{\varepsilon} is compact and Theorem 3.1 ensures that

the following lemma follows directly from the Riesz-Schauder theory.

Assume that conditions (A1) - (A3) hold. Let M ∈ I v ∗ M\in I_{v^{*}} be given. Then for each D 0 > 0 D_{0}>0 and integer k ≥ 1 k\geq 1 , there exists a constant ε ¯ = ε ¯ ​ ( M , D 0 , k ) > 0 \bar{\varepsilon}=\bar{\varepsilon}(M,D_{0},k)>0 such that the closed linear operator ℒ k ε − λ 0 ε , k \mathscr{L}_{k}^{\varepsilon}-\lambda_{0}^{\varepsilon,k} has a bounded right inverse ( ℒ k ε − λ 0 ε , k ) − 1 (\mathscr{L}_{k}^{\varepsilon}-\lambda_{0}^{\varepsilon,k})^{-1} from X s X^{s} to X ν 2 , s X_{\nu}^{2,s} , for each 1 < s < ∞ 1<s<\infty , ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} .

Now, given g ∈ X ∞ ⊂ X s g\in X^{\infty}\subset X^{s} , the equation

has a unique solution h ∈ X ν 2 , s h\in X_{\nu}^{2,s} for each s ∈ ( 1 , ∞ ) s\in(1,\infty) by virtue of Lemma 3.2 . By similar arguments to the remark right after Lemma 2.2 in [ 31 ] , we can show that h h is independent of s s . Therefore, by taking s > ( N / 2 ) ∨ 1 s>(N/2)\vee 1 , we see that h ∈ C α ​ ( Ω ¯ ) h\in C^{\alpha}(\bar{\Omega}) , 0 < α < 1 0<\alpha<1 , by the Sobolev embedding theorem. In particular, h ∈ X ∞ h\in X^{\infty} . Hence, ( ℒ k ε − λ 0 ε , k ) − 1 (\mathscr{L}_{k}^{\varepsilon}-\lambda_{0}^{\varepsilon,k})^{-1} may be considered as a linear mapping from X ∞ X^{\infty} into X ∞ X^{\infty} . In fact, we have the following result.

Assume that conditions (A1) - (A3) hold. Let M ∈ I v ∗ M\in I_{v^{*}} be given. Then for each D 0 > 0 D_{0}>0 and integer k ≥ 1 k\geq 1 , there exists a constant ε ¯ = ε ¯ ​ ( M , D 0 , k ) > 0 \bar{\varepsilon}=\bar{\varepsilon}(M,D_{0},k)>0 such that the inverse operator ( ℒ k ε − λ 0 ε , k ) − 1 : X ∞ → X ∞ (\mathscr{L}_{k}^{\varepsilon}-\lambda_{0}^{\varepsilon,k})^{-1}:X^{\infty}\to X^{\infty} exists and there exists a constant C k = C k ​ ( M , D 0 , ε ¯ ) > 0 C_{k}=C_{k}(M,D_{0},\bar{\varepsilon})>0 such that

for all g ∈ X ∞ g\in X^{\infty} , ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} .

Lemma 3.3 will be proved in Subsection 3.5 .


## 3.2. The principal eigenvalue of ℒ k ε \mathcal{L}^{\varepsilon}_{k}

To prove Theorem 3.1 and Lemma 3.3 , we need to first consider the following local symmetric radial eigenvalue problem with the homogeneous Neumann boundary condition in H r ​ a ​ d 2 ​ ( Ω ) H_{rad}^{2}(\Omega) :

where f u ε , k f_{u}^{\varepsilon,k} and f v ε , k f_{v}^{\varepsilon,k} are defined in ( 3.73 ). Let

denote the sequence of (radial) eigenvalues of ℒ k ε \mathcal{L}^{\varepsilon}_{k} with associated eigenfunctions ϕ 0 ε , k \phi_{0}^{\varepsilon,k} , ϕ 1 ε , k \phi_{1}^{\varepsilon,k} , ϕ 2 ε , k \phi_{2}^{\varepsilon,k} and so on.

The principal eigenvalue μ 0 ε , k \mu_{0}^{\varepsilon,k} of the operator ℒ k ε \mathcal{L}^{\varepsilon}_{k} plays a key role in determining the spectrum of the eigenvalue problem ( 3.71 ). To analyze its asymptotic behavior as ε → 0 \varepsilon\to 0 , we first establish two preparatory lemmas.

Let W ⊂ ℝ N W\subset\mathbb{R}^{N} be a bounded smooth domain. For δ > 0 \delta>0 , define

where d ⁡ ( x ) = dist ⁡ ( x , ∂ W ) d(x)=\dist(x,\partial W) . Assume that d ∈ C 2 ​ ( W δ ¯ ) d\in C^{2}(\overline{W_{\delta}}) and that ρ ∈ C 2 ​ ( W δ ¯ ) \rho\in C^{2}(\overline{W_{\delta}}) satisfies

where c ε ​ ( x ) ≥ c 0 > 0 c^{\varepsilon}(x)\geq c_{0}>0 for all x ∈ W δ ¯ x\in\overline{W_{\delta}} and ε > 0 \varepsilon>0 , and ν \nu is the unit outer normal on ∂ W \partial W . Then for each ε 0 > 0 \varepsilon_{0}>0 , there exists a constant σ 1 = σ 1 ​ ( ε 0 , ‖ Δ ​ d ‖ L ∞ ​ ( W δ ) , c 0 ) > 0 \sigma_{1}=\sigma_{1}(\varepsilon_{0},\|\Delta d\|_{L^{\infty}(W_{\delta})},c_{0})>0 such that

where C > 0 C>0 is a constant depending only on N N and ‖ c ε ‖ L ∞ ​ ( W δ ) \|c^{\varepsilon}\|_{L^{\infty}(W_{\delta})} .

In contrast to Lemma 3.4 , which addresses the decay behavior of ρ ⁡ ( x ) \rho(x) and ∇ ρ ​ ( x ) \nabla\rho(x) near the boundary of a domain, the following lemma concerns the decay as x x approaches an interior point. We formulate it on the ball B R ⊂ ℝ N B_{R}\subset\mathbb{R}^{N} centered at the origin.

Suppose that ρ ∈ C 2 ​ ( B ¯ R ) \rho\in C^{2}(\overline{B}_{R}) satisfies

where c ε ​ ( x ) ≥ c 0 > 0 c^{\varepsilon}(x)\geq c_{0}>0 for all x ∈ B ¯ R x\in\overline{B}_{R} and ε > 0 \varepsilon>0 . Then for each ε 0 > 0 \varepsilon_{0}>0 , there exists a constant σ 2 = σ 2 ​ ( ε 0 , R − 1 , c 0 , N ) > 0 \sigma_{2}=\sigma_{2}(\varepsilon_{0},R^{-1},c_{0},N)>0 such that

where C > 0 C>0 is a constant depending only on N N and ‖ c ε ‖ L ∞ ​ ( B R ) \|c^{\varepsilon}\|_{L^{\infty}(B_{R})} .

Lemmas 3.4 and 3.5 will be proved in subsection 3.3 . Since the spatial dimension N N is fixed, we shall henceforth not explicitly mention the dependence of subsequent quantities on N N when applying Lemmas 3.4 and 3.5 .

Assume that conditions (A1) - (A3) hold. Let M ∈ I v ∗ M\in I_{v^{*}} be given. Then, for each integer k ≥ 1 k\geq 1 and D 0 > 0 D_{0}>0 , the principal eigenvalue μ 0 ε , k \mu_{0}^{\varepsilon,k} of ℒ k ε \mathcal{L}^{\varepsilon}_{k} satisfies

and the L 2 L^{2} -normalized, positive, principal eigenfunction ϕ 0 ε , k \phi_{0}^{\varepsilon,k} of ℒ k ε \mathcal{L}^{\varepsilon}_{k} corresponding to μ 0 ε , k \mu_{0}^{\varepsilon,k} satisfies

uniformly in D ≥ D 0 D\geq D_{0} . Furthermore, there exists a constant ε ¯ = ε ¯ ​ ( M , D 0 , k ) > 0 \bar{\varepsilon}=\bar{\varepsilon}(M,D_{0},k)>0 such that for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} ,

where C k = C k ​ ( M , D 0 , ε ¯ ) > 0 C_{k}=C_{k}(M,D_{0},\bar{\varepsilon})>0 is a constant depending only on the variables indicated.

Let M ∈ I v ∗ M\in I_{v^{*}} , D 0 > 0 D_{0}>0 and the integer k ≥ 1 k\geq 1 be given. We first prove ( 3.86 ). We claim that

To show this, we use the variational characterization of μ 0 ε , k \mu_{0}^{\varepsilon,k} given by

Using ϕ ⁡ ( r ) = w z 0 ​ ( r − R ∗ ε ) \phi(r)=w^{0}_{z}\big(\tfrac{r-R_{*}}{\varepsilon}\big) as a test function, we easily see that

where g ~ ​ ( z ) \widetilde{g}(z) denotes the stretched version of a radial function g ⁡ ( r ) g(r) (with r = | x | r=|x| ) in Ω \Omega , defined by g ~ ​ ( z ) = g ⁡ ( R ∗ + ε ​ z ) \widetilde{g}(z)=g(R_{*}+\varepsilon z) , as adopted at the beginning of subsection 2.5 . Sending ε → 0 \varepsilon\to 0 , we see from ( 2.32 ), ( 2.44 )-( 2.48 ) and the Dominated Convergence Theorem that

Then we see from L 0 ​ w z 0 = 0 L^{0}w^{0}_{z}=0 and ( 2.32 ) that the integral in the numerator equals zero. Thus ( 3.89 ) holds.

Recall that d 0 d_{0} is a fixed constant satisfying ( 2.28 ). Then, by Theorem 2.2 , ( 2.28 ) and ( 3.73 ), there exist two constants K > 0 K>0 and ε ¯ = ε ¯ ​ ( M , D 0 , k ) > 0 \bar{\varepsilon}=\bar{\varepsilon}(M,D_{0},k)>0 such that for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} ,

where we have omitted the dependence of K K and ε ¯ \bar{\varepsilon} on d 0 d_{0} as d 0 d_{0} is fixed. Denote by ϕ 0 ε , k \phi_{0}^{\varepsilon,k} the positive eigenfunction corresponding to the eigenvalue μ 0 ε , k \mu_{0}^{\varepsilon,k} . We first normalize it such that

Then ϕ 0 ε , k \phi_{0}^{\varepsilon,k} satisfies

By ( 3.89 ), ( 3.90 ) and Theorem 2.2 , we can choose ε ¯ \bar{\varepsilon} even smaller if necessary so that for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} ,

We now apply Lemma 3.4 to the equation for ϕ 0 ε , k \phi_{0}^{\varepsilon,k} with ( ρ , c 0 , W , δ ) = ( ϕ 0 ε , k , d 0 2 / 2 , Ω , 1 − R ∗ − ε ​ K ) (\rho,c_{0},W,\delta)=(\phi_{0}^{\varepsilon,k},d_{0}^{2}/2,\Omega,1-R_{*}-\varepsilon K) and obtain from ( 3.89 ), ( 3.90 ) and Theorem 2.2 that there exist two constants σ 1 = σ 1 ​ ( ε ¯ , 1 / R ∗ , D 0 ) > 0 \sigma_{1}=\sigma_{1}(\bar{\varepsilon},1/R_{*},D_{0})>0 and C k , 1 = C k , 1 ​ ( M , D 0 , ε ¯ ) > 0 C_{k,1}=C_{k,1}(M,D_{0},\bar{\varepsilon})>0 such that for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} ,

Similarly, applying Lemma 3.5 to equation for ϕ 0 ε , k \phi_{0}^{\varepsilon,k} with ( ρ , c 0 , R ) = ( ϕ 0 ε , k , d 0 2 / 2 , R ∗ − ε ​ K ) (\rho,c_{0},R)=(\phi_{0}^{\varepsilon,k},d_{0}^{2}/2,R_{*}-\varepsilon K) , we obtain that there exist σ 2 = σ 2 ​ ( ε ¯ , 1 / R ∗ , D 0 ) \sigma_{2}=\sigma_{2}(\bar{\varepsilon},1/R_{*},D_{0}) and C k , 2 = C k , 2 ​ ( M , D 0 , ε ¯ ) > 0 C_{k,2}=C_{k,2}(M,D_{0},\bar{\varepsilon})>0 such that for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} ,

Therefore, setting σ := min ⁡ { σ 1 , σ 2 } \sigma:=\min\{\sigma_{1},\sigma_{2}\} and recalling that ε ¯ = ε ¯ ​ ( M , D 0 , k ) \bar{\varepsilon}=\bar{\varepsilon}(M,D_{0},k) and R ∗ = R ∗ ​ ( M ) R_{*}=R_{*}(M) defined in ( 1.10 ), we see from ( 3.93 ) and ( 3.94 ) that for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} ,

where C k = C k ​ ( M , D 0 , ε ¯ ) > 0 C_{k}=C_{k}(M,D_{0},\bar{\varepsilon})>0 is a constant depending only on the variables indicated.

Clearly, ϕ ~ 0 ε , k ​ ( z ) \widetilde{\phi}_{0}^{\varepsilon,k}(z) satisfies

By the Maximum Principle and ( 3.92 ), we see that ϕ ~ 0 ε , k \widetilde{\phi}_{0}^{\varepsilon,k} can only attain its maximal value on the interval [ − K , K ] [-K,K] for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} . It is easy to see, by applying the Maximum Principle to the equation for ϕ 0 ε , k \phi_{0}^{\varepsilon,k} in ( 3.91 ), that μ 0 ε , k \mu_{0}^{\varepsilon,k} must be bounded above uniformly for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} . Therefore, for any sequences ε n \varepsilon_{n} with lim n → ∞ ε n = 0 \lim_{n\to\infty}\varepsilon_{n}=0 and D n D_{n} satisfying D n ≥ D 0 D_{n}\geq D_{0} , there exists a subsequence (which we still denote by ε n \varepsilon_{n} and D n D_{n} ) such that

Since | ϕ ~ 0 ε n , k ​ ( z ) | ≤ 1 \big|\widetilde{\phi}_{0}^{\varepsilon_{n},k}(z)\big|\leq 1 , by using ( 3.96 ) and ( 3.95 ), interpolation inequalities and a standard compactness argument, we find that, passing to another suitable subsequence of ε n \varepsilon_{n} and D n D_{n} if necessary, ϕ ~ 0 ε n , k \widetilde{\phi}_{0}^{\varepsilon_{n},k} converges to a nonnegative function ϕ ~ 0 ∗ \widetilde{\phi}_{0}^{*} in C l ​ o ​ c 2 ​ ( ℝ ) C^{2}_{loc}(\mathbb{R}) as n → ∞ n\to\infty , where ϕ ~ 0 ∗ \widetilde{\phi}_{0}^{*} satisfies | ϕ ~ 0 ∗ | ≤ 1 |\widetilde{\phi}_{0}^{*}|\leq 1 on ℝ \mathbb{R} , ϕ ~ 0 ∗ ​ ( z ∗ ) = 1 \widetilde{\phi}_{0}^{*}(z_{*})=1 at some point z ∗ ∈ [ − K , K ] z_{*}\in[-K,K] , and

Moreover, the above conclusion combined with ( 3.95 ) implies that ϕ ~ 0 ∗ \widetilde{\phi}_{0}^{*} satisfies the following estimate:

Therefore, multiplying both sides of ( 3.97 ) by w z 0 w^{0}_{z} , integrating over ℝ \mathbb{R} , using integration by parts and then sending n → ∞ n\to\infty , we see from L 0 ​ w z 0 = 0 L^{0}w^{0}_{z}=0 , ( 2.32 ) and ( 3.98 ) that

However, since w z 0 < 0 w^{0}_{z}<0 and ϕ ~ 0 ∗ \widetilde{\phi}_{0}^{*} is a nontrial nonnegative continuous function, this implies μ 0 ∗ = 0 \mu_{0}^{*}=0 . Therefore, ϕ ~ 0 ∗ ∈ C 2 ​ ( ℝ ) \widetilde{\phi}_{0}^{*}\in C^{2}(\mathbb{R}) is a bounded solution which satisfies

This equation has two linearly independent solutions, that is,

The latter one goes to infinity as | z | → ∞ |z|\to\infty , which contradicts ( 3.98 ). Therefore ϕ ~ 0 ∗ = − k ∗ − 1 ​ w z 0 \widetilde{\phi}_{0}^{*}=-k_{*}^{-1}w^{0}_{z} with k ∗ := ‖ w z 0 ‖ L ∞ ​ ( ℝ ) k_{*}:=\|w^{0}_{z}\|_{L^{\infty}(\mathbb{R})} . Since the original sequences ε n \varepsilon_{n} and D n D_{n} could be chosen arbitrarily, we conclude that

Denote

It follows from Theorem 2.2 that u ~ k ε , D \widetilde{u}^{\varepsilon,D}_{k} satisfies

where ℛ ~ ε ​ ( z ) := ℛ ε ​ [ u k ε , D ] ​ ( R ∗ + ε ​ z ) \widetilde{\mathcal{R}}^{\varepsilon}(z):=\mathcal{R}^{\varepsilon}[u^{\varepsilon,D}_{k}](R_{*}+\varepsilon z) . Multiplying the above equation by ( ϕ ~ 0 ε , k ) z (\widetilde{\phi}_{0}^{\varepsilon,k})_{z} , integrating by parts and dividing the result by ε \varepsilon , we obtain that

where

Note that the integral T 4 ε T_{4}^{\varepsilon} is well defined since ( u ~ k ε , D ) z (\widetilde{u}^{\varepsilon,D}_{k})_{z} vanishes near the boundary of the integration interval (cf. ( 2.70 )).

We now estimate T i ε T_{i}^{\varepsilon} for 1 ≤ i ≤ 4 1\leq i\leq 4 in ( 3.101 ).

The following statements hold for T i ε T_{i}^{\varepsilon} :

T 1 ε = 0 T_{1}^{\varepsilon}=0 for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} .

There exists a constant C k = C k ​ ( M , D 0 , ε ¯ ) C_{k}=C_{k}(M,D_{0},\bar{\varepsilon}) such that for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} ,

lim ε → 0 T 4 ε = 0 \lim\limits_{\varepsilon\to 0}T_{4}^{\varepsilon}=0 uniformly in D ≥ D 0 D\geq D_{0} .

We now prove Claim 3.7 . Indeed, Part (i) of Claim 3.7 follows from the fact that both ( ϕ ~ 0 ε , k ) z (\widetilde{\phi}_{0}^{\varepsilon,k})_{z} and ( u ~ k ε , D ) z (\widetilde{u}^{\varepsilon,D}_{k})_{z} vanish at − R ∗ ε -\frac{R_{*}}{\varepsilon} and 1 − R ∗ ε \frac{1-R_{*}}{\varepsilon} . For Part (ii), the first inequality in ( 3.102 ) follows from the uniform boundedness of ϕ ~ 0 ε , k \widetilde{\phi}_{0}^{\varepsilon,k} , ( 3.100 ), ( 2.69 ) and Corollary 2.7 . The second inequality in ( 3.102 ) follows from Theorem 2.2 (ii), ( 3.95 ), ( 3.99 ) and the Dominated Convergence Theorem. It only remains to prove Part (iii) of Claim 3.7 . Using ( 2.55 ) and ( 2.70 ), we obtain

where I 2 = ( − 2 ​ r 0 ε , − r 0 ε ) ∪ ( r 0 ε , 2 ​ r 0 ε ) I_{2}=(-\tfrac{2r_{0}}{\varepsilon},-\tfrac{r_{0}}{\varepsilon})\cup(\tfrac{r_{0}}{\varepsilon},\tfrac{2r_{0}}{\varepsilon}) and I 3 = [ − r 0 ε , r 0 ε ] I_{3}=[-\tfrac{r_{0}}{\varepsilon},\tfrac{r_{0}}{\varepsilon}] are defined in ( 2.55 ). By the Dominated Convergence Theorem, we see from ( 3.99 ), ( 2.70 ) and Proposition 2.1 that for each K ~ > K > 0 \widetilde{K}>K>0 fixed, it holds that

uniformly in D ≥ D 0 D\geq D_{0} . On the other hand, by ( 2.50 ) and ( 2.70 ), ( u ~ k ε , D ) z (\widetilde{u}^{\varepsilon,D}_{k})_{z} is uniformly bounded on I 2 ∪ I 3 I_{2}\cup I_{3} for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} . Hence, it follows from ( 3.95 ) that there exists a constant C k = C k ​ ( M , D 0 , ε ¯ ) > 0 C_{k}=C_{k}(M,D_{0},\bar{\varepsilon})>0 such that

for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} . Consequently, by choosing K ~ \widetilde{K} sufficiently large first and then sending ε → 0 \varepsilon\to 0 in ( 3.103 ), we see from Proposition 2.1 and the above two estimates that Part (iii) of Claim 3.7 holds. This completes the proof of Claim 3.7 .

We now estimate the right hand side of ( 3.101 ). Since, by ( 2.70 ),

we see from ( 2.32 ), ( 2.70 ), ( 3.99 ), ( 3.95 ) and the Dominated Convergence Theorem that

Now, sending ε → 0 \varepsilon\to 0 in ( 3.101 ), we conclude from Claim 3.7 and ( 3.104 ) that

This finished the proof of ( 3.86 ).

Next, we prove ( 3.87 ). We now rescale ϕ 0 ε , k \phi_{0}^{\varepsilon,k} by a normalization constant c ε > 0 c_{\varepsilon}>0 such that c ε ​ ϕ 0 ε , k c_{\varepsilon}\phi_{0}^{\varepsilon,k} is L 2 L^{2} -normalized. Then by ( 3.95 ), ( 3.99 ) and similar arguments as above, we see that

uniformly in D ≥ D 0 D\geq D_{0} , which implies that

This combined with ( 3.99 ) implies ( 3.87 ).

Finally, assume that now ϕ 0 ε , k \phi_{0}^{\varepsilon,k} is L 2 L^{2} -normalized, then ( 3.88 ) follows from ( 3.87 ), ( 3.93 ) and ( 3.94 ). This finishes the proof of the proposition. ∎

Assume that conditions (A1) - (A3) hold. Let M ∈ I v ∗ M\in I_{v^{*}} be given and ϕ 0 ε , k \phi_{0}^{\varepsilon,k} be the L 2 L^{2} -normalized, positive, principal eigenfunction of ℒ k ε \mathcal{L}^{\varepsilon}_{k} corresponding to μ 0 ε , k \mu_{0}^{\varepsilon,k} . Then for each D 0 > 0 D_{0}>0 and g ∈ C r ​ a ​ d ​ ( Ω ¯ ) g\in C_{rad}(\bar{\Omega}) , we have

uniformly in D ≥ D 0 D\geq D_{0} , where ⟨ ⋅ , ⋅ ⟩ \langle\cdot,\cdot\rangle denotes the standard Hilbert inner product in L 2 ​ ( Ω ) L^{2}(\Omega) and C r ​ a ​ d ​ ( Ω ¯ ) C_{rad}(\bar{\Omega}) denotes for the subspace of all radially symmetric functions in C ⁡ ( Ω ¯ ) C(\bar{\Omega}) .

By using ( 3.87 ) and ( 2.52 ), we have

where we used ( 2.52 ), ( 2.70 ), ( 3.87 ), ( 3.95 ), Theorem 2.2 (iii) and the Dominated Convergence Theorem. This proves ( 3.106 ). The proof of ( 3.105 ) is similar and thus omitted. ∎

By elliptic regularity theory, the principal eigenfunction ϕ 0 ε , k \phi_{0}^{\varepsilon,k} of ℒ k ε \mathcal{L}^{\varepsilon}_{k} belongs to C 2 + α ​ ( Ω ¯ ) C^{2+\alpha}(\bar{\Omega}) for some 0 < α < 1 0<\alpha<1 . Hence ϕ 0 ε , k ∈ L r ​ a ​ d s \phi_{0}^{\varepsilon,k}\in L_{rad}^{s} for 1 ≤ s ≤ ∞ 1\leq s\leq\infty . Now for each 1 < s ≤ ∞ 1<s\leq\infty , define

Set

Since the resolvent of ℒ k ε \mathcal{L}^{\varepsilon}_{k} is compact and Proposition 3.6 ensures that

for each s ∈ ( 1 , ∞ ) s\in(1,\infty) , the following lemma follows directly from the Riesz-Schauder theory.

Assume that conditions (A1) - (A3) hold. Let M ∈ I v ∗ M\in I_{v^{*}} be given. Then the closed linear operator ℒ k ε − μ 0 ε , k \mathcal{L}^{\varepsilon}_{k}-\mu_{0}^{\varepsilon,k} has a bounded right inverse ( ℒ k ε − μ 0 ε , k ) − 1 (\mathcal{L}^{\varepsilon}_{k}-\mu_{0}^{\varepsilon,k})^{-1} from Y s Y^{s} to Y ν 2 , s Y_{\nu}^{2,s} for each ε > 0 \varepsilon>0 , D > 0 D>0 , k ∈ ℕ k\in\mathbb{N} and 1 < s < ∞ 1<s<\infty .

Now, given g ∈ Y ∞ g\in Y^{\infty} , by Lemma 3.9 and similar arguments just before Lemma 3.3 , we can see that the equation

has a unique solution h ∈ Y ∞ ∩ C α ​ ( Ω ¯ ) h\in Y^{\infty}\cap C^{\alpha}(\bar{\Omega}) for some 0 < α < 1 0<\alpha<1 . Hence, ( ℒ k ε − μ 0 ε , k ) − 1 (\mathcal{L}^{\varepsilon}_{k}-\mu_{0}^{\varepsilon,k})^{-1} may be considered as a linear mapping from Y ∞ Y^{\infty} into Y ∞ Y^{\infty} . Now we are ready to show the following result.

Assume that conditions (A1) - (A3) hold. Let M ∈ I v ∗ M\in I_{v^{*}} be given. Then for each D 0 > 0 D_{0}>0 and integer k ≥ 1 k\geq 1 , there exists a constant ε ¯ = ε ¯ ​ ( M , D 0 , k ) > 0 \bar{\varepsilon}=\bar{\varepsilon}(M,D_{0},k)>0 such that the inverse operator ( ℒ k ε − μ 0 ε , k ) − 1 : Y ∞ → Y ∞ (\mathcal{L}^{\varepsilon}_{k}-\mu_{0}^{\varepsilon,k})^{-1}:Y^{\infty}\to Y^{\infty} exists and there exists a constant C k = C k ​ ( M , D 0 , ε ¯ ) > 0 C_{k}=C_{k}(M,D_{0},\bar{\varepsilon})>0 satisfying

for all g ∈ Y ∞ g\in Y^{\infty} , ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} .

We prove ( 3.108 ) by contradiction. Assume that there exist two sequences of parameters ε n → 0 \varepsilon_{n}\to 0 , D n ≥ D 0 D_{n}\geq D_{0} and a sequence { g n } ⊂ Y ∞ \{g_{n}\}\subset Y^{\infty} such that

Denote

Then ϱ n \varrho_{n} satisfies

with ‖ ϱ n ‖ L ∞ = 1 \|\varrho_{n}\|_{L^{\infty}}=1 and ‖ q n ‖ L ∞ ≤ 1 n \|q_{n}\|_{L^{\infty}}\leq\frac{1}{n} . Since ϱ n ∈ Y ∞ ∩ C α ​ ( Ω ¯ ) \varrho_{n}\in Y^{\infty}\cap C^{\alpha}(\bar{\Omega}) , replacing ( ϱ n , q n ) (\varrho_{n},q_{n}) with ( − ϱ n , − q n ) (-\varrho_{n},-q_{n}) if necessary, we see that for each n n , there exists some r n ∈ [ 0 , 1 ] r_{n}\in[0,1] such that ‖ ϱ n ‖ L ∞ = ϱ n ​ ( r n ) = 1 \|\varrho_{n}\|_{L^{\infty}}=\varrho_{n}(r_{n})=1 .

Since ‖ q n ‖ L ∞ → 0 \|q_{n}\|_{L^{\infty}}\to 0 and μ n := μ 0 ε n , k = o ⁡ ( ε n ) \mu_{n}:=\mu_{0}^{\varepsilon_{n},k}=o(\varepsilon_{n}) as ε n → 0 \varepsilon_{n}\to 0 by ( 3.86 ), by similar arguments as in the proof of Proposition 3.6 , we see from the equation for ϱ n \varrho_{n} that r n ∈ [ R ∗ − ε n ​ K , R ∗ + ε n ​ K ] r_{n}\in[R_{*}-\varepsilon_{n}K,R_{*}+\varepsilon_{n}K] for all n n large. We now express r n = R ∗ + ε n ​ z n r_{n}=R_{*}+\varepsilon_{n}z_{n} and the equation for ϱ n \varrho_{n} in terms of the stretched variable z = x − R ∗ − ε n ​ z n ε n z=\tfrac{x-R_{*}-\varepsilon_{n}z_{n}}{\varepsilon_{n}} by ϱ ^ n ​ ( z ) = ϱ n ​ ( R ∗ + ε n ​ ( z n + z ) ) \widehat{\varrho}_{n}(z)=\varrho_{n}(R_{*}+\varepsilon_{n}(z_{n}+z)) . Then | z n | ≤ K |z_{n}|\leq K and the equation for ϱ ^ n ​ ( z ) \widehat{\varrho}_{n}(z) is

where q ^ n ​ ( z ) = q n ​ ( R ∗ + ε n ​ ( z n + z ) ) \widehat{q}_{n}(z)=q_{n}(R_{*}+\varepsilon_{n}(z_{n}+z)) . Since ‖ ϱ ^ n ‖ L ∞ = 1 \|\widehat{\varrho}_{n}\|_{L^{\infty}}=1 and | z n | ≤ K |z_{n}|\leq K for all n n , the compactness argument implies that there exist subsequences, which are still denoted by { ε n } \{\varepsilon_{n}\} , { z n } \{z_{n}\} and { ϱ ^ n } \{\widehat{\varrho}_{n}\} , such that

Passing to the limit as n → ∞ n\to\infty in the weak version ( H 1 H^{1} -formation) of ( 3.109 ), and using regularity arguments, we find that ϱ ^ 0 ∈ C 2 ​ ( ℝ ) \widehat{\varrho}_{0}\in C^{2}(\mathbb{R}) satisfies ϱ ^ 0 ​ ( 0 ) = 1 \widehat{\varrho}_{0}(0)=1 , ( ϱ ^ 0 ) z ​ ( 0 ) = 0 (\widehat{\varrho}_{0})_{z}(0)=0 and

Since ϱ ^ 0 \widehat{\varrho}_{0} is a bounded solution with ϱ ^ 0 ​ ( 0 ) = 1 \widehat{\varrho}_{0}(0)=1 , ϱ ^ 0 \widehat{\varrho}_{0} must be a multiple of the principal eigenfunction w z 0 ​ ( z + z ∗ ) w^{0}_{z}(z+z_{*}) of L z ∗ 0 L^{0}_{z_{*}} , namely, ϱ ^ 0 = c ​ w z 0 ​ ( z + z ∗ ) \widehat{\varrho}_{0}=cw^{0}_{z}(z+z_{*}) for some constant c ≠ 0 c\neq 0 . However, since ϱ n ∈ Y ∞ \varrho_{n}\in Y^{\infty} , we see from ( 3.107 ) that

where ϕ ^ 0 ε n , k ​ ( z ) = ϕ 0 ε n , k ​ ( R ∗ + ε n ​ z n + ε n ​ z ) \widehat{\phi}_{0}^{\varepsilon_{n},k}(z)=\phi_{0}^{\varepsilon_{n},k}(R_{*}+\varepsilon_{n}z_{n}+\varepsilon_{n}z) . Sending n → ∞ n\to\infty , it follows from ( 3.87 ), ( 3.95 ), ( 3.110 ), ‖ ϱ ^ n ‖ L ∞ = 1 \|\widehat{\varrho}_{n}\|_{L^{\infty}}=1 and the Dominated Convergence Theorem that

Therefore, c = 0 c=0 and hence ϱ ^ 0 ≡ 0 \widehat{\varrho}_{0}\equiv 0 , which contradicts to ϱ ^ 0 ​ ( 0 ) = 1 \widehat{\varrho}_{0}(0)=1 . So we are done. ∎

Since eigenfunctions associated with μ 1 ε \mu_{1}^{\varepsilon} of ℒ k ε \mathcal{L}^{\varepsilon}_{k} belong to Y ∞ Y^{\infty} , the follow result follows directly from Lemma 3.10 .

Assume that conditions (A1) - (A3) hold. Let M ∈ I v ∗ M\in I_{v^{*}} be given and μ 1 ε , k \mu_{1}^{\varepsilon,k} be the second eigenvalue of the operator ℒ k ε \mathcal{L}^{\varepsilon}_{k} . Then for each D 0 > 0 D_{0}>0 and integer k ≥ 1 k\geq 1 , there exists a constant ε ¯ = ε ¯ ​ ( M , D 0 , k ) > 0 \bar{\varepsilon}=\bar{\varepsilon}(M,D_{0},k)>0 such that

where μ ∗ = μ ∗ ​ ( M , D 0 , k ) > 0 \mu_{*}=\mu_{*}(M,D_{0},k)>0 is a constant depending only on the indicated parameters.

We denote [ ϕ 0 ε , k ] ⟂ [\phi_{0}^{\varepsilon,k}]^{\perp} as the orthogonal complement of ϕ 0 ε , k \phi_{0}^{\varepsilon,k} in L r ​ a ​ d 2 L^{2}_{rad} and 𝒫 ε : L r ​ a ​ d 2 → L r ​ a ​ d 2 \mathcal{P}^{\varepsilon}:L^{2}_{rad}\to L^{2}_{rad} as the orthogonal projection operator onto [ ϕ 0 ε , k ] ⟂ [\phi_{0}^{\varepsilon,k}]^{\perp} . Now we are ready to show the following result.

Assume that conditions (A1) - (A3) hold. Let M ∈ I v ∗ M\in I_{v^{*}} , D 0 > 0 D_{0}>0 and integer k ≥ 1 k\geq 1 be given. Then there exists a constant ε ¯ = ε ¯ ​ ( M , D 0 , k ) > 0 \bar{\varepsilon}=\bar{\varepsilon}(M,D_{0},k)>0 such that the following statements hold.

The inverse operator ( ℒ k ε − μ ) − 1 : [ ϕ 0 ε , k ] ⟂ → [ ϕ 0 ε , k ] ⟂ (\mathcal{L}^{\varepsilon}_{k}-\mu)^{-1}:[\phi_{0}^{\varepsilon,k}]^{\perp}\to[\phi_{0}^{\varepsilon,k}]^{\perp} exists and is L 2 L^{2} -bounded uniformly in ( ε , D ) ∈ ( 0 , ε ¯ ] × [ D 0 , ∞ ) (\varepsilon,D)\in(0,\bar{\varepsilon}]\times[D_{0},\infty) and μ ∈ ℂ \mu\in\mathbb{C} with Re ⁡ μ > − μ ∗ \re\mu>-\mu_{*} , where μ ∗ \mu_{*} is defined as in Corollary 3.11 . Moreover, for g ∈ L r ​ a ​ d 2 g\in L_{rad}^{2} and μ ∈ ℂ \mu\in\mathbb{C} with Re ⁡ μ > − μ ∗ \re\mu>-\mu_{*} ,

for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} .

Let F F be a smooth function in ℝ 2 \mathbb{R}^{2} . Define

Denote

where f u ∗ , ± f_{u}^{*,\pm} are defined in ( 3.1 ). Then for any g ∈ L r ​ a ​ d ∞ g\in L_{rad}^{\infty} and μ ∈ ℂ \mu\in\mathbb{C} with Re ⁡ μ ≥ − μ ^ \re\mu\geq-\widehat{\mu} ,

uniform in D ≥ D 0 D\geq D_{0} and μ ∈ { μ ∈ ℂ | Re ⁡ μ ≥ − μ ^ } \mu\in\{\mu\in\mathbb{C}\,|\,\re\mu\geq-\widehat{\mu}\} , where f u ∗ ​ ( x ) f_{u}^{*}(x) is defined in ( 3.74 ).

Part (i) follows directly from Corollary 3.11 and the eigenfunction expansion of the resolvent operator ( ℒ k ε − μ ) − 1 (\mathcal{L}_{k}^{\varepsilon}-\mu)^{-1} .

For Part (ii), we refer the reader to the proof of [ 32 , Lemma 2.2] . ∎


## 3.3. Proofs of Lemmas 3.4 and 3.5

We only need to find suitable barrier functions. Let

where σ 1 > 0 \sigma_{1}>0 is a constant to be determined later. Then by direct computation, we see that

Since | tanh ⁡ ( σ 1 ​ d ​ ( x ) / ε ) | < 1 |\tanh(\sigma_{1}d(x)/\varepsilon)|<1 and Δ ​ d \Delta d is uniformly bounded on W δ ¯ \overline{W_{\delta}} , there exists a constant σ 1 = σ 1 ​ ( ε 0 , ‖ Δ ​ d ‖ L ∞ ​ ( W δ ) , c 0 ) > 0 \sigma_{1}=\sigma_{1}\big(\varepsilon_{0},\|\Delta d\|_{L^{\infty}(W_{\delta})},c_{0}\big)>0 such that

Let

Then

Therefore, by the maximum principle, we see that ϑ 1 ​ ( x ) ≤ 0 \vartheta_{1}(x)\leq 0 in W δ W_{\delta} . Using the fact that e y 2 ≤ cosh ⁡ ( y ) ≤ e y \frac{e^{y}}{2}\leq\cosh(y)\leq e^{y} for all y ≥ 0 y\geq 0 , we obtain that

Similarly, by working with ρ ⁡ ( x ) + η 1 ​ ( x ) cosh ⁡ ( σ 1 ​ δ / ε ) ​ ‖ ρ ‖ L ∞ ​ ( W δ ) \rho(x)+\frac{\eta_{1}(x)}{\cosh(\sigma_{1}\delta/\varepsilon)}\|\rho\|_{L^{\infty}(W_{\delta})} , we can show that

Combining the above two inequalities, we obtain the first estimate in ( 3.84 ).

The second estimate in ( 3.84 ) follows from the standard pointwise interpolation inequality for derivatives. See. e.g., [ 12 , Chapter 3.4] . ∎

Let η 2 ​ ( x ) = cosh ⁡ ( σ 2 ​ | x | / ε ) \eta_{2}(x)=\cosh(\sigma_{2}|x|/\varepsilon) , where σ 2 > 0 \sigma_{2}>0 is a constant to be determined later. Then by direct computation, we see that

Note that

and the supremum depends only on σ ¯ 2 > 0 \bar{\sigma}_{2}>0 , N N , ε 0 \varepsilon_{0} and R R . Therefore, there exists a constant σ 2 = σ 2 ​ ( ε 0 , R , c 0 , N ) > 0 \sigma_{2}=\sigma_{2}(\varepsilon_{0},R,c_{0},N)>0 such that

Let

Then the rest of the proof follows from similar arguments as in the proof of Lemma 3.4 . Hence, we omit the details. ∎


## 3.4. Proof of Theorem 3.1

Let M ∈ I v ∗ M\in I_{v^{*}} , D 0 > 0 D_{0}>0 and integer k ≥ 1 k\geq 1 be given.

We begin by analyzing the eigenvalue of ℒ k ε \mathscr{L}_{k}^{\varepsilon} with the largest real part. To this end, define

where μ ^ > 0 \widehat{\mu}>0 is given by ( 3.113 ), and E < 0 E<0 , G > 0 G>0 are defined in ( 3.1 ). Next, we introduce the domain

Our first objective is to characterize the spectrum of ℒ k ε \mathscr{L}_{k}^{\varepsilon} in the region ℂ λ ∗ \mathbb{C}_{\lambda_{*}} , in order to establish Theorem 3.1 (i) and (ii).

In the sequel, we assume that λ ε ∈ ℂ λ ∗ \lambda^{\varepsilon}\in\mathbb{C}_{\lambda_{*}} is an eigenvalue of ℒ k ε \mathscr{L}_{k}^{\varepsilon} , and let Φ ε \Phi^{\varepsilon} be a corresponding eigenfunction.

Let ( μ 0 ε , k , ϕ 0 ε , k ) (\mu_{0}^{\varepsilon,k},\phi_{0}^{\varepsilon,k}) be the principal eigenpair of the operator ℒ k ε \mathcal{L}_{k}^{\varepsilon} defined in ( 3.83 ) with ϕ 0 ε , k \phi_{0}^{\varepsilon,k} being L 2 L^{2} -normalized. We decompose Φ ε \Phi^{\varepsilon} as

Then the equation for Φ ε \Phi^{\varepsilon} can be reformulated as follows:

Thanks to Proposition 3.12 (i) and the assumption that λ ε ∈ ℂ λ ∗ \lambda^{\varepsilon}\in\mathbb{C}_{\lambda_{*}} , η ε \eta^{\varepsilon} can be solved from the second equation in ( 3.4 ) as

For notational simplicity, denote

and

Integrating equation ( 3.119 ) over Ω \Omega , we obtain that

We will first prove Parts (i)-(ii) of Theorem 3.1 . Since the proof is rather lengthy, we structure it by isolating several key intermediate results as Claims 3.13 - 3.18 below. Each claim establishes a crucial step in the argument, and together they lead to the proof of Theorem 3.1 (i)-(ii).

There exists a constant ε ¯ = ε ¯ ​ ( M , D 0 , k ) > 0 \bar{\varepsilon}=\bar{\varepsilon}(M,D_{0},k)>0 such that for each ( ε , λ ε ) ∈ ( 0 , ε ¯ ] × ℂ λ ∗ (\varepsilon,\lambda^{\varepsilon})\in(0,\bar{\varepsilon}]\times\mathbb{C}_{\lambda_{*}} and D ≥ D 0 D\geq D_{0} , equation ( 3.122 ) admits a unique solution given explicitly by

Indeed, it follows from ( 3.121 ) and Proposition 3.12 (ii) that

uniformly in ξ ∈ ℂ λ ∗ \xi\in\mathbb{C}_{\lambda_{*}} and D ≥ D 0 D\geq D_{0} , where f v ∗ f^{*}_{v} and f u ∗ f^{*}_{u} are defined in ( 3.74 ). Consequently,

uniformly in ξ ∈ ℂ λ ∗ \xi\in\mathbb{C}_{\lambda_{*}} and D ≥ D 0 D\geq D_{0} . By the definition of λ ∗ \lambda_{*} in ( 3.115 ), the right-hand side of ( 3.125 ) remains uniformly bounded away from zero for all ξ ∈ ℂ λ ∗ \xi\in\mathbb{C}_{\lambda_{*}} . Therefore, there exists a constant ε ¯ = ε ¯ ​ ( M , D 0 , k ) > 0 \bar{\varepsilon}=\bar{\varepsilon}(M,D_{0},k)>0 small such that

This ensures that b ε b^{\varepsilon} is uniquely solvable from equation ( 3.122 ) and is given by ( 3.123 ), which concludes the proof of Claim 3.13 .

Let ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} . Then for λ ε ∈ ℂ λ ∗ \lambda^{\varepsilon}\in\mathbb{C}_{\lambda_{*}} to be an eigenvalue of ℒ k ε \mathscr{L}_{k}^{\varepsilon} , it is necessary that a ε ≠ 0 a^{\varepsilon}\neq 0 in ( 3.116 ).

Suppose for contradiction that Claim 3.14 is false, i.e., a ε = 0 a^{\varepsilon}=0 . Then we see from ( 3.123 ) that b ε = 0 b^{\varepsilon}=0 . This combined with ( 3.119 ) and ( 3.120 ) implies that η ε = 0 \eta^{\varepsilon}=0 and thus Φ ε = 0 \Phi^{\varepsilon}=0 , which is a contradiction since Φ ε \Phi^{\varepsilon} is an eigenfunction of ℒ k ε \mathscr{L}_{k}^{\varepsilon} . This finishes the proof of Claim 3.14 .

By Claim 3.14 , we may, without loss of generality, set

in the remainder of this proof. Substituting a ε = 1 a^{\varepsilon}=1 , ( 3.120 ) and the expression ( 3.123 ) into the first equation of ( 3.4 ), we obtain:

where Λ ∗ \Lambda^{*} is defined in ( 3.80 ).

We now prove Claim 3.15 . Let ε ¯ \bar{\varepsilon} be given as in Claim 3.13 . We first show that, by choosing ε ¯ \bar{\varepsilon} even smaller if necessary, there exists a constant C k = C k ​ ( M , D 0 , ε ¯ ) > 0 C_{k}=C_{k}(M,D_{0},\bar{\varepsilon})>0 such that

We now prove ( 3.128 ). Since the RHS of ( 3.125 ) is a rational function of ξ \xi whose numerator and denominator have the same degree, its modulus is uniformly bounded from above and below by two positive constants in the region ℂ λ ∗ \mathbb{C}_{\lambda_{*}} , due to our choice of λ ∗ \lambda_{*} in ( 3.115 ). Therefore, choosing ε ¯ \bar{\varepsilon} even smaller if necessary, we see from ( 3.125 ) that there exists two constants c ¯ 1 , c ¯ 2 > 0 \bar{c}_{1},\bar{c}_{2}>0 , depending only on M M , D 0 D_{0} , k k and ε ¯ \bar{\varepsilon} , such that

On the other hand, we see from Corollary 3.8 that

both of which hold uniformly in D ≥ D 0 D\geq D_{0} . Therefore, ( 3.128 ) follows directly from ( 3.86 ), ( 3.126 ) and ( 3.129 )-( 3.131 ).

We now prove ( 3.127 ). By ( 3.125 ) and ( 3.128 ), we see that

Dividing both sides of ( 3.126 ) by ε \varepsilon and sending ε → 0 \varepsilon\to 0 , we see from ( 3.86 ) and ( 3.130 )-( 3.132 ) that

uniformly with D ≥ D 0 D\geq D_{0} . This finishes the proof of Claim 3.15 and hence ( 3.79 ).

Let ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} . Then for λ ε ∈ ℂ λ ∗ \lambda^{\varepsilon}\in\mathbb{C}_{\lambda_{*}} to be an eigenvalue of ℒ k ε \mathscr{L}_{k}^{\varepsilon} , it is necessary that λ ε \lambda^{\varepsilon} is real, i.e., Im ⁡ λ ε = 0 \im\lambda^{\varepsilon}=0 .

We now prove Claim 3.16 . Since Λ ∗ ∈ ℝ \Lambda^{*}\in\mathbb{R} , it follows from ( 3.127 ) that

On the other hand, we see from ( 3.126 ) that

Recall that ψ λ ε ε \psi_{\lambda^{\varepsilon}}^{\varepsilon} is defined in ( 3.121 ), which can be rewritten in the form

where 𝒫 ε \mathcal{P}^{\varepsilon} denotes the orthogonal projection onto [ ϕ 0 ε , k ] ⟂ [\phi_{0}^{\varepsilon,k}]^{\perp} . Then, by choosing ε ¯ \bar{\varepsilon} even smaller if necessary, Lemma 3.10 implies that there exists a constant C k = C k ​ ( M , D 0 , ε ¯ ) > 0 C_{k}=C_{k}(M,D_{0},\bar{\varepsilon})>0 such that for all ( ε , λ ε ) ∈ ( 0 , ε ¯ ] × ℂ λ ∗ (\varepsilon,\lambda^{\varepsilon})\in(0,\bar{\varepsilon}]\times\mathbb{C}_{\lambda_{*}} and D ≥ D 0 D\geq D_{0} ,

Here, to obtain the last inequality, we used ( 3.86 ) and ( 3.127 ) to ensure that C k ​ | λ ε − μ 0 ε , k | ≤ 1 2 C_{k}|\lambda^{\varepsilon}-\mu_{0}^{\varepsilon,k}|\leq\frac{1}{2} , Theorem 2.2 to ensure ‖ f v ε , k ‖ L ∞ ≤ C k \|f_{v}^{\varepsilon,k}\|_{L^{\infty}}\leq C_{k} , and ( 3.130 ) and ( 3.131 ) to control the last term. Consequently, we arrive at

Rewrite ( 3.121 ) into its real and imaginary parts respectively, we see that

Then, arguing as in the proof of ( 3.136 ), we obtain that, for all ( ε , λ ε ) ∈ ( 0 , ε ¯ ] × ℂ λ ∗ (\varepsilon,\lambda^{\varepsilon})\in(0,\bar{\varepsilon}]\times\mathbb{C}_{\lambda_{*}} and D ≥ D 0 D\geq D_{0} ,

where, in the last inequality, we used ( 3.136 ). By direct computation, we see from ( 3.132 ), ( 3.133 ) and ( 3.137 ) that for all ( ε , λ ε ) ∈ ( 0 , ε ¯ ] × ℂ λ ∗ (\varepsilon,\lambda^{\varepsilon})\in(0,\bar{\varepsilon}]\times\mathbb{C}_{\lambda_{*}} and D ≥ D 0 D\geq D_{0} ,

Using the estimates ( 3.130 ), ( 3.131 ) and ( 3.138 ), we see from ( 3.134 ) that

By choosing ε ¯ \bar{\varepsilon} eventually smaller such that C k ​ ε ¯ < 1 C_{k}\bar{\varepsilon}<1 , the above inequality yields Im ⁡ λ ε = 0 \im\lambda^{\varepsilon}=0 for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 . D\geq D_{0}. This finishes the proof of Claim 3.16 .

Let ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} . Then equation ( 3.126 ) has a unique solution λ ε \lambda^{\varepsilon} in ℂ λ ∗ \mathbb{C}_{\lambda_{*}} .

We now prove Claim 3.17 . Define a map Γ k ε : [ − λ ∗ ε , ∞ ) → ℝ \Gamma_{k}^{\varepsilon}:[-\frac{\lambda_{*}}{\varepsilon},\infty)\to\mathbb{R} as

Then equation ( 3.126 ) is equivalent to Γ k ε ​ ( λ ε ε ) = λ ε ε \Gamma_{k}^{\varepsilon}(\frac{\lambda^{\varepsilon}}{\varepsilon})=\frac{\lambda^{\varepsilon}}{\varepsilon} . Therefore, by choosing ε ¯ \bar{\varepsilon} even smaller if necessary, we see from Claims 3.15 and 3.16 that, to prove Claim 3.17 , it suffices to prove uniqueness of solution to the equation Γ k ε ​ ( β ) = β \Gamma_{k}^{\varepsilon}(\beta)=\beta on the interval I Λ ∗ I_{\Lambda^{*}} for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} , where

Indeed, it follows from ( 3.135 ) that for any β 1 , β 2 ∈ I Λ ∗ \beta_{1},\beta_{2}\in I_{\Lambda^{*}} ,

Then, by ( 3.136 ) and similar arguments to the proof of ( 3.136 ), we see that

Then, by using estimates ( 3.130 ), ( 3.131 ), ( 3.132 ), the above inequality and similar arguments to the proof of Claim 3.15 , one can easily show that

for all β , β 1 , β 2 ∈ I Λ ∗ \beta,\beta_{1},\beta_{2}\in I_{\Lambda^{*}} , ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} . By the contraction mapping theorem, β = Γ k ε ​ ( β ) \beta=\Gamma_{k}^{\varepsilon}(\beta) has a unique solution in I Λ ∗ I_{\Lambda^{*}} for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} . So we are done.

The nonlocal eigenvalue problem ( 3.71 ) has a unique eigenvalue λ ε \lambda^{\varepsilon} in ℂ λ ∗ \mathbb{C}_{\lambda_{*}} , and it is a simple.

Indeed, by Claim 3.17 , λ ε \lambda^{\varepsilon} is uniquely determined from the equation ( 3.126 ). Substituting ( 3.120 ), ( 3.121 ), ( 3.123 ) and a ε = 1 a^{\varepsilon}=1 into ( 3.119 ), we obtain that

This implies that the second equation in ( 3.4 ) also admits a unique solution for given λ ε \lambda^{\varepsilon} . Therefore, λ ε \lambda^{\varepsilon} is the unique eigenvalue of ℒ k ε \mathscr{L}_{k}^{\varepsilon} in ℂ λ ∗ \mathbb{C}_{\lambda_{*}} , and there exists an eigenfunction Φ ε = ϕ 0 ε , k + η ε \Phi^{\varepsilon}=\phi_{0}^{\varepsilon,k}+\eta^{\varepsilon} of ℒ k ε \mathscr{L}_{k}^{\varepsilon} corresponding to λ ε \lambda^{\varepsilon} , which is unique up to a constant multiple. This finishes the proof of Claim 3.18 .

Now Theorem 3.1 (i) and (ii) follows directly from Claims 3.15 - 3.18 .

For definiteness, we henceforth denote the critical eigenvalue λ ε \lambda^{\varepsilon} of ℒ k ε \mathscr{L}_{k}^{\varepsilon} in ℂ λ ∗ \mathbb{C}_{\lambda_{*}} by λ 0 ε , k \lambda_{0}^{\varepsilon,k} and the corresponding eigenfunction Φ ε \Phi^{\varepsilon} by Φ 0 ε , k \Phi_{0}^{\varepsilon,k} in the remainder of this proof.

Next, we prove Theorem 3.1 (iii). Plugging the estimates ( 3.88 ), ( 3.132 ) and ( 3.136 ) into ( 3.139 ), we immediately obtain that there exists a constant C k = C k ​ ( M , D 0 , ε ¯ ) C_{k}=C_{k}(M,D_{0},\bar{\varepsilon}) such that for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} ,

Therefore, dividing Φ 0 ε , k = ϕ 0 ε , k + η ε \Phi_{0}^{\varepsilon,k}=\phi_{0}^{\varepsilon,k}+\eta^{\varepsilon} by ‖ Φ 0 ε , k ‖ L 2 \|\Phi_{0}^{\varepsilon,k}\|_{L^{2}} so that the resulting function is L 2 L^{2} -normalized and still denoting the resulting function by Φ 0 ε , k \Phi_{0}^{\varepsilon,k} , we see from ( 3.88 ) and ( 3.140 ) that

for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} . This finishes the proof of Theorem 3.1 (iii).

Finally, we prove Theorem 3.1 (iv). Note that the adjoint operator ℒ ^ k ε \widehat{\mathscr{L}}_{k}^{\varepsilon} on L s ​ ( Ω ) L^{s}(\Omega) with domain W ν 2 , s W_{\nu}^{2,s} is defined as:

In the sequel, we assume that λ ^ ε ∈ ℂ λ ∗ \widehat{\lambda}^{\varepsilon}\in\mathbb{C}_{\lambda_{*}} is an eigenvalue of ℒ ^ k ε \widehat{\mathscr{L}}_{k}^{\varepsilon} , and let Φ ^ ε \widehat{\Phi}^{\varepsilon} be a corresponding eigenfunction. We then proceed by applying similar arguments as those used in the proofs of Theorem 3.1 (i)-(iii).

Decompose Φ ^ ε \widehat{\Phi}^{\varepsilon} as

then the equation for Φ ^ ε \widehat{\Phi}^{\varepsilon} can be reformulated as follows:

where 𝟙 \mathds{1} denotes the constant function taking value 1 1 on Ω \Omega . Thanks to Proposition 3.12 (i) and the assumption that λ ^ ε ∈ ℂ λ ∗ \widehat{\lambda}^{\varepsilon}\in\mathbb{C}_{\lambda_{*}} , we can solve for η ^ ε \widehat{\eta}^{\varepsilon} from the second equation in ( 3.4 ). Multiplying the resulting expression of η ^ ε \widehat{\eta}^{\varepsilon} by f v ε , k f_{v}^{\varepsilon,k} yields

For notational simplicity, denote

Integrating equation ( 3.145 ) over Ω \Omega , we obtain that

By similar arguments as in the proof of Claim 3.13 , we see that there exists a constant ε ¯ = ε ¯ ​ ( M , D 0 , k ) > 0 \bar{\varepsilon}=\bar{\varepsilon}(M,D_{0},k)>0 such that for each ( ε , λ ^ ε ) ∈ ( 0 , ε ¯ ] × ℂ λ ∗ (\varepsilon,\widehat{\lambda}^{\varepsilon})\in(0,\bar{\varepsilon}]\times\mathbb{C}_{\lambda_{*}} and D ≥ D 0 D\geq D_{0} , equation ( 3.147 ) admits a unique solution given explicitly by

Then, by reasoning analogous to that used in the proof of Claim 3.14 , we deduce from ( 3.148 ) that for λ ^ ε ∈ ℂ λ ∗ \widehat{\lambda}^{\varepsilon}\in\mathbb{C}_{\lambda_{*}} to be an eigenvalue of ℒ ^ k ε \widehat{\mathscr{L}}_{k}^{\varepsilon} , it is necessary that

Substituting ( 3.146 ) and ( 3.148 ) into the first equation of ( 3.4 ) and canceling the factor a ^ ε ≠ 0 \widehat{a}^{\varepsilon}\neq 0 on both sides, we obtain the following explicit expression for λ ^ ε \widehat{\lambda}^{\varepsilon} :

Then by similar arguments to the proofs used in Claims 3.15 - 3.18 , we obtain:

Let ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} . Then the L 2 L^{2} -adjoint operator ℒ ^ k ε \widehat{\mathscr{L}}_{k}^{\varepsilon} of ℒ k ε \mathscr{L}_{k}^{\varepsilon} has a unique eigenvalue λ ^ ε \widehat{\lambda}^{\varepsilon} in ℂ λ ∗ \mathbb{C}_{\lambda_{*}} , and it is a simple. Moreover, λ ^ ε \widehat{\lambda}^{\varepsilon} is real and satisfies

where Λ ∗ \Lambda^{*} is defined in ( 3.80 ).

We henceforth denote the critical eigenvalue λ ^ ε \widehat{\lambda}^{\varepsilon} of ℒ ^ k ε \widehat{\mathscr{L}}_{k}^{\varepsilon} in ℂ λ ∗ \mathbb{C}_{\lambda_{*}} by λ ^ 0 ε , k \widehat{\lambda}_{0}^{\varepsilon,k} and the corresponding eigenfunction Φ ^ ε \widehat{\Phi}^{\varepsilon} by Φ ^ 0 ε , k \widehat{\Phi}_{0}^{\varepsilon,k} in the remainder of this paper.

By similar arguments to the proof of ( 3.140 ), we can show that there exists a constant C k = C k ​ ( M , D 0 , ε ¯ ) > 0 C_{k}=C_{k}(M,D_{0},\bar{\varepsilon})>0 such that for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} ,

We now claim that

λ 0 ε , k = λ ^ 0 ε , k \lambda_{0}^{\varepsilon,k}=\widehat{\lambda}_{0}^{\varepsilon,k} and ⟨ Φ 0 ε , k , Φ ^ 0 ε , k ⟩ ≠ 0 \langle\Phi_{0}^{\varepsilon,k},\widehat{\Phi}_{0}^{\varepsilon,k}\rangle\neq 0 for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} .

We now prove Claim 3.20 . Since Φ 0 ε , k = ϕ 0 ε , k + η ε \Phi_{0}^{\varepsilon,k}=\phi_{0}^{\varepsilon,k}+\eta^{\varepsilon} and Φ ^ 0 ε , k = a ^ ε ​ ϕ 0 ε , k + η ^ ε \widehat{\Phi}_{0}^{\varepsilon,k}=\widehat{a}^{\varepsilon}\phi_{0}^{\varepsilon,k}+\widehat{\eta}^{\varepsilon} , where 0 ≠ a ^ ε ∈ ℝ 0\neq\widehat{a}^{\varepsilon}\in\mathbb{R} , η ε , η ^ ε ∈ [ ϕ 0 ε , k ] ⟂ \eta^{\varepsilon},\widehat{\eta}^{\varepsilon}\in[\phi_{0}^{\varepsilon,k}]^{\perp} are real functions, it follows from ( 3.140 ) and ( 3.152 ) that

Therefore, by choosing ε ¯ \bar{\varepsilon} even smaller if necessary, we see that ⟨ Φ 0 ε , k , Φ ^ 0 ε , k ⟩ ≠ 0 \langle\Phi_{0}^{\varepsilon,k},\widehat{\Phi}_{0}^{\varepsilon,k}\rangle\neq 0 for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\bar{\varepsilon}] and D ≥ D 0 D\geq D_{0} . Now, multiplying the equation ℒ k ε ​ Φ 0 ε , k = λ 0 ε , k ​ Φ 0 ε , k \mathscr{L}_{k}^{\varepsilon}\Phi_{0}^{\varepsilon,k}=\lambda_{0}^{\varepsilon,k}\Phi_{0}^{\varepsilon,k} by Φ ^ 0 ε , k \widehat{\Phi}_{0}^{\varepsilon,k} and the equation ℒ ^ k ε ​ Φ ^ 0 ε , k = λ ^ 0 ε , k ​ Φ ^ 0 ε , k \widehat{\mathscr{L}}_{k}^{\varepsilon}\widehat{\Phi}_{0}^{\varepsilon,k}=\widehat{\lambda}_{0}^{\varepsilon,k}\widehat{\Phi}_{0}^{\varepsilon,k} by Φ 0 ε , k \Phi_{0}^{\varepsilon,k} , integrating over Ω \Omega and subtracting the resulting equation, we obtain that

It then follows from ⟨ Φ 0 ε , k , Φ ^ 0 ε , k ⟩ ≠ 0 \langle\Phi_{0}^{\varepsilon,k},\widehat{\Phi}_{0}^{\varepsilon,k}\rangle\neq 0 that λ ^ 0 ε , k = λ 0 ε , k \widehat{\lambda}_{0}^{\varepsilon,k}=\lambda_{0}^{\varepsilon,k} . This finishes the proof of Claim 3.20 .

Finally, normalize the eigenfunction Φ ^ 0 ε , k \widehat{\Phi}_{0}^{\varepsilon,k} of the adjoint operator ℒ ^ k ε \widehat{\mathscr{L}}_{k}^{\varepsilon} corresponding to λ ^ 0 ε , k \widehat{\lambda}_{0}^{\varepsilon,k} so that ⟨ Φ ^ 0 ε , k , Φ 0 ε , k ⟩ = 1 \langle\widehat{\Phi}_{0}^{\varepsilon,k},\Phi_{0}^{\varepsilon,k}\rangle=1 , we obtain from ( 3.153 ) that

This combined with ( 3.152 ) completes the proof of Theorem 3.1 (iv). ∎


## 3.5. Proof of Lemma 3.3

We prove ( 3.82 ) by contradiction. Assume that there exist two sequences ε j → 0 \varepsilon_{j}\to 0 , D j ≥ D 0 D_{j}\geq D_{0} and a sequence of functions { g j } ⊂ X ∞ \{g_{j}\}\subset X^{\infty} such that

Put

Then h j h_{j} satisfies

We will apply to ( 3.155 ) the same procedures as in the proof of Theorem 3.1 . Note that since λ 0 ε j , k ∈ ℝ \lambda_{0}^{\varepsilon_{j},k}\in\mathbb{R} , we can decompose h j h_{j} as

Then equation ( 3.155 ) can be reformulated as follows:

and

Denote

Then the equation in ( 3.157 ) can be rewritten as

By similar argument as in the proof of ( 3.136 ), we can show that there exists a constant C k = C k ​ ( M , D 0 ) > 0 C_{k}=C_{k}(M,D_{0})>0 such that for all j j large,

Integrating equation ( 3.158 ) over Ω \Omega , we see that

By similar arguments to the proof of ( 3.132 ), we see that

Therefore, we can solve b j b_{j} from ( 3.160 ) and for all j j sufficiently large and obtain that

Plugging ( 3.162 ) into ( 3.158 ), we obtain that

which combined with ( 3.159 ), ( 3.161 ) and ( 3.130 ) implies that there exists a constant C k = C k ​ ( M , D 0 ) > 0 C_{k}=C_{k}(M,D_{0})>0 such that for all j j sufficiently large,

On the other hand, since h j ∈ X ∞ h_{j}\in X^{\infty} , see ( 3.81 ), we have ⟨ h j , Φ ^ 0 ε j , k ⟩ = 0 \langle h_{j},\widehat{\Phi}_{0}^{\varepsilon_{j},k}\rangle=0 , where Φ ^ 0 ε j , k \widehat{\Phi}_{0}^{\varepsilon_{j},k} is the eigenfunction of the adjoint operator ℒ ^ k ε j \widehat{\mathscr{L}}_{k}^{\varepsilon_{j}} corresponding to λ 0 ε j , k \lambda_{0}^{\varepsilon_{j},k} . It follows from the proof of Theorem 3.1 (iv) that Φ ^ 0 ε j , k = a ^ ε j ​ ϕ 0 ε j , k + η ^ ε j \widehat{\Phi}_{0}^{\varepsilon_{j},k}=\widehat{a}^{\varepsilon_{j}}\phi_{0}^{\varepsilon_{j},k}+\widehat{\eta}^{\varepsilon_{j}} , where η ^ ε j ∈ [ ϕ 0 ε j , k ] ⟂ \widehat{\eta}^{\varepsilon_{j}}\in[\phi_{0}^{\varepsilon_{j},k}]^{\perp} and a ^ ε j ∈ ℝ \ { 0 } \widehat{a}^{\varepsilon_{j}}\in\mathbb{R}\backslash\{0\} satisfy ( 3.152 ) and ( 3.154 ) respectively. Consequently,

which combined with ( 3.152 ) and ( 3.154 ) implies that

Plugging this back into ( 3.163 ), we obtain that

Since lim j → ∞ ε j = 0 \lim_{j\to\infty}\varepsilon_{j}=0 and ‖ q j ‖ L ∞ ≤ j − 1 \|q_{j}\|_{L^{\infty}}\leq j^{-1} , this implies that

Therefore, we see from ( 3.88 ) that

which is a contradiction to ( 3.155 ). This completes the proof of Lemma 3.3 . ∎


## 4. Proof of the main result

In this section, we prove our main result Theorem 1.3 .

We fix an order of approximation k ≥ 2 k\geq 2 in Theorem 2.2 , and look for solutions of equation ( 1.9 ) in the following form:

In terms of p p , equation ( 1.9 ) is equivalent to

where ℛ ε ​ [ u k ε , D ] \mathcal{R}^{\varepsilon}[u^{\varepsilon,D}_{k}] is defined in Theorem 2.2 (ii) and

Note that f u ε , k f_{u}^{\varepsilon,k} and f v ε , k f_{v}^{\varepsilon,k} are defined in ( 3.73 ).

Denote 𝒬 ε \mathcal{Q}^{\varepsilon} the L 2 L^{2} -projection operator onto [ Φ 0 ε , k ] [\Phi_{0}^{\varepsilon,k}] along Φ ^ 0 ε , k \widehat{\Phi}_{0}^{\varepsilon,k} defined by

Rewrite p p in the form

where α = ⟨ Φ ^ 0 ε , k , p ⟩ / ε k + 1 2 ∈ ℝ \alpha=\langle\widehat{\Phi}_{0}^{\varepsilon,k},\,p\rangle/\varepsilon^{k+\frac{1}{2}}\in\mathbb{R} and q ∈ X ∞ q\in X^{\infty} . Note that X ∞ X^{\infty} is defined in ( 3.81 ). Then ( 4.164 ) is reformulated as

According to Lemma 3.3 , the inverse operator ( ℒ k ε − λ 0 ε , k ) − 1 (\mathscr{L}_{k}^{\varepsilon}-\lambda_{0}^{\varepsilon,k})^{-1} is a bounded operator from X ∞ X^{\infty} to itself. Moreover, by the comment just above Lemma 3.3 , we can actually work in the space

and consider the system:

where

Observe that if ( α , q ) ∈ ℝ × X 0 (\alpha,q)\in\mathbb{R}\times X_{0} sovles ( 4.167 ), then actually q q is a classical solution to the second equation in ( 4.166 ). In fact, by the definition of 𝒬 ε \mathcal{Q}^{\varepsilon} , we see that

Therefore, q ∈ X ν 2 , s ⊂ W ν 2 , s q\in X_{\nu}^{2,s}\subset W_{\nu}^{2,s} for any s ∈ ( 1 , ∞ ) s\in(1,\infty) by Lemma 3.2 . Choosing s > N s>N , we may infer that q ∈ C 1 + α ​ ( Ω ¯ ) q\in C^{1+\alpha}(\overline{\Omega}) for some α ∈ ( 0 , 1 ) \alpha\in(0,1) by the Sobolev embedding theorem. Then by the Schauder theory, w w turns out to be of class C 2 + α ​ ( Ω ¯ ) C^{2+\alpha}(\overline{\Omega}) and satisfies the desired zero-Newmann boundary condition.

We now solve ( 4.167 ) by applying Banach’s contraction mapping principle. To this end, we define a mapping 𝒯 : ℝ × X 0 → ℝ × X 0 \mathcal{T}:\mathbb{R}\times X_{0}\to\mathbb{R}\times X_{0} by 𝒯 = ( 𝒯 1 , 𝒯 2 ) \mathcal{T}=(\mathcal{T}_{1},\mathcal{T}_{2}) . We equip ℝ × X 0 \mathbb{R}\times X_{0} with the norm

under which it becomes a Banach space. We first establish the following preparatory lemma.

Assume that conditions (A1) - (A3) hold. Let M ∈ I v ∗ M\in I_{v^{*}} , D 0 > 0 D_{0}>0 , ε 0 > 0 \varepsilon_{0}>0 and integer k ≥ 2 k\geq 2 be given. Then, for each constant R > 0 R>0 , there exists a constant C ^ k = C ^ k ​ ( M , D 0 , ε 0 , R ) > 0 \widehat{C}_{k}=\widehat{C}_{k}(M,D_{0},\varepsilon_{0},R)>0 such that for any ( α , q ) , ( α i , q i ) ∈ ℝ × X 0 (\alpha,q),(\alpha_{i},q_{i})\in\mathbb{R}\times X_{0} satisfying

the following estimates hold for all ε ∈ ( 0 , ε 0 ] \varepsilon\in(0,\varepsilon_{0}] and D ≥ D 0 D\geq D_{0} :

We apply Taylor expansion with remainder to the function F ε ​ [ p ] F^{\varepsilon}[p] defined in ( 4.165 ), yielding that

where C > 0 C>0 is a constant depending only on the sup-norm of ∇ 2 f \nabla^{2}f on a compact region in ℝ 2 \mathbb{R}^{2} determined by ‖ u k ε , D ‖ L ∞ ​ ( Ω ) \|u_{k}^{\varepsilon,D}\|_{L^{\infty}(\Omega)} and ‖ p ‖ L ∞ ​ ( Ω ) \|p\|_{L^{\infty}(\Omega)} . Setting p = α ​ ε k + 1 2 ​ Φ 0 ε , k + ε k ​ q p=\alpha\varepsilon^{k+\frac{1}{2}}\Phi_{0}^{\varepsilon,k}+\varepsilon^{k}q in the above inequality, we obtain ( 4.168 ) from Theorem 2.2 and Theorem 3.1 (iii).

By similar calculation, we can show that

Setting p i = α i ​ ε k + 1 2 ​ Φ 0 ε , k + ε k ​ q i p_{i}=\alpha_{i}\varepsilon^{k+\frac{1}{2}}\Phi_{0}^{\varepsilon,k}+\varepsilon^{k}q_{i} for i = 1 , 2 i=1,2 in the above inequality, we obtain ( 4.169 ). ∎

By Theorem 2.2 (ii) and Theorem 3.1 (iii)-(iv), we have

which implies that

Therefore, using the above estimates, Theorem 3.1 , Lemmas 3.3 and 4.1 , we obtain that

Thus, if we define

and let R = 4 ​ C k R=4C_{k} in Lemma 4.1 , then 𝒯 ⁡ ( ℬ ) ⊂ ℬ \mathcal{T}(\mathcal{B})\subset\mathcal{B} provided that

Moreover, for any ( α 1 , q 1 ) (\alpha_{1},q_{1}) , ( α 2 , q 2 ) ∈ ℬ (\alpha_{2},q_{2})\in\mathcal{B} ,

Thus, with the above choice of ε ¯ \overline{\varepsilon} , we obtain that

Consequently, by the contraction mapping principle, the mapping 𝒯 \mathcal{T} admits a unique fixed point ( α ε , q ε ) (\alpha^{\varepsilon},q^{\varepsilon}) in the ball ℬ \mathcal{B} for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\overline{\varepsilon}] and D ≥ D 0 D\geq D_{0} . Since q ε q^{\varepsilon} actually belongs to class C 2 + α ​ ( Ω ¯ ) C^{2+\alpha}(\overline{\Omega}) and satisfies the zero-Newmann boundary condition, p = α ε ​ ε k + 1 2 ​ Φ 0 ε , k + ε k ​ q ε p=\alpha^{\varepsilon}\varepsilon^{k+\frac{1}{2}}\Phi_{0}^{\varepsilon,k}+\varepsilon^{k}q^{\varepsilon} is a classical solution to ( 4.164 ). Therefore,

yields a family of classical solutions to the scalar nonlocal problem ( 1.9 ) for all ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\overline{\varepsilon}] and D ≥ D 0 D\geq D_{0} . This finishes the proof of existence of u ε , D u^{\varepsilon,D} in Theorem 1.3 .

Now, Part (i) of Theorem 1.3 follows directly from Theorem 2.2 (i) and the above construction. ∎

Note that in order to prove Theorem 1.3 , it suffices to apply Theorem 2.2 with k = 2 k=2 . Nevertheless, one advantage of establishing Theorem 2.2 for general integers k ≥ 2 k\geq 2 is that, in combination with the estimate ‖ Φ 0 ε , k ‖ L ∞ ​ ( Ω ) = O ⁡ ( ε − 1 2 ) \|\Phi_{0}^{\varepsilon,k}\|_{L^{\infty}(\Omega)}=O(\varepsilon^{-\frac{1}{2}}) from Theorem 3.1 (iii), the proof of Theorem 1.3 yields the following higher-order approximation estimates for the solutions.

Assume that conditions (A1)-(A3) hold. Then, for each given M ∈ I v ∗ M\in I_{v^{*}} , D 0 > 0 D_{0}>0 and integer k ≥ 2 k\geq 2 , there exists a constant ε ¯ = ε ¯ ​ ( M , D 0 , k ) > 0 \overline{\varepsilon}=\overline{\varepsilon}(M,D_{0},k)>0 such that the solution ( u ε , D , v ε , D ) (u^{\varepsilon,D},v^{\varepsilon,D}) to system ( 1.3 ) obtained in Theorem 1.1 is approximated by the pair of functions ( u k ε , D , v k ε , D ) (u_{k}^{\varepsilon,D},v_{k}^{\varepsilon,D}) given in Theorem 2.2 with accuracy

for all ε ∈ ( 0 , ε 0 ] \varepsilon\in(0,\varepsilon_{0}] and D ≥ D 0 D\geq D_{0} , where C k = C k ​ ( M , D 0 , ε ¯ ) > 0 C_{k}=C_{k}(M,D_{0},\overline{\varepsilon})>0 is a constant depending only on the variables indicated.

On the other hand, in ( 2.20 ), if we choose U ± , 0 ​ ( x ) ≡ h ± ​ ( A 0 ) U^{\pm,0}(x)\equiv h^{\pm}(A_{0}) in Ω ± \Omega^{\pm} instead, then the resulting approximate solution leads to a different but structurally symmetric family of functions to the one obtained in Theorem 2.2 . This yields the following alternative existence result of Theorem 1.1 , where we still denote the family of subsequent radial solutions by ( u ε , D , v ε , D ) (u^{\varepsilon,D},v^{\varepsilon,D}) .

Assume that conditions (A1)-(A3) hold. Then, for each given

there exists a constant ε ¯ = ε ¯ ​ ( M , D 0 ) > 0 \overline{\varepsilon}=\overline{\varepsilon}(M,D_{0})>0 such that system ( 1.4 ) has a family of spherically symmetric classical solutions ( u ε , D ​ ( r ) , v ε , D ​ ( r ) ) (u^{\varepsilon,D}(r),v^{\varepsilon,D}(r)) defined for ε ∈ ( 0 , ε ¯ ] \varepsilon\in(0,\overline{\varepsilon}] and D ≥ D 0 D\geq D_{0} and satisfying

Moreover, these solutions satisfy the following properties:

There exists a constant C = C ⁡ ( M , D 0 , ε ¯ ) > 0 C=C(M,D_{0},\overline{\varepsilon})>0 such that

For each η > 0 \eta>0 , there exist two constants K = K ⁡ ( η ) > 0 K=K(\eta)>0 and ε ¯ ′ = ε ¯ ′ ​ ( M , D 0 , η ) ≤ ε ¯ \overline{\varepsilon}^{\prime}=\overline{\varepsilon}^{\prime}(M,D_{0},\eta)\leq\overline{\varepsilon} such that for any ε ∈ ( 0 , ε ¯ ′ ] \varepsilon\in(0,\overline{\varepsilon}^{\prime}] , D ≥ D 0 D\geq D_{0} , there hold

where

v ε , D ​ ( x ) = 𝒮 ε ​ [ u ε , D ] − ε D ​ u ε , D ​ ( x ) v^{\varepsilon,D}(x)=\mathcal{S}^{\varepsilon}[u^{\varepsilon,D}]-\frac{\varepsilon}{D}u^{\varepsilon,D}(x) and

We conclude this section with the following remark.

For any fixed integer k ≥ 2 k\geq 2 , it follows directly from the proof of Theorem 1.3 that the family of solutions ( u ε , D , v ε , D ) (u^{\varepsilon,D},v^{\varepsilon,D}) obtained in Theorem 1.1 depends smooth on the parameters ( M , D , ε ) ∈ I v ∗ × [ D 0 , ∞ ) × ( 0 , ε ¯ ] (M,D,\varepsilon)\in I_{v^{*}}\times[D_{0},\infty)\times(0,\overline{\varepsilon}] .

An interesting question is to determine whether the family of solutions ( u ε , D , v ε , D ) (u^{\varepsilon,D},v^{\varepsilon,D}) obtained in Theorem 1.1 is independent of the choice of k k . We can even ask more: For ε > 0 \varepsilon>0 small, is there local uniqueness of solutions to ( 1.6 ) near the limiting transition layer ( u ∗ , v ∗ ) (u^{*},v^{*}) in suitable topology? Here, v ∗ v^{*} is defined as in condition (A3) and

Recently, the local uniqueness of spike/bubble solutions has been widely investigated for singularly perturbed nonlinear elliptic problems; see [ 6 ] and references therein.


## Acknowledgments

The research of He is supported in part by NSFC grant No. 12071141. The research of Liu and He is supported in part by the Shanghai Science and Technology Innovation Action Plan in Basic Research Area (23JC1402600). He and Ye are partially supported by Science and Technology Commission of Shanghai Municipality (No. 22DZ2229014).


## References