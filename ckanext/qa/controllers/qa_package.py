from ckan.lib.base import render, c
from ckanext.qa.reports import five_stars, broken_resource_links_by_dataset
from base import QAController

class QAPackageController(QAController):
    
    def index(self):                
        return render('ckanext/qa/dataset/index.html')

    def five_stars(self):
        c.packages = five_stars()
        return render('ckanext/qa/dataset/five_stars/index.html')

    def broken_resource_links(self):
        c.packages = broken_resource_links_by_dataset()
        return render('ckanext/qa/dataset/broken_resource_links/index.html')
