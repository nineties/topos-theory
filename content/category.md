---
title: 圏論
weight: 3
section: 2
toc: true
---

## 圏論の概要

**圏論(category theory)** は、1942-45年にSamuel EilenbergとSaunders Mac Laneによって代数的位相幾何学の研究の中で発明された数学の一分野であり、数学的概念を表現し議論するための抽象的な言語を提供する。
圏論の諸概念は、それらの例を数学のあらゆる分野で見つけることができる。
圏論に通底する哲学は、集合論を構成する **集合と帰属関係** という原始的な概念を、集合と関数の概念を抽象化した、 **対象と射** という概念に置き換えることである。
さらに言えば、それらを更に抽象化した **関手と自然変換** という概念に置き換えることである。

圏論が発明されて以来、そのアプローチは数学者が各々の主題を捉える方法に深いパラダイムシフトをもたらし、以前ではほとんど不可能だった重要な発見への道を開いた。
圏論の大きな成果の一つがトポス理論であり、これは全面的に圏論の言語で書かれた理論である。

## 圏

最初に、圏の定義を行う。冒頭で述べたように、圏とは集合と関数の概念を抽象化した **対象と射** からなり、関数の合成を抽象化した演算を持つものである。集合と関数全体、ベクトル空間と線形写像全体、群と群準同型写像全体など様々なものを圏と見なすことができる。

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

以上にように、圏とは対象と射によって定められるものであるが、対象と射は定義を満たすものであればどのようなものであっても構わない。

例えば、以下のような数学的対象とその間の準同型写像を射とする圏が様々存在する。
これらの圏は全て局所小圏である。また、いずれも対象の類は集合ではない。

- $\mathbf{Set}$: **集合**と**写像**
- $\mathbf{Top}$: **位相空間**と**連続写像**
- $\mathbf{Grp}$: **群** と **群の準同型写像**
- $\mathbf{Rng}$: **環** と **環の準同型写像**
- $\mathbf{Mod}_R$: **R加群** と **加群の準同型写像**
- $\mathbf{Vect}\_{K}$: **体 $K$ 上のベクトル空間** と **線型写像**

小圏には例えば以下のようなものがある。

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
$$ a\simeq b $$
と書く。
{{% /definition %}}
{{% proposition %}}
$f: a\rightarrow b$ が同型射の時、その逆射は一意に定まる。
{{% /proposition %}}
{{% details 証明 %}}
$f: a\rightarrow b$ が同型射であるとし $g,h:b\rightarrow a$ は共に逆射 であるとすると $ g = g\circ 1_b = g\circ f\circ h = 1_a\circ h = h $ $\square$
{{% /details %}}

簡単に示せるように同型関係は同値関係である。

圏から新しい圏を作る様々な操作が可能である。最も基本的な構成として積圏がある。これは集合の直積を一般化したようなものである。(実際 $\mathcal{C},\mathcal{D}$ が離散圏なら $\mathcal{C}\times\mathcal{D}$ はその直積集合となる。)

{{% definition title="積圏" %}}
圏 $\mathcal{C},\mathcal{D}$ に対して $\mathcal{C},\mathcal{D}$ の対象の組 $(a,b)$ を対象とし、射の組 $(f,g)$ を射とする圏を **積圏(product category)** といい $\mathcal{C}\times\mathcal{D}$ 書く。射の合成は要素毎に行う。
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

関手は様々な代数系における **準同型写像(homomorphism)** と同じものである。圏の代数系としての構造を定める恒等射、合成関係を保つ写像となっている。


恒等写像であるような関手 $F$ を **恒等関手(identity functor)** といい $1\_\mathcal{C}:\mathcal{C}\rightarrow\mathcal{C}$ や $\mathrm{id}\_{\mathcal{C}}$ と書く。
また、関手 $F:\mathcal{C}\rightarrow\mathcal{D}, G:\mathcal{D}\rightarrow\mathcal{E}$ に対して対象・射共に通常の関数合成を行うと$\mathcal{C}$ から $\mathcal{E}$ への関手が得られる。これを関手の合成といい $G\circ F:\mathcal{C}\rightarrow\mathcal{E}$ と書く。 $\circ$ を省略して $GF$ と書くこともある。すると、以下のような圏を構成できる事が分かる。

{{% definition title="小圏のなす圏" %}}
小圏を対象、関手を射とすると(大きな)圏となる。これを $\mathbf{Cat}$ と書く。
{{% /definition %}}

射の向きが逆になるような対応を反変関手という。後ほど登場するが、反変関手 $\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ の事を **前層(presheaf)** といい、特に重要である。

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

特に重要なのは、関手 $\mathbf{1}\rightarrow\mathcal{C}$ は $\mathcal{C}$ の対象1つとみなす事ができるという事である。すなわち、関手の特別な場合として対象が含まれる訳であるから、**関手とは"対象"を一般化させた概念である** という事ができる。同様に、後ほど関手と関手の間の準同型である **自然変換(natural transformation)** という概念が出てくるが、これは射を一般化させた概念であると言える。すなわち、 **"対象と射"を一般化させた概念が"関手と自然変換"である** という見方ができる。

準同型としての関手、図式としての関手、対象の一般化としての関手などの見方を状況によって使い分けられるようになると、様々な定理のイメージが掴みやすくなる。

### 関手の性質

関手 $F:\mathcal{C}\rightarrow\mathcal{D}$ によって $\mathcal{C}$ を $\mathcal{D}$ に移して $\mathcal{D}$ の中で $\mathcal{C}$ について調べるということがよく行われる。その為には、以下のような性質を持つ関手が重要となる。

{{% definition title="忠実・充満・本質的全射" %}}
関手 $F:\mathcal{C}\rightarrow\mathcal{D}$ について

- $F: \mathcal{C}(a,b)\rightarrow\mathcal{D}(F(a),F(b))$ が全ての$a,b\in\mathcal{C}$ について単射の時 $F$ は **忠実(faithful)** であるという。
- $F: \mathcal{C}(a,b)\rightarrow\mathcal{D}(F(a),F(b))$ が全ての$a,b\in\mathcal{C}$ について全射の時 $F$ は **充満(full)** であるという。
- 任意の$b\in\mathcal{D}$ についてある $a\in\mathcal{C}$ が存在して $F(a)\simeq b$ となるとき $F$ は **本質的全射(essentially surjective)**  であるという。
{{% /definition %}}

本質的全射が全射と異なるのは $F(a)\simeq b$ と $F(a)=b$ の違い。
圏論では、同型な対象はその圏論的な性質によっては区別する事ができず、実質的に1つの対象と見なすことが自然である。よって、対象の厳密な一致ではなく同型 $\simeq$ を用いて定められた性質の方がより本質的な性質となる。

{{% proposition %}}
$F:\mathcal{C}\rightarrow\mathcal{D}$ が忠実であるならば、$F(f)$ がモノならば $f$ もモノ。同様に $F(f)$ がエピならば $f$ もエピ。
{{% /proposition %}}
{{% details 証明 %}}
$F(m): F(a)\rightarrow F(b)$ がモノであるとする。ここで、射 $f,g:c\rightarrow a$ について
$ m\circ f = m\circ g $ であるとすると、全体を $F$ で移して $ F(m)\circ F(f) = F(m)\circ F(g) $である。よって $F(m)$ がモノであるから $F(f)=F(g)$ であるので $F$ が忠実であることから $f=g$。従って $ m$ はモノである。エピについても同様。 $\square$
{{% /details %}}

{{% proposition label="prop.embedding" %}}
$F:\mathcal{C}\rightarrow\mathcal{D}$ が忠実充満であるならば、任意の $a,b\in\mathcal{C}$ について
$$ a\simeq b \Leftrightarrow F(a)\simeq F(b)$$
{{% /proposition %}}
{{% details 証明 %}}
$\Rightarrow$ は明らか。
$F(a)\simeq F(b)$ であるとすると、同型射 $f: F(a)\rightarrow F(b), g:F(b)\rightarrow F(a)$ が存在する。
$F,G$ は充満だから $f=F(f'), g=F(g')$ となる $f':a\rightarrow b, g':b\rightarrow a$ が存在し
$$ g\circ f = 1\_{F(a)} \Rightarrow F(g')\circ F(f')=F(1_a) \Rightarrow F(g'\circ f')=F(1_a)$$
である。そして $F$ は忠実であるから $g'\circ f'=1_a$ である。同様にして $f'\circ g'=1_b$ であるから $f',g'$ は同型射。従って $a\simeq b$ である。 $\square$
{{% /details %}}

## 自然変換

関手の間の準同型の事を **自然変換(natural transformation)** という。また {{< refer def.functor-as-a-diagram >}}で述べたように、対象を一般化したものが関手であるとすると、射を一般化したものが自然変換である。

### 自然変換・自然同型

{{% definition title="自然変換" %}}
関手 $F,G:\mathcal{C}\rightarrow\mathcal{D}$ に対して、$F$ から $G$ への**自然変換(natural transformation)** $\phi:F\rightarrow G$ とは、$\mathcal{D}$の射の族 $\\{\phi_a: F(a)\rightarrow G(a)\\}\_{a\in\mathcal{C}}$ であり、任意の $\mathcal{C}$ の射 $f:a\rightarrow b$ に対して、以下の図式が可換となるものである。 $\phi_a$ を $\phi$ の **$a$コンポーネント($a$-component)** という。

$$\xymatrix{
F(a) \ar[r]^{\phi_a} \ar[d]\_{F(f)} & G(a) \ar[d]^{G(f)} \\\\
F(b) \ar[r]^{\phi_b} & G(b)
}$$

$\phi_a$ が全て同型射であるとき $\phi$ を **自然同型(natural isomorphism)** もしくは **自然同値(natural equivalence)** という。また自然同型 $\phi:F\rightarrow G$ が存在する時 $F\simeq G$ と書く。
{{% /definition %}}

複雑な定義に見えるが、関手を図式と思えばなんて事はなく、つまり $\mathcal{D}$ の中の $\mathcal{C}$ の形の図式の対応する点を同じ向きに繋ぐ
射の族で、全体が可換であるような物を自然変換というのである。

{{% tikz %}}
  \begin{tikzpicture}
    \coordinate (xa) at (-1, 1.5) node at (xa) [above] {$F(a)$};
    \coordinate (xb) at (1, 1.5) node at (xb) [above] {$F(b)$};
    \coordinate (xc) at (1.5, 2.5);
    \coordinate (xd) at (0, 3.5);
    \coordinate (xe) at (-1.3, 2.7);
    \coordinate (a)  at (-1, -1) node at (a) [below] {$G(a)$};
    \coordinate (b)  at (1, -1) node at (b) [below] {$G(b)$};
    \coordinate (c)  at (1.5, 0);
    \coordinate (d)  at (0, 1);
    \coordinate (e)  at (-1.3, 0.2);
    \draw [-latex, thick] (xa) to node [above] {$F(f)$} (xb);
    \draw [-latex, thick] (xa) to node [right] {$\phi_a$} (a);
    \draw [-latex, thick] (xb) to node [left] {$\phi_b$} (b);
    \draw [-latex] (xc) to (c);
    \draw [-latex] (xd) to (d);
    \draw [-latex] (xe) to (e);
    \draw [-latex, thick] (a) to node [below] {$G(f)$} (b);
    \draw (b) to (c);
    \draw (c) to (d);
    \draw (d) to (e);
    \draw (e) to (a);
    \draw (xb) to (xc);
    \draw (xc) to (xd);
    \draw (xd) to (xe);
    \draw (xe) to (xa);
  \end{tikzpicture}
{{% /tikz %}}


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
$$ \mathcal{C}^\mathbf{0}\simeq\mathbf{1},\quad\mathcal{C}^\mathbf{1}\simeq\mathcal{C}$$

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

### 同型・圏同値

2つの圏 $\mathcal{C},\mathcal{D}$ が何らかの意味で同じであるという事を表す方法として、 **同型**、**圏同値** という異なる関係性がある。これらの違いをしっかり理解したいので、合わせてここで紹介する。

{{% definition title="圏の同型" %}}
圏 $\mathcal{C},\mathcal{D}$ が **同型(isomorphic)** であるとは関手 $F:\mathcal{C}\rightarrow\mathcal{D}$ と $G:\mathcal{D}\rightarrow\mathcal{C}$ で
$$ G\circ F = 1\_{\mathcal{C}},\ F\circ G=1\_{\mathcal{D}}$$
を満たすものが存在する事である。
{{% /definition %}}

これは、本質的全射の所で述べたのと同じ理由で条件が強すぎて、同型な対象 $a\simeq b$ は同じものと見なした上で圏が本質的に一致する条件を考えたい。
そこで、圏同値という概念が重要となる。

{{% definition title="圏の同値" %}}
圏 $\mathcal{C},\mathcal{D}$ が **同値(equivalent)** であるとは関手 $F:\mathcal{C}\rightarrow\mathcal{D}$ と $G:\mathcal{D}\rightarrow\mathcal{C}$ で自然同型
$$ G\circ F \simeq 1\_{\mathcal{C}},\ F\circ G \simeq 1\_{\mathcal{D}}$$
を満たすものが存在する事である。$F,G$ を **圏同値(equivalence of categories)** という。
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
$F:\mathcal{C}\rightarrow\mathcal{D}$ が圏同値、すなわち関手 $G:\mathcal{D}\rightarrow\mathcal{C}$ が存在して自然同型 $\phi: G\circ F\rightarrow 1\_{\mathcal{C}}, \psi: F\circ G\rightarrow 1\_{\mathcal{D}}$ が存在するとする。

任意の$b\in\mathcal{D}$ に対して $a=G(b)$ とおけば $F(a)=FG(b)\simeq 1\_{\mathcal{D}}(b) = b$。従って $F$ は本質的全射。

任意の$f,g\in\mathcal{C}(a,b)$ について $F(f)=F(g)$ であるとすると $GF(f)=GF(g)$ であるから、$\phi_b\circ GF(f)\circ\phi_a^{-1} = f$ であることより $f = g$。従って$F:\mathcal{C}(a,b)\rightarrow\mathcal{D}(F(a),F(b))$ は単射であるから $F$ は忠実。

$$\xymatrix{
GF(a) \ar[d]\_{GF(f)} \ar@{<-}[r]^{\phi^{-1}_a} & a \ar[d]^{f} \\\\
GF(b) \ar[r]\_{\phi_b} & b \\\\
}$$

また、任意の $g:F(a)\rightarrow F(b)$ に対して $ f = \phi\_{b}\circ G(g)\circ \phi^{-1}\_{a} $とおくと、これを変形して $G(g) = \phi_b^{-1}\circ f\circ\phi_a = GF(f)$ となるが、 $F$ と同様にして $G$ も単射である事が分かるので $g=F(f)$ となる。よって $F:\mathcal{C}(a,b)\rightarrow\mathcal{D}(F(a),F(b))$ は全射であるから $F$ は充満である。$\square$

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

$FG\simeq 1\_{\mathcal{D}}$ はこれまでの議論より明らか。これより右から$F$を合成して$FGF\simeq F$ も得られるが $F$ が充満忠実であることから $GF\simeq 1\_{\mathcal{C}}$ となる。$\square$
{{% /details %}}

## 極限
集合論における直積や直和のような概念は圏論においては **普遍性(universal property)** と呼ばれる性質を用いた **普遍的構成(universal construction)** という方法を用いて定義することができる。 **極限(limit)** は普遍的構成の特別なものであるが、非常に広範な数学的概念に共通する抽象概念である。まずは具体例として終対象・始対象、積・余積を例にあげた後に極限の定義や性質を紹介する。

### 終対象・始対象

{{% definition title="終対象・始対象" %}}
圏 $\mathcal{C}$ の **終対象(terminal object)** とは、任意の対象 $x\in\mathcal{C}$ に対して射 $x\rightarrow 1$ が唯一つ存在するような対象 $1\in\mathcal{C}$ の事である。

$$\xymatrix{
x \ar@{.>}[r]^{!} & 1
}$$

終対象の双対概念を **始対象(initial object)** という。すなわち、任意の対象 $x\in\mathcal{C}$ に対して射 $0\rightarrow x$ が唯一つ存在するような対象 $0\in\mathcal{C}$ の事である。

$$\xymatrix{
0 \ar@{.>}[r]^{!} & x
}$$

これら唯一の射を $!$ や $!\_x$ などと書く。
{{% /definition %}}

例えば、$\mathbf{Set}$ における終対象は一点集合、始対象は空集合である。posetにおける終対象・始対象は、もし存在するならば、最大値・最小値である。

ここで注意したいのは、普遍性による概念の定義はある特定の対象や射を定めるものではないということである。例えば $\mathbf{Set}$ における終対象である一点集合は無数に存在し、その特定の1つを指定することはできない。しかし、以下の命題で示されるように終対象・始対象は同型を除いて一意であり、対象の同型関係は同値関係であるので具体的な対象の選び方によらず、同値類は一意に決定される。このことは、終対象・始対象に限らず一般化されることを後ほど見ていく。

{{% proposition %}}
始対象・終対象は同型を除いて一意に定まる。
{{% /proposition %}}

{{% details 証明 %}}
$0,0'\in\mathcal{C}$ が共に始対象 であるとすると、射 $f:0\rightarrow 0', g:0'\rightarrow 0$ が存在し、
これらを合成すると $g\circ f:0\rightarrow 0$ が得られるが $0$ が始対象であることより $0\rightarrow 0$ は唯一つであるので $g\circ f=1_0$。同様にして $f\circ g=1_{0'}$ であるので$f:0\rightarrow 0'$ は同型射。よって $0\simeq 0'$。 終対象についても同様。
$$\xymatrix{
0 \ar[r]\_f \ar@/^1pc/[rr]^{1_0} & 0' \ar[r]\_g & 0
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

終対象・始対象、積・余積を抽象化した概念が **極限(limit)** である。これがどのようなものか理解するために、具体例として積についてに考える。積の図式は少し書き直してみると以下のように書くことができるが、この点線で囲まれた $a\xleftarrow{f} x \xrightarrow{g} b$ という形の図式を対象とする圏を考える事が出来る。
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
    \draw [-latex] (x) to node [right] {\small $f$} (a);
    \draw [-latex] (x) to node [right] {\small $g$} (b);
    \draw [-latex, thick] (p) to node [left] {\small $\pi_a$} (a);
    \draw [-latex, thick] (p) to node [left] {\small $\pi_b$} (b);
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

では錐と錐の圏の定義を進める。 {{< refer def.functor-as-a-diagram >}} で説明したように、錐の底面はその形を表す添字圏  $\mathcal{J}$ からの関手 $F: \mathcal{J}\rightarrow\mathcal{C}$ で表す事ができる。そして、底面の各頂点に対して $x$ から射が生えているというのが一般的な錐の定義であるが、対象と射より関手と自然変換によって物事を説明した方が使い勝手が良い為、ここでは別の定義行おうと思う。その為には、下図の用に頂点 $x$ を底面と同じ形に開いてしまおう。

{{% tikz %}}
  \begin{tikzpicture}
    \coordinate (xa) at (-1, 1.5) node at (xa) [above] {$x$};
    \coordinate (xb) at (1, 1.5) node at (xb) [above] {$x$};
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
    \draw [-latex, thick] (xa) to node [above] {$1_x$} (xb);
    \draw (xb) to (xc);
    \draw (xc) to (xd);
    \draw (xd) to (xe);
    \draw (xe) to (xa);
  \end{tikzpicture}
{{% /tikz %}}

このように展開してみると、上面を形が $\mathcal{J}$ の定数関手 $x$ で表せる事がわかるだろう。これを $\Delta(x):\mathcal{J}\rightarrow\mathcal{C}$ という記号で書く事にする。すると、錐とは上面 $\Delta(x)$ から底面 $F$ への自然変換であるとして表す事ができる。また、この双対版として底面から上面への錐も考える事ができる。

{{% definition title="錐" %}}
図式 $F:\mathcal{J}\rightarrow\mathcal{C}$ と対象 $x\in\mathcal{C}$ について、自然変換 $\phi:\Delta(x)\rightarrow F$ を **$x$ から $F$ への 錐(cone)** という。同じ錐を $(x,\phi)$ とも書く。

同様に、自然変換 $\phi:F\rightarrow\Delta(x)$ を **$F$ から $x$ への錐** もしくは **余錐(cocone)** という。
{{% /definition %}}

定義が高階になり難しく見えるが、関手を図式と思えば二つの面 $\Delta(x)$ と $F$ を縦に繋いだものが錐なのだと自然に理解できるだろう。ところで、ここで登場した $\Delta$ はそれ自体が関手である。今後使うので定義をしておく。

{{% definition title="対角関手" %}}
圏 $\mathcal{J}$ と $\mathcal{C}$ について、対象 $x\in\mathcal{C}$ を定数関手 $x:\mathcal{J}\rightarrow\mathcal{C}$ に、射$f:x\rightarrow y$ をそれらの間の自然変換(これは $f$ と同一視可能)に移す対応は関手
$$ \Delta:\mathcal{C}\rightarrow\mathcal{C}^{\mathcal{J}} $$
となる。これを **対角関手(diagonal functor)** という。
{{% /definition %}}

そして、錐の頂点の間の射によって、錐から錐への射を定義する事で錐の圏が出来上がる。

{{% definition title="錐の圏" %}}
図式 $F:\mathcal{J}\rightarrow\mathcal{C}$ への錐を対象とし、2つの錐
$\phi:\Delta(x)\rightarrow F$ と $\psi:\Delta(y)\rightarrow F$ の間の射を、以下が可換となるような自然変換 $f:\Delta(x)\rightarrow\Delta(y)$ (これは射 $f:x\rightarrow y$ と同一) によって定めると圏となる。これを **$F$ への錐の圏(category of cones to $F$)** という。
$$\xymatrix{
\Delta(x) \ar[r]^f \ar[d]\_{\phi} & \Delta(y) \ar[ld]^{\psi} \\\\
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
$F:\mathcal{J}\rightarrow\mathcal{C}$ への錐の圏の終対象の頂点を $\varprojlim F$ と書き、錐 $(\varprojlim F,\phi)$ を$F$の **極限(limit)** もしくは **射影的極限(projective limit)** という。また $\phi$ を **標準射影(canonical projection)** という。

$F:\mathcal{J}\rightarrow\mathcal{C}$ からの錐の圏の始対象の頂点を $\varinjlim F$ と書き、 $(\varinjlim F,\psi)$ を$F$の **余極限(colimit)** もしくは **帰納的極限(inductive limit)** という。また $\psi$ を **標準入射(canonical inclusion)** という。

$\displaystyle\varprojlim F$ の代わりに、$\displaystyle \varprojlim\_{i\in\mathcal{J}}F(i)$ とも書く。
{{% /definition %}}

極限は終対象であるから、同型を除いて一意に定まる。余極限も同様。

上の定義のように、極限とは条件を満たす"錐"(極限錐という)の事であるが、極限錐の頂点の事をさして極限という場合もある。しかし、同型な極限錐の頂点同士も同型であるし、逆に $a\simeq b$ で $a$ が極限錐の頂点であるならば、 $b$ もそれと同型な極限錐の頂点となる事が簡単に示せるので、用語の濫用は実用上は問題とならない。

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
である。これは少し分かり辛いので例を挙げる。例えば $f,g:\mathbb{N}\rightarrow\mathbb{N}$ が $f(n) = n, g(n) = n + 2$ の場合は
$$ 0 \sim 2 \sim 4 \cdots,\quad 1\sim 3\sim 5\cdots $$
であるような最小の同値関係(すなわち $n$ の偶奇の一致)で$\mathbb{N}$を割ったものが $\mathrm{coeq}(f,g)$ なので
$$ \mathrm{coeq}(f,g) = \\{[0],[1]\\}$$
となる。

$A\xrightarrow{f}C\xleftarrow{g}B$ の引き戻しは
$$A\times\_C B=\\{(x,y) \in A\times B \mid f(x)=g(y) \\}$$
である。また $A\xleftarrow{f}C\xrightarrow{g}B$ の押し出しは $(0,f(x))\sim(1,g(x))\ (\forall x\in C)$ となるような最小の同値関係 $\sim$ による $A+B$ の商集合
$$ A+\_C B = (A+B)/{\sim}$$
である。

### 完備性・極限の存在定理

前節のように $\mathbf{Set}$ は任意の(小さい)極限や余極限が存在するという良い性質を持っている。このような圏の性質を **完備性(completeness)** という。

{{% definition title="完備性" %}}
圏 $\mathcal{C}$ が任意の小さな圏 $J$ について、任意の図式 $\mathcal{J}\rightarrow\mathcal{C}$ の極限を持つならば $\mathcal{C}$ は **完備(complete)** であるという。余極限を持つならば **余完備(cocomplete)** であるという。また、完備かつ余完備であることを **双完備(bicomplete)** という。

また、任意の有限の圏(対象の集合、射の集合が共に有限集合である圏)$J$ について、極限を持つならば **有限完備(finite complete)**、余極限を持つならば **有限余完備(finite cocomplete)** という。
{{% /definition %}}

任意の極限を持つことを直接証明するのは難しいが、以下の定理より、積とイコライザもしくは余積とコイコライザを持つ事のみ示せば十分である。

{{% theorem title="極限の存在定理" %}}
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
$$\xymatrix{
x \ar[r]^{\phi} & \prod\_{i\in\mathcal{J}}F(i) \ar@<2pt>[r]^s \ar@<-2pt>[r]_t & \prod\_{f: i\rightarrow j\in\mathcal{J}}F(j) 
}$$

$\phi=(\phi_i)\_{i\in\mathcal{J}}$ とおくと、これは全ての $\mathcal{J}$ の射 $f:i\rightarrow j$ に対して、$j\in\mathcal{J}, F(f)\circ \phi_i = \phi_j$ であること、すなわち以下の図式が可換であることと同値。
$$\xymatrix{
x \ar[d]\_{\phi_i} \ar[rd]^{\phi_j} \\\\
F(i) \ar[r]_{F(f)} & F(j)
}$$
すなわち、 $(x,\\{\phi_i\\})$ は $F$ への錐に他ならない。したがって、この図式に対するイコライザは $x$ から $F$ への錐の圏の終対象、すなわち$F$ の極限と一致する。
{{% /details %}}

{{% proposition %}}
$\mathbf{Set}$ は双完備である。
{{% /proposition %}}

## 普遍性

本節では圏論において非常に重要な概念である **普遍性(universal property)** と関連する諸概念について説明する。普遍性を用いると、圏論の様々な概念を統一的な方法で構成する事ができる。前節で説明した極限も普遍性を用いた構成の一つである。

普遍性の説明には複数の方法があるが、ここではエミリー・リール(Emily Riehl)による **表現可能関手(representable functor)** を用いた説明を行う。

### Hom関手
圏論の語彙では、対象や射が具体的に何であるか(例えばベクトル空間や線型写像であるといったこと)を特定し、その性質(例えばベクトル空間の定理)を用いて議論を行う事が基本的には出来ない。従って、圏論においてある対象 $a\in\mathcal{C}$ について調べる時には $a$に向かう射の集合 $\mathcal{C}(x, a)$や、 $a$ から出る射の集合 $\mathcal{C}(a, x)$ について調べる事が主要な手段となる。そこで **Hom関手(hom-functor)** という概念が登場する。

$\mathcal{C}$ を局所小圏とすると、任意の $a,x\in\mathcal{C}$ について $\mathcal{C}(a, x)$ は集合になる。
すなわち $\mathbf{Set}$ の対象になるので、$x\longmapsto \mathcal{C}(a, x)$ という $\mathcal{C}$ から $\mathbf{Set}$ への対象の対応を得ることができる。このとき、射 $f:x\rightarrow y$ に対応する$\mathbf{Set}$ の射 $\mathcal{C}(a, f): \mathcal{C}(a, x)\rightarrow\mathcal{C}(a, y)$ も定める事ができて、この対応は関手となる。

{{% definition title="共変Hom関手" %}}
局所小圏 $\mathcal{C}$ と対象 $a\in\mathcal{C}$ に対して、 $x\in\mathcal{C}$ を $\mathcal{C}(a, x)$ に移し, $f: x\rightarrow y$ を
$$\mathcal{C}(a,x) \ni g \mapsto f\circ g \in\mathcal{C}(a,y)$$
に移す対応 $\mathcal{C}(a, -)$ は関手$\mathcal{C}\rightarrow\mathbf{Set}$となる。
これを **共変Hom関手(covariant hom functor)** という。

$$
\xymatrix{
            & a \ar[ld]\_{\mathcal{C}(a,x)\ni g}^{}=\"p\"  \ar[rd]^{f\circ g\in\mathcal{C}(a,y)}\_{}=\"q\" &    \\\\
x \ar[rr]_f &             & y
\ar@{~>} \"p\";\"q\"
}
$$
{{% /definition %}}

{{% details 関手であることの証明 %}}
任意の $a,x\in\mathcal{C}$, $f:a\rightarrow x$ について
$$ \mathcal{C}(a,-)(1_x): f\longmapsto 1_x\circ f = f$$
であるから $ \mathcal{C}(a,-)(1_x) = 1_{\mathcal{C}(a,x)} $
また、任意の $f: x\rightarrow y, g:y\rightarrow z$ と $p:a\rightarrow x$ について
$$ (\mathcal{C}(a,-)(g)\circ\mathcal{C}(a,-)(f))(p) = g\circ(f\circ p) = (g\circ f)\circ p = \mathcal{C}(a,-)(g\circ f)(p) $$
$\square$
{{% /details %}}

{{% definition title="反変Hom関手" %}}
局所小圏 $\mathcal{C}$ と対象 $a\in\mathcal{C}$ に対して、 $x\in\mathcal{C}$ を $\mathcal{C}(x, a)$ に移し、 $f: x\rightarrow y$ を
$$\mathcal{C}(y,a) \ni g \mapsto g\circ f \in\mathcal{C}(x,a)$$
に移す対応 $\mathcal{C}(-, a)$ は関手 $\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ となる。
これを **反変Hom関手(contravariant hom functor)** という。

$$
\xymatrix{
            & a \ar@{<-}[ld]\_{\mathcal{C}(x,a)\ni g\circ f}^{}=\"p\" \ar@{<-}[rd]^{g\in\mathcal{C}(y,a)}\_{}=\"q\" &    \\\\
x \ar[rr]\_f &             & y
\ar@{<~} \"p\";\"q\"
}
$$
{{% /definition %}}

証明は共変Hom関手と同様なので省略。「共変」「反変」は誤解の恐れがない場合は省略する事が多い。

### 表現可能関手
Hom関手 $\mathcal{C}(a, -), \mathcal{C}(-, a)$ は、対象 $a$ 一つのみでその全てが表現される。この意味でHom関手 $\mathcal{C}(a, -), \mathcal{C}(-, a)$ 及びこれらと自然同型な関手は **表現可能(representable)** であると言われ、 $a$ をそれを **表現する対象(representing object)** という。

{{% definition title="表現可能関手" %}}
局所小圏 $\mathcal{C}$ から $\mathbf{Set}$ への反変関手 $F:\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ が、ある $a\in\mathcal{C}$ について
$$ F\simeq\mathcal{C}(-, a) $$
である時、 $F$ を **表現可能関手(representable functor**) といい、 $\mathcal{C}(-, a)$ を $F$ の **表現(representation)** 、$a$ を $F$ を **表現する対象(representing object)** という。

同様に $\mathcal{C}(a, -)$ と自然同型である関手を **余表現可能関手(co-representable functor)** もしくはこれも表現可能関手という。
{{% /definition %}}

後に示すように表現可能関手 $F$ を表現する対象は同型を除いて一意であるので、表現可能性を用いて対象 $a$ を定義する事も可能である。

表現可能関手とはどのようなものか具体例を見てみよう。非常に簡単な例として、 $\mathcal{C}$ として自然数の集合 $\mathbb{N}$ をとる。これは離散圏であり、恒等射以外存在しないので
関手 $\mathbb{N}(-, n)$ は $\mathbb{N}(n, n) = \\{1_n\\}$ で、それ以外は空集合となる関手である。すなわち、単集合を $1$、空集合を $0$ とすれば表現可能関手 $\mathbb{N}(-, n)$ は
$$ 0, 0, \ldots, 0, \overbrace{1}^{n\text{番目}}, 0,\ldots $$
という集合の列である。自然数 $n$ という情報のみでこれが定まるし、逆に $\mathbf{Set}$ 内で $n$ が表現されているというイメージも得られるだろう。
また $\mathbb{N}$ の対象が表現されているだけでなく、 $\mathbb{N}$ の射も表現されている。というのは自然変換 $\mathbb{N}(-, n)\rightarrow\mathbb{N}(-, n)$ は空関数 $0\rightarrow 0$ と単一の関数 $1\rightarrow 1$ で図式を
縦に繋いだ物のみであるからただ一つしか存在しない。そして $m\neq n$ の時、自然変換 $\mathbb{N}(-, m)\rightarrow\mathbb{N}(-, n)$ は存在しない。何故ならば、$1\rightarrow 0$ なる関数は存在しないからである。
これは $\mathbb{N}(n ,n)$ が単集合、 $\mathbb{N}(m, n)\quad (m\neq n)$ が空集合であるということと対応している。

続いて、同じ $\mathbb{N}$ だが、これを順序集合とした場合を考えよう。これは以下のような圏であり、各射は大小関係 $\leq$ である。
$$
0 \rightarrow 1 \rightarrow\cdots\rightarrow n-1\rightarrow n\rightarrow n+1\rightarrow\cdots
$$
すると、表現可能関手 $\mathbb{N}(-, n):\mathbb{N}^{\mathrm{op}}\rightarrow\mathbb{Set}$ は以下の図式となる。

$$
1\leftarrow 1 \leftarrow\cdots\leftarrow 1\leftarrow\overbrace{1}^{n\text{番目}} \leftarrow 0 \leftarrow \cdots
$$

すると、先ほどと同様にして $m\leq n$ ならば $\mathbb{N}(-, m)\rightarrow\mathbb{N}(-, n)$ がただ一つ存在し、そうでなければ存在しないという事がわかる。これは $\mathbb{N}(m, n)$ の要素数と一致する。

以上は非常にシンプルな例であるが、$a\in\mathcal{C}$ と表現可能関手 $\mathcal{C}(-, a)$ が、その周囲の射も含め綺麗に対応している事が分かるであろう。誤解を恐れずに言えば $a$ と $\mathcal{C}(-, a)$ は同じものの異なる表現であると言える。続く節で **米田埋め込み(Yoneda embedding)** としてこれを説明する。

### 米田埋め込み・米田の補題

表現可能関手の定義では自然変換 $\mathcal{C}(-, a)\rightarrow F$ や $\mathcal{C}(a, -)\rightarrow F$ が使われるが、これらに関する非常に重要な定理が **米田の補題(Yoneda's Lemma)** である。
Emily Riehlによれば米田の補題は"圏論の最も重要な成果"である。

{{% definition title="米田埋め込み" %}}
局所小圏 $\mathcal{C}$ について、関手 $\mathcal{Y}:\mathcal{C}\rightarrow\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}$ を
$$ \mathcal{Y}(a) = \mathcal{C}(-, a) $$
$$ \mathcal{Y}(f): \mathcal{C}(-, a)\ni (g\circ -)\longmapsto (f\circ g\circ -)\in\mathcal{C}(-, b)$$
にて定めたものを **米田埋め込み(Yoneda embedding)** という。
{{% /definition %}}

$\mathcal{C}$ を $\mathcal{C}^{\mathrm{op}}$ に置き換えることで、この双対版も同様に考える事ができる。
非常に高階になってきて分かりにくいので、改めて関手を図式とみなすやり方で描いてみると下図のようになる。
対象 $a,b$ を点線で囲まれた図式(表現可能関手)に写し、射 $f:a\rightarrow b$ をそれらを繋ぐ射の族(自然変換) に写す関手が米田埋め込みである。

$$\xymatrix{
a \ar[d]^f && \cdots \ar[r] & \mathcal{C}(x, a) \ar[r]\ar[d]^{f\circ -} & \mathcal{C}(y, a) \ar[r]\ar[d]^{f\circ -} & \cdots \\\\
b          && \cdots \ar[r] & \mathcal{C}(x, b) \ar[r] & \mathcal{C}(y, b) \ar[r] & \cdots
\ar@{~>}^{\mathcal{Y}}(10, -9);(20,-9)
\ar@{.}(25,7);(120,7)
\ar@{.}(120,7);(120,-5)
\ar@{.}(120,-5);(25,-5)
\ar@{.}(25,-5);(25,7)
\ar@{.}(25,-14);(120,-14)
\ar@{.}(120,-14);(120,-26)
\ar@{.}(120,-26);(25,-26)
\ar@{.}(25,-26);(25,-14)
}$$

反変関手 $\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ を **前層(presheaf)** とも呼ぶと既に述べたが、米田埋め込みは圏 $\mathcal{C}$ を前層の圏 $\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}$ に埋め込む操作であると言うこともできる。前層の圏については次章で詳しく説明するがとても良い性質をもった圏である。

{{% theorem title="米田の補題" %}}
局所小圏 $\mathcal{C}$ と関手 $F:\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ 、$a\in\mathcal{C}$ について $a,F$ について自然な同型
$$ \mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(a),F)\simeq F(a) \qquad (\alpha\mapsto\alpha_a(1_a))$$
が成り立つ。
{{% /theorem %}}

米田の補題の同型が $a$ について自然であるというのは、任意の $f:b\rightarrow a$ について以下が可換である事であり、

$$\xymatrix{
\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(a), F) \ar[r]^(.6){\simeq}  \ar[d]\_{\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(f), F)} & F(a) \ar[d]^{F(f)} \\\\
\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(b), F) \ar[r]^(.6){\simeq} & F(b)
}$$

$F$ について自然であるというのは、任意の $\rho:F\rightarrow G$ について以下が可換となる事である。

$$\xymatrix{
\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(a), F) \ar[r]^(.6){\simeq}  \ar[d]\_{\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(a), \rho)} & F(a) \ar[d]^{\rho_a} \\\\
\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(a), G) \ar[r]^(.6){\simeq} & G(a)
}$$

{{% details 証明 %}}
$\alpha\in\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(a),F)$ とする。 $\alpha$ は自然変換であるから任意の $f:y\rightarrow x$ について、以下が可換である。

$$\xymatrix{
\mathcal{C}(x, a) \ar[r]^{\alpha_x}  \ar[d]\_{-\circ f} & F(x) \ar[d]^{F(f)} \\\\
\mathcal{C}(y, a) \ar[r]\_{\alpha_y} & F(y)
}$$

すなわち、任意の $h:x\rightarrow a$ に対して
$$ \alpha_y(h\circ f) = F(f)(\alpha_x(h)) $$
である。ここで

$$ \phi\_{a,F}: \mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(a),F)\ni\alpha\longmapsto \alpha_a(1_a)\in F(a) $$
$$ \psi\_{a,F}: F(a)\ni x \longmapsto F(-)(x)\in\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(a),F)$$

とおくと

$$\psi\_{a,F}\circ\phi\_{a,F}(\alpha)(h) = F(h)(\alpha_a(1_a)) = \alpha_x(1_a\circ h) = \alpha_x(h)$$
$$\phi\_{a,F}\circ\psi\_{a,F}(x) = F(1_a)(x) = 1\_{F(a)}(x) = x$$

であるので $\phi\_{a,F},\psi\_{a,F}$ は同型写像。

続いて同型の自然性を確認する。任意の$f: b\rightarrow a$ と $\alpha\in\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(a), F)$ について

$$
F(f)(\phi\_{a,F}(\alpha)) = F(f)(\alpha_a(1_a)) = \alpha_b(1_a\circ f) = \alpha_b(f)
$$
$$
\phi\_{b,F}(\alpha\circ \mathcal{Y}(f)) = \phi\_{b,F}(\alpha\circ \mathcal{C}(-, f)) = (\alpha_b\circ\mathcal{C}(b, f))(1_b) = \alpha_b(f\circ 1_b) = \alpha_b(f)
$$

より、
$F(f)(\phi\_{a,F}(\alpha)) = \phi\_{b,F}(\alpha\circ \mathcal{Y}(f)) $ であるから、
$\phi\_{a,F}$ は $a$ について自然。続いて、任意の $\rho:F\rightarrow G$ と $\alpha\in\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(a), F)$ について

$$
\rho_a(\phi\_{a,F}(\alpha)) = \rho_a(\alpha_a(1_a)) = \rho_a\circ\alpha_a(1_a)
$$
$$
\phi\_{a,G}(\rho\circ\alpha) = \rho_a\circ\alpha_a(1_a)
$$

より$\rho_a(\phi\_{a,F}(\alpha)) =\phi\_{a,G}(\rho\circ\alpha)$ であるから $F$ についても自然。 $\square$
{{% /details %}}

米田の補題のイメージを掴むため、具体例を考えてみよう。まず、既に説明した $\mathcal{C}$ が自然数の集合 $\mathbb{N}$ である場合を考えると、
自然変換 $\mathbf{Set}^{\mathbb{N}^{\mathrm{op}}}(\mathcal{Y}(a),F)$ は、以下の縦の射の族である。ここで$0$ は空集合、 $1$ は単集合である。

$$\xymatrix{
0 \ar[d] & \cdots & 0 \ar[d] & 1 \ar[d] & 0 \ar[d] & \cdots \\\\
F(0)     & \cdots & F(a-1)   & F(a)     & F(a+1) & \cdots
}$$

この自然変換がいくつあるかというと、　$0\rightarrow F(x)$ は空関数しかあり得ないので一意に定まり、 $1\rightarrow F(a)$ は $F(a)$ の要素数だけ存在する。
従って $\mathbf{Set}^{\mathbb{N}^{\mathrm{op}}}(\mathcal{Y}(a), F)\simeq F(a)$  である。

$\mathbb{N}$ が順序集合の場合も考えよう。この場合の自然変換は以下の図式の縦の射の族となる。

$$\xymatrix{
1 \ar[d]^{\alpha_0} \ar@{<-}[r] & \cdots \ar@{<-}[r] & 1 \ar[d]^{\alpha\_{a-1}}\ar@{<-}[r] & 1 \ar[d]^{\alpha\_a}\ar@{<-}[r] & 0 \ar[d]^{\alpha\_{a+1}}\ar@{<-}[r] & \cdots \\\\
F(0) \ar@{<-}[r]    & \cdots \ar@{<-}[r] & F(a-1) \ar@{<-}[r]  & F(a) \ar@{<-}[r]    & F(a+1) \ar@{<-}[r] & \cdots
}$$
すると、先ほどと同様にして $\alpha\_{a+1}$ より右側は全て空関数となり、 $\alpha_a$ は $F(a)$ の要素数だけ存在する。そして、 $\alpha_0,\ldots,\alpha\_{a-1}$ は図式の可換性から $\alpha_a$ が定まれば自動的に決まる。
従って、この場合も自然変換は $F(a)$ の要素数だけ存在し $\mathbf{Set}^{\mathbb{N}^{\mathrm{op}}}(\mathcal{Y}(a), F)\simeq F(a)$ となる。また、この全単射が $\alpha\mapsto\alpha_a(1_a)$ で与えられることもわかるであろう。また、この例から $F(a)$ の要素が自然変換 $\mathcal{Y}(a)\rightarrow F$ 全体を**生成する** ことが分かる。

一般の場合も同様で、任意の対象 $x\in\mathcal{C}$ について、射 $x\rightarrow a$ が存在しない時には、$\mathcal{C}(x, a)=\emptyset$ であるので、自然変換 $\mathcal{Y}(a)\rightarrow F$ の$x$コンポーネントは空関数に一意に定まる。射 $x\rightarrow a$ が存在する時には、射 $\mathcal{C}(a,a)\rightarrow\mathcal{C}(x,a)$ が存在するから以下の図式を考えることができて、図式の可換性から $\alpha_a(1_a) \in F(a)$ が決まれば、 $\alpha_x$ が一意に決まる。また、この特別な場合として$x=a$ の場合を考えれば $\alpha_a(1_a)$ が決まれば、 $\alpha_a$ 自身も一意に決まる。従って、 $\alpha_a(1_a) \in F(a)$ が自然変換 $\alpha$ 全体を生成するので、$\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(a),F)\simeq F(a)$ となるわけである。

$$\xymatrix{
\mathcal{C}(a, a) \ar[r]\ar[d]^{\alpha_a} & \mathcal{C}(x, a)\ar[d]^{\alpha_x} \\\\
F(a) \ar[r] & F(x)
}$$

### 米田埋め込みの性質

米田埋め込みが"埋め込み"と呼ばれるのに相応しいのは以下の命題より。

{{% proposition %}}
米田埋め込みは忠実充満
{{% /proposition %}}
{{% details 証明 %}}
米田の補題より、任意の $a,b\in\mathcal{C}$ について自然な全単射
$$ \mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(a),\mathcal{Y}(b))\simeq \mathcal{Y}(b)(a)=\mathcal{C}(a,b) $$
が存在する。 $\square$
{{% /details %}}

従って {{< refer prop.embedding >}} より
$$\mathcal{Y}(a)\simeq \mathcal{Y}(b)\Leftrightarrow a\simeq b$$
である。 米田埋め込みの双対 $\mathcal{C}(a, -): \mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}^{\mathcal{C}}$ についても全く同様であり、 **米田の原理(Yoneda principle)** と呼ばれる以下の命題を得る。

{{% proposition title="米田の原理" %}}
局所小圏 $\mathcal{C}$ の対象 $a,b$ について
$$a\simeq b\ \Leftrightarrow\ \mathcal{C}(-, a)\simeq\mathcal{C}(-, b)\ \Leftrightarrow\ \mathcal{C}(a, -)\simeq\mathcal{C}(b, -)$$
{{% /proposition %}}

この定理から直ちに以下が示される。

{{% proposition %}}
表現可能関手を表現する対象は同型を除いて一意である。
{{% /proposition %}}

また、以下が成り立つ。

{{% proposition label="prop.yoneda-preserves-limits" %}}
米田埋め込みは極限を保つ。すなわち自然同型
$$ \mathcal{Y}(\varprojlim F) \simeq \varprojlim (\mathcal{Y}\circ F)$$
が存在する。
{{% /proposition %}}
{{% details 証明 %}}
$x\in\mathcal{C}$ について自然な同型
$$\mathcal{Y}(\varprojlim F)(x) = \mathcal{C}(x, \varprojlim F) \simeq\mathcal{C}^{\mathcal{J}}(\Delta(x), F)\simeq \mathbf{Set}^{\left(\mathcal{C}^\mathcal{J}\right)^{\mathrm{op}}}(\mathcal{Y}\circ\Delta(x), \mathcal{Y}\circ F)$$
が存在する。最後の同型は米田の原理による。
ここで、対角関手 $\Delta$ について $\mathcal{Y}\circ\Delta(x)\simeq\Delta(\mathcal{Y}(x))$ である事が簡単に分かるので
$$\mathbf{Set}^{\left(\mathcal{C}^\mathcal{J}\right)^{\mathrm{op}}}(\mathcal{Y}\circ\Delta(x), \mathcal{Y}\circ F) \simeq 
\mathbf{Set}^{\left(\mathcal{C}^\mathcal{J}\right)^{\mathrm{op}}}(\Delta(\mathcal{Y}(x)), \mathcal{Y}\circ F) \simeq 
\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(x), \varprojlim (\mathcal{Y}\circ F))
$$
であり、米田の補題よりこれは
$$ \varprojlim(\mathcal{Y}\circ F)(x)$$
と同型。したがって
$$ \mathcal{Y}(\varprojlim F)(x) \simeq \varprojlim(\mathcal{Y}\circ F)(x)$$
であり、以上の同型は全て $x$ について自然であるので
$$ \mathcal{Y}(\varprojlim F) \simeq \varprojlim(\mathcal{Y}\circ F)$$
となる。$\square$
{{% /details %}}
余極限は一般には保たれないので注意。

この命題の具体例をいくつか並べてみると以下のような等式を得る。

{{% proposition label="prop.yoneda-preserves-limits-examples" %}}

$$\begin{align\*}
\mathcal{C}(x, 1) &\simeq 1 \\\\
\mathcal{C}(x, a\times b) &\simeq \mathcal{C}(x, a)\times\mathcal{C}(x, b) \\\\
\mathcal{C}\left(x, \prod\_{i\in\mathcal{J}} a_i\right) &\simeq \prod\_{i\in\mathcal{J}}\mathcal{C}(x, a_i)
\end{align\*}$$
これらの $\mathcal{C}$ を $\mathcal{C}^{\mathrm{op}}$ に置き換えれば以下も成立する。
$$\begin{align\*}
\mathcal{C}(0, x) &\simeq 1 \\\\
\mathcal{C}(a+b, x) &\simeq \mathcal{C}(a, x)\times\mathcal{C}(b, x) \\\\
\mathcal{C}\left(\coprod\_{i\in\mathcal{J}} a_i, x\right) &\simeq \prod\_{i\in\mathcal{J}}\mathcal{C}(a_i, x)
\end{align\*}$$
{{% /proposition %}}

また、これと米田の原理を組み合わせれば様々な圏における極限・余極限の性質の証明が簡単にできる。例えば

{{% proposition %}}
$$\begin{align\*}
a \times 1 &\simeq a \\\\
a \times b &\simeq b \times a \\\\
a + 0 & \simeq a \\\\
a + b &\simeq b + a
\end{align\*}$$
{{% /proposition %}}
などである。例えば1つ目は
$$ \mathcal{Y}(a\times 1)(x)\simeq \mathcal{C}(x, a\times 1) \simeq\mathcal{C}(x, a)\times\mathcal{C}(x, 1)\simeq\mathcal{C}(x, a)\times 1\simeq\mathcal{C}(x, a)\simeq\mathcal{Y}(a)(x)$$
が $x$ に関して自然な同型であることを集合論的に簡単に示すことができ、これから $\mathcal{Y}(a\times 1)\simeq\mathcal{Y}(a)$ を得るので、米田の原理より $a\times 1\simeq a$ が導かれる。

代数的なアナロジーが自由に使えるわけではないので注意。例えば $a\times 0=0$といった性質は一般には成り立たない。

以上のように $\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}$ は非常に良い性質を持っているので、米田埋め込みによって一旦議論の舞台を $\mathcal{C}$ から $\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}$ に移すことで様々な議論が行いやすくなるわけである。

### 普遍性・普遍要素

米田の補題より、 自然同型 $\mathcal{Y}(a)\simeq F$ に対応する要素 $u\in F(a)$ が存在する。これを $F$ の普遍要素という。

{{% definition title="普遍要素" %}}
表現可能関手 $F: \mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ を表現する対象が $a$ である時、米田の補題によって自然同型
$$ \mathcal{Y}(a)\simeq F$$
と対応する $u\in F(a)$ を $F$ の **普遍要素(universal element)** という。
{{% /definition %}}

この $u$ を普遍要素と呼ぶ理由を説明する。米田の補題の所で説明したように、 $u$ のみから自然変換 $\mathcal{Y}(a)\rightarrow F$ 全体を生成する事が可能である訳だが、特にこれが自然同型 $\mathcal{Y}(a)\simeq F$ の時には $F$ そのものを生成することが出来る。ということは、 $a\in\mathcal{C}$ と $u\in F(a)$ のみから、任意の $x\in\mathcal{C}$ について $F(x)$ の任意の要素を具体的に構成することができる。この性質を $u$ の **普遍性(universal property)** といい、この構成を **普遍的構成(universal construction)** という。


普遍要素 $u$ 及び、普遍構成について調べる。米田の補題の証明より $\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(a),F)$ と $F(a)$ の同型は

$$ \phi\_{a,F}: \mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(a),F)\ni\alpha\longmapsto \alpha_a(1_a)\in F(a) $$
$$ \psi\_{a,F}: F(a)\ni x \longmapsto F(-)(x)\in\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(a),F)$$

によって与えられるので、 $\alpha$ が同型射であるときに、対応する $u=\alpha_a(1_a)$ が普遍要素である。そして、 $\alpha_a$ は $\alpha_a: \mathcal{C}(a, a)\rightarrow F(a)$ という全単射であるので、この左辺の $1_a$ 対応する要素が普遍要素である。そして、
$$ F(-)(u): \mathcal{C}(-, a)\rightarrow F$$
が自然同型 $\mathcal{C}(-, a)\simeq F$ の具体的な構成であることも分かる。

{{% proposition title="普遍要素・普遍的構成" %}}
表現可能関手 $\mathcal{C}(-, a)\simeq F$ について、同型 $\mathcal{C}(a, a)\simeq F(a)$ によって $1_a$ に対応する $u\in F(a)$ が普遍要素であり、この自然同型は $F(-)(u):\mathcal{C}(-, a)\rightarrow F$ によって与えられる。

すなわち、任意の $x\in\mathcal{C}$ と $v\in F(x)$ に対して、 $v=F(f)(u)$ となるような $f: x\rightarrow a$ がただ一つ存在する。
{{% /proposition %}}

これは逆も成立し、普遍性の説明でよく登場する定義が得られる。

{{% proposition label="prop.universal-construction" %}}
局所小圏 $\mathcal{C}$, 関手 $F:\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$, 対象 $a\in\mathcal{C}$, 要素 $u\in F(a)$ について、
任意の $x\in\mathcal{C}$ と $v\in F(x)$ に対して、 $v=F(f)(u)$ となるような $f: x\rightarrow a$がただ一つ存在するならば、 $F$ は表現可能関手であり、 $a$ がそれを表現する対象であり、 $u$ が普遍要素である。
{{% /proposition %}}

普遍的構成の具体例を見てみよう。例として関手 $F = \mathcal{C}(-, a)\times\mathcal{C}(-, b)$ を考えよう。これが表現可能関手となるのは
ある対象 $p\in\mathcal{C}$ と、 $F(p)=\mathcal{C}(p, a)\times\mathcal{C}(p, b)$ の要素、すなわち射 $\pi_a:p\rightarrow a$ と $\pi_b: p\rightarrow b$ があって、
任意の $x\in\mathcal{C}$ と、$F(x)$ の要素、すなわち射 $f:x\rightarrow a$ と $g:x\rightarrow b$ に対して、
$$ (f, g) = F(\xi)(\pi_a, \pi_b)=(\mathcal{C}(\xi, a)\times\mathcal{C}(\xi, b))(\pi_a,\pi_b) = (\pi_a\circ\xi, \pi_b\circ\xi) $$
となるような $\xi: x\rightarrow p$ がただ一つ存在することである。となって、積の定義が得られる。

$$\xymatrix{
            & x \ar[ld]\_{f} \ar[rd]^{g} \ar@{.>}[d]^{\exists! \xi} &\\\\
a           & p \ar[l]\_{\pi_a} \ar[r]^{\pi_b} & b
}$$

まとめると、関手 $\mathcal{C}(-, a)\times\mathcal{C}(-, b)$ が表現可能の時、これを表現する対象が $a\times b$ で、普遍要素が標準射影 $\pi_a:a\times b\rightarrow a, \pi_b:a\times b\rightarrow b$ である。
同様にして、関手 $\varprojlim(\mathcal{Y}\circ F)$ を表現する対象が $\varprojlim F$ で、普遍要素が極限錐 $\phi:\Delta(\varprojlim F)\rightarrow F$ である。

## 指数対象

極限とは異なる普遍性をもつ対象に **指数対象(exponential object)** がある。指数対象は "関数" のような性質を持つ対象のことで、"引数" を与えて "結果" を得る事が出来る。
すなわち $f$ と $a$ から $f(a)$ を得るような操作を圏論的に一般化したものである。

### 指数対象の定義

{{% definition title="指数対象" %}}
有限積を持つ圏 $\mathcal{C}$ において関手
$$ \mathcal{C}(-\times a, b):\mathcal{C}\rightarrow\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}$$
が表現可能であるならば、これを表現する対象を **指数対象(exponential object)** といい $b^a$ と書く。また普遍要素を **評価射(evaluation map)** といい $\epsilon:b^a\times a\rightarrow b$ と書く。
{{% /definition %}}

これを{{< refer prop.universal-construction >}}を用いて図式を用いた定義に翻訳すると、任意の $f:x\times a\rightarrow b$ に対して
$$ f = \mathcal{C}(u\times a, b)(\epsilon) = (-\circ (u\times 1_a))(\epsilon) = \epsilon \circ (u\times 1_a) $$
となるような $u: x\rightarrow b^a$ が一意に存在する、と言う事が指数対象の持つ普遍性となる。

$$\xymatrix{
x\times a \ar[d]\_{u\times 1_a} \ar[rd]^f & \\\\
b^a\times a \ar[r]^{\epsilon} & b
}$$

{{% proposition %}}
$\mathbf{Set}$ における指数対象 $b^a$ は $\mathbf{Set}(a,b)$ である。
{{% /proposition %}}
{{% details 証明 %}}
評価射 $\epsilon: B^A\times A\rightarrow B$ を
$$ \epsilon(f, a) = f(a)$$
によって定める。任意の $g:X\times A\rightarrow B$ について $u:X\rightarrow B^A$ が
指数対象の図式の可換性を満たすとすると、任意の $(x,a)\in X\times A$ について
$$ \epsilon\circ (u\times 1_a)(x, a) = g(x, a) \Leftrightarrow u(x)(a) = g(x, a)$$
であるから、これが成立する$ u(x) = (a\mapsto g(x, a))$が唯一つ存在する。
$\square$
{{% /details %}}

### 指数対象の性質

指数対象が $a^b$ と書かれるのは指数法則と類似した性質を満たす為である。

{{% proposition %}}
$$ (a^b)^c \simeq a^{b\times c} $$
{{% /proposition %}}
{{% details 証明 %}}
$$ \mathcal{C}(x,(a^b)^c)\simeq\mathcal{C}(x\times c, a^b)\simeq\mathcal{C}((x\times c)\times b, a)\simeq\mathcal{C}(x\times (b\times c), a)\simeq\mathcal{C}(x, a^{b\times c}) $$
と米田の原理より。 $\square$
{{% /details %}}

{{% proposition %}}
$$ (a\times b)^c \simeq a^c\times b^c$$
{{% /proposition %}}
{{% details 証明 %}}
{{< refer prop.yoneda-preserves-limits-examples >}} を用いて
$$\begin{align\*}
\mathcal{C}(x, (a\times b)^c) &\simeq \mathcal{C}(x\times c, a\times b) \\\\
                              &\simeq \mathcal{C}(x\times c, a)\times\mathcal{C}(x\times c, b) \\\\
                              &\simeq \mathcal{C}(x, a^c)\times\mathcal{C}(x, b^c) \\\\
                              &\simeq \mathcal{C}(x, a^c\times b^c)
\end{align\*}$$
と米田の原理より。 $\square$
{{% /details %}}

{{% proposition %}}
$$ 1^a\simeq 1$$
{{% /proposition %}}
{{% details 証明 %}}
$$\mathcal{C}(x, 1^a)\simeq\mathcal{C}(x\times a, 1)\simeq\mathcal{C}(x, 1)$$
と米田の原理より。2つ目の同型は $1$ が終対象であることより。 $\square$
{{% /details %}}

余積 $0$ や $a+b$ に関する指数法則は一般に成立しないが、**分配圏** においてはこれらも成立する。

{{% definition title="分配圏" %}}
任意の有限積と有限余積を持つ圏 $\mathcal{C}$ の、任意の $a,b,c\in\mathcal{C}$ について **標準射(canonical map)**
$$ a\times b + a\times c \rightarrow a\times (b + c) $$
が同型射である時、この圏は **分配圏(distributive category)** であるという。

ここで標準射とは、標準射影・標準入射から構成される唯一の射であり、この場合は以下の図式より $[1_a\times i_b, 1_a\times i_c]$ のことである。
$$\xymatrix{
          & a\times (b+c) &          \\\\
a\times b \ar[ru]^-{1_a\times i_b} \ar[r]^-{i\_{a\times b}} & a\times b + a\times c \ar[u]& a\times c \ar[l]\_-{i\_{a\times c}} \ar[lu]\_-{1_a\times i_c}
}$$
{{% /definition %}}

{{% proposition %}}
分配圏では、任意の対象 $a\in\mathcal{C}$ について $a\times 0\simeq 0$
{{% /proposition %}}
{{% details 証明 %}}
任意の $x\in\mathcal{C}$ に対して射 $a\times 0\rightarrow x$ が唯一つ存在することを示せば良い。ここで $a\times 0\xrightarrow{\pi_0} 0 \xrightarrow{!} x$ が存在するので射が0本ということはない。

ここで、分配圏であるから同型
$$ r: a\times 0 + a\times 0 \rightarrow a \times (0+0) \rightarrow a\times 0$$
が存在する。そこで以下の図式を考えると、標準入射 $i_1,i_2:a\times 0\rightarrow a\times 0 + a\times 0$ は共に $r^{-1}$ と一致する事が分かる。

$$\xymatrix{
          & a\times 0 \ar@<-2pt>[d]\_{r^{-1}} \ar@<2pt>@{<-}[d]^r&          \\\\
a\times 0 \ar[ru]^-{1\_{a\times 0}} \ar[r]^-{i_1} & a\times 0 + a\times 0 & a\times 0 \ar[l]\_-{i_2} \ar[lu]\_-{1\_{a\times 0}}
}$$

続いて、任意の対象 $x\in\mathcal{C}$ について射 $f,g: a\times 0\rightarrow x$ が存在したとし、以下の図式を考えると $ f = [f,g]\circ r^{-1} = g$ である。

$$\xymatrix{
          & x \ar@<2pt>@{<-}[d]^-{[f,g]} &          \\\\
a\times 0 \ar[ru]^-{f} \ar@<2pt>[r]^-{r^{-1}} \ar@<-2pt>@{<-}[r]\_-{r} & a\times 0 + a\times 0 & a\times 0 \ar@<2pt>@{<-}[l]^-{r^{-1}} \ar@<-2pt>[l]\_-{r} \ar[lu]\_-{g}
}$$

以上より射 $a\times 0\rightarrow x$ は唯一つしか存在しないので $a\times 0$ は始対象である。そして始対象は全て同型であるから $a\times 0\simeq 0$ である。 $\square$
{{% /details %}}

{{% proposition %}}
分配圏では $a^{b+c}\simeq a^b \times a^c$
{{% /proposition %}}
{{% details 証明 %}}
$x$ について自然な同型
$$\begin{align\*}
&\mathcal{C}(x, a^{b+c})\simeq\mathcal{C}(x\times(b+c), a)\simeq\mathcal{C}(x\times b + x\times c, a)\simeq\mathcal{C}(x\times b, a)\times\mathcal{C}(x\times c, a)\\\\
&\simeq\mathcal{C}(x, a^b)\times\mathcal{C}(x,a^c)\simeq\mathcal{C}(x,a^b\times a^c)
\end{align\*}$$
が存在するので米田の原理より $a^{b+c}\simeq a^b\times a^c$ $\square$
{{% /details %}}

{{% proposition %}}
分配圏では $a^0\simeq 1$
{{% /proposition %}}
{{% details 証明 %}}
任意の $x\in\mathcal{C}$ について同型
$$\mathcal{C}(x, a^0) \simeq \mathcal{C}(x\times 0, a) \simeq \mathcal{C}(0, a)$$
が存在するが、$0$が始対象であることから最右辺の要素数は1である。したがって射 $x\rightarrow a^0$ も唯一つしか存在しない為 $a^0$ は終対象である。したがって $a^0\simeq 1$ $\square$
{{% /details %}}

### カルテシアン閉圏

{{% definition title="カルテシアン閉圏" %}}
任意の有限積と指数対象を持つ圏を **カルテシアン閉圏(cartesian closed category)** もしくは **デカルト閉圏** という。
{{% /definition %}}

カルテシアン閉圏は集合のような対象と、それらの間の写像のようなものが一つの圏の中に同居しているものである。例えば $\mathbf{Set}$ や $\mathbf{Cat}$ はカルテシアン閉圏である。
また、論理学における **含意(implication)** $P\Rightarrow Q$ も指数対象で表す事ができ、カルテシアン閉圏が主要な舞台となる。

{{% theorem label="prop.ccc-is-distributive" %}}
任意の有限余積を持つカルテシアン閉圏は分配圏である。
{{% /theorem %}}
{{% details 証明 %}}
任意の $x\in\mathcal{C}$ について自然な同型
$$\begin{align\*}
&\mathcal{C}(a\times b+a\times c, x)
\simeq \mathcal{C}(a\times b, x)\times\mathcal{C}(a\times c, x)
\simeq \mathcal{C}(b, x^a) \times \mathcal{C}(c, x^a) \\\\
& \simeq \mathcal{C}(b+c, x^a)
\simeq \mathcal{C}(a\times(b+c), x)
\end{align\*}$$
が存在するので米田の原理より $a\times b+a\times c\simeq a\times(b+c)$ である。 $\square$
{{% /details %}}

## 随伴
**随伴(adjunction)** は2つの関手の間の関係であるが、

> "Adjoint functors arise everywhere”
> (S. Mac Lane, Categories for the working mathematician)

とマクレーンが言っているように、数学の様々な場所で普遍的に現れる重要な概念である。

### 随伴の定義

{{% definition title="随伴" label="def.adjunction" %}}
圏 $\mathcal{C}$ と $\mathcal{D}$ の間の **随伴(adjunction)** とは、
関手 $F:\mathcal{C}\rightarrow\mathcal{D}$ と $G:\mathcal{D}\rightarrow\mathcal{C}$ の対であり、以下の2つの関手 $\mathcal{C}^{\mathrm{op}}\times\mathcal{D}\rightarrow\mathbf{Set}$ の間の自然同型

$$ \phi: \mathcal{D}(F(-), -)\longrightarrow\mathcal{C}(-,G(-)) $$

が存在するものをいう。言い換えれば、 任意の $a\in\mathcal{C},b\in\mathcal{D}$ に対して全単射
$$ \mathcal{D}(F(a), b)\simeq\mathcal{C}(a,G(b)) $$
が存在し、これが $a,b$ について自然となるものをいう。

この時 $F$ を $G$ の**左随伴(left adjoint)**、 $G$ を$F$ の **右随伴(right adjoint)** といい、 $F\dashv G$ と書く。以下のような図式で表現することもある。

$$\xymatrix{
\mathcal{C} \ar@/^4pt/[r]^{F}\_{}=\"x\" & \mathcal{D} \ar@/^4pt/[l]^{G}\_{}=\"y\"
\ar@{}|{\perp} \"x\";\"y\"
}$$
{{% /definition %}}

$$ \phi\_{a,b}: \mathcal{D}(F(a), b)\simeq \mathcal{C}(a,G(b)) $$

が $a,b$ について自然であるというのは、任意の $f:a'\rightarrow a, g:b\rightarrow b'$ について

$$ \xymatrix{
\mathcal{D}(F(a), b)   \ar[r]^{\phi\_{a,b}} \ar[d]\_{\mathcal{D}(F(f), g)} & \mathcal{C}(a, G(b)) \ar[d]^{\mathcal{C}(f, G(g))} \\\\
\mathcal{D}(F(a'), b') \ar[r]^{\phi\_{a',b'}} & \mathcal{C}(a', G(b'))
} $$

が成り立つことであるので、component-wiseに書けば、任意の $h: F(a)\rightarrow b$ について
$$ \phi\_{a',b'}(g\circ h\circ F(f)) = G(g)\circ \phi\_{a,b}(h)\circ f $$
が成り立つということである。ただ、これだと煩雑すぎるので $\phi(h),\phi^{-1}(h)$ を $\bar{h}$ という風に書くと(もちろん $\bar{\bar{h}}=h$である)、

$$ \overline{g\circ h\circ F(f)} = G(g)\circ\bar{h}\circ f $$

と分かりやすくなる。もしくは、任意の $h: a\rightarrow G(b)$ について

$$ \overline{G(g)\circ h\circ f} = g\circ\bar{h}\circ F(f) $$

であると書いても同じことである。以後この記法を用いる。
また、対象を明示して以下のような書き方をする場合もある。

$$ \overline{F(a') \xrightarrow{F(f)} F(a) \xrightarrow{h} b \xrightarrow{g} b'} = a' \xrightarrow{f} a \xrightarrow{\bar{h}} G(b) \xrightarrow{G(g)} G(b') $$

{{% definition title="単位射・余単位射" label="def.unit" %}}
随伴 $F\dashv G$ が存在する時、以下の全単射において左辺の単位元 $1\_{F(a)}$ に対応する右辺の射 $\eta_a: a\rightarrow GF(a)$ の族が定める自然変換
$\eta: 1\_{\mathcal{C}}\rightarrow GF$ をこの随伴の **単位射(unit)** という。
$$ \mathcal{D}(F(a), F(a))\simeq \mathcal{C}(a,GF(a)) $$

同様に、以下の全単射において右辺の単位元 $1\_{G(b)}$ に対応する左辺の射 $\epsilon_b: FG(b)\rightarrow b$ の族が定める自然変換 $\epsilon: FG\rightarrow 1\_{\mathcal{D}}$ を **余単位射(counit)** という。
$$ \mathcal{D}(FG(b), b)\simeq\mathcal{C}(G(b),G(b)) $$
{{% /definition %}}

つまり、具体的に書けば
$$ \eta_a = \overline{1\_{F(a)}},\quad \epsilon_b = \overline{1\_{G(b)}} $$
である。

### 三角等式

{{% theorem label="prop.triangle" %}}
関手 $F:\mathcal{C}\rightarrow\mathcal{D}$ と $G:\mathcal{D}\rightarrow\mathcal{C}$ が随伴 $F\dashv G$ であることは、自然変換 $\eta: 1\_{\mathcal{D}}\rightarrow GF$ と $\epsilon: FG\rightarrow 1\_{\mathcal{D}}$ が存在して、以下の図式(**三角等式(triangle identities)**) が可換となることと同値。

$$\xymatrix{
F \ar[r]^{F\eta} \ar[rd]\_{1_F} & FGF \ar[d]^{\epsilon F} & G \ar[r]^{\eta G} \ar[rd]\_{1_G} & GFG \ar[d]^{G \epsilon} \\\\
                                          & F                       &                                            & G
}$$

{{% /theorem %}}
{{% details 証明 %}}
({{< refn def.adjunction >}}, {{< refn def.unit >}} $\Rightarrow$ {{< refer prop.triangle >}}の三角等式)
$F:\mathcal{C}\rightarrow\mathcal{D}, G:\mathcal{D}\rightarrow\mathcal{C}$ の間に随伴関係があるとする。また、 $\eta,\epsilon $ を単位射、余単位射とする。

任意の $a\in\mathcal{C}$ について

$$\begin{align*}
\overline{F(a) \xrightarrow{F(\eta_a)} FGF(a) \xrightarrow{\epsilon\_{F(a)}} F(a)} &= a\xrightarrow{\eta_a} GF(a) \xrightarrow{\overline{\epsilon\_{F(a)}}} GF(a) \\\\
 &= a\xrightarrow{\eta_a} GF(a) \xrightarrow{1\_{GF(a)}} GF(a) \\\\
 &= a\xrightarrow{\eta_a} GF(a) \\\\
 &= \overline{F(a)\xrightarrow{1\_{F(a)}}F(a)}
\end{align*}$$

であるので $\epsilon\_{F(a)}\circ F(\eta_a) = 1\_{F(a)}$ すなわち $\epsilon F\circ F\eta = 1_F$ である。

同様に任意の $b\in\mathcal{D}$ について
$$\begin{align*}
\overline{G(b)\xrightarrow{\eta\_{G(b)}} GFG(b)\xrightarrow{G(\epsilon_b)} G(b)} &= FG(b)\xrightarrow{\overline{\eta\_{G(b)}}} FG(b)\xrightarrow{\epsilon_b} b \\\\
&= FG(b)\xrightarrow{1\_{FG(b)}} FG(b)\xrightarrow{\epsilon_b} b \\\\
&= FG(b)\xrightarrow{\epsilon_b} b \\\\
&= \overline{G(b)\xrightarrow{1\_{G(b)}}G(b)}
\end{align*}$$

であるので $G\epsilon\circ\eta G=1\_{G}$である。

({{< refer prop.triangle >}}の三角等式 $\Rightarrow$ {{< refn def.adjunction >}}, {{< refn def.unit >}})

$\epsilon F\circ F\eta = 1_F,\quad G\epsilon\circ\eta G=1\_{G}$であるとする。
すなわち、以下が成立

$$ F(a) \xrightarrow{F(\eta_a)} FGF(a) \xrightarrow{\epsilon\_{F(a)}} F(a) = F(a)\xrightarrow{1\_{F(a)}}F(a) \qquad (a\in\mathcal{C})\qquad\cdots(A)$$
$$ G(a)\xrightarrow{\eta\_{G(a)}} GFG(a)\xrightarrow{G(\epsilon_a)} G(a) = G(a)\xrightarrow{1\_{G(a)}}G(a)\qquad (a\in\mathcal{D})\qquad\cdots(B)$$

また、$\eta, \epsilon$ は自然変換であるから、以下が成立。

$$ a\xrightarrow{f}b \xrightarrow{\eta_b}GF(b) = a\xrightarrow{\eta_a}GF(a)\xrightarrow{GF(f)} GF(b)\qquad (f:a\rightarrow b \in\mathcal{C})\qquad\cdots(C)$$
$$ FG(a)\xrightarrow{\epsilon_a}a\xrightarrow{f}b = FG(a)\xrightarrow{FG(f)}FG(b)\xrightarrow{\epsilon_b}b \qquad(f:a\rightarrow b \in\mathcal{D})\qquad\cdots(D)$$

ここで写像 $\phi:\mathcal{D}(F(a),b)\leftrightarrow \mathcal{D}(a, G(b)):\psi$ を以下のように置く

$$ \phi(F(a)\xrightarrow{h}b) = a\xrightarrow{\eta_a}GF(a)\xrightarrow{G(h)}G(b) $$
$$ \psi(a\xrightarrow{h}G(b)) = F(a)\xrightarrow{F(h)}FG(b)\xrightarrow{\epsilon_b}b $$

すると
$$\begin{align\*}
\psi\circ\phi(F(a)\xrightarrow{h}b) &= F(a)\xrightarrow{F(\eta_a)}FGF(a)\xrightarrow{FG(h)}FG(b)\xrightarrow{\epsilon_b}b \\\\
&= F(a)\xrightarrow{F(\eta_a)}FGF(a)\xrightarrow{\epsilon\_{F(a)}}F(a)\xrightarrow{h} b \qquad(\because D)\\\\
&= F(a)\xrightarrow{1\_{F(a)}} F(a)\xrightarrow{h} b \qquad(\because A)\\\\
&= F(a)\xrightarrow{h} b
\end{align\*}$$
同様に
$$\begin{align\*}
\phi\circ\psi(a\xrightarrow{h}G(b)) &= a\xrightarrow{\eta_a}GF(a)\xrightarrow{GF(h)}GFG(b)\xrightarrow{G(\epsilon_b)} G(b) \\\\
&= a\xrightarrow{h}G(b)\xrightarrow{\eta\_{G(b)}}GFG(b)\xrightarrow{G(\epsilon_b)} G(b) \qquad(\because C)\\\\
&= a\xrightarrow{h}G(b)\xrightarrow{1\_{G(b)}} G(b) \\\\
&= a\xrightarrow{h}G(b)
\end{align\*}$$
であるから $\phi,\psi$ は全単射 $\mathcal{D}(F(a),b)\leftrightarrows\mathcal{D}(a, G(b))$ である。以後$\phi(h),\psi(h)$ を $\bar{h}$ と書く。

任意の $f:a'\rightarrow a, g:b\rightarrow b',h: F(a)\rightarrow b$ について

$$\begin{align\*}
\overline{F(a') \xrightarrow{F(f)} F(a) \xrightarrow{h} b \xrightarrow{g} b'}
&= a'\xrightarrow{\eta\_{a'}}GF(a') \xrightarrow{GF(f)} GF(a) \xrightarrow{G(h)} G(b) \xrightarrow{G(g)} G(b') \\\\
&= a'\xrightarrow{f}a\xrightarrow{\eta_a}GF(a)\xrightarrow{G(h)} G(b) \xrightarrow{G(g)} G(b') \qquad(\because C)\\\\
&= a'\xrightarrow{f}a\xrightarrow{G(h)\circ \eta_a}G(b)\xrightarrow{G(g)}G(b')\\\\
&= a'\xrightarrow{f}a\xrightarrow{\bar{h}}G(b)\xrightarrow{G(g)}G(b')
\end{align\*}$$

であるから、この全単射は $a,b$ について自然である。また $\phi,\psi$ の定義より
$$\eta_a = \overline{1\_{F(a)}}, \epsilon_b = \overline{1\_{G(b)}}$$
である。$\square$
{{% /details %}}

今の証明より以下が分かる。
{{% proposition %}}
随伴 $F\dashv G$ の単位射が $\eta$ 、余単位射が $\epsilon$ であるときの全単射
$ \phi: \mathcal{D}(F(a), b)\rightarrow\mathcal{C}(a,G(b)) $
は
$$ \phi(f) = G(f)\circ\eta_a,\quad \phi^{-1}(f) = \epsilon_b \circ F(f)$$
で与えられる。
{{% /proposition %}}

{{% proposition %}}
ある関手の右随伴が存在するならば、それは自然同型を除いて一意に定まる。
左随伴についても同様。
{{% /proposition %}}
{{% details 証明 %}}
関手 $F:\mathcal{C}\rightarrow\mathcal{D}$ と $G,G':\mathcal{D}\rightarrow\mathcal{C}$ の間に
随伴 $F\dashv G$ と $F\dashv G'$ の関係があるとする。すなわち任意の $a\in\mathcal{C},b\in\mathcal{D}$ について自然な同型
$$ \mathcal{D}(F(a), b)\simeq\mathcal{C}(a,G(b)) $$
$$ \mathcal{D}(F(a), b)\simeq\mathcal{C}(a,G'(b)) $$
が存在するので、自然な同型
$$ \mathcal{C}(a,G(b))\simeq \mathcal{C}(a,G'(b)) $$
が得られる。これが $a$ について自然であるので
$$ \mathcal{C}(-,G(b))\simeq \mathcal{C}(-,G'(b)) $$
であるから、米田の原理より
$$ G(b)\simeq G'(b) $$
となる。これが $b$ について自然であることから
$$ G\simeq G' $$
となる。従って、$F$ の右随伴は同型を除いて一意である。

左随伴についても、米田埋め込みの双対版を考えることで同様に示せる。$\square$
{{% /details %}}

### 随伴の例

{{% example title="極限と対角関手" %}}
$F:J\rightarrow\mathcal{C}$ の極限が全て存在する時
$$ \Delta \dashv \varprojlim $$
である。同様に余極限が全て存在する時
$$ \varinjlim \dashv \Delta $$
である。
{{% /example %}}

$ \Delta \dashv \varprojlim $に関する射の対応は以下のようになっている。$a$ から $F$ への錐と、任意の錐に対して一意に存在する射 $a\rightarrow\varprojlim F$ が対応している。

$$\begin{array}{rcccl}
\Delta(a) & \rightarrow & F \\\\ \hline
a & \rightarrow & \varprojlim F
\end{array}
$$

また、この時の単位射 $a\rightarrow\varprojlim\Delta(a)$ は恒等射 $1_a$ であり、余単位射 $\Delta(\varprojlim F)\rightarrow F$ は極限錐である。


