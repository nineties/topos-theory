---
title: 圏論I
weight: 3
section: 2
toc: true
---

## 圏論の概要

**圏論(category theory)** は、1942-45年にSamuel EilenbergとSaunders Mac Laneによって代数的位相幾何学の研究の中で発明された数学の一分野であり、数学的概念を表現し議論するための抽象的な言語を提供する。
圏論の諸概念は、それらの例を数学のあらゆる分野で見つけることができる。
圏論に通底する哲学は、集合論を構成する **集合と関数** という原始的な概念を、集合と関数の概念を抽象化した、 **対象と射** という概念に置き換えることである。
さらに言えば、それらを更に抽象化した **関手と自然変換** という概念に置き換えることである。

圏論が発明されて以来、そのアプローチは数学者が各々の主題を捉える方法に深いパラダイムシフトをもたらし、以前ではほとんど不可能だった重要な発見への道を開いた。
圏論の大きな成果の一つがトポス理論であり、これは全面的に圏論の言語で書かれた理論である。

## 圏

圏とは集合と関数の概念を抽象化した **対象と射** からなり、関数の合成を抽象化した演算を持つものである。集合と関数全体、ベクトル空間と線形写像全体、群と群準同型写像全体など様々なものを圏と見なすことができる。

### 圏の定義

{{% definition title="圏" label="def.category" %}}
**圏(category)** $\mathcal{C}$ とは **対象(object)** の類 $\mathrm{Ob}(\mathcal{C})$ と各対象 $a, b$ ごとに定められた **射(arrow)** の類 $\mathcal{C}(a,b)$ からなる。 $\mathcal{C}(a,b)$ の事を、**hom類(hom-class)** (集合である場合には **hom集合(hom-set)**) と呼び、$\mathrm{Hom}\_{\mathcal{C}}(a,b)$ と書くこともある。また、射 $f\in\mathcal{C}(a, b)$ を $f:a\rightarrow b$ と書いたり、以下のような矢印の図式で表したりする。
$$\xymatrix{ a \ar[r]^f & b } $$
$a$ を $f$ の **ドメイン(domain)** と呼び $\mathrm{dom}(f)=a$ と書く。同様に、 $b$ を **コドメイン(codomain)** と呼び $\mathrm{cod}(f)=b$ と書く。

そして、以下を満たす。

1. 任意の射 $f:a\rightarrow b, g:b\rightarrow c$ について、これらの **合成(composition)** $g\circ f: a\rightarrow c$ が存在する。
$$\xymatrix{ a \ar[r]\_f \ar@/^1pc/[rr]^{g\circ f} & b \ar[r]\_g & c }$$
2. 射の合成は結合的である。(よって 括弧を外して $h\circ g\circ f$ と書いても問題ない)
$$ h\circ (g\circ f) = (h\circ g)\circ f$$
3. 各対象 $a$ について **恒等射(identity arrow)** $1_a:a\rightarrow a$ が存在し、任意の $f: a\rightarrow b$ について以下を満たす。
    $$ f\circ 1_a = 1_b\circ f = f$$

射の類が全て集合である圏を **局所小圏(locally small category)**、対象の類も射の類も集合である圏を **小圏(small category)** という。
{{% /definition %}}

例えば、以下のような数学的対象とその間の準同型写像を射とする圏が様々存在する。
これらの圏は全て局所小圏であるが小圏ではない。

- $\mathbf{Set}$: **集合**と**写像**
- $\mathbf{Top}$: **位相空間**と**連続写像**
- $\mathbf{Grp}$: **群** と **群の準同型写像**
- $\mathbf{Rng}$: **環** と **環の準同型写像**
- $\mathbf{Mod}_R$: **R加群** と **加群の準同型写像**
- $\mathbf{Vect}\_{K}$: **体 $K$ 上のベクトル空間** と **線型写像**

これらの例は全て(何らかの性質を備えた)集合と写像からなる圏であるが、
対象と射は定義を満たすものであればどのようなものであっても構わない。
例えば以下のようなものも圏である。これらは小圏である。

- **集合** : 射が恒等射のみである小圏。 **離散圏(discrete category)** ともいう。
- **モノイド**: 対象が1つしかない小圏。
- **半順序集合** : $a \leq b$ を射 $a\rightarrow b$ と見なしたもの。任意の対象 $a,b$ について射 $a\rightarrow b$ が高々一つであり、$a\rightarrow b$ と $b\rightarrow a$ が共に存在するならば $a=b$ であるような小圏。半順序集合(partially ordered set)を略して **poset** とも言う。

また、以下のような単純な圏も部品として様々な場面で用いられる

- $\mathbf{0}$: 対象の類も射の類も空集合であるような圏。**空圏(empty category)** という。
- $\mathbf{1}$: 対象が1つで、恒等射のみの圏
- $\mathbf{2}$: 対象が2つで、恒等射以外の射が1つの圏
- $\mathbf{3}$: 対象が3つで、恒等射以外の射が3つ(1つは他2つの合成)の圏

$$
\xymatrix {
\mathbf{1} & \mathbf{2}    &          & \mathbf{3} & \\\\
\bullet    & \bullet\ar[r] & \bullet  & \bullet \ar[r] \ar@/^1pc/[rr] & \bullet \ar[r] & \bullet \\\\
}
$$

圏論では射の等式の代わりに **可換図式(commutative diagram)**  を用いる事が多い。
図式が可換であるとは、図式内の射の列の合成射は始点と終点が一致するならば経路の選び方によらず一致するということ。
例えば $g\circ f=h$ であるということを「以下の図式が可換である」などと表現する。

$$
\xymatrix {
a \ar[d]_f \ar[rd]^h &      \\\\
b \ar[r]_g & c
}
$$

では可換図式を用いて、命題を一つ証明してみる。

{{% proposition %}}
任意の対象 $a$ に対して、恒等射 $1_a$ は一意に定まる。
{{% /proposition %}}
$1_a,1'\_a: a\rightarrow a$ が共に恒等射であるとすると、以下の図式の上半分、下半分がいずれも恒等射の性質より可換となるから、図式を辿って $1_a=1'\_a$ を得る $\square$

$$
\xymatrix {
a \ar[r]^{1_a} \ar@/^2pc/[rr]^{1_a} \ar@/_2pc/[rr]\_{1'\_a} & a \ar[r]^{1'_a} & a 
}
$$

このような図式を辿る事による証明方法をdiagram chasingという。

{{% definition title="同型" %}}
$f: a\rightarrow b,\ g: b\rightarrow a$ が
$$ g\circ f=1_a,\ f\circ g=1_b $$
を満たす時、 $f,g$ を **同型射(isomorphism)** という。 $g$ を $f$ の **逆射(inverse morphism)** と呼び $f^{-1}$ と書く。

$$
\xymatrix {
a \ar@(ul,dl)[]_{1_a} \ar@/^/[rr]|{f} && b \ar@/^/[ll]|{g} \ar@(ur,dr)[]^{1_b}
}
$$

対象 $a,b$ の間に同型射が存在する時これらは **同型(isomorphic)** であるといい、
$$ a\cong b $$
と書く。
{{% /definition %}}
{{% proposition %}}
$f: a\rightarrow b$ が同型射の時、その逆射は一意に定まる。
{{% /proposition %}}
{{% details 証明 %}}
$f: a\rightarrow b$ が同型射であるとし $g,h:b\rightarrow a$ は共に逆射 であるとすると $ g = g\circ 1_b = g\circ f\circ h = 1_a\circ h = h $ $\square$
{{% /details %}}

同型関係は同値関係である。すなわち任意の対象 $a,b,c$ に対して

1. $a\cong a$
2. $a\cong b, b\cong c \Rightarrow a\cong c$
3. $a\cong b \Rightarrow b\cong a$

が成り立つ。

圏から新しい圏を作る様々な操作が可能である。最も基本的な構成として積圏がある。これは集合の直積を一般化したようなものである。(実際 $\mathcal{C},\mathcal{D}$ が離散圏なら $\mathcal{C}\times\mathcal{D}$ はその直積集合となる。)

{{% definition title="積圏" %}}
圏 $\mathcal{C},\mathcal{D}$ に対して $\mathcal{C},\mathcal{D}$ の対象の組 $(a,b)$ を対象とし、射の組 $(f,g)$ を射とする圏を **積圏(product category)** といい $\mathcal{C}\times\mathcal{D}$ 書く。射の合成は要素毎に行う。
{{% /definition %}}

圏の一部だけを取り出したものを部分圏という。

{{% definition title="部分圏" %}}
圏 $\mathcal{C}$ の対象の類の部分類、射の類の部分類からなり圏の条件を満たす圏 $\mathcal{D}$ を $\mathcal{C}$ の **部分圏(subcategory)** という。

任意の対象 $a,b\in\mathcal{D}$ に対して $\mathcal{D}(a,b) = \mathcal{C}(a,b)$ である部分圏 $\mathcal{D}$ を **充満部分圏(full subcategory)** という。
{{% /definition %}}

### 双対性

圏の射の向きを全て逆にした圏を双対圏という。

{{% definition title="双対圏" %}}
圏 $\mathcal{C}$ の **双対圏(dual category)** $\mathcal{C}^{\mathrm{op}}$とは
$$ \mathrm{Ob}(\mathcal{C}^{\mathrm{op}}) = \mathrm{Ob}(\mathcal{C}),\ \mathcal{C}^{\mathrm{op}}(a,b)=\mathcal{C}(b,a) $$

であり $f\in\mathcal{C}^{\mathrm{op}}(a,b), g\in\mathcal{C}^{\mathrm{op}}(b,c)$ に対してその合成を
$$ g\circ_{\mathcal{C}^\mathrm{op}}f = f\circ_{\mathcal{C}} g $$
と定めたもの。${\mathcal{C}^{\mathrm{op}}}^{\mathrm{op}}$ は $\mathcal{C}$ と一致する。
{{% /definition %}}

圏論における多くの概念は、その双対版が存在するが、以下の原理から一方について証明が出来ればもう一方は自動的に示される。

{{% theorem title="双対原理" %}}
ある命題が圏 $\mathcal{C}$ で真であるとき、射の向きを全て逆にし合成の順序を入れ替えて得られる **双対命題(dual statement)** は圏 $\mathcal{C}^{\mathrm{op}}$ でも真である。
{{% /theorem %}}

単純な原理であるが、圏論の言語での2つの双対命題は、それを「具体的な」圏で解釈したときには、非常に異なる(しかも同値ではない!)命題となる事がある。
時折、通常の数学的命題の圏論の言語を用いた抽象的な証明を得ることが可能である。そのような場合は、双対原理を用いることで、元の文脈における双対バージョンの命題を得ることができる。

双対な概念の例として、モノ射・エピ射を取り上げる。これらは単射・全射を抽象化したものである。また、トポス理論においては **部分対象(subobject)** を定義する為にモノ射が利用される。

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

冒頭で述べたように、モノ射・エピ射は単射・全射の概念を抽象化したものであり $\mathbf{Set}$ においては実際に一致する。 **ただし、一般の圏においては、単射・全射とモノ・エピは一致しない** ので注意。

{{% proposition %}}
$\mathbf{Set}$ おいてモノ射とは単射の事である。
{{% /proposition %}}
{{% details 証明 %}}
$m: A\rightarrow B$ をモノ射とする。対象$x,y\in A$ について $m(x) = m(y)$  であるとすると、$x,y$ を一点集合からの写像 $1\rightarrow A$ と見なせば $m\circ x=m\circ y$ であるので $m$ がモノ射であることより $x=y$。従って $m$ は単射である。

逆に $m: A\rightarrow B$ が単射であるとする。写像 $f,g: C\rightarrow A$ が $m\circ f=m\circ g$ をみたすならば、任意の $x\in C$ について $m(f(x))=m(g(x))$ であるから $m$ が単射であることより $f(x)=g(x)$。従って $f=g$ であるから $m$ はモノ射である。$\square$
{{% /details %}}

{{% proposition %}}
$\mathbf{Set}$ おいてエピ射とは全射の事である。
{{% /proposition %}}
{{% details 証明 %}}
$e: A\rightarrow B$ をエピ射とする。$e$ が全射でないとし、写像 $f,g:B\rightarrow\\{0,1\\}$ を以下のように定義する。

$$ f(x) = 0,\ g(x)=\begin{cases}
0   & (x\in e(A)) \\\\
1   & (x\not\in e(A))
\end{cases}
$$

すると、$f\circ e = g\circ e$ である。しかし $e$ が全射でないことより$x\not\in e(A)$ すなわち $f(x)\neq g(x)$ となる$x\in B$が少なくも一つ存在するから $f\neq g$ である。これは矛盾であるので $e$ は全射である。

逆に $e:A\rightarrow B$ を全射とし、写像 $f,g:B\rightarrow C$ が $f\circ e = g\circ e$ をみたすとすると任意の $x\in B$ についてある $y\in A$ が存在して $x=e(y)$ と書けるので $f(x)=g(x)$ である。よって $f=g$ であるから $e$ はエピ射。$\square$
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

## 関手

例えばベクトル空間の間に、その構造を保つ写像として線型写像が定義されるように、圏の間にも構造を保つ写像を定める事ができる。これを関手という。関手を用いると、異なる圏の間の関係性を述べる事ができるようになる。

### 関手の定義

{{% definition title="関手" %}}
圏 $\mathcal{C}$ から圏 $\mathcal{D}$ への **関手(functor)** もしくは **共変関手(covariant functor)** $F$ とは
写像 $F:\mathrm{Ob}(\mathcal{C})\rightarrow\mathrm{Ob}(\mathcal{D})$ と任意の対象 $a,b\in\mathcal{C}$ に対する写像 $F:\mathcal{C}(a,b)\rightarrow \mathcal{D}(F(a), F(b))$ であり

- 任意の対象 $a\in\mathcal{C}$ について $F(1\_a)=1\_{F(a)}$
- 任意の$f:a\rightarrow b, g:b\rightarrow c$ について $F(g\circ f)=F(g)\circ F(f)$

を満たすものである。
{{% /definition %}}

恒等写像であるような関手 $F$ を **恒等関手(identity functor)** といい $1\_\mathcal{C}:\mathcal{C}\rightarrow\mathcal{C}$ や $\mathrm{id}\_{\mathcal{C}}$ と書く。
また、関手 $F:\mathcal{C}\rightarrow\mathcal{D}, G:\mathcal{D}\rightarrow\mathcal{E}$ に対して対象・射共に通常の関数合成を行うと$\mathcal{C}$ から $\mathcal{E}$ への関手が得られる。これを関手の合成といい $G\circ F:\mathcal{C}\rightarrow\mathcal{E}$ と書く。 $\circ$ を省略して $GF$ と書くこともある。すると、以下のような圏を構成できる事が分かる。

{{% definition title="小圏のなす圏" %}}
小圏を対象、関手を射とすると(大きな)圏となる。これを $\mathbf{Cat}$ と書く。
{{% /definition %}}

射の向きが逆になるような対応を反変関手という。

{{% definition title="反変関手" %}}
$\mathcal{C}^{\mathrm{op}}$ から $\mathcal{D}$ への関手 $F:\mathcal{C}^{\mathrm{op}}\rightarrow\mathcal{D}$ を、$\mathcal{C}$ から $\mathcal{D}$ への **反変関手(contravariant functor)** という。
{{% /definition %}}

全てを一つの対象に潰す関手を定数関手という。

{{% definition title="定数関手" %}}
関手 $\mathcal{C}\rightarrow\mathcal{D}$ であって、$\mathcal{C}$ の全ての対象をある対象 $a\in\mathcal{D}$ に、射を $1_a$ に移すものを **定数関手(constant functor)** という。対象 $a$ についての定数関手を同じ記号を用いて $a:\mathcal{C}\rightarrow\mathcal{D}$ と書くこともある。
{{% /definition %}}

### 図式としての関手

今後の為に、関手を **図式(diagram)** とみなす考え方に慣れておいた方が良い。
図式の方が視覚的なイメージを得やすい為、今後登場する抽象的・高階な概念や定理の理解がしやすくなる。
例えば関数 $\mathbb{N}\rightarrow\mathbb{R}$ について考える、ということと実数列 $a_0,a_1,\ldots$ について考えるという事は同じ事であるが、後者の方がイメージを得やすい場面もあるだろう。これと同じ事である。

{{% definition title="図式としての関手" label="def.functor-as-a-diagram" %}}
圏 $\mathcal{J}$ から $\mathcal{C}$ への関手 $F:\mathcal{J}\rightarrow\mathcal{C}$ を形が $\mathcal{J}$ である $\mathcal{C}$ における **図式(diagram)** という。このとき、$\mathcal{J}$ を **添字圏(index category)** という。
{{% /definition %}}
$\mathcal{J}$ という文字を使ったり、添字圏という名前を使ってはいるが、$F$ は至って普通の関手である。任意の関手 $\mathcal{C}\rightarrow\mathcal{D}$ は $\mathcal{D}$ の中の $\mathcal{C}$ と同じ形の図式なのである。

例えば添字圏 $\mathcal{J}$ が対象が3つの
$$\xymatrix{ \bullet \ar[r] & \bullet & \bullet \ar[l] }$$
のような圏 であるとすると、関手 $F:\mathcal{J}\rightarrow\mathcal{C}$ は$\mathcal{C}$ の中の以下の形の図式と同一視することができる。
$$\xymatrix{ a \ar[r] & c & b \ar[l] }$$

特に重要なのは、関手 $\mathbf{1}\rightarrow\mathcal{C}$ は $\mathcal{C}$ の対象1つとみなす事ができるという事である。すなわち、**関手とは"対象"を一般化させた概念である** という事ができる。

- 圏の準同型としての関手
- 図式としての関手
- 対象の一般化としての関手

などの見方を状況によって使い分けられるようになると、様々な定理のイメージが掴みやすくなる。

### 関手の性質

関手 $F:\mathcal{C}\rightarrow\mathcal{D}$ によって $\mathcal{C}$ を $\mathcal{D}$ に移して $\mathcal{D}$ の中で $\mathcal{C}$ について調べるということがよく行われる。その為には、以下のような性質を持つ関手が重要となる。

{{% definition title="忠実・充満・本質的全射" %}}
関手 $F:\mathcal{C}\rightarrow\mathcal{D}$ について

- $F: \mathcal{C}(a,b)\rightarrow\mathcal{D}(F(a),F(b))$ が全ての$a,b\in\mathcal{C}$ について単射の時 $F$ は **忠実(faithful)** であるという。
- $F: \mathcal{C}(a,b)\rightarrow\mathcal{D}(F(a),F(b))$ が全ての$a,b\in\mathcal{C}$ について全射の時 $F$ は **充満(full)** であるという。
- 任意の$b\in\mathcal{D}$ についてある $a\in\mathcal{C}$ が存在して $F(a)\cong b$ となるとき $F$ は **本質的全射(essentially surjective)**  であるという。
{{% /definition %}}

本質的全射が全射と異なるのは $F(a)\cong b$ と $F(a)=b$ の違い。
同型な対象はその圏論的な性質によっては区別する事ができない為、 圏論では **同型な対象は実質的に1つの対象と見なす** ことが自然である。よって、対象の厳密な一致ではなく同型 $\cong$ を用いて定められた性質の方がより本質的な性質となる。

{{% proposition %}}
$F:\mathcal{C}\rightarrow\mathcal{D}$ が忠実であるならば、$F(f)$ がモノならば $f$ もモノ。同様に $F(f)$ がエピならば $f$ もエピ。
{{% /proposition %}}
{{% details 証明 %}}
$F(m): F(a)\rightarrow F(b)$ がモノであるとする。ここで、射 $f,g:c\rightarrow a$ について
$ m\circ f = m\circ g $ であるとすると、全体を $F$ で移して $ F(m)\circ F(f) = F(m)\circ F(g) $である。よって $F(m)$ がモノであるから $F(f)=F(g)$ であるので $F$ が忠実であることから $f=g$。従って $ m$ はモノである。エピについても同様。 $\square$
{{% /details %}}

{{% proposition label="prop.embedding" %}}
$F:\mathcal{C}\rightarrow\mathcal{D}$ が忠実充満であるならば、任意の $a,b\in\mathcal{C}$ について
$$ a\cong b \Leftrightarrow F(a)\cong F(b)$$
{{% /proposition %}}
{{% details 証明 %}}
$\Rightarrow$ は明らか。
$F(a)\cong F(b)$ であるとすると、同型射 $f: F(a)\rightarrow F(b), g:F(b)\rightarrow F(a)$ が存在する。
$F,G$ は充満だから $f=F(f'), g=F(g')$ となる $f':a\rightarrow b, g':b\rightarrow a$ が存在し
$$ g\circ f = 1\_{F(a)} \Rightarrow F(g')\circ F(f')=F(1_a) \Rightarrow F(g'\circ f')=F(1_a)$$
である。そして $F$ は忠実であるから $g'\circ f'=1_a$ である。同様にして $f'\circ g'=1_b$ であるから $f',g'$ は同型射。従って $a\cong b$ である。 $\square$
{{% /details %}}

## 自然変換

関手の間の準同型の事を **自然変換(natural transformation)** という。 {{< refer def.functor-as-a-diagram >}}で述べたように、対象を一般化したものが関手であるとすると、射を一般化したものが自然変換である。

### 自然変換・自然同型

{{% definition title="自然変換" %}}
関手 $F,G:\mathcal{C}\rightarrow\mathcal{D}$ に対して、$F$ から $G$ への**自然変換(natural transformation)** $\phi:F\rightarrow G$ とは、$\mathcal{D}$の射の族 $\\{\phi_a: F(a)\rightarrow G(a)\\}\_{a\in\mathcal{C}}$ であり、任意の $\mathcal{C}$ の射 $f:a\rightarrow b$ に対して、以下の図式が可換となるものである。 $\phi_a$ を $\phi$ の **$a$コンポーネント($a$-component)** という。

$$\xymatrix{
F(a) \ar[r]^{\phi_a} \ar[d]\_{F(f)} & G(a) \ar[d]^{G(f)} \\\\
F(b) \ar[r]^{\phi_b} & G(b)
}$$

$\phi_a$ が全て同型射であるとき $\phi$ を **自然同型(natural isomorphism)** もしくは **自然同値(natural equivalence)** という。また自然同型 $\phi:F\rightarrow G$ が存在する時 $F\cong G$ と書く。
{{% /definition %}}

複雑な定義に見えるが、関手を図式と思えばなんて事はなく、つまり $\mathcal{D}$ の中の $\mathcal{C}$ の形の図式 $F$ と図式 $G$ と対応する点を繋ぐ $\phi$ があったときに、全体が可換であるような物を自然変換というのである。すなわち、 diagram chasingをする際に、 $F,G,\phi$ の中をどのような順序で辿っても得られる射は同じになる。

{{< figure src="../images/natural-transformation.png" width="20%" >}}

関手 $F,G,H:\mathcal{C}\rightarrow\mathcal{D}$ の間に自然変換 $\phi:F\rightarrow G, \psi: G\rightarrow H$ が存在する時、下図の横の射をそれぞれ合成した射の族 $\\{\psi_a\circ\phi_a\\}$ は 自然変換 $F\rightarrow H$ となる。これを自然変換の合成といい $\psi\circ \phi$ と書く。

$$\xymatrix{
F(a) \ar[r]^{\phi_a} \ar[d]\_{F(f)} & G(a) \ar[r]^{\psi_a} \ar[d]^{G(f)} & H(a) \ar[d]^{H(f)} \\\\
F(b) \ar[r]^{\phi_b}                & G(b) \ar[r]^{\psi_b}               & H(b)
}$$

そうすると、関手を対象とし自然変換を射とする圏を定める事が出来る。

### 関手圏

{{% definition title="関手圏" %}}
圏 $\mathcal{C},\mathcal{D}$ について、関手 $\mathcal{C}\rightarrow \mathcal{D}$ を対象とし、それらの間の自然変換を射とする圏を **関手圏(functor category)** といい、 $\[\mathcal{C},\mathcal{D}\]$ や $\mathcal{D}^{\mathcal{C}}$ と書く。
{{% /definition %}}

{{% example title="$\mathcal{C}^\mathbf{0}, \mathcal{C}^\mathbf{1}$" %}}
$\mathbf{0}$ を空圏、$\mathbf{1}$ を対象が一つで恒等射のみの圏をすると、任意の圏 $\mathcal{C}$ について
$$ \mathcal{C}^\mathbf{0}\cong\mathbf{1},\quad\mathcal{C}^\mathbf{1}\cong\mathcal{C}$$

1つ目の等式は、空集合から任意の集合への関数が **空関数(empty function)** の唯一つしか存在しないことによる。2つ目は関手 $\mathbf{1}\rightarrow\mathcal{C}$ と $\mathcal{C}$ の対象が一対一に対応することから分かる。
{{% /example %}}

{{% example title="射圏" %}}
対象が2つで、恒等射と対象の間に射が一本あるような圏 $\mathbf{2}$ から圏 $\mathcal{C}$ への関手のなす圏 $\mathcal{C}^\mathbf{2}$ を **射圏(arrow category)** といい$\mathcal{C}^{\rightarrow}$ と書く。

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

{{% example title="前層の圏" %}}
関手圏 $\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}$ を **前層の圏(category of preshaves)** といい、 $\hat{\mathcal{C}}$ や $\mathbf{PSh}(\mathcal{C})$ と書く。
{{% /example %}}

{{% definition title="対角関手" %}}
$\mathcal{C}$ の対象 $a$ を、 定数関手 $a: \mathcal{J}\rightarrow\mathcal{C}$ に移し、射 $f$ を全てのコンポーネントが $f$ である自然変換に移す対応は関手
$$ \Delta: \mathcal{C}\rightarrow \mathcal{C}^{\mathcal{J}}$$
である。これを **対角関手(diagonal functor)** という。
{{% /definition %}}

### 圏の同型・同値

2つの圏 $\mathcal{C},\mathcal{D}$ が何らかの意味で同じであるという事を表す方法として、 **同型**、**圏同値** という異なる関係性がある。これらの違いをしっかり理解したいので、合わせてここで紹介する。

{{% definition title="圏の同型" %}}
圏 $\mathcal{C},\mathcal{D}$ が **同型(isomorphic)** であるとは関手 $F:\mathcal{C}\rightarrow\mathcal{D}$ と $G:\mathcal{D}\rightarrow\mathcal{C}$ で
$$ GF = 1\_{\mathcal{C}},\ FG=1\_{\mathcal{D}}$$
を満たすものが存在する事である。この時 $\mathcal{C}\cong\mathcal{D}$ と書く。
{{% /definition %}}

これは、本質的全射の所で述べたのと同じ理由で条件が強すぎて、同型な対象 $a\cong b$ は同じものと見なした上で圏が本質的に一致する条件を考えたい。
そこで、圏同値という概念が重要となる。

{{% definition title="圏の同値" %}}
圏 $\mathcal{C},\mathcal{D}$ が **同値(equivalent)** であるとは関手 $F:\mathcal{C}\rightarrow\mathcal{D}$ と $G:\mathcal{D}\rightarrow\mathcal{C}$ で自然同型
$$ GF \cong 1\_{\mathcal{C}},\ FG \cong 1\_{\mathcal{D}}$$
を満たすものが存在する事である。$F,G$ を **圏同値(equivalence of categories)** という。この時 $\mathcal{C}\simeq\mathcal{D}$ と書く。
{{% /definition %}}

例えば、$\mathcal{C}$ を対象が1つで、恒等射のみの圏、$\mathcal{D}$ を対象が2つであり、その2つの間に同型射がある圏とする。これらはそもそも対象の数、射の数が異なり同型ではないが、$\mathcal{D}$ の2つの対象は同型なのであるから実質対象が1つの圏と考える事ができる。実際、 $\mathcal{C}$ と $\mathcal{D}$ は圏同値になる。

$$\xymatrix{
\mathcal{C} & & \mathcal{D} \\\\
\bullet     & & a \ar@/^1pc/[d]^{f} \\\\
            & & b \ar@/^1pc/[u]^{f^{-1}}
}$$

もう少し実践的な例をあげると、実数値の数ベクトル空間 $\mathbb{R}^n\ (n=0,1,\ldots)$ を対象とし線形写像を射とする圏 $\mathcal{C}$と、有限次元の実数係数ベクトル空間と線形写像の圏 $\mathcal{D}$ は同型ではないが同値となる。

{{% proposition %}}
選択公理を仮定すると、関手 $F$ が圏同値であることと $F$ が充満忠実かつ本質的に全射であることは同値
{{% /proposition %}}

{{% details 証明 %}}
($\Rightarrow$)
$F:\mathcal{C}\rightarrow\mathcal{D}$ が圏同値、すなわち関手 $G:\mathcal{D}\rightarrow\mathcal{C}$ が存在して自然同型 $\phi: GF\rightarrow 1\_{\mathcal{C}}, \psi: FG\rightarrow 1\_{\mathcal{D}}$ が存在するとする。

任意の$b\in\mathcal{D}$ に対して $a=G(b)$ とおけば $F(a)=FG(b)\cong 1\_{\mathcal{D}}(b) = b$。従って $F$ は本質的全射。

任意の$f,g\in\mathcal{C}(a,b)$ について $F(f)=F(g)$ であるとすると $GF(f)=GF(g)$ であるから、$\phi_b\circ GF(f)\circ\phi_a^{-1} = f$ であることより $f = g$。従って$F:\mathcal{C}(a,b)\rightarrow\mathcal{D}(F(a),F(b))$ は単射であるから $F$ は忠実。

$$\xymatrix{
GF(a) \ar[d]\_{GF(f)} \ar@{<-}[r]^{\phi^{-1}_a} & a \ar[d]^{f} \\\\
GF(b) \ar[r]\_{\phi_b} & b \\\\
}$$

また、任意の $g:F(a)\rightarrow F(b)$ に対して $ f = \phi\_{b}\circ G(g)\circ \phi^{-1}\_{a} $とおくと、これを変形して $G(g) = \phi_b^{-1}\circ f\circ\phi_a = GF(f)$ となるが、 $F$ と同様にして $G$ も単射である事が分かるので $g=F(f)$ となる。よって $F:\mathcal{C}(a,b)\rightarrow\mathcal{D}(F(a),F(b))$ は全射であるから $F$ は充満である。$\square$

($\Leftarrow$)
$F:\mathcal{C}\rightarrow\mathcal{D}$ が充満忠実かつ本質的全射であるとする。

本質的全射であることより、任意の $b\in\mathcal{D}$ に対してある $a\in\mathcal{C}$ が存在して $F(a)\cong b$ となる。選択公理を用いてそのような $a$ を各 $b$ について選ぶ事によって、対象間の写像 $G:\mathrm{Ob}(\mathcal{D})\rightarrow\mathrm{Ob}(\mathcal{C})$ を作る事が出来る。また同型射の族 $\psi\_b: FG(b)\rightarrow b$が得られる。

続いて、射の対応 $G:\mathcal{D}(a,b)\rightarrow\mathcal{C}(a,b)$ を定める。任意の $\mathcal{D}$ の射 $f:a\rightarrow b$ に対して
$$ \psi\_b^{-1}\circ f\circ\psi\_a: FG(a)\rightarrow FG(b)$$
という射が得られるが、 $F$ が忠実充満であるので
$$ G(f) = F^{-1}(\psi\_b^{-1}\circ f\circ\psi\_a): G(a)\rightarrow G(b)$$
という対応を定める事ができる。

$G$ の関手性は明らか。$\psi$ の定義より $\psi\_b\circ FG(f)= f\circ\psi_a$ が成り立つので $\psi$ は自然変換であり、 $\psi\_a$ は全て同型射だから $\psi$ は自然同型。

あとは自然同型 $\phi: GF\rightarrow 1\_{\mathcal{C}}$ の存在を示せばよい。
$F$ が忠実充満であることより $\psi\_{F(a)}: FGF(a)\rightarrow F(a)$ に対応する $\mathcal{C}$ の射が一意に定まるので
$$ \phi\_{a} = F^{-1}(\psi\_{F(a)})$$ 
と定める。 この時、任意の$\mathcal{C}$ の射 $f:a\rightarrow b$ に対して $\psi$ が自然変換であることより
$$ F(f)\circ\psi\_{F(a)} = \psi\_{F(b)}\circ FGF(f)$$
であり、$F$ が忠実充満であることより $F^{-1}(p\circ q)=F^{-1}(p)\circ F^{-1}(q)$ であることに注意すると
$$ f\circ F^{-1}(\psi\_{F(a)}) = F^{-1}(\psi\_{F(b)})\circ GF(f)$$
すなわち $ f\circ\phi\_a = \phi\_b\circ GF(f)$ であるので $\phi$ は自然変換。また同様に $F^{-1}$ が射の合成関係を保つことに注意すると $\phi\_{F(a)}$ が同型射であることより $\phi\_a$ も同型射。よって $\phi$ も自然同型。 $\square$
{{% /details %}}

## 極限
集合論における直積や直和のような概念は圏論においては **普遍性(universal property)** と呼ばれる性質を用いた **普遍的構成(universal construction)** という方法を用いて定義することができる。 **極限(limit)** は普遍的構成の特別なものであるが、非常に広範な数学的概念に共通する抽象概念である。まずは具体例として終対象・始対象、積・余積を例にあげた後に極限の定義や性質を紹介する。

### 終対象・始対象

{{% definition title="終対象・始対象" %}}
圏 $\mathcal{C}$ の **終対象(terminal object)** とは、任意の対象 $x\in\mathcal{C}$ に対して射 $x\rightarrow 1$ が唯一つ存在するような対象 $1\in\mathcal{C}$ の事である。

$$\xymatrix{
x \ar@{.>}[r]^{\exists!} & 1
}$$

終対象の双対概念を **始対象(initial object)** という。すなわち、任意の対象 $x\in\mathcal{C}$ に対して射 $0\rightarrow x$ が唯一つ存在するような対象 $0\in\mathcal{C}$ の事である。

$$\xymatrix{
0 \ar@{.>}[r]^{\exists!} & x
}$$

これら唯一の射を $!$ や $!\_x$ などと書く。
{{% /definition %}}

例えば、$\mathbf{Set}$ における終対象は一点集合、始対象は空集合である。posetにおける終対象・始対象は、もし存在するならば、最大値・最小値である。

ここで注意したいのは、普遍性による概念の定義はある特定の対象や射を定めるものではないということである。例えば $\mathbf{Set}$ における終対象である一点集合は無数に存在し、その特定の1つを指定することはできない。しかし、以下の命題で示されるように終対象・始対象は **同型を除いて一意(unique up to isomorphism)** である。

{{% proposition %}}
始対象・終対象は同型を除いて一意に定まる。
{{% /proposition %}}

{{% details 証明 %}}
$0,0'\in\mathcal{C}$ が共に始対象 であるとする。下の図式の射 $0\rightarrow 0$ の一意性から $!\_0\circ !\_{0'}=1_0$ 。逆も同様なので、$!\_0,!\_{0'}$は同型射であり $0\cong 0'$。終対象についても同様。
$$\xymatrix{
0 \ar[r]\_{!\_{0'}} \ar@/^1pc/[rr]^{1_0} & 0' \ar[r]\_{!\_0} & 0
}$$
$\square$
{{% /details %}}

### 積・余積

集合 $A,B$ の直積 $A\times B$ および直和 $A\oplus B$ を圏論的に一般化した概念が **積(product)** と **余積(coproduct)** である。

{{% definition title="積" %}}
圏 $\mathcal{C}$ の対象 $a,b$ に対する **積(product)** とは、 $a\times b$ と書かれるある対象 $a\times b\in\mathcal{C}$ および射 $\pi_a: a\times b\rightarrow a, \pi_b: a\times b\rightarrow b$ の組であって、 任意の対象 $x$ と射 $f:x\rightarrow a, g:x\rightarrow b$ に対して、以下の図式が可換となるような射 $u: x\rightarrow a\times b$ が唯一つ存在するものである。

$$\xymatrix{
            & x \ar[ld]\_{f} \ar[rd]^{g} \ar@{.>}[d]^{\exists! u} &\\\\
a           & a\times b \ar[l]\_{\pi_a} \ar[r]^{\pi_b} & b
}$$
この $u$ を $\langle f, g\rangle$ とも書く。また、 $f:a\rightarrow b, g:c\rightarrow d$ に対して $a\times c, b\times d$ が存在するならば $u=\langle f\circ\pi_a, g\circ\pi_c\rangle$が存在するがこれを $f\times g$ と書く。
$$\xymatrix{
            & a\times c \ar[ld]\_{f\circ\pi_a} \ar[rd]^{g\circ\pi_c} \ar@{.>}[d]^{f\times g} &\\\\
b           & b\times d \ar[l]\_{\pi_c} \ar[r]^{\pi_d} & d
}$$
{{% /definition %}}

終対象と同様に積も同型を除いて一意となる事も示す事が出来る。これについては後に一般化して証明する。

{{% example %}}
$\mathbf{Set}$ における積は直積集合(もしくはそれと同型な集合)である。
{{% /example %}}
{{% details 証明 %}}
集合 $A,B$ の直積集合とは
$$ A\times B = \\{(a,b)\mid a\in A, b\in B\\}$$
である。ここで $\pi_A,\pi_B$ を
$$ \pi_A((a,b)) = a, \pi_B((a,b)) = b $$
で定めると、 $A\times B,\pi_A,\pi_B$、が積の定義を満たす事を示す。$X$ を任意の集合、 $f:X\rightarrow A, g:X\rightarrow B$ を任意の関数とする。すると $u:X\rightarrow A\times B$ として
$$ u(x) = (f(x), g(x)) $$
なる関数を取ることができる。これは$\pi_A\circ u = f, \pi_B\circ u=g$ を満たす。
ここで、他の関数 $v:X\rightarrow A\times B$ が$\pi_A\circ v=f, \pi_B\circ v=g$ を満たすとすると、関数 $v_A: X\rightarrow A, v_B: X\rightarrow B$ が存在して
$$ v(x) = (v_A(x), v_B(x))$$
と書けるが、この時 $\pi_A\circ v=f$ より $v_A(x)=f(x)$。これが任意の $x\in X$ について成立するから $v_A=f$。同様にして $v_B=g$。従って $v=u$ であるから、 積の図式の可換性を満たす $u$ は唯一つに定まる。以上より直積集合 $A\times B$ は積であり、積が同型を除いて一意であることから命題は示された。$\square$
{{% /details %}}

上記の例におけるカッコ書きに相当する言い回しは、省略しても圏論の語彙を用いた議論の範疇に於いては矛盾が生じないので今後は省略することにする。
直積以外には例えば、posetの要素 $a,b$ の積は、もし存在するならば$\\{a,b\\}$の下限となる。例えば

- 数値と大小関係からなるposet: $\min\\{a,b\\}$
- 集合と包含関係からなるposet: $a\cap b$

などである。他にも論理式を対象とし、証明を射とする圏を考える事ができるが、この圏においては$a \wedge $b が積となる。このように数学における様々な概念が積として表現される。

積の双対概念が余積である。

{{% definition title="余積" %}}
圏 $\mathcal{C}$ の対象 $a,b$ に対する **余積(coproduct)** とは、 $a+b$ と書かれるある対象 $a+b\in\mathcal{C}$ および射 $i_a: a\rightarrow a+b, i_b: b\rightarrow a+b$ の組であって、 任意の対象 $x$ と射 $f:a\rightarrow x, g:b\rightarrow x$ に対して、以下の図式が可換となるような射 $u: a+b\rightarrow x$ が唯一つ存在するものである。

$$\xymatrix{
            & x \ar@{<-}[ld]\_{f} \ar@{<-}[rd]^{g} \ar@{<.}[d]^{\exists! u} &\\\\
a           & a+b \ar@{<-}[l]\_{i_a} \ar@{<-}[r]^{i_b} & b
}$$
この $u$ を $[f, g]$ とも書く。また $f:a\rightarrow b, g:c\rightarrow d$ に対する $f+g: a+c\rightarrow b+d$ も積と同様に定義される。
{{% /definition %}}

{{% example %}}
$\mathbf{Set}$ における余積は直和集合である。
{{% /example %}}
{{% details 証明 %}}
集合 $A,B$ の直和集合
$$ A\oplus B = \\{(0,a)\mid a\in A\\}\cup\\{(1, b)\mid b\in B\\}$$
に対して
$$i_A(a) = (0,a), i_B(b)=(1,b)$$
とすると $A\oplus B, i_A, i_B$ が余積の定義を満たすことを示す。ここで $X$ を任意の集合、 $f: A\rightarrow X, g: B\rightarrow X$ を任意の関数とし、
$$ u((0, x)) = f(x), u((1, x)) = g(x)$$
と定めると、これは余積の図式の可換性 $u\circ i_A = f, u\circ i_B = g$ を満たす。$u$ の一意性は直積が積である事の証明と同様にできる。 $\square$
{{% /details %}}

先ほど、積の例としてあげた $\min\\{a,b\\}$, $a\cap b$, $a\wedge b$ の圏論的双対は $\max\\{a, b\\}$, $a\cup b$, $a\vee b$ であり、これらは直感的にも理解しやすいと思う。しかし、集合の直積と直和の間の双対性は、集合論的な定義においてはなかなか認識し難い関係であり面白い。但し、集合の直和以外の直和概念一般には言えないので注意。例えば環の直和は余積ではなく、積となる。

### 極限

終対象・始対象、積・余積を抽象化した概念が **極限(limit)** である。これがどのようなものか理解するために、具体例として積について考える。積の図式は少し書き直してみると以下のように書くことができるが、この点線で囲まれた $a\xleftarrow{f} x \xrightarrow{g} b$ という形の図式を対象とする圏を考える事が出来る。
そして、$u:x\rightarrow a\times b$ がただ一つ存在するという事は、対象 $a\xleftarrow{\pi_a} a\times b\xrightarrow{\pi_b}b$ がその圏の終対象であることとして表現する事が出来る。

$$\xymatrix{
a \ar[d]^{1_a} & x \ar[l]\_{f} \ar[r]^{g} \ar@{.>}[d]^{\exists! u} & b \ar[d]^{1_b}\\\\
a            & a\times b \ar[l]\_{\pi_a} \ar[r]^{\pi_b}            & b
\ar@{.}(-5,7);(47,7)
\ar@{.}(47,7);(47,-5)
\ar@{.}(47,-5);(-5,-5)
\ar@{.}(-5,-5);(-5,7)
\ar@{.}(-5,-13);(47,-13)
\ar@{.}(47,-13);(47,-25)
\ar@{.}(47,-25);(-5,-25)
\ar@{.}(-5,-25);(-5,-13)
}$$

後ほど定義を行うが、このような対象を **錐(cone)** という。この場合は $a,b$ が底で$x$が頂点であるような錐である。
以下のように立てて描いてみるとイメージが湧きやすいかもしれない。

{{% tikz %}}
  \begin{tikzpicture}
    \coordinate (p) at (-0.5, 1.5) node at (p) [above] {$a\times b$};
    \coordinate (x) at (1.5, 1.5) node at (x) [above] {$x$};
    \coordinate (a) at (-1, -1) node at (a) [below] {$a$};
    \coordinate (b) at (1, -1) node at (b) [below] {$b$};
    \draw [-latex] (x) to node [pos=0.25, left] {\small $f$} (a);
    \draw [-latex] (x) to node [pos=0.25, right] {\small $g$} (b);
    \draw [-latex, thick] (p) to node [pos=0.25, left] {\small $\pi_a$} (a);
    \draw [-latex, thick] (p) to node [pos=0.25, right] {\small $\pi_b$} (b);
    \draw [-latex, dotted] (x) to node [above] {\small $u$} (p);
  \end{tikzpicture}
{{% /tikz %}}

より一般には、下図のように底面の頂点が複数あり、その間に射があるようなものを錐として考える事で、様々な概念を統一的に議論できるというわけである。

{{% tikz %}}
  \begin{tikzpicture}
    \coordinate (x) at (0, 2.5) node at (x) [above] {$x$};
    \coordinate (a) at (-1, -1);
    \coordinate (b) at (1, -1);
    \coordinate (c) at (1.5, 0);
    \coordinate (d) at (0, 1);
    \coordinate (e) at (-1.3, 0.2);
    \draw [-latex, thick] (x) to (a);
    \draw [-latex, thick] (x) to (b);
    \draw [-latex] (x) to (c);
    \draw [-latex] (x) to (d);
    \draw [-latex] (x) to (e);
    \draw [-latex, thick] (a) to (b);
    \draw (b) to (c);
    \draw (c) to (d);
    \draw (d) to (e);
    \draw (e) to (a);
  \end{tikzpicture}
{{% /tikz %}}

では錐と錐の圏の定義を進める。 {{< refer def.functor-as-a-diagram >}} で説明したように、錐の底面はその形を表す添字圏  $\mathcal{J}$ からの関手 $F: \mathcal{J}\rightarrow\mathcal{C}$ で表す事ができる。そして、底面の各頂点に対して $x$ から射が生えているというのが一般的な錐の定義であるが、対象と射より関手と自然変換によって物事を説明した方が使い勝手が良い為、ここでは別の定義を行おうと思う。その為には、下図の用に頂点 $x$ を底面と同じ形に開いてしまおう。

{{% tikz %}}
  \begin{tikzpicture}
    \coordinate (xa) at (-1, 1.5) node at (xa) [left] {$x$};
    \coordinate (xb) at (1, 1.5) node at (xb) [right] {$x$};
    \coordinate (xc) at (1.5, 2.5);
    \coordinate (xd) at (0, 3.5);
    \coordinate (xe) at (-1.3, 2.7);
    \coordinate (a)  at (-1, -1) node at (a) [below] {$F(a)$};
    \coordinate (b)  at (1, -1) node at (b) [below] {$F(b)$};
    \coordinate (c)  at (1.5, 0);
    \coordinate (d)  at (0, 1);
    \coordinate (e)  at (-1.3, 0.2);
    \draw [-latex, thick] (xa) to (a);
    \draw [-latex, thick] (xb) to (b);
    \draw [-latex] (xc) to (c);
    \draw [-latex] (xd) to (d);
    \draw [-latex] (xe) to (e);
    \draw [-latex, thick] (a) to node [below] {$F(f)$} (b);
    \draw (b) to (c);
    \draw (c) to (d);
    \draw (d) to (e);
    \draw (e) to (a);
    \draw [-latex, thick] (xa) to node [pos=0.4,above] {$1_x$} (xb);
    \draw (xb) to (xc);
    \draw (xc) to (xd);
    \draw (xd) to (xe);
    \draw (xe) to (xa);
  \end{tikzpicture}
{{% /tikz %}}

このように展開してみると、上面を形が $\mathcal{J}$ の定数関手 $x$ で表せる事がわかる。すると、錐とは上面 $x$ から底面 $F$ への自然変換であるとして表す事ができる。また、この双対版として底面から上面への錐も考える事ができる。

{{% definition title="錐" %}}
図式 $F:\mathcal{J}\rightarrow\mathcal{C}$ と対象 $x\in\mathcal{C}$ について、自然変換 $\phi:x\rightarrow F$ を **$x$ から $F$ への 錐(cone)** という。
同様に、自然変換 $\phi:F\rightarrow x$ を **$F$ から $x$ への錐** もしくは **余錐(cocone)** という。

(ここでは $x$ という記号を対象 $x\in \mathcal{C}$ と定数関手 $x:\mathcal{J}\rightarrow\mathcal{C}$ の両方に用いているが、混乱の恐れがある場合には対角関手を用いて
$\phi:\Delta(x)\rightarrow F$ と表せばよい。)
{{% /definition %}}

そして、錐の頂点の間の射によって、錐から錐への射を定義する事で錐の圏が出来上がる。

{{% definition title="錐の圏" %}}
図式 $F:\mathcal{J}\rightarrow\mathcal{C}$ への錐を対象とし、2つの錐
$\phi:x\rightarrow F$ と $\psi:y\rightarrow F$ の間の射を、以下が可換となるような自然変換 $f:x\rightarrow y$ (これは射 $f:x\rightarrow y$ と同一) によって定めると圏となる。これを **$F$ への錐の圏(category of cones to $F$)** という。
$$\xymatrix{
x \ar[r]^f \ar[d]\_{\phi} & y \ar[ld]^{\psi} \\\\
F & \\\\
}$$

この双対概念を **$F$ からの錐の圏(category of cones from $F$)** という。
{{% /definition %}}

この圏のイメージは以下のようになる。すなわち $x$ から $F$ への錐を $f:x\rightarrow y$ と $y$ から $F$ への錐に分解できるという状況を錐の間に射 $f$ が存在すると定めるのである。

{{% tikz %}}
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
{{% /tikz %}}

{{% definition title="極限" %}}
$F:\mathcal{J}\rightarrow\mathcal{C}$ への錐の圏の終対象の頂点を $\varprojlim F$ と書き、錐 $\phi:\varprojlim F\rightarrow F$ を$F$の **極限(limit)** もしくは **射影的極限(projective limit)** という。また $\phi$ を **標準射影(canonical projection)** という。

$F:\mathcal{J}\rightarrow\mathcal{C}$ からの錐の圏の始対象の頂点を $\varinjlim F$ と書き、 $\psi: F\rightarrow \varinjlim F$ を$F$の **余極限(colimit)** もしくは **帰納的極限(inductive limit)** という。また $\psi$ を **標準入射(canonical inclusion)** という。

$\displaystyle\varprojlim F,\displaystyle\varinjlim F$ の代わりに、$\displaystyle \varprojlim\_{i\in\mathcal{J}}F(i),\displaystyle \varinjlim\_{i\in\mathcal{J}}F(i)$ とも書く。
{{% /definition %}}

極限は終対象であるから、同型を除いて一意に定まる。余極限も同様。

上の定義のように、極限とは条件を満たす"錐"(極限錐という)の事であるが、極限錐の頂点の事をさして極限という場合もある。しかし、同型な極限錐の頂点同士も同型であるし、逆に $a\cong b$ で $a$ が極限錐の頂点であるならば、 $b$ もそれと同型な極限錐の頂点となる事が簡単に示せるので、用語の濫用は実用上は問題とならない。

### 極限の例

既に紹介した終対象・始対象、積・余積も極限・余極限の例である。まず $\mathcal{J}$ として空圏(対象も射も空集合の圏)をとった極限が終対象、余極限が始対象である。そして、積・余積は次のように一般化できる。

{{% definition title="積・余積" %}}
$\mathcal{J}$ が離散圏の時の極限を **積(product)** 、余極限を **余積(coproduct)** という。関手 $\mathcal{J}\rightarrow\mathcal{C}$ は $\mathcal{C}$ の対象の集合 $\\{a_i\\}\_{i\in\mathcal{J}}$ と同一視できるので、このとき積・余積を次のように書く。
$$ \prod\_{i\in\mathcal{J}} a_i,\quad\coprod\_{i\in\mathcal{J}} a_i$$
$\mathcal{J}$ が有限集合の時は **有限積(finite product)**、**有限余積(finite coproduct)** ともいい、 
$$ a_1\times a_2\times\cdots a_n,\quad a_1+a_2+\cdots+a_n$$
のようにも書く。
{{% /definition %}}

{{% definition title="イコライザ・コイコライザ" %}}
$\mathcal{J}$ が $\bullet\rightrightarrows\bullet$ という形の時の極限を **イコライザ(equalizer)**、余極限を **コイコライザ(coequalizer)** という。並行射 $f,g$ についてのイコライザを $\mathrm{eq}(f,g)$、コイコライザを $\mathrm{coeq}(f,g)$ と書く。

$$ \xymatrix {
\mathrm{eq}(f, g) \ar[r] & a \ar@<+2pt>[r]^{f} \ar@<-2pt>[r]\_{g} & b && a \ar@<+2pt>[r]^{f} \ar@<-2pt>[r]\_{g} & b \ar[r] & \mathrm{coeq}(f,g)
}$$
{{% /definition %}}

{{% definition title="引き戻し・押し出し" %}}
$\mathcal{J}$ が $\bullet\rightarrow\bullet\leftarrow\bullet$ という形の時の極限を **引き戻し(pullback)** という。
図式が $a\rightarrow c\leftarrow b$ であるときの引き戻しを$ a\times\_{c} b $ と書く。

同様に、$\bullet\leftarrow\bullet\rightarrow\bullet$ という形の時の余極限を **押し出し(pushout)** といい、図式が $a\leftarrow c\rightarrow b$ であるときの押し出しを $ a+\_{c} b $ と書く。

$$ \xymatrix {
a\times\_{c} b \ar[r] \ar[d] & b \ar[d] && a+\_{c} b & b \ar[l]  \\\\
a \ar[r]                     & c        && a \ar[u]  & c \ar[l] \ar[u]
}$$
{{% /definition %}}

引き戻しは、後ほど初等トポスを定義する際に重要な道具となる。そこで再びその特徴について掘り下げて説明する。

#### $\mathbf{Set}$ における極限

$\mathbf{Set}$ は任意の(小さい)極限や余極限が存在するという良い性質を持っている。
まず

- 終対象は一点集合、始対象は空集合
- 積は直積集合、余積は直和集合

である。関数 $f,g: A\rightarrow B$ が与えられた時のイコライザは
$$\mathrm{eq}(f,g) = \\{x\in A\mid f(x)=g(x)\\}$$
すなわち、 $f=g$ の解集合である。コイコライザは $f(x)\sim g(x)\ (\forall x\in B)$ となるような最小の同値関係 $\sim$ による $B$ の商集合
$$\mathrm{coeq}(f,g)= B/{\sim}$$
である。例えば $f,g:\mathbb{N}\rightarrow\mathbb{N}$ が $f(n) = n, g(n) = n + 2$ の場合は
$$ 0 \sim 2 \sim 4 \cdots,\quad 1\sim 3\sim 5\cdots $$
であるような最小の同値関係(すなわち $n$ の偶奇の一致)で$\mathbb{N}$を割ったものであり $ \mathrm{coeq}(f,g) = \\{0,1\\}$ となる。

$A\xrightarrow{f}C\xleftarrow{g}B$ の引き戻しは
$$A\times\_C B=\\{(x,y) \in A\times B \mid f(x)=g(y) \\}$$
である。引き戻しは関数の **逆像(inverse image)の一般化** であると考えることもできる。例えば、写像 $f:A\rightarrow B$ と $B$ の部分集合 $C\subseteq B$ に対して
以下は引き戻しの図式となる。

$$\xymatrix{
f^{-1}(C) \ar[r] \ar@{^{(}->}[d] & C \ar@{^{(}->}[d] \\\\
A \ar[r]^f & B
}$$


$A\xleftarrow{f}C\xrightarrow{g}B$ の押し出しは $(0,f(x))\sim(1,g(x))\ (\forall x\in C)$ となるような最小の同値関係 $\sim$ による $A+B$ の商集合
$$ A+\_C B = (A+B)/{\sim}$$
である。

### 完備性

前節のように $\mathbf{Set}$ は任意の(小さい)極限や余極限が存在するという良い性質を持っている。このような圏の性質を **完備性(completeness)** という。

{{% definition title="完備性" %}}
圏 $\mathcal{C}$ が任意の小さな圏 $J$ について、任意の図式 $\mathcal{J}\rightarrow\mathcal{C}$ の極限を持つならば $\mathcal{C}$ は **完備(complete)** であるという。余極限を持つならば **余完備(cocomplete)** であるという。また、完備かつ余完備であることを **双完備(bicomplete)** という。

また、任意の有限の圏(対象の集合、射の集合が共に有限集合である圏)$J$ について、極限を持つならば **有限完備(finite complete)**、余極限を持つならば **有限余完備(finite cocomplete)** という。
{{% /definition %}}

任意の極限を持つことを直接証明するのは難しいが、以下の定理より、積とイコライザもしくは余積とコイコライザを持つ事のみ示せば十分である。

{{% theorem title="極限の存在定理" label="th.existence-of-limits" %}}
$\mathcal{C}$ が任意の並行射に対するイコライザと、圏 $\mathcal{J}$ の対象や射で添字付けられた任意の積を持つとする。この時、図式 $F:\mathcal{J}\rightarrow\mathcal{C}$ の極限は
$$ s, t: \prod\_{i\in\mathcal{J}}F(i)\rightrightarrows\prod\_{f: i\rightarrow j\in\mathcal{J}}F(j) $$

$$ \begin{align*}
s &= (F(f)\circ \pi_i)\_{f:i\rightarrow j\in\mathcal{J}} \\\\
t &= (\pi_j)\_{f:i\rightarrow j\in\mathcal{J}}
\end{align*}$$
のイコライザである。ここで、$\pi_k:\prod\_{i\in\mathcal{J}}F(i)\rightarrow F(k)$ は積の標準射影。

双対をとれば、余極限をコイコライザと余積によって表現する定理も同様に得られる。
{{% /theorem %}}

{{% details 証明の概要 %}}
$x\in\mathcal{C}$ と射 $\phi:x\rightarrow\prod\_{i\in\mathcal{J}}F(i)$ について以下の図式が可換であるとする。
$$ x\xrightarrow{\phi} \prod\_{i\in\mathcal{J}}F(i)\overset{s}{\underset{t}{\rightrightarrows}}\prod\_{f: i\rightarrow j\in\mathcal{J}}F(j) $$

$$\xymatrix{
x \ar[r]^{\phi} & \prod\_{i\in\mathcal{J}}F(i) \ar@<2pt>[r]^s \ar@<-2pt>[r]_t & \prod\_{f: i\rightarrow j\in\mathcal{J}}F(j) 
}$$

$\phi=(\phi_i)\_{i\in\mathcal{J}}$ とおくと、これは全ての $\mathcal{J}$ の射 $f:i\rightarrow j$ に対して、$j\in\mathcal{J}, F(f)\circ \phi_i = \phi_j$ であること、すなわち以下の図式が可換であることと同値。
$$\xymatrix{
x \ar[d]\_{\phi_i} \ar[rd]^{\phi_j} \\\\
F(i) \ar[r]_{F(f)} & F(j)
}$$
すなわち、射の族 $\\{\phi\_i\\}\_{i\in\mathcal{J}}$ は自然変換 $x\rightarrow F$ すなわち $F$ への錐に他ならない。
従って、この図式に対するイコライザは $x$ から $F$ への錐の圏の終対象、すなわち$F$ の極限と一致する。$\square$
{{% /details %}}

{{% proposition %}}
$\mathbf{Set}$ は双完備である。
{{% /proposition %}}

### 連続性

{{% definition title="連続関手" %}}
関手 $F: \mathcal{C}\rightarrow\mathcal{D}$ について、
$\mathcal{J}$ を小圏として任意の関手 $G:\mathcal{J}\rightarrow\mathcal{C}$ が極限を持つ時、
$F\circ G: \mathcal{J}\rightarrow\mathcal{D}$ も極限を持ち
$$F(\varprojlim G) \cong \varprojlim F\circ G$$
が成立するならば、$F$ は **連続(continuous)** であるという。
同様に $F$ が小さな余極限を保つ時は **余連続(cocontinuous)** であるという。
{{% /definition %}}

### 関手圏の極限

{{% theorem title="関手圏の極限の点別計算定理" label="th.limits-of-functor-categories" %}}
図式 $F:\mathcal{J}\rightarrow\mathcal{D}^{\mathcal{C}}$ について
$a\in \mathcal{C}$ に固定した関手 $F\_{(-)}(a):\mathcal{J}\rightarrow\mathcal{D} $ の極限 $\displaystyle\varprojlim\_{i\in\mathcal{J}} F\_i(a)$ が全ての $a\in\mathcal{C}$ について存在するならば、$F$ の極限も存在し

$$ \left(\varprojlim\_{i\in\mathcal{J}} F\_i\right)(a) \cong \varprojlim\_{i\in\mathcal{J}} F\_i(a) $$

である。余極限についても同様。
{{% /theorem %}}

これは、下図赤線で囲った部分のように、各対象ごとに個別に極限を求めたものが、関手圏の極限と一致するという定理である。

$$\xymatrix{
\varprojlim\_{i\in\mathcal{J}}F\_i(a) \ar[d] \ar[r] & \varprojlim\_{i\in\mathcal{J}} F\_i(b) \ar[r] \ar[d] & \varprojlim\_{i\in\mathcal{J}} F\_i(c) \ar[d] & =\quad \varprojlim\_{i\in\mathcal{J}}F\_i \\\\
F\_i(a) \ar[d] \ar[r] & F\_i(b) \ar[r] \ar[d] & F\_i(c) \ar[d] & \\\\
F\_j(a)        \ar[r] & F\_j(b) \ar[r]        & F\_j(c)        &
\ar@{.}(-15,7);(95,7)
\ar@{.}(95,7);(95,-7)
\ar@{.}(95,-7);(-15,-7)
\ar@{.}(-15,-7);(-15,7)
\ar@{.}(-15,-15);(95,-15)
\ar@{.}(95,-15);(95,-28)
\ar@{.}(95,-28);(-15,-28)
\ar@{.}(-15,-28);(-15,-15)
\ar@{.}(-15,-37);(95,-37)
\ar@{.}(95,-37);(95,-50)
\ar@{.}(95,-50);(-15,-50)
\ar@{.}(-15,-50);(-15,-37)
\ar@\[red\]@{.}(-17,9);(15,9)
\ar@\[red\]@{.}(15,9);(15,-52)
\ar@\[red\]@{.}(15,-52);(-17,-52)
\ar@\[red\]@{.}(-17,-52);(-17,9)
}$$

{{% details 証明 %}}

全ての $a\in\mathcal{C}$ について $\varprojlim\_{i\in\mathcal{J}} F\_i(a)$ が存在するとする。
$\mathcal{J}$ の射 $f: i\rightarrow j$ に対応する自然変換 $F\_f:F\_i\rightarrow F\_j$ を $\mathcal{C}$ の射 $u: a\rightarrow b$ についてcomponent-wiseに描くと以下のようになり、これが全ての $f:i\rightarrow j$ と $u:a\rightarrow b$ について可換となる。

$$ \xymatrix{
F\_i(a) \ar[d]\_{F\_f(a)} \ar[r]^{F\_i(u)}  & F\_i(b) \ar[d]^{F\_f(b)} \\\\
F\_j(a)                  \ar[r]\_{F\_j(u)} & F\_j(b)
}$$

ここで $\varprojlim\_{i\in\mathcal{J}} F\_i(a)$ が存在するので、下図のような極限錐がそれぞれ存在する。

$$ \xymatrix{
\varprojlim\_{i\in\mathcal{J}}F\_i(a) \ar[rd] \ar@/_1pc/[rdd] &&& \varprojlim\_{i\in\mathcal{J}}F\_i(b) \ar[ld] \ar@/^1pc/[ldd] \\\\
& F\_i(a) \ar[d]\_{F\_f(a)} \ar[r]^{F\_i(u)} & F\_i(b) \ar[d]^{F\_f(b)}& \\\\
& F\_j(a)                  \ar[r]\_{F\_j(u)} & F\_j(b)                &
}$$

ここで $\varprojlim\_{i\in\mathcal{J}}F\_i(a)$ の錐の側面に各 $F\_i(u)$ (図の水平の射) を合成したものは $F(-)(b):\mathcal{J}\rightarrow\mathcal{D}$ への錐となるので、下図が可換となる射 $\bar{u}: \varprojlim\_{i\in\mathcal{J}}F\_i(a)\rightarrow\varprojlim\_{i\in\mathcal{J}}F\_i(b)$ が唯一つ存在。

$$ \xymatrix{
\varprojlim\_{i\in\mathcal{J}}F\_i(a) \ar[rd] \ar@/_1pc/[rdd] \ar@{.>}[rrr]^{\bar{u}} &&& \varprojlim\_{i\in\mathcal{J}}F\_i(b) \ar[ld] \ar@/^1pc/[ldd] \\\\
& F\_i(a) \ar[d]\_{F\_f(a)} \ar[r]^{F\_i(u)} & F\_i(b) \ar[d]^{F\_f(b)}& \\\\
& F\_j(a)                  \ar[r]\_{F\_j(u)} & F\_j(b)                &
}$$

そこで、$\mathcal{C}$ の各対象 $a$ に $\varprojlim\_{i\in\mathcal{J}}F\_i(a)$ を、射 $u:a\rightarrow b$ に $\bar{u}$ を対応させる関係を考えるとこれは関手 $G: \mathcal{C}\rightarrow\mathcal{D}$ となる。これが $\varprojlim\_{i\in\mathcal{J}}F\_i$ である事を示す。

そこで任意の $H:\mathcal{C}\rightarrow\mathcal{D}$ から $F$ への錐を考える。
$$ \xymatrix{
\varprojlim\_{i\in\mathcal{J}}F\_i(a) \ar[rd] \ar@/_1pc/[rdd] \ar@{.>}[rrr]^{\bar{u}} &&& \varprojlim\_{i\in\mathcal{J}}F\_i(b) \ar[ld] \ar@/^1pc/[ldd] \\\\
& F\_i(a) \ar[d]\_{F\_f(a)} \ar[r]^{F\_i(u)} & F\_i(b) \ar[d]^{F\_f(b)}& \\\\
& F\_j(a)                  \ar[r]\_{F\_j(u)} & F\_j(b)                & \\\\
H(a) \ar[ru] \ar@/^1pc/[ruu] \ar[rrr]^{H(u)} &&& H(b) \ar[lu] \ar@/_1pc/[luu]
}$$

この左側だけに注目すると $\varprojlim_{i\in\mathcal{J}}$ についての普遍性より以下を可換にする射 $H(a)\rightarrow\varprojlim_{i\in\mathcal{J}}F\_i(a)$ が一意に存在。右側も同様。

$$ \xymatrix{
\varprojlim\_{i\in\mathcal{J}}F\_i(a) \ar[rd] \ar@/_1pc/[rdd] \ar@{.>}[rrr]^{\bar{u}} &&& \varprojlim\_{i\in\mathcal{J}}F\_i(b) \ar[ld] \ar@/^1pc/[ldd] \\\\
& F\_i(a) \ar[d]\_{F\_f(a)} \ar[r]^{F\_i(u)} & F\_i(b) \ar[d]^{F\_f(b)}& \\\\
& F\_j(a)                  \ar[r]\_{F\_j(u)} & F\_j(b)                & \\\\
H(a) \ar[ru] \ar@/^1pc/[ruu] \ar@{.>}[uuu] \ar[rrr]^{H(u)} &&& H(b) \ar[lu] \ar@/_1pc/[luu] \ar@{.>}[uuu]
}$$

この射の族 $\left\\{H(a)\rightarrow\varprojlim_{i\in\mathcal{J}}F\_i(a)\right\\}$ は自然変換 $H\rightarrow G$ となり、これが一意であるので $G\cong \varprojlim\_{i\in\mathcal{J}}F\_i$ である。$\square$
{{% /details %}}
