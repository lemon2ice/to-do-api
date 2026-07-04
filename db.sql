-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS todo_app;
USE todo_app;

-- Crear la tabla de tareas
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status ENUM('pending', 'in_progress', 'completed') DEFAULT 'pending',
    priority ENUM('low', 'medium', 'high') DEFAULT 'medium',
    due_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Crear usuario solo si no existe (así se crea una única vez)
CREATE USER IF NOT EXISTS 'api_todo'@'localhost' IDENTIFIED BY 'h5399NO2ew$Y';

-- Otorgar solo los permisos necesarios para un CRUD sobre la tabla de tareas
GRANT SELECT, INSERT, UPDATE, DELETE ON todo_app.tasks TO 'api_todo'@'localhost';

-- Aplicar cambios de privilegios
FLUSH PRIVILEGES;

-- Insertar algunos datos de ejemplo
INSERT INTO tasks (title, description, status, priority, due_date) VALUES
('Comprar leche', 'Ir al supermercado y comprar leche deslactosada', 'pending', 'high', '2026-06-10'),
('Estudiar SQL', 'Repasar consultas avanzadas de MySQL', 'in_progress', 'medium', '2026-06-09'),
('Hacer ejercicio', '30 minutos de cardio', 'completed', 'low', '2026-06-08'),
('Llamar al médico', 'Agendar cita para chequeo anual', 'pending', 'high', '2026-06-12');