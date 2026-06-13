from flask import Flask, render_template_string

app = Flask(__name__)

# CSS para deixar o visual profissional
style = '''
<style>
    body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; color: #333; margin: 0; padding: 20px; display: flex; flex-direction: column; align-items: center; }
    .container { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); width: 100%; max-width: 500px; text-align: center; }
    h1 { color: #2c3e50; margin-bottom: 25px; }
    ul { list-style: none; padding: 0; }
    li { margin: 10px 0; }
    .btn { display: block; background-color: #3498db; color: white; padding: 12px; text-decoration: none; border-radius: 6px; transition: 0.3s; font-weight: bold; }
    .btn:hover { background-color: #2980b9; transform: translateY(-2px); }
    .btn-back { display: inline-block; margin-top: 20px; color: #7f8c8d; text-decoration: none; font-size: 0.9em; }
    .btn-back:hover { color: #333; }
</style>
'''

# Layout Base para evitar repetição de código
def layout(title, content, show_back=True):
    back_link = '<a href="/" class="btn-back">← Voltar ao Menu</a>' if show_back else ''
    return render_template_string(f'''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        {style}
    </head>
    <body>
        <div class="container">
            {content}
            {back_link}
        </div>
    </body>
    </html>
    ''')

@app.route('/')
def home():
    menu = '''
    <h1>🤖 Menu do Robô</h1>
    <ul>
        <li><a class="btn" href="/affiliates">Gerenciar Afiliados</a></li>
        <li><a class="btn" href="/campaigns">Minhas Campanhas</a></li>
        <li><a class="btn" href="/reports">Ver Relatórios</a></li>
        <li><a class="btn" href="/settings">Configurações</a></li>
        <li><a class="btn" href="/support">Suporte Técnico</a></li>
        <li><a class="btn" href="/members">Área de Membros</a></li>
    </ul>
    '''
    return layout("Menu do Robô", menu, show_back=False)

@app.route('/affiliates')
def affiliates():
    return layout("Afiliados", "<h2>👥 Afiliados</h2><p>Gerencie sua base de parceiros aqui.</p>")

@app.route('/campaigns')
def campaigns():
    return layout("Campanhas", "<h2>🚀 Campanhas</h2><p>Configure seus disparos e links aqui.</p>")

@app.route('/reports')
def reports():
    return layout("Relatórios", "<h2>📊 Relatórios</h2><p>Veja suas métricas de conversão.</p>")

@app.route('/settings')
def settings():
    return layout("Configurações", "<h2>⚙️ Configurações</h2><p>Ajuste as chaves de API e preferências.</p>")

@app.route('/support')
def support():
    return layout("Suporte", "<h2>🎧 Suporte</h2><p>Precisa de ajuda? Abra um chamado.</p>")

@app.route('/members')
def members():
    return layout("Membros", "<h2>💎 Área de Membros</h2><p>Acesse o conteúdo exclusivo.</p>")

if __name__ == '__main__':
    app.run(debug=True)
