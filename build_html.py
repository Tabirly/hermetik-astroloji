import json

with open('sabian_data.js', 'r', encoding='utf-8') as f:
    sabian_js = f.read()

html_template = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
    <title>Tabirly | Hermetik Semboller Kahini</title>
    <style>
        :root {
            --candy-1: #00FFE8;
            --candy-2: #00FFB3;
            --candy-3: #008CFF;
            --candy-4: #4B5CFF;
            --bg-base: #060913;
            --card-bg: rgba(11, 16, 32, 0.7);
            --text-main: #f0f6fc;
            --text-muted: #8b9bb4;
            --radius: 16px;
            --gap: 16px;
            --glow-aqua: 0 0 22px rgba(0,255,232,.4), 0 0 44px rgba(0,140,255,.3);
            --glow-blue: 0 0 22px rgba(0,140,255,.5), 0 0 44px rgba(75,92,255,.4);
            --border-soft: 1px solid rgba(0,255,232,0.15);
        }

        * { box-sizing: border-box; }

        html, body {
            margin: 0 !important;
            padding: 0 !important;
            width: 100% !important;
            height: 100% !important;
            overflow: hidden !important; 
            font-family: 'Inter', system-ui, sans-serif;
            background-color: var(--bg-base) !important;
        }

        .wrap {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            right: 0 !important;
            bottom: 0 !important;
            z-index: 99999 !important; 
            /* Rich colorful background with pattern */
            background-color: var(--bg-base) !important;
            background-image: 
                radial-gradient(circle at 15% 50%, rgba(0, 255, 232, 0.08), transparent 50%),
                radial-gradient(circle at 85% 30%, rgba(75, 92, 255, 0.12), transparent 50%),
                radial-gradient(circle at 50% 100%, rgba(0, 140, 255, 0.1), transparent 50%),
                radial-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px) !important;
            background-size: 100% 100%, 100% 100%, 100% 100%, 30px 30px !important;
            color: var(--text-main);
            overflow-y: auto !important;
            -webkit-overflow-scrolling: touch;
            padding: 20px 15px 120px 15px !important;
            box-sizing: border-box;
            line-height: 1.6;
        }

        /* Glass Panel */
        .panel {
            background: var(--card-bg);
            border: var(--border-soft);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-radius: var(--radius);
            padding: 24px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            max-width: 800px;
            margin: 0 auto 24px auto;
            text-align: center;
        }

        h1, h2, h3 {
            color: var(--candy-1);
            margin-top: 0;
            text-transform: uppercase;
            letter-spacing: 1px;
            text-shadow: 0 0 15px rgba(0,255,232,0.3);
        }

        p { color: var(--text-muted); font-size: 15px; }

        .btn {
            background: linear-gradient(180deg, var(--candy-1), var(--candy-3));
            color: #041018 !important;
            border: none;
            border-radius: 20px;
            padding: 12px 24px;
            font-weight: 800;
            font-size: 16px;
            cursor: pointer;
            box-shadow: var(--glow-aqua);
            transition: transform .15s ease, box-shadow .2s ease, filter .2s ease;
            margin: 10px;
            position: relative;
            overflow: hidden;
        }
        .btn::after {
            content: "";
            position: absolute; inset: -60% -20% auto auto;
            width: 160%; height: 160%;
            background: radial-gradient(ellipse at top right, rgba(255,255,255,.55) 0%, rgba(255,255,255,.12) 35%, transparent 60%);
            transform: rotate(20deg);
            pointer-events: none;
        }
        .btn:hover {
            transform: translateY(-2px);
            filter: brightness(1.05);
            box-shadow: var(--glow-blue);
        }
        .btn.outline {
            background: transparent;
            color: var(--candy-1) !important;
            border: 1px solid var(--candy-1);
            box-shadow: none;
        }
        .btn.outline:hover { background: rgba(0, 255, 232, 0.05); box-shadow: var(--glow-aqua); }

        /* Navigation */
        .nav {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 30px;
        }

        /* Views */
        .view { display: none; animation: fadeIn 0.4s ease forwards; }
        .view.active { display: block; }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Zodiac Selector */
        .zodiac-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
            gap: 10px;
            margin-bottom: 20px;
        }
        .zodiac-btn {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            color: var(--text-main);
            padding: 12px;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.2s;
        }
        .zodiac-btn.active {
            border-color: var(--candy-1);
            color: var(--candy-1);
            background: rgba(0,255,232,0.05);
            box-shadow: 0 0 10px rgba(0,255,232,0.2);
        }
        
        /* Degree Selector */
        .degree-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(45px, 1fr));
            gap: 8px;
            margin-bottom: 20px;
        }
        .degree-btn {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            color: var(--text-muted);
            padding: 8px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
        }
        .degree-btn:hover { background: rgba(255,255,255,0.1); color: #fff; }
        .degree-btn.active {
            background: linear-gradient(180deg, var(--candy-1), var(--candy-3));
            color: #000;
            font-weight: bold;
            border-color: transparent;
            box-shadow: var(--glow-aqua);
        }

        /* Card / Symbol Details */
        .symbol-card {
            background: radial-gradient(circle at top, rgba(0,255,232,0.05), transparent 70%), var(--card-bg);
            border: 1px solid rgba(0, 255, 232, 0.15);
            border-radius: 20px;
            padding: 30px;
            position: relative;
            overflow: hidden;
            text-align: center;
            max-width: 420px;
            margin: 0 auto;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
        }
        .symbol-image-container {
            display: flex;
            justify-content: center;
            margin-bottom: 24px;
        }
        .symbol-image-placeholder, .symbol-image-active {
            width: 100%;
            max-width: 140px;
            aspect-ratio: 3/5;
            border-radius: 14px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.4);
        }
        .symbol-image-placeholder {
            background: linear-gradient(135deg, rgba(255,255,255,0.02), rgba(255,255,255,0.005));
            border: 1px dashed rgba(0,255,232,0.25);
            display: flex;
            align-items: center;
            justify-content: center;
            color: rgba(0,255,232,0.4);
            font-style: italic;
            font-size: 13px;
        }
        .symbol-image-active {
            object-fit: cover;
            border: 1px solid rgba(0,255,232,0.2);
        }
        .s-degree { color: var(--candy-1); font-weight: bold; font-size: 20px; margin-bottom: 10px; text-shadow: 0 0 10px rgba(0,255,232,0.2); }
        .s-vision { font-size: 24px; font-weight: 300; line-height: 1.4; color: #fff; margin-bottom: 24px; font-style: italic;}
        
        .s-meta { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: left;}
        .meta-box { background: rgba(0,0,0,0.4); padding: 12px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05); }
        .meta-title { font-size: 11px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; }
        .meta-val { font-size: 14px; font-weight: bold; color: var(--text-main); }

        /* Alchemy Colors for the glowing text */
        .stage-Nigredo .meta-val.stage-val { color: #aaa; text-shadow: 0 0 8px rgba(255,255,255,0.2);}
        .stage-Albedo .meta-val.stage-val { color: #fff; text-shadow: 0 0 10px rgba(255,255,255,0.6); }
        .stage-Rubedo .meta-val.stage-val { color: #ff3b6e; text-shadow: 0 0 15px rgba(255,59,110,0.5); }

        /* 3D Card Draw Animation */
        .card-container {
            perspective: 1000px;
            width: 250px;
            height: 380px;
            margin: 40px auto;
            cursor: pointer;
        }
        .card-flipper {
            position: relative;
            width: 100%;
            height: 100%;
            text-align: center;
            transition: transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            transform-style: preserve-3d;
        }
        .card-container.flipped .card-flipper { transform: rotateY(180deg); }
        .card-face {
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.6);
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .card-front {
            background: radial-gradient(120% 85% at 20% 15%, rgba(255,255,255,.15), transparent 60%), linear-gradient(135deg, var(--candy-4), var(--candy-1) 50%, var(--candy-3));
            border: 1px solid rgba(255,255,255,0.2);
        }
        .card-front::before {
            content: ""; position: absolute; inset: 0;
            background: radial-gradient(circle at 25% 25%, rgba(255,255,255,.15) 0 1px, transparent 1px) 0 0/18px 18px,
                        radial-gradient(circle at 75% 75%, rgba(255,255,255,.05) 0 1px, transparent 1px) 0 0/18px 18px;
            mix-blend-mode: overlay; opacity: .6; border-radius: 20px;
        }
        .card-front::after {
            content: "\\2726";
            font-size: 60px;
            color: #fff;
            text-shadow: 0 0 20px rgba(255,255,255,0.5);
            position: relative; z-index: 2;
        }
        .card-back {
            background: var(--card-bg);
            border: 1px solid rgba(0,255,232,0.3);
            transform: rotateY(180deg);
            padding: 20px;
            flex-direction: column;
            box-shadow: inset 0 0 20px rgba(0,255,232,0.05);
        }

        /* Static Info Panel */
        .info-panel {
            background: rgba(0,0,0,0.5);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 12px;
            padding: 12px 20px;
            margin: 0 auto 24px auto;
            max-width: 800px;
            font-size: 13px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }
        .info-title { color: var(--candy-1); font-weight: bold; margin-bottom: 5px; text-transform: uppercase; letter-spacing: 1px; font-size: 11px;}
        .info-stages span { margin: 0 8px; white-space: nowrap; }

        /* Scroll To Top Button */
        .scroll-top-btn {
            position: fixed;
            bottom: 30px;
            right: 30px;
            z-index: 100000;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            padding: 0;
            display: none;
            align-items: center;
            justify-content: center;
            font-size: 20px;
        }
        /* Mobile Responsive adjustments */
        @media (max-width: 600px) {
            .nav {
                flex-direction: column;
                margin-top: 25px;
                gap: 10px;
                padding: 0 10px; /* add some padding so buttons don't touch screen edges */
            }
            .nav .btn {
                width: 100%;
                margin: 0; /* remove the 10px margin that causes overflow */
                box-sizing: border-box;
                justify-content: center;
            }
        }
        
    </style>
</head>
<body>

<div class="wrap" id="app">
    
    <div class="nav">
        <button class="btn outline" onclick="switchView('home')">🔮 Kahin</button>
        <button class="btn outline" onclick="switchView('explorer')">🔍 Kütüphane</button>
        <a href="https://tr.tabirly.com/" class="btn outline" style="text-decoration:none; display:flex; align-items:center;">🏠 Tabirly'ye Dön</a>
    </div>

    <!-- HOME / DRAW CARD VIEW -->
    <div id="view-home" class="view active">
        <div class="panel">
            <h1>Hermetik Kahini</h1>
            <p>Ruhsal durumunuza veya sorunuza yanıt bulmak için bir Hermetik Sembol çekin.</p>
            
            <div class="card-container" id="oracleCard" onclick="drawCard()">
                <div class="card-flipper">
                    <div class="card-face card-front"></div>
                    <div class="card-face card-back" id="cardResult">
                        <div class="s-degree" id="c-degree">--</div>
                        <div class="s-vision" id="c-vision" style="font-size:18px;">Karta Dokun</div>
                    </div>
                </div>
            </div>
            
            <div style="display: flex; gap: 10px; justify-content: center;">
                <button class="btn" onclick="drawCard()" id="drawBtn">Bir Kart Çek</button>
                <button class="btn outline" onclick="resetKahin()" id="resetKahinBtn" style="display:none; margin: 10px 0;">Sıfırla</button>
            </div>
        </div>
    </div>

    <!-- EXPLORER VIEW -->
    <div id="view-explorer" class="view">
        <div class="panel">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <div style="text-align: left;">
                    <h2 style="margin:0;">Sembol Kütüphanesi</h2>
                    <p style="margin:5px 0 0 0;">Zodyak'ın 360 derecesindeki tüm sembolleri keşfedin.</p>
                </div>
                <button class="btn outline" onclick="resetExplorer()" id="resetExplorerBtn" style="display:none; padding: 8px 16px; font-size: 13px; margin: 0;">Sıfırla</button>
            </div>
            
            <div class="zodiac-grid" id="signGrid"></div>
            
            <div id="degreeSection" style="display:none;">
                <h3 style="margin: 20px 0 10px; font-size:14px; color:var(--silver-1);">Derece Seçin</h3>
                <div class="degree-grid" id="degreeGrid"></div>
            </div>
        </div>
        
        <div id="explorerResult" style="display:none;">
            <!-- Rendered by JS -->
        </div>
    </div>

    <div class="info-panel" style="margin-top: 40px; text-align: left; padding: 25px; line-height: 1.6;">
        <h3 style="color: var(--candy-1); text-align: center; margin-top: 0; margin-bottom: 20px; text-shadow: 0 0 10px rgba(0,255,232,0.5);">SİMYASAL AŞAMALAR NE ANLAMA GELİR?</h3>
        <p style="margin-bottom: 15px; font-size: 15px; opacity: 0.9;">Hermetik felsefede ve ruhsal simyada kişinin içsel yolculuğu üç temel aşamaya ayrılır. Çektiğiniz kartın veya incelediğiniz derecenin simyasal aşaması, şu an içinde bulunduğunuz ruhsal döngü hakkında derin bir ipucu verir:</p>
        
        <div style="margin-bottom: 15px;">
            <strong style="color: #a8a8a8; font-size: 16px;">🌑 Nigredo (Karanlık ve Arınma):</strong> 
            <span style="font-size: 14px; opacity: 0.8;">Bu aşama, eski alışkanlıkların, yanılgıların ve egonun yıkıldığı, zorlu ama bir o kadar da gerekli bir arınma sürecidir. Kafa karışıklığı, kaos veya belirsizlik hissetseniz bile korkmayın; bu aşama yepyeni ve sağlam bir başlangıç için toprağın havalandırılması ve eski kabukların atılmasıdır.</span>
        </div>
        
        <div style="margin-bottom: 15px;">
            <strong style="color: var(--candy-1); font-size: 16px;">🌔 Albedo (Aydınlanma ve Uyanış):</strong> 
            <span style="font-size: 14px; opacity: 0.8;">Uzun süren karanlığın ardından gelen ilk umut ışığıdır. Farkındalık artar, zihin berraklaşır ve hayatınızda neyin doğru neyin yanlış olduğu netleşmeye başlar. Olayların iç yüzünü kavradığınız, ruhunuzun arındığı ve derin bir şifalanmanın başladığı aydınlanma dönemidir.</span>
        </div>
        
        <div style="margin-bottom: 10px;">
            <strong style="color: var(--candy-2); font-size: 16px;">🌕 Rubedo (Bütünleşme ve Tamamlanma):</strong> 
            <span style="font-size: 14px; opacity: 0.8;">Ruhsal yolculuğun nihai zirvesidir. Zıtlıklar birleşir, öğrenilen tüm dersler ve bilgelik eyleme dökülür. Kişi kendi içindeki en yüksek potansiyele ulaşmış ve gerçek gücünü eline almıştır. Güçlü bir tamamlanma, meyve verme, yaratım ve büyük başarı enerjisi taşır.</span>
        </div>
    </div>

    <button id="scrollTopBtn" class="btn scroll-top-btn" onclick="scrollToTop()">⬆</button>
</div>

<!-- VERI DOSYASI -->
<script>
{sabian_data}
</script>

<script>
    const signs = [
        "Koç", "Boğa", "İkizler", "Yengeç", "Aslan", "Başak",
        "Terazi", "Akrep", "Yay", "Oğlak", "Kova", "Balık"
    ];

    let currentSign = "";

    // Scroll to Top Logic
    const appContainer = document.getElementById('app');
    const scrollBtn = document.getElementById('scrollTopBtn');
    
    appContainer.addEventListener('scroll', function() {
        if (appContainer.scrollTop > 300) {
            scrollBtn.style.display = 'flex';
        } else {
            scrollBtn.style.display = 'none';
        }
    });

    function scrollToTop() {
        appContainer.scrollTo({top: 0, behavior: 'smooth'});
    }

    function switchView(viewId) {
        document.querySelectorAll('.view').forEach(el => el.classList.remove('active'));
        document.getElementById('view-' + viewId).classList.add('active');
        
        // Reset state if going to explorer
        if(viewId === 'explorer' && !document.getElementById('signGrid').innerHTML) {
            initExplorer();
        }
    }

    function drawCard() {
        const card = document.getElementById('oracleCard');
        const btn = document.getElementById('drawBtn');
        
        // Pick random symbol
        const randomIndex = Math.floor(Math.random() * sabianData.length);
        const symbol = sabianData[randomIndex];
        
        // Update content
        document.getElementById('c-degree').innerHTML = `${symbol.sign} ${symbol.degree}&#176;`;
        document.getElementById('c-vision').innerHTML = `"${symbol.symbol}"`;
        
        card.classList.add('flipped');
        btn.innerText = "Başka Bir Kart Çek";
        document.getElementById('resetKahinBtn').style.display = 'inline-block';
        
        // Remove old appended card if exists
        const oldCard = document.querySelector('#view-home > .symbol-card');
        if(oldCard) oldCard.remove();
        
        // Wait a bit, then show detailed modal or navigate to detail
        setTimeout(() => {
            renderSymbolCard(symbol, document.getElementById('view-home'), true);
        }, 1000);
    }
    
    function resetKahin() {
        const card = document.getElementById('oracleCard');
        card.classList.remove('flipped');
        
        setTimeout(() => {
            document.getElementById('c-degree').innerHTML = '--';
            document.getElementById('c-vision').innerHTML = 'Karta Dokun';
        }, 300); // wait for flip animation
        
        document.getElementById('drawBtn').innerText = "Bir Kart Çek";
        document.getElementById('resetKahinBtn').style.display = 'none';
        
        const oldCard = document.querySelector('#view-home > .symbol-card');
        if(oldCard) oldCard.remove();
    }

    function initExplorer() {
        const signGrid = document.getElementById('signGrid');
        signGrid.innerHTML = '';
        signs.forEach(sign => {
            const btn = document.createElement('div');
            btn.className = 'zodiac-btn';
            btn.innerHTML = sign;
            btn.onclick = () => selectSign(sign, btn);
            signGrid.appendChild(btn);
        });
    }

    function selectSign(sign, btnEl) {
        currentSign = sign;
        document.querySelectorAll('.zodiac-btn').forEach(el => el.classList.remove('active'));
        btnEl.classList.add('active');
        
        const dGrid = document.getElementById('degreeGrid');
        dGrid.innerHTML = '';
        for(let i=1; i<=30; i++) {
            const btn = document.createElement('div');
            btn.className = 'degree-btn';
            btn.innerHTML = i;
            btn.onclick = () => selectDegree(i, btn);
            dGrid.appendChild(btn);
        }
        document.getElementById('degreeSection').style.display = 'block';
        document.getElementById('explorerResult').innerHTML = ''; // clear old
        document.getElementById('explorerResult').style.display = 'none';
        document.getElementById('resetExplorerBtn').style.display = 'inline-block';
    }

    function selectDegree(degree, btnEl) {
        document.querySelectorAll('.degree-btn').forEach(el => el.classList.remove('active'));
        btnEl.classList.add('active');
        
        const symbol = sabianData.find(s => s.sign === currentSign && s.degree === degree);
        if(symbol) {
            renderSymbolCard(symbol, document.getElementById('explorerResult'), false);
            document.getElementById('explorerResult').style.display = 'block';
            document.getElementById('explorerResult').scrollIntoView({behavior: "smooth"});
        }
    }
    
    function resetExplorer() {
        currentSign = "";
        document.querySelectorAll('.zodiac-btn').forEach(el => el.classList.remove('active'));
        document.getElementById('degreeSection').style.display = 'none';
        document.getElementById('explorerResult').innerHTML = '';
        document.getElementById('explorerResult').style.display = 'none';
        document.getElementById('resetExplorerBtn').style.display = 'none';
    }

    function renderSymbolCard(symbol, container, isAppend) {
        const stageClass = "stage-" + symbol.stage.replace(/[^a-zA-Z]/g, '');
        
        let imageHtml = `<div class="symbol-image-placeholder">[Görsel Alanı]</div>`;
        
        // Örnek URL haritası (kullanıcı linkleri verdiğinde doldurulacak)
        const imageLinks = {
            "boga-3": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrgZFKhlRDIzpLlHigqUvX9xWju5SJ9YzMGO_5mjfFTMpjzU31BU-LKUhXyzw3bAbWD92GMS5SJgzZHMU0n0nf5yfVIFYgXRmkVq1sKNSPpbOtcq15Gtiq0aH2yke0fM8mo71Fi4HC75Wo0BOSWMEdIHQ6Nmu5F99REx6AzUd8Z70YXN-r4WtFg2lY_Lw/s800/sabian-sembolu-boga-3-derece-rubedo.jpeg",
            "boga-2": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjeMQenqdsY9m9POUqqMP9jJ9yEY6bciR0vgSKXoZVDjIX9GNwyXOVc7ftv4kon5z9zOtxlg6ynK1OR7vuLOIjQbNDdSw7YU2EpDi6hCVP4UHw2P0m8Ci_lZDsNbD3oSVlslB8uIROOqQlCfPoM474jfzqKxw51HpQGT6y0riT1tdgNKqgnv74740maKjk/s800/sabian-sembolu-boga-2-derece-rubedo.jpeg",
            "boga-1": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjkunQlwpULv7q-lHDjryiLoC36sRxKoWjc3QxSQ5DeR4rgoOceF0o5WgZ9jo_TbwUjJVvv8-lTa2K1hoHyJQd0NIoWNjTm4jdhfltGB70NsPbRF8FJyKPh-KGeRIgqk-258rughdGS3cQKLm-OMWw8oKWDEDLOG12XPGHDzfOBoWKstbVlPIbUYgVksxA/s800/sabian-sembolu-boga-1-derece-albedo.jpeg",
            "koc-3": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjBgf6BC8DsgL9NoKfPh5xs8S7UBBV7vkGmQfoQpd0mOeMYn_UUJazBMtAnlf1phaegF0xKkfuVqyPidSzYtpIMUV_EFK7Q0HtPqywQXOLkALXVqQHg1T78l6Q27wR_tLWOh8UK0maUhJsfJInzqV5g8eXPSNtF2RqBoiYhC6a6OMx-cObLQqj8rIKqguU/s800/sabian-sembolu-koc-3-derece-albedo.jpeg",
            "koc-2": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxFSOiqUx3g6WYmMPuazqX2AHrpXCVaYEoXsC2c5fFW3VnGkgwranfQt9013CWkazB-aLnQg0UNPyWetgwYUT7VJfbUnofULlnGS8UqE_GyZoFuG4CEKYqz28Qg1yspuoHUXc0JQ7YV3OO9woUR6J-FTr6QpqbKZ0LLgpVlLfELQcocTlLIGPzImPM7bQ/s800/sabian-sembolu-koc-2-derece-nigredo.jpeg",
            "koc-1": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh41wduPTnwiuRoopcaTT5FTtcphWAaScER6KaTqBdS_hxuGTE8xWb-HWUktmNIuM-YzvWS0yxtxv9PVdBv3ag2MUaUyHfzD2uK3Nlqj2VwBp4gv9a1mBQZP4o9fH1wRjG8EzcYPE1njoCfFS0RCm8-5S41ENRLkpJHmaIwy7BYc-e7jVLLD-IW4w6CVds/s800/sabian-sembolu-koc-1-derece-nigredo.jpeg",
            "i\u0307kizler-1": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhBdgRDJbQphuJXSWWduElgNnt50MOEBn-1ins8XuHThMlNQP7aiL0GzmK50-urFdndCK4J5AToKM6EsswL3Q3n6lSqUgqqJBzYGMMTdHO5_Y8Q2TG-dnXvhrs0NX0A_TpTRvWLsEETuLnkuXfE6sO9oUzQO9h4zGvUOYFOG5AwrwJy9R07ELRgfc7ElCE/s800/sabian-sembolu-ikizler-1-derece-albedo.jpeg",
            "i\u0307kizler-2": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvQFK5KMchJH4UDDLmH3jQTsQMu3SrwiYB9OFU0b5D99_AD1tPvQa4PrGEJrNqe7XCS6cQphdzfgrT8b_AJDxFzpww1qgsBpLyuH4kC81e12G6hBRS_umIwyvdwDdzyBx1Zeq62qrPK57OIeKfXa6prS-GbWSxoVLb7XoemgmOwPL5A3y0sXtliGi5h4s/s800/hermetik-astroloji-sembolu-ikizler-2-derece-rubedo.jpeg",
            "i\u0307kizler-3": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgKTYRBGY0L-QyCbh8Kmdu_QxZc3VRoqzDNWA5xKmph8z3Z919dHa1QW0TJhxqrTklK6N27nTSVrZxRCRqAkNnn7VnA787zowAzwurbA1cH45ChhL1lpltk4vKCP_cF2z_ggpXt6xhxLQCWGFdXFXbBmjSjdK2Ew3sAT11UUShtLZRyJiIYr1JRlQjw00/s800/hermetik-astroloji-sembolu-ikizler-3-derece-rubedo.jpeg",
            "yengec-1": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgBOcJw2goyDth8IxJPmV8cFqcO_vQspPvoEJVi6cET9WfCFOktZmNCvYFafQ7Uw-QNh7W4CMUbuv4DBNXfgMoDqWljlz-4MfvIUv8hN0O3YPh7r6bvrWLTFqCgCMeqRFfQe7R-TTfUD7BQuxZzD0IkiyquFNcx8ml92Qxigqp1zj2Ch6iu7Ur3QdZg4GE/s800/hermetik-astroloji-sembolu-yengec-1-derece-albedo.jpeg",
            "yengec-2": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgeTkV2gK43z-sineAh0NjlJ7IfqlSCGvKDYDeMZ60U2ra9umQvUOWYiY04H82OFZbqlfNsiYb165Z1yfkSw_ILTJU7XmH_72ErSUPizY6yExY3oYU9g23DdR9Hx3uCSDY3vbYfsEJiw_M7kzP59Rj9OMvbdD5u_vqI-WXyTVip2XeIkAlb8UYs4Uax_A8/s800/hermnetik-astroloji-sembolu-yengec-2-derece-albedo.jpeg",
            "yengec-3": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivmZA6yRKvAdeuog7He_GV5MP7IGUuuKHMLaLGlfXGXKjz_cwFiii0DBkfltpw1EN7SvYjITOR6Df0rMUYfpc5ohxvqtRBwe_3vf2YRy_3jWgKl_Xe-D7gJd-p3CDlt3LSUtjRvEz_BtxIrIKFxrgROfZxy1LbPIaDGSFIvEWWemLmqwEFJOP236M9Thk/s800/hermetik-astroloji-sembolu-yengec-3-derece-rubedo.jpeg",
            "aslan-1": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiAutynexnYCihJQEEa8rk8oyzWN0T4BWJvspZ3_FfNxepOx8GZm4qfHie1Z3YSVKsSxpfyqRGEPVRYaDyMKK4XdOGf2lmgom7eDNcQ8k0MfZs_nbCKpa4oWH5g-0gqljO10Rgqxxuex9_uoUPNM4_spJiIAwlpaKS7sXzksHqvLk9Hzu56JEBFHgjXyzA/s800/hermetik-astroloji-asembolu-aslan-1-derece-rubedo.jpeg",
            "aslan-2": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhz2Jy6VQL3ORwQMOVqJ29D6jC-aQKczxXTMSEO_oWM8Tzg0jDZ3EiRvdAQlEjMLScbxYnu4cWEcfG-qCuccNuqtoIvUREIeckiVfVBaN_Xj1mP6LKn0knemd6ZYdvDXv3qDEt1PUh0NVc_fwfkDFzt1quUI2PT0jqhyphenhyphen1aEbJi0QMTf2mPnt2ddLrh8PVM/s800/hermetik-astroloji-sembolu-aslan-2-derece-rubedo.jpeg",
            "aslan-3": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirkFjoCy39o5XM9XqMHjPxbsuVlwNTN016-oVnOvEVjTezm1WN1-FhJvgtfllPwQB9YOYRw47pCJUdpZXZK0O-tFFRmuc7lpaSPDzWB7XMwXg5qKMMkrDLfQ68rDkrBAR4wwfVf5vjiF_NpNlacxTEX5lXWDHIPRUgMfqCtKx3Gl1r_Iky8q_lQiC17uQ/s800/hermetik-astroloji-sembolu-aslan-3-derece-albedo.jpeg",
            "basak-1": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhemuAFQzS8B1TJW7E7vnLsqQjKB2B8MHpJqdv1eAWWbyhgKQ13AC_QvaT0fRpcuIAXLwqyLqaCQuGz3APfYmXTkZ6odcOCHQPukug84YJ2UKFPr2XZRzrA-eHFDrfVdFf_qEMGdwlP45sZHgqLDE1u4khIGnba2J__rHE2SYREkrAApcGwaAUpoX-GZFI/s800/hermetik-astroloji-sembolu-basak-1-derece-nigredo.jpeg",
            "basak-2": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEinxYYp5r_TDgoy3lNEJqOEhj3sieZwIoFsp-CldWtepV-HNFB3mcCW-EHWkos0YbvbDJ8ySnrLY-HbFQ6UztZcKL8oDT7Z_MPO3WIDvsS-TJ5eOBVsTO5BDjZJf2_MiilLhjnBMMGy7IZlqrp4lQfxDadyfAIAqqzRACWQMgmF9R-BNPU_Rcz8s4e3vio/s800/hermetik-astroloji-sembolu-basak-2-derece-albedo.jpeg",
            "basak-3": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWVMlplhR1yK5dwGpEFtNLYcXkq7DxrEgI7_A2Wwx8rO85CsbAzUMCBNTlKhI9QpRHKLUOpMdzPl_jRlmGmnmruwOP5WiTFbHIaOKWCEUWrzD75FHkBiQDvhrZYRKf93JOO65RlCJvT9YzHxaX8-yaY8z_qmVU95Ds04S0SLuc7NCUy55Ycq2BEkoHugQ/s800/hermetik-astroloji-sembolu-basak-3-derece-rubedo.jpeg",
            "terazi-1": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisMVbQI5m0HQHpSymR6yHLbZshusn9uDNEPumexL5g_q5k91Qs1fiPkMF2ReOSA-MDimmWRa68tOXmV9no1IpRgNFbpZl1UG3aWTUVep7A9CR2wXQQ4338VBTbSJPbz8mP9xb5NH0UCwaTZV6s7luRX0yKrpZzNxM0Zcf-aq026iqrTEd7czaZhSHrbI4/s800/hermetik-astroloji-sombolu-terazi-1-derece-albedo.jpeg",
            "koc-4": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEie2yMPQGv_-cRH7AzX-KqDC0fy8IDeGK1jjo1JdExR9lDaPbZ2EXP6_zTh_zi4J47pvK22jarGYVZ7uG4ZXtsGzgfDB-JjlLSQPaRq3XCd9c1zFSghQSFSNnNC6k6VxWgLxmdWVV3j9JDA5m7kLNey9W2us5COEyaLqse2ZA_N9jHiez7GxDiveaIr-rI/s800/koc-4-derece-taze-tarlada-yeseren-tohumlar-albedo.jpeg",
            "koc-5": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiISo914tZEsXYA7pIR9mTT6zB9KyJxLE1jUX6FScGX88uh-QUJYlrmY2OsPVQPa-a7Oh6LI8xLvmFs0f_fVAXAdvutikPiTo20CUo8kAZnl3Zb6Dy-JfliFE0S17LrqBNmSYoDNYOaUcc5KswtJQq79WoQvwebkJL5-r5Me0XhbyZvaYUPWeZS80aQzrw/s800/koc-5-derece-kanatlarini-acan-kelebek-rubedo.jpeg",
            "koc-6": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibjcuNdXpTi0_kQ4mRNJKaFJ83ovEKSSIx8NVl2BzToBqm1JbKQlwxua4uj18kVg6Zc3CYwjC8Ew4Iz7Eyz_G-hmfcSWcr4xyjK1PQqqtBw2QRUK8l-fvr9zKnBqoEETfYJ0KRBgZM13HxyE9wd5n5FHHbtiBIq7BoI49ODXbGF6MwwktS3Umq42vB2Og/s800/koc-6-derece-adam-yeni-bir-ulkeye-goc-eder-rubedo.jpeg",
            "koc-7": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgqjaEY2E5DyRbLc9zj7ds3g8YaSRo1Ii8CI4eMzLVW2ThMZ6phErOrwgNpNM871Y8TZTWkxHTi8LSVkA8iKSEcQmTMuW-PIwkjCa4TCcF2Y6UqxbB0-4Tc0UCY3bU-J8EVLuxKX-V1UEto-EkacNviu1OJXZvZpP3oQkKbJ46wCwyB2XxR4n8AKRQ-ZxM/s800/koc-7-derece-kadin-su-tasiyor-albedo.jpeg",
            "koc-8": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_jc5LiDSGcK3WMrAibnXWt37C2QJ0iYu3Qf9Ax7isiRcqu5R2jPruf8_PKLXELvAnh_ZSpw3DZHCE4PTQPrNu5soPuQnmtPQMUGvpALyfnlHmNUGXxse5A6SfXcdUn-KD9mEhLWiAx4RSBGKHZg2s1ps0ssbZetO06QIT68J6vMitJskekfpOB0DyOPA/s800/koc-8-derece-kadin-sarki-soyleyen-kusu-dinler-albedo.jpeg",
            "koc-9": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiEhV7sdKqcBPnjS-Rgnl4w5FReVx-z9_Mhhm2l5Fd3_kQ1B3BBx5_6WrumuyR6WG6O1YpMnoNp5Fl_1Nh5T5zgedywR2UizOUE_bqgfjgmK7p4-lNiqENCs271ffUf050FkRVA1GzbrCRgj7x-DubMfqyb_nFuUoixNcYOsY5toG_NVzlFrIt1ZIu3NzM/s800/koc-9-kristal-selale-rubedo.jpeg",
            "koc-10": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjV6482XZ3HhAWf6TNBu64_U_oKxcpGe79arG9u91JxB8RNDrOX4jmBpRZWYL6wYKmbPNbTU9WvJ4H1yRd7FsiEB4-JOPPQGqdZUPXF3VmeCU85VMhx8eqWfL1Hl2LDk7RALoFf81Ezfks7vS1VE_5enxFzqCofdZUS73Ps0aRuhF-ykde_KGwxolklhH4/s800/koc-10-adam-kendi-golgesini-inceler-nigredo.jpeg",
            "koc-11": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZfxxXg2DpVa9w9OI69D4rB82ZDu92wd8weSRqzrPpSB9GCAtNHv62w2j0MAKKAr2_mIGQ7Uv3tUTl2qgv9qmMnmZfz1Ov-APVloHyQhgiBBqGlaluBiq-ZttDXYCMJ7oNHyOgqnxiSnd25Gb3sTayEY9ZARKyL3Rgl-HHORJ_Swl8ThD_xpGJi5oAVZU/s800/koc-11-derece-insan-yuzune-donusen-maske-albedo.jpeg",
            "koc-12": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnQhafN_Va1-px_Ack4t7O64fkgim3G0T53_kL9KOs5r_a84KOvgwNLbhbz8S249D1S3S6LZ9e9f6hvGDupA9uIFSyv4sQ0-s7d19rbqMqd33m5Ks7alHdropkik6KiMqSMq-2gmPjHxvLBL_wI2jq-BLXSB2DvQ-6wcFnk2K8FWGKVGYw-2PIsfP8eC8/s800/koc-12-derece-vahsi-ati-ehlilestiren-adam-rubedo.jpeg",
            "koc-13": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitilLZGFbR2EXnnAJn8vmKIr_iPRpzAIBlnzeXqnectd_PwpQ59MUMEbFK8q6d4J9CKBHhY_S60NWEt9NVG07RG0yEl2264X8tsHsbi7WMh-BThiPnv5o0h_JbQyzsy4HMSW0aUQu5A7lR4sLRilUO7mthkD8V6HGKoQ9Bt8oW2ft8w0pVYB3hPQA1Bsk/s800/koc-13-gunes-banyosu-yapan-cocuklar-albedo.jpeg",
            "koc-14": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxmyl39l_5ZBlkStOHogMhDbVOZ2AHvSzhrchZZvQnzDr9X3As9jjZuvg8BUXK0vUBcQ5oXFQNUTZ2zX4aMPZte36NUltybvOMHYXQzbNyq6kFWwJHl8KPJiFpKoX9Aevj5MYd8F8HWdBXNZDPN7mY4p6Sn8ABa6klL2rrzU1fWtTZ9Im77RnXOW6hLcY/s800/koc-14-yuksek-dagda-bayrak-diken-kasif-rubedo.jpeg",
            "koc-15": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhw1jX-J5mju_FTU3Ah22rhg7AXYGcbRorQ2IzgeMNaVd7BFGsAz-kKVlna-wzSPO_j_fLuZIsyWe_NC-K5XCIkHDkbyt8uwvrXSCYV6HV31xPcPBkMQNuk1M0EOXtHKHNuziOXK9mRL7-UhHzuh3yo6V4pplMh8L6cj_A1vfnKjYcLTEOa6hogt471lDI/s800/koc-15-yanan-mumun-etrafinda-toplanan-insanlar-rubedo.jpeg",
            "koc-16": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg2AS3SUfRaEFKXaHYj7nfMXfZqSTCgbdlgHBA8cM0wpf7Rn7Ubnr6enfjAAGErgqr2yy8FVcTRWT8a18NBcerOQOXdwS-uDgAMEjw4DWqFJcpabiEFUQs8_v3IuLZJr8k4QSo_UY3f9nytL9Qv2smYeynKR_a137qYJNR7yQ5tCjhcnxP-mrjIbzBNQyA/s800/koc-16-dogayi-dinleyen-adam-albedo.jpeg",
            "koc-17": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgmKfrgP8RR0IaYuBJAon8bLKtjqoBsEEJVWyilkYkFDC6kGXmwvIxNFz0BajmWP_QoYyKmEkx6Xm-Y2nlVVDyu3gdPLZZycjDrGuWylxrUFE55Kh90zgU4K7uIg8SSXT6l4XhkSpCLOay0VzP9zI3vUP4ucgAITUEHboWErR0UD6cob3iJuyjRh-OnCdQ/s800/koc-17-kadin-ruzgarda-dans-eder-rubedo.jpeg",
            "koc-18": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSQqWFaZMGvRLuDcXnZ2TR2kVrA97aqChJjHJBKh7GUetNAB7sWbfGxaiztf90Ylo_dYbjFmQ9NVg4T79txdoaFvGaeytfIyrf24daoROOR4h5xqOyfgW-ud4OD9D_EiAzRMW6ChrN8BXUK68MBft5u88wxNdOGNjNDeNksszhCOinTJkN_gpj0ndKFVA/s800/koc-18-atesle-arinan-savasci-rubedo.jpeg",
            "koc-19": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimx3f157A36cUPpY2ViAYq5jfGwWwSae1FGerJqeMyfMZk1hF0QrZ6Bg8colFVr3jWuIWlBzxQEArRT_N7MVdvjTGPO_9a2K850GlcRRTl-9M8ffVNbWoFiIhtbtgJxNvuZp3atayf07BHho09x7pr7t4ckXG0dmPaeV2TfEDWQf2oh13IHtLHQBwVH0A/s800/koc-19-dogal-kaynak-kesfeden-adam-albedo.jpeg",
            "koc-20": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdEKIN-S8Ziz-NsWbjIxWdbXQXMG2u66Pwb1NiKVA2D-4Hw-Yc7NEPLFkzQw_gxH9-gQPrTqPky1oWlH5c4H_xi9ll7alIT1biYuNQ5WtZYUFtVtDhs9js9l3UMiLIGq4PjFR3T2Hk4b_5z-w6kddoMFNyiij30D7phIRATEm-cv3CCl7KBhlpMXNpNGM/s800/koc-20-mesaleli-grup-karanlikta-ilerler-rubedo.jpeg",
            "koc-21": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5YpjyDypx0ncnf8Yhbd13-4OX-a2P97Ps6-pMIh6bVVh_ux0MgttJAWB-xdDi8V-1Q7jOPxmquDGryiCIY3Iz_bUHOUu1MY22f-8s3dymJ4Kf6cfWzqZDC7wz4NbpQ-uqJCJWKFE58PyriNbdKgP176TzXQ-kuZ-6msb_R42HHYBPGlLuz3SvWSi7zhg/s800/koc-21-isik-sutunu-goge-uzanir.jpeg",
            "koc-22": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjMzKBgGIQlwekSKtZjQ5Cv3rtuy5e34ZbSy-ptHLGi-y__stY9Bq4GD7lv-jd-oUxksqm9exFMqIF_FWdm8Kt8yL5E6K-HUH6GxljNchK1LyBNTVUpxkS6gjXv2B_meWlzzzrViywDf16dOARxRtzz-0-hY5VgSsiBx0GgYZHzV15qKqrQ7tkw37VA9aE/s800/koc-22-mesale-tasiyan-adam-rubedo.jpeg",
            "koc-23": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSuIymTiFFH3sPsD48kmX-aBAWTt18h0j5FZyXtVgZANI8zWpWc21cSgkX9V7ItsM6Fd8qGfNpdVHo776XTVZfUh-TaDLYrjMBZLzoyAA3HhWFDHoKCQxGLSwa4rogvT11F_czlM5IiKCw4akbvw7ERMOA3L4P2bc4OXNg-1prLdlNNYD7dC9ykyg5_gw/s800/koc-23-genis-ova-uzerinde-kartal-rubedo.jpeg",
            "koc-24": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlxp1M_7n1_8AHdpiWlBWUUjCJmcY2huU57IODNfXROI6oDqP-5Y2gPBNf_fvbU6AqWv39a8kr3rAnxtF81NOg-m4ac1i6RxPNxyL4qLQr4SuUSKBx9dQ60tXCB7ozQdYUxUStSiSrz8Ct36cpJh9-Zw3QK6fLPYxdnbF86xbozbpJntftABRK-SsYrJ0/s800/koc-24-kadin-kirmizi-bir-gul-tasir-rubedo.jpeg",
            "koc-25": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjOqU-gFjQaH8NbJxCbraw5iTmQW3aKC62fGVLC0yrK5hiqtr61CMwVxx2jYnGM8w01QMm_eh8_pLHxDqyIpwyn3hABXz4CMjKcH2xNW1Hn-9maCwI2ZdFu22dnBCnuU4gwdjG_eZws1pTIHxNe5VhICszAE_DTt9GNvtea1tcJ5Tl2F-xM45nm5qWjODc/s800/koc-25-atesten-gecerek-arinan-topluluk.jpeg",
            "koc-26": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzrzcLJLym94HMYOR3zTlVOG4OQNn_qFi-ECUw9099CnMIv_9jVdGm2msgvg7IWQOrmaandeIt_Pzi_o0EqGfspRiK2O6UCWPjDIwUb4KOu4jAaIqP8C8XkcEcBgPsPjdKyREKt5YkkA_heqSvfbwUb0i5ExCUO1WzsjkeOW0JztXe-l4ByLQ2CUuE8zI/s800/koc-26-tac-giyen-savasci-rubedo.jpeg",
            "koc-27": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiyjaviP2ksmRgMB_0dN2Wh5wt5KS38I7L_O_R3vcGFAth1lfi5qkgdJdmsGbsQQRqYpoLKNdo5yXayXgDPHhh8U1agUMrbOZOEk9_o5nubX2TCp4jly0GRN3QMJqFZd0XKzCHsA_uZdc2ahKgDt1dkji3GidazZ8IQVX1vX77Au3OTPFoelwj3us4NiMs/s800/koc-27-goge-yukselen-yelkenli-gemi-rubedo.jpeg",
            "koc-28": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6V7D2JomVehuSFd-XL2FyeAk2LB8TVzRIGkzNYpZkxW6qrpM75QgwEHcUy-lR0agWxO6W1rPW_AAlm55xDmpK0dIXahryTmXKGJH7Ac2mX7tFU5vldHhpj8xk4CBbWLgyJjW5jVJRe4PpwWrtkpgFQyYIOXYs0vme1JILjkhsgHvxx3WhdbZThv67Uk4/s800/koc-28-tapinak-kapisi-acilir-rubedo.jpeg",
            "koc-29": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgUvHgpwtiJ2BfNwnM_aKGYXXWSsz2FWCRCk2QLSIZ2UkbZdsuc4zYMrkY7tQHMnJExTjdOP_tTIC3kV1MYKETiWeqnvOqU9lyrxJxyKlK3i7HUJCyNgFuPEzoV7vEFLFoiiaJ34_SDoyNnXIvXPFjt9m5Ehli_NmUderV7imH7W1ao-hAqBS6Z1eRV5Ro/s800/koc-29-kutsal-yazitlari-okuyan-bilge-rubedo.jpeg",
            "koc-30": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9qoHWsCQEt-wDM-wCu_TK5HSDYRwePAV5fWvpaNxpUgH_W4tT4ixOgiyG5MnvUYRVIrcFBHPy4IP-MQtyc4zoV829LLlFKhcTK2-j50MH4kX1oVY1GuXQAfoCb2OefMgSJl9ZJKjH3f4VJ8tonQCUA7z8xNjhUIyFF6BDNz2MxkLn_fzK8VoohJe-iiE/s800/koc-30-altin-bir-isik-halkasi-rubedo.jpeg",
            "boga-4": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZ339CyLmLYyt1a6sm8ztK-tb_tviE0XRC8ot6JNFBWqk7_3bvxmT6PehorefBW8gr6bJ5MSBHf6ajrba-qmNbhrEu_Wz0HEnjH-Kus-rM5uqFVT2shxdTg1tAgVxAHFfjPBrDlN5Nzzz_J-dIsuD-Z_54jhBg0qt78MqD9guQVMqBHWQy8NrjmDBHNlA/w600-rw/boga-4-yontulmus-tas-uzerine-oturan-boga-nigredo-tabirly.jpeg",
            "boga-5": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgAUBtu2Frm4BMeU9mdVYdvKjibw_L_gjvXtAaV9tyfpg7_onOttz1NPKRj8afZ6KWmsRkYvBbB0BXsC0S90nNOrlI17-Y6ZlnyACHGNtyHUJCEF4yPoE_tCzdw_2rx-57WbuLHJ-ZJ39epMHX_kwos52iBVGH20ZBWFjZSAiV7nfHVWmf35i-4sJY2cRo/w600-rw/boga-5-zengin-kadin-albedo-tabirly.jpeg",
            "boga-6": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0BonrK8d6lC8Z3CiSIFBDYmlr7caBPmZlO7EyHvKR46f7H_Nq9YmCa8z9kH_8MNpxvnOHl3YBKGkRYoxmbMWDa2UkVuFWVzDCJD4-ekOPMKgBPt9bcHFJQyRzDk91ED-fkZk9rmb2d-06eq4aFTysccqPHSIloZaBljIIo5-42WwirGGoOWU7kRA_jX0/w600-rw/boga-6-altin-yildiz-rubedo-tabirly.jpeg",
            "boga-7": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXvlPxK8o97e2nV5EnDSn4MELWVM4YA7CRsEMk55M31ew3ORfOdEDWOfqyHkYBPArr6fwUslvC-uFbhu7Tj4Av11KiaJHpaZRean0Re2omOEatWl6ylLeLOS2rD_7KZVi585DJBYTMt8c3clgsiwnUKxyT_g9G4M4Ojg84CvYYFgljYD94ykhtlCv6GhA/w600-rw/boga-7-insa-halinde-tapinak-albedo-tabirly.jpeg",
            "boga-8": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEib8naS-qJe7YFPgQ-Y7ITGbjouRNV2DLi6gTjn6vsuOgOiKyoMUTnPQUxxrin65GyA23_CT7BO5TPyCdKXeVg_BFjeLpqb2MGxPtzVX7Cc9eZA708mwo3Dkaj8kquWCBMtWzmZmf1j_lxtgdEUPKQeFd2IfssEEqu0TAt4fIZs6W-nzRWMDwTQkqhuyAc/w600-rw/boga-8-gul-bahcesi-albedo-tabirly.jpeg",
            "boga-9": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEieAreDNxyHWODnCY8_HWArPdl5jB1px5b883EWwLK067VR2AYCe9s7f8pyI5d_OqiYHAnj-6tX5wuHEA3Wd5znR3Fi2uOFBsD6HEwk5H3i2FeMlppsCirAcXRgMXF-96_1-LvvIEZwvzwqTtQTS6A824GjemToj_elMWwEnbBLcH-EtaYWOc70S0_vk2c/w600-rw/boga-9-cift-toprakla-calisiyor-rubedo-tabirly.jpeg",
            "boga-10": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg0rFQfOmZ9GxVbjNOBgMCAmCzOkSukVFHt-YHwfgYWf7MZXV-UaV9L5Q94L4M9_ghtdLY93EvCJuqPrt-FfG3fe_O-Y_t2jodlnthSoSckErIgoa1dkl67xPDZns3FC4ds7d5AZo6WdZBYn-FZT8wfv_ZtKlrR7wPKFulEedvkyfio54O082ZuQNPU7oY/w600-rw/boga-10-coban-surusunu-yonlendiriyor-rubedo-tabirly.jpeg",
            "boga-11": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8_TJLfNmMpVZjNqGyfBHgYqBMAkurRK9xGIyTpt71D27DWi55rdv78p_L0EZaxGiX6LCIUVf7612HfOQ7mnzQZp46M5mqpttpR0OjgNa9imW1-D_J2hWLReJ_0n1oBU4hkU54Ypt62NLXZ17KAmfjM_br9Gc4FuDIWw2Trkim_yvDCFrLg3XKfZzK3mA/w600-rw/boga-11-sofrada-toplanan-insanlar-albedo-tabirly.jpeg",
            "boga-12": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfn_qdZ-_U-sTW38-iMnZsdxyjPy35jx9gsnKNjA9PWF2PxBob7V7C3C6bNOR6seO2yrzT27fea-DNhxwtQQShq9CslO4qqIy8WiaPQ7cX2UdCfj7eNrO4pPp3WtIu84G1iXy1j5CQdM4H2xux-ZuaQcuh0Xbpz7UIo2YRYO0JFP4RoITnOR5rSKZ4HbA/w600-rw/boga-12-parlayan-elmas-rubedo-tabirly.jpeg",
            "boga-13": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_ir0DosFiHd1vu3NxqcZG2Sx9NWRQ5ajGFmrNpMArw5541beAu-JI8B0u_VCflXgLLkrhn2Ox-YgomNlo41BskktFB2UQd_qcly4dvGllDQZP3eEuJGSqe3ZtzUgzuIzn-F_EGCWbWr7li5sOyk_YKT6t1pz8ezY9DXZTtjY476btqhNZGcz7owQbf90/w600-rw/boga-13-ekin-eken-ciftci-albedo-tabirly.jpeg",
            "boga-14": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPz5BVMs1QpPQdzmdyrw8lWYmDunel84r_WzxiAdedh5Zf60PfghnERfPEfLlKMoXnUymfC169JPYSPxKDR9fjIgWqL3wxozzqCFJG4oqHkUAQiPnYxibSEJcZrkC0ggXVPi_RIVfVEvVB_I-Oz_sppS2lHOX8dLeeki8BMKHiP5wRs8moI-zhcOAKMRs/w600-rw/boga-14-cicek-acan-agac-albedo-tabirly.jpeg",
            "boga-15": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUtqkzUIZL3fvg-R4DQnwW5zS3VE8lhd-eQxbcww_vjCfiyvOEr0Ob5NgkvzxlW3_KWEdJlmaPOzZH9PuJOICo6r2-T3ald6MdAJbEWOs0gdrb9FK1AZnQvu_STDrIRvTJUtA544bk06_YJ-J8_g0klDomzlz9MREnRyOSSjN8I_kLUcvibT8ASihtjZ0/w600-rw/boga-15-cocuklar-halat-cekiyor-rubedo.jpeg",
            "boga-16": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhT2-Yxpu_Rymd8D0jhQ33CzATY-vi4-jxz5MQHrSyLKEh2-N9TfntWSfEw-HMd8znRfyOSCLC7nQS51Q34psREIfU98phNd85bZFeYlqb5RCvTLSxC_i5hY9OhEv7kruCMHi-Q6HBfATRaZmH435zmE7jW68TKXo5vSnM3-Qka7TSk2SBOlI2fE7Xb-KA/w600-rw/boga-16-kadin-toprakla-dua-eder-rubedo-tabirly.jpeg",
            "boga-17": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimb-W3CiDFUjtGBl-8sLoLvCKKgxajs4XfU64XkOUfFzcLdkHAHd0rx8yLNk72BQMe85lyn3tIpDkoHKdlABysQntRiR2EGHYYW6Dh2cbwoVib4R7qcTgT4kOdlSktr4_7UXrAGI2OLlNgWVteXQlszc8chFCrRsLjbIrQYb7WFj04rwnjL4JsHrRHpK0/w600-rw/boga-17-inci-takan-kadin-rubedo-tabirly.jpeg",
            "boga-18": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgme85Mn4um9_JHGCGCmfcpF4EBQLXRim0-_nld4KiCRINn36MCbjnmjiddKukBtdPMS0DmAx1NUbux9JxxGFQeqvxSht2Z6wsCPIDICxHHChj1HYwzSAIx41YFeIp2UVaeKrcHCGSrKRkbRZYjjd3SnDXpoRry_HeSZS0NUR8Ewj2Xnpbl5PDHH6iYCb0/w600-rw/boga-18-pisen-ekmek-albedo-tabirly.jpeg",
            "boga-19": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8t-eli9iXCQ88QrSdIKbEjJfN4Z5R9qAPkE5z_dIdbJ7B3E1ozw9WdMd4Po1p18xYHDMNX28Zxn9ok2XGqV6lV8HMv_-ubOZKHn1avHq0aNwPcDzfNPsXxa8-tAnFAEsbHcpc3PxbSPxFSKSwovIYUpwmEKKLMsLoCY5V49C-NDg2PXixLsBrB5f_0Vc/w600-rw/boga-19-tas-duvar-oruluyor-albedo-tabirly.jpeg",
            "boga-20": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgLdjbs7zTjTMvAmvY8eI-OmjKNqg1XsKH2KHD8F9DgJ9cConxleY2-o4RBiyJ9Gg4x5n6DduLYo29E6Arjj7unq7hPtNp34M3448bcOy_e6pG6N-3OaG4HIjpVZJic99C9I-UJ6Dfxim2OyWFTFctNAB2OgXyNL96bD6reMH8LiHfUBPJYkXwtgv-UbLA/w600-rw/boga-20-ay-isiginda-parlayan-gol-rubedo.jpeg",
            "boga-21": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueNmqVLKE4ml-B_qyVSLWr36LG-8q-9fn9wIsuS3jbbXmsSeDBn3Jw4cpSvXvMLo2GpJg30KcF4tSvrokRSTLqhrOMZya5eBPn3e5LXRiZ2ea7c2tYDTe_evIFQcwHe51Aygn0BlmV-lN90-tMdhC5rvM-ad1QRp67T4fvNHql_i09tViw11bq9-tHHw/w600-rw/boga-21-topraga-gomulen-tohum-albedo-tabirly.jpeg",
            "boga-22": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikYU5ZouGYTnHIuwU5RMu8BbbHDylBpb3adB2h8nLDmnsrYnN21dvqWdw_2t0jYTdTKNggkA4tKurwNdMnbtQCS8AFyRleq_r_tqXIg_JGw6ao-EwVK4gpeaTd0EJBYcqF11pRPUwK-5lQ0ljBjx5esxFkWlQ4ey3Y9YfSDSQNyKCpsp5fSE5G26FYf4s/w600-rw/boga-22-yeseren-filiz-rubedo-tabirly.jpeg",
            "boga-23": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVZNt6PiWC7_cWcw1NIF_VluTLh9kJp9UDpOT8tJBzOaoY67Sin3Pfj23SkotvWbp9z7A3J6blfm2VndW7e1HxyFYv_SUZ1C_eFEmsJe1mTlVdzcqYob2Jk07lcxtlHvvchBrqF_pCknP77v1RVbHxl36EKAyX-Y8Ix_E0o3BBLYxZNzav2ZKigjOR7_k/w600-rw/boga-23-isigin-optugu-cicek-rubedo-tabirly.jpeg",
            "boga-24": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEw-SO0FAoxxKlsAerUQ6y4NLE9CgpKO9Z_QMc4cIy5BEDI8mZZvt6LkJ6ROaaa14U2-LPTXsXHLKb6NRoFjblqYT4MNDdpt6mze2ZN7fXR6qV1YwVKmmXsXnnBvEVo3BS5A4O1ed7LnYUXPPZc7LEZAgM6ERpnK5-UVZ7e-bFZMcWv_YM9o9MDaNX5fA/w600-rw/boga-24-tapinakta-ekmek-paylasimi-rubedo-tabirly.jpeg",
            "boga-25": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgAVtRfReFLgCjlqfLx6rUfro3_VgubTb-7_tvDL6sjXzy1nQv0UvatDMuxLcD52wbk9gwTLjC0i2VNuMxrT3Qy-u7T5BGUgbmK91Sp6WFy7j-QzPV7TlrB3buyXWVYYqQwGLvnojUsF5NV2fkDmefdNvfkbenruWHLQi2PwZshgq0lzvXlJ9P1ROPWrO0/w600-rw/boga-25-inci-denizin-yuzeyine-cikar-rubedo-tabirly.jpeg",
            "boga-26": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiumHpm2OOG1xPFBDo5msHr_A1I1cIeX71z6S7boFND_2LvKuABO3TPkv_YuDIcovgP2thgmLRYKyWyiVcEapaq6pwTOBVGyYmnvLDfrTUNWIPUmfC2Sdr8XHlaFKrKxJ_UA_P9qNjHNZYlXQZIGvstv1eqHR1ikzEmGlPUgiiC-GUREp4kkrwm0ITtqiw/w600-rw/boga-26-bolluk-tanricasi-rubedo-tabirly.jpeg",
            "boga-27": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirjYDHwW3IkntZcac1U3MwqVcuse_ppO1XXaHpRpBlWxAG6j57wXjGKi9Xhu20cyKRrK6IWa_3Vg_HaiHB9VVVEj16AUWmXqBq1sbqgYAoUz_mEKOg1KU_H7xN-xIlYu3KlQ78HxMzi_lVwN4mDDCX2O0Cne53DqeOCNuFTGd-WuFgcxfFqsVsp6sELYo/w600-rw/boga-27-bahar-bayrami-rubedo-tabirly.jpeg",
            "boga-28": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDYorQ-YzVzWRsESQnvilwVQ6-n-a_AlgdInyCNLzS5eXRo_lPAqcwL3T_x22z1JOpnUJCcCfd9qaPzk5x_wQ2SnwS-aKza0ucbnNjnqQLXlRSVNMESceNWIYgYiCf_LnKKMzt-8GF2e1cpl5xpw71mVelOmniS3I5jDhHdjjh8mGFLz_lDw79E6WRre8/w600-rw/boga-28-altin-vazo-rubedo-tabirly.jpeg",
            "boga-29": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj3JRdgDKS1PuBwQ4_bVG9meivcVSDWT510Q5NCRmCGzHZzm-1Oh1KPRX81AKgCRZJdviuOWuhK2_Hj2jzUbpAEjR8-1CjS8RcCnT0hhrMgsvFDgMnIzF2Z4pHWnmipaMobZzwl5nCap2X9P7NsdQDsSioAPs3IIz1TIdzClrcU41bH3gJTlsH2Fm1TiP4/w600-rw/boga-29-gul-bahcesi-rubedo-tabirly.jpeg",
            "boga-30": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlLiNWbs9FOn3RsSWkOfLSO9_X-frs-fxJm_RlS1vkfgu27ubOO9pGz2AM5GkxbfjsOqZWbRi8NpWWewjkFfXrE6dg1lSRYxwyLsDnAPm8Vg57dASMHaBRSSIO0ZmYy4BWyrH2G4Bz_-1SBqedyX4NVOaqr50KwRmmqfGyiHSi7OjmgFOHOkfmzkxAPig/w600-rw/boga-30-kutsal-isik-topragi-sarar-rubedo-tabirly.jpeg"
        };
        
        if (imageLinks[symbol.id]) {
            const altText = `${symbol.sign} ${symbol.degree} Derece Hermetik Sembolü - ${symbol.symbol.replace(/"/g, '&quot;')}`;
            imageHtml = `<img src="${imageLinks[symbol.id]}" class="symbol-image-active" alt="${altText}" title="${altText}" loading="lazy" />`;
        }
        
        const html = `
            <div class="symbol-card ${stageClass}" style="margin-top: 20px;">
                <div class="symbol-image-container">
                    ${imageHtml}
                </div>
                <div class="s-degree">${symbol.sign} ${symbol.degree}°</div>
                <div class="s-vision">"${symbol.symbol}"</div>
                
                <div class="s-meta">
                    <div class="meta-box">
                        <div class="meta-title">Anahtar Tema</div>
                        <div class="meta-val">${symbol.theme}</div>
                    </div>
                    <div class="meta-box">
                        <div class="meta-title">Hermetik Karşılık</div>
                        <div class="meta-val">${symbol.hermetic}</div>
                    </div>
                    <div class="meta-box" style="grid-column: span 2;">
                        <div class="meta-title">Simyasal Aşama</div>
                        <div class="meta-val stage-val">${symbol.stage}</div>
                    </div>
                </div>
            </div>
        `;
        
        if (isAppend) {
            // Remove previous appended card if exists
            const prev = container.querySelector('.symbol-card:not(.card-flipper .symbol-card)');
            if(prev) prev.remove();
            container.insertAdjacentHTML('beforeend', html);
            container.lastElementChild.scrollIntoView({behavior: "smooth", block: "start"});
        } else {
            container.innerHTML = html;
        }
    }
</script>
</body>
</html>
"""

final_html = html_template.replace('{sabian_data}', sabian_js)
with open('Sabian_Araci.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("HTML artifact built.")
