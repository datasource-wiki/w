print("----------DATADSOURCE WIKI PAGE GENERATOR----------")
with open("datasource-wiki-page.txt", "w") as f:
    f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
            ''')
    title = input("Enter the title of the wiki page: ")
    f.write(title)
    f.write('''</title>
    <link rel="stylesheet" href="wiki-style.css">
</head>
<body>

<div id="container">
    <div id="header-tabs">
        <div class="header-logo-group">
            <a href="index.html">DataSource Wiki</a>
        </div>
        <form class="top-search-group" onsubmit="handleSearch(event)">
            <input type="text" id="wikiSearchInput" placeholder="Search DataSource Wiki...">
            <button type="submit">Search</button>
        </form>
    </div>

    <div id="content">
        <h1 id="firstHeading">''' + title)
    f.write('''</h1>

        <div class="article-box">
            <div class="article-body">''')
    content = input("Enter the content of the wiki page: ")
    f.write(content)
    infobox = True if input("Do you want to add an infobox? (y/n): ").strip().lower() == "y" else False
    if infobox:
        f.write('''            <div class="infobox">
                <h3>''')
        f.write(title)
        f.write('''</h3>
                <table>''')
        continue_infobox = True
        while continue_infobox:
            key = input("Enter infobox key (or type '' to finish): ")
            if key == "":
                continue_infobox = False
                break
            value = input(f"Enter value for '{key}': ")
            f.write(f'''
                    <tr>
                        <td class="label">{key}</td>
                        <td>{value}</td>
                    </tr>''')
        f.write('''                </table>
            </div>''')
    f.write('''        </div>

        <div class="alphabet-index">
            <span>Browse by letter:</span>
            <a href="search.html?search=A">A</a> |
            <a href="search.html?search=B">B</a> |
            <a href="search.html?search=C">C</a> |
            <a href="search.html?search=D">D</a> |
            <a href="search.html?search=E">E</a> |
            <a href="search.html?search=F">F</a> |
            <a href="search.html?search=G">G</a> |
            <a href="search.html?search=H">H</a> |
            <a href="search.html?search=I">I</a> |
            <a href="search.html?search=J">J</a> |
            <a href="search.html?search=K">K</a> |
            <a href="search.html?search=L">L</a> |
            <a href="search.html?search=M">M</a> |
            <a href="search.html?search=N">N</a> |
            <a href="search.html?search=O">O</a> |
            <a href="search.html?search=P">P</a> |
            <a href="search.html?search=Q">Q</a> |
            <a href="search.html?search=R">R</a> |
            <a href="search.html?search=S">S</a> |
            <a href="search.html?search=T">T</a> |
            <a href="search.html?search=U">U</a> |
            <a href="search.html?search=V">V</a> |
            <a href="search.html?search=W">W</a> |
            <a href="search.html?search=X">X</a> |
            <a href="search.html?search=Y">Y</a> |
            <a href="search.html?search=Z">Z</a>
        </div>
    </div>
</div>
</body>
</html>''')
    print("Wiki page generated successfully! Check 'datasource-wiki-page.txt' for the output.")
        
