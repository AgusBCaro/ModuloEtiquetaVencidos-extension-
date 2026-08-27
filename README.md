# Módulo de Extensión Odoo: Alerta de Facturas Vencidas (> 90 Días)

Este módulo de extensión para **Odoo Facturación / Contabilidad** añade la lógica y etiquetas necesarias para identificar y etiquetar automáticamente como **"Vencida"** a cualquier factura publicada en estado **"No pagadas"** que haya superado los **90 días de antigüedad** desde su fecha de vencimiento (o fecha de emisión).

---

## 🌟 Características Principales

1. **Etiquetado Automático:**
   - Detecta de forma dinámica las facturas en estado de pago **"No pagadas"** (`not_paid`) o **Parciales** (`partial`).
   - Asigna la etiqueta badge **"Vencida"** (en color rojo) cuando `días > 90`.

2. **Detección Visual en Vista Lista:**
   - Colorea en **rojo** toda la fila de la factura que supere los 90 días de vencimiento (`decoration-danger`).
   - Muestra la columna / badge de mora **"Vencida"** antes del estado de pago.

3. **Filtro de Búsqueda Rápida:**
   - Añade la opción **"Vencidas (> 90 días)"** en la barra de filtros de Facturación para consultar en un clic la lista completa de morosos a +90 días.

---

## 📁 Estructura del Módulo

```text
ModuloEtiquetaVencidos(extension)/
├── __manifest__.py           # Manifiesto y metadatos del módulo Odoo
├── __init__.py               # Inicializador Python del módulo
├── README.md                 # Documentación e instrucciones
├── models/
│   ├── __init__.py           # Inicializador de modelos
│   └── account_move.py       # Extensión de account.move (cálculo y búsqueda de mora)
└── views/
    └── account_move_views.xml# Vistas XML heredadas (tree views y vista search)
```

---

## 🛠️ Instrucciones de Instalación en Odoo

1. **Copiar o Enlazar el Módulo:**
   Copia la carpeta de este repositorio en el directorio de addons de tu servidor Odoo (por ejemplo `custom_addons` o `/var/lib/odoo/addons/`):
   ```bash
   cp -r ModuloEtiquetaVencidos(extension) /ruta/a/tu/odoo/custom_addons/account_invoice_overdue_90
   ```

2. **Reiniciar Odoo:**
   Reinicia el servicio de tu Odoo:
   ```bash
   sudo service odoo restart
   # O en Docker:
   docker restart odoo_container_name
   ```

3. **Actualizar Lista de Aplicaciones:**
   - Accede a Odoo con un usuario Administrador.
   - Activa el **Modo Desarrollador** (*Ajustes -> Activar modo desarrollador*).
   - Dirígete al menú **Aplicaciones**.
   - Haz clic en **Actualizar lista de aplicaciones** en la barra superior.

4. **Instalar el Módulo:**
   - En la barra de búsqueda de Aplicaciones, quita el filtro predeterminado *Aplicaciones*.
   - Busca: `Facturación - Alerta Vencido 90 Días` (o nombre técnico: `account_invoice_overdue_90`).
   - Haz clic en **Instalar**.

---

## 🧪 Verificación de Funcionamiento

1. Ve a **Facturación / Contabilidad -> Clientes -> Facturas** (o *Proveedores -> Facturas*).
2. Aquellas facturas en estado **"No pagadas"** con más de 90 días desde su fecha de vencimiento mostrarán:
   - Fila resaltada en rojo.
   - Badge con la etiqueta **"Vencida"**.
3. En la barra de búsqueda, haz clic en **Filtros** y selecciona **"Vencidas (> 90 días)"** para filtrar únicamente esas facturas.
