# CSS
```
层叠样式表(英文全称：Cascading Style Sheets)是一种用来表现HTML（标准通用标记语言的一个应用）或XML（标准通用标记语言的一个子集）等文件样式的计算机语言。CSS不仅可以静态地修饰网页，还可以配合各种脚本语言动态地对网页各元素进行格式化
CSS 能够对网页中元素位置的排版进行像素级精确控制，支持几乎所有的字体字号样式，拥有对网页对象和模型样式编辑的能力。
```

### web项目开发中css的位置
```
css主要一般都是由前端开发工程师,或者UI设计师完成的.
css3是目前的最新版本
```
### 学习工具

```
学习css一般有三种工具提供给我们开发:
1. 代码编辑器本身一般自带提示或者语法提示.

2. css手册,内部提供提供了所有的样式属性和样式值的使用参考,甚至包括一些演示代码.
   http://css.doyoe.com
   
3. 浏览器也内置了一些css辅助工具给我们学习和开发.
   F12,或者Ctrl+shift+i,或者鼠标右键,检查代码
```


# css的基本使用

```css在使用过程中,主要就是嵌套进网页中进行使用的.使用过程中,一般有三种引入方式:```

### 行内样式

主要在开始标签中, 通过style属性来编写样式.在工作中,行内样式是使用频率最少的.

一般都是将来通过来javascript来控制的样式才会使用行内样式.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body style="background-color: orange;color: red;">
    <h1 style="border: 1px solid #ccc;">网页的内容</h1>
</body>
</html>
```

### 内部样式

主要通过在head的内部子标签style标签中编写css样式.

在开发中,内样样式主要都是编写在html网页内部,但是开发中一个web项目往往由多个html网页组成.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
    body {
        background-color: orange;
    }
    h1 {
        background-color: blue;
        color: white;
    }
    </style>
</head>
<body>
    <h1>网页的内容</h1>
</body>
</html>
```

### 外部样式

主要是在css文件中编写css样式, 然后在head的子标签link标签的href属性中指定css路径引入到网页中进行“导包”使用.

创建html网页,编写代码:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="css/index.css">
</head>
<body>
    <h1>网页的内容</h1>
</body>
</html>
```

```css
创建css文件,例如,上面所说的,index.css,保存当前网页的同级目录css目录下, 然后编写代码
body{
    background-color: orange;
}
h1{
    color: red;
}
```



# css的基本语法

```
格式: 
选择符{
  样式属性: 属性值;
  样式属性: 属性值 属性值 ...;
}

选择符{样式属性: 属性值;样式属性: 属性值 属性值 ...;}

# 注意:
1. 选择符主要是告诉浏览器,接下来花括号里面样式给哪一个标签或者那一批标签添加外观的,在行内样式中,不需要加选择符
2. 样式属性主要是告诉浏览器,给指定的标签添加什么样的外观,样式属性在同一个花括号里面或者同一个标签中,是唯一的.如果出现重复的话,在浏览器产生覆盖效果.
3. 属性值主要是告诉浏览器,给指定标签添加的指定外观是什么效果,一般如果没有指定样式,浏览器内部都会有对应的默认值,写上属性和属性值以后就会覆盖默认值.属性值也是唯一的.多个属性值的情况下,必须使用英文的空格隔开.
4. css中所有的代码,都不需要缩进或者换行.
```



## 注释

在css中也有注释,注释的目的是为了解释代码的用途或者作用.方便其他开发者更好的了解当前的代码.

```css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
    /*
       多行注释, 这里的内容就不会被显示或者不会被浏览器执行.
     */
    body{
        background-color: blue; /* 背景-颜色: 蓝色; */
        color: white;  /* 字体颜色: 白色; */
    }
    </style>
</head>
<body>
    <h1>网页的内容</h1>
</body>
</html>
```

## css的选择符

#### 万能选择符`*`

在工作中, 星号基本不用, 如果有使用的话,基本就是用在页面的外观初始化时.

```css
* { /* 代表网页中的所有元素 */
	color: blue;
}
```

#### 标签选择符

也叫元素选择符,可以指定同一种名称的标签的外观效果,例如,p,h1,a,li在css中都是标签选择符

```css
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
	<style>
	body{
		background-color: #cccccc;
	}
	p { /* 通过标签名来控制指定哪些标签的外观效果,这就是标签选择符 */
		font-size: 26px;
	}
	</style>
</head>
<body>
<h1>静夜诗</h1>
<p>
	床前明月光,<br>
	疑是地上霜.<br>
	....
</p>
<p>
	另一个段落
</p>
</body>
</html>
```



#### ID选择符

给指定的标签指定id值,把这个id值作为选择符,左边加上`#`,就可以在css中给这个标签[html元素]加上样式了.

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
	<style>
	#p1{ /* 告诉浏览器找到id值为p1的标签,给它加上外观样式 */
		color: orange; /* 颜色: 橙色 */
		font-size: 32px; /* 字体-大小: 32像素; */
	}
	#h2{
		color: blue;
	}
	</style>
</head>
<body>
<h1>静夜诗</h1>
<p>
	床前明月光,<br>
	疑是地上霜.<br>
	....
</p>
<p id="p1">
	另一个段落
</p>

<h2 id="h2">h2标题</h2>
</body>
</html>
```



#### class类选择符

通过标签的class属性值可以对页面中的标签进行分类, 然后在css样式中,使用`.分类名`作为选择符,可以给指定分类的所有标签增加样式外观

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
	<style>
	.c1{ /* 指定具有class属性值为c1的所有的标签的样式 */
		color: blue;
	}
	.p1{
		font-size: 32px;
	}
	.p2{
		background-color: orange;
	}
	</style>
</head>
<body>
<h1>静夜诗</h1>
<p class="p2">
	床前明月光,<br>
	疑是地上霜.<br>
	....
</p>

<p class="c1 p1 p2" id="c1">另一个段落</p>
<h2 class="c1">h2标题</h2>
<p class="c1 p1">还有一个段落</p>
</body>
</html>
```



### 关系选择符

#### 包含选择符

可以控制到内部所有的标签,不管是子级或者隔代[爷爷.祖先…控制后代]的.

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
	<style>
	.box p{ /* div元素包含的所有的p元素 */
		background-color: blue;
		color: #fff;
	}
	</style>
</head>
<body>
	<p>这是一个网页</p>
	<div class="box">
		<p>这里也有一个段落</p>
		<p>详情请点击<a href="">了解更多</a></p>
	</div>
</body>
</html>
```



#### 父子选择符

```css
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
	<style>
	.header p{ /* class=headers的元素里面所有的子标签p或者孙子标签p... */
		background-color: #ccc;
		color: blue;
	}
	.header>p{ /* class=header的元素的子标签p */
		color: red;
	}
	</style>
</head>
<body>
	<div class="header">
		<div class="header-left">
			<p>页面的左边</p>
		</div>
		<p>中间的一段文本</p>
		<div class="header-right">
			<p>页面的右边</p>
		</div>
	</div>
</body>
</html>
```



#### 兄弟选择符

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
	<style>
	#three+li{ /* id=three的下一个标签叫li的,如果下一个标签不叫li或者不是指定的选择符,则样式的修改无效 */
		color: red;
	}
	#three~.a1{/* id=three的后面所有class=a1的兄弟元素 */
		background-color: orange;
	}
	</style>
</head>
<body>
	<ul>
		<li>第1个li元素</li>
		<li>第2个li元素</li>
		<li id="three">第3个li元素</li>
		<li>第4个li元素</li>
		<li class="a1">第5个li元素</li>
		<li>第6个li元素</li>
		<li class="a1">第7个li元素</li>
	</ul>
</body>
</html>
```



### 属性选择符

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
	<style>
	input[type]{ /* 控制所有具有type属性的input元素 */
		outline: none;/* 去除外边线 */
	}
	input[type=text]{ /* 控制所有type="text"的input元素 */
		color: red;
	}
	</style>
</head>
<body>
	用户名: <input type="text" name="" /><br>
	昵称: <input type="text" /><br>
	密码: <input type="password" /><br>
	性别: <input type="radio" name="">男
</body>
</html>
```



### 伪类选择符

用于控制标签在某一个特殊环境或者处于某种状态下的时候,控制它们的外观.

```
E:hover 当元素处于被鼠标悬浮的时候,指定样式
E:nth-child()  当元素处于父元素的指定某一个位置时
```

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
	<style>
	a{
		color: blue;
	}
	a:hover{ /* 当标签处于被鼠标悬浮的时候 */
		color: #7cffa7;
	}
	a:nth-child(1){/* 处于第一个位置的子元素 */
		color: red;
	}
	a:last-child{
		color: red;
	}
	.list1 li:nth-child(odd){ /* odd排名在奇数位置的li标签 */
		background-color: red;
	}
	.list1 li:nth-child(even){
		background-color: blue;
	}
	.last2 li:nth-child(3n-2){
		background-color: red;
	}
	.last2 li:nth-child(3n-1){
		background-color: green;
	}
	.last2 li:nth-child(3n){
		background-color: blue;
	}
	</style>
</head>
<body>
	<a href="http://www.baidu.com/">老男孩</a><br>
	<a href="http://www.baidu.com/">老男孩</a><br>
	<a href="http://www.baidu.com/">老男孩</a><br>
	<a href="http://www.baidu.cn/">老男孩</a>
	<ul class="list1">
		<li>1</li>
		<li>1</li>
		<li>1</li>
		<li>1</li>
		<li>1</li>
		<li>1</li>
	</ul>
	<ul class="last2">
		<li>1</li>
		<li>1</li>
		<li>1</li>
		<li>1</li>
		<li>1</li>
		<li>1</li>
	</ul>
</body>
</html>
```



### 伪对象选择符

```html
E:before / E::before 在元素之前
E:after / E::after   在元素之后
E::selection         在元素鼠标划选文本时
```

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
	<style>
	.price{
		color: red;
	}
	.price::before{
		content: "<<";
		color: blue;
	}
	.price::after{
		content: ">>";
		color: blue;
	}
	.price::selection{
		background-color: red;
		color: orange;
	}
	</style>
</head>
<body>
	<span class="price">价格</span>
</body>
</html>
```



## css的属性

```html
文本属性
	text-align       文本水平对齐方式
	text-indent      文本的首行缩进
	letter-spacing   字符间距
	vertical-align   文本垂直对齐方式[一般都是在图片排版的时候使用]
	line-height      文本行高
	text-decoration  文本的装饰线
字体属性	
	font-size        字体大小
	font-family      字体种类
	font-weight      字体粗细
	font-style       字体正斜
	font             字体属性的缩写[包括上面接]
	color            字体颜色

尺寸属性
	width               元素的宽度
	height              元素的高度
	min-width           元素的最小宽度
	max-width           元素的最大宽度

边框属性
	border-width       边框的宽度
	border-style       边框的样式
	border-color       边框的颜色
	border             上面三个边框属性的缩写

背景属性
	border-radius      元素的圆角
	background-color   背景颜色
	background-image   背景图片
	background-repeat  背景平铺方式
	background-position 背景定位位置
	background-size     背景尺寸大小
	background          上面几个背景属性的缩写

边距属性
	margin              元素与其他元素的外边距
                      元素上下的外边距如果重合取最大值,元素左右的边距进行相加
	padding             元素与子元素或内容之间的内边距

定位属性
	position            元素的定位类型
		static     静态定位
		relative   相对于元素自身原来的位置进行定位
    absolute   相对于父级定位元素的位置进行定位
	  fixed      相对于浏览器窗口位置进行定位[固定定位]

	top                 定位元素离顶部的距离
	bottom              定位元素离底部的距离
	right               定位元素离右边的距离
	left                定位元素离左边的距离
	z-index             元素在z轴上的高度[高的元素被覆盖低的元素]

动画相关
	opacity             不透明度
	box-shadow          元素的阴影
	transition          元素切换样式值时的过渡效果
	animation           元素的动画效果


列表属性
	list-style          列表的项目符号效果

表格属性
	border-collapse     表格的边框合并

光标属性
	cursor              光标属性

布局属性
	display             元素的显示模式
		inline            设置元素为行内元素
    block             设置元素为块级元素
	  inline-block      设置元素为行内块级元素
		none              设置元素为隐藏元素

	float               元素的浮动效果
		none;             设置元素不浮动
		left;             设置元素靠左浮动
	  right;            设置元素靠右浮动

	clear               清除浮动效果
	overflow            处理元素的溢出内容效果

	flex                设置元素的弹性方式
```



# 元素的显示模式
```
html元素因为不同的显示模式,一般可以划分成4种.
隐藏元素
		css属性: display: none;
		特征: 在页面中不会显示,不占据页面位置,用户看不到
		例如:
			head
			<input type="hidden">  隐藏域

行内元素,也叫内联元素
		css属性: display: inline; 
		特征: 在页面中同类标签一行多个,标签本身不会换行
		没有宽度和高度的,设置没有上下的内外边距,它的宽度和高度完全是由内部的子元素或者内容来撑开的.
		例如:
			a, b, span,....
			
行内块级元素,也叫内联块级元素
		css属性: display: inline-block
		特征: 类似于行内元素,一行多个,不会自带换行,但是有自己的宽度和高度以及内外边距
		例如:
			input
			textarea
			img

块级元素
		css属性: display: block
		特征: 一个元素独占一行, 自带换行,默认占据100%的宽度.有宽度高度以及内外边距
		例如:
			p, h1,....
			
元素的类型并非固定不变的,这些都是属于html默认自定的样式而已, 我们可以通过css提供的display来转换标签的类型.也就是修改元素的显示模式.
```

# css的网页布局

## table布局

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
    /* 初始化 */
    h1,h2,h3,h4,h5,h6,body,ul,li,table,tr,td,input,textarea,select,p{
        margin: 0;
        padding: 0;
        font-size: 16px;
        font-family: Arial;
    }
    ul{
        list-style: none;
    }
    a{
        text-decoration: none;
        color: #000;
    }
    table{
        border-collapse: collapse;/* 合并边框 */
    }
    .page {
        border: 1px solid #ddd;
        width: 100%;
        max-width: 1270px;
        margin: 0 auto; /* 可以让块级元素左右居中 */
    }
    .text-left {
        float: left; /* 让文本设置左中右,使用 text-align,如果让块级元素设置左中右,则需要使用margin或者float了 */
        margin-left: 20px;
    }
    .text-right{
        float: right;
        margin-right: 20px;
    }
    .table-header{
        height: 42px;
        line-height: 42px;
        background-color: #f5f5f5;
        border: 1px solid #ddd;
    }
    .text-left,.text-right{
        font-weight: bold;
    }
    .data-table{
        margin: 20px;
        width: 1230px;
        border: 1px solid #ddd;
    }
    .data-table td{
        border: 1px solid #ddd;
    }
    .row-1{
        height: 36px;
        line-height: 36px;
        text-indent: 8px;
        background-color: #F5FAFE;

    }
    .row-1 td{
        font-weight: bold;
        font-size: 12px;
    }
    .colum-1{
        width: 368px;
    }
    .colum-2{
        width: 245px;
    }
    .colum-3{
        width: 614px;
    }
    .row-n td{
        font-size: 12px;
        color: #333;
        height: 36px;
        line-height: 36px;
        text-indent: 8px;
    }
    </style>
</head>
<body>
    <table class="page">
        <tr>
            <td class="table-header">
                <span class="text-left">lib中的第三方插件</span>
                <span class="text-right">非必选插件，请有选择性的使用，用不上的可自行删除，减少框架体积</span>
            </td>
        </tr>
        <tr>
            <td>
                <table class="data-table">
                    <tr class="row-1">
                        <td class="colum-1">名称</td>
                        <td class="colum-2">版本号</td>
                        <td class="colum-3">描述</td>
                    </tr>
                    <tr class="row-n">
                        <td>jQuery.js</td>
                        <td>1.9.1</td>
                        <td>jQuery库，可自行下载新版本，替换现有版本。</td>
                    </tr>
                </table>
            </td>
        </tr>

    </table>
</body>
</html>
```



## div+css布局

```
准备:
1. div和span的使用
   div是一个没有额外属性的块级元素,用于包含网页中的一整块内容,一般都是包含多段多行的内容
   div里面的子元素可以是其他的块级元素.块级元素里面的子元素也可以有div
   
   span是一个没有峨眉属性的内联元素,用于包含网页中的一部分内容,一般都是包含单行的内容
   span里面的子元素可以是其他的内联元素,但是一般不会出现块级元素
   
   常见是下面这种:
   <p>
     <span>xxx</span>
   </p>
   下方是: 错误的
   <span>
   		<h1></h1>
   </span>
   
2. 常用的选择符: class+id选择符
   一般命名上注意规范:
      写法上面一般分三种:
          模块化写法:
               模块名-位置/作用
               .header-left
               .header-center
               .nav-first
          位置的写法:
               .top-left
               .top-right
          顺序写法:
               .row-1
               .row-2
               .colum-1
               .table-1
  书写规范:
         多个单词拼接:
               驼峰式写法
                   .headerLeft   小驼峰
                   .HeaderLeft   大驼峰
               匈牙利写法
                   .header_left
                   .header-left

```

演示代码:

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="./css/reset.css">
    <style>
    .wraper {
        width: 424px;
        height: 570px;
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        margin: auto; /* 让块级元素自动居中 */
        background: url("./image/bg.png") no-repeat;
        padding-left: 36px;
    }
    label{
        display: block;
        font-size: 12px;
        font-family: Arial;
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
    }
    .username-text{
        margin-top: 150px;
    }
    input[type=text],input[type=password]{
        margin-bottom: 26px;
        width: 382px;
        height: 30px;
        line-height: 30px;
        background-color: transparent;
        outline: none;
        border: 1px solid #999;
    }
    input[type=submit]{
        width: 114px;
        height: 44px;
        background: url("./image/button.png") 0 0 no-repeat;
        outline: none;
        border: none;
        cursor: pointer;
    }
    input[type=submit]:hover{
        background: url("./image/button.png") 0 -44px no-repeat;
    }
    textarea{
        width: 382px;
        height: 106px;
        line-height: 30px;
        background-color: transparent;
    }
    </style>
</head>
<body>
    <div class="wraper">
        <label class="username-text">username:</label>
        <input type="text" name="username">
        <label>password:</label>
        <input type="password" name="password">
        <label>email:</label>
        <input type="text" name="emial">
        <label>message:</label>
        <textarea name=""></textarea>
        <input type="submit" value="">
    </div>
</body>
</html>
```

