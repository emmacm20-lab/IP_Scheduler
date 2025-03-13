# 📂 src/schedule_task.py - Automatización de eventos en Windows
import os

def schedule_ip_change():
    """Programa un evento en Windows Task Scheduler para cambiar la IP periódicamente."""
    task_name = "Change_IP_Task"
    script_path = os.path.abspath("change_ip.py")
    command = f"schtasks /create /tn {task_name} /tr \"python {script_path}\" /sc daily /st 12:00"
    os.system(command)
    print("Tarea programada exitosamente.")

if __name__ == "__main__":
    schedule_ip_change()