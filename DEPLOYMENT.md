# Guía de Despliegue - PNLIO Framework

Este documento proporciona instrucciones para desplegar la página web del PNLIO Framework en diferentes plataformas.

---

## 🚀 Opciones de Despliegue

### 1. GitHub Pages (GRATUITO - Recomendado)

**Ventajas:**
- Completamente gratuito
- Integrado con GitHub
- Despliegue automático
- HTTPS incluido

**Pasos:**

1. Ve a: `https://github.com/godear6959-creator/PNLIO-Framework/settings/pages`
2. En "Source", selecciona "Deploy from a branch"
3. Selecciona rama: `main`
4. Selecciona carpeta: `/ (root)`
5. Click en "Save"

**Tu página estará en:**
```
https://godear6959-creator.github.io/PNLIO-Framework
```

**Tiempo de despliegue:** 1-2 minutos

---

### 2. Vercel (GRATUITO)

**Ventajas:**
- Gratuito para proyectos públicos
- Despliegue automático desde GitHub
- Performance optimizado
- Analytics incluido

**Pasos:**

1. Ve a: `https://vercel.com`
2. Haz clic en "New Project"
3. Importa el repositorio de GitHub: `godear6959-creator/PNLIO-Framework`
4. Vercel detectará automáticamente la configuración
5. Click en "Deploy"

**Tu página estará en:**
```
https://pnlio-framework.vercel.app
```

**Tiempo de despliegue:** 2-5 minutos

---

### 3. Netlify (GRATUITO)

**Ventajas:**
- Gratuito para proyectos públicos
- Despliegue automático desde GitHub
- Formularios y funciones serverless
- Preview automáticas

**Pasos:**

1. Ve a: `https://netlify.com`
2. Haz clic en "New site from Git"
3. Selecciona GitHub como proveedor
4. Autoriza Netlify en GitHub
5. Selecciona el repositorio: `godear6959-creator/PNLIO-Framework`
6. Netlify detectará automáticamente la configuración
7. Click en "Deploy site"

**Tu página estará en:**
```
https://pnlio-framework.netlify.app
```

**Tiempo de despliegue:** 2-5 minutos

---

### 4. Railway (PAGO - Prueba Gratuita)

**Ventajas:**
- Prueba gratuita de $5 USD
- Fácil de usar
- Soporte para múltiples servicios
- Escalable

**Pasos:**

1. Ve a: `https://railway.app`
2. Haz clic en "New Project"
3. Selecciona "Deploy from GitHub repo"
4. Autoriza Railway en GitHub
5. Selecciona el repositorio: `godear6959-creator/PNLIO-Framework`
6. Railway usará `railway.json` para la configuración
7. Click en "Deploy"

**Tu página estará en:**
```
https://pnlio-framework.up.railway.app
```

**Tiempo de despliegue:** 3-5 minutos
**Costo:** Después de créditos gratuitos, ~$5-10 USD/mes

---

### 5. Render (PAGO - Prueba Gratuita)

**Ventajas:**
- Prueba gratuita
- Interfaz intuitiva
- Despliegue automático
- Escalable

**Pasos:**

1. Ve a: `https://render.com`
2. Haz clic en "New +"
3. Selecciona "Web Service"
4. Conecta tu repositorio de GitHub
5. Selecciona: `godear6959-creator/PNLIO-Framework`
6. Render usará `render.yaml` para la configuración
7. Click en "Create Web Service"

**Tu página estará en:**
```
https://pnlio-framework.onrender.com
```

**Tiempo de despliegue:** 3-5 minutos
**Costo:** Después de créditos gratuitos, ~$7 USD/mes

---

## 📋 Comparativa de Plataformas

| Plataforma | Costo | Tiempo | HTTPS | Auto-Deploy | Recomendación |
|-----------|-------|--------|-------|-------------|---------------|
| GitHub Pages | Gratuito | 1-2 min | ✅ | ✅ | ⭐⭐⭐⭐⭐ |
| Vercel | Gratuito | 2-5 min | ✅ | ✅ | ⭐⭐⭐⭐⭐ |
| Netlify | Gratuito | 2-5 min | ✅ | ✅ | ⭐⭐⭐⭐⭐ |
| Railway | $5+ USD | 3-5 min | ✅ | ✅ | ⭐⭐⭐ |
| Render | $7+ USD | 3-5 min | ✅ | ✅ | ⭐⭐⭐ |

---

## 🔧 Configuración Incluida

Este repositorio incluye archivos de configuración para todas las plataformas:

- **`.github/workflows/pages.yml`** - GitHub Pages
- **`vercel.json`** - Vercel
- **`netlify.toml`** - Netlify
- **`railway.json`** - Railway
- **`render.yaml`** - Render

---

## 📝 Notas Importantes

1. **Despliegue Automático:** Cada push a la rama `main` actualiza automáticamente tu página en todas las plataformas

2. **Dominio Personalizado:** Todas las plataformas permiten agregar tu propio dominio personalizado

3. **HTTPS:** Todas las plataformas proporcionan certificados SSL/HTTPS gratuitos

4. **Rendimiento:** Para mejor rendimiento, se recomienda usar GitHub Pages, Vercel o Netlify

---

## 🎯 Recomendación

**Para mejor experiencia, se recomienda:**

1. **Primero:** Activa GitHub Pages (gratuito, sin configuración adicional)
2. **Segundo:** Despliega en Vercel o Netlify (gratuito, mejor rendimiento)
3. **Opcional:** Usa Railway o Render si necesitas funcionalidades avanzadas

---

## 📞 Soporte

Si tienes problemas con el despliegue:

1. Verifica que el repositorio sea público
2. Asegúrate de que `index.html` esté en la raíz del repositorio
3. Revisa los logs de despliegue en la plataforma
4. Consulta la documentación oficial de cada plataforma

---

**¡Tu página web del PNLIO Framework está lista para desplegar!**
