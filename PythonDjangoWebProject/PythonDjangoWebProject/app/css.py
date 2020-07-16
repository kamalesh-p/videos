from PythonDjangoWebProject.settings import APP_STATIC

def CSS(css):
    css = str(css)
    css = css.replace(';',';\n')
    css = css.replace('{',' {\n')
    css = css.replace('}','}\n')
    css = css.replace('*/','*/\n')
    return css

def css(color = 'grey', tab = 'black', active = 'white', background = 'white'):
    html = "/* tag */body{background-color:" + background + ";}h1, h2, h3, h4, h5, h6 {color:" + tab + ";}footer{color:" + tab + ";}textarea{width:400px;height:400px;}/* class */.navbar{font-size:16px;}.navbar {color:" + color + ";background-color:" + tab + ";border-color:" + background + ";}.navbar a:not(#active){color:" + color + ";text-decoration: none;}.navbar a:not(#active):hover, .navbar a:not(#active):active {color:" + active + ";text-decoration: none;}/* id */#BottomFixed{background-color:" + tab + ";}#rough{font-size:0px;}#container{background-color:" + background + ";}#active{color:" + color + ";background-color:" + background + ";}" + "#active:hover, #active:active{color: " + tab + ";text-decoration: none;}"
    html = CSS(html)
    with open(APP_STATIC + "content/layout.css", "w") as file:
        file.write(html)
    return html
css()