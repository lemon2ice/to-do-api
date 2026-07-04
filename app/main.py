from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.models import TaskModel

app = FastAPI(title="To-Do List App")

# Configurar templates
templates = Jinja2Templates(directory="app/templates")

# Ruta principal: listar tareas
@app.get("/")
def index(request: Request):
    tasks = TaskModel.get_all_tasks()
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

# Formulario para crear tarea
@app.get("/tasks/create")
def create_form(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

# Procesar creación
@app.post("/tasks")
def create_task(
    title: str = Form(...),
    description: str = Form(""),
    priority: str = Form("medium"),
    due_date: str = Form(None)
):
    TaskModel.create_task(title, description, priority, due_date)
    return RedirectResponse("/", status_code=303)

# Ver detalle / editar tarea (formulario con datos actuales)
@app.get("/tasks/{task_id}/edit")
def edit_form(request: Request, task_id: int):
    task = TaskModel.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return templates.TemplateResponse("edit.html", {"request": request, "task": task})

# Procesar actualización
@app.post("/tasks/{task_id}/update")
def update_task(
    task_id: int,
    title: str = Form(...),
    description: str = Form(""),
    priority: str = Form("medium"),
    due_date: str = Form(None),
    status: str = Form("pending")
):
    task = TaskModel.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    TaskModel.update_task(task_id, title, description, priority, due_date, status)
    return RedirectResponse("/", status_code=303)

# Cambiar estado rápidamente (pendiente, en progreso, completada)
@app.post("/tasks/{task_id}/status")
def change_status(task_id: int, status: str = Form(...)):
    task = TaskModel.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    TaskModel.update_status(task_id, status)
    return RedirectResponse("/", status_code=303)

# Eliminar tarea
@app.post("/tasks/{task_id}/delete")
def delete_task(task_id: int):
    task = TaskModel.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    TaskModel.delete_task(task_id)
    return RedirectResponse("/", status_code=303)