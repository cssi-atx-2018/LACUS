import webapp2
import jinja2

template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env=jinja2.Environment(loader=template_loader)

ac_dict = {'4TTV0024A': [22, 24000], '4TTV0036A': [22, 36000], '4TTV0048A': [22, 48000], '4TTV0060A': [22, 60000]}
states_dict = {'tx': 10.98}

class AppliancePage(webapp2.RequestHandler):
    def get(self):
        beg_template = template_env.get_template('templates/appliances.html')
        self.response.write(beg_template.render())

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        ac=str(self.request.get('ac-type'))
        ac2=str(self.request.get('ac-type-2'))
        state = str(self.request.get('state'))
        seer = ac_dict[ac][0]
        size = ac_dict[ac][1]
        seer2 = ac_dict[ac2][0]
        size2 = ac_dict[ac2][1]
        money = states_dict[state]
        my_dict = {'seer': seer, 'size': size, 'money': money, 'seer2': seer2, 'size2': size2}
        end_template = template_env.get_template('templates/app-results.html')
        self.response.write(end_template.render(my_dict))




app = webapp2.WSGIApplication([
    ('/appliances', AppliancePage),
], debug=True)
