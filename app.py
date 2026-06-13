from flask import Flask, render_template_string

app = Flask(__name__)

# HTML Templates
index_html = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Menu do Robô de Afiliado</title>
</head>
<body>
    <h1>Menu do Robô de Afiliado</h1>
    <ul>
        <li><a href="/affiliates">Gerenciamento de Afiliados</a></li>
        <li><a href="/campaigns">Campanhas</a></li>
        <li><a href="/reports">Relatórios</a></li>
        <li><a href="/settings">Configurações</a></li>
        <li><a href="/support">Suporte</a></li>
        <li><a href="/members">Área de Membros</a></li>
    </ul>
</body>
</html>
'''

affiliates_html = '<h2>Gerenciamento de Afiliados</h2><p>Conteúdo relacionado a afiliados aqui.</p>'
campaigns_html = '<h2>Campanhas</h2><p>Conteúdo relacionado a campanhas aqui.</p>'
reports_html = '<h2>Relatórios</h2><p>Conteúdo relacionado a relatórios aqui.</p>'
settings_html = '<h2>Configurações</h2><p>Conteúdo relacionado a configurações aqui.</p>'
support_html = '<h2>Suporte</h2><p>Conteúdo de suporte aqui.</p>'
members_html = '<h2>Área de Membros</h2><p>Conteúdo para membros aqui.</p>'

@app.route('/')
def home():
    return render_template_string(index_html)

@app.route('/affiliates')
def affiliates():
    return render_template_string(affiliates_html)

@app.route('/campaigns')
def campaigns():
    return render_template_string(campaigns_html)

@app.route('/reports')
def reports():
    return render_template_string(reports_html)

@app.route('/settings')
def settings():
    return render_template_string(settings_html)

@app.route('/support')
def support():
    return render_template_string(support_html)

@app.route('/members')
def members():
    return render_template_string(members_html)

if __name__ == '__main__':
    app.run(debug=True)
