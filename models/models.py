# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Modulos(models.Model):
    _name = 'alumnos.modulos'
    _description = 'Modulos disponibles'
    _rec_name = 'nombre' # Esto indica que campo mostrar cuando se busca en otro modelo

    # Campo básico para el nombre del tipo (ej: Mantenimiento, Desarrollo, Admin)
    nombre = fields.Char(string="Nombre del Módulo", required=True)
    descripcion = fields.Text(string="Descripción")
    # Relación inversa (opcional pero muy útil): ver qué alumnos están matriculados
    # alumnos_ids = fields.Many2many(
    #    comodel_name='alumnos.alumnos',
    #    relation='alumnos_alumnos_modulos_rel',  # nombre tabla intermedia
    #    column1='modulo_id',                    # FK hacia alumnos.modulos
    #    column2='alumno_id',                    # FK hacia alumnos.alumnos
    #    string="Alumnos matriculados",
    #    help="Alumnos que están matriculados en este módulo"
    #)
    # Para evitar duplicados de módulos con el mismo nombre pongo un sql constraint
    # la otra forma peor, sería poner una constraint sobre el atributo nombre de la forma
    # from odoo.exceptions import ValidationError
    # @api.constrains('nombre')
    # def _check_nombre_unique(self):     
    #   for rec in self:
    #     if rec.nombre and self.search_count([('nombre', '=', rec.nombre), ('id', '!=', rec.id)]) > 0:
    #         raise ValidationError("Ya existe un módulo con ese nombre.")
        
    _sql_constraints = [
        ('modulo_nombre_unique', 'unique(nombre)', 'Ya existe un módulo con ese nombre.'),
    ]

class Alumnos(models.Model):
    _name = 'alumnos.alumnos'
    _description = 'Modelo principal para gestionar alumnos'

    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required= True)
    foto = fields.Image(
        string="Foto",
        max_width=1024,
        max_height=1024,
        help="Foto del alumno (se redimensiona si excede el máximo)."
    )
    # Campo para mostrar el alumno como "Nombre Apellidos"
    nombre_completo = fields.Char(
        string="Nombre completo",
        compute="_compute_nombre_completo",
        store=True
    )

    # --- NUEVO CAMPO RELACIONAL (Many2many) ---
    # Relaciona esta tarea con un único registro del modelo 'lista_tareas.tipo_tarea'
    modulos_ids = fields.Many2many(
        comodel_name='alumnos.modulos', # Nombre exacto del otro modelo
        # los argumentos siguientes son opcionales para forzar el nombre de la tabla intermedia
        # relation='alumnos_alumnos_modulos_rel',  # MISMA tabla intermedia que arriba
        # column1='alumno_id',                     # FK hacia alumnos.alumnos
        # column2='modulo_id',                     # FK hacia alumnos.modulos
        string="Módulos matriculados",
        help="Módulos en los que ha sido matriculado el alumno"
    )

    @api.depends('nombre', 'apellidos')
    def _compute_nombre_completo(self):
        for rec in self:
            # evitamos el None y quitamos los espacios en los extremos con strip
            n = (rec.nombre or '').strip()
            a = (rec.apellidos or '').strip()
            rec.nombre_completo = (n + " " + a).strip()

