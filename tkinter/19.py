import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import mysql.connector
from mysql.connector import Error

class MySQLConnectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conector MySQL")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        self.connection = None
        self.cursor = None
        
        self.setup_ui()
        
    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar pesos de columnas
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Título
        title_label = ttk.Label(main_frame, text="CONEXIÓN A BASE DE DATOS MySQL", 
                                font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Frame de conexión
        conn_frame = ttk.LabelFrame(main_frame, text="Datos de Conexión", padding="10")
        conn_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        conn_frame.columnconfigure(1, weight=1)
        
        # Campos de conexión
        ttk.Label(conn_frame, text="Host:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.host_entry = ttk.Entry(conn_frame, width=30)
        self.host_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
        self.host_entry.insert(0, "localhost")
        
        ttk.Label(conn_frame, text="Puerto:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.port_entry = ttk.Entry(conn_frame, width=30)
        self.port_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        self.port_entry.insert(0, "3306")
        
        ttk.Label(conn_frame, text="Usuario:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.user_entry = ttk.Entry(conn_frame, width=30)
        self.user_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(conn_frame, text="Contraseña:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.password_entry = ttk.Entry(conn_frame, width=30, show="*")
        self.password_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(conn_frame, text="Base de Datos:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.database_entry = ttk.Entry(conn_frame, width=30)
        self.database_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Botones de conexión
        button_frame = ttk.Frame(conn_frame)
        button_frame.grid(row=5, column=0, columnspan=2, pady=10)
        
        self.connect_btn = ttk.Button(button_frame, text="Conectar", command=self.connect_to_mysql)
        self.connect_btn.pack(side=tk.LEFT, padx=5)
        
        self.disconnect_btn = ttk.Button(button_frame, text="Desconectar", command=self.disconnect_from_mysql, state=tk.DISABLED)
        self.disconnect_btn.pack(side=tk.LEFT, padx=5)
        
        # Frame de consultas
        query_frame = ttk.LabelFrame(main_frame, text="Consultas SQL", padding="10")
        query_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        query_frame.columnconfigure(0, weight=1)
        query_frame.rowconfigure(1, weight=1)
        
        # Área de consulta
        ttk.Label(query_frame, text="Ingrese su consulta SQL:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.query_text = scrolledtext.ScrolledText(query_frame, height=5, width=70)
        self.query_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        # Botón ejecutar
        self.execute_btn = ttk.Button(query_frame, text="Ejecutar Consulta", 
                                      command=self.execute_query, state=tk.DISABLED)
        self.execute_btn.grid(row=2, column=0, pady=10)
        
        # Frame de resultados
        result_frame = ttk.LabelFrame(main_frame, text="Resultados", padding="10")
        result_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        result_frame.columnconfigure(0, weight=1)
        result_frame.rowconfigure(0, weight=1)
        
        # Treeview para mostrar resultados
        self.result_tree = ttk.Treeview(result_frame, show="headings", height=10)
        self.result_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbar para el treeview
        scrollbar = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, command=self.result_tree.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.result_tree.configure(yscrollcommand=scrollbar.set)
        
        # Estado de conexión
        self.status_label = ttk.Label(main_frame, text="Estado: Desconectado", relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
    def connect_to_mysql(self):
        try:
            # Obtener datos de conexión
            host = self.host_entry.get()
            port = self.port_entry.get()
            user = self.user_entry.get()
            password = self.password_entry.get()
            database = self.database_entry.get() if self.database_entry.get() else None
            
            # Crear conexión
            self.connection = mysql.connector.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database
            )
            
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                
                # Actualizar UI
                self.status_label.config(text=f"Estado: Conectado a {host}:{port} - Usuario: {user}")
                self.connect_btn.config(state=tk.DISABLED)
                self.disconnect_btn.config(state=tk.NORMAL)
                self.execute_btn.config(state=tk.NORMAL)
                
                messagebox.showinfo("Éxito", "Conexión establecida correctamente")
                
        except Error as e:
            messagebox.showerror("Error de Conexión", f"No se pudo conectar a MySQL:\n{str(e)}")
            
    def disconnect_from_mysql(self):
        try:
            if self.connection and self.connection.is_connected():
                if self.cursor:
                    self.cursor.close()
                self.connection.close()
                
                # Actualizar UI
                self.status_label.config(text="Estado: Desconectado")
                self.connect_btn.config(state=tk.NORMAL)
                self.disconnect_btn.config(state=tk.DISABLED)
                self.execute_btn.config(state=tk.DISABLED)
                
                # Limpiar resultados
                self.clear_treeview()
                
                messagebox.showinfo("Desconectado", "Conexión cerrada correctamente")
                
        except Error as e:
            messagebox.showerror("Error", f"Error al desconectar:\n{str(e)}")
            
    def execute_query(self):
        if not self.connection or not self.connection.is_connected():
            messagebox.showwarning("Sin conexión", "Primero debe conectarse a la base de datos")
            return
            
        query = self.query_text.get("1.0", tk.END).strip()
        
        if not query:
            messagebox.showwarning("Consulta vacía", "Por favor ingrese una consulta SQL")
            return
            
        try:
            # Ejecutar consulta
            self.cursor.execute(query)
            
            # Verificar si es SELECT u otra consulta
            if query.strip().upper().startswith("SELECT"):
                # Obtener resultados
                results = self.cursor.fetchall()
                columns = [desc[0] for desc in self.cursor.description]
                
                # Mostrar resultados
                self.display_results(columns, results)
                messagebox.showinfo("Éxito", f"Consulta ejecutada. {len(results)} filas obtenidas.")
            else:
                # Para INSERT, UPDATE, DELETE
                self.connection.commit()
                rows_affected = self.cursor.rowcount
                self.clear_treeview()
                messagebox.showinfo("Éxito", f"Consulta ejecutada. {rows_affected} filas afectadas.")
                
        except Error as e:
            messagebox.showerror("Error de Consulta", f"Error al ejecutar la consulta:\n{str(e)}")
            # Revertir cambios si hubo error
            if self.connection:
                self.connection.rollback()
                
    def display_results(self, columns, results):
        # Limpiar treeview actual
        self.clear_treeview()
        
        # Configurar columnas
        self.result_tree["columns"] = columns
        
        # Configurar encabezados
        for col in columns:
            self.result_tree.heading(col, text=col)
            self.result_tree.column(col, width=100, anchor=tk.W)
            
        # Insertar datos
        for row in results:
            self.result_tree.insert("", tk.END, values=row)
            
    def clear_treeview(self):
        self.result_tree["columns"] = []
        for item in self.result_tree.get_children():
            self.result_tree.delete(item)

def main():
    root = tk.Tk()
    app = MySQLConnectorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()