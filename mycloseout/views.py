from mycloseout.models import DBSession
from mycloseout.models import Leads
from pyramid.view import view_config

@view_config(route_name='home', renderer='landing.mak')
def landing_page(request):
    if request.POST.get('Submit'):
        email  = request.POST.get('email')
        lead = Leads(email)
        session = DBSession()
        session.add(lead)
    return {}
    

		
