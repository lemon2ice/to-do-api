from datetime import datetime
from typing import List, Dict, Optional

class TaskModel:
    # Almacenamiento en memoria
    _tasks: Dict[int, dict] = {}
    _next_id: int = 1
    
    @staticmethod
    def get_all_tasks() -> List[dict]:
        """Obtener todas las tareas ordenadas por fecha de creación descendente"""
        tasks = list(TaskModel._tasks.values())
        tasks.sort(key=lambda x: x['created_at'], reverse=True)
        return tasks
    
    @staticmethod
    def get_task_by_id(task_id: int) -> Optional[dict]:
        """Obtener una tarea por su ID"""
        return TaskModel._tasks.get(task_id)
    
    @staticmethod
    def create_task(title: str, description: str, priority: str, due_date: str, status: str = "pending") -> int:
        """Crear una nueva tarea"""
        task_id = TaskModel._next_id
        TaskModel._next_id += 1
        
        task = {
            'id': task_id,
            'title': title,
            'description': description,
            'priority': priority,
            'due_date': due_date if due_date else None,
            'status': status,
            'created_at': datetime.now()
        }
        
        TaskModel._tasks[task_id] = task
        return task_id
    
    @staticmethod
    def update_task(task_id: int, title: str, description: str, priority: str, due_date: str, status: str):
        """Actualizar una tarea existente"""
        if task_id in TaskModel._tasks:
            TaskModel._tasks[task_id].update({
                'title': title,
                'description': description,
                'priority': priority,
                'due_date': due_date if due_date else None,
                'status': status
            })
    
    @staticmethod
    def delete_task(task_id: int):
        """Eliminar una tarea"""
        if task_id in TaskModel._tasks:
            del TaskModel._tasks[task_id]
    
    @staticmethod
    def update_status(task_id: int, status: str):
        """Actualizar solo el estado de una tarea"""
        if task_id in TaskModel._tasks:
            TaskModel._tasks[task_id]['status'] = status