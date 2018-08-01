import webapp2
import jinja2
import air_con

template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env=jinja2.Environment(loader=template_loader)

"""ac_dict = {"Trane XV20i TruComfort Variable Speed, Model 4TTV0024A": [22, 24000],
    "Trane XV20i TruComfort Variable Speed, Model 4TTV0036A": [22, 36000],
    "Trane XV20i TruComfort Variable Speed, Model 4TTV0048A": [22, 48000],
    "Trane XV20i TruComfort Variable Speed, Model 4TTV0060A": [22, 60000]}
states_dict = {'Texas': 10.98}"""

def avgthese(a, b):
    one = int(a)
    two = int(b)
    sum = one+two
    return sum/2
        
class HomePage(webapp2.RequestHandler):
    def get(self):
        home_temp = template_env.get_template('templates/home.html')
        self.response.write(home_temp.render())

class AboutPage(webapp2.RequestHandler):
    def get(self):
        about_temp = template_env.get_template('templates/about_temp.html')
        self.response.write(about_temp.render())        
      
class RegionPage(webapp2.RequestHandler):
    def get(self):
        region_template = template_env.get_template('templates/region.html')
        self.response.write(region_template.render())

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        min = self.request.get('mintemp')
        max = self.request.get('maxtemp')
        avg = avgthese(min, max)
        regavg = 69.95
        stavg = 69.9
        if avg < stavg:
            diff = stavg - avg
            diffst = 'Your household setpoint is {diff} degrees lower than your state\'s average.'.format(diff=diff)
        elif avg > stavg:
            diff = avg - stavg
            diffst = 'Your household setpoint is {diff} degrees higher than your state\'s average.'.format(diff=diff)
        else:
            diff = 0
            diffst = 'Your household setpoint is equal to your state\'s average.'
        result_dict = {
                    'user': 'Your average temperature is {user}.'.format(user=avg),
                    'region': 'Your region\'s average temperature is {regavg}.'.format(regavg=regavg),
                    'state': 'Your state\'s average temperature is {stavg}.'.format(stavg=stavg),
                    'diff': diffst}
        region_template = template_env.get_template('templates/region.html')
        self.response.write(region_template.render(result_dict))

class AppliancePage(webapp2.RequestHandler):
    def get(self):
        beg_template = template_env.get_template('templates/app-results.html')
        self.response.write(beg_template.render())

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        ac=str(self.request.get('ac-type'))
        ac2=str(self.request.get('ac-type-2'))
        state = str(self.request.get('state'))
        seer = air_con.ac_dict[ac][0]
        size = air_con.ac_dict[ac][1]
        seer2 = air_con.ac_dict[ac2][0]
        size2 = air_con.ac_dict[ac2][1]
        money = air_con.states_dict[state]
        my_dict = {'name1': ac, 'name2': ac2, 'state': state, 'seer': seer, 'size': size, 'money': money, 'seer2': seer2, 'size2': size2}
        end_template = template_env.get_template('templates/app-results.html')
        self.response.write(end_template.render(my_dict))

app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/region', RegionPage),
    ('/appliances', AppliancePage),
], debug=True)
