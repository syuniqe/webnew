$html = Get-Content -Path 'C:\Users\Harsh\Downloads\index (1).html' -Raw
$css = [regex]::Match($html, '(?s)<style>(.*?)</style>').Groups[1].Value
$js = [regex]::Match($html, '(?s)<script>(.*?)</script>').Groups[1].Value
$newHtml = $html -replace '(?s)<style>.*?</style>', '<link rel="stylesheet" href="css/styles.css">'
$newHtml = $newHtml -replace '(?s)<script>.*?</script>', '<script src="js/main.js"></script>'

New-Item -ItemType Directory -Force -Path 'css'
New-Item -ItemType Directory -Force -Path 'js'

Set-Content -Path 'index.html' -Value $newHtml
Set-Content -Path 'css\styles.css' -Value $css
Set-Content -Path 'js\main.js' -Value $js
