import json

def update_galeria_and_modal():
    with open('PrototipoJuan.html', 'r', encoding='utf-8') as f:
        html = f.read()

    tag = '<script type="__bundler/template">\n'
    idx = html.find(tag)
    assert idx != -1, "Template tag not found"
    json_start = idx + len(tag)
    decoder = json.JSONDecoder()
    data, end_offset = decoder.raw_decode(html, json_start)

    # 1. Clean public <section id="galeria"> - NO guide box in public view!
    s_gal = data.find('<section id="galeria"')
    e_gal = data.find('</section>', s_gal) + len('</section>')
    assert s_gal != -1 and e_gal != -1, "Galeria section not found"

    clean_galeria_html = """<section id="galeria" style="background:#F6F7F9;padding:88px 0;scroll-margin-top:80px">
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
    </div>
  </section>"""
    data = data[:s_gal] + clean_galeria_html + data[e_gal:]

    # 2. Locate existing script before </body> and replace it
    s_script = data.rfind('<script>')
    s_body_end = data.rfind('</body>')
    assert s_script != -1 and s_body_end != -1, "Script or body end not found"

    new_script_content = r"""<script>
  (function() {
    var STORAGE_KEY = 'cfp_proyectos_data';
    var ADMIN_PIN = '403';
    var adminLogueado = false;

    var DEFAULT_PROJS = [
      {
        id: 'proj-1',
        titulo: 'Videojuego 2D: Retro Arcade',
        categoria: 'Videojuegos',
        tipo: 'link',
        url: 'https://itch.io',
        imagen: 'assets/entornos/sala-informatica.jpg',
        descripcion: 'Juego de plataformas 2D programado en Python por estudiantes del trayecto de Programación y Videojuegos.',
        color: '#08BCE3'
      },
      {
        id: 'proj-2',
        titulo: 'Identidad Visual y Packaging Comercial',
        categoria: 'Diseño',
        tipo: 'foto',
        url: '',
        imagen: 'assets/entornos/sala-informatica.jpg',
        descripcion: 'Diseño de marcas, logotipos y piezas publicitarias desarrollado en el trayecto de Diseño y Marketing Digital.',
        color: '#E5177B'
      },
      {
        id: 'proj-3',
        titulo: 'Cultivo Agroecológico y Hongos Comestibles',
        categoria: 'Agro',
        tipo: 'foto',
        url: '',
        imagen: 'assets/entornos/taller-textil.jpg',
        descripcion: 'Producción sustentable y manejo de cultivos especiales realizada en el entorno de huerta.',
        color: '#08BCE3'
      },
      {
        id: 'proj-4',
        titulo: 'Colección de Indumentaria y Lencería',
        categoria: 'Textil',
        tipo: 'foto',
        url: '',
        imagen: 'assets/entornos/taller-textil.jpg',
        descripcion: 'Prendas de vestir confeccionadas con maquinaria industrial y moldería propia del Taller Textil.',
        color: '#7A3F80'
      },
      {
        id: 'proj-5',
        titulo: 'Elaboración de Pastelería y Panificación',
        categoria: 'Gastronomía',
        tipo: 'foto',
        url: '',
        imagen: 'assets/entornos/salon-gastronomia.jpg',
        descripcion: 'Productos gastronómicos y técnicas de inocuidad alimentaria aplicadas en el Salón de Gastronomía.',
        color: '#E5177B'
      },
      {
        id: 'proj-6',
        titulo: 'Plataforma Web Institucional y Catálogo',
        categoria: 'Páginas Web',
        tipo: 'link',
        url: 'https://github.com',
        imagen: 'assets/entornos/sala-informatica.jpg',
        descripcion: 'Sitio web interactivo con diseño responsive y base de datos desarrollado en el trayecto web.',
        color: '#087C99'
      }
    ];

    function obtenerProyectos() {
      try {
        var guardados = localStorage.getItem(STORAGE_KEY);
        if (guardados) return JSON.parse(guardados);
      } catch (e) {}
      return DEFAULT_PROJS;
    }

    function guardarProyectos(projs) {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(projs));
      } catch (e) {}
      try {
        fetch('guardar_proyectos.php', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ pin: ADMIN_PIN, proyectos: projs })
        }).catch(function() {});
      } catch (e) {}
      renderizarGaleria();
    }

    function colorPorCat(cat) {
      var map = {
        'Videojuegos': '#08BCE3',
        'Páginas Web': '#087C99',
        'Diseño': '#E5177B',
        'Textil': '#7A3F80',
        'Gastronomía': '#E5177B',
        'Agro': '#08BCE3'
      };
      return map[cat] || '#087C99';
    }

    function ensureModalesEnDOM() {
      if (document.getElementById('galeria-modales-root')) return;
      var root = document.createElement('div');
      root.id = 'galeria-modales-root';
      root.innerHTML = [
        '<!-- Lightbox Modal -->',
        '<div id="galeria-lightbox" style="display:none;position:fixed;inset:0;z-index:99999;background:rgba(20,18,31,0.85);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);place-items:center;padding:24px;box-sizing:border-box">',
        '  <div style="position:relative;max-width:800px;width:100%;max-height:90vh;background:#fff;border-radius:24px;overflow:hidden;box-shadow:0 30px 60px rgba(0,0,0,0.5);display:flex;flex-direction:column">',
        '    <button id="btn-cerrar-lightbox" style="position:absolute;top:16px;right:16px;z-index:10;width:38px;height:38px;border-radius:50%;border:0;background:rgba(20,18,31,0.7);color:#fff;cursor:pointer;display:grid;place-items:center">',
        '      <cfp-icon glyph="assets/icons/x.svg" style="display:block;width:20px;height:20px;"></cfp-icon>',
        '    </button>',
        '    <div style="width:100%;max-height:55vh;background:#14121F;overflow:hidden;display:grid;place-items:center">',
        '      <img id="lightbox-img" src="" alt="" style="max-width:100%;max-height:55vh;object-fit:contain;display:block">',
        '    </div>',
        '    <div style="padding:24px 28px;display:flex;flex-direction:column;gap:10px;background:#fff">',
        '      <div style="display:flex;align-items:center;gap:10px">',
        '        <span id="lightbox-cat" style="font-size:12px;font-weight:700;padding:5px 12px;border-radius:999px;background:#E5177B;color:#fff;text-transform:uppercase"></span>',
        '      </div>',
        '      <h3 id="lightbox-titulo" style="margin:0;font-size:22px;font-weight:800;color:#14121F"></h3>',
        '      <p id="lightbox-desc" style="margin:0;font-size:15px;line-height:1.6;color:#5B5664"></p>',
        '    </div>',
        '  </div>',
        '</div>',
        '<!-- Modal Admin -->',
        '<div id="modal-admin-proyectos" style="display:none;position:fixed;inset:0;z-index:99999;background:rgba(20,18,31,0.8);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);place-items:center;padding:20px;box-sizing:border-box">',
        '  <div style="position:relative;max-width:820px;width:100%;max-height:92vh;background:#fff;border-radius:24px;overflow:hidden;box-shadow:0 35px 70px rgba(0,0,0,0.5);display:flex;flex-direction:column">',
        '    <div style="padding:22px 28px;background:linear-gradient(135deg,#087C99,#08BCE3);color:#fff;display:flex;justify-content:space-between;align-items:center">',
        '      <div style="display:flex;align-items:center;gap:10px">',
        '        <cfp-icon glyph="assets/icons/lock.svg" style="display:block;width:22px;height:22px;"></cfp-icon>',
        '        <div style="font-weight:800;font-size:20px">Panel Administrador: Galería de Proyectos</div>',
        '      </div>',
        '      <button id="btn-cerrar-admin" style="background:rgba(255,255,255,0.25);border:0;color:#fff;width:34px;height:34px;border-radius:50%;cursor:pointer;display:grid;place-items:center">',
        '        <cfp-icon glyph="assets/icons/x.svg" style="display:block;width:18px;height:18px;"></cfp-icon>',
        '      </button>',
        '    </div>',
        '    <!-- Vista 1: Login con PIN + Botón Ver Guía -->',
        '    <div id="admin-login-view" style="padding:36px 32px;display:flex;flex-direction:column;align-items:center;gap:18px;text-align:center;overflow-y:auto;max-height:calc(92vh - 80px)">',
        '      <div style="width:56px;height:56px;border-radius:16px;background:#EAF1F7;color:#087C99;display:grid;place-items:center">',
        '        <cfp-icon glyph="assets/icons/lock.svg" style="display:block;width:28px;height:28px;"></cfp-icon>',
        '      </div>',
        '      <div>',
        '        <h4 style="margin:0 0 6px;font-size:20px;font-weight:800;color:#14121F">Acceso de Gestión</h4>',
        '        <p style="margin:0;font-size:14px;color:#5B5664">Ingresá tu clave o PIN de administrador para editar y subir proyectos.</p>',
        '      </div>',
        '      <div style="display:flex;gap:10px;width:100%;max-width:320px">',
        '        <input id="admin-pin-input" type="password" placeholder="Ingresá PIN (ej: 403)" style="flex:1;padding:12px 16px;border-radius:12px;border:1.5px solid #DADDE3;font-size:15px;outline:none">',
        '        <button id="admin-pin-btn" style="background:#087C99;color:#fff;font-weight:700;padding:12px 20px;border-radius:12px;border:0;cursor:pointer">Entrar</button>',
        '      </div>',
        '      <div id="admin-login-error" style="display:none;color:#E5177B;font-size:13px;font-weight:600">PIN incorrecto. Intentá con 403.</div>',
        '      <!-- Botón e información de guía dentro del login -->',
        '      <div style="margin-top:10px;width:100%;max-width:720px;display:flex;flex-direction:column;align-items:center;gap:10px">',
        '        <button id="btn-toggle-guia-login" type="button" style="background:#F0F7FA;border:1.5px solid #08BCE3;color:#087C99;font-weight:700;font-size:13.5px;padding:9px 18px;border-radius:999px;cursor:pointer;display:flex;align-items:center;gap:6px">',
        '          📖 ¿Cómo funciona esta sección? (Guía para el equipo)',
        '        </button>',
        '        <div id="guia-login-view" style="display:none;width:100%;text-align:left;background:#F9FAFC;border:1.5px solid #DADDE3;border-radius:16px;padding:20px;box-sizing:border-box">',
        '          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;border-bottom:1px solid #ECEEF2;padding-bottom:8px">',
        '            <strong style="color:#087C99;font-size:15px">Guía de Referencia y Funcionamiento (Luis & Juan)</strong>',
        '            <button id="btn-cerrar-guia-login" type="button" style="background:none;border:0;color:#5B5664;font-size:12px;cursor:pointer;text-decoration:underline">Ocultar</button>',
        '          </div>',
        '          <div style="display:flex;flex-direction:column;gap:12px;font-size:13px;line-height:1.55;color:#333">',
        '            <div style="background:#fff;padding:10px 14px;border-radius:10px;border-left:3px solid #08BCE3">',
        '              <strong style="color:#087C99">1. Visualización según tipo:</strong><br>',
        '              • <strong>Videojuegos y Páginas Web (Enlaces):</strong> Tienen etiqueta indicativa (🎮 Jugar Online ↗ o 🌐 Visitar Web ↗). Al hacer clic abren en pestaña nueva (<code>target="_blank"</code>).<br>',
        '              • <strong>Textil, Gastronomía, Agro y Diseño (Fotografías):</strong> Tienen etiqueta 🔍 Ver Foto y Detalle. Abren visor ampliado (Lightbox).',
        '            </div>',
        '            <div style="background:#fff;padding:10px 14px;border-radius:10px;border-left:3px solid #08BCE3">',
        '              <strong style="color:#087C99">2. Carga y edición de proyectos:</strong><br>',
        '              • <strong>Subida de fotos:</strong> Podés subir foto desde tu PC/celular o pegar una ruta/URL.<br>',
        '              • <strong>Selector de Tipo:</strong> Elegir si es Enlace interactivo o Fotografía.<br>',
        '              • <strong>Categorías:</strong> Videojuegos, Páginas Web, Diseño, Textil, Gastronomía, Agro.<br>',
        '              • <strong>Acciones:</strong> Editar o Eliminar proyectos existentes.',
        '            </div>',
        '            <div style="background:#fff;padding:10px 14px;border-radius:10px;border-left:3px solid #7A3F80">',
        '              <strong style="color:#7A3F80">3. Persistencia y Compatibilidad Dual:</strong><br>',
        '              • <strong>En GitHub Pages (actual):</strong> Guarda al instante en el navegador (<code>localStorage</code>) y contás con el botón <em>⬇ Descargar proyectos.json</em>.<br>',
        '              • <strong>En servidor propio (www.cfp43.com):</strong> Ya programado con <code>guardar_proyectos.php</code> para sincronizar automáticamente al hosting PHP.',
        '            </div>',
        '          </div>',
        '        </div>',
        '      </div>',
        '    </div>',
        '    <!-- Vista 2: Panel de Gestión -->',
        '    <div id="admin-panel-view" style="display:none;padding:24px 28px;overflow-y:auto;max-height:calc(92vh - 80px);flex-direction:column;gap:20px">',
        '      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;padding-bottom:16px;border-bottom:1px solid #ECEEF2">',
        '        <div style="font-size:14px;color:#5B5664"><strong>Estado:</strong> Guardado en el navegador y listo para sincronizar con www.cfp43.com</div>',
        '        <div style="display:flex;gap:10px;flex-wrap:wrap">',
        '          <button id="btn-toggle-guia-panel" style="background:#EAF1F7;color:#087C99;font-weight:700;padding:9px 16px;border-radius:999px;border:1px solid #08BCE3;cursor:pointer;display:flex;align-items:center;gap:6px">',
        '            📖 Guía de Uso',
        '          </button>',
        '          <button id="btn-nuevo-proyecto" style="background:#08BCE3;color:#fff;font-weight:700;padding:9px 16px;border-radius:999px;border:0;cursor:pointer;display:flex;align-items:center;gap:6px">',
        '            + Agregar Proyecto',
        '          </button>',
        '          <button id="btn-descargar-json" style="background:#14121F;color:#fff;font-weight:700;padding:9px 16px;border-radius:999px;border:0;cursor:pointer">',
        '            ⬇ Descargar proyectos.json',
        '          </button>',
        '        </div>',
        '      </div>',
        '      <!-- Guía colapsable en el panel de gestión -->',
        '      <div id="admin-guia-box" style="display:none;background:#FFFFFF;border:1.5px solid #08BCE3;border-radius:18px;padding:20px;box-shadow:0 4px 16px rgba(8,188,227,0.08);flex-direction:column;gap:14px">',
        '        <div style="display:flex;justify-content:space-between;align-items:center">',
        '          <h4 style="margin:0;font-size:16px;font-weight:800;color:#087C99">¿Cómo funciona la nueva sección? (Guía para el equipo)</h4>',
        '          <button id="btn-cerrar-guia-panel" type="button" style="background:none;border:0;color:#5B5664;font-size:12px;cursor:pointer;text-decoration:underline">Ocultar</button>',
        '        </div>',
        '        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr));gap:14px">',
        '          <div style="background:#F9FAFC;padding:12px 14px;border-radius:12px;border:1px solid #ECEEF2;font-size:12.5px;line-height:1.5">',
        '            <strong style="color:#087C99;display:block;margin-bottom:4px">1. Visualización según tipo:</strong>',
        '            • <strong>Videojuegos y Web:</strong> Enlaces con etiqueta <em>🎮 Jugar</em> / <em>🌐 Visitar</em>. Abren directo en pestaña nueva (<code>target="_blank"</code>).<br>',
        '            • <strong>Textil, Cocina, Agro, Diseño:</strong> Fotos con <em>🔍 Ver Foto</em>. Abren visor ampliado (Lightbox).',
        '          </div>',
        '          <div style="background:#F9FAFC;padding:12px 14px;border-radius:12px;border:1px solid #ECEEF2;font-size:12.5px;line-height:1.5">',
        '            <strong style="color:#08BCE3;display:block;margin-bottom:4px">2. Carga y edición:</strong>',
        '            • <strong>PIN:</strong> Clave <code>403</code> o <code>admin403</code>.<br>',
        '            • <strong>Subida:</strong> Directo desde PC/celular o ingresando ruta.<br>',
        '            • <strong>Tipo:</strong> Elegir Enlace (con URL) o Fotografía.<br>',
        '            • <strong>Acciones:</strong> Editar o Eliminar cualquier publicación.',
        '          </div>',
        '          <div style="background:#F9FAFC;padding:12px 14px;border-radius:12px;border:1px solid #ECEEF2;font-size:12.5px;line-height:1.5">',
        '            <strong style="color:#7A3F80;display:block;margin-bottom:4px">3. Hosting y sincronización:</strong>',
        '            • <strong>GitHub Pages:</strong> Guarda en <code>localStorage</code> y permite descargar <code>proyectos.json</code>.<br>',
        '            • <strong>www.cfp43.com:</strong> Listo con <code>guardar_proyectos.php</code> para guardar directo al servidor sin tocar código.',
        '          </div>',
        '        </div>',
        '      </div>',
        '      <!-- Formulario de Proyecto -->',
        '      <div id="form-proyecto-container" style="display:none;background:#F9FAFC;border:1.5px solid #08BCE3;border-radius:18px;padding:22px;flex-direction:column;gap:16px">',
        '        <h4 id="form-proyecto-titulo-modo" style="margin:0;font-size:18px;font-weight:800;color:#087C99">Agregar Nuevo Proyecto</h4>',
        '        <input type="hidden" id="proj-edit-id" value="">',
        '        <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">',
        '          <div>',
        '            <label style="display:block;font-size:13px;font-weight:700;margin-bottom:6px;color:#14121F">Título del Proyecto:</label>',
        '            <input id="proj-in-titulo" type="text" placeholder="Ej: Videojuego Retro 2D" style="width:100%;box-sizing:border-box;padding:10px 14px;border-radius:10px;border:1px solid #DADDE3;font-size:14px">',
        '          </div>',
        '          <div>',
        '            <label style="display:block;font-size:13px;font-weight:700;margin-bottom:6px;color:#14121F">Categoría:</label>',
        '            <select id="proj-in-categoria" style="width:100%;box-sizing:border-box;padding:10px 14px;border-radius:10px;border:1px solid #DADDE3;font-size:14px;background:#fff">',
        '              <option value="Videojuegos">Videojuegos</option>',
        '              <option value="Páginas Web">Páginas Web</option>',
        '              <option value="Diseño">Diseño y Marketing</option>',
        '              <option value="Textil">Confección Textil</option>',
        '              <option value="Gastronomía">Gastronomía y Pastelería</option>',
        '              <option value="Agro">Producción Hortícola y Agro</option>',
        '            </select>',
        '          </div>',
        '        </div>',
        '        <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">',
        '          <div>',
        '            <label style="display:block;font-size:13px;font-weight:700;margin-bottom:6px;color:#14121F">Tipo de Publicación:</label>',
        '            <select id="proj-in-tipo" style="width:100%;box-sizing:border-box;padding:10px 14px;border-radius:10px;border:1px solid #DADDE3;font-size:14px;background:#fff">',
        '              <option value="link">Enlace interactivo (Videojuego / Web)</option>',
        '              <option value="foto">Fotografía de trabajo (Textil, Cocina, etc)</option>',
        '            </select>',
        '          </div>',
        '          <div id="campo-url-container">',
        '            <label style="display:block;font-size:13px;font-weight:700;margin-bottom:6px;color:#14121F">Enlace URL del juego o página:</label>',
        '            <input id="proj-in-url" type="url" placeholder="https://..." style="width:100%;box-sizing:border-box;padding:10px 14px;border-radius:10px;border:1px solid #DADDE3;font-size:14px">',
        '          </div>',
        '        </div>',
        '        <div>',
        '          <label style="display:block;font-size:13px;font-weight:700;margin-bottom:6px;color:#14121F">Imagen de portada / foto del proyecto:</label>',
        '          <div style="display:flex;gap:12px;align-items:center;flex-wrap:wrap">',
        '            <input type="file" id="proj-in-archivo" accept="image/*" style="display:none">',
        '            <button id="btn-seleccionar-archivo" type="button" style="background:#EAF1F7;color:#087C99;font-weight:700;border:1px solid #08BCE3;padding:10px 18px;border-radius:10px;cursor:pointer">',
        '              📁 Subir imagen desde la PC',
        '            </button>',
        '            <span style="font-size:13px;color:#5B5664">o pegar ruta/URL:</span>',
        '            <input id="proj-in-imgurl" type="text" placeholder="assets/entornos/sala-informatica.jpg" style="flex:1;min-width:200px;box-sizing:border-box;padding:10px 14px;border-radius:10px;border:1px solid #DADDE3;font-size:14px">',
        '          </div>',
        '          <div id="preview-foto-box" style="margin-top:12px;display:none;align-items:center;gap:12px">',
        '            <img id="preview-foto-img" src="" style="width:120px;height:80px;object-fit:cover;border-radius:8px;border:1px solid #DADDE3">',
        '            <span style="font-size:13px;color:#087C99;font-weight:600">✓ Imagen cargada</span>',
        '          </div>',
        '        </div>',
        '        <div>',
        '          <label style="display:block;font-size:13px;font-weight:700;margin-bottom:6px;color:#14121F">Descripción del trabajo:</label>',
        '          <textarea id="proj-in-desc" rows="3" placeholder="Contá brevemente de qué se trata el proyecto desarrollado..." style="width:100%;box-sizing:border-box;padding:10px 14px;border-radius:10px;border:1px solid #DADDE3;font-size:14px;font-family:inherit"></textarea>',
        '        </div>',
        '        <div style="display:flex;justify-content:flex-end;gap:10px">',
        '          <button id="btn-cancelar-proyecto" type="button" style="background:#fff;border:1px solid #DADDE3;padding:10px 18px;border-radius:10px;cursor:pointer;font-weight:700;color:#5B5664">Cancelar</button>',
        '          <button id="btn-guardar-proyecto" type="button" style="background:#087C99;border:0;padding:10px 24px;border-radius:10px;cursor:pointer;font-weight:700;color:#fff">💾 Guardar Proyecto</button>',
        '        </div>',
        '      </div>',
        '      <div>',
        '        <h4 style="margin:0 0 12px;font-size:16px;font-weight:800;color:#14121F">Proyectos Publicados (<span id="admin-proj-count">0</span>)</h4>',
        '        <div id="admin-proyectos-lista" style="display:flex;flex-direction:column;gap:10px"></div>',
        '      </div>',
        '    </div>',
        '  </div>',
        '</div>'
      ].join('\n');
      document.body.appendChild(root);

      // Bind dynamic listeners
      document.getElementById('btn-cerrar-lightbox').addEventListener('click', cerrarLightbox);
      document.getElementById('galeria-lightbox').addEventListener('click', function(e) { if (e.target === this) cerrarLightbox(); });
      document.getElementById('btn-cerrar-admin').addEventListener('click', cerrarAdminProyectos);
      document.getElementById('modal-admin-proyectos').addEventListener('click', function(e) { if (e.target === this) cerrarAdminProyectos(); });
      
      document.getElementById('admin-pin-btn').addEventListener('click', verificarAdminPin);
      document.getElementById('admin-pin-input').addEventListener('keydown', function(e) { if (e.key === 'Enter') verificarAdminPin(); });

      // Listeners para la guia
      document.getElementById('btn-toggle-guia-login').addEventListener('click', function() {
        var box = document.getElementById('guia-login-view');
        box.style.display = box.style.display === 'none' ? 'block' : 'none';
      });
      document.getElementById('btn-cerrar-guia-login').addEventListener('click', function() {
        document.getElementById('guia-login-view').style.display = 'none';
      });

      document.getElementById('btn-toggle-guia-panel').addEventListener('click', function() {
        var box = document.getElementById('admin-guia-box');
        box.style.display = box.style.display === 'none' ? 'flex' : 'none';
      });
      document.getElementById('btn-cerrar-guia-panel').addEventListener('click', function() {
        document.getElementById('admin-guia-box').style.display = 'none';
      });
      
      document.getElementById('btn-nuevo-proyecto').addEventListener('click', mostrarFormularioProyecto);
      document.getElementById('btn-descargar-json').addEventListener('click', descargarProyectosJSON);
      
      document.getElementById('proj-in-tipo').addEventListener('change', function() { cambiarTipoProyecto(this.value); });
      
      document.getElementById('btn-seleccionar-archivo').addEventListener('click', function() {
        document.getElementById('proj-in-archivo').click();
      });
      document.getElementById('proj-in-archivo').addEventListener('change', procesarArchivoFoto);
      document.getElementById('proj-in-imgurl').addEventListener('input', function() { previsualizarRutaFoto(this.value); });
      
      document.getElementById('btn-cancelar-proyecto').addEventListener('click', ocultarFormularioProyecto);
      document.getElementById('btn-guardar-proyecto').addEventListener('click', guardarProyectoForm);
    }

    function renderizarGaleria() {
      var grid = document.getElementById('galeria-proyectos-grid');
      if (!grid) return;
      var projs = obtenerProyectos();
      grid.innerHTML = '';

      projs.forEach(function(p, i) {
        var card = document.createElement('div');
        card.className = 'galeria-proj-card';
        card.style.cssText = 'background:#fff;border:1.5px solid #ECEEF2;border-radius:24px;overflow:hidden;display:flex;flex-direction:column;position:relative;box-shadow:0 4px 16px rgba(20,18,31,.04)';
        
        var isLink = p.tipo === 'link' && p.url;
        var badgeAccion = isLink 
          ? (p.categoria === 'Videojuegos' ? '🎮 Jugar Online ↗' : '🌐 Visitar Web ↗')
          : '🔍 Ver Foto y Detalle';
        
        var badgeBg = isLink ? 'linear-gradient(90deg,#087C99,#08BCE3)' : 'rgba(20,18,31,0.75)';

        card.innerHTML = [
          '<div style="position:relative;height:230px;background:#14121F;overflow:hidden">',
          '  <img src="' + p.imagen + '" alt="' + p.titulo + '" loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block;transition:transform .5s ease" class="galeria-proj-img">',
          '  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0.1) 60%,rgba(20,18,31,0.6) 100%);pointer-events:none"></div>',
          '  <span style="position:absolute;top:12px;left:12px;background:' + colorPorCat(p.categoria) + ';color:#fff;font-size:12px;font-weight:700;padding:5px 12px;border-radius:999px;letter-spacing:0.02em">' + p.categoria + '</span>',
          '  <span style="position:absolute;top:12px;right:12px;background:' + badgeBg + ';color:#fff;font-size:11.5px;font-weight:700;padding:5px 11px;border-radius:999px;backdrop-filter:blur(6px)">' + badgeAccion + '</span>',
          '</div>',
          '<div style="padding:20px 22px 22px;display:flex;flex-direction:column;gap:10px;flex:1">',
          '  <h4 style="margin:0;font-size:18.5px;font-weight:800;color:#14121F;line-height:1.25">' + p.titulo + '</h4>',
          '  <p style="margin:0;font-size:14px;line-height:1.55;color:#5B5664;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden">' + p.descripcion + '</p>',
          '  <div style="margin-top:auto;padding-top:8px;display:flex;align-items:center;gap:6px;font-size:14px;font-weight:700;color:#087C99">',
          '    ' + (isLink ? 'Abrir enlace directo ↗' : 'Ver fotografía completa 🔍'),
          '  </div>',
          '</div>'
        ].join('\n');

        card.addEventListener('click', function() {
          if (isLink) {
            window.open(p.url, '_blank');
          } else {
            abrirLightbox(p);
          }
        });

        grid.appendChild(card);
      });
    }

    function abrirLightbox(p) {
      ensureModalesEnDOM();
      var box = document.getElementById('galeria-lightbox');
      if (!box) return;
      document.getElementById('lightbox-img').src = p.imagen;
      document.getElementById('lightbox-cat').textContent = p.categoria;
      document.getElementById('lightbox-cat').style.background = colorPorCat(p.categoria);
      document.getElementById('lightbox-titulo').textContent = p.titulo;
      document.getElementById('lightbox-desc').textContent = p.descripcion;
      box.style.display = 'grid';
    }

    function cerrarLightbox() {
      var box = document.getElementById('galeria-lightbox');
      if (box) box.style.display = 'none';
    }

    function abrirAdminProyectos() {
      ensureModalesEnDOM();
      var mod = document.getElementById('modal-admin-proyectos');
      if (!mod) return;
      mod.style.display = 'grid';
      if (!adminLogueado) {
        document.getElementById('admin-login-view').style.display = 'flex';
        document.getElementById('admin-panel-view').style.display = 'none';
        document.getElementById('admin-login-error').style.display = 'none';
        var pinInput = document.getElementById('admin-pin-input');
        if (pinInput) { pinInput.value = ''; pinInput.focus(); }
      } else {
        document.getElementById('admin-login-view').style.display = 'none';
        document.getElementById('admin-panel-view').style.display = 'flex';
        renderizarAdminLista();
      }
    }

    function cerrarAdminProyectos() {
      var mod = document.getElementById('modal-admin-proyectos');
      if (mod) mod.style.display = 'none';
    }

    function verificarAdminPin() {
      var pin = (document.getElementById('admin-pin-input').value || '').trim();
      if (pin === ADMIN_PIN || pin === 'admin403') {
        adminLogueado = true;
        document.getElementById('admin-login-view').style.display = 'none';
        document.getElementById('admin-panel-view').style.display = 'flex';
        renderizarAdminLista();
      } else {
        document.getElementById('admin-login-error').style.display = 'block';
      }
    }

    function renderizarAdminLista() {
      var projs = obtenerProyectos();
      document.getElementById('admin-proj-count').textContent = projs.length;
      var lista = document.getElementById('admin-proyectos-lista');
      if (!lista) return;
      lista.innerHTML = '';

      projs.forEach(function(p, i) {
        var fila = document.createElement('div');
        fila.style.cssText = 'display:flex;align-items:center;justify-content:space-between;gap:14px;background:#F6F7F9;padding:10px 14px;border-radius:14px;border:1px solid #ECEEF2';
        
        var tipoIcon = p.tipo === 'link' ? '🔗 Enlace' : '📷 Foto';

        fila.innerHTML = [
          '<div style="display:flex;align-items:center;gap:12px;min-width:0;flex:1">',
          '  <img src="' + p.imagen + '" style="width:48px;height:48px;border-radius:10px;object-fit:cover;flex:none;background:#14121F">',
          '  <div style="min-width:0;display:flex;flex-direction:column;gap:3px">' +
          '    <div style="font-weight:800;font-size:14.5px;color:#14121F;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">' + p.titulo + '</div>',
          '    <div style="font-size:12px;color:#5B5664"><span style="color:' + colorPorCat(p.categoria) + ';font-weight:700">' + p.categoria + '</span> • ' + tipoIcon + (p.url ? ' (' + p.url + ')' : '') + '</div>',
          '  </div>',
          '</div>',
          '<div style="display:flex;gap:8px;flex:none">',
          '  <button class="btn-edit-proj" style="background:#fff;border:1px solid #DADDE3;padding:6px 12px;border-radius:8px;cursor:pointer;font-weight:700;font-size:12.5px;color:#087C99">✏ Editar</button>',
          '  <button class="btn-del-proj" style="background:#fff;border:1px solid #E5177B;padding:6px 12px;border-radius:8px;cursor:pointer;font-weight:700;font-size:12.5px;color:#E5177B">🗑 Eliminar</button>',
          '</div>'
        ].join('\n');

        fila.querySelector('.btn-edit-proj').addEventListener('click', function() { editarProyecto(i); });
        fila.querySelector('.btn-del-proj').addEventListener('click', function() { eliminarProyecto(i); });

        lista.appendChild(fila);
      });
    }

    function cambiarTipoProyecto(tipo) {
      var campoUrl = document.getElementById('campo-url-container');
      if (campoUrl) campoUrl.style.display = tipo === 'link' ? 'block' : 'none';
    }

    function mostrarFormularioProyecto() {
      document.getElementById('form-proyecto-container').style.display = 'flex';
      document.getElementById('form-proyecto-titulo-modo').textContent = 'Agregar Nuevo Proyecto';
      document.getElementById('proj-edit-id').value = '';
      document.getElementById('proj-in-titulo').value = '';
      document.getElementById('proj-in-categoria').value = 'Videojuegos';
      document.getElementById('proj-in-tipo').value = 'link';
      cambiarTipoProyecto('link');
      document.getElementById('proj-in-url').value = '';
      document.getElementById('proj-in-imgurl').value = '';
      document.getElementById('proj-in-desc').value = '';
      document.getElementById('preview-foto-box').style.display = 'none';
      document.getElementById('proj-in-titulo').focus();
    }

    function ocultarFormularioProyecto() {
      document.getElementById('form-proyecto-container').style.display = 'none';
    }

    function previsualizarRutaFoto(url) {
      var box = document.getElementById('preview-foto-box');
      var img = document.getElementById('preview-foto-img');
      if (url && url.trim().length > 3) {
        img.src = url.trim();
        box.style.display = 'flex';
      } else {
        box.style.display = 'none';
      }
    }

    function procesarArchivoFoto(e) {
      var file = e.target.files && e.target.files[0];
      if (!file) return;
      var reader = new FileReader();
      reader.onload = function(evt) {
        var base64 = evt.target.result;
        document.getElementById('proj-in-imgurl').value = base64;
        previsualizarRutaFoto(base64);
      };
      reader.readAsDataURL(file);
    }

    function guardarProyectoForm() {
      var titulo = (document.getElementById('proj-in-titulo').value || '').trim();
      if (!titulo) {
        alert('Por favor ingresá un título para el proyecto.');
        return;
      }
      var categoria = document.getElementById('proj-in-categoria').value;
      var tipo = document.getElementById('proj-in-tipo').value;
      var url = (document.getElementById('proj-in-url').value || '').trim();
      var imagen = (document.getElementById('proj-in-imgurl').value || '').trim() || 'assets/entornos/sala-informatica.jpg';
      var desc = (document.getElementById('proj-in-desc').value || '').trim();
      var editId = document.getElementById('proj-edit-id').value;

      var projs = obtenerProyectos();

      if (editId) {
        var idx = projs.findIndex(function(p) { return p.id === editId; });
        if (idx !== -1) {
          projs[idx].titulo = titulo;
          projs[idx].categoria = categoria;
          projs[idx].tipo = tipo;
          projs[idx].url = url;
          projs[idx].imagen = imagen;
          projs[idx].descripcion = desc;
          projs[idx].color = colorPorCat(categoria);
        }
      } else {
        projs.push({
          id: 'proj-' + Date.now(),
          titulo: titulo,
          categoria: categoria,
          tipo: tipo,
          url: url,
          imagen: imagen,
          descripcion: desc,
          color: colorPorCat(categoria)
        });
      }

      guardarProyectos(projs);
      renderizarAdminLista();
      ocultarFormularioProyecto();
    }

    function editarProyecto(index) {
      var projs = obtenerProyectos();
      var p = projs[index];
      if (!p) return;
      mostrarFormularioProyecto();
      document.getElementById('form-proyecto-titulo-modo').textContent = 'Editar Proyecto: ' + p.titulo;
      document.getElementById('proj-edit-id').value = p.id;
      document.getElementById('proj-in-titulo').value = p.titulo;
      document.getElementById('proj-in-categoria').value = p.categoria;
      document.getElementById('proj-in-tipo').value = p.tipo;
      cambiarTipoProyecto(p.tipo);
      document.getElementById('proj-in-url').value = p.url || '';
      document.getElementById('proj-in-imgurl').value = p.imagen || '';
      previsualizarRutaFoto(p.imagen || '');
      document.getElementById('proj-in-desc').value = p.descripcion || '';
    }

    function eliminarProyecto(index) {
      if (!confirm('¿Estás seguro de que deseás eliminar este proyecto?')) return;
      var projs = obtenerProyectos();
      projs.splice(index, 1);
      guardarProyectos(projs);
      renderizarAdminLista();
    }

    function descargarProyectosJSON() {
      var projs = obtenerProyectos();
      var blob = new Blob([JSON.stringify(projs, null, 2)], { type: 'application/json' });
      var a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = 'proyectos.json';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    }

    // Expose helpers globally if needed
    window.abrirLightbox = abrirLightbox;
    window.cerrarLightbox = cerrarLightbox;
    window.abrirAdminProyectos = abrirAdminProyectos;
    window.cerrarAdminProyectos = cerrarAdminProyectos;
    window.verificarAdminPin = verificarAdminPin;

    function initGaleriaAdmin() {
      var btnAdmin = document.getElementById('btn-admin-proyectos');
      if (btnAdmin && !btnAdmin._bound) {
        btnAdmin._bound = true;
        btnAdmin.addEventListener('click', function(e) {
          e.preventDefault();
          abrirAdminProyectos();
        });
      }
      renderizarGaleria();
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initGaleriaAdmin);
    } else {
      initGaleriaAdmin();
    }
    
    // Polling safety check until rendered
    var timer = setInterval(function() {
      var grid = document.getElementById('galeria-proyectos-grid');
      var btnAdmin = document.getElementById('btn-admin-proyectos');
      if (btnAdmin && !btnAdmin._bound) {
        btnAdmin._bound = true;
        btnAdmin.addEventListener('click', function(e) {
          e.preventDefault();
          abrirAdminProyectos();
        });
      }
      if (grid && grid.children.length === 0) {
        renderizarGaleria();
      }
    }, 400);
    setTimeout(function() { clearInterval(timer); }, 8000);

  })();
  </script>
"""

    data = data[:s_script] + new_script_content + data[s_body_end:]

    new_json_str = json.dumps(data)
    new_json_str = new_json_str.replace('</', r'<\u002F')
    new_html = html[:json_start] + new_json_str + html[end_offset:]

    with open('PrototipoJuan.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

    print("SUCCESS: Guia movida al modal de administracion y removida de la vista publica!")

if __name__ == '__main__':
    update_galeria_and_modal()
