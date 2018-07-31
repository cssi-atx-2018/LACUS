import webapp2
import jinja2

template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env=jinja2.Environment(loader=template_loader)

def seers(x):
    arr = [22]
    return arr[x]

def sizes(y):
    lis = [24000]
    return lis[y]

def states(z):
    if z == 'tx':
        return 10.98

class AppliancePage(webapp2.RequestHandler):
    def get(self):
        beg_template = template_env.get_template('appliances.html')
        self.response.write(beg_template.render())



    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        ac=self.request.get('ac-type')
        ac = int(ac)
        price = self.request.get('state')
        price = str(price)
        seer = seers(ac)
        size = sizes(ac)
        money = states(price)
        my_dict = {'seer': seer, 'sizes': size, 'money': money}
        end_template = template_env.get_template('app-results.html')
        self.response.write(end_template.render(my_dict))




app = webapp2.WSGIApplication([
    ('/appliances', AppliancePage),
], debug=True)

