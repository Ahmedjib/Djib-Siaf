# -*- coding: utf-8 -*-

from odoo import models, fields, api

class siaf_zone(models.Model):
    _name = 'siaf.zone'
    _description = 'Zone de Local'

    name = fields.Char("Zone Name", required=True)
    Address = fields.Text("Address", required=True)
    
class siaf_type(models.Model):
    _name = 'siaf.type'
    _description = 'Type de Local'

    name = fields.Char("Type Name", required=True)
    
    
class siaf_article(models.Model):
    _inherit = 'product.template'
    
    N_d_Lot = fields.Interger('Numéro de Lot',required=True )
    S_d_Lot = fields.Float('Superficie du Lot',required=True)
    Nom_Projet = fields.Char('Nom du Projet')
    Numéro_Projet = fields.Inter('Numéro du Projet')
    Zone = fields.Many2one('siaf.zone')
