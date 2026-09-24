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
        

        /* Guide Accordion Styles */
        .s-guide-container {
            margin-top: 18px;
            width: 100%;
            text-align: left;
        }
        .guide-toggle-btn {
            width: 100%;
            background: linear-gradient(135deg, rgba(0, 255, 232, 0.08), rgba(75, 92, 255, 0.12));
            border: 1px solid rgba(0, 255, 232, 0.3);
            border-radius: 12px;
            color: var(--candy-1);
            padding: 12px 16px;
            font-size: 13px;
            font-weight: 600;
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            font-family: inherit;
        }
        .guide-toggle-btn:hover, .guide-toggle-btn.active {
            background: linear-gradient(135deg, rgba(0, 255, 232, 0.16), rgba(75, 92, 255, 0.22));
            border-color: rgba(0, 255, 232, 0.6);
            box-shadow: 0 4px 20px rgba(0, 255, 232, 0.2);
        }
        .guide-btn-title {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .guide-icon {
            font-size: 16px;
        }
        .guide-chevron {
            font-size: 11px;
            transition: transform 0.3s ease;
            color: rgba(255, 255, 255, 0.7);
        }
        .guide-content {
            margin-top: 10px;
            background: rgba(6, 10, 24, 0.92);
            border: 1px solid rgba(0, 255, 232, 0.2);
            border-radius: 14px;
            padding: 18px;
            backdrop-filter: blur(10px);
            animation: fadeInGuide 0.3s ease;
        }
        @keyframes fadeInGuide {
            from { opacity: 0; transform: translateY(-6px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .guide-block {
            margin-bottom: 14px;
        }
        .guide-block:last-child {
            margin-bottom: 0;
        }
        .guide-block-title {
            font-size: 12px;
            font-weight: 700;
            color: var(--candy-2);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 5px;
        }
        .guide-block-desc {
            font-size: 13.5px;
            line-height: 1.6;
            color: #d1d5db;
        }
        .guide-block-desc strong {
            color: #fff;
        }
        .guide-affirmation-block {
            background: linear-gradient(135deg, rgba(75, 92, 255, 0.18), rgba(0, 255, 232, 0.1));
            border-left: 3px solid var(--candy-1);
            padding: 12px 14px;
            border-radius: 8px;
        }
        .guide-affirmation-block .guide-block-title {
            color: var(--candy-1);
        }
        .affirmation-text {
            font-style: italic;
            color: #f0f6fc;
            font-weight: 500;
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

    function toggleGuide(btn) {
        const content = btn.nextElementSibling;
        const chevron = btn.querySelector('.guide-chevron');
        if (content.style.display === 'none' || !content.style.display) {
            content.style.display = 'block';
            chevron.style.transform = 'rotate(180deg)';
            btn.classList.add('active');
        } else {
            content.style.display = 'none';
            chevron.style.transform = 'rotate(0deg)';
            btn.classList.remove('active');
        }
    }
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
            "koc-1": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/sabian-sembolu-koc-1-derece-nigredo-tabirly.jpeg",
            "koc-2": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/sabian-sembolu-koc-2-derece-nigredo-tabirly.jpeg",
            "koc-3": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/sabian-sembolu-koc-3-derece-albedo-tabirly.jpeg",
            "koc-4": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-4-derece-taze-tarlada-yeseren-tohumlar-albedo-tabirly.jpeg",
            "koc-5": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-5-derece-kanatlarini-acan-kelebek-rubedo-tabirly.jpeg",
            "koc-6": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-6-derece-adam-yeni-bir-ulkeye-goc-eder-rubedo-tabirly.jpeg",
            "koc-7": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-7-derece-kadin-su-tasiyor-albedo-tabirly.jpeg",
            "koc-8": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-8-derece-kadin-sarki-soyleyen-kusu-dinler-albedo-tabirly.jpeg",
            "koc-9": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-9-kristal-selale-rubedo-tabirly.jpeg",
            "koc-10": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-10-adam-kendi-golgesini-inceler-nigredo-tabirly.jpeg",
            "koc-11": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-11-derece-insan-yuzune-donusen-maske-albedo-tabirly.jpeg",
            "koc-12": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-12-derece-vahsi-ati-ehlilestiren-adam-rubedo-tabirly.jpeg",
            "koc-13": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-13-gunes-banyosu-yapan-cocuklar-albedo-tabirly.jpeg",
            "koc-14": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-14-yuksek-dagda-bayrak-diken-kasif-rubedo-tabirly.jpeg",
            "koc-15": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-15-yanan-mumun-etrafinda-toplanan-insanlar-rubedo-tabirly.jpeg",
            "koc-16": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-16-dogayi-dinleyen-adam-albedo-tabirly.jpeg",
            "koc-17": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-17-kadin-ruzgarda-dans-eder-rubedo-tabirly.jpeg",
            "koc-18": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-18-atesle-arinan-savasci-rubedo-tabirly.jpeg",
            "koc-19": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-19-dogal-kaynak-kesfeden-adam-albedo-tabirly.jpeg",
            "koc-20": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-20-mesaleli-grup-karanlikta-ilerler-rubedo-tabirly.jpeg",
            "koc-21": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-21-isik-sutunu-goge-uzanir-tabirly.jpeg",
            "koc-22": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-22-mesale-tasiyan-adam-rubedo-tabirly.jpeg",
            "koc-23": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-23-genis-ova-uzerinde-kartal-rubedo-tabirly.jpeg",
            "koc-24": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-24-kadin-kirmizi-bir-gul-tasir-rubedo-tabirly.jpeg",
            "koc-25": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-25-atesten-gecerek-arinan-topluluk-tabirly.jpeg",
            "koc-26": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-26-tac-giyen-savasci-rubedo-tabirly.jpeg",
            "koc-27": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-27-goge-yukselen-yelkenli-gemi-rubedo-tabirly.jpeg",
            "koc-28": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-28-tapinak-kapisi-acilir-rubedo-tabirly.jpeg",
            "koc-29": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-29-kutsal-yazitlari-okuyan-bilge-rubedo-tabirly.jpeg",
            "koc-30": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/koc/koc-30-altin-bir-isik-halkasi-rubedo-tabirly.jpeg",
            "boga-1": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/sabian-sembolu-boga-1-derece-albedo-tabirly.jpeg",
            "boga-2": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/sabian-sembolu-boga-2-derece-rubedo-tabirly.jpeg",
            "boga-3": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/sabian-sembolu-boga-3-derece-rubedo-tabirly.jpeg",
            "boga-4": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-4-yontulmus-tas-uzerine-oturan-boga-nigredo-tabirly.jpeg",
            "boga-5": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-5-zengin-kadin-albedo-tabirly.jpeg",
            "boga-6": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-6-altin-yildiz-rubedo-tabirly.jpeg",
            "boga-7": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-7-insa-halinde-tapinak-albedo-tabirly.jpeg",
            "boga-8": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-8-gul-bahcesi-albedo-tabirly.jpeg",
            "boga-9": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-9-cift-toprakla-calisiyor-rubedo-tabirly.jpeg",
            "boga-10": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-10-coban-surusunu-yonlendiriyor-rubedo-tabirly.jpeg",
            "boga-11": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-11-sofrada-toplanan-insanlar-albedo-tabirly.jpeg",
            "boga-12": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-12-parlayan-elmas-rubedo-tabirly.jpeg",
            "boga-13": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-13-ekin-eken-ciftci-albedo-tabirly.jpeg",
            "boga-14": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-14-cicek-acan-agac-albedo-tabirly.jpeg",
            "boga-15": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-15-cocuklar-halat-cekiyor-rubedo-tabirly.jpeg",
            "boga-16": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-16-kadin-toprakla-dua-eder-rubedo-tabirly.jpeg",
            "boga-17": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-17-inci-takan-kadin-rubedo-tabirly.jpeg",
            "boga-18": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-18-pisen-ekmek-albedo-tabirly.jpeg",
            "boga-19": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-19-tas-duvar-oruluyor-albedo-tabirly.jpeg",
            "boga-20": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-20-ay-isiginda-parlayan-gol-rubedo-tabirly.jpeg",
            "boga-21": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-21-topraga-gomulen-tohum-albedo-tabirly.jpeg",
            "boga-22": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-22-yeseren-filiz-rubedo-tabirly.jpeg",
            "boga-23": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-23-isigin-optugu-cicek-rubedo-tabirly.jpeg",
            "boga-24": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-24-tapinakta-ekmek-paylasimi-rubedo-tabirly.jpeg",
            "boga-25": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-25-inci-denizin-yuzeyine-cikar-rubedo-tabirly.jpeg",
            "boga-26": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-26-bolluk-tanricasi-rubedo-tabirly.jpeg",
            "boga-27": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-27-bahar-bayrami-rubedo-tabirly.jpeg",
            "boga-28": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-28-altin-vazo-rubedo-tabirly.jpeg",
            "boga-29": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-29-gul-bahcesi-rubedo-tabirly.jpeg",
            "boga-30": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/boga/boga-30-kutsal-isik-topragi-sarar-rubedo-tabirly.jpeg",
            "i̇kizler-1": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-1-derece-albedo-tabirly.jpeg",
            "ikizler-1": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-1-derece-albedo-tabirly.jpeg",
            "i̇kizler-2": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/hermetik-astroloji-sembolu-ikizler-2-derece-rubedo-tabirly.jpeg",
            "ikizler-2": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/hermetik-astroloji-sembolu-ikizler-2-derece-rubedo-tabirly.jpeg",
            "i̇kizler-3": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/hermetik-astroloji-sembolu-ikizler-3-derece-rubedo-tabirly.jpeg",
            "ikizler-3": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/hermetik-astroloji-sembolu-ikizler-3-derece-rubedo-tabirly.jpeg",
            "i̇kizler-4": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-4-derece-albedo-tabirly.png",
            "ikizler-4": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-4-derece-albedo-tabirly.png",
            "i̇kizler-5": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-5-derece-albedo-tabirly.png",
            "ikizler-5": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-5-derece-albedo-tabirly.png",
            "i̇kizler-6": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-6-derece-rubedo-tabirly.png",
            "ikizler-6": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-6-derece-rubedo-tabirly.png",
            "i̇kizler-7": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-7-derece-albedo-tabirly.png",
            "ikizler-7": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-7-derece-albedo-tabirly.png",
            "i̇kizler-8": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-8-derece-rubedo-tabirly.png",
            "ikizler-8": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-8-derece-rubedo-tabirly.png",
            "i̇kizler-9": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-9-derece-albedo-tabirly.png",
            "ikizler-9": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-9-derece-albedo-tabirly.png",
            "i̇kizler-10": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-10-derece-rubedo-tabirly.png",
            "ikizler-10": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-10-derece-rubedo-tabirly.png",
            "i̇kizler-11": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-11-derece-rubedo-tabirly.png",
            "ikizler-11": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-11-derece-rubedo-tabirly.png",
            "i̇kizler-12": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-12-derece-albedo-tabirly.png",
            "ikizler-12": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-12-derece-albedo-tabirly.png",
            "i̇kizler-13": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-13-derece-rubedo-tabirly.png",
            "ikizler-13": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-13-derece-rubedo-tabirly.png",
            "i̇kizler-14": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-14-derece-albedo-tabirly.png",
            "ikizler-14": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-14-derece-albedo-tabirly.png",
            "i̇kizler-15": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-15-derece-rubedo-tabirly.png",
            "ikizler-15": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-15-derece-rubedo-tabirly.png",
            "i̇kizler-16": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-16-derece-albedo-tabirly.png",
            "ikizler-16": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-16-derece-albedo-tabirly.png",
            "i̇kizler-17": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-17-derece-albedo-tabirly.png",
            "ikizler-17": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-17-derece-albedo-tabirly.png",
            "i̇kizler-18": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-18-derece-rubedo-tabirly.png",
            "ikizler-18": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-18-derece-rubedo-tabirly.png",
            "i̇kizler-19": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-19-derece-rubedo-tabirly.png",
            "ikizler-19": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-19-derece-rubedo-tabirly.png",
            "i̇kizler-20": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-20-derece-rubedo-tabirly.png",
            "ikizler-20": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-20-derece-rubedo-tabirly.png",
            "i̇kizler-21": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-21-derece-rubedo-tabirly.png",
            "ikizler-21": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-21-derece-rubedo-tabirly.png",
            "i̇kizler-22": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-22-derece-rubedo-tabirly.png",
            "ikizler-22": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-22-derece-rubedo-tabirly.png",
            "i̇kizler-23": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-23-derece-rubedo-tabirly.png",
            "ikizler-23": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-23-derece-rubedo-tabirly.png",
            "i̇kizler-24": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-24-derece-rubedo-tabirly.png",
            "ikizler-24": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-24-derece-rubedo-tabirly.png",
            "i̇kizler-25": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-25-derece-rubedo-tabirly.png",
            "ikizler-25": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-25-derece-rubedo-tabirly.png",
            "i̇kizler-26": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-26-derece-rubedo-tabirly.png",
            "ikizler-26": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-26-derece-rubedo-tabirly.png",
            "i̇kizler-27": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-27-derece-rubedo-tabirly.png",
            "ikizler-27": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-27-derece-rubedo-tabirly.png",
            "i̇kizler-28": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-28-derece-rubedo-tabirly.png",
            "ikizler-28": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-28-derece-rubedo-tabirly.png",
            "i̇kizler-29": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-29-derece-rubedo-tabirly.png",
            "ikizler-29": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-29-derece-rubedo-tabirly.png",
            "i̇kizler-30": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-30-derece-rubedo-tabirly.png",
            "ikizler-30": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/ikizler/sabian-sembolu-ikizler-30-derece-rubedo-tabirly.png",
            "yengec-1": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/hermetik-astroloji-sembolu-yengec-1-derece-albedo-tabirly.jpeg",
            "yengec-2": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/hermnetik-astroloji-sembolu-yengec-2-derece-albedo-tabirly.jpeg",
            "yengec-3": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/hermetik-astroloji-sembolu-yengec-3-derece-rubedo-tabirly.jpeg",
            "yengec-4": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-4-derece-albedo-tabirly.png",
            "yengec-5": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-5-derece-rubedo-tabirly.png",
            "yengec-6": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-6-derece-albedo-tabirly.png",
            "yengec-7": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-7-derece-nigredo-tabirly.png",
            "yengec-8": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-8-derece-rubedo-tabirly.png",
            "yengec-9": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-9-derece-rubedo-tabirly.png",
            "yengec-10": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-10-derece-rubedo-tabirly.png",
            "yengec-11": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-11-derece-albedo-tabirly.png",
            "yengec-12": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-12-derece-albedo-tabirly.png",
            "yengec-13": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-13-derece-rubedo-tabirly.png",
            "yengec-14": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-14-derece-rubedo-tabirly.png",
            "yengec-15": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-15-derece-albedo-tabirly.png",
            "yengec-16": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-16-derece-rubedo-tabirly.png",
            "yengec-17": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-17-derece-albedo-tabirly.png",
            "yengec-18": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-18-derece-albedo-tabirly.png",
            "yengec-19": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-19-derece-rubedo-tabirly.png",
            "yengec-20": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-20-derece-rubedo-tabirly.png",
            "yengec-21": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-21-derece-rubedo-tabirly.png",
            "yengec-22": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-22-derece-rubedo-tabirly.png",
            "yengec-23": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-23-derece-rubedo-tabirly.png",
            "yengec-24": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-24-derece-rubedo-tabirly.png",
            "yengec-25": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-25-derece-rubedo-tabirly.png",
            "yengec-26": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-26-derece-rubedo-tabirly.png",
            "yengec-27": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-27-derece-rubedo-tabirly.png",
            "yengec-28": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-28-derece-rubedo-tabirly.png",
            "yengec-29": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-29-derece-rubedo-tabirly.png",
            "yengec-30": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yengec/sabian-sembolu-yengec-30-derece-rubedo-tabirly.png",
            "aslan-1": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/hermetik-astroloji-asembolu-aslan-1-derece-rubedo-tabirly.jpeg",
            "aslan-2": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/hermetik-astroloji-sembolu-aslan-2-derece-rubedo-tabirly.jpeg",
            "aslan-3": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/hermetik-astroloji-sembolu-aslan-3-derece-albedo-tabirly.jpeg",
            "aslan-4": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-4-derece-rubedo-tabirly.png",
            "aslan-5": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-5-derece-albedo-tabirly.png",
            "aslan-6": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-6-derece-nigredo-tabirly.png",
            "aslan-7": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-7-derece-rubedo-tabirly.png",
            "aslan-8": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-8-derece-albedo-tabirly.png",
            "aslan-9": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-9-derece-rubedo-tabirly.png",
            "aslan-10": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-10-derece-rubedo-tabirly.png",
            "aslan-11": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-11-derece-rubedo-tabirly.png",
            "aslan-12": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-12-derece-albedo-tabirly.png",
            "aslan-13": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-13-derece-rubedo-tabirly.png",
            "aslan-14": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-14-derece-rubedo-tabirly.png",
            "aslan-15": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-15-derece-albedo-tabirly.png",
            "aslan-16": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-16-derece-rubedo-tabirly.png",
            "aslan-17": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-17-derece-rubedo-tabirly.png",
            "aslan-18": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-18-derece-rubedo-tabirly.png",
            "aslan-19": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-19-derece-rubedo-tabirly.png",
            "aslan-20": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-20-derece-rubedo-tabirly.png",
            "aslan-21": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-21-derece-rubedo-tabirly.png",
            "aslan-22": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-22-derece-rubedo-tabirly.png",
            "aslan-23": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-23-derece-rubedo-tabirly.png",
            "aslan-24": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-24-derece-rubedo-tabirly.png",
            "aslan-25": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-25-derece-rubedo-tabirly.png",
            "aslan-26": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-26-derece-rubedo-tabirly.png",
            "aslan-27": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-27-derece-rubedo-tabirly.png",
            "aslan-28": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-28-derece-rubedo-tabirly.png",
            "aslan-29": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-29-derece-rubedo-tabirly.png",
            "aslan-30": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/aslan/sabian-sembolu-aslan-30-derece-rubedo-tabirly.png",
            "basak-1": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/hermetik-astroloji-sembolu-basak-1-derece-nigredo-tabirly.jpeg",
            "basak-2": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/hermetik-astroloji-sembolu-basak-2-derece-albedo-tabirly.jpeg",
            "basak-3": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/hermetik-astroloji-sembolu-basak-3-derece-rubedo-tabirly.jpeg",
            "basak-4": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-4-derece-albedo-tabirly.png",
            "basak-5": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-5-derece-rubedo-tabirly.png",
            "basak-6": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-6-derece-albedo-tabirly.png",
            "basak-7": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-7-derece-rubedo-tabirly.png",
            "basak-8": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-8-derece-rubedo-tabirly.png",
            "basak-9": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-9-derece-albedo-tabirly.png",
            "basak-10": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-10-derece-nigredo-tabirly.png",
            "basak-11": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-11-derece-rubedo-tabirly.png",
            "basak-12": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-12-derece-albedo-tabirly.png",
            "basak-13": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-13-derece-albedo-tabirly.png",
            "basak-14": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-14-derece-albedo-tabirly.png",
            "basak-15": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-15-derece-albedo-tabirly.png",
            "basak-16": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-16-derece-rubedo-tabirly.png",
            "basak-17": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-17-derece-rubedo-tabirly.png",
            "basak-18": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-18-derece-albedo-tabirly.png",
            "basak-19": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-19-derece-rubedo-tabirly.png",
            "basak-20": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-20-derece-rubedo-tabirly.png",
            "basak-21": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-21-derece-rubedo-tabirly.png",
            "basak-22": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-22-derece-rubedo-tabirly.png",
            "basak-23": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-23-derece-rubedo-tabirly.png",
            "basak-24": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-24-derece-rubedo-tabirly.png",
            "basak-25": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-25-derece-rubedo-tabirly.png",
            "basak-26": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-26-derece-rubedo-tabirly.png",
            "basak-27": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-27-derece-rubedo-tabirly.png",
            "basak-28": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-28-derece-rubedo-tabirly.png",
            "basak-29": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-29-derece-rubedo-tabirly.png",
            "basak-30": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/basak/sabian-sembolu-basak-30-derece-rubedo-tabirly.png",
            "terazi-1": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/hermetik-astroloji-sombolu-terazi-1-derece-albedo-tabirly.jpeg",
            "terazi-2": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-2-derece-albedo-tabirly.png",
            "terazi-3": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-3-derece-rubedo-tabirly.png",
            "terazi-4": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-4-derece-albedo-tabirly.png",
            "terazi-5": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-5-derece-rubedo-tabirly.png",
            "terazi-6": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-6-derece-rubedo-tabirly.png",
            "terazi-7": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-7-derece-albedo-tabirly.png",
            "terazi-8": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-8-derece-rubedo-tabirly.png",
            "terazi-9": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-9-derece-albedo-tabirly.png",
            "terazi-10": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-10-derece-albedo-tabirly.png",
            "terazi-11": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-11-derece-albedo-tabirly.png",
            "terazi-12": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-12-derece-albedo-tabirly.png",
            "terazi-13": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-13-derece-rubedo-tabirly.png",
            "terazi-14": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-14-derece-rubedo-tabirly.png",
            "terazi-15": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-15-derece-albedo-tabirly.png",
            "terazi-16": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-16-derece-rubedo-tabirly.png",
            "terazi-17": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-17-derece-rubedo-tabirly.png",
            "terazi-18": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-18-derece-rubedo-tabirly.png",
            "terazi-19": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-19-derece-rubedo-tabirly.png",
            "terazi-20": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-20-derece-rubedo-tabirly.png",
            "terazi-21": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-21-derece-rubedo-tabirly.png",
            "terazi-22": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-22-derece-rubedo-tabirly.png",
            "terazi-23": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-23-derece-rubedo-tabirly.png",
            "terazi-24": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-24-derece-rubedo-tabirly.png",
            "terazi-25": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-25-derece-rubedo-tabirly.png",
            "terazi-26": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-26-derece-rubedo-tabirly.png",
            "terazi-27": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-27-derece-rubedo-tabirly.png",
            "terazi-28": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-28-derece-rubedo-tabirly.png",
            "terazi-29": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-29-derece-rubedo-tabirly.png",
            "terazi-30": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/terazi/sabian-sembolu-terazi-30-derece-rubedo-tabirly.png",
            "akrep-1": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-1-derece-nigredo-tabirly.png",
            "akrep-2": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-2-derece-albedo-tabirly.png",
            "akrep-3": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-3-derece-rubedo-tabirly.png",
            "akrep-4": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-4-derece-nigredo-tabirly.png",
            "akrep-5": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-5-derece-rubedo-tabirly.png",
            "akrep-6": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-6-derece-nigredo-tabirly.png",
            "akrep-7": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-7-derece-albedo-tabirly.png",
            "akrep-8": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-8-derece-nigredo-tabirly.png",
            "akrep-9": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-9-derece-albedo-tabirly.png",
            "akrep-10": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-10-derece-rubedo-tabirly.png",
            "akrep-11": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-11-derece-nigredo-tabirly.png",
            "akrep-12": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-12-derece-rubedo-tabirly.png",
            "akrep-13": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-13-derece-albedo-tabirly.png",
            "akrep-14": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-14-derece-nigredo-tabirly.png",
            "akrep-15": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-15-derece-albedo-tabirly.png",
            "akrep-16": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-16-derece-rubedo-tabirly.png",
            "akrep-17": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-17-derece-nigredo-tabirly.png",
            "akrep-18": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-18-derece-rubedo-tabirly.png",
            "akrep-19": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-19-derece-albedo-tabirly.png",
            "akrep-20": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-20-derece-rubedo-tabirly.png",
            "akrep-21": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-21-derece-rubedo-tabirly.png",
            "akrep-22": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-22-derece-rubedo-tabirly.png",
            "akrep-23": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-23-derece-rubedo-tabirly.png",
            "akrep-24": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-24-derece-rubedo-tabirly.png",
            "akrep-25": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-25-derece-rubedo-tabirly.png",
            "akrep-26": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-26-derece-rubedo-tabirly.png",
            "akrep-27": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-27-derece-rubedo-tabirly.png",
            "akrep-28": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-28-derece-rubedo-tabirly.png",
            "akrep-29": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-29-derece-rubedo-tabirly.png",
            "akrep-30": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/akrep/sabian-sembolu-akrep-30-derece-rubedo-tabirly.png",
            "yay-1": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-1-derece-albedo-tabirly.png",
            "yay-2": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-2-derece-rubedo-tabirly.png",
            "yay-3": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-3-derece-rubedo-tabirly.png",
            "yay-4": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-4-derece-rubedo-tabirly.png",
            "yay-5": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-5-derece-rubedo-tabirly.png",
            "yay-6": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-6-derece-albedo-tabirly.png",
            "yay-7": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-7-derece-rubedo-tabirly.png",
            "yay-8": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-8-derece-albedo-tabirly.png",
            "yay-9": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-9-derece-albedo-tabirly.png",
            "yay-10": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-10-derece-rubedo-tabirly.png",
            "yay-11": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-11-derece-albedo-tabirly.png",
            "yay-12": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-12-derece-rubedo-tabirly.png",
            "yay-13": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-13-derece-rubedo-tabirly.png",
            "yay-14": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-14-derece-rubedo-tabirly.png",
            "yay-15": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-15-derece-albedo-tabirly.png",
            "yay-16": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-16-derece-rubedo-tabirly.png",
            "yay-17": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-17-derece-rubedo-tabirly.png",
            "yay-18": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-18-derece-rubedo-tabirly.png",
            "yay-19": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-19-derece-nigredo-tabirly.png",
            "yay-20": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-20-derece-rubedo-tabirly.png",
            "yay-21": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-21-derece-rubedo-tabirly.png",
            "yay-22": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-22-derece-rubedo-tabirly.png",
            "yay-23": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-23-derece-rubedo-tabirly.png",
            "yay-24": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-24-derece-rubedo-tabirly.png",
            "yay-25": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-25-derece-rubedo-tabirly.png",
            "yay-26": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-26-derece-rubedo-tabirly.png",
            "yay-27": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-27-derece-rubedo-tabirly.png",
            "yay-28": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-28-derece-rubedo-tabirly.png",
            "yay-29": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-29-derece-rubedo-tabirly.png",
            "yay-30": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/yay/sabian-sembolu-yay-30-derece-rubedo-tabirly.png",
            "oglak-1": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-1-derece-nigredo-tabirly.png",
            "oglak-2": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-2-derece-albedo-tabirly.png",
            "oglak-3": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-3-derece-rubedo-tabirly.png",
            "oglak-4": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-4-derece-nigredo-tabirly.png",
            "oglak-5": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-5-derece-albedo-tabirly.png",
            "oglak-6": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-6-derece-rubedo-tabirly.png",
            "oglak-7": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-7-derece-albedo-tabirly.png",
            "oglak-8": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-8-derece-rubedo-tabirly.png",
            "oglak-9": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-9-derece-rubedo-tabirly.png",
            "oglak-10": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-10-derece-nigredo-tabirly.png",
            "oglak-11": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-11-derece-albedo-tabirly.png",
            "oglak-12": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-12-derece-rubedo-tabirly.png",
            "oglak-13": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-13-derece-rubedo-tabirly.png",
            "oglak-14": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-14-derece-rubedo-tabirly.png",
            "oglak-15": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-15-derece-nigredo-tabirly.png",
            "oglak-16": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-16-derece-rubedo-tabirly.png",
            "oglak-17": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-17-derece-albedo-tabirly.png",
            "oglak-18": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-18-derece-albedo-tabirly.png",
            "oglak-19": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-19-derece-rubedo-tabirly.png",
            "oglak-20": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-20-derece-rubedo-tabirly.png",
            "oglak-21": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-21-derece-rubedo-tabirly.png",
            "oglak-22": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-22-derece-rubedo-tabirly.png",
            "oglak-23": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-23-derece-rubedo-tabirly.png",
            "oglak-24": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-24-derece-rubedo-tabirly.png",
            "oglak-25": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-25-derece-rubedo-tabirly.png",
            "oglak-26": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-26-derece-rubedo-tabirly.png",
            "oglak-27": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-27-derece-rubedo-tabirly.png",
            "oglak-28": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-28-derece-rubedo-tabirly.png",
            "oglak-29": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-29-derece-rubedo-tabirly.png",
            "oglak-30": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/oglak/sabian-sembolu-oglak-30-derece-rubedo-tabirly.png",
            "kova-1": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-1-derece-albedo-tabirly.png",
            "kova-2": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-2-derece-rubedo-tabirly.png",
            "kova-3": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-3-derece-rubedo-tabirly.png",
            "kova-4": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-4-derece-albedo-tabirly.png",
            "kova-5": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-5-derece-rubedo-tabirly.png",
            "kova-6": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-6-derece-rubedo-tabirly.png",
            "kova-7": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-7-derece-albedo-tabirly.png",
            "kova-8": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-8-derece-rubedo-tabirly.png",
            "kova-9": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-9-derece-albedo-tabirly.png",
            "kova-10": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-10-derece-rubedo-tabirly.png",
            "kova-11": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-11-derece-rubedo-tabirly.png",
            "kova-12": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-12-derece-albedo-tabirly.png",
            "kova-13": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-13-derece-rubedo-tabirly.png",
            "kova-14": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-14-derece-rubedo-tabirly.png",
            "kova-15": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-15-derece-rubedo-tabirly.png",
            "kova-16": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-16-derece-rubedo-tabirly.png",
            "kova-17": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-17-derece-rubedo-tabirly.png",
            "kova-18": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-18-derece-rubedo-tabirly.png",
            "kova-19": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-19-derece-albedo-tabirly.png",
            "kova-20": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-20-derece-rubedo-tabirly.png",
            "kova-21": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-21-derece-rubedo-tabirly.png",
            "kova-22": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-22-derece-rubedo-tabirly.png",
            "kova-23": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-23-derece-rubedo-tabirly.png",
            "kova-24": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-24-derece-rubedo-tabirly.png",
            "kova-25": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-25-derece-rubedo-tabirly.png",
            "kova-26": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-26-derece-rubedo-tabirly.png",
            "kova-27": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-27-derece--tabirly.png",
            "kova-28": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-28-derece-rubedo-tabirly.png",
            "kova-29": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-29-derece-rubedo-tabirly.png",
            "kova-30": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/kova/sabian-sembolu-kova-30-derece-rubedo-tabirly.png",
            "balik-1": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-1-derece-nigredo-tabirly.png",
            "balik-2": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-2-derece-albedo-tabirly.png",
            "balik-3": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-3-derece-rubedo-tabirly.png",
            "balik-4": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-4-derece-albedo-tabirly.png",
            "balik-5": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-5-derece-albedo-tabirly.png",
            "balik-6": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-6-derece-nigredo-tabirly.png",
            "balik-7": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-7-derece-rubedo-tabirly.png",
            "balik-8": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-8-derece-albedo-tabirly.png",
            "balik-9": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-9-derece-rubedo-tabirly.png",
            "balik-10": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-10-derece-rubedo-tabirly.png",
            "balik-11": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-11-derece-albedo-tabirly.png",
            "balik-12": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-12-derece-albedo-tabirly.png",
            "balik-13": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-13-derece-rubedo-tabirly.png",
            "balik-14": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-14-derece-rubedo-tabirly.png",
            "balik-15": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-15-derece-rubedo-tabirly.png",
            "balik-16": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-16-derece-nigredo-tabirly.png",
            "balik-17": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-17-derece-rubedo-tabirly.png",
            "balik-18": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-18-derece-rubedo-tabirly.png",
            "balik-19": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-19-derece-rubedo-tabirly.png",
            "balik-20": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-20-derece-rubedo-tabirly.png",
            "balik-21": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-21-derece-rubedo-tabirly.png",
            "balik-22": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-22-derece-rubedo-tabirly.png",
            "balik-23": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-23-derece-rubedo-tabirly.png",
            "balik-24": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-24-derece-rubedo-tabirly.png",
            "balik-25": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-25-derece-rubedo-tabirly.png",
            "balik-26": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-26-derece-rubedo-tabirly.png",
            "balik-27": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-27-derece-rubedo-tabirly.png",
            "balik-28": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-28-derece-rubedo-tabirly.png",
            "balik-29": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-29-derece-rubedo-tabirly.png",
            "balik-30": "https://raw.githubusercontent.com/Tabirly/hermetik-astroloji/main/images/balik/sabian-sembolu-balik-30-derece-rubedo-tabirly.png"
        };
        
        if (imageLinks[symbol.id]) {
            const altText = `${symbol.sign} ${symbol.degree} Derece Hermetik Sembolü - ${symbol.symbol.replace(/"/g, '&quot;')}`;
            imageHtml = `<img src="${imageLinks[symbol.id]}" class="symbol-image-active" alt="${altText}" title="${altText}" loading="lazy" />`;
        }
        
        let guideHtml = '';
        if (symbol.guide) {
            guideHtml = `
                <div class="s-guide-container">
                    <button type="button" class="guide-toggle-btn" onclick="toggleGuide(this)">
                        <span class="guide-btn-title"><span class="guide-icon">🔮</span> Sembolün Derin Anlamı & Yaşam Rehberi</span>
                        <span class="guide-chevron">▼</span>
                    </button>
                    <div class="guide-content" style="display: none;">
                        <div class="guide-block">
                            <div class="guide-block-title">✨ Ezoterik & Sembolik Anlam</div>
                            <div class="guide-block-desc">${symbol.guide.meaning}</div>
                        </div>
                        <div class="guide-block">
                            <div class="guide-block-title">🧭 Günlük Hayatta Nasıl Kullanabiliriz?</div>
                            <div class="guide-block-desc">${symbol.guide.daily_use}</div>
                        </div>
                        <div class="guide-block">
                            <div class="guide-block-title">⚖️ Gölge Yönü & Dikkat Edilmesi Gerekenler</div>
                            <div class="guide-block-desc">${symbol.guide.shadow}</div>
                        </div>
                        <div class="guide-block guide-affirmation-block">
                            <div class="guide-block-title">🧘 Hermetik Olumlama & Meditasyon</div>
                            <div class="guide-block-desc affirmation-text">"${symbol.guide.affirmation}"</div>
                        </div>
                    </div>
                </div>
            `;
        } else {
            const stageDesc = {
                "Nigredo": "Çürüme ve ego ölümü evresi; tohumun toprağın karanlığında kabuğunu çatlatıp yeni bir bilinç kıvılcımına hazırlandığı başlangıç anıdır.",
                "Albedo": "Arınma ve Ay bilinci evresi; duygusal berraklık, sezgisel netlik ve zihinsel tortuların temizlendiği aydınlanma sürecidir.",
                "Citrinitas": "Güneş bilinci ve altın ışık evresi; felsefi uyanış, bilgelik ve hakikatin doğrudan kavrandığı zihinsel aydınlanmadır.",
                "Rubedo": "Bütünleşme ve Felsefe Taşı evresi; ruhun dünyevi bedende ustalıkla tezahür etmesi, saf ruhsal altının açığa çıkışıdır."
            }[symbol.stage] || "Ruhsal dönüşüm evresi.";

            guideHtml = `
                <div class="s-guide-container">
                    <button type="button" class="guide-toggle-btn" onclick="toggleGuide(this)">
                        <span class="guide-btn-title"><span class="guide-icon">🔮</span> Sembolün Derin Anlamı & Yaşam Rehberi</span>
                        <span class="guide-chevron">▼</span>
                    </button>
                    <div class="guide-content" style="display: none;">
                        <div class="guide-block">
                            <div class="guide-block-title">✨ Ezoterik & Sembolik Anlam</div>
                            <div class="guide-block-desc">"${symbol.symbol}" vizyonu; ruhun ${symbol.sign} burcundaki ${symbol.degree}. derecesinde <strong>${symbol.theme}</strong> ilkesini açığa çıkarır. Bu sembol, bilincin derin katmanlarındaki saklı potansiyeli uyandırmak için bir anahtardır.</div>
                        </div>
                        <div class="guide-block">
                            <div class="guide-block-title">🧭 Günlük Hayatta Nasıl Kullanabiliriz?</div>
                            <div class="guide-block-desc">Bu derece gündeminizdeyken, hayatınızdaki <strong>${symbol.theme}</strong> alanına odaklanın. Kararlarınızı aceleye getirmeden, içsel bilgeliğinizin ve <strong>${symbol.hermetic}</strong> kozmik ilkesinin size rehberlik etmesine izin verin.</div>
                        </div>
                        <div class="guide-block">
                            <div class="guide-block-title">⚗️ Simyasal Süreç: ${symbol.stage}</div>
                            <div class="guide-block-desc">${stageDesc}</div>
                        </div>
                        <div class="guide-block guide-affirmation-block">
                            <div class="guide-block-title">🧘 Hermetik Olumlama</div>
                            <div class="guide-block-desc affirmation-text">"Evrenin kusursuz ritmiyle uyum içindeyim; ${symbol.theme.toLowerCase()} bilincimle varlığımı onurlandırıyorum."</div>
                        </div>
                    </div>
                </div>
            `;
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
                ${guideHtml}
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

    function toggleGuide(btn) {
        const content = btn.nextElementSibling;
        const chevron = btn.querySelector('.guide-chevron');
        if (content.style.display === 'none' || !content.style.display) {
            content.style.display = 'block';
            chevron.style.transform = 'rotate(180deg)';
            btn.classList.add('active');
        } else {
            content.style.display = 'none';
            chevron.style.transform = 'rotate(0deg)';
            btn.classList.remove('active');
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
