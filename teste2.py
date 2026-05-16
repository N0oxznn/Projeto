from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>N0oxznn | Desenvolvedor Python & Discord</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; scroll-behavior: smooth; }
        
        body {
            background: #050505;
            color: white;
            font-family: 'Arial', Helvetica, sans-serif;
            overflow-x: hidden;
        }

        /* FUNDO ONDULADO COM MANCHAS PRETO E BRANCO */
        .bg {
            position: fixed;
            inset: 0;
            background: 
                radial-gradient(circle at 20% 30%, rgba(255,255,255,0.08) 0%, transparent 50%),
                radial-gradient(circle at 70% 20%, rgba(255,255,255,0.06) 0%, transparent 55%),
                radial-gradient(circle at 40% 70%, rgba(255,255,255,0.07) 0%, transparent 45%),
                radial-gradient(circle at 80% 80%, rgba(30,30,30,0.9) 0%, transparent 60%);
            background-size: 250% 250%;
            animation: blobMove 45s ease infinite;
            z-index: -1;
            filter: contrast(1.1);
        }

        @keyframes blobMove {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        nav {
            position: fixed; top: 0; width: 100%; padding: 28px 8%;
            display: flex; justify-content: space-between; align-items: center;
            backdrop-filter: blur(12px); background: rgba(5,5,5,0.95);
            border-bottom: 1px solid #1a1a1a; z-index: 1000;
        }
        .logo { font-size: 34px; font-weight: 800; letter-spacing: -1.5px; }
        .logo span { color: #cfcfcf; }

        nav ul { display: flex; gap: 42px; list-style: none; }
        nav a { color: #d0d0d0; text-decoration: none; font-weight: 500; }
        nav a:hover { color: white; }

        /* ANIMAÇÃO HACK FORTE NO NOME */
        .hero { min-height: 100vh; display: flex; align-items: center; padding: 0 8%; }
        .name {
            font-size: 108px;
            font-weight: 900;
            line-height: 1;
            position: relative;
            display: inline-block;
            animation: matrixHack 0.25s infinite linear alternate-reverse;
            color: #fff;
            text-shadow: 0 0 15px #00ff41;
        }

        @keyframes matrixHack {
            0%   { transform: translate(0,0) skew(0deg); text-shadow: 4px 0 #00ff41, -4px 0 #ff00ff; }
            10%  { transform: translate(-5px, 4px) skew(8deg); }
            20%  { transform: translate(6px, -5px) skew(-6deg); }
            30%  { transform: translate(-4px, 3px); }
            40%  { transform: translate(5px, -4px); }
            50%  { transform: translate(-3px, 5px) skew(5deg); }
            100% { transform: translate(0,0) skew(0deg); text-shadow: -4px 0 #00ff41, 4px 0 #ff00ff; }
        }

        .name::before {
            content: "N0oxznn";
            position: absolute;
            top: 0; left: 0;
            opacity: 0.15;
            animation: matrixText 0.15s infinite linear;
        }

        @keyframes matrixText {
            0% { content: "N0oxznn"; }
            33% { content: "ノ0oxznn"; }
            66% { content: "N0oXznn"; }
        }

        .badge { 
            padding: 11px 26px; border: 1px solid #444; background: #0f0f0f; 
            border-radius: 50px; font-size: 14.5px; letter-spacing: 3px; 
            margin-bottom: 30px; display: inline-block; 
        }

        section { padding: 140px 8%; }
        .section-title { font-size: 17px; letter-spacing: 4px; color: #888; margin-bottom: 14px; }
        .big-title { font-size: 58px; margin-bottom: 35px; line-height: 1.1; }
        .text { font-size: 21px; color: #b0b0b0; max-width: 900px; line-height: 1.85; }

        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
            gap: 30px;
            margin-top: 70px;
        }
        .card {
            background: #0a0a0a; border: 1px solid #1f1f1f; border-radius: 28px;
            padding: 45px 38px; transition: all 0.4s ease;
        }
        .card:hover {
            transform: translateY(-10px); border-color: #777;
            box-shadow: 0 0 40px rgba(255,255,255,0.12);
        }
        .card h3 { font-size: 29px; margin-bottom: 22px; }

        .tech-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 24px;
        }
        .tech-card {
            background: #0a0a0a; border: 1px solid #1f1f1f; border-radius: 26px;
            padding: 38px 20px; text-align: center; transition: all 0.4s;
        }
        .tech-card:hover {
            transform: translateY(-12px) scale(1.05);
            border-color: #888; box-shadow: 0 0 45px rgba(255,255,255,0.15);
        }
        .tech-card img { width: 78px; margin-bottom: 18px; transition: 0.4s; }
        .tech-card:hover img { transform: scale(1.2) rotate(8deg); }

        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(460px, 1fr));
            gap: 40px;
            margin-top: 60px;
        }
        .project-card {
            background: #090909; border: 1px solid #1f1f1f; border-radius: 32px;
            padding: 50px 45px; transition: all 0.4s;
        }
        .project-card:hover {
            transform: translateY(-8px); border-color: #777;
            box-shadow: 0 0 50px rgba(255,255,255,0.1);
        }

        .tags { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 40px; }
        .tag {
            background: #141414; border: 1px solid #282828;
            padding: 11px 22px; border-radius: 12px; font-size: 15px;
        }

        .contact { text-align: center; padding: 160px 8% 140px; }
        .contact a {
            display: inline-block; padding: 24px 52px; background: #cfcfcf; color: black;
            font-size: 22px; font-weight: bold; border-radius: 20px;
            text-decoration: none; box-shadow: 0 0 35px rgba(207,207,207,0.3);
        }
        .contact a:hover { transform: scale(1.07); }

        footer { text-align: center; padding: 70px 8%; color: #555; border-top: 1px solid #111; }
    </style>
</head>
<body>
    <div class="bg"></div>

    <nav>
        <div class="logo"><span>N0</span>oxznn</div>
        <ul>
            <li><a href="#sobre">Sobre</a></li>
            <li><a href="#tech">Tecnologias</a></li>
            <li><a href="#projetos">Projetos</a></li>
            <li><a href="#contato">Contato</a></li>
        </ul>
    </nav>

    <section class="hero">
        <div>
            <div class="badge">🚀 Aberto a novos projetos</div>
            <h1 class="name" data-text="N0oxznn">N0oxznn</h1>
            <p style="font-size: 23px; color: #b5b5b5; max-width: 800px;">
                Desenvolvedor full-stack focado em Python, bots para Discord e websites modernos.
            </p>
        </div>
    </section>

    <section id="sobre">
        <div class="section-title">MINHA TRAJETÓRIA</div>
        <h2 class="big-title">Quem sou eu</h2>
        <p class="text">
            Comecei na programação por pura curiosidade, assistindo vídeos no YouTube e tentando entender como sites, bots e sistemas funcionavam por trás. 
            O que começou como um simples hobby rapidamente virou uma paixão intensa. Dediquei muitas horas estudando Python, lógica de programação, 
            desenvolvimento web e criação de bots para Discord. Com o tempo, passei a criar projetos mais complexos e profissionais, sempre buscando melhorar 
            a qualidade do código, a performance e a experiência do usuário. Hoje me orgulho de entregar soluções completas, bem estruturadas e visualmente atraentes. 
            Estou constantemente evoluindo, estudando novas tecnologias e aceitando desafios que me façam crescer como desenvolvedor.
        </p>

        <div class="cards-grid">
            <div class="card">
                <h3>💻 Desenvolvimento Web</h3>
                <p>Crio websites modernos, rápidos, totalmente responsivos e com design premium.</p>
            </div>
            <div class="card">
                <h3>🤖 Bots Discord</h3>
                <p>Desenvolvo bots personalizados e profissionais para servidores grandes.</p>
            </div>
            <div class="card">
                <h3>🔥 Aprendizado Contínuo</h3>
                <p>Estudo diariamente para evoluir minhas habilidades.</p>
            </div>
        </div>
    </section>

    <section id="tech">
        <div class="section-title">STACK TECNOLÓGICA</div>
        <h2 class="big-title">Tecnologias</h2>

        <div style="margin-bottom: 60px;">
            <h3 style="margin-bottom:20px; color:#aaa;">Tecnologias que domino</h3>
            <div class="tech-grid">
                <div class="tech-card">
                    <img src="https://cdn-icons-png.flaticon.com/512/5968/5968350.png">
                    <h3>Python</h3>
                </div>
            </div>
        </div>

        <div style="margin-bottom: 60px;">
            <h3 style="margin-bottom:20px; color:#aaa;">Estou aprendendo</h3>
            <div class="tech-grid">
                <div class="tech-card">
                    <img src="https://cdn-icons-png.flaticon.com/512/226/226777.png" style="width:85px;">
                    <h3>Java</h3>
                </div>
            </div>
        </div>

        <div>
            <h3 style="margin-bottom:20px; color:#aaa;">Quero aprender em breve</h3>
            <div class="tech-grid">
                <div class="tech-card"><img src="https://cdn-icons-png.flaticon.com/512/5968/5968292.png"><h3>JavaScript</h3></div>
                <div class="tech-card"><img src="https://cdn-icons-png.flaticon.com/512/5968/5968267.png"><h3>HTML5</h3></div>
                <div class="tech-card"><img src="https://cdn-icons-png.flaticon.com/512/5968/5968242.png"><h3>CSS3</h3></div>
                <div class="tech-card"><img src="https://cdn-icons-png.flaticon.com/512/6132/6132222.png"><h3>C#</h3></div>
            </div>
        </div>
    </section>

    <section id="projetos">
        <div class="section-title">PORTFÓLIO</div>
        <h2 class="big-title">Principais Projetos</h2>
        
        <div class="projects-grid">
            <div class="project-card">
                <h3>⚡ Bots para Discord</h3>
                <p>Desenvolvimento de bots completos e profissionais para servidores grandes. 
                Crio sistemas avançados com tickets interativos e painéis bonitos, loja virtual completa com economia e itens, 
                sistema de ranks e níveis automáticos, moderação avançada com logs, proteção anti-raid, comandos personalizados, 
                integração com banco de dados MySQL, sistemas de configuração dinâmica, automações complexas e muito mais. 
                Todos os bots são otimizados para alta performance, estabilidade, segurança e fácil manutenção pelo dono do servidor. 
                Já desenvolvi bots para diversas comunidades e sempre busco entregar um produto de qualidade premium.</p>
                <div class="tags">
                    <div class="tag">Python</div>
                    <div class="tag">discord.py</div>
                    <div class="tag">MySQL</div>
                    <div class="tag">Automação</div>
                </div>
            </div>
            
            <div class="project-card">
                <h3>🌐 Websites Profissionais</h3>
                <p>Criação de sites modernos, elegantes e de alta performance. 
                Desenvolvo portfólios, landing pages, sites institucionais e sistemas web completos. 
                Cada projeto é pensado nos mínimos detalhes: design premium, total responsividade em todos os dispositivos, 
                otimização de velocidade de carregamento, código limpo e bem organizado, SEO básico, animações suaves 
                e uma experiência fluida e agradável para o usuário final. Utilizo as melhores práticas do mercado para entregar um produto final de alto nível.</p>
                <div class="tags">
                    <div class="tag">Flask</div>
                    <div class="tag">HTML/CSS</div>
                    <div class="tag">Responsivo</div>
                    <div class="tag">Design Premium</div>
                </div>
            </div>
        </div>
    </section>

    <section id="contato" class="contact">
        <div class="section-title">CONTATO</div>
        <h2 class="big-title">Vamos trabalhar juntos?</h2>
        <a href="https://discord.gg/G2KWFvBMGV" target="_blank">Entrar no meu Discord</a>
    </section>

    <footer>
        © 2026 N0oxznn — Todos os direitos reservados.
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(debug=True)