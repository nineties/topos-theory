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
- 各 $a, b\in\mathrm{Ob}(\mathcal{C})$ に対して **射(arrow)** の集合 $\mathcal{C}(a,b)$
- 各 $a,b,c\in\mathrm{Ob}(\mathcal{C})$ に対して射の **合成(composition)**
$$ \mathcal{C}(a,b)\times\mathcal{C}(b,c)\ni(f,g)\mapsto g\circ f\in\mathcal{C}(a,c)$$

からなり、以下の2条件を満たすものである。

1. 任意の $f\in\mathcal{C}(a,b), g\in\mathcal{C}(b,c),h\in\mathcal{C}(c,d)$ に対して
    $$ h\circ(g\circ f) = (h\circ g)\circ f $$
    (よって 括弧を外して $h\circ g\circ f$ と書いても問題ない)
2. 任意の $a\in\mathrm{Ob}(\mathcal{C})$ について **恒等射(identity arrow)** $1_a\in\mathcal{C}(a,a)$ が存在し、任意の $f\in\mathcal{C}(a,b)$ について
    $$ f\circ 1_a = 1_b\circ f = f$$

$f \in\mathcal{C}(a,b)$ の代わりに、$f \in\mathrm{Hom}\_{\mathcal{C}}(a,b)$ や $f:a\rightarrow b$ とも書く。$a$ を $f$ の **ドメイン(domain)** と呼び $\mathrm{dom}(f)=a$ と書く。同様に、 $b$ を **コドメイン(codomain)** と呼び $\mathrm{cod}(f)=b$ と書く。

{{% /definition %}}

対象や射の集まりとして集合より大きな **類,クラス(class)** を用いる事でより大きな圏を考える事もできる。また、圏の定義は一階述語理論的な公理化も可能である。

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
- $\mathrm{Arr}(f)$ を $f\in\coprod_{a,b\in\mathrm{Ob}(\mathcal{C})}\mathcal{C}(a,b)$
- $\mathrm{Dom}(f)$ を $\mathrm{dom}(f)$、$\mathrm{Cod}(f)$ を $\mathrm{cod}(f)$、$\mathrm{Id}(a)$ を $1_a$、$\circ$ を $\circ$

と解釈することでこの公理系を満たす。

圏論では等式の代わりに **可換図式(commutative diagram)** を用いる事が多い。例えば $g\circ f=h$ であるということを「以下の図式が可換である」などと表現する。図式が可換であるとは、図式内の射の列の合成射は始点と終点が一致するならば経路の捕り方によらず一致するということ。

$$
\xymatrix {
a \ar[d]^f \ar[rd]^h &      \\\\
b \ar[r]^g & c
}
$$

{{% proposition %}}
任意の対象 $a$ に対して、恒等射 $1_a$ は一意に定まる。
{{% /proposition %}}
{{% details 証明 %}}
$1_a,1'_a: a\rightarrow a$ が共に恒等射であるとすると、以下の図式が可換となるから $1_a=1'_a$ (証明終)
$$
\xymatrix {
a \ar[r]^{1_a} \ar@/^2pc/[rr]^{1_a} \ar@/_2pc/[rr]\_{1'\_a} & a \ar[r]^{1'_a} & a 
}
$$
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
ある命題が圏 $\mathcal{C}$ で真であるとき、射の向きを全て逆に合成の順序を入れ替えて得られる **双対命題(dual statement)** は圏 $\mathcal{C}^{\mathrm{op}}$ でも真である。
{{% /theorem %}}

$\mathcal{C}^{\mathrm{op}}$ の双対は $\mathcal{C}$ だから結局

$$ \text{命題 $P$ が圏 $\mathcal{C}$ で真} \Leftrightarrow \text{$P$ の双対命題が $\mathcal{C}^{\mathrm{op}}$ で真} $$

である。単純な原理であるが、圏論の言語での2つの双対命題は、それを「具体的な」圏で解釈したときには、非常に異なる(しかも同値ではない!)命題となる事がある。
時折、通常の数学的命題の圏論の言語を用いた抽象的な証明を得ることが可能である。そのような場合は、双対原理を用いることで、元の文脈における双対バージョンの命題を得ることができる。

### 圏の例

数学対象と対象とし、その間の写像を射とする圏は様々な存在する。例えば

- $\mathbf{Set}$: **集合**と**写像**
- $\mathbf{Top}$: **位相空間**と**連続写像**
- $\mathbf{Gr}$: *群* と **群の準同型写像**
- $\mathbf{Rng}$: *環* と **間の準同型写像**
- $\mathbf{Vect}\_{K}$: 体 $K$ 上の **ベクトル空間** と **線型写像**

などである。実際、任意の一階の理論(一階述語理論で記述された理論) $\mathbb{T}$ に対して、(集合論ベースの)モデルを対象とし、その間の準同型写像を射とする圏 $\mathbb{T}\mathrm{-mod}(\mathbf{Set})$ を考える事ができる。

また、数学的対象「1つ」を圏と見なす事もできる。例えば

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
射 $m: a\rightarrow b$ が **モノ射(mono-morphism)** もしくは **モニック射(monic)** であるとは、任意の対象 $c$ と射 $f,g: c\rightarrow a$ について
$$ m\circ f = m\circ g \quad\Rightarrow\quad f=g $$
が成り立つことである。この性質を$m$は **左簡約可能(left cancelable)** であるという。

$$
\xymatrix {
c \ar@<2pt>[r]^{f} \ar@<-2pt>[r]\_{g} & a \ar[r]^{m} & b
}
$$
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

逆に $e:A\rightarrow B$ を全射とし、集合 $C$ と写像 $f,g:B\rightarrow C$ が $f\circ e = g\circ e$ をみたするとする。任意の $x\in B$ についてある $y\in A$ が存在して $x=e(y)$ と書けるので $f(x)=g(x)$ である。よって $e$ はエピ射。(証明終)
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
- 任意の$f:a\rightarrow b, g:b\rightarrow f$ について $F(g\circ f)=F(g)\circ F(f)$

を満たすものである。
{{% /definition %}}

恒等写像であるような関手 $F$ を **恒等関手(identity functor)** といい $\mathrm{id}_\mathcal{C}:\mathcal{C}\rightarrow\mathcal{C}$ と書く。
また、関手 $F:\mathcal{C}\rightarrow\mathcal{D}, G:\mathcal{D}\rightarrow\mathcal{E}$ に対して対象・射共に通常の関数合成を行うと$\mathcal{C}$ から $\mathcal{E}$ への関手が得られる。これを関手の合成といい $G\circ F:\mathcal{C}\rightarrow\mathcal{E}$ と書く。

{{% definition title="反変関手" %}}
$\mathcal{C}^{\mathrm{op}}$ から $\mathcal{D}$ への関手 $F:\mathcal{C}^{\mathrm{op}}\rightarrow\mathcal{D}$ を、$\mathcal{C}$ から $\mathcal{D}$ への **反変関手(contravariant functor)** という。
{{% /definition %}}

{{% definition title="小さい圏の圏" %}}
小さい圏を対象、関手を射とした圏は(小さくない)圏となる。これを $\mathbf{Cat}$ と書く。
{{% /definition %}}

{{% definition title="前層" %}}
圏 $\mathcal{C}$ から $\mathbf{Set}$ への反変関手
$$ F:\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$$
を $\mathcal{C}$ 上の **前層(presheaf)** という。
{{% /definition %}}

{{% definition title="自然変換" %}}
関手 $F,G:\mathcal{C}\rightarrow\mathcal{D}$ に対して、$F$ から $G$ への**自然変換(natural transformation)** $\phi:F\rightarrow G$ とは、$\mathcal{C}$ の対象 $a$ に、$\mathcal{D}$の射 $\phi(a): F(a)\rightarrow G(a)$ を対応させる関数であり、任意の $\mathcal{C}$ の射 $f:a\rightarrow b$ に対して、以下の図式が可換となるものである。

$$\xymatrix{
F(a) \ar[r]^{\phi(a)} \ar[d]\_{F(f)} & G(a) \ar[d]^{G(f)} \\\\
F(b) \ar[r]^{\phi(b)} & G(b)
}$$

$\phi(a)$ が全て同型射であるとき $\phi$ を **自然同型(natural isomorphism)** もしくは **自然同値(natural equivalence)** という。また自然同型 $\phi:F\rightarrow G$ が存在する時 $F\simeq G$ と書く。
{{% /definition %}}

{{% example %}}
ベクトル空間をその双対ベクトル空間に写す反変関手
$$ \*:\mathbf{Vect}\_K^{\mathrm{op}}\ni V\longmapsto V^\*=\mathbf{Vect}_K(V,K)\in\mathbf{Vect}\_K $$

について $\mathrm{Id}\_{\mathbf{Vect}\_K}\rightarrow **$ は自然変換である。
{{% /example %}}
これは自然同型ではないので注意。一般に無限次元のベクトル空間 $V$ については $V\not\simeq V^{**}$

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

{{% details 証明 %}}
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
{{% /definitio %}}

表現可能という言葉の意味については、後述する米田の補題の所で説明する。

{{% definition title="充満・忠実・本質的全射" %}}
関手 $F:\mathcal{C}\rightarrow\mathcal{D}$ について

- $F: \mathcal{C}(a,b)\rightarrow\mathcal{D}(F(a),F(b))$ が全ての$a,b\in\mathcal{C}$ について全射の時 $F$ は **充満(full)** であるという。
- $F: \mathcal{C}(a,b)\rightarrow\mathcal{D}(F(a),F(b))$ が全ての$a,b\in\mathcal{C}$ について単射の時 $F$ は **忠実(faithful)** であるという。
- $F: \mathrm{Ob}(\mathcal{C})\rightarrow\mathrm{Ob}(\mathcal{D})$ が全射の時 $F$ は **本質的全射(essentially surjective)**  であるという。
{{% /definition %}}
