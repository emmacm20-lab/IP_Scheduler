# 📂 docs/README.md - Documentación del Proyecto
"""
# 🔄 Automatización de Cambio de IP en Windows mediante Eventos Programados

## 📌 Descripción del Proyecto

Este proyecto permite la automatización del cambio de **IP pública** en un sistema Windows mediante eventos programados. Cuando se activa una acción en el sistema, se ejecuta un evento de Windows que configura una IP específica.

### 📌 ¿Para qué es útil?
- ✅ **Gestión de acceso y seguridad**: Permite cambiar la IP pública para acceder a ciertos servicios con restricciones geográficas o de seguridad.
- ✅ **Balanceo de conexiones**: Alternar entre diferentes IPs puede ayudar a optimizar el uso del ancho de banda.
- ✅ **Automatización en entornos empresariales**: útil para empresas que necesitan cambiar direcciones IP de servidores por políticas internas.

## 📂 Estructura del Proyecto
```
📁 IP_Scheduler
│── 📂 src/
│   │── change_ip.py       # Script para modificar la IP en Windows
│   │── schedule_task.py   # Automatización de eventos de Windows
│── 📂 tests/
│   │── test_change_ip.py  # Pruebas para cambio de IP
│── 📂 docs/
│   │── README.md          # Documentación del proyecto
```

## 🚀 Instalación y Ejecución

1. **Clona este repositorio:**
   ```sh
   git clone https://github.com/emmacm20-lab/IP_Scheduler.git
   ```
2. **Ejecuta el script para programar el evento en Windows:**
   ```sh
   python src/schedule_task.py  # Configura el evento de Windows
   ```
3. **Para cambiar manualmente la IP ejecuta:**
   ```sh
   python src/change_ip.py  # Cambia la IP configurada
   ```

## 📩 Flujo de Trabajo
1. **Definición de IPs**: El usuario configura la IP deseada en el script.
2. **Programación del Evento en Windows**: Se ejecuta un `task scheduler` que activa el cambio de IP automáticamente.
3. **Ejecuta cambio de IP**: Se activa el comando para modificar la configuración de red según la planificación definida.

## 🛠 Tecnologías Utilizadas
- **Python**: Automación del cambio de IP y programación de eventos.
- **Windows Task Scheduler**: Configuración de tareas programadas.
- **PowerShell**: Comandos para modificar la IP en el sistema.

## 📈 Resultados Esperados
- 📌 **Automatización del cambio de IP sin intervención manual.**
- 📌 **Facilidad de integración con redes empresariales y de seguridad.**
- 📌 **Ejecución de eventos programados sin necesidad de supervisión.**

## 🧪 Pruebas
El proyecto incluye pruebas unitarias para validar el correcto funcionamiento del cambio de IP.
1. **Ejecución de pruebas:**
   ```sh
   python -m unittest discover tests/
   ```

## 📬 Contacto
Para consultas o sugerencias, contáctame en [emmanuel.cmora20@gmail.com].
"""
