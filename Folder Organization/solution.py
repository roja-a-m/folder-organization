def minFolders(cssFiles, jsFiles, readMeFiles, capacity):
    ans = 0
    rm = readMeFiles
    while (cssFiles > 0 and jsFiles > 0) or rm > 0:
        cur_cap = capacity
        if rm > 0:
            cur_cap -= 1
            rm -= 1

        if cssFiles == 0:
            jsFiles -= rm
            ans += rm
            rm = 0
            continue

        elif jsFiles == 0:
            cssFiles -= rm
            ans += rm
            rm = 0
            continue

        if cssFiles > jsFiles and cur_cap > 0:
            cur_css = 0
            cur_js = 0
            cur_css = cur_cap // 2 + 1
            if cur_cap % 2 == 0:
                cur_js = cur_cap // 2 - 1
            else:
                cur_js = cur_cap // 2

            cssFiles -= cur_css
            jsFiles -= cur_js

        elif jsFiles == cssFiles and cur_cap > 0:
            cur_css = 0
            cur_js = 0
            if cur_cap % 2 == 0:
                cur_css = cur_cap // 2
                cur_js = cur_cap // 2
            else:
                cur_css = cur_cap // 2 + 1
                cur_js = cur_cap // 2

            cssFiles -= cur_css
            jsFiles -= cur_js

        elif jsFiles > cssFiles and cur_cap > 0:
            cur_css = 0
            cur_js = 0

            if cur_cap % 2 == 0:
                cur_js = cur_cap // 2 + 1
                cur_css = cur_cap // 2 - 1
            else:
                cur_js = cur_cap // 2 + 1
                cur_css = cur_cap // 2

            cssFiles -= cur_css
            jsFiles -= cur_js
        ans += 1
        
    if cssFiles > 0:
        ans += cssFiles
    elif jsFiles > 0:
        ans += jsFiles

    ans = max(ans, readMeFiles)
    return ans