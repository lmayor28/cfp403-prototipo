import json

def update_with_guia():
    with open('PrototipoJuan.html', 'r', encoding='utf-8') as f:
        html = f.read()

    tag = '<script type="__bundler/template">\n'
    idx = html.find(tag)
    assert idx != -1, "Template tag not found"
    json_start = idx + len(tag)
    decoder = json.JSONDecoder()
    data, end_offset = decoder.raw_decode(html, json_start)

    s_gal = data.find('<section id="galeria"')
    e_gal = data.find('</section>', s_gal) + len('</section>')
    assert s_gal != -1 and e_gal != -1, "Galeria section not found"

    guia_html = """<section id="galeria" style="background:#F6F7F9;padding:88px 0;scroll-margin-top:80px">
    <style>
      .galeria-btn-admin:hover { background:#087C99 !important; color:#fff !important; }
      .galeria-btn-insta:hover { background:#14121F !important; color:#fff !important; border-color:#14121F !important; }
      .galeria-proj-card { transition: all .35s ease; cursor: pointer; }
      .galeria-proj-card:hover { transform: translateY(-6px); border-color: #08BCE3 !important; box-shadow: 0 20px 40px -15px rgba(8,188,227,0.3) !important; }
      .galeria-proj-card:hover .galeria-proj-img { transform: scale(1.05); }
    </style>
    <div style="max-width:1200px;margin:0 auto;padding:0 24px;display:flex;flex-direction:column;gap:36px">
      <div data-reveal="" style="display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap">
        <div style="display:flex;flex-direction:column;gap:10px;max-width:620px">
          <div style="font-size:13px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#0A7FA0">Galería de proyectos</div>
          <h2 style="margin:0;font-size:clamp(30px,3.6vw,46px);line-height:1.08;font-weight:800;letter-spacing:-0.02em;text-wrap:balance">Lo que crean nuestros estudiantes</h2>
        </div>
        <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap">
          <button id="btn-admin-proyectos" class="galeria-btn-admin" style="display:flex;align-items:center;gap:8px;font-family:inherit;font-weight:700;font-size:15px;color:#087C99;background:#fff;padding:11px 18px;border-radius:999px;border:1.5px solid #08BCE3;cursor:pointer;transition:all .2s;box-shadow:0 2px 8px rgba(8,188,227,.15)">
            <cfp-icon glyph="assets/icons/lock.svg" style="display:block;width:16px;height:16px;"></cfp-icon>Panel Administrador
          </button>
          <a id="btn-insta-proyectos" class="galeria-btn-insta" href="https://www.instagram.com/cfp_mercedes/" target="_blank" rel="noopener noreferrer" style="display:flex;align-items:center;gap:8px;font-family:inherit;font-weight:700;font-size:15px;color:#14121F;background:#fff;padding:11px 18px;border-radius:999px;border:1.5px solid #DADDE3;text-decoration:none;transition:all .2s">
            <cfp-icon glyph="assets/icons/instagram.svg" style="display:block;width:18px;height:18px;"></cfp-icon>Ver más en Instagram
          </a>
        </div>
      </div>
      
      <!-- Contenedor dinámico de proyectos -->
      <div id="galeria-proyectos-grid" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,340px),1fr));gap:24px">
      </div>

      <!-- Guía Provisoria para el Equipo (Luis & Administradores) -->
      <div id="guia-equipo-proyectos" style="margin-top:20px;background:#FFFFFF;border:1.5px solid #08BCE3;border-radius:24px;padding:28px 32px;box-shadow:0 6px 24px rgba(8,188,227,0.08);display:flex;flex-direction:column;gap:22px">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:14px;border-bottom:1.5px solid #F0F3F7;padding-bottom:16px">
          <div style="display:flex;align-items:center;gap:14px">
            <div style="background:linear-gradient(135deg,#087C99,#08BCE3);color:#fff;border-radius:12px;width:40px;height:40px;display:grid;place-items:center;font-weight:800;font-size:20px;box-shadow:0 4px 10px rgba(8,188,227,0.25)">ℹ</div>
            <div>
              <h3 style="margin:0;font-size:20px;font-weight:800;color:#087C99;letter-spacing:-0.01em">¿Cómo funciona la nueva sección?</h3>
              <p style="margin:3px 0 0;font-size:13.5px;color:#5B5664">Guía de referencia rápida y funcionamiento para el equipo administrador (Luis & Juan).</p>
            </div>
          </div>
          <span style="background:#EAF1F7;color:#087C99;font-size:12px;font-weight:700;padding:6px 14px;border-radius:999px;border:1px solid #08BCE3">Modo Provisorio de Pruebas</span>
        </div>

        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:22px">
          
          <!-- Bloque 1: Visualización diferenciada -->
          <div style="display:flex;flex-direction:column;gap:12px;background:#F9FAFC;padding:22px;border-radius:16px;border:1.5px solid #ECEEF2">
            <div style="display:flex;align-items:center;gap:10px">
              <span style="background:#087C99;color:#fff;width:24px;height:24px;border-radius:50%;display:grid;place-items:center;font-size:13px;font-weight:800">1</span>
              <h4 style="margin:0;font-size:16px;font-weight:800;color:#14121F">Visualización según el tipo de proyecto</h4>
            </div>
            <div style="font-size:13.5px;line-height:1.6;color:#333;display:flex;flex-direction:column;gap:12px">
              <div style="background:#fff;padding:12px 14px;border-radius:10px;border-left:4px solid #08BCE3;box-shadow:0 2px 6px rgba(0,0,0,0.02)">
                <strong style="color:#087C99">🎮 Videojuegos y 🌐 Páginas Web (Enlaces):</strong><br>
                Tienen una etiqueta indicativa (<em>🎮 Jugar Online ↗</em> o <em>🌐 Visitar Web ↗</em>). Al hacer clic en la tarjeta, abre directamente el enlace del juego o sitio web en una pestaña nueva (<code>target="_blank"</code>).
              </div>
              <div style="background:#fff;padding:12px 14px;border-radius:10px;border-left:4px solid #E5177B;box-shadow:0 2px 6px rgba(0,0,0,0.02)">
                <strong style="color:#E5177B">📷 Textil, Gastronomía, Agro y Diseño (Fotografías):</strong><br>
                Tienen la etiqueta <em>🔍 Ver Foto y Detalle</em>. Al hacer clic, abre un visor ampliado (<strong>Lightbox</strong>) con la foto en alta resolución, categoría y descripción completa del trabajo.
              </div>
            </div>
          </div>

          <!-- Bloque 2: Panel de Administrador -->
          <div style="display:flex;flex-direction:column;gap:12px;background:#F9FAFC;padding:22px;border-radius:16px;border:1.5px solid #ECEEF2">
            <div style="display:flex;align-items:center;gap:10px">
              <span style="background:#08BCE3;color:#fff;width:24px;height:24px;border-radius:50%;display:grid;place-items:center;font-size:13px;font-weight:800">2</span>
              <h4 style="margin:0;font-size:16px;font-weight:800;color:#14121F">Panel de Administrador Integrado</h4>
            </div>
            <div style="font-size:13.5px;line-height:1.6;color:#333;display:flex;flex-direction:column;gap:10px">
              <div style="background:#fff;padding:10px 14px;border-radius:10px;border:1px solid #E5E8ED">
                <strong>Acceso con PIN:</strong> Al lado del botón "Ver más en Instagram" se incorporó el botón <em>Panel Administrador</em>. Solicita PIN de seguridad: <code style="background:#EAF1F7;color:#087C99;padding:2px 6px;border-radius:4px;font-weight:700">403</code> o <code style="background:#EAF1F7;color:#087C99;padding:2px 6px;border-radius:4px;font-weight:700">admin403</code>.
              </div>
              <div style="background:#fff;padding:12px 14px;border-radius:10px;border:1px solid #E5E8ED">
                <strong>Carga y edición de proyectos:</strong>
                <ul style="margin:6px 0 0 16px;padding:0;display:flex;flex-direction:column;gap:4px">
                  <li><strong>Subida de imágenes:</strong> Podés subir la foto directamente desde tu computadora o celular (se procesa y previsualiza de inmediato) o ingresar una ruta/URL.</li>
                  <li><strong>Selector de Tipo:</strong> Elegir si es <em>Enlace interactivo</em> (habilita campo URL) o <em>Fotografía</em>.</li>
                  <li><strong>Categorías:</strong> Videojuegos, Páginas Web, Diseño, Textil, Gastronomía, Agro.</li>
                  <li><strong>Acciones:</strong> Podés editar cualquier proyecto existente o eliminarlo.</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Bloque 3: Persistencia y Hosting -->
          <div style="display:flex;flex-direction:column;gap:12px;background:#F9FAFC;padding:22px;border-radius:16px;border:1.5px solid #ECEEF2">
            <div style="display:flex;align-items:center;gap:10px">
              <span style="background:#7A3F80;color:#fff;width:24px;height:24px;border-radius:50%;display:grid;place-items:center;font-size:13px;font-weight:800">3</span>
              <h4 style="margin:0;font-size:16px;font-weight:800;color:#14121F">Persistencia y Compatibilidad Dual</h4>
            </div>
            <div style="font-size:13.5px;line-height:1.6;color:#333;display:flex;flex-direction:column;gap:12px">
              <div style="background:#fff;padding:12px 14px;border-radius:10px;border-left:4px solid #7A3F80;box-shadow:0 2px 6px rgba(0,0,0,0.02)">
                <strong style="color:#7A3F80">En GitHub Pages (actual):</strong><br>
                Los cambios se guardan al instante en el navegador (<code>localStorage</code>) y contás con el botón <strong>⬇ Descargar proyectos.json</strong> para guardar una copia de respaldo en el repositorio.
              </div>
              <div style="background:#fff;padding:12px 14px;border-radius:10px;border-left:4px solid #087C99;box-shadow:0 2px 6px rgba(0,0,0,0.02)">
                <strong style="color:#087C99">En tu servidor propio (www.cfp43.com):</strong><br>
                Ya quedó programado y subido el archivo <code style="background:#EAF1F7;color:#087C99;padding:2px 6px;border-radius:4px;font-weight:700">guardar_proyectos.php</code>. Cuando subas la web a tu hosting PHP, el panel guardará los cambios automáticamente en el servidor sin requerir ninguna modificación extra de código.
              </div>
            </div>
          </div>

        </div>
      </div>

    </div>
  </section>"""

    data = data[:s_gal] + guia_html + data[e_gal:]

    new_json_str = json.dumps(data)
    new_json_str = new_json_str.replace('</', r'<\u002F')
    new_html = html[:json_start] + new_json_str + html[end_offset:]

    with open('PrototipoJuan.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

    print("SUCCESS: Guia informativa integrada con exito!")

if __name__ == '__main__':
    update_with_guia()
