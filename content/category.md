---
title: 圏論的準備
weight: 3
section: 2
toc: true
---

## 圏論の概要
[元になったOlivia先生の講義スライド](https://www.oliviacaramello.com/Teaching/Lectures2_3_4.pdf)

**圏論(category theory)** は、1942-45年にSamuel EilenbergとSaunders Mac Laneによって代数的位相幾何学の文脈で発明された数学の一分野であり、数学的概念を表現し議論するための抽象的な言語を提供する。
実際、圏論の諸概念は、それらの例を数学のあらゆる分野で見つけることができる統一的な概念である。
圏論に通底する哲学は、集合論を構成する、集合とその所属関係という原始的な概念を、集合と関数の概念を抽象化した、対象と射という概念で置き換えることである。

発明されて以来、このアプローチは数学者が自分の主題を捉える方法に深いパラダイムシフトをもたらし、以前ではほとんど不可能だった重要な発見への道を開いた。
圏論の大きな成果の一つがトポス理論であり、これは全面的に圏論の言語で書かれた理論である。

## 圏論の諸概念
### 圏

{{% definition title="圏" label="def.category" %}}
(小さな) **圏(category)** $\mathcal{C}$ は

- **対象(object)** の 集合 $\mathrm{Ob}(\mathcal{C})$
- 各 $a, b\in\mathrm{Ob}(\mathcal{C})$ に対する **射(arrow)** の集合 $\mathcal{C}(a,b)$
- 各 $a,b,c\in\mathrm{Ob}(\mathcal{C})$ に対する射の **合成(composition)**
$$ \mathcal{C}(a,b)\times\mathcal{C}(b,c)\ni(f,g)\mapsto g\circ f\in\mathcal{C}(a,c)$$

からなり、以下の2条件を満たすものである。

1. 任意の $f\in\mathcal{C}(a,b), g\in\mathcal{C}(b,c),h\in\mathcal{C}(c,d)$ に対して
    $$ h\circ(g\circ f) = (h\circ g)\circ f $$
    (よって 括弧を外して $h\circ g\circ f$ と書いても問題ない)
2. 任意の $a\in\mathrm{Ob}(\mathcal{C})$ について **恒等射(identity arrow)** $1_a\in\mathcal{C}(a,a)$ が存在し、任意の $f\in\mathcal{C}(a,b)$ について
    $$ f\circ 1_a = 1_b\circ f = f$$

$f \in\mathcal{C}(a,b)$ の代わりに、$f \in\mathrm{Hom}\_{\mathcal{C}}(a,b)$ や $f:a\rightarrow b$ とも書く。$a$ を $f$ の **ドメイン(domain)** と呼び $\mathrm{dom}(f)=a$ と書く。同様に、 $b$ を **コドメイン(codomain)** と呼び $\mathrm{cod}(f)=b$ と書く。

{{% /definition %}}

対象や射の集まりとして集合より大きな **類(class)** を用いる事でより大きな圏を考える事もできる。また、圏の定義は一階述語理論的な公理化も可能である。

{{% definition title="圏の一階述語論理的公理化" %}}

圏とは以下の6つの述語・関数と等号をもち

- 一引数の述語 $\mathrm{Obj},\mathrm{Arr}$
- 一引数の関数 $\mathrm{Dom},\mathrm{Cod},\mathrm{Id}$
- 二引数の関数 $\circ$

以下の公理を満たすものである。

$$
\begin{align*}
& \forall f,\ \mathrm{Arr}(f) \Rightarrow \mathrm{Obj}(\mathrm{Dom}(f))\wedge\mathrm{Obj}(\mathrm{Cod}(f)) \\\\
& \forall f,g,\ (\mathrm{Arr}(f)\wedge\mathrm{Arr}(g)\wedge\mathrm{Cod}(f)=\mathrm{Dom}(g)) \\\\
& \Rightarrow\mathrm{Arr}(g\circ f)\wedge\mathrm{Dom}(g\circ f)=\mathrm{Dom}(f)\wedge\mathrm{Cod}(g\circ f)=\mathrm{Cod}(g) \\\\
& \forall a,\ \mathrm{Obj}(a)\Rightarrow\mathrm{Arr}(\mathrm{Id}(a))\wedge\mathrm{Dom}(\mathrm{Id}(a))=\mathrm{Cod}(\mathrm{Id}(a))=a \\\\
& \forall f,g,h,\ (\mathrm{Arr}(f)\wedge\mathrm{Arr}(g)\wedge\mathrm{Arr}(h)\wedge\mathrm{Cod}(f)=\mathrm{Dom}(g)\wedge\mathrm{Cod}(g)=\mathrm{Dom}(h) \\\\
& \Rightarrow h\circ(g\circ f)=(h\circ g)\circ f \\\\
& \forall f,a\ \mathrm{Arr}(f)\wedge\mathrm{Obj}(a) \\\\
& \Rightarrow(\mathrm{Dom}(f)=a\Rightarrow f\circ\mathrm{Id}(a)=f)\wedge(\mathrm{Cod}(f)=a\Rightarrow \mathrm{Id}(a)\circ f=f)
\end{align*}
$$
<font color="blue">(Olivia先生のスライドでは二引数関数 $\circ$ の代わりに合成に関する三引数の *述語* を用いると書いてある。$f,g$ を合成して $h=g\circ f$ となることを $\mathrm{Comp}(f, g, h)$ といった述語で表す公理系を指しているのだろう。) </font>

{{% /definition %}}

{{< refn def.category >}}を満たす圏 $\mathcal{C}$ は

- $\mathrm{Obj}(a)$ を $a\in\mathrm{Ob}(\mathcal{C})$
- $\mathrm{Arr}(f)$ を $\displaystyle f\in\coprod_{a,b\in\mathrm{Ob}(\mathcal{C})}\mathcal{C}(a,b)$
- $\mathrm{Dom}(f)$ を $\mathrm{dom}(f)$、$\mathrm{Cod}(f)$ を $\mathrm{cod}(f)$、$\mathrm{Id}(a)$ を $1_a$、$\circ$ を $\circ$

と解釈することでこの公理系を満たす。

圏論では等式の代わりに **可換図式(commutative diagram)** を用いる事が多い。
図式が可換であるとは、図式内の射の列の合成射は始点と終点が一致するならば経路の捕り方によらず一致するということ。
例えば $g\circ f=h$ であるということを「以下の図式が可換である」などと表現する。

$$
\xymatrix {
a \ar[d]_f \ar[rd]^h &      \\\\
b \ar[r]_g & c
}
$$

{{% proposition %}}
任意の対象 $a$ に対して、恒等射 $1_a$ は一意に定まる。
{{% /proposition %}}
{{% details 証明 %}}
$1_a,1'_a: a\rightarrow a$ が共に恒等射であるとすると、以下の図式が可換となるから $1_a=1'_a$
$$
\xymatrix {
a \ar[r]^{1_a} \ar@/^2pc/[rr]^{1_a} \ar@/_2pc/[rr]\_{1'\_a} & a \ar[r]^{1'_a} & a 
}
$$
(証明終)
{{% /details %}}

このような図式を辿る事による証明方法をdiagram chasingという。

### 双対原理

{{% definition title="双対圏" %}}
圏 $\mathcal{C}$ の **双対圏(dual category)** $\mathcal{C}^{\mathrm{op}}$とは
$$ \mathrm{Ob}(\mathcal{C}^{\mathrm{op}}) = \mathrm{Ob}(\mathcal{C}),\ \mathcal{C}^{\mathrm{op}}(a,b)=\mathcal{C}(b,a) $$

であり $f\in\mathcal{C}^{\mathrm{op}}(a,b), g\in\mathcal{C}^{\mathrm{op}}(b,c)$ に対してその合成を
$$ g\circ_{\mathcal{C}^\mathrm{op}}f = f\circ_{\mathcal{C}} g $$
と定めたもの。${\mathcal{C}^{\mathrm{op}}}^{\mathrm{op}}$ は $\mathcal{C}$ と一致する。
{{% /definition %}}

つまり、双対圏は元の圏の射の向きを全て逆にしたもの。

{{% theorem title="双対原理" %}}
ある命題が圏 $\mathcal{C}$ で真であるとき、射の向きを全て逆にし合成の順序を入れ替えて得られる **双対命題(dual statement)** は圏 $\mathcal{C}^{\mathrm{op}}$ でも真である。
{{% /theorem %}}

$\mathcal{C}^{\mathrm{op}}$ の双対は $\mathcal{C}$ だから結局

$$ \text{命題 $P$ が圏 $\mathcal{C}$ で真} \Leftrightarrow \text{$P$ の双対命題が $\mathcal{C}^{\mathrm{op}}$ で真} $$

である。単純な原理であるが、圏論の言語での2つの双対命題は、それを「具体的な」圏で解釈したときには、非常に異なる(しかも同値ではない!)命題となる事がある。
時折、通常の数学的命題の圏論の言語を用いた抽象的な証明を得ることが可能である。そのような場合は、双対原理を用いることで、元の文脈における双対バージョンの命題を得ることができる。

### 圏の例

数学対象と対象とし、その間の写像を射とする圏は様々な存在する。例えば

- $\mathbf{Set}$: **集合**と**写像**
- $\mathbf{Top}$: **位相空間**と**連続写像**
- $\mathbf{Gr}$: **群** と **群の準同型写像**
- $\mathbf{Rng}$: **環** と **環の準同型写像**
- $\mathbf{Vect}\_{K}$: 体 $K$ 上の **ベクトル空間** と **線型写像**

などである。実際、任意の一階の理論(一階述語理論で記述された理論) $\mathbb{T}$ に対して、(集合論ベースの)モデルを対象とし、その間の準同型写像を射とする圏 $\mathbb{T}\mathrm{-mod}(\mathbf{Set})$ を考える事ができる。

また、数学的対象1つを圏と見なす事もできる。例えば

- 集合: 要素を対象とし、射は恒等射のみとしたもの。**離散圏(discrete category)** という。
- 前順序集合: 要素を対象とし、$a \leq b$ を射 $a\rightarrow b$ とみなしたもの。任意の対象 $a,b$ について射 $a\rightarrow b$ が高々一つしかない圏。
- モノイド: 対象が1つの圏。モノイドの元を射としたもの。
- 亜群(groupoid): 全ての射が同型射である圏。
- 群: 全ての射が同型射で対象が一つの圏。

### 同型・モノ射・エピ射

{{% definition title="同型" %}}
$f: a\rightarrow b,\ g: b\rightarrow a$ が
$$ g\circ f=1_a,\ f\circ g=b $$
を満たす時、 $f,g$ を **同型射(isomorphism)** という。 $g$ を $f$ の **逆射(inverse morphism)** と呼び $f^{-1}$ と書く。

$$
\xymatrix {
a \ar@(ul,dl)[]_{1_a} \ar@/^/[rr]|{f} && b \ar@/^/[ll]|{g} \ar@(ur,dr)[]^{1_b}
}
$$

対象 $a,b$ の間に同型射が存在する時これらは **同型(isomorphic)** であるといい、
$$ a\simeq b $$
と書く。
{{% /definition %}}
{{% proposition %}}
$f: a\rightarrow b$ が同型射の時、その逆射は一意に定まる。
{{% /proposition %}}
{{% details 証明 %}}
$f: a\rightarrow b$ が同型射であるとし $g,h:b\rightarrow a$ は共に逆射 であるとすると $ g = g\circ 1_b = g\circ f\circ h = 1_a\circ h = h $ (証明終)
{{% /details %}}

{{% definition title="モノ射" %}}
射 $m: a\rightarrow b$ が **モノ射(monomorphism)** もしくは **モニック射(monic)** であるとは、任意の対象 $c$ と射 $f,g: c\rightarrow a$ について
$$ m\circ f = m\circ g \quad\Rightarrow\quad f=g $$
が成り立つことである。この性質を$m$は **左簡約可能(left cancelable)** であるという。

$$
\xymatrix {
c \ar@<2pt>[r]^{f} \ar@<-2pt>[r]\_{g} & a \ar[r]^{m} & b
}
$$

ある射がモノ射である事を $a\xhookrightarrow{} b$ という矢印で書くこともある。
{{% /definition %}}

モノ射の双対をエピ射という。

{{% definition title="エピ射" %}}
射 $e: a\rightarrow b$ が **エピ射(epi-morphism)** もしくは **エピック射(epic)** であるとは、任意の対象 $c$ と射 $f,g: b\rightarrow c$ について
$$ f\circ e = g\circ e \quad\Rightarrow\quad f=g $$
が成り立つことである。この性質を$e$は **右簡約可能(right cancelable)** であるという。

$$
\xymatrix {
a \ar[r]^{e} & b \ar@<2pt>[r]^{f} \ar@<-2pt>[r]\_{g} & c
}
$$

ある射がエピ射である事を $a\twoheadrightarrow b$ という矢印で書くこともある。
{{% /definition %}}

以下のように、モノ射・エピ射は単射・全射の概念を抽象化したものと考える事が出来る。ただ一般の圏においては、単射・全射そのものではない。

{{% proposition %}}
$\mathbf{Set}$ おいてモノ射と単射は一致する。
{{% /proposition %}}
{{% details 証明 %}}
$m: A\rightarrow B$ をモノ射とする。対象$x,y\in A$ について $m(x) = m(y)$  であるとすると、$x,y$ を一点集合からの写像 $1\rightarrow A$ と見なせば $m\circ x=m\circ y$ であるので $m$ がモノ射であることより $x=y$。従って $m$ は単射である。

逆に $m: A\rightarrow B$ が単射であるとする。集合 $C$ と写像 $f,g: C\rightarrow A$ が $m\circ f=m\circ g$ をみたするとする。任意の $x\in C$ について $m(f(x))=m(g(x))$ であるから $m$ が単射であることより $f(x)=g(x)$。従って $f=g$ であるから $m$ はモノ射である。(証明終)
{{% /details %}}

{{% proposition %}}
$\mathbf{Set}$ おいてエピ射と全射は一致する。
{{% /proposition %}}
{{% details 証明 %}}
$e: A\rightarrow B$ をエピ射とする。$e$ が全射でないととし、写像 $f,g:B\rightarrow\\{0,1\\}$ を以下のように定義する。

$$ f(x) = 0,\ g(x)=\begin{cases}
0   & (x\in e(A)) \\\\
1   & (x\not\in e(A))
\end{cases}
$$

すると、$f\circ e = g\circ e$ である。しかし $e$ が全射でないことより$x\not\in e(A)$ すなわち $f(x)\neq g(x)$ となる$x\in B$が少なくも一つ存在するから $f\neq g$ である。これは矛盾であるので $e$ は全射である。

逆に $e:A\rightarrow B$ を全射とし、集合 $C$ と写像 $f,g:B\rightarrow C$ が $f\circ e = g\circ e$ をみたするとする。任意の $x\in B$ についてある $y\in A$ が存在して $x=e(y)$ と書けるので $f(x)=g(x)$ である。よって $f=g$ であるから $e$ はエピ射。(証明終)
{{% /details %}}

モノ射とエピ射は圏論の世界では対称的な定義だが、具体的な集合と関数では一見そのように見えないというところが面白い。また、これらの命題から直ちに以下が言える。

{{% proposition %}}
$\mathbf{Set}$ おいて同型射と全単射は一致する。
{{% /proposition %}}

より一般に、以下が言える。逆射を両辺に合成することで、左簡約も右簡約も可能であるからである。

{{% proposition %}}
同型射はモノかつエピである。
{{% /proposition %}}

ただし、この逆は成立しない。例えば、順序集合を$\leq$を射とする圏とみなしたとき、全ての射はモノかつエピだが同型射とは限らない。

### 関手・自然変換

圏から圏への準同型写像(構造を保つ写像)を関手という。

{{% definition title="関手" %}}
圏 $\mathcal{C}$ から圏 $\mathcal{D}$ への **関手(functor)** $F$ とは
写像 $F:\mathrm{Ob}(\mathcal{C})\rightarrow\mathrm{Ob}(\mathcal{D})$ と任意の対象 $a,b\in\mathcal{C}$ に対する写像 $F:\mathcal{C}(a,b)\rightarrow \mathcal{D}(F(a), F(b))$ であり

- 任意の対象 $a\in\mathcal{C}$ について $F(1\_a)=1\_{F(a)}$
- 任意の$f:a\rightarrow b, g:b\rightarrow c$ について $F(g\circ f)=F(g)\circ F(f)$

を満たすものである。
{{% /definition %}}

恒等写像であるような関手 $F$ を **恒等関手(identity functor)** といい $\mathrm{id}_\mathcal{C}:\mathcal{C}\rightarrow\mathcal{C}$ と書く。
また、関手 $F:\mathcal{C}\rightarrow\mathcal{D}, G:\mathcal{D}\rightarrow\mathcal{E}$ に対して対象・射共に通常の関数合成を行うと$\mathcal{C}$ から $\mathcal{E}$ への関手が得られる。これを関手の合成といい $G\circ F:\mathcal{C}\rightarrow\mathcal{E}$ と書く。 $\circ$ を省略して $GF$ と書くこともある。

{{% definition title="反変関手" %}}
$\mathcal{C}^{\mathrm{op}}$ から $\mathcal{D}$ への関手 $F:\mathcal{C}^{\mathrm{op}}\rightarrow\mathcal{D}$ を、$\mathcal{C}$ から $\mathcal{D}$ への **反変関手(contravariant functor)** という。
{{% /definition %}}

{{% definition title="小さい圏の圏" %}}
小さい圏を対象、関手を射とした圏は(大きな)圏となる。これを $\mathbf{Cat}$ と書く。
{{% /definition %}}

{{% definition title="前層" %}}
圏 $\mathcal{C}$ から $\mathbf{Set}$ への反変関手
$$ F:\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$$
を $\mathcal{C}$ 上の **前層(presheaf)** という。
{{% /definition %}}

{{% definition title="自然変換" %}}
関手 $F,G:\mathcal{C}\rightarrow\mathcal{D}$ に対して、$F$ から $G$ への**自然変換(natural transformation)** $\phi:F\rightarrow G$ とは、$\mathcal{C}$ の各対象 $a$ に、$\mathcal{D}$の射 $\phi_a: F(a)\rightarrow G(a)$ を対応させる関数であり、任意の $\mathcal{C}$ の射 $f:a\rightarrow b$ に対して、以下の図式が可換となるものである。

$$\xymatrix{
F(a) \ar[r]^{\phi_a} \ar[d]\_{F(f)} & G(a) \ar[d]^{G(f)} \\\\
F(b) \ar[r]^{\phi_b} & G(b)
}$$

$\phi_a$ が全て同型射であるとき $\phi$ を **自然同型(natural isomorphism)** もしくは **自然同値(natural equivalence)** という。また自然同型 $\phi:F\rightarrow G$ が存在する時 $F\simeq G$ と書く。
{{% /definition %}}

{{% example %}}
ベクトル空間をその双対ベクトル空間に写す反変関手
$$ \*:\mathbf{Vect}\_K^{\mathrm{op}}\ni V\longmapsto V^\*=\mathbf{Vect}_K(V,K)\in\mathbf{Vect}\_K $$

について $\mathrm{id}\_{\mathbf{Vect}\_K}\rightarrow **$ は自然変換である。
{{% /example %}}
これは自然同型ではないので注意。一般に無限次元のベクトル空間 $V$ については $V\not\simeq V^{**}$

{{% definition title="定数関手" %}}
関手 $\mathcal{C}\rightarrow\mathcal{D}$ であって、$\mathcal{C}$ の全ての対象をある対象 $a\in\mathcal{D}$ に、射を $1_a$ に移すものを **定数関手(constant functor)** という。対象 $a$ についての定数関手を同じ記号を用いて $a:\mathcal{C}\rightarrow\mathcal{D}$ と書くこともある。

任意の射 $f:a\rightarrow b$ は定数関手 $a, b:\mathcal{C}\rightarrow\mathcal{D}$ の間の自然変換である。
{{% /definition %}}

{{% definition title="共変Hom関手" %}}
圏 $\mathcal{C}$ と対象 $a\in\mathcal{C}$ に対して以下で定義される
$\mathcal{C}(a,-):\mathcal{C}\rightarrow\mathbf{Set}$ は関手となる。
- $\mathcal{C}(a,-)(b) = \mathcal{C}(a,b)$
- $f:b\rightarrow c$ に対して
$$\mathcal{C}(f): \mathcal{C}(a,b) \ni g \mapsto f\circ g \in\mathcal{C}(a,c)$$

$\mathcal{C}(a,-)$ の代わりに $\mathrm{Hom}_{\mathcal{C}}(a,-)$ とも書く。これを **共変Hom関手(covariant hom functor)** という。

$$
\xymatrix{
            & a \ar[ld]_{\mathcal{C}(a,b)\ni g} \ar[rd]^{f\circ g\in\mathcal{C}(a,c)} &    \\\\
b \ar[rr]^f &             & c
}
$$
{{% /definition %}}

{{% details 関手であることの証明 %}}
任意の $a,b\in\mathcal{C}$, $f:a\rightarrow b$ について
$$ \mathcal{C}(a,-)(1_b): f\longmapsto 1_b\circ f = f$$
であるから $ \mathcal{C}(a,-)(1_b) = 1_{\mathcal{C}(a,b)} $
また、任意の $f: b\rightarrow c, g:c\rightarrow d$ と $p:a\rightarrow b$ について
$$ (\mathcal{C}(a,-)(g)\circ\mathcal{C}(a,-)(f))(p) = g\circ(f\circ p) = (g\circ f)\circ p = \mathcal{C}(a,-)(g\circ f)(p) $$
(証明終)
{{% /details %}}

{{% definition title="反変Hom関手" %}}
圏 $\mathcal{C}$ と対象 $a\in\mathcal{C}$ に対して以下で定義される
$\mathcal{C}(-,a):\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ は関手となる。
- $\mathcal{C}(-,a)(b) = \mathcal{C}(b,a)$
- $f:b\rightarrow c$ に対して
$$\mathcal{C}(f): \mathcal{C}(c,a) \ni g \mapsto g\circ f \in\mathcal{C}(b,a)$$

$\mathcal{C}(-,a)$ の代わりに $\mathrm{Hom}_{\mathcal{C}}(-,a)$ とも書く。これを **反変Hom関手(contravariant hom functor)** という。

$$
\xymatrix{
            & a \ar@{<-}[ld]_{\mathcal{C}(b,a)\ni g\circ f} \ar@{<-}[rd]^{g\in\mathcal{C}(c,a)} &    \\\\
b \ar[rr]^f &             & c
}
$$
{{% /definition %}}

証明は共変Hom関手と同様なので省略。

{{% definition title="表現可能関手" %}}
ある $a\in\mathcal{C}$ に対して $\mathcal{C}(a, -): \mathcal{C}\rightarrow\mathbf{Set}$ と自然同型である関手を **表現可能関手(representable functor)** という。

同様に $\mathcal{C}(-,a)$ と自然同型である関手を余表現可能関手(co-representable functor)という。
{{% /definition %}}

表現可能という言葉の意味については、後述する米田の補題の所で説明する。

{{% definition title="充満・忠実・本質的全射" %}}
関手 $F:\mathcal{C}\rightarrow\mathcal{D}$ について

- $F: \mathcal{C}(a,b)\rightarrow\mathcal{D}(F(a),F(b))$ が全ての$a,b\in\mathcal{C}$ について全射の時 $F$ は **充満(full)** であるという。
- $F: \mathcal{C}(a,b)\rightarrow\mathcal{D}(F(a),F(b))$ が全ての$a,b\in\mathcal{C}$ について単射の時 $F$ は **忠実(faithful)** であるという。
- 任意の$b\in\mathcal{D}$ についてある $a\in\mathcal{C}$ が存在して $F(a)\simeq b$ となるとき $F$ は **本質的全射(essentially surjective)**  であるという。
{{% /definition %}}

本質的全射が全射と異なるのは $F(a)\simeq b$ と $F(a)=b$ の違い。
圏論では、同型な対象はその圏論的な性質によっては区別する事ができず、実質的に1つの対象と見なすことが自然である。よって、対象の厳密な一致ではなく同型 $\simeq$ を用いて定められた性質の方がより本質的な性質となる。

### 圏同値

圏 $\mathcal{C}$ と $\mathcal{D}$ が本質的に同じとはどういう事かを考える。素朴には、まず圏の同型という関係性がある。

{{% definition title="圏の同型" %}}
圏 $\mathcal{C},\mathcal{D}$ が **同型(isomorphic)** であるとは関手 $F:\mathcal{C}\rightarrow\mathcal{D}$ と $G:\mathcal{D}\rightarrow\mathcal{C}$ で
$$ G\circ F = \mathrm{id}\_{\mathcal{C}},\ F\circ G=\mathrm{id}\_{\mathcal{D}}$$
を満たすものが存在する事である。
{{% /definition %}}

これは、本質的全射の所で述べたのと同じ理由で条件が強すぎて、同型な対象 $a\simeq b$ は同じものと見なした上で圏が本質的に一致する条件を考えたい。
そこで、圏同値という概念が重要となる。

{{% definition title="圏の同値" %}}
圏 $\mathcal{C},\mathcal{D}$ が **同値(equivalent)** であるとは関手 $F:\mathcal{C}\rightarrow\mathcal{D}$ と $G:\mathcal{D}\rightarrow\mathcal{C}$ で自然同型
$$ G\circ F \simeq \mathrm{id}\_{\mathcal{C}},\ F\circ G \simeq\mathrm{id}\_{\mathcal{D}}$$
を満たすものが存在する事である。$F,G$ を **圏同値(equivalence of categories)** という。
{{% /definition %}}

{{% proposition %}}
選択公理を仮定すると、
$$ \text{関手 $F$ が圏同値} \Leftrightarrow \text{関手 $F$ が充満忠実かつ本質的に全射} $$
{{% /proposition %}}

{{% details 証明 %}}
($\Rightarrow$)
$F:\mathcal{C}\rightarrow\mathcal{D}$ が圏同値、すなわち関手 $G:\mathcal{D}\rightarrow\mathcal{C}$ が存在して自然同型 $\phi: G\circ F\rightarrow\mathrm{id}\_{\mathcal{C}}, \psi: F\circ G\rightarrow\mathrm{id}\_{\mathcal{D}}$ が存在するとする。

任意の$b\in\mathcal{D}$ に対して $a=G(b)$ とおけば $F(a)=FG(b)\simeq\mathrm{id}\_{\mathcal{D}}(b) = b$。従って $F$ は本質的全射。

任意の$f,g\in\mathcal{C}(a,b)$ について $F(f)=F(g)$ であるとすると $GF(f)=GF(g)$ であるから、$\phi_b\circ GF(f)\circ\phi_a^{-1} = f$ であることより $f = g$。従って$F:\mathcal{C}(a,b)\rightarrow\mathcal{D}(F(a),F(b))$ は単射であるから $F$ は忠実。

$$\xymatrix{
GF(a) \ar[d]\_{GF(f)} \ar@{<-}[r]^{\phi^{-1}_a} & a \ar[d]^{f} \\\\
GF(b) \ar[r]\_{\phi_b} & b \\\\
}$$

また、任意の $g:F(a)\rightarrow F(b)$ についてこれを $G$ で移した $G(g):GF(a)\rightarrow GF(b)$ を $GF\simeq\mathrm{id}\_{\mathcal{C}}$ によって射 $a\rightarrow b$ と見なしたものを $f$ とする。すなわち$ f = \phi\_{b}\circ G(g)\circ \phi^{-1}\_{a} $とおく。これを変形して $G(g) = \phi_b^{-1}\circ f\circ\phi_a = GF(f)$ となるが、 $G$ は単射なので $g=F(f)$ となる。よって $F:\mathcal{C}(a,b)\rightarrow\mathcal{D}(F(a),F(b))$ は全射であるから $F$ は充満である。(証明終)

($\Leftarrow$)
$F:\mathcal{C}\rightarrow\mathcal{D}$ が充満忠実かつ本質的全射であるとする。

本質的全射であることより、任意の $b\in\mathcal{D}$ に対してある $a\in\mathcal{C}$ が存在して $F(a)\simeq b$ となる。選択公理を用いてそのような $a$ を各 $b$ について選ぶ事によって、対象間の写像 $G:\mathrm{Ob}(\mathcal{D})\rightarrow\mathrm{Ob}(\mathcal{C})$ を作る事が出来る。すなわち、任意の $b\in\mathcal{D}$ について $FG(b)\simeq b$ である。

これと、$F$ が充満忠実であることとより、任意の$x,y\in\mathcal{D}$ について全単射

$$\mathcal{C}(G(x), G(y)) \simeq \mathcal{D}(FG(x), FG(y)) \simeq \mathcal{D}(x, y)$$

が存在する。 この対応を射の対応 $G:\mathcal{D}(x,y)\rightarrow\mathcal{C}(G(x), G(y))$ とすると $G$ は関手となる。なぜならば、以下の図式の一番右に $1_x:x\rightarrow x$ を入れると、真ん中は $1_{FG(x)}=F(1_{G(x)})$ となる($\because$ $F$ は関手) ので対応する左の射は $1_{G(x)}$。すなわち $G(1_x)=1_{G(x)}$。

同様に、この図式を2つ重ねる事により右側の $g\circ f$ に対応する真ん中の射は $FG(g)\circ FG(f)=F(G(g)\circ G(f))$ となるので、 対応する左の射は $G(g)\circ G(f)$。すなわち $G(g\circ f)=G(g)\circ G(f)$ となるから。
$$
\xymatrix{
G(x) \ar[d]^{G(f)}=\"a\" & & FG(x) \ar[d]\_{FG(f)}=\"b\" \ar[r]^{\phi_x} & x \ar[d]_{f} \\\\
G(y)               & & FG(y) \ar[r]\_{\phi_y}                & y
\ar@{~>}^F \"a\";\"b\"
}
$$

$FG\simeq\mathrm{id}\_{\mathcal{D}}$ はこれまでの議論より明らか。これより右から$F$を合成して$FGF\simeq F$ も得られるが $F$ が充満忠実であることから $GF\simeq\mathrm{id}\_{\mathcal{C}}$ となる。(証明終)
{{% /details %}}

## 代表的な圏の構成

### 関手圏

{{% definition title="関手圏" %}}
圏 $\mathcal{C},\mathcal{D}$ について、関手 $\mathcal{C}\rightarrow \mathcal{D}$ を対象とし、それらの間の自然変換を射とする圏を **関手圏(functor category)** といい、 $\[\mathcal{C},\mathcal{D}\]$ や $\mathcal{D}^{\mathcal{C}}$ と書く。
{{% /definition %}}

{{% example title="射圏" %}}
対象が2つで、恒等射と対象の間に射が一本あるような圏 $\mathbf{2}$ から圏 $\mathcal{C}$ への関手のなす圏 $\[\mathbf{2},\mathcal{C}\]$ を **射圏(arrow category)** といい$\mathcal{C}^{\rightarrow}$ と書く。

関手 $\mathbf{2}\rightarrow\mathcal{C}$ は $\mathcal{C}$ の射と一対一対応する。

$$\xymatrix{
0 \ar[d]^{}=\"x\" & a \ar[d]_{}=\"y\"^f \\\\
1              & b
\ar@{~>} \"x\";\"y\"
}$$

従って、射圏とは射が対象で、可換な四角形が射となるような圏の事である。
$$\xymatrix{
a \ar[d]^f \ar[r]^p & c \ar[d]^g \\\\
b          \ar[r]_q & d          \\\\
}$$
{{% /example %}}

{{% example title="$M$-作用をもつ集合の圏" %}}
モノイド $M$ (を圏と見なしたもの)から$\mathbf{Set}$ への関手の圏
$\[M,\mathbf{Set}\]$ を$M$-$\mathbf{Set}$ と書く。

関手 $F:M\rightarrow\mathbf{Set}$ とはどんなものか考えると、
$M$ は対象が1つの圏であるから、$\mathbf{Set}$ の1つの対象と対応するのでこの集合を $X$ とする。$M$ の各射(これはモノイドの元)事に、対応する関数 $X\rightarrow X$ が存在する。つまり、写像(もしくは演算)
$$ \cdot: M\times X \rightarrow X$$
が存在する。そして $F$ が関手であることから、$M$の単位元を $e$ とすると $F(e)=1_x$ である。これは

- $M$ の単位元 $e$ と任意の $x\in X$ に対して $e\cdot x=x$

と同値。そして、任意の $a,b\in M$ に対して $F(ab)=F(a)\circ F(b)$ であるというのは

- 任意の $a,b\in M, x\in X$ に対して $a\cdot(b\cdot x)=(ab)\cdot x$

と同値。これはつまり $M$ が $X$ への **モノイド作用(monoid act)**  になっている事を表す。

すなわち $M$-$\mathbf{Set}$ とは $M$-作用を持つ集合が対象であり、それらの間の準同型写像が射である圏となる。 
{{% /example %}}

{{% example title="バンドルの圏" %}}
離散圏 $I$ から $\mathbf{Set}$ への関手の圏 $\[I,\mathbf{Set}\]$ を **$I$の上のバンドルの圏 (categories of bundles over $I$)** といい $\mathbf{Bn}(I)$ と書く。

一般に、集合 $I,X$ と関数 $p:I\rightarrow X$ の三つ組 $(I,p,X)$ をバンドルといい、$\mathbf{Bn}(I)$ はこのバンドルを対象とする圏である。

もしくは $I$ を添字集合とする集合族 $\\{X_i\\}\_{i\in I}$ を対象とし、関数の族 $\\{X_i\rightarrow Y_i\\}_{i\in i}$ を射とする圏とみなすこともできる。
{{% /example %}}

### スライス圏・部分対象

{{% definition title="スライス圏" %}}
圏 $\mathcal{C}$ と対象 $a\in\mathcal{C}$ に対して、
$x\rightarrow a$ の形の射を対象とし、以下の図式を可換にする $f:x\rightarrow y$ を $x\rightarrow a$ から $y\rightarrow a$ への射とする圏を $a$ 上の $\mathcal{C}$ の **スライス圏(slice category)** といい $\mathcal{C}/a$ と書く。
$$\xymatrix{
x \ar[rd] \ar[rr]^f & & y \ar[ld] \\\\
                    &a&
}$$

{{% /definition %}}

離散集合 $I$ に対して $\mathbf{Set}/I\simeq\mathbf{Bn}(I)$ である。
これは、関数 $f:X\rightarrow I$ と集合族 $\\{f^{-1}(i)\\}\_{i\in I}$ が一対一に対応することからわかる。

{{% definition title="部分対象" %}}

圏 $\mathcal{C}$ の対象 $a\in\mathcal{C}$ について、モノ射 $x\xhookrightarrow{} a$ を $\mathcal{C}/a$ における同型関係で割った同値類を $a$ の **部分対象(subobject)** という。

{{% /definition %}}

### 積圏

{{% definition title="積圏" %}}
圏 $\mathcal{C},\mathcal{D}$ に対して $\mathcal{C},\mathcal{D}$ の対象の組 $(a,b)$ を対象とし、射の組 $(f,g)$ を射とする圏を **積圏(product category)** といい $\mathcal{C}\times\mathcal{D}$ という。射の合成は要素毎に行う。
{{% /definition %}}

## 普遍性

驚くべき事実であるが、数学的な対象の多くがその内部構造(集合論に基づく古典的な考え方)ではなく,その対象が属する数学世界における他の対象との関係性(圏の中での対象や射を用いた考え方)を通して定義できることがよくある。後者は所謂、 **普遍性(universal property)** と呼ばれる性質を用いている。

ただし、ある圏において同型な対象は、それらが満足する圏論的な性質の観点からは区別することができない。実際、普遍性を用いた定義は、絶対的に一意に対象を決定するのではなく、与えられた圏内で **同型を除いて(up to isomorphism)** 一意に対象を決定するものとなる。

### 始対象・終対象

普遍性による定義の最も単純なものが、始対象・終対象である。

{{% definition title="始対象" %}}
圏 $\mathcal{C}$ の **始対象(initial object)** とは、任意の対象 $x\in\mathcal{c}$ に対して射 $0\rightarrow x$ が唯一つ存在するような対象 $0\in\mathcal{C}$ の事である。

始対象の双対概念を **終対象(terminal object)** という。すなわち、圏 $\mathcal{C}$ の任意の対象 $x\in\mathcal{c}$ に対して射 $x\rightarrow 1$ が唯一つ存在するような対象 $1\in\mathcal{C}$ の事である。
{{% /definition %}}

{{% proposition %}}
始対象・終対象は同型を除いて一意に定まる。
{{% /proposition %}}

{{% details 証明 %}}
$0,0'\in\mathcal{C}$ が共に始対象 であるとすると、射 $f:0\rightarrow 0', g:0'\rightarrow 0$ が存在し、
これらを合成すると $g\circ f:0\rightarrow 0$ が得られるが $0$ が始対象であることより $0\rightarrow 0$ は唯一つであるので $g\circ f=1_0$。同様にして $f\circ g=1_{0'}$ であるので$f:0\rightarrow 0'$ は同型射。よって $0\simeq 0'$。 終対象についても同様。
$$\xymatrix{
0 \ar[r]\_f \ar@/^1pc/[rr]^{1_0} & 0' \ar[r]\_g & 0
}$$
(証明終)
{{% /details %}}

### 極限

{{% definition title="図式としての関手" %}}

圏 $\mathcal{J}$ から $\mathcal{C}$ への関手 $F:\mathcal{J}\rightarrow\mathcal{C}$ を形が $\mathcal{J}$ である $\mathcal{C}$ における **図式(diagram)** という。

{{% /definition %}}

例えば $\mathcal{J}$ が対象が3つの
$$\xymatrix{
\bullet \ar[r] & \bullet & \bullet \ar[l]
}$$
のような圏 であるとすると、関手 $F:\mathcal{J}\rightarrow\mathcal{C}$ は$\mathcal{C}$ の中の以下の形の図式と同一視することができる。
$$\xymatrix{
a \ar[r] & c & b \ar[l]
}$$

{{% definition title="対角関手" %}}
圏 $\mathcal{J}$ と $\mathcal{C}$ について、対象 $i\in\mathcal{C}$ を定数関手 $i:\mathcal{J}\rightarrow\mathcal{C}$ に、射$f:i\rightarrow j$ を定数関手の間の自然変換(これは $f$ と同一視可能)に移す対応は関手
$$ \Delta:\mathcal{C}\rightarrow\mathcal{C}^{\mathcal{J}} $$
となる。これを **対角関手(diagonal functor)** という。
{{% /definition %}}

例えば、 $\mathcal{J}$ が2点集合の場合、定数関手 $a:\mathcal{J}\rightarrow\mathcal{C}$ は組 $(a,a)$ と同一視できるから、 $\Delta(a) \simeq (a,a)$ となる。

{{% definition title="錐" %}}
図式 $F:\mathcal{J}\rightarrow\mathcal{C}$ と対象 $x\in\mathcal{C}$ について、自然変換 $\phi:\Delta(x)\rightarrow F$ を **$x$ から $F$ への 錐(cone)** という。同じ錐を $(x,\phi)$ とも書く。

同様に、自然変換 $\phi:F\rightarrow\Delta(x)$ を **$F$ から $x$ への錐** もしくは **余錐(cocone)** という。
{{% /definition %}}

錐の$\mathcal{J}$ の射 $f:i\rightarrow j$ に対応する部分は左下の図式のようになっており、
上側は全て $x$ であるから書き直せば右下の三角形の図式となる。

$$\xymatrix{
x \ar[r]^{=} \ar[d]\_{\phi_a} & x \ar[d]^{\phi_b} \\\\
F(i) \ar[r]\_{F(f)} & F(j)
}
\qquad
\xymatrix{
x \ar[d]\_{\phi_a} \ar[rd]^{\phi_b} & \\\\
F(i) \ar[r]\_{F(f)} & F(j)
}$$

これを全て集めると、以下のような感じで頂点に $x$ があり、側面に現れる三角図式が全て可換であるようなものが錐である。


<script type="text/tikz">
  \begin{tikzpicture}
    \coordinate (x) at (0, 2.5) node at (x) [above] {$x$};
    \coordinate (a) at (-1, -1) node at (a) [below] {$F(i)$};
    \coordinate (b) at (1, -1) node at (b) [below] {$F(j)$};
    \coordinate (c) at (1.5, 0);
    \coordinate (d) at (0, 1);
    \coordinate (e) at (-1.3, 0.2);
    \draw [-latex, thick] (x) to (a);
    \draw [-latex, thick] (x) to (b);
    \draw [-latex] (x) to (c);
    \draw [-latex] (x) to (d);
    \draw [-latex] (x) to (e);
    \draw [-latex, thick] (a) to node [below] {\small $F(f)$} (b);
    \draw (b) to (c);
    \draw (c) to (d);
    \draw (d) to (e);
    \draw (e) to (a);
  \end{tikzpicture}
</script>

{{% definition title="錐の圏" %}}
図式 $F:\mathcal{J}\rightarrow\mathcal{C}$ への錐を対象とし、
$\phi:\Delta(x)\rightarrow F$ と $\psi:\Delta(y)\rightarrow F$ について、全ての $i\in\mathcal{J}$ について
$\phi_i = \psi_i\circ p$ が成立するような射 $p:x\rightarrow y$ を射 $\phi\rightarrow\psi$ とすると圏となる。これを **$F$ への錐の圏(category of cones to $F$)** という。

$$\xymatrix{
x \ar[r]^p \ar[d]\_{\phi\_a} & y \ar[ld]^{\psi\_a} \\\\
F(i) & \\\\
}$$

この双対概念を **$F$ からの錐の圏(category of cones from $F$)** という。
{{% /definition %}}

この圏のイメージは以下のようになる。すなわち $x$ から $F$ への錐を $p:x\rightarrow y$ と $y$ から $F$ への錐に分解できるという状況である。

<script type="text/tikz">
  \begin{tikzpicture}
    \coordinate (x) at (0, 2.5) node at (x) [above] {$x$};
    \coordinate (a) at (-1, -1) node at (a) [below] {$F(i)$};
    \coordinate (b) at (1, -1) node at (b) [below] {$F(j)$};
    \coordinate (c) at (1.5, 0);
    \coordinate (d) at (0, 1);
    \coordinate (e) at (-1.3, 0.2);
    \draw [-latex, thick] (x) to (a);
    \draw [-latex, thick] (x) to (b);
    \draw [-latex] (x) to (c);
    \draw [-latex] (x) to (d);
    \draw [-latex] (x) to (e);
    \draw [-latex, thick] (a) to node [below] {\small $F(f)$} (b);
    \draw (b) to (c);
    \draw (c) to (d);
    \draw (d) to (e);
    \draw (e) to (a);

    \coordinate (eq) at (2, 1) node at (eq) [above] {$=$};

    \coordinate (x_) at (4, 2.5) node at (x_) [above] {$x$};
    \coordinate (y_) at (5, 2.5) node at (y_) [above] {$y$};
    \coordinate (a_) at (3, -1) node at (a_) [below] {$F(i)$};
    \coordinate (b_) at (5, -1) node at (b_) [below] {$F(j)$};
    \coordinate (c_) at (5.5, 0);
    \coordinate (d_) at (4, 1);
    \coordinate (e_) at (2.7, 0.2);
    \draw [-latex] (x_) to (y_);
    \draw [-latex, thick] (y_) to (a_);
    \draw [-latex, thick] (y_) to (b_);
    \draw [-latex] (y_) to (c_);
    \draw [-latex] (y_) to (d_);
    \draw [-latex] (y_) to (e_);
    \draw [-latex, thick] (a_) to node [below] {\small $F(f)$} (b_);
    \draw (b_) to (c_);
    \draw (c_) to (d_);
    \draw (d_) to (e_);
    \draw (e_) to (a_);
  \end{tikzpicture}
</script>

{{% definition title="極限" %}}
$F:\mathcal{J}\rightarrow\mathcal{C}$ への錐の圏の終対象 $(\varprojlim F,\phi)$ を$F$の **極限(limit)** もしくは **射影的極限(projective limit)** という。また $\phi$ を **標準射影(canonical projection)** という。

$F:\mathcal{J}\rightarrow\mathcal{C}$ からの錐の圏の始対象 $(\varinjlim F,\psi)$ を$F$の **余極限(colimit)** もしくは **帰納的極限(inductive limit)** という。また $\phi$ を **標準入射(canonical inclusion)** という。


$\displaystyle\varprojlim F$ の代わりに、$\displaystyle \varprojlim_{i\in\mathcal{J}}F(i)$ とも書く。
{{% /definition %}}

極限は終対象であるから、同型を除いて一意に定まる。余極限も同様。

上の定義のように極限とは条件を満たすとなる"錐"(極限錐という)の事であるが、極限錐の頂点の事をさして極限という場合もある。しかし、同型な極限錐の頂点同士も同型であるし、逆に $a\simeq b$ で $a$ が極限錐の頂点であるならば、 $b$ もそれと同型な極限錐の頂点となる事が簡単に示せるので、用語の濫用は実用上は問題とならない。

{{% definition title="極限の保存" %}}
関手 $F:\mathcal{J}\rightarrow\mathcal{C}$ と $G: \mathcal{C}\rightarrow\mathcal{D}$ について極限 $(\varprojlim F,\\{\phi_x\\})$ を $G$ で移した $(G(\varprojlim F),\\{G(\phi_x)\\})$ が極限となるとき、$G$ は $F$ の極限を **保存する(preserves limit of $F$)** という。また、この時
$$ \varprojlim G\circ F \simeq G(\varprojlim F) $$
である。余極限についても同様。
{{% /definition %}}

### 極限の例
$\mathcal{J}$ として空圏(対象も射も空集合の圏)を取ると、極限は **終対象(terminal object)**　余極限は **始対象(initial object)** と一致。

$\mathcal{J}$ が離散圏の時の極限を **積(product)** 、余極限を **余積(coproduct)** という。それぞれ以下のように書く。
$$ \prod\_{i\in\mathcal{J}}F(i)\qquad\coprod\_{i\in\mathcal{J}}F(i) $$

$\mathcal{J}$ が2点集合の極限は、 $A\times B, A+B$。
3点以上の場合も同様に $A\times B\times C$ などと書く。

$\mathcal{J}$ が $\bullet\rightarrow\bullet\leftarrow\bullet$ という形の時の極限を **引き戻し(pullback)** という。図式が $A\rightarrow C\leftarrow B$ であるときの引き戻しを$ A\times\_{C} B $ と書く。

同様に、$\bullet\leftarrow\bullet\rightarrow\bullet$ という形の時の余極限を **押し出し(pushout)** といい、図式が $A\leftarrow C\rightarrow B$ であるときの押し出しを $ A+\_{C} B $ と書く。

$\mathcal{J}$ が $\bullet\rightrightarrows\bullet$ という形の時の極限を **イコライザ(equalizer)**、余極限を **コイコライザ(coequalizer)** という。並行射 $f,g$ についてのイコライザを $\mathrm{eq}(f,g)$、コイコライザを $\mathrm{coeq}(f,g)$ と書く。

### コンマ圏

錐の圏はコンマ圏という概念の特別な場合として説明することもできる。

{{% definition title="コンマ圏" %}}
圏 $\mathcal{A},\mathcal{B},\mathcal{C}$ と関手 $F:\mathcal{A}\rightarrow\mathcal{C}, G:\mathcal{B}\rightarrow\mathcal{C}$ について
$$\xymatrix{\mathcal{A} \ar[r]^F & \mathcal{C} & \mathcal{B} \ar[l]\_G}$$

$a\in\mathcal{A},b\in\mathcal{B}$ と$\mathcal{C}$ の射 $f:F(a)\rightarrow G(b)$ の三つ組 $(a,b,f)$ を対象とし、以下の図式を可換にする射の組 $(p,q)$ を射 $(a,b,f)\rightarrow(a',b',f')$ とする圏を **コンマ圏(comma category)** といい $F\downarrow G$ と書く。

$$\xymatrix{
F(a) \ar[d]\_{f} \ar[r]^{p}  & F(a') \ar[d]^{f'} \\\\
G(b)             \ar[r]\_{q} & G(b')
}$$

{{% /definition %}}

以前説明したスライス圏もコンマ圏の特別な場合である。

{{% proposition %}}
$$\mathrm{id}\_{\mathcal{C}}\downarrow a \simeq \mathcal{C}/a $$
ただし、左辺の $a$ は定数関手 $a:1\rightarrow\mathcal{C}$。
$$ \xymatrix{\mathcal{C}\ar[r]^{\mathrm{id}\_{\mathcal{C}}} & \mathcal{C} & 1 \ar[l]\_{a} } $$
{{% /proposition %}}

錐の圏は以下のようになる。

{{% proposition %}}
$$ \text{$F$ への錐の圏} \simeq \Delta\downarrow F$$
$$ \text{$F$ からの錐の圏} \simeq F\downarrow\Delta$$

$$\xymatrix{\mathcal{C}\ar[r]^{\Delta} & \mathcal{C}^{\mathcal{J}} & 1 \ar[l]\_{F}}$$
{{% /proposition %}}

$F$ への錐の件の方を具体的に書いてみると、まず $\Delta\downarrow F$ の対象は三つ組
$(\Delta(x), F, \phi)$ である。ここで $\phi$ は関手圏 $\mathcal{C}^{\mathcal{J}}$ の射、すなわち自然変換 $\phi:\Delta(x)\rightarrow F$ であって$F$ への錐の定義と一致する。
$\Delta\downarrow F$ の射は以下が可換図式となるような自然変換 $\Delta(p)$ である。
$$\xymatrix{
\Delta(x) \ar[d]\_{\phi} \ar[r]^{\Delta(p)} & \Delta{y} \ar[d]^{\psi} \\\\
F \ar[r]\_{=}                               & F
}$$

これをcomponent-wiseに書き直してみると、全ての $i\in\mathcal{C}$ について以下を可換とする射 $p$ が錐の間の射となる。以上にようにして、$\Delta\downarrow F$ が錐の圏と一致する事が分かる。

$$\xymatrix{
x \ar[d]\_{\phi_a} \ar[r]^{p} & y \ar[d]^{\psi_a} \\\\
F(i) \ar[r]\_{=}                               & F(i)
}$$

### 極限の存在定理

{{% theorem title="極限の存在定理" %}}
$\mathcal{C}$ が任意の並行射に対するイコライザと、圏 $\mathcal{J}$ の対象や射で添字付けられた任意の積を持つとする。この時、図式 $F:\mathcal{J}\rightarrow\mathcal{C}$ の極限は
$$ s, t: \prod\_{i\in\mathcal{J}}F(i)\rightrightarrows\prod\_{f: i\rightarrow j\in\mathcal{J}}F(j) $$
$$ \begin{align*}
s &= (F(f)\circ \pi_i)\_{f:i\rightarrow j\in\mathcal{J}} \\\\
t &= (\pi_j)\_{f:i\rightarrow j\in\mathcal{J}}
\end{align*}$$
のイコライザである。ここで、$\pi_k:\prod\_{i\in\mathcal{J}}F(i)\rightarrow F(k)$ は積の標準射影。
{{% /theorem %}}

{{% details 証明の概要 %}}
$x\in\mathcal{C}$ と射 $\phi:x\rightarrow\prod\_{i\in\mathcal{J}}F(i)$ について以下の図式が可換であるとする。
$$\xymatrix{
x \ar[r]^{\phi} & \prod\_{i\in\mathcal{J}}F(i) \ar@<2pt>[r]^s \ar@<-2pt>[r]_t & \prod\_{f: i\rightarrow j\in\mathcal{J}}F(j) 
}$$

$\phi=(\phi_i)\_{i\in\mathcal{J}}$ とおくと、これは全ての $\mathcal{J}$ の射 $f:i\rightarrow j$ に対して、$j\in\mathcal{J}, F(f)\circ \phi_i = \phi_j$ であること、すなわち以下の図式が可換であることと同値。
$$\xymatrix{
x \ar[d]\_{\phi_i} \ar[rd]^{\phi_j} \\\\
F(i) \ar[r]_{F(f)} & F(j)
}$$
すなわち、 $(x,\\{\phi_i\\})$ は $F$ への錐に他ならない。
{{% /details %}}

双対をとれば、余極限をコイコライザと余積によって表現する定理も同様に得られる。

### 関手圏の極限

{{% theorem title="関手圏の極限は各点毎に計算可能" %}}
図式 $F:\mathcal{J}\rightarrow\mathcal{D}^{\mathcal{C}}$ について
$a\in \mathcal{C}$ に固定した関手 $F(-)(a):\mathcal{J}\rightarrow\mathcal{D} $ の極限 $\varprojlim_{i\in\mathcal{J}} F(i)(a)$ が全ての $a\in\mathcal{C}$ について存在するならば、$F$ の極限も存在し

$$ \left(\varprojlim\_{i\in\mathcal{J}} F(i)\right)(a) \simeq \varprojlim_{i\in\mathcal{J}} F(i)(a) $$

である。余極限についても同様。
{{% /theorem %}}
{{% details 証明 %}}

全ての $a\in\mathcal{C}$ について $\varprojlim\_{i\in\mathcal{J}} F(i)(a)$ が存在するとする。
$\mathcal{J}$ の射 $f: i\rightarrow j$ に対応する自然変換 $F(f):F(i)\rightarrow F(j)$ を $\mathcal{C}$ の射 $u: a\rightarrow b$ についてcomponent-wiseに描くと以下のようになり、これが全ての $f:i\rightarrow j$ と $u:a\rightarrow b$ について可換となる。

$$ \xymatrix{
F(i)(a) \ar[d]\_{F(f)_a} \ar[r]^{F(i)(u)}  & F(i)(b) \ar[d]^{F(f)_b} \\\\
F(j)(a)                  \ar[r]\_{F(j)(u)} & F(j)(b)
}$$

ここで $\varprojlim\_{i\in\mathcal{J}} F(i)(a)$ が存在するので、下図のような極限錐がそれぞれ存在する。

$$ \xymatrix{
\varprojlim\_{i\in\mathcal{J}}F(i)(a) \ar[rd] \ar@/_1pc/[rdd] &&& \varprojlim\_{i\in\mathcal{J}}F(i)(b) \ar[ld] \ar@/^1pc/[ldd] \\\\
& F(i)(a) \ar[d]\_{F(f)_a} \ar[r]^{F(i)(u)} & F(i)(b) \ar[d]^{F(f)_b}& \\\\
& F(j)(a)                  \ar[r]\_{F(j)(u)} & F(j)(b)                &
}$$

ここで $\varprojlim\_{i\in\mathcal{J}}F(i)(a)$ の錐の側面に各 $F(i)(u)$ (図の水平の射) を合成したものは $F(-)(b):\mathcal{J}\rightarrow\mathcal{D}$ への錐となるので、下図が可換となる射 $\bar{u}: \varprojlim\_{i\in\mathcal{J}}F(i)(a)\rightarrow\varprojlim\_{i\in\mathcal{J}}F(i)(b)$ が唯一つ存在。

$$ \xymatrix{
\varprojlim\_{i\in\mathcal{J}}F(i)(a) \ar[rd] \ar@/_1pc/[rdd] \ar@{.>}[rrr]^{\bar{u}} &&& \varprojlim\_{i\in\mathcal{J}}F(i)(b) \ar[ld] \ar@/^1pc/[ldd] \\\\
& F(i)(a) \ar[d]\_{F(f)_a} \ar[r]^{F(i)(u)} & F(i)(b) \ar[d]^{F(f)_b}& \\\\
& F(j)(a)                  \ar[r]\_{F(j)(u)} & F(j)(b)                &
}$$

そこで、$\mathcal{C}$ の各対象 $a$ に $\varprojlim\_{i\in\mathcal{J}}F(i)(a)$ を、射 $u:a\rightarrow b$ に $\bar{u}$ を対応させる関係を考えるとこれは関手 $G: \mathcal{C}\rightarrow\mathcal{D}$ となる。これが $\varprojlim\_{i\in\mathcal{J}}F(i)$ である事を示す。

そこで任意の $H:\mathcal{C}\rightarrow\mathcal{D}$ から $F$ への錐を考える。
$$ \xymatrix{
\varprojlim\_{i\in\mathcal{J}}F(i)(a) \ar[rd] \ar@/_1pc/[rdd] \ar@{.>}[rrr]^{\bar{u}} &&& \varprojlim\_{i\in\mathcal{J}}F(i)(b) \ar[ld] \ar@/^1pc/[ldd] \\\\
& F(i)(a) \ar[d]\_{F(f)_a} \ar[r]^{F(i)(u)} & F(i)(b) \ar[d]^{F(f)_b}& \\\\
& F(j)(a)                  \ar[r]\_{F(j)(u)} & F(j)(b)                & \\\\
H(a) \ar[ru] \ar@/^1pc/[ruu] \ar[rrr]^{H(u)} &&& H(b) \ar[lu] \ar@/_1pc/[luu]
}$$

この左側だけに注目すると $\varprojlim_{i\in\mathcal{J}}$ についての普遍性より以下を可換にする射 $H(a)\rightarrow\varprojlim_{i\in\mathcal{J}}F(i)(a)$ が一意に存在。右側も同様。

$$ \xymatrix{
\varprojlim\_{i\in\mathcal{J}}F(i)(a) \ar[rd] \ar@/_1pc/[rdd] \ar@{.>}[rrr]^{\bar{u}} &&& \varprojlim\_{i\in\mathcal{J}}F(i)(b) \ar[ld] \ar@/^1pc/[ldd] \\\\
& F(i)(a) \ar[d]\_{F(f)_a} \ar[r]^{F(i)(u)} & F(i)(b) \ar[d]^{F(f)_b}& \\\\
& F(j)(a)                  \ar[r]\_{F(j)(u)} & F(j)(b)                & \\\\
H(a) \ar[ru] \ar@/^1pc/[ruu] \ar@{.>}[uuu] \ar[rrr]^{H(u)} &&& H(b) \ar[lu] \ar@/_1pc/[luu] \ar@{.>}[uuu]
}$$

この射の族 $\\{H(a)\rightarrow\varprojlim_{i\in\mathcal{J}}F(i)(a)\\}$ は自然変換 $H\rightarrow G$ となり、これが一意であるので $G\simeq \varprojlim\_{i\in\mathcal{J}}F(i)$ である。(証明終)
{{% /details %}}

## 随伴
**随伴(adjunction)** は2つの関手の間の関係であるが、

> "Adjoint functors arise everywhere”
> (S. Mac Lane, Categories for the working mathematician)

とマクレーンが言っているように、数学の様々な場所で普遍的に現れる重要な概念である。

{{% definition title="随伴" %}}
圏 $\mathcal{C}$ と $\mathcal{D}$ の間の **随伴(adjunction)** とは、
関手 $F:\mathcal{C}\rightarrow\mathcal{D}$ と $G:\mathcal{D}\rightarrow\mathcal{C}$ の対であり、以下の2つの関手 $\mathcal{C}^{\mathrm{op}}\times\mathcal{D}\rightarrow\mathbf{Set}$ の間の自然同型

$$ \phi: \mathcal{D}(F(-), -)\longrightarrow\mathcal{C}(-,G(-)) $$

が存在するものをいう。言い換えれば、 任意の $a\in\mathcal{C},b\in\mathcal{D}$ に対して全単射
$$ \mathcal{D}(F(a), b)\simeq\mathcal{C}(a,G(b)) $$
が存在し、これが $a,b$ について自然となるものをいう。

この時 $F$ を $G$ の**左随伴(left adjoint)**、 $G$ を$F$ の **右随伴(right adjoint)** といい、 $F\dashv G$ と書く。
{{% /definition %}}
