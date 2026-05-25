---
title: 圏論II
weight: 4
section: 3
toc: true
---

## 普遍性

本節では圏論において非常に重要な概念である **普遍性(universal property)** と関連する諸概念について説明する。普遍性を用いると、圏論の様々な概念を統一的な方法で構成する事ができる。前節で説明した極限も普遍性を用いた構成(**普遍的構成(universal construction)**)の一つである。

普遍性の説明には複数の方法があるが、ここではエミリー・リール(Emily Riehl)による **表現可能関手(representable functor)** を用いた説明を行う。

### Hom関手
圏論の語彙では、対象や射が具体的に何であるか(例えばベクトル空間や線型写像であるといったこと)を特定し、その性質(例えばベクトル空間の公理)を用いて議論を行う事が基本的には出来ない。従って、圏論においてある対象 $a\in\mathcal{C}$ について調べる時には $a$に向かう射の集合 $\mathcal{C}(x, a)$や、 $a$ から出る射の集合 $\mathcal{C}(a, x)$ について調べる事が主要な手段となる。そこで **Hom関手(hom-functor)** という概念が登場する。

$\mathcal{C}$ を局所小圏とすると、任意の $a,x\in\mathcal{C}$ について $\mathcal{C}(a, x)$ は集合になる。
すなわち $\mathbf{Set}$ の対象になるので、$x\longmapsto \mathcal{C}(a, x)$ という $\mathcal{C}$ から $\mathbf{Set}$ への対象の対応を得ることができる。このとき、射 $f:x\rightarrow y$ に対応する$\mathbf{Set}$ の射 $\mathcal{C}(a, f): \mathcal{C}(a, x)\rightarrow\mathcal{C}(a, y)$ も定める事ができて、この対応は関手となる。

{{% definition title="共変Hom関手" %}}
局所小圏 $\mathcal{C}$ と対象 $a\in\mathcal{C}$ に対して、 $x\in\mathcal{C}$ を $\mathcal{C}(a, x)$ に移し, $f: x\rightarrow y$ を
$$\mathcal{C}(a, f): \mathcal{C}(a,x) \ni g \mapsto f\circ g \in\mathcal{C}(a,y)$$
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
$$ \mathcal{C}(a,1_x): f\longmapsto 1_x\circ f = f$$
であるから $ \mathcal{C}(a,1_x) = 1_{\mathcal{C}(a,x)} $
また、任意の $f: x\rightarrow y, g:y\rightarrow z$ と $p:a\rightarrow x$ について
$$ (\mathcal{C}(a,g)\circ\mathcal{C}(a,f))(p) = g\circ(f\circ p) = (g\circ f)\circ p = \mathcal{C}(a,g\circ f)(p) $$
$\square$
{{% /details %}}

{{% definition title="反変Hom関手" %}}
局所小圏 $\mathcal{C}$ と対象 $a\in\mathcal{C}$ に対して、 $x\in\mathcal{C}$ を $\mathcal{C}(x, a)$ に移し、 $f: x\rightarrow y$ を
$$\mathcal{C}(f, a): \mathcal{C}(y,a) \ni g \mapsto g\circ f \in\mathcal{C}(x,a)$$
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
$$ F\cong\mathcal{C}(-, a) $$
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

以上は非常にシンプルな例であるが、$a\in\mathcal{C}$ と表現可能関手 $\mathcal{C}(-, a)$ が、その周囲の射も含め綺麗に対応している事が分かるであろう。誤解を恐れずに言えば $a$ と $\mathcal{C}(-, a)$ は同じものの異なる表現であると言える。

### 表現可能関手と極限

極限は表現可能関手によって定める事ができる。

{{% proposition %}}
圏 $\mathcal{C}$ の終対象 $1$ は、定数関手 $\\{\ast\\}: \mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ を表現する。すなわち
$$ \\{\ast\\} \cong \mathcal{C}(-, 1) $$
同様に、始対象 $0$ は、定数関手 $\\{\ast\\}: \mathcal{C}\rightarrow\mathbf{Set}$ を表現する。すなわち
$$ \\{\ast\\}\cong\mathcal{C}(0, -)$$
{{% /proposition %}}

任意の $x\in\mathcal{C}$ に対して $\mathcal{C}(x, 1), \mathcal{C}(0, x)$ が一点集合であるということであり、終対象・始対象の定義と一致することがわかる。

{{% proposition %}}
圏 $\mathcal{C}$ の積 $a\times b$ は、関手 $\mathcal{C}(-, a)\times\mathcal{C}(-, b): \mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ を表現する。すなわち
$$ \mathcal{C}(-, a)\times\mathcal{C}(-, b) \cong \mathcal{C}(-, a\times b)$$
同様に、余積 $a+b$ は、関手 $\mathcal{C}(a, -)\times\mathcal{C}(b, -): \mathcal{C}\rightarrow\mathbf{Set}$ を表現する。すなわち
$$ \mathcal{C}(a, -)\times\mathcal{C}(b, -) \cong \mathcal{C}(a+b, -)$$
{{% /proposition %}}

積の定義より、任意の $x\in\mathcal{C}$ に対して 射の組 $(f, g) \in \mathcal{C}(x, a)\times\mathcal{C}(x, b)$ と、射 $\langle f, g\rangle \in \mathcal{C}(x, a\times b)$ が一対一に対応するので
$$ \mathcal{C}(x, a)\times\mathcal{C}(x, b) \cong \mathcal{C}(x, a\times b)$$
である事がわかる。さらに $\langle f,g\rangle $の一意性より、任意の $h:x\rightarrow y$ に対して $\langle f\circ h, g\circ h\rangle = \langle f, g\rangle\circ h$ が成り立つので以下が可換となる。
$$ \xymatrix{
\mathcal{C}(y,a)\times\mathcal{C}(y, b) \ar[d]^{(-\circ h)\times (-\circ h)} \ar[r] & \mathcal{C}(y, a\times b) \ar[d]^{-\circ h}\\\\
\mathcal{C}(x,a)\times\mathcal{C}(x, b) \ar[r] & \mathcal{C}(x, a\times b)
}$$
よって以下が自然同型である事がわかる。
$$ \mathcal{C}(-, a)\times\mathcal{C}(-, b) \cong \mathcal{C}(-, a\times b)$$
以上を一般化すると以下の定理を得る。

{{% theorem %}}
図式 $F: \mathcal{J}\rightarrow\mathcal{C}$ の極限が存在する時
$$ \varprojlim\_{i\in\mathcal{J}}\mathcal{C}(-, F(i))\cong\mathcal{C}(-, \varprojlim F)$$
である。また、余極限が存在する時
$$ \varprojlim\_{i\in\mathcal{J}}\mathcal{C}(F(i), -)\cong\mathcal{C}(\varinjlim F, -)$$
である。
{{% /theorem %}}
{{% details 証明 %}}
極限について示す。 {{< refer th.limits-of-functor-categories >}} と {{< refer th.existence-of-limits >}} より、任意の $x\in\mathcal{C}$ に対して
$$ \left(\varprojlim\_{i\in\mathcal{J}}\mathcal{C}(-, F(i))\right)(x) \cong \varprojlim\_{i\in\mathcal{J}}\mathcal{C}(x, F(i)) 
\cong \\{ (\phi\_i: x\rightarrow F(i))\_{i\in\mathcal{J}} \mid \forall (f:i\rightarrow j)\in\mathcal{J},F(f)\circ\phi\_i=\phi\_j  \\}
$$
であり、この右辺は $x$ から $F$ への錐全体の集合 $\mathcal{C}^{\mathcal{J}}(x, F)$ と同型である。従って、自然同型
$$ \varprojlim\_{i\in\mathcal{J}}\mathcal{C}(-, F(i)) \cong \mathcal{C}^{\mathcal{J}}(-, F) $$
を得る。あとは、自然同型
$$ \mathcal{C}^{\mathcal{J}}(-, F) \cong \mathcal{C}(-, \varprojlim F)$$
を示せばよい。まず、任意の $x$ について、錐 $x\rightarrow F$ と射 $x\rightarrow\varprojlim F$ は一対一に対応するので
$$ \mathcal{C}^{\mathcal{J}}(x, F) \cong \mathcal{C}(x, \varprojlim F)$$
そして、任意の $f:x\rightarrow y$ について以下の図式を考えると、錐の各側面に $f$ を合成して得られる錐と頂点に $f$ を合成して得られる錐は同一であるからこれは可換であるから、この同型は $x$ について自然である。
$$ \xymatrix{
\mathcal{C}^{\mathcal{J}}(y, F) \ar[r] \ar[d]^{-\circ f} & \mathcal{C}(y, \varprojlim F) \ar[d]^{-\circ f} \\\\
\mathcal{C}^{\mathcal{J}}(x, F) \ar[r] & \mathcal{C}(x, \varprojlim F)
}$$

余極限は双対圏における極限であるので、 $\mathcal{C}^{\mathrm{op}}$ において上記の議論を適用すれば良い。 $\square$
{{% /details %}}

### 米田埋め込み・米田の補題

表現可能関手の定義では自然変換 $\mathcal{C}(-, a)\rightarrow F$ や $\mathcal{C}(a, -)\rightarrow F$ が使われるが、これらに関する非常に重要な定理が **米田の補題(Yoneda's Lemma)** である。
Emily Riehlによれば米田の補題は"圏論の最も重要な成果"である。

{{% definition title="米田埋め込み" %}}
局所小圏 $\mathcal{C}$ について、関手 $\mathcal{Y}:\mathcal{C}\rightarrow\hat{\mathcal{C}}$ を
$$ \mathcal{Y}(a) = \mathcal{C}(-, a) $$
$$ \mathcal{Y}(f) = f\circ -$$
にて定めたものを **米田埋め込み(Yoneda embedding)** という。
{{% /definition %}}

$\mathcal{Y}$ の関手性は明らかである。$\mathcal{C}$ を $\mathcal{C}^{\mathrm{op}}$ に置き換えることで、この双対版も同様に考える事ができる。
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

反変関手 $\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ を **前層(presheaf)** とも呼ぶと既に述べたが、米田埋め込みは圏 $\mathcal{C}$ を前層の圏 $\hat{\mathcal{C}}$ に埋め込む操作であると言うこともできる。前層の圏については次章で詳しく説明するがとても良い性質をもった圏である。

{{% theorem title="米田の補題" %}}
局所小圏 $\mathcal{C}$ と関手 $F:\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ 、$a\in\mathcal{C}$ について $a,F$ について自然な同型
$$ \hat{\mathcal{C}}(\mathcal{Y}(a),F)\cong F(a) \qquad (\alpha\mapsto\alpha_a(1_a))$$
が成り立つ。
{{% /theorem %}}

米田の補題の同型が $a$ について自然であるというのは、任意の $f:b\rightarrow a$ について以下が可換である事であり、

$$\xymatrix{
\hat{\mathcal{C}}(\mathcal{Y}(a), F) \ar[r]^(.6){\cong}  \ar[d]\_{\hat{\mathcal{C}}(\mathcal{Y}(f), F)} & F(a) \ar[d]^{F(f)} \\\\
\hat{\mathcal{C}}(\mathcal{Y}(b), F) \ar[r]^(.6){\cong} & F(b)
}$$

$F$ について自然であるというのは、任意の $\rho:F\rightarrow G$ について以下が可換となる事である。

$$\xymatrix{
\hat{\mathcal{C}}(\mathcal{Y}(a), F) \ar[r]^(.6){\cong}  \ar[d]\_{\hat{\mathcal{C}}(\mathcal{Y}(a), \rho)} & F(a) \ar[d]^{\rho_a} \\\\
\hat{\mathcal{C}}(\mathcal{Y}(a), G) \ar[r]^(.6){\cong} & G(a)
}$$

証明に入る前に、具体例を考えてみよう。まず、$\mathcal{C}$ が自然数の集合 $\mathbb{N}$ である場合を考えると、
自然変換 $\mathbf{Set}^{\mathbb{N}^{\mathrm{op}}}(\mathcal{Y}(a),F)$ は、以下の縦の射の族である。ここで$0$ は空集合、 $1$ は単集合である。

$$\xymatrix{
0 \ar[d] & \cdots & 0 \ar[d] & 1 \ar[d] & 0 \ar[d] & \cdots \\\\
F(0)     & \cdots & F(a-1)   & F(a)     & F(a+1) & \cdots
}$$

この自然変換がいくつあるかというと、$0\rightarrow F(x)$ は空関数しかあり得ないので一意に定まり、 $1\rightarrow F(a)$ は $F(a)$ の要素数だけ存在する。
従って $\mathbf{Set}^{\mathbb{N}^{\mathrm{op}}}(\mathcal{Y}(a), F)\cong F(a)$  である。

$\mathbb{N}$ が順序集合の場合も考えよう。この場合の自然変換は以下の図式の縦の射の族となる。

$$\xymatrix{
1 \ar[d]^{\alpha_0} \ar@{<-}[r] & \cdots \ar@{<-}[r] & 1 \ar[d]^{\alpha\_{a-1}}\ar@{<-}[r] & 1 \ar[d]^{\alpha\_a}\ar@{<-}[r] & 0 \ar[d]^{\alpha\_{a+1}}\ar@{<-}[r] & \cdots \\\\
F(0) \ar@{<-}[r]    & \cdots \ar@{<-}[r] & F(a-1) \ar@{<-}[r]  & F(a) \ar@{<-}[r]    & F(a+1) \ar@{<-}[r] & \cdots
}$$
すると、先ほどと同様にして $\alpha\_{a+1}$ より右側は全て空関数となり、 $\alpha_a$ は $F(a)$ の要素数だけ存在する。そして、 $\alpha_0,\ldots,\alpha\_{a-1}$ は図式の可換性から $\alpha_a$ が定まれば自動的に決まる。
従って、この場合も自然変換は $F(a)$ の要素数だけ存在し $\mathbf{Set}^{\mathbb{N}^{\mathrm{op}}}(\mathcal{Y}(a), F)\cong F(a)$ となる。また、この全単射が $\alpha\mapsto\alpha_a(1_a)$ で与えられることもわかるであろう。また、この例から $F(a)$ の要素が自然変換 $\mathcal{Y}(a)\rightarrow F$ 全体を**生成する** ことが分かる。

一般の場合も同様で、任意の対象 $x\in\mathcal{C}$ について、射 $x\rightarrow a$ が存在しない時には、$\mathcal{C}(x, a)=\emptyset$ であるので、自然変換 $\mathcal{Y}(a)\rightarrow F$ の$x$コンポーネントは空関数に一意に定まる。射 $x\rightarrow a$ が存在する時には、射 $\mathcal{C}(a,a)\rightarrow\mathcal{C}(x,a)$ が存在するから以下の図式を考えることができて、図式の可換性から $\alpha_a(1_a) \in F(a)$ が決まれば、 $\alpha_x$ が一意に決まる。また、この特別な場合として$x=a$ の場合を考えれば $\alpha_a(1_a)$ が決まれば、 $\alpha_a$ 自身も一意に決まる。従って、 $\alpha_a(1_a) \in F(a)$ が自然変換 $\alpha$ 全体を生成するので、$\hat{\mathcal{C}}(\mathcal{Y}(a),F)\cong F(a)$ となるわけである。

$$\xymatrix{
\mathcal{C}(a, a) \ar[r]\ar[d]^{\alpha_a} & \mathcal{C}(x, a)\ar[d]^{\alpha_x} \\\\
F(a) \ar[r] & F(x)
}$$


{{% details 米田の補題の証明 %}}
$\alpha\in\hat{\mathcal{C}}(\mathcal{Y}(a),F)$ とする。 $\alpha$ は自然変換であるから任意の $f:y\rightarrow x$ について、以下が可換である。

$$\xymatrix{
\mathcal{C}(x, a) \ar[r]^{\alpha_x}  \ar[d]\_{-\circ f} & F(x) \ar[d]^{F(f)} \\\\
\mathcal{C}(y, a) \ar[r]\_{\alpha_y} & F(y)
}$$

すなわち、任意の $h:x\rightarrow a$ に対して
$$ \alpha_y(h\circ f) = F(f)(\alpha_x(h)) $$
である。ここで

$$ \phi\_{a,F}: \hat{\mathcal{C}}(\mathcal{Y}(a),F)\ni\alpha\longmapsto \alpha_a(1_a)\in F(a) $$
$$ \psi\_{a,F}: F(a)\ni x \longmapsto F(-)(x)\in\hat{\mathcal{C}}(\mathcal{Y}(a),F)$$

とおくと

$$\psi\_{a,F}\circ\phi\_{a,F}(\alpha)(h) = F(h)(\alpha_a(1_a)) = \alpha_x(1_a\circ h) = \alpha_x(h)$$
$$\phi\_{a,F}\circ\psi\_{a,F}(x) = F(1_a)(x) = 1\_{F(a)}(x) = x$$

であるので $\phi\_{a,F},\psi\_{a,F}$ は同型写像。

続いて同型の自然性を確認する。任意の$f: b\rightarrow a$ と $\alpha\in\hat{\mathcal{C}}(\mathcal{Y}(a), F)$ について

$$
F(f)(\phi\_{a,F}(\alpha)) = F(f)(\alpha_a(1_a)) = \alpha_b(1_a\circ f) = \alpha_b(f)
$$
$$
\phi\_{b,F}(\alpha\circ \mathcal{Y}(f)) = \phi\_{b,F}(\alpha\circ \mathcal{C}(-, f)) = (\alpha_b\circ\mathcal{C}(b, f))(1_b) = \alpha_b(f\circ 1_b) = \alpha_b(f)
$$

より、
$F(f)(\phi\_{a,F}(\alpha)) = \phi\_{b,F}(\alpha\circ \mathcal{Y}(f)) $ であるから、
$\phi\_{a,F}$ は $a$ について自然。続いて、任意の $\rho:F\rightarrow G$ と $\alpha\in\hat{\mathcal{C}}(\mathcal{Y}(a), F)$ について

$$
\rho_a(\phi\_{a,F}(\alpha)) = \rho_a(\alpha_a(1_a)) = \rho_a\circ\alpha_a(1_a)
$$
$$
\phi\_{a,G}(\rho\circ\alpha) = \rho_a\circ\alpha_a(1_a)
$$

より$\rho_a(\phi\_{a,F}(\alpha)) =\phi\_{a,G}(\rho\circ\alpha)$ であるから $F$ についても自然。 $\square$
{{% /details %}}

### 米田埋め込みの性質

米田埋め込みが"埋め込み"と呼ばれるのに相応しいのは以下の命題より。

{{% proposition %}}
米田埋め込みは忠実充満
{{% /proposition %}}
{{% details 証明 %}}
米田の補題より、任意の $a,b\in\mathcal{C}$ について自然な全単射
$$ \hat{\mathcal{C}}(\mathcal{Y}(a),\mathcal{Y}(b))\cong \mathcal{Y}(b)(a)=\mathcal{C}(a,b) $$
が存在する。 $\square$
{{% /details %}}

従って {{< refer prop.embedding >}} より
$$\mathcal{Y}(a)\cong \mathcal{Y}(b)\Leftrightarrow a\cong b$$
である。 米田埋め込みの双対 $\mathcal{C}(a, -): \mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}^{\mathcal{C}}$ についても全く同様であり、 **米田の原理(Yoneda principle)** と呼ばれる以下の命題を得る。

{{% proposition title="米田の原理" %}}
局所小圏 $\mathcal{C}$ の対象 $a,b$ について
$$a\cong b\ \Leftrightarrow\ \mathcal{C}(-, a)\cong\mathcal{C}(-, b)\ \Leftrightarrow\ \mathcal{C}(a, -)\cong\mathcal{C}(b, -)$$
{{% /proposition %}}

この定理から直ちに以下が示される。

{{% proposition %}}
表現可能関手を表現する対象は同型を除いて一意である。
{{% /proposition %}}

また、既に示した自然同型
$$ \varprojlim\_{i\in\mathcal{J}}\mathcal{C}(-, F(i))\cong\mathcal{C}(-, \varprojlim F)$$
は以下のようにも表現できる。

{{% proposition label="prop.yoneda-preserves-limits" %}}
米田埋め込みは連続である。すなわち自然同型
$$ \mathcal{Y}(\varprojlim F) \cong \varprojlim (\mathcal{Y}\circ F)$$
が存在する。
{{% /proposition %}}

余極限は一般には保たれないので注意。
この命題の具体例をいくつか並べてみると以下のような等式を得る。

{{% proposition label="prop.yoneda-preserves-limits-examples" %}}

$$\begin{align\*}
\mathcal{C}(x, 1) &\cong 1 \\\\
\mathcal{C}(x, a\times b) &\cong \mathcal{C}(x, a)\times\mathcal{C}(x, b) \\\\
\mathcal{C}\left(x, \prod\_{i\in\mathcal{J}} a_i\right) &\cong \prod\_{i\in\mathcal{J}}\mathcal{C}(x, a_i)
\end{align\*}$$
これらの $\mathcal{C}$ を $\mathcal{C}^{\mathrm{op}}$ に置き換えれば以下も成立する。
$$\begin{align\*}
\mathcal{C}(0, x) &\cong 1 \\\\
\mathcal{C}(a+b, x) &\cong \mathcal{C}(a, x)\times\mathcal{C}(b, x) \\\\
\mathcal{C}\left(\coprod\_{i\in\mathcal{J}} a_i, x\right) &\cong \prod\_{i\in\mathcal{J}}\mathcal{C}(a_i, x)
\end{align\*}$$
{{% /proposition %}}

また、これと米田の原理を組み合わせれば様々な圏における極限・余極限の性質の証明が簡単にできる。例えば

{{% proposition %}}
$$\begin{align\*}
a \times 1 &\cong a \\\\
a \times b &\cong b \times a \\\\
a + 0 & \cong a \\\\
a + b &\cong b + a
\end{align\*}$$
{{% /proposition %}}
などである。例えば1つ目は
$$ \mathcal{Y}(a\times 1)(x)\cong \mathcal{C}(x, a\times 1) \cong\mathcal{C}(x, a)\times\mathcal{C}(x, 1)\cong\mathcal{C}(x, a)\times 1\cong\mathcal{C}(x, a)\cong\mathcal{Y}(a)(x)$$
が $x$ に関して自然な同型であることを集合論的に簡単に示すことができ、これから $\mathcal{Y}(a\times 1)\cong\mathcal{Y}(a)$ を得るので、米田の原理より $a\times 1\cong a$ が導かれる。

代数的なアナロジーが自由に使えるわけではないので注意。例えば $a\times 0=0$といった性質は一般には成り立たない。

以上のように $\hat{\mathcal{C}}$ は非常に良い性質を持っているので、米田埋め込みによって一旦議論の舞台を $\mathcal{C}$ から $\hat{\mathcal{C}}$ に移すことで様々な議論が行いやすくなるわけである。

### 普遍性・普遍要素・普遍的構成

米田の補題より、 自然同型 $\mathcal{Y}(a)\cong F$ に対応する要素 $u\in F(a)$ が存在する。これを $F$ の普遍要素という。

{{% definition title="普遍要素" %}}
表現可能関手 $F: \mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ を表現する対象が $a$ である時、米田の補題によって自然同型
$$ \mathcal{Y}(a)\cong F$$
と対応する $u\in F(a)$ を $F$ の **普遍要素(universal element)** という。
{{% /definition %}}

この $u$ を普遍要素と呼ぶ理由を説明する。米田の補題の所で説明したように、 $u$ のみから自然変換 $\mathcal{Y}(a)\rightarrow F$ 全体を生成する事が可能である訳だが、特にこれが自然同型 $\mathcal{Y}(a)\cong F$ の時には $F$ そのものを生成することが出来る。ということは、 $a\in\mathcal{C}$ と $u\in F(a)$ のみから、任意の $x\in\mathcal{C}$ について $F(x)$ の任意の要素を具体的に構成することができる。この性質を $u$ の **普遍性(universal property)** といい、この構成を **普遍的構成(universal construction)** という。

普遍要素 $u$ 及び、普遍的構成について調べる。米田の補題の証明より $\hat{\mathcal{C}}(\mathcal{Y}(a),F)$ と $F(a)$ の同型は

$$ \phi\_{a,F}: \hat{\mathcal{C}}(\mathcal{Y}(a),F)\ni\alpha\longmapsto \alpha_a(1_a)\in F(a) $$
$$ \psi\_{a,F}: F(a)\ni x \longmapsto F(-)(x)\in\hat{\mathcal{C}}(\mathcal{Y}(a),F)$$

によって与えられるので、 $\alpha$ が同型射であるときに、対応する $u=\alpha_a(1_a)$ が普遍要素である。そして、 $\alpha_a$ は $\alpha_a: \mathcal{C}(a, a)\rightarrow F(a)$ という全単射であるので、この左辺の $1_a$ 対応する要素が普遍要素である。そして、
$$ F(-)(u): \mathcal{C}(-, a)\rightarrow F$$
が自然同型 $\mathcal{C}(-, a)\cong F$ の具体的な構成であることも分かる。

{{% proposition title="普遍要素・普遍的構成" %}}
表現可能関手 $\mathcal{C}(-, a)\cong F$ について、同型 $\mathcal{C}(a, a)\cong F(a)$ によって $1_a$ に対応する $u\in F(a)$ が普遍要素であり、この自然同型は $F(-)(u):\mathcal{C}(-, a)\rightarrow F$ によって与えられる。

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

### 稠密性定理

前層の圏 $\hat{\mathcal{C}}$ には表現可能関手とそうでない関手の2種類が存在する。稠密(ちゅうみつ)性定理はこれらの関係について述べたもので非常に役に立つ定理である。

{{% theorem title="稠密性定理" label="th.density-theorem" %}}
任意の前層 $F: \mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ は表現可能関手の余極限である。
すなわち、適当な図式 $d: \mathcal{J}\rightarrow\mathcal{C}$ が存在して
$$ F \cong \varinjlim\mathcal{Y}\circ d = \varinjlim\_{i\in\mathcal{J}}\mathcal{Y}(d_i) = \varinjlim\_{i\in\mathcal{J}}\mathcal{C}(-, d_i) $$
と表せる。
{{% /theorem %}}

これを証明する為に、まず **要素の圏** というものを考える。
{{% definition title="要素の圏" %}}
関手 $F:\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ に対して、対象を$a\in\mathcal{C}$ と $x\in F(a)$ の組 $(a,x)$ 全て、
射 $(a,x)\rightarrow (b,y)$ を $F(f)(y)=x$ となるような $f:a\rightarrow b$ によって定めた圏を $F$ の **要素の圏(category of elements)** といい、
$\mathrm{el}(F)$ や　$ \int^{\mathcal{C}}F $ と書く。

また、 $(a,x)$ を $a$ に移し、 $f: (a,x)\rightarrow (b,y)$ を $f:a\rightarrow b$ に移す対応は関手 $\int^{\mathcal{C}}F\rightarrow\mathcal{C}$ となる。
これを **射影関手(projection functor)** といい、 $\pi_F$ と書く。
{{% /definition %}}

例えば $\mathcal{C}$ を対象が $a,b$ で恒等射以外の射が $f:b\rightarrow a$ のみの圏とし、 $F:\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ を

{{% tikz %}}
  \begin{tikzpicture}
    \coordinate (f0) at (-1.2, 1.5) node at (f0) [left] {$F(a)$};
    \coordinate (f1) at (4.2, 1.5) node at (f1) [right] {$F(b)$};
    \coordinate (x) at (0, 2) node at (x) [left] {$x$};
    \coordinate (y) at (0, 1) node at (y) [left] {$y$};
    \coordinate (p) at (3, 2) node at (p) [right] {$p$};
    \coordinate (q) at (3, 1) node at (q) [right] {$q$};
    \draw (-0.2, 1.5) circle [x radius=1, y radius = 1.2];
    \draw (3.2, 1.5) circle [x radius=1, y radius = 1.2];
    \draw [-latex] (x) to (p);
    \draw [-latex] (y) to (p);
  \end{tikzpicture}
{{% /tikz %}}

のような関手とすると、 $\int^{\mathcal{C}}F$ は以下のようなこれを"開いた"圏である。
つまり、集合と関数を全て要素単位に開いて、対象と射で表し直した圏である。但し、射の向きに注意。

{{% tikz %}}
  \begin{tikzpicture}
    \coordinate (x) at (0, 2) node at (x) [left] {$(a, x)$};
    \coordinate (y) at (0, 1) node at (y) [left] {$(a, y)$};
    \coordinate (p) at (3, 2) node at (p) [right] {$(b, p)$};
    \coordinate (q) at (3, 1) node at (q) [right] {$(b, q)$};
    \draw [-latex] (p) to (x);
    \draw [-latex] (p) to (y);
  \end{tikzpicture}
{{% /tikz %}}

これを $\pi_F$ で $\mathcal{C}$ に射影すると以下のようになり

{{% tikz %}}
  \begin{tikzpicture}
    \coordinate (x) at (0, 2) node at (x) [left] {$a$};
    \coordinate (y) at (0, 1) node at (y) [left] {$a$};
    \coordinate (p) at (3, 2) node at (p) [right] {$b$};
    \coordinate (q) at (3, 1) node at (q) [right] {$b$};
    \draw [-latex] (p) to node [above] {$f$} (x);
    \draw [-latex] (p) to node [below] {$f$} (y);
  \end{tikzpicture}
{{% /tikz %}}

これを $\mathcal{Y}$ で $\hat{\mathcal{C}}$ に埋め込むと

{{% tikz %}}
  \begin{tikzpicture}
    \coordinate (x) at (0, 2) node at (x) [left] {$\mathcal{C}(-, a)$};
    \coordinate (y) at (0, 1) node at (y) [left] {$\mathcal{C}(-, a)$};
    \coordinate (p) at (3, 2) node at (p) [right] {$\mathcal{C}(-, b)$};
    \coordinate (q) at (3, 1) node at (q) [right] {$\mathcal{C}(-, b)$};
    \draw [-latex] (p) to node [above] {$f\circ-$} (x);
    \draw [-latex] (p) to node [below] {$f\circ-$} (y);
  \end{tikzpicture}
{{% /tikz %}}

となる。そして、この図式の余極限を取るとそれが $F$ と一致する。直感的に説明すると、極限錐
は4つの自然変換 $\phi_x,\phi_y,\phi_p,\phi_q$ からなり、
$$ \phi_p = \phi_x\circ(f\circ -) $$
$$ \phi_p = \phi_y\circ(f\circ -) $$
が成り立ち、これ以外に余分な情報を持たなものである。この錐が $F$ と同一の情報を持っている事が分かるだろう。

{{% tikz %}}
  \begin{tikzpicture}
    \coordinate (l) at (1.5, 4) node at (l) [above] {$\varinjlim\mathcal{C}(-, d_i)$};
    \coordinate (x) at (0, 2) node at (x) [left] {$\mathcal{C}(-, a)$};
    \coordinate (y) at (0, 1) node at (y) [left] {$\mathcal{C}(-, a)$};
    \coordinate (p) at (3, 2) node at (p) [right] {$\mathcal{C}(-, b)$};
    \coordinate (q) at (3, 1) node at (q) [right] {$\mathcal{C}(-, b)$};
    \draw [-latex] (p) to node [above] {$f\circ-$} (x);
    \draw [-latex] (p) to node [below] {$f\circ-$} (y);
    \draw [-latex] (x) to node [above] {$\phi_x$} (l);
    \draw [-latex] (y) to node [above] {$\phi_y$} (l);
    \draw [-latex] (p) to node [above] {$\phi_p$} (l);
    \draw [-latex] (q) to node [above] {$\phi_q$} (l);
  \end{tikzpicture}
{{% /tikz %}}

すなわち、極限錐の側面の自然変換の集合 $\\{\varinjlim\_{i\in\mathcal{J}}\mathcal{C}(-,d_i)\rightarrow \mathcal{C}(-, a)\\}$ が $F(a)$ と一致し、
側面の可換性として、 $F(f): F(a)\rightarrow F(b)$ が表現されるわけである。では証明する。

{{% details 証明 %}}
関手 $F:\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ に対して、
$$ d: \int^{\mathcal{C}}F \xrightarrow{\pi_F} \mathcal{C} $$
とすると
$$ F \cong \varinjlim\mathcal{Y}\circ d = \varinjlim\_{(a,x)\in\int^{\mathcal{C}}F}\mathcal{C}(-, d\_{a,x}) $$
であることを示す。以下、 $\mathcal{J} = \int^{\mathcal{C}}F$ とおく。

まず、錐 $\phi: \mathcal{Y}\circ d\rightarrow F$ を定める。これは自然変換の族
$$ \\{\phi\_{a,x}: \mathcal{C}(-, d\_{a,x})\rightarrow F\\}\_{(a,x)\in\mathcal{J}}$$
であって、$\phi\_{a,x}$ は射の族
$$ \\{\phi\_{a,x,p}: \mathcal{C}(p, d\_{a,x})\rightarrow F(p) \\}\_{p\in\mathcal{C}} $$
である。ここで $d\_{a,x}=a$ であることに注意して
$$ \phi\_{a,x,p}(f: p\rightarrow a) = F(f)(x) $$
と定める。こうして定義した $\phi$ が自然変換であることは簡単に示せるので省略する。

後は $G:\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ を頂点とする錐 $\psi: \mathcal{Y}\circ d\rightarrow F$ に対して
以下の図式(A)が可換となる $u: F\rightarrow G$ がただ一つに定まることを示せば良い。
$$\xymatrix{
F \ar[r]^{u} & G \\\\
\mathcal{Y}\circ d \ar[u]^{\phi} \ar[ur]\_{\psi} & 
}$$
この時、全ての$a,p\in\mathcal{C}$, $x\in F(a)$ に対して以下が可換である必要がある。
$$\xymatrix{
F(p) \ar[r]^{u_p} & G(p) \\\\
\mathcal{C}(p, a) \ar[u]^{\phi\_{a,x,p}} \ar[ur]\_{\psi\_{a,x,p}} & 
}$$
特に
$$\xymatrix{
F(a) \ar[r]^{u_a} & G(a) \\\\
\mathcal{C}(a, a) \ar[u]^{\phi\_{a,x,a}} \ar[ur]\_{\psi\_{a,x,a}} & 
}$$
が可換であるので、左下に $1_a$ を入れると $\phi\_{a,x,a}(1_a) = F(1_a)(x) = x$ であるから
$$ u_a(x) = \psi\_{a,x,a}(1_a)$$
である必要がある。ここで $x\in F(a)$ は $F(a)$ 全体にわたるので $u_a$、そして $u$ は一意に定まる。

このとき、以下の図式(B)の左下に $f: p\rightarrow a$ を代入すると
$$\xymatrix{
F(p) \ar[r]^{u_p} & G(p) \\\\
\mathcal{C}(p, a) \ar[u]^{\phi\_{a,x,p}} \ar[ur]\_{\psi\_{a,x,p}} & 
}$$
$$ u_p(\phi\_{a,x,p}(f)) = u_p(F(f)(x)) = \psi\_{p,F(f)(x),p}(1_p)$$
である。ここで $\psi$ は自然変換であるから、 $\mathcal{J}$ の射 $(p,F(f)(x)) \xrightarrow{f} (a,x)$に関して以下が可換。
$$\xymatrix{
G \ar[r]^{1_G} & G \\\\ 
\mathcal{Y}(d\_{p,F(f)(x)}) \ar[r]^-{f\circ-} \ar[u]^{\psi\_{p,F(f)(x)}} & \mathcal{Y}(d\_{a,x}) \ar[u]\_{\psi\_{a,x}}
}$$
従って以下が可換
$$\xymatrix{
G(p) \ar[r]^{1\_{G(p)}} & G(p) \\\\
\mathcal{C}(p, p) \ar[r]^-{f\circ-} \ar[u]^{\psi\_{p,F(f)(x),p}} & \mathcal{C}(p, a) \ar[u]\_{\psi\_{a,x,p}}
}$$
従って左下に $1_p$ を代入して
$$ \psi\_{p,F(f)(x),p}(1_p) = \psi\_{a,x,p}(f)$$
となるから図式(B)は可換。よって図式(A)も可換となる。$u$ が自然変換であることは簡単に示せるから省略する。
以上より図式(A)を可換とする$u:F\rightarrow G$ は一意に定まるから $F$ は余極限の普遍性を満たし、余極限が同型を除いて一意であることから
$$ F \cong \varinjlim\mathcal{Y}\circ d $$
である。 $\square$
{{% /details %}}

## 指数対象

極限とは異なる普遍性をもつ対象に **指数対象(exponential object)** がある。指数対象は "関数" のような性質を持つ対象のことで、"引数" を与えて "結果" を得る事が出来る。
すなわち $f$ と $a$ から $f(a)$ を得るような操作を圏論的に一般化したものである。

### 指数対象の定義

{{% definition title="指数対象" %}}
有限積を持つ圏 $\mathcal{C}$ において関手
$$ \mathcal{C}(-\times a, b):\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$$
が表現可能であるならば、これを表現する対象を **指数対象(exponential object)** といい $b^a$ と書く。すなわち、指数対象は自然同型
$$ \mathcal{C}(-\times a, b) \cong \mathcal{C}(-, b^a)$$
を与える対象である。また普遍要素を **評価射(evaluation map)** といい $\mathrm{ev}:b^a\times a\rightarrow b$ と書く。
{{% /definition %}}

ここで登場した $\mathcal{C}(-\times a, b)$ は $\mathcal{C}(-, b)\circ (-\times a)$ という2つの関手を合成したもので、 関手 $-\times a$ は $x\in\mathcal{C}$ を $x\times a$ に移し、 $f:x\rightarrow y$ を $f\times 1_a$ に移すような関手である。

この定義を {{< refer prop.universal-construction >}}を用いて図式を用いた定義に翻訳すると、任意の $f:x\times a\rightarrow b$ に対して
$$ f = \mathcal{C}(u\times a, b)(\mathrm{ev}) = (-\circ (u\times 1_a))(\mathrm{ev}) = \mathrm{ev} \circ (u\times 1_a) $$
となるような $u: x\rightarrow b^a$ が一意に存在する、と言う事が指数対象の持つ普遍性となる。

$$\xymatrix{
x\times a \ar[d]\_{u\times 1_a} \ar[rd]^f & \\\\
b^a\times a \ar[r]^{\mathrm{ev}} & b
}$$

{{% proposition %}}
$\mathbf{Set}$ における指数対象 $b^a$ は $\mathbf{Set}(a,b)$ である。
{{% /proposition %}}
{{% details 証明 %}}
評価射 $\mathrm{ev}: B^A\times A\rightarrow B$ を
$$ \mathrm{ev}(f, a) = f(a)$$
によって定める。任意の $g:X\times A\rightarrow B$ について $u:X\rightarrow B^A$ が
指数対象の図式の可換性を満たすとすると、任意の $(x,a)\in X\times A$ について
$$ \mathrm{ev}\circ (u\times 1_a)(x, a) = g(x, a) \Leftrightarrow u(x)(a) = g(x, a)$$
であるから、これが成立する$ u(x) = (a\mapsto g(x, a))$が唯一つ存在する。
$\square$
{{% /details %}}

### 指数対象の性質

指数対象が $a^b$ と書かれるのは指数法則と類似した性質を満たす為である。

{{% proposition %}}
$$ (a^b)^c \cong a^{b\times c} $$
{{% /proposition %}}
{{% details 証明 %}}
$$ \mathcal{C}(x,(a^b)^c)\cong\mathcal{C}(x\times c, a^b)\cong\mathcal{C}((x\times c)\times b, a)\cong\mathcal{C}(x\times (b\times c), a)\cong\mathcal{C}(x, a^{b\times c}) $$
と米田の原理より。 $\square$
{{% /details %}}

{{% proposition %}}
$$ (a\times b)^c \cong a^c\times b^c$$
{{% /proposition %}}
{{% details 証明 %}}
{{< refer prop.yoneda-preserves-limits-examples >}} を用いて
$$\begin{align\*}
\mathcal{C}(x, (a\times b)^c) &\cong \mathcal{C}(x\times c, a\times b) \\\\
                              &\cong \mathcal{C}(x\times c, a)\times\mathcal{C}(x\times c, b) \\\\
                              &\cong \mathcal{C}(x, a^c)\times\mathcal{C}(x, b^c) \\\\
                              &\cong \mathcal{C}(x, a^c\times b^c)
\end{align\*}$$
と米田の原理より。 $\square$
{{% /details %}}

{{% proposition %}}
$$ 1^a\cong 1$$
{{% /proposition %}}
{{% details 証明 %}}
$$\mathcal{C}(x, 1^a)\cong\mathcal{C}(x\times a, 1)\cong\mathcal{C}(x, 1)$$
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
分配圏では、任意の対象 $a\in\mathcal{C}$ について $a\times 0\cong 0$
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

以上より射 $a\times 0\rightarrow x$ は唯一つしか存在しないので $a\times 0$ は始対象である。そして始対象は全て同型であるから $a\times 0\cong 0$ である。 $\square$
{{% /details %}}

{{% proposition %}}
分配圏では $a^{b+c}\cong a^b \times a^c$
{{% /proposition %}}
{{% details 証明 %}}
$x$ について自然な同型
$$\begin{align\*}
&\mathcal{C}(x, a^{b+c})\cong\mathcal{C}(x\times(b+c), a)\cong\mathcal{C}(x\times b + x\times c, a)\cong\mathcal{C}(x\times b, a)\times\mathcal{C}(x\times c, a)\\\\
&\cong\mathcal{C}(x, a^b)\times\mathcal{C}(x,a^c)\cong\mathcal{C}(x,a^b\times a^c)
\end{align\*}$$
が存在するので米田の原理より $a^{b+c}\cong a^b\times a^c$ $\square$
{{% /details %}}

{{% proposition %}}
分配圏では $a^0\cong 1$
{{% /proposition %}}
{{% details 証明 %}}
任意の $x\in\mathcal{C}$ について同型
$$\mathcal{C}(x, a^0) \cong \mathcal{C}(x\times 0, a) \cong \mathcal{C}(0, a)$$
が存在するが、$0$が始対象であることから最右辺の要素数は1である。したがって射 $x\rightarrow a^0$ も唯一つしか存在しない為 $a^0$ は終対象である。したがって $a^0\cong 1$ $\square$
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
\cong \mathcal{C}(a\times b, x)\times\mathcal{C}(a\times c, x)
\cong \mathcal{C}(b, x^a) \times \mathcal{C}(c, x^a) \\\\
& \cong \mathcal{C}(b+c, x^a)
\cong \mathcal{C}(a\times(b+c), x)
\end{align\*}$$
が存在するので米田の原理より $a\times b+a\times c\cong a\times(b+c)$ である。 $\square$
{{% /details %}}

## 随伴
普遍的構成の一種である **随伴(adjunction)** は二つの圏 $\mathcal{C},\mathcal{D}$ を相互に繋ぐ関手
$$ F: \mathcal{C}\rightleftarrows\mathcal{D}: G$$
の間の関係であるが、

> "Adjoint functors arise everywhere”
> (S. Mac Lane, Categories for the working mathematician)

とマクレーンが言っているように、数学の様々な場所で普遍的に現れるものである。様々な数学的概念を随伴として表現する事ができる。

### 随伴の定義

{{% definition title="随伴" label="def.adjunction" %}}
圏 $\mathcal{C}$ と $\mathcal{D}$ の間の **随伴(adjunction)** とは、
関手 $F:\mathcal{C}\rightarrow\mathcal{D}$ と $G:\mathcal{D}\rightarrow\mathcal{C}$ の対であり、 $a\in\mathcal{C},b\in\mathcal{D}$ について自然な同型
$$ \mathcal{D}(F(a), b)\cong\mathcal{C}(a,G(b)) $$
が存在するものをいう。

この時 $F$ を $G$ の**左随伴(left adjoint)**、 $G$ を$F$ の **右随伴(right adjoint)** といい、 $F\dashv G$ と書く。以下のような図式で表現することもある。

$$\xymatrix{
\mathcal{C} \ar@/^4pt/[r]^{F}\_{}=\"x\" & \mathcal{D} \ar@/^4pt/[l]^{G}\_{}=\"y\"
\ar@{}|{\perp} \"x\";\"y\"
}$$

随伴関手、左随伴関手、右随伴関手という用語を使うこともある。
{{% /definition %}}

以下のように図示すると対応が分かりやすい。

$$\begin{array}{rcccl}
F(a) & \rightarrow & b & \text{in $\mathcal{D}$}\\\\ \hline
a & \rightarrow & G(b) & \text{in $\mathcal{C}$}
\end{array}$$

ここで、自然同型 $ \phi\_{a,b}: \mathcal{D}(F(a), b)\cong \mathcal{C}(a,G(b)) $
が $a,b$ について自然であるというのは、任意の $f:a'\rightarrow a, g:b\rightarrow b'$ について

$$ \xymatrix{
\mathcal{D}(F(a), b)   \ar[r]^{\phi\_{a,b}} \ar[d]\_{\mathcal{D}(F(f), g)=g\circ - \circ F(f)} & \mathcal{C}(a, G(b)) \ar[d]^{\mathcal{C}(f, G(g))=G(g)\circ - \circ f} \\\\
\mathcal{D}(F(a'), b') \ar[r]^{\phi\_{a',b'}} & \mathcal{C}(a', G(b'))
} $$

が成り立つことである。見にくいので $\phi\_{a,b}(h),\phi^{-1}\_{a,b}(h)$ をいずれも $\overline{h}$ と書けば、任意の $h: F(a)\rightarrow b$ に対して以下の等式が成り立つ。
もちろん $\overline{\overline{h}}=h$ である。

{{% proposition label="prop.adjunction-equality" %}}
$$\xymatrix{
\mathcal{C} \ar@/^4pt/[r]^{F}\_{}=\"x\" & \mathcal{D} \ar@/^4pt/[l]^{G}\_{}=\"y\"
\ar@{}|{\perp} \"x\";\"y\"
}$$
の時、任意の $\mathcal{D}$ の射$f: a'\rightarrow a$、$\mathcal{C}$ の射 $g:b\rightarrow b'$、$\mathcal{C}$ の射 $h: F(a)\rightarrow b$ に対して以下の等式が成り立つ。
$$ \overline{g\circ h \circ F(f)} = G(g)\circ\overline{h}\circ f $$
対象を明示して以下のようにも書く。
$$ \overline{F(a')\xrightarrow{F(f)} F(a)\xrightarrow{h}b\xrightarrow{g} b'} = a'\xrightarrow{f}a\xrightarrow{\overline{h}} G(b)\xrightarrow{G(g)} G(b') $$
{{% /proposition %}}

### 随伴の例

任意の関手 $F:\mathcal{J}\rightarrow \mathcal{C}$ について極限が存在する場合、
$\varprojlim:\mathcal{C}^{\mathcal{J}}\rightarrow\mathcal{C}$
という関手が存在する。

{{% definition title="極限関手" label="def.limit-functor" %}}
$\mathcal{J}$ を小圏とし、 $\mathcal{C}$ を任意の関手 $F:\mathcal{J}\rightarrow\mathcal{C}$ について極限が存在する圏であるとする。

ここで $F\in\mathcal{C}^{\mathcal{J}}$ を $\varprojlim F$ に移し、$\mathcal{C}^{\mathcal{J}}$ の射(自然変換) $\phi: F\rightarrow G$ を
極限錐 $\Delta(\varprojlim F)\rightarrow F$ に $\phi$ を合成してできる $G$ を底とする錐 $\Delta(\varprojlim F)\rightarrow G$ から、
極限錐 $\Delta(\varprojlim G)\rightarrow G$ への一意な射 $\varprojlim F\rightarrow \varprojlim G$ に移す対応
$$ \varprojlim : \mathcal{C}^{\mathcal{J}}\rightarrow\mathcal{C}$$
は関手となる。これを **極限関手(limit functor)** という。 **余極限関手(colimit functor)** $ \varinjlim:\mathcal{C}^{\mathcal{J}}\rightarrow\mathcal{C}$ も同様に定義される。
{{% /definition %}}

すると対角関手 $\Delta:\mathcal{C}\rightarrow\mathcal{C}^{\mathcal{J}}$ と極限関手 $\varinjlim:\mathcal{C}^{\mathcal{J}}\rightarrow\mathcal{C}$ に関して、
以下の自然な同型対応がある事が分かる。

$$\begin{array}{rccl}
\Delta(x) & \rightarrow & F & \text{in $\mathcal{\mathcal{C}^{\mathcal{J}}}$}\\\\ \hline
x & \rightarrow & \varprojlim F & \text{in $\mathcal{C}$}
\end{array}$$

余極限に関しても同様で $\varprojlim,\varinjlim$ と対角関手の間に随伴関係が存在する事が分かる。

{{% proposition title="極限に関する随伴" label="prop.limit-as-adjoint" %}}
小圏 $\mathcal{J}$ について $F:J\rightarrow\mathcal{C}$ の極限が全て存在する時
$$ \Delta \dashv \varprojlim $$
である。同様に余極限が全て存在する時
$$ \varinjlim \dashv \Delta $$
である。
{{% /proposition %}}

指数対象についても同様の随伴を構成する事ができる。

{{% definition title="指数関手" label="def.exponential-functor" %}}
任意の $x\in\mathcal{C}$ に対して、指数対象 $x^a$ が存在する時、 $x$ を $x^a$ に移し、 $\mathcal{C}$ の射 $f:x\rightarrow y$を
指数対象の普遍性より射 $f\circ\mathrm{ev}: x^a\times a\rightarrow y$ に一意に対応する射 $u: x^a \rightarrow y^a$ に移す対応は関手
$$ (-)^a: \mathcal{C}\rightarrow\mathcal{C} $$
となる。これを **指数関手(exponential functor)** という。

$$\xymatrix{
x^a\times a \ar[d]\_{u\times 1_a} \ar[rd]^{f\circ\mathrm{ev}\_x}& \\\\
y^a\times a \ar[r]^{\mathrm{ev}\_y} & b
}$$
{{% /definition %}}

すると、以下のような $x,y$ について自然な同型が存在して、これは随伴関係である。

$$\begin{array}{rcccl}
x\times a & \rightarrow & y   & \text{in $\mathcal{C}$} \\\\ \hline
x         & \rightarrow & y^a & \text{in $\mathcal{C}$}
\end{array}$$

{{% proposition title="指数対象に関する随伴" %}}
任意の $x\in\mathcal{C}$ に対して $x\times a$、$x^a$ が存在する時
$$ (-)\times a \dashv (-)^a $$
{{% /proposition %}}

### 随伴の性質

{{% proposition %}}
ある関手の右随伴が存在するならば、それは自然同型を除いて一意に定まる。
左随伴についても同様。
{{% /proposition %}}
{{% details 証明 %}}
関手 $F:\mathcal{C}\rightarrow\mathcal{D}$ と $G,G':\mathcal{D}\rightarrow\mathcal{C}$ の間に
随伴 $F\dashv G$ と $F\dashv G'$ の関係があるとする。すなわち任意の $a\in\mathcal{C},b\in\mathcal{D}$ について自然な同型
$$ \mathcal{D}(F(a), b)\cong\mathcal{C}(a,G(b)) $$
$$ \mathcal{D}(F(a), b)\cong\mathcal{C}(a,G'(b)) $$
が存在するので、自然な同型
$$ \mathcal{C}(a,G(b))\cong \mathcal{C}(a,G'(b)) $$
が得られる。これが $a$ について自然であるので
$$ \mathcal{C}(-,G(b))\cong \mathcal{C}(-,G'(b)) $$
であるから、米田の原理より
$$ G(b)\cong G'(b) $$
となる。これが $b$ について自然であることから
$$ G\cong G' $$
となる。従って、$F$ の右随伴は同型を除いて一意である。

左随伴についても、米田埋め込みの双対版を考えることで同様に示せる。$\square$
{{% /details %}}

随伴に関して、以下の性質は特に重要である。様々な概念が随伴で構成できる為、役に立つ場面が多い。

{{% proposition %}}
右随伴関手は連続、左随伴関手は余連続である。
{{% /proposition %}}
{{% details 証明 %}}
随伴
$$\xymatrix{
\mathcal{C} \ar@/^4pt/[r]^{F}\_{}=\"x\" & \mathcal{D} \ar@/^4pt/[l]^{G}\_{}=\"y\"
\ar@{}|{\perp} \"x\";\"y\"
}$$
が存在する時、$G$ が任意の小さい極限を持つならば、$x\in\mathcal{C}$、 $A:\mathcal{J}\rightarrow\mathcal{D}$ について、
随伴関係と米田埋め込みの連続性から $x$ について自然な同型
$$\mathcal{C}(x, G(\varprojlim A)) \cong \mathcal{D}(F(x), \varprojlim A) \cong \varprojlim\mathcal{D}(F(x), A(-)) \cong \varprojlim\mathcal{C}(x, GA(-)) \cong \mathcal{C}(x, \varprojlim GA)$$
が存在する。従って米田の原理より $G(\varprojlim A)\cong \varprojlim GA$。
左随伴関手についても同様。 \square
{{% /details %}}

例えば、 随伴関係 $(-)\times a \dashv (-)^a$ から
$$ (\varprojlim F)^a \cong \varprojlim (-)^a \circ F, \quad (\varinjlim F)\times a \cong \varinjlim ((-)\times a)\circ F$$
が成り立つので $ (x\times y)^a \cong x^a \times y^a$ や $ (x + y)\times a \cong x\times a + y\times a$ が成立するといった事が示せる。

### 三角等式・単位元・余単位元

{{% theorem label="prop.triangle" %}}
関手 $F:\mathcal{C}\rightarrow\mathcal{D}$ と $G:\mathcal{D}\rightarrow\mathcal{C}$ が随伴 $F\dashv G$ であることは、自然変換 $\eta: 1\_{\mathcal{C}}\rightarrow GF$ と $\epsilon: FG\rightarrow 1\_{\mathcal{D}}$ が存在して、以下の図式(**三角等式(triangle identities)**) が可換となることと同値。

$$\xymatrix{
F \ar[r]^{F\eta} \ar[rd]\_{1_F} & FGF \ar[d]^{\epsilon F} & G \ar[r]^{\eta G} \ar[rd]\_{1_G} & GFG \ar[d]^{G \epsilon} \\\\
                                          & F                       &                                            & G
}$$

$\eta$ を **単位射(unit)**、 $\epsilon$ を **余単位射(counit)** という。
{{% /theorem %}}
{{% details 証明 %}}
({{< refn def.adjunction >}} $\Rightarrow$ {{< refer prop.triangle >}}の三角等式)

$F:\mathcal{C}\rightarrow\mathcal{D}, G:\mathcal{D}\rightarrow\mathcal{C}$ の間に随伴関係$F\dashv G$があるとする。
$\eta, \epsilon$ の各コンポーネントを
$$ \eta_a = \overline{1\_{F(a)}}, \epsilon_a = \overline{1\_{G(a)}}$$
にて定めるとこれらは自然変換となる。例えば、任意の $f:a\rightarrow b$ に対して以下の図式を考えると
$$\xymatrix{
a \ar[r]^{\eta_a}\ar[d]^f & GF(a) \ar[d]^{GF(f)} \\\\
b \ar[r]^{\eta_b} & GF(b)
}$$
{{< refer prop.adjunction-equality >}}より
$$ \begin{aligned}
a\xrightarrow{\eta_a} GF(a)\xrightarrow{GF(f)} GF(b) &= \overline{F(a)\xrightarrow{\overline{\eta_a}} F(a)\xrightarrow{F(f)} F(b)} \\\\
                                                     &= \overline{F(a)\xrightarrow{1\_{F(a)}} F(a)\xrightarrow{F(f)} F(b)} \\\\
                                                     &= \overline{F(a)\xrightarrow{F(f)} F(b) \xrightarrow{1\_{F(b)}} F(b)} \\\\
                                                     &= a\xrightarrow{f} b \xrightarrow{\overline{1\_{F(b)}}} GF(b) \\\\
                                                     &= a\xrightarrow{f} b \xrightarrow{\eta_b} GF(b)
\end{aligned}$$
となり $\eta$ が自然変換である事がわかる。 $\epsilon$ も同様。
この時、任意の $a\in\mathcal{C}$ について

$$\begin{align*}
\overline{F(a) \xrightarrow{F(\eta_a)} FGF(a) \xrightarrow{\epsilon\_{F(a)}} F(a)} &= a\xrightarrow{\eta_a} GF(a) \xrightarrow{\overline{\epsilon\_{F(a)}}} GF(a) \\\\
 &= a\xrightarrow{\eta_a} GF(a) \xrightarrow{1\_{GF(a)}} GF(a) \\\\
 &= a\xrightarrow{\eta_a} GF(a) \\\\
 &= \overline{F(a)\xrightarrow{1\_{F(a)}}F(a)}
\end{align*}$$

であるので $\epsilon\_{F(a)}\circ F(\eta_a) = 1\_{F(a)}$ すなわち $\epsilon F\circ F\eta = 1_F$ である。
$G\epsilon\circ\eta G=1\_{G}$ も同様。

({{< refer prop.triangle >}}の三角等式 $\Rightarrow$ {{< refn def.adjunction >}})

$\epsilon F\circ F\eta = 1_F,\quad G\epsilon\circ\eta G=1\_{G}$であるとする。
すなわち、以下が成立

$$ F(a) \xrightarrow{F(\eta_a)} FGF(a) \xrightarrow{\epsilon\_{F(a)}} F(a) = F(a)\xrightarrow{1\_{F(a)}}F(a) \qquad (\forall a\in\mathcal{C})\qquad\cdots(A)$$
$$ G(a)\xrightarrow{\eta\_{G(a)}} GFG(a)\xrightarrow{G(\epsilon_a)} G(a) = G(a)\xrightarrow{1\_{G(a)}}G(a)\qquad (\forall a\in\mathcal{D})\qquad\cdots(B)$$

また、$\eta, \epsilon$ は自然変換であるから、以下が成立。

$$ a\xrightarrow{f}b \xrightarrow{\eta_b}GF(b) = a\xrightarrow{\eta_a}GF(a)\xrightarrow{GF(f)} GF(b)\qquad (\forall f:a\rightarrow b \in\mathcal{C})\qquad\cdots(C)$$
$$ FG(a)\xrightarrow{\epsilon_a}a\xrightarrow{f}b = FG(a)\xrightarrow{FG(f)}FG(b)\xrightarrow{\epsilon_b}b \qquad(\forall f:a\rightarrow b \in\mathcal{D})\qquad\cdots(D)$$

ここで写像 $\phi:\mathcal{D}(F(a),b)\leftrightarrow \mathcal{C}(a, G(b)):\psi$ を以下のように置く

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
であるから $\phi,\psi$ は全単射 $\mathcal{D}(F(a),b)\leftrightarrows\mathcal{C}(a, G(b))$ である。以後$\phi(h),\psi(h)$ を $\bar{h}$ と書く。

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

今の証明から分かるように、単位元・余単位元は以下の関係から求められる。

{{% proposition %}}
$$\xymatrix{
\mathcal{C} \ar@/^4pt/[r]^{F}\_{}=\"x\" & \mathcal{D} \ar@/^4pt/[l]^{G}\_{}=\"y\"
\ar@{}|{\perp} \"x\";\"y\"
}$$
である時、単位射 $\eta:1\_{\mathcal{C}}\rightarrow GF$ の $a$コンポーネントは自然同型
$$ \mathcal{D}(F(a), F(a)) \cong \mathcal{C}(a, GF(a))$$
の左辺の $1\_{F(a)}$ に対応する右辺の射 $\eta\_a: a\rightarrow GF(a)$ で与えられる。

同様に、余単位射 $\epsilon: FG\rightarrow 1\_{\mathcal{D}}$ の $b$ コンポーネントは自然同型
$$ \mathcal{D}(FG(b), b) \cong \mathcal{C}(G(b), G(b))$$
の右辺の $1\_{G(b)}$ に対応する左辺の射 $\epsilon\_b: GF(b)\rightarrow b$ で与えられる。
{{% /proposition %}}

### 単位元・余単位元の例

単位射・余単位射の具体的な例を見てみよう。例えば随伴

$$\begin{array}{rcccl}
\Delta(x) & \rightarrow & F             \\\\ \hline
x         & \rightarrow & \varprojlim F
\end{array}$$

の単位射は

$$\begin{array}{rcccl}
\Delta(x) & \rightarrow & \Delta(x)             \\\\ \hline
x         & \rightarrow & \varprojlim \Delta(x)
\end{array}$$

の上の恒等射に対応する下の射である。 $\varprojlim \Delta(x) = x$ であることは容易にわかるから、下の対応する射は $1_x$ すなわち、 $\eta_x=1_x$ である。
続いて、余単位射は

$$\begin{array}{rcccl}
\Delta(\varprojlim F) & \rightarrow & F             \\\\ \hline
\varprojlim F         & \rightarrow & \varprojlim F
\end{array}$$
の下の恒等射に対応する上の射である。従って $\epsilon$ は極限錐 $\epsilon: \Delta(\varprojlim F)\rightarrow F$ である。

同様に、随伴
$$\begin{array}{rcccl}
x\times a & \rightarrow & y             \\\\ \hline
x         & \rightarrow & y^a
\end{array}$$
の余単位射は評価射 $\mathrm{ev}: y^a\times a\rightarrow y$ である。
