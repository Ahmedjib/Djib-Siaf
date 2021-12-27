# -*- coding: utf-8 -*-

from odoo import models, fields, api

class siaf_zone(models.Model):
    _name = 'siaf.zone'
    _description = 'Zone de Local'

    def name_get(self):
        res=[]
        for rec in self:
            res.append((rec.id, '%s %s' % (rec.name, rec.Address)))
        return res
    
    name = fields.Char("Zone Name", required=True)
    Address = fields.Text("Address", required=True)
    
class siaf_type(models.Model):
    _name = 'siaf.type'
    _description = 'Type de Local'

    name = fields.Char("Type Name", required=True)

class siaf_project(models.Model):   
    _name = 'siaf.project'
    _description = 'Project'
    
    def name_get(self):
        res=[]
        for rec in self:
            res.append((rec.id, '%s %s' % (rec.Nom_Projet, rec.Address)))
        return res
    
    Nom_Projet = fields.Char('Nom du Projet')
    Numéro_Projet = fields.Integer('Numéro du Projet')
    Address = fields.Text("Address", required=True)
    Project_doc = fields.Selection([
        ('pdf', 'PDF'), ('google_slide', 'Google Slide'), ('text', 'Text')],
        string="Work Sheet", default="pdf",
        help="Defines if you want to use a PDF or a Google Slide."
    )
    note = fields.Html('Description', help="Text worksheet description")
    worksheet = fields.Binary('PDF')
    worksheet_google_slide = fields.Char('Google Slide', help="Paste the url of your Google Slide. Make sure the access to the document is public.")
    
class siaf_article(models.Model):
    _inherit = 'product.template'
    
    N_d_Lot = fields.Integer('Numéro de Lot' )
    S_d_Lot = fields.Float('Superficie du Lot')
    Project_ids = fields.Many2one('siaf.project')
    Zone_ID = fields.Many2one('siaf.zone', required=True)
    Type_ID = fields.Many2one('siaf.type')
    Article_type = fields.Selection([
        ('pdf', 'PDF'), ('google_slide', 'Google Slide'), ('text', 'Text')],
        string="Work Sheet", default="pdf",
        help="Defines if you want to use a PDF or a Google Slide."
    )
    note = fields.Html('Description', help="Text worksheet description")
    worksheet = fields.Binary('PDF')
    worksheet_google_slide = fields.Char('Google Slide', help="Paste the url of your Google Slide. Make sure the access to the document is public.")
    
class siaf_contrat(models.Model):
    _description = 'siaf_contrat'
    
    N_d_contrat = fields.Integer('Numéro du contrat',required=True )

class siaf_res_partner(models.Model):
    _inherit = 'res.partner'
    
    Numéro_CNI = fields.Integer('Numéro CNI',required=True )
    Documentations = fields.Many2many('ir.attachment', 'class_ir_attachments_rel', 'class_id', 'attachment_id', 'Attachments')
    


